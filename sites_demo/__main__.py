"""Offline CLI. The launcher measures a fresh pipeline process, including startup."""
import argparse
import ctypes
from datetime import datetime, timezone
from html.parser import HTMLParser
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
import time
import zipfile

from . import render
from .contracts import (D09_SHA, F1_PATH, F1_SHA, ROOT, SCHEMAS, QUESTION_IDS, SHA_RE, DemoError, artifact,
                        canonical, create_output, local_path, read_json, require, sha, write_new)
from .pipeline import prepare, product_digest, product_inventory, verify_f1


def stamp():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def network_disabled(event, args):
    # gethostname reads the local computer name; it performs no DNS or connection.
    if event.startswith("socket.") and event != "socket.gethostname":
        raise DemoError("NETWORK_DISABLED", event)


def peak_memory():
    if sys.platform != "win32":
        return None
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
            (name, ctypes.c_size_t) for name in ("PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
                                                "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage",
                                                "PagefileUsage", "PeakPagefileUsage")]
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
    psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
    counters = Counters()
    counters.cb = ctypes.sizeof(counters)
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.cb):
        return None
    return counters.PeakWorkingSetSize


def hardware():
    info = {"cpu": platform.processor(), "logical_cpu_count": os.cpu_count(), "physical_ram_bytes": None}
    if sys.platform == "win32":
        from ctypes import wintypes

        class MemoryStatus(ctypes.Structure):
            _fields_ = [("length", wintypes.DWORD), ("load", wintypes.DWORD)] + [
                (name, ctypes.c_ulonglong) for name in ("total_physical", "available_physical", "total_page", "available_page",
                                                       "total_virtual", "available_virtual", "available_extended")]
        status = MemoryStatus()
        status.length = ctypes.sizeof(status)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            info["physical_ram_bytes"] = status.total_physical
        import winreg
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0") as key:
            info["cpu"] = winreg.QueryValueEx(key, "ProcessorNameString")[0].strip()
    return info


def runtime_identity():
    base = Path(sys.base_prefix)
    inventory = []
    for directory in (base / "Lib", base / "DLLs"):
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".py", ".pyd", ".dll", ".zip"} and not {"site-packages", "__pycache__"}.intersection(path.parts):
                inventory.append([path.relative_to(base).as_posix(), sha(path.read_bytes())])
    inventory.sort()
    return {"python": platform.python_version(), "implementation": platform.python_implementation(),
            "platform": platform.platform(), "machine": platform.machine(), "cache_tag": sys.implementation.cache_tag,
            "pointer_bits": 64 if sys.maxsize > 2**32 else 32,
            "root_binaries": {p.name: sha(p.read_bytes()) for p in sorted(base.iterdir()) if p.suffix.lower() in {".exe", ".dll"}},
            "stdlib_native_file_count": len(inventory), "stdlib_native_sha256": sha(canonical(inventory))}


def runtime_profile(reviewer, role, exposure):
    browsers = []
    for base in (os.environ.get("PROGRAMFILES(X86)"), os.environ.get("PROGRAMFILES"), os.environ.get("LOCALAPPDATA")):
        if not base:
            continue
        for relative in ("Microsoft/Edge/Application/msedge.exe", "Google/Chrome/Application/chrome.exe"):
            path = Path(base) / relative
            if path.is_file() and str(path) not in [b["path"] for b in browsers]:
                browsers.append({"path": str(path), "sha256": sha(path.read_bytes()), "status": "INSTALLED_FILE_VERIFIED_NOT_TASK_EXECUTION"})
    return {"schema_version": 1, "identity": runtime_identity(), "hardware": hardware(),
            "reviewer": {"identity": reviewer, "role": role, "prior_exposure": exposure},
            "executable": sys.executable, "base_prefix": sys.base_prefix, "browsers": browsers,
            "browser_task": "NOT_MEASURED", "scope": "Prospective product profile; independent of historical F1 author runtime. OS/system DLLs are not hermetic."}


