"""Portable boundary tests. Full offline demo/E8 execution remains Windows CPython 3.14.7 only."""
import tempfile
from pathlib import Path
import unittest

from sites_demo.contracts import DemoError, canonical, local_path, percent, rational, read_json, utc
from sites_demo.pipeline import guard_records, query


class PortableContracts(unittest.TestCase):
    def test_json_canonical_roundtrip_and_duplicate_key_rejection(self):
        self.assertEqual(canonical({"é": 2, "a": [1]}), '{"a":[1],"é":2}\n'.encode("utf-8"))
        self.assertEqual(read_json(canonical({"n": 1})), {"n": 1})
        with self.assertRaisesRegex(DemoError, "INVALID_JSON"):
            read_json(b'{"id":1,"id":2}')

    def test_unsafe_paths_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            self.assertEqual(local_path(root, "sample/data.json"), Path(root) / "sample" / "data.json")
            for name in ("../escape", "a//b", "/tmp/file", "C:/Windows/file", "a\\b", "CON", "x."):
                with self.subTest(name=name), self.assertRaisesRegex(DemoError, "UNSAFE_PATH"):
                    local_path(root, name)

    def test_ratios_have_explicit_null_and_exact_boundaries(self):
        self.assertIsNone(rational(None, 4))
        self.assertIsNone(rational(0, 0))
        self.assertEqual(rational(1, 3), {"numerator": 1, "denominator": 3})
        self.assertEqual(percent(rational(1, 3)), "33.3333%")
        with self.assertRaisesRegex(DemoError, "INVALID_SIGNAL"):
            rational(4, 3)

    def test_date_parser_normalizes_explicit_offset_only(self):
        self.assertEqual(utc("2019-01-01T01:00:00+01:00"), "2019-01-01T00:00:00Z")
        self.assertIsNone(utc("2019-01-01T00:00:00"))

    def test_invalid_category_and_query_are_rejected(self):
        with self.assertRaisesRegex(DemoError, "UNKNOWN_CATEGORY"):
            guard_records([{"work_id": "1901.00001", "version_id": "1901.00001v1",
                            "categories_current": ["cs.AI"]}])
        with self.assertRaisesRegex(DemoError, "INVALID_QUERY"):
            query([], "not-fuzzing", "2019-01", "2019-06")


if __name__ == "__main__":
    unittest.main()
