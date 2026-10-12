"""Exercise real Git objects and disposable artifacts, without altering project evidence."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import verify_git_bytes


class GitBytesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.doc = self.repo / "docs/note.md"
        self.doc.parent.mkdir()
        self.doc.write_bytes(b"first\nsecond\n")
        verify_git_bytes.git(self.repo, "init", "--quiet")
        verify_git_bytes.git(self.repo, "-c", "core.autocrlf=false", "add", "docs/note.md")
        verify_git_bytes.git(self.repo, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                             "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "fixture")
        self.revision = verify_git_bytes.git(self.repo, "rev-parse", "HEAD").decode().strip()

    def run_cli(self, *extra, paths=("docs/note.md",), compare=True):
        command = [sys.executable, verify_git_bytes.__file__, "--repo", str(self.repo),
                   "--revision", self.revision]
        for path in paths:
            command.extend(["--path", path])
        if compare:
            command.extend(["--compare-root", str(self.repo)])
        result = subprocess.run([*command, *extra], capture_output=True, text=True)
        return result, json.loads(result.stdout) if result.stdout else None

    def test_exact_hash_and_deterministic_read_only_comparison(self):
        before = self.doc.read_bytes()
        first, report = self.run_cli()
        second, _ = self.run_cli()
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(report["files"][0]["state"], "exact")
        self.assertEqual(report["files"][0]["committed_sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(self.doc.read_bytes(), before)

    def test_digest_only_uses_objects_even_if_artifact_corrupted(self):
        self.doc.write_bytes(b"corrupt")
        result, report = self.run_cli(compare=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["files"][0]["state"], "hashed")
        self.assertEqual(report["files"][0]["committed_sha256"], hashlib.sha256(b"first\nsecond\n").hexdigest())

    def test_corruption_fails_even_with_doc_exception(self):
        self.doc.write_bytes(b"wrong\r\nsecond\r\n")
        result, report = self.run_cli("--allow-doc-eol", "docs/note.md")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["mismatched_paths"], ["docs/note.md"])
        self.assertEqual(self.doc.read_bytes(), b"wrong\r\nsecond\r\n")

    def test_missing_artifact_and_missing_git_blob_fail(self):
        self.doc.unlink()
        result, report = self.run_cli(paths=("docs/note.md", "docs/absent.md"))
        self.assertEqual(result.returncode, 1)
        self.assertEqual([row["state"] for row in report["files"]], ["missing_git_blob", "missing_artifact"])
        self.assertEqual(report["mismatched_paths"], ["docs/absent.md", "docs/note.md"])

    def test_line_endings_require_explicit_documentation_exception(self):
        self.doc.write_bytes(b"first\r\nsecond\r\n")
        strict, report = self.run_cli()
        self.assertEqual(strict.returncode, 1)
        self.assertEqual(report["files"][0]["state"], "byte_mismatch")
        allowed, report = self.run_cli("--allow-doc-eol", "docs/note.md")
        self.assertEqual(allowed.returncode, 0, allowed.stderr)
        self.assertEqual(report["files"][0]["state"], "documentation_eol_only")
        self.assertNotEqual(report["files"][0]["committed_sha256"], report["files"][0]["artifact_sha256"])
        self.assertEqual(self.doc.read_bytes(), b"first\r\nsecond\r\n")

    def test_frozen_artifacts_cannot_opt_into_normalization(self):
        for path in ("experiments/raw.xml", "experiments/config.json", "experiments/signal_evaluator.py",
                     "experiments/measurements.json", "experiments/raw/note.md", "docs/config.json"):
            with self.subTest(path=path):
                result, report = self.run_cli("--allow-doc-eol", path, paths=(path,))
                self.assertEqual(result.returncode, 2)
                self.assertIsNone(report)
                self.assertIn("EOL exceptions", result.stderr)

    def test_invalid_scope_and_revision_are_nonzero(self):
        for path in ("../outside.md", "/outside.md", "docs/../note.md", "docs\\note.md"):
            with self.subTest(path=path):
                result, _ = self.run_cli(paths=(path,))
                self.assertEqual(result.returncode, 2)
        self.revision = "no-such-revision"
        result, _ = self.run_cli()
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
