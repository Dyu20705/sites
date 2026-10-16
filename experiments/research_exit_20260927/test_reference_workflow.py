import unittest
from copy import deepcopy

from simulate_reference_workflow import fixture, reconcile


class ReferenceWorkflowTests(unittest.TestCase):
    def test_complete_fixture_retains_raw_judgments_and_uncertainty(self):
        records = fixture()
        before = deepcopy(records)
        result = reconcile(records)
        self.assertEqual(records, before)
        self.assertEqual(result["raw_judgment_count"], 54)
        self.assertEqual(result["agreements"], 18)
        self.assertEqual(result["adjudications"], 9)
        self.assertEqual(result["final_label_counts"],
                         {"NEGATIVE": 9, "POSITIVE": 9, "UNCERTAIN": 9})
        self.assertEqual(result["records"][20]["raw_judgments"]["a"]["label"], "POSITIVE")
        self.assertEqual(result["records"][20]["final_label"], "UNCERTAIN")
        self.assertEqual(result["independent_scientific_quality"], "NOT_MEASURED")

    def test_missing_evidence_is_not_negative(self):
        records = fixture()[:1]
        records[0]["a"]["evidence_refs"] = []
        with self.assertRaisesRegex(ValueError, "requires evidence"):
            reconcile(records)

    def test_unresolved_disagreement_does_not_complete(self):
        records = fixture()[18:19]
        records[0]["c"] = None
        with self.assertRaisesRegex(ValueError, "pending"):
            reconcile(records)

    def test_duplicate_cannot_inflate_support(self):
        record = fixture()[0]
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            reconcile([record, deepcopy(record)])

    def test_real_id_or_reference_is_rejected(self):
        records = fixture()[:1]
        records[0]["work_id"] = "1902.09334"
        with self.assertRaisesRegex(ValueError, "Fictional"):
            reconcile(records)
        records = fixture()[:1]
        records[0]["a"]["evidence_refs"] = ["https://arxiv.org/abs/1902.09334"]
        with self.assertRaisesRegex(ValueError, "outside"):
            reconcile(records)

    def test_invalid_role_label_or_rationale_is_rejected(self):
        for key, value in (("role", "HUMAN_A"), ("mode", "INDEPENDENT"),
                           ("label", "TREND"), ("rationale", "")):
            records = fixture()[:1]
            records[0]["a"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                reconcile(records)

    def test_agreement_cannot_be_rewritten_by_adjudicator(self):
        records = fixture()[:1]
        records[0]["c"] = fixture()[18]["c"]
        with self.assertRaisesRegex(ValueError, "No adjudication"):
            reconcile(records)


if __name__ == "__main__":
    unittest.main()
