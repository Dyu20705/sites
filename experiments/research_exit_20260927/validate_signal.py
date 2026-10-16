"""Read-only checks of signal provenance, raw XML arithmetic and paired documents."""
import argparse
import ast
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

from offline_audit import checked_bytes, digest
from signal_evaluator import MONTHS, write_json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def validate(run, output):
    declaration = json.loads((run / "declaration-corrected.json").read_text())
    frozen = ROOT / declaration["frozen_run"]
    for name, expected in declaration["frozen_inputs"].items():
        checked_bytes(frozen / name, expected)
    assert (HERE / "preregistration.json").read_bytes() == (frozen / "inputs/preregistration.json").read_bytes()
    outputs = {}
    for name in ("measurements.json", "controlled-checks.json"):
        one = (run / "corrected-replay-1" / name).read_bytes()
        two = (run / "corrected-replay-2" / name).read_bytes()
        assert one == two, "Nondeterministic semantic output"
        outputs[name] = digest(one)
    report = json.loads((run / "corrected-replay-1/measurements.json").read_text())
    for replay in ("corrected-replay-1", "corrected-replay-2"):
        execution = json.loads((run / replay / "execution.json").read_text())
        assert execution["declaration_sha256"] == digest((run / "declaration-corrected.json").read_bytes())
        assert execution["outputs_sha256"] == outputs
        for name, expected in execution["code_sha256"].items():
            checked_bytes(HERE / name, expected)
    # A distinct direct-XML arithmetic implementation, not an evaluator rerun.
    ns = {"a": "http://www.w3.org/2005/Atom"}
    totals, counts, match_refs, raw_ids = Counter(), Counter(), {}, set()
    manifest = json.loads((frozen / "acquisition.json").read_text())
    for request in manifest["requests"]:
        if not Path(request["file"]).name.startswith("v1-"):
            continue
        raw = checked_bytes(frozen / request["file"], request["sha256"])
        for index, entry in enumerate(ET.fromstring(raw).findall("a:entry", ns)):
            entry_id = entry.findtext("a:id", namespaces=ns)
            work = entry_id.split("/abs/")[1].removesuffix("v1")
            assert work not in raw_ids
            raw_ids.add(work)
            title = " ".join(entry.findtext("a:title", namespaces=ns).split())
            event = datetime.fromisoformat(entry.findtext("a:published", namespaces=ns).replace("Z", "+00:00")).astimezone(timezone.utc)
            month = event.strftime("%Y-%m")
            assert month in MONTHS
            totals[month] += 1
            if re.search(declaration["execution_pattern"], title, re.IGNORECASE):
                counts[month] += 1
                match_refs[work] = {"file": request["file"], "entry_index": index, "entry_id": entry_id, "sha256": request["sha256"]}
    assert totals.total() == 598
    assert {row["work_id"] for row in report["result"]["matches"]} == set(match_refs)
    for match in report["result"]["matches"]:
        assert match["source_ref"] == match_refs[match["work_id"]]
    denominator_ids = []
    for row in report["result"]["months"]:
        assert (row["count"], row["eligible_works"]) == (counts[row["month"]], totals[row["month"]])
        assert row["share"] == counts[row["month"]] / totals[row["month"]]
        assert row["title_missing"] == row["title_invalid"] == 0
        denominator_ids.extend(row["denominator_ids"])
    assert len(set(denominator_ids)) == len(denominator_ids) == 598
    assert set(denominator_ids) == raw_ids
    assert report["as_of"]["denominator"] is None and report["labels"] is None
    # Compare first and corrected runs ignoring corrected provenance text only.
    initial = json.loads((run / "replay-1/measurements.json").read_text())
    assert initial["result"] == report["result"] and initial["sensitivity"] == report["sensitivity"]
    assert all(row["count"] == literal["count"] for row, literal in zip(report["result"]["months"], report["sensitivity"]["archived_literal_transport_diagnostic"]["months"]))
    broken, links = [], 0
    files = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines()
    for name in sorted(set(files)):
        path = ROOT / name
        if name.endswith(".md"):
            for destination in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8-sig")):
                target = destination.strip("<>").split("#", 1)[0]
                if not target or re.match(r"[a-z]+:", target) or target.startswith("/"):
                    continue
                links += 1
                resolved = (path.parent / unquote(target)).resolve()
                if not resolved.exists() and resolved != output.resolve():
                    broken.append({"file": name, "target": target})
        elif name.endswith(".json") and name.startswith("experiments/research_exit_20260927/"):
            json.loads(path.read_text(encoding="utf-8"))
        elif name.endswith(".py") and name.startswith("experiments/research_exit_20260927/"):
            ast.parse(path.read_text(encoding="utf-8"))
    assert not broken, broken
    statuses = {}
    paired = [(ROOT / "docs" / lang / "research/14_D08_DEVELOPMENT_EVALUATION_20261010.md").read_text(encoding="utf-8")
              for lang in ("english", "vietnamese")]
    assert re.findall(r"^\| 2019-.*$", paired[0], re.M) == re.findall(r"^\| 2019-.*$", paired[1], re.M)
    pilot = json.loads((run / "reference-pilot-plan.json").read_text())
    assert len(pilot["records"]) == len({row["work_id"] for row in pilot["records"]}) == 27
    assert all(row["annotator_a"] is row["annotator_b"] is row["adjudication"] is None for row in pilot["records"])
    for lang in ("english", "vietnamese"):
        decision = (ROOT / "docs" / lang / "master/07_DECISION_LOG.md").read_text(encoding="utf-8")
        for n in range(5, 10):
            section = re.search(rf"^## \d+\. D0{n} .*?(?=^## |\Z)", decision, re.M | re.S).group()
            status = re.search(r"\*\*(?:Status|Trạng thái):\*\* (\w+)", section).group(1)
            assert status == ("ACCEPTED" if n < 7 else "PROPOSED")
            statuses[f"{lang}/D0{n}"] = status
    return {"status": "PASS", "frozen_inputs_verified": len(declaration["frozen_inputs"]),
            "output_sha256": outputs, "replay_equal": True, "raw_xml_records_checked": totals.total(),
            "match_lineage_checked": len(match_refs), "distinct_denominator_ids_checked": 598,
            "correction_changed_measurements": False, "config_literal_equals_executed_rule": True,
            "relative_links_checked": links, "broken_links": broken, "decision_statuses": statuses,
            "paired_monthly_tables_equal": True, "reference_pilot_status": "PROPOSED_NOT_ANNOTATED",
            "validator_code_sha256": digest(Path(__file__).read_bytes()),
            "scope": "Automated same-host agent verification; no independent scientific/human validation; external URLs/anchors and bilingual meaning require separate review."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = validate(args.run, args.output)
    write_json(args.output, result)
    print(json.dumps(result, indent=2))
