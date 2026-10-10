"""Hand-calculated field validation and integrity rejection; offline only."""
import tempfile
import unittest
from pathlib import Path
import offline_audit as audit


class FieldAuditTests(unittest.TestCase):
    def test_missing_and_invalid_dates_are_distinct(self):
        self.assertEqual(audit.date_status("")[0], "missing")
        for value in ("2019-02-30T00:00:00Z", "2019-01-01T00:00:00", "broken"):
            self.assertEqual(audit.date_status(value)[0], "invalid")
        self.assertEqual(audit.date_status("2019-02-01T00:30:00+01:00")[1].strftime("%Y-%m"), "2019-01")

    def test_field_status_does_not_treat_missing_title_as_nonmatch(self):
        record = {field: "value" for field in audit.FIELDS}
        record.update(title_v1="", published_at="2019-01-02T00:00:00Z", updated_at="2019-01-01T00:00:00Z", categories_v1=["cs.SE"], categories_current=[""])
        statuses = audit.field_status(record)
        self.assertEqual(statuses["title_v1"], "missing")
        self.assertEqual(statuses["updated_at"], "invalid")
        self.assertEqual(statuses["categories_current"], "invalid")

    def test_work_and_version_identity(self):
        self.assertEqual(audit.identity("http://arxiv.org/abs/1901.00001v3"), ("1901.00001", 3))
        for value in ("http://arxiv.org/abs/1901.00001", "http://arxiv.org/abs/1901.00001v0", "other"):
            with self.assertRaises(ValueError):
                audit.identity(value)

    def test_checksum_corruption_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "raw.xml"
            path.write_bytes(b"original")
            expected = audit.digest(path.read_bytes())
            path.write_bytes(b"corrupt")
            with self.assertRaisesRegex(ValueError, "Checksum mismatch"):
                audit.checked_bytes(path, expected)


if __name__ == "__main__":
    unittest.main()
