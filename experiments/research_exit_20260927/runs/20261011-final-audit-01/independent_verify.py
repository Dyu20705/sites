"""Raw Atom/token-set recount; stdlib only, no SITES evaluator/parser imports."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "experiments/research_exit_20260927"
DATA = BASE / "runs/20261010-development-01"
SIGNAL = BASE / "runs/20261010-signal-01"
NS = {"a": "http://www.w3.org/2005/Atom"}
MONTHS = [f"2019-{n:02}" for n in range(1, 7)]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def tokens(title):
    # Python Unicode word characters, independently scanning boundaries.
    word = ""
    for char in title + " ":
        if char.isalnum() or char == "_":
            word += char
        elif word:
            # Unicode IGNORECASE special equivalents relevant to this vocabulary.
            yield word.replace("İ", "i").replace("ı", "i").replace("ſ", "s").lower()
            word = ""


def matched(title, exact=False):
    allowed = {"fuzzing"} if exact else {"fuzz", "fuzzing", "fuzzer", "fuzzers"}
    return any(token in allowed for token in tokens(title))


def verify():
    declaration = read(SIGNAL / "declaration-corrected.json")
    config = read(DATA / "inputs/preregistration.json")
    pattern = declaration["execution_pattern"]
    assert pattern == config["candidate_title_pattern"] == r"\bfuzz(?:ing|er|ers)?\b"
    assert declaration["regex_flags"] == "IGNORECASE"
    cases = {"Fuzz": True, "FUZZING": True, "fuzzer": True, "fuzzers": True,
             "fuzzing-based": True, "(fuzzing)": True, "fuzzy": False,
             "defuzzing": False, "fuzzing2": False, "fuzzing_name": False,
             "éfuzzing": False, "fuzzingé": False, "AFL software testing": False,
             "fuZZİNG": True, "fuzzıng": True, "fuzzerſ": True,
             "fuzzing\nfuzzers": True, "": False}
    for title, expected in cases.items():
        assert matched(title) == expected == bool(re.search(pattern, title, re.I)), title
    assert re.search(r"\\bfuzz(?:ing|er|ers)?\\b", "Fuzzing", re.I) is None
    inputs = {}
    for relative, expected in declaration["frozen_inputs"].items():
        path = DATA / relative
        raw = path.read_bytes()
        committed = subprocess.check_output(["git", "show", "HEAD:" + path.relative_to(ROOT).as_posix()], cwd=ROOT)
        assert raw == committed and sha(raw) == expected, relative
        inputs[relative] = expected
    groups = {"v1": {}, "current": {}}
    manifest = read(DATA / "acquisition.json")
    assert manifest["reported_total"] == 598
    for request in manifest["requests"]:
        raw = (DATA / request["file"]).read_bytes()
        assert sha(raw) == request["sha256"] and len(raw) == request["bytes"]
        name = Path(request["file"]).name
        kind = "v1" if name.startswith("v1-") else "current" if name.startswith("current-") else None
        if kind is None:
            continue
        for index, entry in enumerate(ET.fromstring(raw).findall("a:entry", NS)):
            entry_id = entry.findtext("a:id", namespaces=NS)
            version_id = entry_id.split("/abs/")[1]
            work, version = version_id.rsplit("v", 1)
            assert work not in groups[kind] and int(version) >= 1
            if kind == "v1":
                assert version == "1"
            event = entry.findtext("a:published", namespaces=NS)
            month = datetime.fromisoformat(event.replace("Z", "+00:00")).astimezone(timezone.utc).strftime("%Y-%m")
            assert month in MONTHS
            groups[kind][work] = {"version_id": version_id, "event": event, "month": month,
                "title": " ".join(entry.findtext("a:title", namespaces=NS).split()),
                "categories": sorted(n.get("term") for n in entry.findall("a:category", NS)),
                "ref": {"file": request["file"], "entry_index": index, "entry_id": entry_id, "sha256": request["sha256"]}}
    first, current = groups["v1"], groups["current"]
    normalized = read(DATA / "replay-1/normalized-records.json")
    assert len(first) == len(current) == len(normalized) == 598
    assert set(first) == set(current) == {r["work_id"] for r in normalized}
    for r in normalized:
        w = r["work_id"]
        assert r["version_id"] == first[w]["version_id"]
        assert r["published_at"] == first[w]["event"] == current[w]["event"]
        assert r["available_at"] is None and r["retrospective_exclusions"] == []
        assert set(r["field_status"].values()) == {"valid"}
        for kind in groups:
            assert r["source_ref"][kind] == groups[kind][w]["ref"]
            assert r["title_" + kind] == groups[kind][w]["title"]
            assert r["categories_" + kind] == groups[kind][w]["categories"]
        assert "cs.SE" in current[w]["categories"]
    report = read(SIGNAL / "corrected-replay-1/measurements.json")
    totals = Counter(v["month"] for v in first.values())
    counts = Counter(v["month"] for v in first.values() if matched(v["title"]))
    assert [totals[m] for m in MONTHS] == [91, 79, 97, 103, 122, 106]
    assert [counts[m] for m in MONTHS] == [0, 1, 2, 1, 4, 1]
    for row in report["result"]["months"]:
        m = row["month"]
        ids = sorted(w for w, v in first.items() if v["month"] == m)
        hits = [w for w in ids if matched(first[w]["title"])]
        assert row["denominator_ids"] == ids and row["matched_ids"] == hits
        assert (row["count"], row["eligible_works"], row["share"]) == (len(hits), len(ids), len(hits) / len(ids))
    for hit in report["result"]["matches"]:
        assert hit["source_ref"] == first[hit["work_id"]]["ref"]
    for name, variant in report["sensitivity"].items():
        population = {w: v for w, v in first.items()
                      if not (name.startswith("exclude_nine") and w[:4] > "1906")
                      and not (name == "v1_category_subset" and "cs.SE" not in v["categories"])}
        source = current if name == "current_title_diagnostic" else first
        hit_ids = {w for w in population if matched(source[w]["title"], name == "exact_fuzzing")}
        assert hit_ids == set(variant["matched_ids"])
        for row in variant["months"]:
            ids = {w for w, v in population.items() if v["month"] == row["month"]}
            assert (row["count"], row["eligible_works"], row["share"]) == (len(ids & hit_ids), len(ids), len(ids & hit_ids) / len(ids))
    for row in report["adjacent_bimonth"]:
        n, total = sum(counts[m] for m in row["months"]), sum(totals[m] for m in row["months"])
        assert (row["count"], row["eligible_works"], row["share"]) == (n, total, n / total)
    late = sorted(w for w in first if w[:4] > "1906")
    assert late == sorted(r["work_id"] for r in read(DATA / "crosscheck.json")["late_id_month_records"])
    assert len(late) == 9
    pilot = read(SIGNAL / "reference-pilot-plan.json")
    selected = {w for w, v in first.items() if matched(v["title"])}
    for m in MONTHS:
        candidates = [w for w, v in first.items() if v["month"] == m and not matched(v["title"])]
        selected.update(sorted(candidates, key=lambda w: sha((pilot["seed"] + ":" + w).encode()))[:3])
    assert selected == {r["work_id"] for r in pilot["records"]} and len(selected) == 27
    assert all(r["annotator_a"] is r["annotator_b"] is r["adjudication"] is None for r in pilot["records"])
    assert report["reference_quality"] == "NOT_MEASURED" and report["labels"] is None
    assert all(report["as_of"][key] is None for key in ("count", "denominator", "share"))
    return {"status": "PASS", "method": "Direct Atom parse plus Unicode token-set membership; no project imports",
        "scope": "Independent calculation method on same host; not independent reviewer/scientific validation",
        "monthly_N": [totals[m] for m in MONTHS], "monthly_n": [counts[m] for m in MONTHS],
        "frozen_inputs_and_git_bytes": inputs, "denominator_lineage_records": 598, "numerator_lineage_records": 9,
        "lexical_boundary_cases": len(cases), "sensitivity_variants_verified": len(report["sensitivity"]),
        "late_ids": late, "pilot_selection_reproduced": 27, "real_annotations": 0,
        "normalized_sha256": sha((DATA / "replay-1/normalized-records.json").read_bytes()),
        "measurement_sha256": sha((SIGNAL / "corrected-replay-1/measurements.json").read_bytes()),
        "script_sha256": sha(Path(__file__).read_bytes())}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify()
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, indent=2))
