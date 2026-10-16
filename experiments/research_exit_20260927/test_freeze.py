"""Integrity regressions against the real bounded manifest, never live provider data."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import verify_freeze as freeze

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json"


class FreezeTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST.read_bytes())
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "manifest.json"

    def check(self, manifest=None, root=ROOT, digest=None):
        raw = json.dumps(self.manifest if manifest is None else manifest).encode()
        self.path.write_bytes(raw)
        return freeze.verify(self.path, digest or freeze.sha(raw), root, ROOT)

    def test_external_anchor_rejects_manifest_edit(self):
        with self.assertRaisesRegex(ValueError, "external SHA-256"):
            self.check(digest="0" * 64)

    def test_each_mandatory_section_cannot_be_omitted(self):
        for key in freeze.REQUIRED:
            with self.subTest(key=key):
                changed = copy.deepcopy(self.manifest)
                del changed[key]
                with self.assertRaisesRegex(ValueError, "mandatory"):
                    self.check(changed)

    def test_scope_escalation_and_scientific_claims_rejected(self):
        for section, key, value in (("holdout", "authorized", True), ("criteria", "original_E3", "PASS"),
                                    ("criteria", "D09", "ACCEPTED"), ("reviewers", "real_annotations", 27),
                                    ("exposure", "independent_preregistration", True),
                                    ("budget", "measured_product_E8", True)):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.manifest)
                changed[section][key] = value
                with self.assertRaises(ValueError):
                    self.check(changed)

    def test_missing_reference_cannot_be_unhashed(self):
        changed = copy.deepcopy(self.manifest)
        del changed["files"][changed["artifact_roles"]["config"]]
        with self.assertRaisesRegex(ValueError, "Unhashed"):
            self.check(changed)

    def test_escape_path_rejected(self):
        changed = copy.deepcopy(self.manifest)
        changed["files"]["../outside.json"] = {"sha256": "0" * 64, "origin": "freeze_support"}
        with self.assertRaisesRegex(ValueError, "repository-relative"):
            self.check(changed)

    def test_missing_or_corrupted_artifact_rejected(self):
        root = Path(self.temp.name) / "empty-root"
        root.mkdir()
        with self.assertRaises(FileNotFoundError):
            self.check(root=root)
        first = sorted(self.manifest["files"])[0]
        path = root / first
        path.parent.mkdir(parents=True)
        path.write_bytes(b"corrupted frozen artifact")
        with self.assertRaisesRegex(ValueError, "Artifact SHA-256 mismatch"):
            self.check(root=root)


if __name__ == "__main__":
    unittest.main()
