"""Development-only retrospective count/share evaluator. No network operations."""
import argparse
import json
import platform
import re
from datetime import datetime, timezone
from pathlib import Path

import acquire
import checks
import offline_audit
from checks import share
from offline_audit import audit, checked_bytes, date_status, digest

MONTHS = tuple(f"2019-{month:02d}" for month in range(1, 7))
START = datetime(2019, 1, 1, tzinfo=timezone.utc)
END = datetime(2019, 6, 30, 23, 59, 59, tzinfo=timezone.utc)
PATTERN = checks.PATTERN


def evaluate(records, pattern=PATTERN, title_field="title_v1", require_v1_category=False,
             exclude_late_ids=False):
    """N includes eligible nonmatches and unknown titles; unknown titles make n/p null."""
    regex = re.compile(pattern, re.IGNORECASE)
    unique, excluded, unassigned = {}, [], []
    duplicates = revisions = 0
    for record in records:
        work = record.get("work_id")
        if not isinstance(work, str) or not re.fullmatch(r"\d{4}\.\d{4,5}", work):
            raise ValueError("Invalid work identity")
        version = record.get("version_id", "")
        if not re.fullmatch(re.escape(work) + r"v[1-9]\d*", version):
            raise ValueError("Invalid work/version relationship")
        if version != work + "v1":
            revisions += 1
            continue
        if work in unique:
            if unique[work] != record:
                raise ValueError("Conflicting observations for one work/v1")
            duplicates += 1
            continue
        unique[work] = record
    buckets = {month: [] for month in MONTHS}
    for work, record in sorted(unique.items()):
        value = record.get("published_at")
        status, event = date_status(value) if value is None or isinstance(value, str) else ("invalid", None)
        if status != "valid":
            unassigned.append({"work_id": work, "reason": status + "_event_time"})
            continue
        reasons = []
        if not START <= event <= END:
            reasons.append("outside_development_window")
        if "cs.SE" not in record.get("categories_current", []):
            reasons.append("outside_current_query_category")
        if record.get("retrospective_exclusions"):
            reasons.extend(record["retrospective_exclusions"])
        if require_v1_category and "cs.SE" not in record.get("categories_v1", []):
            reasons.append("v1_category_sensitivity")
        if exclude_late_ids and work[:4] > "1906":
            reasons.append("late_id_diagnostic_not_as_of_repair")
        if reasons:
            excluded.append({"work_id": work, "reasons": sorted(set(reasons))})
            continue
        buckets[event.strftime("%Y-%m")].append(record)
    rows, matches = [], []
    for month in MONTHS:
        eligible = buckets[month]
        known_matches, missing, invalid = [], [], []
        for record in eligible:
            title = record.get(title_field)
            if title is None or (isinstance(title, str) and not title.strip()):
                missing.append(record["work_id"])
            elif not isinstance(title, str):
                invalid.append(record["work_id"])
            elif regex.search(title):
                known_matches.append(record["work_id"])
                matches.append({"work_id": record["work_id"], "version_id": record["version_id"],
                                "month": month, "title": title,
                                "source_ref": record.get("source_ref", {}).get("current" if title_field == "title_current" else "v1")})
        unknown = len(missing) + len(invalid)
        n = len(known_matches) if not unknown and not unassigned else None
        total = len(eligible) if not unassigned else None
        rows.append({"month": month, "eligible_works": total, "assigned_works": len(eligible),
                     "known_matches": len(known_matches), "count": n, "share": share(n, total),
                     "title_missing": len(missing), "title_invalid": len(invalid),
                     "unknown_title_ids": sorted(missing + invalid),
                     "share_bounds": [share(len(known_matches), total), share(len(known_matches) + unknown, total)],
                     "status": "UNRESOLVED_EVENT_TIME" if unassigned else "UNRESOLVED_TITLE" if unknown else "UNDEFINED_EMPTY_BIN" if not total else "DEFINED",
                     "denominator_ids": [record["work_id"] for record in eligible],
                     "matched_ids": known_matches})
    return {"months": rows, "matches": matches, "excluded": excluded, "unassigned": unassigned,
            "duplicate_observations_ignored": duplicates, "non_v1_observations_ignored": revisions}


def bimonth(rows):
    result = []
    for index in (0, 2, 4):
        pair = rows[index:index + 2]
        n = sum(row["count"] for row in pair) if all(row["count"] is not None for row in pair) else None
        total = sum(row["eligible_works"] for row in pair) if all(row["eligible_works"] is not None for row in pair) else None
        result.append({"months": [row["month"] for row in pair], "count": n,
                       "eligible_works": total, "share": share(n, total)})
    return result


