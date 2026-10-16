"""Fresh same-host F1 verification; never writes frozen evidence or uses a provider."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
BASE = Path("experiments/research_exit_20260927")
HERE = Path(__file__).resolve().parent
manifest = HERE / "freeze-v1.json"
digest = hashlib.sha256(manifest.read_bytes()).hexdigest()
anchor = (HERE / "freeze-v1.sha256").read_text().split()[0]
if digest != anchor:
    raise ValueError("External receipt mismatch")
scratch = ROOT / BASE / "__pycache__/exit-temp"
scratch.mkdir(parents=True, exist_ok=True)
os.environ["TEMP"] = os.environ["TMP"] = str(scratch)
tempfile.tempdir = str(scratch)
commands = []
start = datetime.now(timezone.utc).isoformat()


def run(name, args, cwd=ROOT, parse=True):
    result = subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)
    row = {"name": name, "argv": [sys.executable, *map(str, args)], "cwd": str(cwd),
           "exit_code": result.returncode, "stderr": result.stderr}
    commands.append(row)
    output = json.loads(result.stdout) if parse and result.stdout else {"stdout": result.stdout}
    with (HERE / (name + ".json")).open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(output, indent=2, sort_keys=True) + "\n")
    row["output"] = name + ".json"
    row["output_sha256"] = hashlib.sha256((HERE / row["output"]).read_bytes()).hexdigest()
    return result.returncode == 0


ok = run("freeze-verification", [ROOT / BASE / "verify_freeze.py", "--manifest", manifest,
         "--expected-sha256", anchor, "--root", ROOT, "--repo", ROOT])
ok = run("regressions", ["-m", "unittest", "discover", "-s", BASE, "-p", "test_*.py", "-v"], parse=False) and ok
independent_path = scratch / ("raw-recount-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + ".json")
ok = run("independent-verification", [BASE / "runs/20261011-final-audit-01/independent_verify.py", "--output", independent_path]) and ok
with tempfile.TemporaryDirectory(prefix="clean-artifact-tree-", dir=scratch) as directory:
    clean = Path(directory)
    m = json.loads(manifest.read_bytes())
    for relative in m["files"]:
        destination = clean / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    copied_manifest = clean / "freeze-v1.json"
    shutil.copyfile(manifest, copied_manifest)
    ok = run("clean-freeze-verification", [clean / BASE / "verify_freeze.py", "--manifest", copied_manifest,
             "--expected-sha256", anchor, "--root", clean, "--repo", ROOT], cwd=clean) and ok
report = {"status": "PASS" if ok else "FAIL", "started_utc": start,
          "ended_utc": datetime.now(timezone.utc).isoformat(), "manifest_sha256": digest,
          "commands": commands, "clean_run": "New artifact directory and separate process, same author machine/runtime. Source Git objects read from original repository. Not independent reviewer/product replay.",
          "network": "No acquisition/provider calls in these commands; no new July-December files accessed",
          "frozen_inputs": "All manifest entries verified against exact bytes; research_source entries also against pinned Git commit"}
with (HERE / "execution.json").open("x", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": report["status"], "commands": len(commands), "report": str(HERE / "execution.json")}))
raise SystemExit(0 if ok else 1)
