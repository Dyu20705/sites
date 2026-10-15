import unittest

from sites_demo.render import render


class RenderTests(unittest.TestCase):
    def test_untrusted_titles_and_source_text_are_escaped(self):
        attack = '<script>alert("x")</script>&'
        ref = {
            "role": "v1",
            "artifact": {
                "path": "frozen/raw.xml",
                "sha256": "0" * 64,
                "size_bytes": 1,
                "origin": "research_source",
            },
            "entry_index": 0,
            "entry_id": "http://arxiv.org/abs/1901.00001v1",
            "acquired_at": "2026-10-10T00:00:00+00:00",
        }
        work = {
            "work_id": "1901.00001",
            "version_id": "1901.00001v1",
            "current_version": 1,
            "title_v1": attack,
            "title_current": attack,
            "categories_v1": ["cs.SE"],
            "categories_current": ["cs.SE"],
            "submitted_v1_at": "2019-01-01T00:00:00Z",
            "updated_current_at": "2019-01-01T00:00:00Z",
            "available_at": None,
            "event_month": "2019-01",
            "title_status": "valid",
            "event_status": "valid",
            "category_status": "valid",
            "v1_ref": ref,
            "current_ref": {**ref, "role": "current"},
        }
        point = {
            "rule_id": "RE-20260927-01-documented-word-boundary-v1",
            "months": ["2019-01"],
            "n": 0,
            "N": 1,
            "known_matches": 0,
            "share": {"numerator": 0, "denominator": 1},
            "lower_share": {"numerator": 0, "denominator": 1},
            "upper_share": {"numerator": 0, "denominator": 1},
            "status": "DEFINED",
            "denominator_ids": ["1901.00001"],
            "matched_ids": [],
            "unknown_title_ids": [],
            "unassigned_work_ids": [],
        }
        query = {
            "concept": "fuzzing",
            "start": "2019-01",
            "end": "2019-01",
            "monthly": [point],
            "pooled": point,
            "evidence_ids": ["1901.00001"],
            "freeze_sha256": "0" * 64,
            "claim_scope": "OBSERVED_RETROSPECTIVE_LEXICAL_PREVALENCE",
        }
        artifacts = render(
            [query],
            [{
                "work": work,
                "rule_id": point["rule_id"],
                "matched": False,
                "contribution": "NONMATCH",
                "freeze_id": "F1-M1-R-20261012-v1",
                "freeze_sha256": "0" * 64,
                "contract_version": "M1-R-20261010-v1",
                "current_entry_text": attack,
                "v1_entry_text": attack,
            }],
        )
        page = artifacts["evidence/1901.00001v1.html"].decode("utf-8")
        self.assertNotIn("<script>", page)
        self.assertIn("&lt;script&gt;", page)
        self.assertNotIn("javascript:", page.lower())


if __name__ == "__main__":
    unittest.main()
