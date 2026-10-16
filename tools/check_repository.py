"""Repository publication guard and immutable F1 manifest verifier (stdlib only).

This check intentionally does not guess a document's language or claim scientific
validity. CI and independent human review enforce different obligations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
F1 = ROOT / "experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json"
EXPECTED_F1_SHA = "bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a"
REQUIRED = (
    "README.md",
    "AGENTS.md",
    ".github/pull_request_template.md",
    ".github/workflows/quality.yml",
    ".agents/README.md",
    "docs/english/README.md",
    "docs/english/governance/REPOSITORY_POLICY.md",
)
LINK_SOURCES = ("README.md", "docs/README.md", "docs/english/README.md")
BANNED_PARTS = {".venv", "__pycache__", ".pytest_cache", "node_modules", ".tox"}
BANNED_NAMES = {".env", ".env.local", "id_rsa", "id_ed25519"}
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        check=True, capture_output=True,
    )
    return [Path(path.decode("utf-8")) for path in result.stdout.split(b"\0") if path]


def check_paths(errors: list[str]) -> None:
    for path in REQUIRED:
        if not (ROOT / path).is_file():
            fail(f"missing required file: {path}", errors)
    for path in tracked_files():
        parts = set(path.parts)
        if parts & BANNED_PARTS or path.name in BANNED_NAMES or path.suffix in {".pyc", ".pyo"}:
            fail(f"forbidden tracked output/secret-like file: {path}", errors)
    for entry in LINK_SOURCES:
        source = ROOT / entry
        if not source.exists():
            continue
        text = source.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split()[0].strip("<>").split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("https:", "http:", "mailto:", "data:")):
                continue
            relative = unquote(target)
            destination = (source.parent / relative).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                fail(f"broken local link: {entry} -> {raw}", errors)


def check_f1(errors: list[str]) -> None:
    if not F1.exists():
        print("F1: ABSENT (baseline without merged research evidence)")
        return
    raw = F1.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_F1_SHA:
        fail(f"F1 manifest digest mismatch: {actual}", errors)
        return
    try:
        value = json.loads(raw)
        artifacts = value["files"]
        if not isinstance(artifacts, dict) or len(artifacts) != 122:
            raise ValueError("expected exactly 122 artifact entries")
        for relative, record in artifacts.items():
            path = (ROOT / relative).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                fail(f"F1 missing/escaping artifact: {relative}", errors)
                continue
            content = path.read_bytes()
            digest = hashlib.sha256(content).hexdigest()
            if digest != record["sha256"]:
                fail(f"F1 hash mismatch: {relative}", errors)
            if "size_bytes" in record and len(content) != record["size_bytes"]:
                fail(f"F1 size mismatch: {relative}", errors)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        fail(f"F1 invalid structure: {exc}", errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--freeze-only", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    if not args.freeze_only:
        check_paths(errors)
    check_f1(errors)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"repository-policy: {'FAIL' if errors else 'PASS'} ({len(errors)} error(s))")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
