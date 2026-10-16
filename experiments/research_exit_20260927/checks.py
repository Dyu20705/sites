"""Offline, standard-library evidence checks. Synthetic availability is not source evidence."""
import argparse
import hashlib
import json
import re
import sys
import unittest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
PATTERN = r"\bfuzz(?:ing|er|ers)?\b"


def share(count, total):
    if count is None or total is None:
        return None
    if not 0 <= count <= total:
        raise ValueError("Invalid count/denominator")
    if total == 0:
        return None
    return count / total


def dt(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timezone required")
    return parsed


def assess(records, cutoff, vocabulary_at, complete=True):
    boundary = dt(cutoff)
    if not complete:
        return {"status": "INSUFFICIENT_EVIDENCE", "reason": "coverage_unknown"}
    if not vocabulary_at or dt(vocabulary_at) > boundary:
        return {"status": "INSUFFICIENT_EVIDENCE", "reason": "vocabulary_unavailable"}
    unique = {}
    for record in records:
        if record["version"] != 1:
            continue  # This spike measures first-version titles, not latest-version text.
        if dt(record["event_at"]) > boundary:
            continue
        if not record.get("available_at") or not record.get("membership_available_at"):
            return {"status": "INSUFFICIENT_EVIDENCE", "reason": "availability_unknown"}
        if max(dt(record["available_at"]), dt(record["membership_available_at"])) > boundary:
            continue
        if not record.get("title"):
            return {"status": "INSUFFICIENT_EVIDENCE", "reason": "title_missing"}
        previous = unique.get(record["id"])
        if previous is not None and previous != record:
            raise ValueError("Conflicting observations for one work/version")
        unique[record["id"]] = record
    matched = sorted(k for k, r in unique.items() if re.search(PATTERN, r["title"], re.I))
    return {"count": len(matched), "denominator": len(unique),
            "share": share(len(matched), len(unique)), "contributors": matched,
            "denominator_ids": sorted(unique)}


def evaluate(records=None, **kwargs):
    return assess(FIXTURE["records"] if records is None else records,
                  kwargs.get("cutoff", FIXTURE["cutoff"]),
                  kwargs.get("vocabulary_at", FIXTURE["vocabulary_available_at"]),
                  kwargs.get("complete", True))


class Checks(unittest.TestCase):
    def test_hand_calculated_series(self):
        for row in FIXTURE["series"]:
            with self.subTest(case=row["id"]):
                self.assertEqual([share(n, d) for n, d in zip(row["counts"], row["totals"])], row["expected"])

    def test_invalid_count(self):
        for count, total in ((2, 1), (1, 0), (-1, 10), (0, -1)):
            with self.assertRaises(ValueError):
                share(count, total)

    def test_lineage_and_expected(self):
        self.assertEqual(evaluate(), FIXTURE["expected_base"])

    def test_idempotency(self):
        self.assertEqual(evaluate(FIXTURE["records"] * 2), FIXTURE["expected_base"])

    def test_order_independence(self):
        self.assertEqual(evaluate(list(reversed(FIXTURE["records"]))), FIXTURE["expected_base"])

    def test_revision_not_double_counted(self):
        revision = dict(FIXTURE["records"][1], version=2, title="Fuzzing new version")
        self.assertEqual(evaluate(FIXTURE["records"] + [revision]), FIXTURE["expected_base"])

    def test_conflicting_version_fails(self):
        with self.assertRaises(ValueError):
            evaluate(FIXTURE["records"] + [dict(FIXTURE["records"][0], title="Changed title")])

    def test_future_observation_isolated(self):
        future = dict(FIXTURE["records"][0], id="future", event_at="2019-07-01T00:00:00+00:00")
        self.assertEqual(evaluate(FIXTURE["records"] + [future]), FIXTURE["expected_base"])

    def test_late_availability_isolated(self):
        for field in ("available_at", "membership_available_at"):
            late = dict(FIXTURE["records"][0], id="late", **{field: "2019-07-01T00:00:00+00:00"})
            self.assertEqual(evaluate(FIXTURE["records"] + [late]), FIXTURE["expected_base"])

    def test_unknown_availability_not_zero(self):
        unknown = dict(FIXTURE["records"][0], available_at=None)
        self.assertEqual(evaluate([unknown])["reason"], "availability_unknown")

    def test_vocabulary_cutoff(self):
        self.assertEqual(evaluate(vocabulary_at="2019-07-01T00:00:00+00:00")["reason"], "vocabulary_unavailable")

    def test_missing_title(self):
        self.assertEqual(evaluate([dict(FIXTURE["records"][0], title="")])["reason"], "title_missing")

    def test_unknown_coverage(self):
        self.assertEqual(evaluate(complete=False)["reason"], "coverage_unknown")

    def test_alias_limitation_is_visible(self):
        alias = [dict(FIXTURE["records"][0], title="AFL software testing")]
        self.assertEqual(evaluate(alias)["count"], 0)  # Known false-negative risk, not validation of recall.

    def test_timezone_required(self):
        with self.assertRaises(ValueError):
            evaluate(cutoff="2019-06-30")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    initial = json.loads((ROOT / "acquisition.json").read_text(encoding="utf-8"))
    diagnostic = json.loads((ROOT / "accept-atom-diagnostic/acquisition.json").read_text(encoding="utf-8"))
    current_config_hash = hashlib.sha256((ROOT / "preregistration.json").read_bytes()).hexdigest()
    if any(m["preregistration_sha256"] != current_config_hash for m in (initial, diagnostic)):
        raise SystemExit("Preregistration changed after acquisition")
    report = {
        "synthetic_only": True, "tests_run": result.testsRun,
        "failures": len(result.failures), "errors": len(result.errors),
        "series": [{"id": row["id"], "expected": row["expected"],
                    "actual": [share(n, d) for n, d in zip(row["counts"], row["totals"])]} for row in FIXTURE["series"]],
        "record_result": evaluate(),
        "sample_audit": {"status": "NOT_MEASURED_ACCESS_FAILURE", "successful_record_responses": 0,
                         "observed_http_statuses": [m["requests"][0]["status"] for m in (initial, diagnostic)],
                         "corpus_total": None, "missingness": None, "coverage": None,
                         "v1_comparison": None, "real_signal": None, "E3": "NOT_PASSED"},
        "limitations": ["Availability in fixtures is stipulated, not measured", "No holdout or real corpus evaluated",
                        "Alias and provider composition changes can defeat both count and share"],
        "inputs": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                   for name in ("fixtures.json", "preregistration.json", "acquisition.json", "accept-atom-diagnostic/acquisition.json", "checks.py")}
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    main()