def verify_evaluation(root, path, expected, actual_runtime=None):
    raw = Path(path).read_bytes()
    require(isinstance(expected, str) and SHA_RE.fullmatch(expected) and sha(raw) == expected,
            "EVALUATION_DIGEST", "evaluation differs from external anchor")
    evaluation = read_json(raw)
    require(type(evaluation["schema_version"]) is int and evaluation["schema_version"] == 1 and evaluation["evaluation_id"].startswith("D09-EVAL-")
            and evaluation["freeze_sha256"] == F1_SHA and evaluation["d09_sha256"] == D09_SHA,
            "EVALUATION_DIGEST", "evaluation contract mismatch")
    require(re.fullmatch(r"[0-9a-f]{40}", evaluation["product_commit"]) is not None
            and evaluation["product_code_sha256"] == product_digest(root), "PRODUCT_DIGEST", "code/commit identity mismatch")
    require(all(type(v) is int for v in evaluation["budget"].values())
            and evaluation["budget"] == {"max_works": 598, "wall_seconds": 60, "peak_process_bytes": 256 * 1024 * 1024, "live_requests": 0},
            "EVALUATION_DIGEST", "budget differs from accepted contract")
    require(evaluation["schemas"] == SCHEMAS and all(type(v) is int for v in evaluation["schemas"].values())
            and evaluation["protocol"]["question_ids"] == QUESTION_IDS
            and evaluation["protocol"]["questions_required"] == 5
            and evaluation["protocol"]["independent_scientific_quality"] == "NOT_MEASURED",
            "EVALUATION_DIGEST", "schema/task/claim boundary differs")
    required_docs = {"evaluation/reviewer-task.md", "evaluation/REPLAY.md", "evaluation/owner-acceptance.json"}
    require(set(evaluation["protocol_artifacts"]) == required_docs, "EVALUATION_DIGEST", "missing prospective instructions/acceptance")
    for name, digest in evaluation["protocol_artifacts"].items():
        require(sha(local_path(root, name).read_bytes()) == digest, "EVALUATION_DIGEST", name)
    runtime_ref = evaluation["runtime_profile"]
    profile_raw = local_path(root, runtime_ref["path"]).read_bytes()
    require(sha(profile_raw) == runtime_ref["sha256"], "RUNTIME_PROFILE", "prospective profile hash mismatch")
    profile = read_json(profile_raw)
    require(profile["reviewer"] == evaluation["reviewer"], "RUNTIME_PROFILE", "reviewer/exposure mismatch")
    require(profile["identity"] == (actual_runtime if actual_runtime is not None else runtime_identity())
            and profile["hardware"] == hardware(), "RUNTIME_PROFILE", "environment differs; freeze a separate prospective profile before running")
    require(profile["identity"]["python"] == "3.14.7" and profile["identity"]["implementation"] == "CPython"
            and profile["identity"]["pointer_bits"] == 64 and sys.platform == "win32", "RUNTIME_PROFILE", "accepted target is Windows CPython 3.14.7 x64")
    return evaluation


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.targets = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        require(tag not in {"script", "iframe", "object", "embed", "base", "form"}, "UNSAFE_HTML", tag)
        require(not any(k.lower().startswith("on") for k in attrs), "UNSAFE_HTML", "event handler")
        for key in ("href", "src"):
            if key in attrs:
                self.targets.append(attrs[key])
        if "id" in attrs:
            self.ids.add(attrs["id"])


def check_navigation(root, names):
    parsed = {}
    links = 0
    for name in names:
        if name.endswith(".html"):
            page = Links()
            page.feed(local_path(root, name).read_text(encoding="utf-8"))
            parsed[name] = page
    for name, page in parsed.items():
        for target in page.targets:
            require(not any(c in target for c in (":", "\\", "%", "?")) and not target.startswith("/"), "UNSAFE_HTML", target)
            path, _, anchor = target.partition("#")
            parts = list(PurePosixPath(name).parent.parts)
            for part in path.split("/") if path else []:
                if part == "..":
                    require(bool(parts), "UNSAFE_HTML", "path escapes output")
                    parts.pop()
                elif part and part != ".":
                    parts.append(part)
            destination = "/".join(parts) if path else name
            require(destination in names, "BROKEN_LINK", f"{name} -> {target}")
            if anchor:
                require(destination in parsed and anchor in parsed[destination].ids, "BROKEN_LINK", target)
            links += 1
    return {"html_pages": len(parsed), "local_links": links, "status": "PASS"}