def synthetic_record(index, title="Other topic", month="01", **changes):
    record = {"work_id": f"1901.{index:05d}", "version_id": f"1901.{index:05d}v1",
              "title_v1": title, "published_at": f"2019-{month}-10T12:00:00Z",
              "categories_current": ["cs.SE"], "categories_v1": ["cs.SE"],
              "available_at": None, "source_ref": {"v1": {"synthetic": True}},
              "retrospective_exclusions": []}
    return dict(record, **changes)


def synthetic_corpus(total, positive):
    return [synthetic_record(i, "Fuzzing" if i < positive else "Other topic") for i in range(total)]


def controlled_checks():
    """Assertions use hand-specified expectations; provider behavior is not simulated evidence."""
    reports = []
    def series(name, corpora, expected, implication):
        actual = [[row["count"], row["eligible_works"], row["share"]]
                  for corpus in corpora for row in evaluate(corpus)["months"][:1]]
        if actual != expected:
            raise AssertionError((name, actual, expected))
        reports.append({"case": name, "expected": expected, "actual": actual, "status": "PASS",
                        "evidence_type": "CONTROLLED_SYNTHETIC", "implication": implication})
    series("corpus_growth", [synthetic_corpus(100, 10), synthetic_corpus(200, 20)],
           [[10, 100, .1], [20, 200, .1]], "Count doubles; share cancels proportional corpus growth.")
    series("denominator_drift", [synthetic_corpus(100, 10), synthetic_corpus(200, 10)],
           [[10, 100, .1], [10, 200, .05]], "Share changes with denominator composition; no topic decline established.")
    base = synthetic_corpus(10, 1)
    series("duplicates_revisions", [base, base * 2 + [dict(base[0], version_id=base[0]["work_id"] + "v2", title_v1="Other")]],
           [[1, 10, .1], [1, 10, .1]], "Repeated observations and v2 do not add contributions.")
    series("missing_invalid_title", [[synthetic_record(0, None), synthetic_record(1, 42), synthetic_record(2, "Fuzzing")]],
           [[None, 3, None]], "Two unknown fields remain in N; n/p abstain, known matches=1, bounds 1/3..1.")
    series("sparse_small_empty", [synthetic_corpus(1, 1), synthetic_corpus(2, 1), []],
           [[1, 1, 1.0], [1, 2, .5], [0, 0, None]], "Small N is unstable; empty share undefined, no trend labels.")
    series("vocabulary_alias_drift", [[synthetic_record(0, "Fuzzing")], [synthetic_record(0, "AFL software testing")]],
           [[1, 1, 1.0], [0, 1, .0]], "Stipulated same topic renamed; lexical rule misses alias. Recall not measured.")
    delayed = synthetic_record(0, "Fuzzing", available_at="2019-07-02T00:00:00Z")
    series("delayed_availability", [[delayed]], [[1, 1, 1.0]],
           "Retrospective event-bin includes delayed item; synthetic as-of checks exclude it. Not E3 evidence.")
    series("query_selection_bias", [synthetic_corpus(100, 10), synthetic_corpus(10, 10)],
           [[10, 100, .1], [10, 10, 1.0]], "Concept-selected sample inflates share; complete selected query need not represent the field.")
    mutated = synthetic_record(0, "Fuzzing", categories_v1=["cs.LG"])
    current = evaluate([mutated])["months"][0]
    original = evaluate([mutated], require_v1_category=True)["months"][0]
    if [current["count"], original["count"]] != [1, 0]:
        raise AssertionError("Category sensitivity")
    reports.append({"case": "category_mutation", "status": "PASS", "evidence_type": "CONTROLLED_SYNTHETIC",
                    "current_category_count": 1, "v1_category_count": 0,
                    "implication": "Category rule changes numerator/denominator; neither reconstructs removed historical members."})
    future = synthetic_record(9999, "Fuzzing", published_at="2019-07-01T00:00:00Z")
    if evaluate(base + [future])["months"] != evaluate(base)["months"]:
        raise AssertionError("Future event leaked")
    # Reuse existing synthetic as-of contract to test availability, membership and vocabulary independently.
    for field in ("available_at", "membership_available_at"):
        late = dict(checks.FIXTURE["records"][0], id="late", **{field: "2019-07-01T00:00:00+00:00"})
        if checks.evaluate(checks.FIXTURE["records"] + [late]) != checks.FIXTURE["expected_base"]:
            raise AssertionError("Late availability leaked")
    if checks.evaluate(vocabulary_at="2019-07-01T00:00:00+00:00")["reason"] != "vocabulary_unavailable":
        raise AssertionError("Future vocabulary leaked")
    reports.append({"case": "cutoff_leakage", "status": "PASS", "evidence_type": "CONTROLLED_SYNTHETIC",
                    "implication": "Future event excluded; stipulated late availability/membership excluded and future vocabulary rejected by existing as-of fixture. Real availability remains unknown."})
    return reports


