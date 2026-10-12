"""Output-preservation regressions; the frozen legacy calculation stays unchanged."""
import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import checks_cli_v2


class PreservingChecksCliTests(unittest.TestCase):
    def test_existing_evidence_is_preserved_without_running_checker(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            target.write_bytes(b"historical evidence")
            with patch.object(checks_cli_v2.subprocess, "run") as run:
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                    checks_cli_v2.main(["--output", str(target)])
            self.assertEqual(error.exception.code, 2)
            run.assert_not_called()
            self.assertEqual(target.read_bytes(), b"historical evidence")

    def test_fresh_report_equals_frozen_result_and_repeat_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            command = [sys.executable, str(Path(checks_cli_v2.__file__)),
                       "--output", str(target)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = Path(__file__).with_name("results") / "run-1.json"
            self.assertEqual(target.read_bytes(), expected.read_bytes())
            repeat = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(repeat.returncode, 2)
            self.assertEqual(target.read_bytes(), expected.read_bytes())

    def test_failed_checker_does_not_publish_a_report(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            failure = subprocess.CompletedProcess([], 1, "", "fixture check failed")
            with patch.object(checks_cli_v2.subprocess, "run", return_value=failure):
                with contextlib.redirect_stderr(io.StringIO()):
                    result = checks_cli_v2.main(["--output", str(target)])
            self.assertEqual(result, 1)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
