import json
import math
from pathlib import Path
import tempfile
import unittest

from sites_demo.contracts import ContractError, canonical_json, load_json_strict, validate_local_path


class ContractTests(unittest.TestCase):
    def test_canonical_json_is_stable_utf8_lf_and_rejects_nonfinite(self):
        self.assertEqual(canonical_json({"z": 1, "é": [2]}), '{"z":1,"é":[2]}\n'.encode())
        with self.assertRaises(ContractError):
            canonical_json({"bad": math.nan})

    def test_json_duplicate_keys_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"x":1,"x":2}', encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "duplicate"):
                load_json_strict(path)

    def test_local_paths_reject_escape_absolute_drive_and_url(self):
        self.assertEqual(validate_local_path("windows/2019-01_2019-02.html"), "windows/2019-01_2019-02.html")
        for bad in ("../x", "/tmp/x", "C:/x", "https://example.test/x", "a//b", "./x", "a\\b"):
            with self.subTest(path=bad):
                with self.assertRaises(ContractError):
                    validate_local_path(bad)


if __name__ == "__main__":
    unittest.main()
