from dataclasses import replace
import unittest

from sites_demo.contracts import ArtifactRef, DemoError, SourceRef, Work
from sites_demo.pipeline import MONTHS, measure, query


def work(index, month="2019-01", title="Other", *, title_status="valid", event_status="valid"):
    work_id = f"1901.{index:05d}"
    artifact = ArtifactRef("raw/v1.xml", "0" * 64, 1, "research_source")
    ref = SourceRef("v1", artifact, 0, f"http://arxiv.org/abs/{work_id}v1", "2026-10-10T00:00:00Z")
    return Work(work_id, work_id + "v1", 1, title, title, ("cs.SE",), ("cs.SE",),
                None if event_status != "valid" else month + "-10T00:00:00Z", "2019-01-10T00:00:00Z",
                None, None if event_status != "valid" else month, title_status, event_status, "valid", ref,
                replace(ref, role="current"))


class PipelineTests(unittest.TestCase):
    def test_measure_preserves_null_bounds_and_empty_bin(self):
        points = measure((work(1, title="Fuzzing"), work(2, title=None, title_status="missing")))
        january = points[0]
        self.assertEqual((january.status, january.n, january.N, january.known_matches),
                         ("UNRESOLVED_TITLE", None, 2, 1))
        self.assertEqual(january.lower_share, {"numerator": 1, "denominator": 2})
        self.assertEqual(january.upper_share, {"numerator": 2, "denominator": 2})
        self.assertEqual(points[1].status, "UNDEFINED_EMPTY_BIN")
        self.assertIsNone(points[1].share)

    def test_invalid_event_invalidates_every_month(self):
        points = measure((work(1, event_status="invalid"),))
        self.assertTrue(all(point.status == "UNRESOLVED_EVENT_TIME" for point in points))
        self.assertTrue(all(point.n is None and point.N is None for point in points))
        self.assertEqual(points[0].unassigned_work_ids, ("1901.00001",))

    def test_window_query_uses_ratio_of_sums_and_rejects_invalid_requests(self):
        points = measure((work(1, "2019-01", "Fuzzing"), work(2, "2019-01"),
                          work(3, "2019-02", "Fuzzing")))
        result = query(points, (work(1, "2019-01", "Fuzzing"), work(2, "2019-01"),
                                work(3, "2019-02", "Fuzzing")), "fuzzing", "2019-01", "2019-02")
        self.assertEqual(result["pooled"]["share"], {"numerator": 2, "denominator": 3})
        for concept, start, end in (("rag", "2019-01", "2019-02"),
                                    ("fuzzing", "2019-02", "2019-01"),
                                    ("fuzzing", "2018-01", "2019-01")):
            with self.subTest(concept=concept, start=start, end=end):
                with self.assertRaisesRegex(DemoError, "INVALID_QUERY"):
                    query(points, (), concept, start, end)


if __name__ == "__main__":
    unittest.main()
