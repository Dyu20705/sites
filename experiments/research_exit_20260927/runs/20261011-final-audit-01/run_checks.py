"""Reproduce this bounded audit in fresh ignored directories; preserve command evidence."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
BASE = Path("experiments/research_exit_20260927")
HERE = Path(__file__).resolve().parent
scratch = ROOT / BASE / "__pycache__/audit-temp"
scratch.mkdir(parents=True, exist_ok=True)
os.environ["TMP"] = os.environ["TEMP"] = str(scratch)
tempfile.tempdir = str(scratch)
output = Path(tempfile.mkdtemp(prefix="verification-", dir=scratch))
commands = []
started = datetime.now(timezone.utc).isoformat()


def run(arguments, expected=0):
    result = subprocess.run([sys.executable, *map(str, arguments)], cwd=ROOT, capture_output=True, text=True)
    commands.append({"argv": [sys.executable, *map(str, arguments)], "exit_code": result.returncode,
                     "expected_exit_code": expected, "stdout": result.stdout, "stderr": result.stderr})
    assert result.returncode == expected, commands[-1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


run(["-m", "unittest", "discover", "-s", BASE, "-p", "test_*.py", "-v"])
data = BASE / "runs/20261010-development-01"
signal = BASE / "runs/20261010-signal-01"
for n in (1, 2):
    run([BASE / "checks.py", "--output", output / f"legacy-{n}.json"])
    run([BASE / "offline_audit.py", "--run", data, "--output", output / f"audit-{n}"])
    run([BASE / "signal_evaluator.py", "--declaration", signal / "declaration-corrected.json", "--output", output / f"signal-{n}"])
    run([BASE / "simulate_reference_workflow.py", "--output", output / f"workflow-{n}.json"])
run([BASE / "crosscheck.py", "--run", data, "--output", output / "crosscheck.json"])
run([BASE / "validate_signal.py", "--run", signal, "--output", output / "signal-validation.json"])
run([BASE / "validate.py", "--output", output / "package-validation.json"])
run([BASE / "validate.py", "--output", output / "package-validation.json"], expected=2)
comparisons = {}
for relative, expected in {
    "legacy-1.json": BASE / "results/run-1.json", "legacy-2.json": BASE / "results/run-2.json",
    "audit-1/audit.json": data / "replay-1/audit.json", "audit-2/audit.json": data / "replay-2/audit.json",
    "audit-1/normalized-records.json": data / "replay-1/normalized-records.json",
    "audit-2/normalized-records.json": data / "replay-2/normalized-records.json",
    "signal-1/measurements.json": signal / "corrected-replay-1/measurements.json",
    "signal-2/measurements.json": signal / "corrected-replay-2/measurements.json",
    "signal-1/controlled-checks.json": signal / "corrected-replay-1/controlled-checks.json",
    "signal-2/controlled-checks.json": signal / "corrected-replay-2/controlled-checks.json",
    "workflow-1.json": BASE / "runs/20261010-amendment-01/simulated-workflow.json",
    "workflow-2.json": BASE / "runs/20261010-amendment-01/simulated-workflow.json",
    "crosscheck.json": data / "crosscheck.json"
}.items():
    assert (output / relative).read_bytes() == (ROOT / expected).read_bytes(), relative
    comparisons[relative] = {"equals_frozen": str(expected).replace("\\", "/"), "sha256": digest(output / relative)}
report = {"status": "PASS", "started_utc": started, "ended_utc": datetime.now(timezone.utc).isoformat(),
          "python": platform.python_version(), "platform": platform.platform(), "executable": sys.executable,
          "head_before": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
          "temporary_directory": str(output), "TEMP_and_TMP": str(scratch),
          "commands": commands, "byte_comparisons": comparisons,
          "scope": "Same-host separate processes; no network, holdout, independent human validation or product benchmark"}
with (output / "execution.json").open("x", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": "PASS", "command_count": len(commands), "comparisons": len(comparisons),
                  "report": str(output / "execution.json")}))
