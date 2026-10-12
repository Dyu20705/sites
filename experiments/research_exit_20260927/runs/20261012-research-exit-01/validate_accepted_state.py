"""Read-only checks for the accepted research state; old validators stay historical."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, default=HERE / "accepted-state-validation.json")
OUT = parser.parse_args().output.absolute()
checks = []


def check(name, condition, detail):
    checks.append({"check": name, "status": "PASS" if condition else "FAIL", "detail": detail})


def read(path):
    return json.loads(path.read_bytes())


manifest = read(HERE / "freeze-v1.json")
expected = "bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a"
check("manifest_external_anchor", hashlib.sha256((HERE / "freeze-v1.json").read_bytes()).hexdigest() == expected, expected)
changed = [name for name, spec in manifest["files"].items()
           if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != spec["sha256"]]
check("all_122_frozen_artifacts_still_exact", not changed and len(manifest["files"]) == 122, changed)
execution = read(HERE / "execution.json")
check("new_verification_commands", execution["status"] == "PASS" and len(execution["commands"]) == 4
      and all(row["exit_code"] == 0 for row in execution["commands"]), "freeze, 56 tests, independent-method raw recount, clean artifact tree")
for row in execution["commands"]:
    check("execution_output_" + row["name"], hashlib.sha256((HERE / row["output"]).read_bytes()).hexdigest() == row["output_sha256"], row["output"])
baseline = read(HERE / "baseline-regressions.json")
check("historical_regression_replay", baseline["status"] == "PASS" and len(baseline["byte_comparisons"]) == 13
      and all(c["exit_code"] == c["expected_exit_code"] for c in baseline["commands"]), "13 commands, 13 byte comparisons, pre-reconciliation state; overwrite refusal exit 2 is expected")
independent = read(HERE / "independent-verification.json")
check("corpus_metrics_lineage", independent["status"] == "PASS"
      and independent["monthly_n"] == [0, 1, 2, 1, 4, 1]
      and independent["monthly_N"] == [91, 79, 97, 103, 122, 106]
      and independent["denominator_lineage_records"] == 598 and independent["numerator_lineage_records"] == 9,
      "14 raw inputs, 598 denominator refs, 9 numerator refs, 18 lexical boundaries, 5 variants and bimonthly ratios checked")
simulation = read(ROOT / manifest["artifact_roles"]["simulation"])
check("simulation_scope", simulation["real_corpus_works_annotated"] == 0
      and simulation["work_count"] == 27 and simulation["raw_judgment_count"] == 54,
      "Fictional SYN workflow; real pilot stays null; no scientific-quality claim")
for lang in ("english", "vietnamese"):
    base = ROOT / "docs" / lang
    log = (base / "master/07_DECISION_LOG.md").read_text(encoding="utf-8")
    states = {}
    for n in range(5, 10):
        section = re.search(r"## \d+\. D0" + str(n) + r"\b[\s\S]*?(?=\n## |\Z)", log).group()
        states[f"D0{n}"] = re.search(r"\*\*(?:Status|Trạng thái):\*\* (\w+)", section).group(1)
    check(lang + "_decision_states", states == {"D05": "ACCEPTED", "D06": "ACCEPTED", "D07": "ACCEPTED", "D08": "ACCEPTED", "D09": "PROPOSED"}, states)
    check(lang + "_owner_authority", "6119490874" in log and "M1-R-20261010-v1" in log and expected in log, "Exact external owner record + F1 anchor")
    for relative in ("baseline/M1.md", "master/06_EVALUATION_PROTOCOL.md", "master/08_MONTH1_BACKLOG.md", "master/09_CURRENT_STATE.md"):
        text = (base / relative).read_text(encoding="utf-8").split("## ", 1)[0]
        check(lang + "/" + relative, "RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY" in text
              and "NOT PASSED" in text and "NOT MEASURED" in text and "PROPOSED" in text and "6119490874" in text,
              "Current accepted narrow gate precedes explicitly historical text; D09/product/scientific claims remain separate")
broken = []
links = 0
for path in (ROOT / "docs").rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0]).strip("<>")
        if not target:
            continue
        links += 1
        destination = (path.parent / target).resolve()
        if not destination.exists() and destination != OUT:
            broken.append({"document": str(path.relative_to(ROOT)), "target": target})
check("documentation_local_links", not broken, {"checked": links, "broken": broken})
modified = subprocess.check_output(["git", "diff", "--diff-filter=MDR", "--name-only", "97bf499718c13166667a8e5da09b201065d9e117"], cwd=ROOT, text=True).splitlines()
check("no_old_experiment_edits", not any(name.startswith("experiments/") for name in modified), modified)
check("holdout_and_product_boundary", manifest["holdout"]["authorized"] is False
      and manifest["criteria"]["D09"] == "PROPOSED" and manifest["criteria"]["original_E3"] == "NOT_PASSED",
      "Verification code inspected: local files/subprocesses only, no acquire.py execution; no sites_demo or #72/#73 implementation created. Independent demo remains 0/7.")
result = {"status": "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL",
          "utc": datetime.now(timezone.utc).isoformat(), "checks": checks,
          "research_gate": "RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY",
          "authority": "https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874",
          "contract": "M1-R-20261010-v1", "manifest_sha256": expected,
          "limits": "No historical E3 pass, independent scientific quality, human validation, product demo, measured E8, new acquisition or holdout access"}
if result["status"] != "PASS":
    result["research_gate"] = "NOT_PASSED"
with OUT.open("x", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
print(json.dumps({"status": result["status"], "checks": len(checks), "failures": [c for c in checks if c["status"] == "FAIL"]}))
raise SystemExit(0 if result["status"] == "PASS" else 1)