def verify_index(path):
    path = Path(path).absolute()
    root = path.parent
    index = read_json(path.read_bytes())
    require(type(index["schema_version"]) is int and index["schema_version"] == 1 and index["freeze_sha256"] == F1_SHA
            and re.fullmatch(r"[0-9a-f]{40}", index["product_commit"]) and SHA_RE.fullmatch(index["product_code_sha256"]),
            "MANIFEST_DIGEST", "semantic index contract")
    require(local_path(root, "COMPLETE").is_file(), "INCOMPLETE_RUN", str(root))
    complete = read_json((root / "COMPLETE").read_bytes())
    require(complete["index_sha256"] == sha(path.read_bytes())
            and complete["execution_sha256"] == sha((root / "execution.json").read_bytes()),
            "INCOMPLETE_RUN", "completion marker identity")
    execution = read_json((root / "execution.json").read_bytes())
    require(execution["status"] == "PASS" and execution["semantic_sha256"] == index["semantic_sha256"],
            "INCOMPLETE_RUN", "execution failed or refers to different artifacts")
    require(0 <= execution["elapsed_seconds"] <= 60 and type(execution["peak_process_bytes"]) is int
            and 0 < execution["peak_process_bytes"] <= 256 * 1024 * 1024 and execution["live_requests"] == 0,
            "BUDGET_EXCEEDED", "completed execution violates accepted budget")
    names = [a["path"] for a in index["artifacts"]]
    require(names == sorted(set(names)), "ARTIFACT_DIGEST", "duplicate/unsorted artifact inventory")
    actual_names = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    require(actual_names == set(names) | {path.name, "execution.json", "COMPLETE"}, "ARTIFACT_DIGEST", "artifact set differs")
    for entry in index["artifacts"]:
        require(type(entry["size_bytes"]) is int and entry["size_bytes"] >= 0, "ARTIFACT_DIGEST", "invalid size type")
        require(artifact(entry["path"], local_path(root, entry["path"]).read_bytes()) == entry,
                "ARTIFACT_DIGEST", entry["path"])
    require(sha(canonical([[a["path"], a["sha256"]] for a in index["artifacts"]])) == index["semantic_sha256"],
            "ARTIFACT_DIGEST", "semantic root digest")
    return index


def compare(left, right):
    a, b = verify_index(left), verify_index(right)
    require(a == b, "REPLAY_MISMATCH", "F1/product/schema/artifact set or semantic bytes differ")
    return {"status": "PASS", "semantic_sha256": a["semantic_sha256"], "artifacts": len(a["artifacts"]),
            "execution_records": "Separate, not required byte-identical; reviewer/runtime evidence must be assessed independently"}


def worker(args):
    sys.addaudithook(network_disabled)
    require(not any(args.out.iterdir()), "OUTPUT_EXISTS", "worker requires empty new directory")
    evaluation = verify_evaluation(args.root, args.evaluation, args.expected_evaluation_sha)
    snapshot = prepare(args.root, args.f1, args.expected_f1_sha)
    entries = []
    for name, raw in render.artifacts(snapshot):
        write_new(args.out, name, raw)
        entries.append(artifact(name, raw))
    entries.sort(key=lambda a: a["path"])
    require(len(entries) == len({a["path"] for a in entries}), "ARTIFACT_DIGEST", "duplicate output path")
    navigation = check_navigation(args.out, {a["path"] for a in entries})
    index = {"schema_version": 1, "freeze_sha256": F1_SHA, "product_commit": evaluation["product_commit"],
             "product_code_sha256": evaluation["product_code_sha256"], "artifacts": entries,
             "semantic_sha256": sha(canonical([[a["path"], a["sha256"]] for a in entries]))}
    write_new(args.out, "semantic-index.json", canonical(index))
    write_new(args.out, ".worker-result.json", canonical({"peak_process_bytes": peak_memory(), "navigation": navigation,
                                                        "runtime_profile_sha256": evaluation["runtime_profile"]["sha256"]}))


