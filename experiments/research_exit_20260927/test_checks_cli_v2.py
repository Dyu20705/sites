"""Output-preservation regressions; the frozen legacy calculation stays unchanged."""
import contextlib
import errno
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import time
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
            self.assertEqual(list(Path(directory).iterdir()), [target])

    def test_fresh_report_equals_frozen_result_and_repeat_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            command = [sys.executable, str(Path(checks_cli_v2.__file__)),
                       "--output", str(target)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = Path(__file__).with_name("results") / "run-1.json"
            self.assertEqual(target.read_bytes(), expected.read_bytes())
            self.assertEqual(list(Path(directory).iterdir()), [target])
            repeat = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(repeat.returncode, 2)
            self.assertEqual(target.read_bytes(), expected.read_bytes())
            self.assertEqual(list(Path(directory).iterdir()), [target])

    def test_failed_checker_does_not_publish_a_report(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            failure = subprocess.CompletedProcess([], 1, "", "fixture check failed")
            with patch.object(checks_cli_v2.subprocess, "run", return_value=failure):
                with contextlib.redirect_stderr(io.StringIO()):
                    result = checks_cli_v2.main(["--output", str(target)])
            self.assertEqual(result, 1)
            self.assertFalse(target.exists())
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_partial_preparation_failure_never_exposes_destination(self):
        for raised in (False, True):
            with self.subTest(raised=raised), tempfile.TemporaryDirectory() as directory:
                target = Path(directory) / "report.json"

                def failed_preparation(command, **kwargs):
                    Path(command[-1]).write_bytes(b'{"partial":')
                    self.assertFalse(target.exists())
                    if raised:
                        raise OSError(errno.ENOSPC, "simulated preparation failure")
                    return subprocess.CompletedProcess(command, 1, "", "write failed")

                with patch.object(checks_cli_v2.subprocess, "run", side_effect=failed_preparation):
                    with patch.object(checks_cli_v2.os, "link") as link:
                        with contextlib.redirect_stderr(io.StringIO()):
                            if raised:
                                with self.assertRaises(SystemExit) as error:
                                    checks_cli_v2.main(["--output", str(target)])
                                self.assertEqual(error.exception.code, 1)
                            else:
                                self.assertEqual(checks_cli_v2.main(["--output", str(target)]), 1)
                        link.assert_not_called()
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_unsupported_hard_links_fail_closed_and_clean_up(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            errors = io.StringIO()
            with patch.object(checks_cli_v2.os, "link", side_effect=OSError(errno.EOPNOTSUPP, "unsupported")):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(errors):
                    with self.assertRaises(SystemExit) as error:
                        checks_cli_v2.main(["--output", str(target)])
            self.assertEqual(error.exception.code, 1)
            self.assertIn("Atomic no-clobber publication failed", errors.getvalue())
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_two_processes_race_only_after_both_reports_are_complete(self):
        child = '''
import pathlib, sys
import checks_cli_v2
real_link = checks_cli_v2.os.link
def gated_link(source, destination):
    pathlib.Path(sys.argv[2]).write_bytes(pathlib.Path(source).read_bytes())
    sys.stdin.readline()
    real_link(source, destination)
checks_cli_v2.os.link = gated_link
raise SystemExit(checks_cli_v2.main(["--output", sys.argv[1]]))
'''
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "report.json"
            ready = [Path(directory) / f"ready-{n}" for n in range(2)]
            expected = (Path(__file__).with_name("results") / "run-1.json").read_bytes()
            processes = []
            try:
                for marker in ready:
                    processes.append(subprocess.Popen(
                        [sys.executable, "-c", child, str(target), str(marker)],
                        cwd=Path(__file__).parent, stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
                deadline = time.monotonic() + 15
                while not all(marker.exists() for marker in ready):
                    self.assertLess(time.monotonic(), deadline, "publication barrier timed out")
                    self.assertTrue(all(p.poll() is None for p in processes), "child exited before barrier")
                    time.sleep(0.01)
                self.assertFalse(target.exists())
                for marker in ready:
                    self.assertEqual(marker.read_bytes(), expected)
                for process in processes:
                    process.stdin.write("\n")
                    process.stdin.flush()
                output = [p.communicate(timeout=15) for p in processes]
                self.assertEqual(sorted(p.returncode for p in processes), [0, 2], output)
                self.assertEqual(target.read_bytes(), expected)
                self.assertEqual(set(Path(directory).iterdir()), {target, *ready})
            finally:
                for process in processes:
                    if process.poll() is None:
                        process.kill()
                    process.communicate()


if __name__ == "__main__":
    unittest.main()