def write_json(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--declaration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    declaration_bytes = args.declaration.read_bytes()
    declaration = json.loads(declaration_bytes)
    if declaration["status"] != "DEVELOPMENT_ONLY_EXPLORATORY_NOT_ACCEPTED" or declaration["execution_pattern"] != PATTERN:
        raise ValueError("Unexpected experiment declaration/rule")
    run = Path(declaration["frozen_run"])
    if run.as_posix() != "experiments/research_exit_20260927/runs/20261010-development-01":
        raise ValueError("Only declared frozen development run allowed")
    for relative, expected in declaration["frozen_inputs"].items():
        checked_bytes(run / relative, expected)
    records, audited = audit(run)
    if audited["inputs"] != declaration["frozen_inputs"]:
        raise ValueError("Frozen input manifest changed")
    original = json.loads((run / "inputs/preregistration.json").read_text())
    if original["query"] != declaration["query"] or original["candidate_title_pattern"] != declaration["archived_literal_pattern"]:
        raise ValueError("Original contract changed")
    started = datetime.now(timezone.utc).isoformat()
    result = evaluate(records)
    variants = {
        "archived_literal_transport_diagnostic": evaluate(records, declaration["archived_literal_pattern"]),
        "exact_fuzzing": evaluate(records, r"\bfuzzing\b"),
        "current_title_diagnostic": evaluate(records, title_field="title_current"),
        "v1_category_subset": evaluate(records, require_v1_category=True),
        "exclude_nine_late_ids_diagnostic_not_as_of": evaluate(records, exclude_late_ids=True)}
    compact = {name: {"months": [{key: row[key] for key in ("month", "count", "eligible_works", "share", "title_missing", "title_invalid")}
                                for row in value["months"]], "matched_ids": [row["work_id"] for row in value["matches"]],
                      "excluded": value["excluded"]} for name, value in variants.items()}
    report = {"experiment_id": declaration["id"], "evidence_type": "REAL_DATA_RETROSPECTIVE_DEVELOPMENT_ONLY",
              "construct": declaration["construct"], "query": declaration["query"],
              "concept_rule": {"version": declaration["rule_version"], "pattern": PATTERN, "flags": "IGNORECASE",
                               "provenance": "Frozen preregistration literal equals existing checks.PATTERN; no lexical amendment"},
              "formula": {"count": "n(c,b) = distinct eligible works matching title rule", "share": "p(c,b) = n(c,b)/N(b), N(b)>0; otherwise null",
                          "unknown_titles": "N includes unknowns; n/p null; known matches and bounds retained"},
              "input_hashes": audited["inputs"], "as_of": {"count": None, "denominator": None, "share": None,
                          "reason": "Historical public field/membership/vocabulary availability unresolved", "E3": "NOT_PASSED"},
              "reference_quality": "NOT_MEASURED", "labels": None, "result": result,
              "sensitivity": compact, "adjacent_bimonth": bimonth(result["months"])}
    controlled = controlled_checks()
    args.output.mkdir(parents=True, exist_ok=False)
    write_json(args.output / "measurements.json", report)
    write_json(args.output / "controlled-checks.json", controlled)
    code_paths = [Path(__file__), Path(checks.__file__), Path(offline_audit.__file__), Path(acquire.__file__)]
    write_json(args.output / "execution.json", {
        "started_at_utc": started, "ended_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "platform": platform.platform(),
        "declaration_sha256": digest(declaration_bytes),
        "code_sha256": {path.name: digest(path.read_bytes()) for path in code_paths},
        "outputs_sha256": {name: digest((args.output / name).read_bytes()) for name in ("measurements.json", "controlled-checks.json")},
        "scope": "Same-host agent execution; no network, holdout or independent scientific validation"})
    print(json.dumps({"monthly": [[r["count"], r["eligible_works"], r["share"]] for r in result["months"]],
                      "matches": len(result["matches"]), "controlled_cases": len(controlled)}))


if __name__ == "__main__":
    main()