def build(args):
    # Output is reserved once; failed runs remain visibly incomplete, never overwritten.
    output = create_output(args.out)
    started, start = stamp(), time.perf_counter()
    command = [sys.executable, "-B", "-m", "sites_demo", "_worker", "--root", str(args.root), "--f1", str(args.f1),
               "--expected-f1-sha", args.expected_f1_sha, "--evaluation", str(args.evaluation),
               "--expected-evaluation-sha", args.expected_evaluation_sha, "--out", str(output)]
    result = {"schema_version": 1, "evaluation_sha256": args.expected_evaluation_sha,
              "semantic_sha256": None, "runtime_profile_sha256": None, "started_utc": started,
              "argv": command, "status": "FAIL", "error_codes": [], "peak_process_bytes": None,
              "memory_method": "Windows GetProcessMemoryInfo PeakWorkingSetSize: worker + launcher measured separately; budget uses max, sum also reported",
              "boundary": "Launcher wall clock from before fresh worker interpreter startup through input/runtime checks, all 21 windows/598 evidence pages, link verification and output writes. Browser is separate.",
              "live_requests": 0, "network_guard": "worker audit hook rejects socket creation/connections/DNS; local gethostname allowed"}
    try:
        process = subprocess.run(command, cwd=args.root, capture_output=True, text=True, encoding="utf-8", timeout=60,
                                 env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        if process.returncode:
            try:
                failure = read_json(process.stdout)
            except DemoError:
                failure = {"code": "WORKER_FAILED", "error": process.stdout.strip() + process.stderr.strip()}
            raise DemoError(failure.get("code", "WORKER_FAILED"), failure.get("error", "worker failed"))
        worker_result = read_json((output / ".worker-result.json").read_bytes())
        index = read_json((output / "semantic-index.json").read_bytes())
        (output / ".worker-result.json").unlink()
        result.update(semantic_sha256=index["semantic_sha256"], runtime_profile_sha256=worker_result["runtime_profile_sha256"],
                      navigation=worker_result["navigation"])
        worker_peak, launcher_peak = worker_result["peak_process_bytes"], peak_memory()
        result.update(worker_peak_bytes=worker_peak, launcher_peak_bytes=launcher_peak)
        require(worker_peak is not None and launcher_peak is not None, "MEMORY_NOT_MEASURED", "native process peak unavailable")
        result.update(peak_process_bytes=max(worker_peak, launcher_peak), process_peaks_sum_bytes=worker_peak + launcher_peak)
        require(time.perf_counter() - start <= 60 and result["peak_process_bytes"] <= 256 * 1024 * 1024,
                "BUDGET_EXCEEDED", "replay exceeds accepted wall/process budget")
        result["status"] = "PASS"
    except subprocess.TimeoutExpired:
        result["error_codes"] = ["BUDGET_EXCEEDED"]
    except (DemoError, OSError, ValueError, KeyError) as error:
        result["error_codes"] = [getattr(error, "code", "EXECUTION_ERROR")]
        result["error"] = str(error)
    result.update(ended_utc=stamp(), elapsed_seconds=time.perf_counter() - start)
    if result["elapsed_seconds"] > 60:
        result.update(status="FAIL", error_codes=["BUDGET_EXCEEDED"])
    write_new(output, "execution.json", canonical(result))
    if result["status"] == "PASS":
        write_new(output, "COMPLETE", canonical({"index_sha256": sha((output / "semantic-index.json").read_bytes()),
                                               "execution_sha256": sha((output / "execution.json").read_bytes())}))
    print(canonical(result).decode(), end="")
    return 0 if result["status"] == "PASS" else 1


def package(args):
    """Create one offline ZIP from an allowlist; never archive the working directory."""
    manifest, files = verify_f1(args.root, args.f1, args.expected_f1_sha)
    evaluation = verify_evaluation(args.root, args.evaluation, args.expected_evaluation_sha)
    payloads = dict(files)
    payloads[F1_PATH] = args.f1.read_bytes()
    for entry in product_inventory(args.root):
        payloads[entry["path"]] = local_path(args.root, entry["path"]).read_bytes()
    for path in (args.evaluation, local_path(args.root, evaluation["runtime_profile"]["path"]),
                 *(local_path(args.root, name) for name in evaluation["protocol_artifacts"]),
                 args.root / "evaluation/AS_BUILT.md", args.root / "evaluation/D09-M1-20261012-v1.md"):
        name = path.relative_to(args.root).as_posix()
        payloads[name] = path.read_bytes()
    payloads["evaluation/expected-sha256.json"] = canonical({"evaluation_path": args.evaluation.relative_to(args.root).as_posix(),
                                                           "evaluation_sha256": args.expected_evaluation_sha, "freeze_sha256": F1_SHA})
    package_index = {"schema_version": 1, "artifacts": [artifact(n, r) for n, r in sorted(payloads.items())]}
    payloads["package-index.json"] = canonical(package_index)
    require(not args.out.exists() and not args.out.is_symlink(), "OUTPUT_EXISTS", str(args.out))
    local_path(args.out.parent, args.out.name)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("xb") as stream, zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, raw in sorted(payloads.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 12, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, raw)
    print(canonical({"status": "PASS", "files": len(payloads), "sha256": sha(args.out.read_bytes()),
                     "package_index_sha256": sha(payloads["package-index.json"])}).decode(), end="")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    runtime = commands.add_parser("runtime", help="record a candidate profile before evaluation")
    runtime.add_argument("--reviewer", required=True)
    runtime.add_argument("--role", required=True)
    runtime.add_argument("--exposure", required=True)
    runtime.add_argument("--out", type=Path, required=True)
    comparison = commands.add_parser("compare")
    comparison.add_argument("left", type=Path)
    comparison.add_argument("right", type=Path)
    for command in ("verify", "build", "_worker", "package"):
        sub = commands.add_parser(command)
        sub.add_argument("--root", type=Path, default=ROOT)
        sub.add_argument("--f1", type=Path, required=True)
        sub.add_argument("--expected-f1-sha", required=True)
        sub.add_argument("--evaluation", type=Path, required=True)
        sub.add_argument("--expected-evaluation-sha", required=True)
        if command != "verify":
            sub.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "runtime":
            raw = canonical(runtime_profile(args.reviewer, args.role, args.exposure))
            write_new(args.out.absolute().parent, args.out.name, raw)
            print(canonical({"status": "CANDIDATE", "sha256": sha(raw)}).decode(), end="")
        elif args.command == "compare":
            print(canonical(compare(args.left, args.right)).decode(), end="")
        else:
            args.root, args.f1, args.evaluation = args.root.absolute(), args.f1.absolute(), args.evaluation.absolute()
            if args.command == "build":
                return build(args)
            if args.command == "_worker":
                args.out = args.out.absolute()
                worker(args)
            elif args.command == "package":
                args.out = args.out.absolute()
                package(args)
            else:
                sys.addaudithook(network_disabled)
                verify_evaluation(args.root, args.evaluation, args.expected_evaluation_sha)
                snapshot = prepare(args.root, args.f1, args.expected_f1_sha)
                print(canonical({"status": "PASS", "frozen_artifacts": len(snapshot["files"]),
                                 "works": len(snapshot["works"]), "windows": len(snapshot["windows"]),
                                 "monthly": [[p["n"], p["N"]] for p in snapshot["points"]]}).decode(), end="")
    except (DemoError, OSError, ValueError, KeyError, TypeError) as error:
        print(canonical({"status": "FAIL", "code": getattr(error, "code", "INVALID_INPUT"), "error": str(error)}).decode(), end="")
        return 2 if isinstance(error, DemoError) and error.code == "OUTPUT_EXISTS" else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
