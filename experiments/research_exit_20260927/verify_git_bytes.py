"""Read-only SHA-256 verification of explicit Git blobs and optional artifact files."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess


def git(repo, *arguments):
    return subprocess.check_output(["git", "-C", str(repo), *arguments], stderr=subprocess.PIPE)


def scoped_path(value):
    path = PurePosixPath(value)
    if (not value or path.is_absolute() or ".." in path.parts
            or path.as_posix() != value or any(c in value for c in "\\:\x00")):
        raise ValueError(f"Expected a literal repository-relative file path: {value!r}")
    return value


def verify(repo, revision, paths, compare_root=None, allow_doc_eol=()):
    paths = sorted({scoped_path(path) for path in paths})
    allowed = {scoped_path(path) for path in allow_doc_eol}
    if not paths:
        raise ValueError("An explicit nonempty file scope is required")
    if any(path not in paths or not path.startswith("docs/") or not path.endswith(".md")
           for path in allowed):
        raise ValueError("EOL exceptions must name scoped Markdown files under docs/; experiment files require exact bytes")
    if allowed and compare_root is None:
        raise ValueError("EOL exceptions require --compare-root")
    commit = git(repo, "rev-parse", "--verify", "--end-of-options", revision + "^{commit}").decode().strip()
    root = Path(compare_root).resolve() if compare_root is not None else None
    rows = []
    for path in paths:
        row = {"path": path}
        rows.append(row)
        try:
            committed = git(repo, "cat-file", "blob", f"{commit}:{path}")
        except subprocess.CalledProcessError:
            row["state"] = "missing_git_blob"
            continue
        row["committed_sha256"] = hashlib.sha256(committed).hexdigest()
        row["state"] = "hashed"
        if root is None:
            continue
        actual_path = root / path
        if not actual_path.resolve().is_relative_to(root):
            row["state"] = "outside_compare_root"
            continue
        try:
            actual = actual_path.read_bytes()
        except FileNotFoundError:
            row["state"] = "missing_artifact"
            continue
        except OSError:
            row["state"] = "unreadable_artifact"
            continue
        row["artifact_sha256"] = hashlib.sha256(actual).hexdigest()
        if actual == committed:
            row["state"] = "exact"
        elif path in allowed and actual.replace(b"\r\n", b"\n") == committed.replace(b"\r\n", b"\n"):
            row["state"] = "documentation_eol_only"
        else:
            row["state"] = "byte_mismatch"
    mismatches = [row["path"] for row in rows
                  if row["state"] not in {"hashed", "exact", "documentation_eol_only"}]
    return {"status": "FAIL" if mismatches else "PASS", "revision": commit,
            "comparison": "artifact_bytes" if root is not None else "git_blobs_only",
            "allowed_documentation_eol": sorted(allowed), "mismatched_paths": mismatches, "files": rows}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Git repository (default: cwd)")
    parser.add_argument("--revision", required=True)
    parser.add_argument("--path", action="append", required=True, help="Literal repo-relative file; repeat for scope")
    parser.add_argument("--compare-root", type=Path, help="Also compare files below this directory")
    parser.add_argument("--allow-doc-eol", action="append", default=[], help="Named docs/*.md file permitting CRLF/LF only")
    args = parser.parse_args(argv)
    try:
        report = verify(args.repo, args.revision, args.path, args.compare_root, args.allow_doc_eol)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(2, f"Verification setup failed: {error}\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
