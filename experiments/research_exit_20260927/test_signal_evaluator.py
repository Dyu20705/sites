"""Offline contract tests with independently specified expectations."""
import re
import unittest
from signal_evaluator import (PATTERN, bimonth, controlled_checks, evaluate,
                              synthetic_corpus, synthetic_record)


class SignalTests(unittest.TestCase):
    def test_word_boundary_and_stipulated_double_escape(self):
        wrong_synthetic_pattern = r"\\bfuzz(?:ing|er|ers)?\\b"
        self.assertIsNone(re.search(wrong_synthetic_pattern, "Fuzzing software", re.I))
        for title in ("Fuzz", "FUZZING", "A fuzzer", "Two fuzzers"):
            self.assertIsNotNone(re.search(PATTERN, title, re.I))
        for title in ("Fuzzy logic", "Defuzzing", "AFL software testing"):
            self.assertIsNone(re.search(PATTERN, title, re.I))

    def test_all_ten_controlled_failures(self):
        reports = controlled_checks()
        self.assertEqual(len(reports), 10)
        self.assertTrue(all(row["status"] == "PASS" for row in reports))

    def test_missing_invalid_titles_not_nonmatches(self):
        result = evaluate([synthetic_record(0, None), synthetic_record(1, 42), synthetic_record(2, "Fuzzing")])
        row = result["months"][0]
        self.assertEqual((row["count"], row["eligible_works"], row["share"]), (None, 3, None))
        self.assertEqual((row["known_matches"], row["title_missing"], row["title_invalid"]), (1, 1, 1))
        self.assertEqual(row["share_bounds"], [1 / 3, 1])

    def test_missing_invalid_event_time_invalidates_denominator(self):
        for value in (None, 42, "bad", "2019-01-10T12:00:00"):
            result = evaluate([synthetic_record(0, "Fuzzing", published_at=value)])
            self.assertTrue(all(row["eligible_works"] is None and row["count"] is None for row in result["months"]))
            self.assertEqual(len(result["unassigned"]), 1)

    def test_conflicting_v1_fails(self):
        original = synthetic_record(0, "Fuzzing")
        with self.assertRaises(ValueError):
            evaluate([original, dict(original, title_v1="Other")])

    def test_identity_and_version_fails(self):
        for changes in ({"work_id": "bad"}, {"version_id": "1901.00001v1"}, {"version_id": "1901.00000v0"}):
            with self.assertRaises(ValueError):
                evaluate([synthetic_record(0, **changes)])

    def test_empty_vs_observed_zero(self):
        empty = evaluate([])["months"][0]
        zero = evaluate(synthetic_corpus(10, 0))["months"][0]
        self.assertEqual((empty["count"], empty["share"]), (0, None))
        self.assertEqual((zero["count"], zero["share"]), (0, 0))

    def test_order_and_identity_idempotency(self):
        records = synthetic_corpus(10, 2)
        expected = evaluate(records)
        self.assertEqual(evaluate(list(reversed(records))), expected)
        self.assertEqual(evaluate(records * 3)["months"], expected["months"])

    def test_utc_binning_and_cutoff(self):
        a = synthetic_record(0, "Fuzzing", published_at="2019-02-01T00:30:00+01:00")
        b = synthetic_record(1, "Fuzzing", published_at="2019-07-01T00:30:00+01:00")
        c = synthetic_record(2, "Fuzzing", published_at="2019-07-01T00:00:00Z")
        result = evaluate([a, b, c])
        self.assertEqual([row["count"] for row in result["months"]], [1, 0, 0, 0, 0, 1])
        self.assertEqual(result["excluded"][0]["work_id"], c["work_id"])

    def test_lineage_matches_and_nonmatches(self):
        result = evaluate(synthetic_corpus(3, 1))
        self.assertEqual(result["months"][0]["denominator_ids"], ["1901.00000", "1901.00001", "1901.00002"])
        self.assertEqual(result["matches"][0]["source_ref"], {"synthetic": True})

    def test_bimonth_is_ratio_of_sums(self):
        result = evaluate([synthetic_record(0, "Fuzzing"), synthetic_record(1, "Other", month="02"), synthetic_record(2, "Other", month="02")])
        row = bimonth(result["months"])[0]
        self.assertEqual((row["count"], row["eligible_works"], row["share"]), (1, 3, 1 / 3))


if __name__ == "__main__":
    unittest.main()
