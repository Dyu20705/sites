"""Characterize an unsupported-input boundary without changing frozen evaluator bytes."""
import argparse
import json
from pathlib import Path
import sys
import tempfile

BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE))
from offline_audit import audit
from signal_evaluator import evaluate, synthetic_record

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
record = synthetic_record(0, "Fuzzing")
del record["categories_current"]
result = evaluate([record])
assert result["months"][0]["eligible_works"] == 0
assert result["excluded"][0]["reasons"] == ["outside_current_query_category"]
scratch = BASE / "__pycache__/audit-temp"
scratch.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=scratch) as directory:
    path = Path(directory)
    (path / "acquisition.json").write_text(json.dumps({"status": "ACCESS_OR_RESPONSE_FAILURE"}))
    try:
        audit(path)
    except ValueError as error:
        partial_rejection = str(error)
    else:
        raise AssertionError("Partial acquisition was accepted")
report = {"status": "LIMITATION_CONFIRMED", "fixture": record,
          "observed_january": result["months"][0], "excluded": result["excluded"],
          "partial_acquisition_rejected": partial_rejection,
          "finding": "Standalone helper maps unknown current membership to exclusion/empty bin; not a general fail-closed input interface.",
          "impact": "No effect on fixed hash-pinned 598 works: all current membership fields valid and cs.SE. Do not reuse helper on new inputs under the proposed unknown-field guarantee.",
          "disposition": "Preserve frozen implementation; require a separately versioned guard/correction and regression before any broader input contract. No estimand or owner acceptance changed."}
with args.output.open("x", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
