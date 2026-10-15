import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from urllib.parse import urlsplit

from sites_demo.contracts import DemoError, canonical_json
from sites_demo.pipeline import (DEVELOPMENT_CLAIM, F1_DIGEST, INDEPENDENT_CLAIM,
                                 INTERPRETATION_TASKS, SCHEMA_IDENTITIES, _build_worker,
                                 build, compare, evidence, measure,
                                 launch_build, product_identity, project, query, runtime_identity,
                                 verify_inputs)

ROOT = Path(__file__).resolve().parents[1]
F1 = ROOT / "experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json"


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.circles = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "a" and "href" in values:
            self.hrefs.append(values["href"])
        if tag == "link" and "href" in values:
            self.hrefs.append(values["href"])
        if tag == "circle":
            self.circles += 1


def evaluation_file(directory):
    product = product_identity(ROOT)
    runtime = runtime_identity()
    manifest = json.loads(F1.read_text())
    controls_path = manifest["artifact_roles"]["controls"]
    record = {
        "schema_version": 1,
        "evaluation_id": "D09-EVAL-v1-DEVELOPMENT",
        "mode": "DEVELOPMENT_ONLY",
        "d09": {"version": "D09-M1-20261012-v1",
                 "sha256": "a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc",
                 "acceptance_url": "https://github.com/Dyu20705/sites/issues/71#issuecomment-6123995295"},
        "f1": {"id": "F1-M1-R-20261012-v1", "sha256": F1_DIGEST},
        "product": product,
        "reviewer": {"identity": None, "role": "AUTOMATED_DEVELOPMENT_CHECK",
                     "prior_exposure": "FULL", "independent": False},
        "runtime_profile": runtime,
        "runtime_profile_sha256": hashlib.sha256(canonical_json(runtime)).hexdigest(),
        "schemas": SCHEMA_IDENTITIES,
        "tasks": {"interpretation_items": INTERPRETATION_TASKS,
                  "navigation": {"open_match": True, "open_nonmatch": True},
                  "replay": {"builds": 2, "semantic_compare": True}},
        "controls": {
            "control_artifact": {"path": controls_path,
                                 "sha256": manifest["files"][controls_path]["sha256"]},
            "sensitivity_names": manifest["sensitivities"],
        },
        "limits": {"works": 598, "seconds": 60, "peak_process_bytes": 268435456,
                   "network_requests": 0},
        "claim": DEVELOPMENT_CLAIM,
    }
    path = Path(directory) / "evaluation.json"
    path.write_bytes(canonical_json(record))
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


class IntegrationTests(unittest.TestCase):
    def test_real_frozen_corpus_projects_measures_queries_and_traces(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, digest = evaluation_file(directory)
            verified = verify_inputs(ROOT, F1, F1_DIGEST, evaluation, digest)
            works = project(verified)
            points = measure(works)
            self.assertEqual(len(works), 598)
            self.assertEqual([p.n for p in points], [0, 1, 2, 1, 4, 1])
            self.assertEqual([p.N for p in points], [91, 79, 97, 103, 122, 106])
            result = query(points, works, "fuzzing", "2019-01", "2019-06")
            self.assertEqual(result["pooled"]["share"], {"numerator": 9, "denominator": 598})
            bundle = evidence("1903.02981", verified, works)
            self.assertEqual(bundle["contribution"], "MATCH")
            self.assertIn("1903.02981v1", bundle["v1_entry_text"])

    def test_build_is_complete_offline_traceable_and_replay_equal(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, digest = evaluation_file(directory)
            out1, out2 = Path(directory) / "run-1", Path(directory) / "run-2"
            first = build(ROOT, F1, F1_DIGEST, evaluation, digest, out1)
            second = build(ROOT, F1, F1_DIGEST, evaluation, digest, out2)
            self.assertTrue((out1 / "COMPLETE").is_file())
            self.assertEqual(len(list((out1 / "windows").glob("*.html"))), 21)
            self.assertEqual(len(list((out1 / "evidence").glob("*.html"))), 598)
            self.assertIn("Observed v1-title lexical prevalence", (out1 / "index.html").read_text())
            self.assertNotIn("emerging", (out1 / "index.html").read_text().lower())
            sensitivities = json.loads((out1 / "data/sensitivities.json").read_text())
            first_work = json.loads((out1 / "data/works.json").read_text())[0]
            self.assertEqual(
                set(first_work["v1_ref"]),
                {"role", "artifact", "entry_index", "entry_id", "acquired_at"},
            )
            self.assertEqual(set(first_work["v1_ref"]["artifact"]),
                             {"path", "sha256", "size_bytes", "origin"})
            self.assertGreater(first_work["v1_ref"]["artifact"]["size_bytes"], 0)
            self.assertEqual(first_work["v1_ref"]["artifact"]["origin"], "research_source")
            self.assertEqual(
                sensitivities["adjacent_bimonth"],
                [
                    {"count": 1, "eligible_works": 170, "months": ["2019-01", "2019-02"],
                     "share": 0.0058823529411764705},
                    {"count": 3, "eligible_works": 200, "months": ["2019-03", "2019-04"],
                     "share": 0.015},
                    {"count": 5, "eligible_works": 228, "months": ["2019-05", "2019-06"],
                     "share": 0.021929824561403508},
                ],
            )
            self.assertIn("Adjacent bimonth ratio of sums",
                          (out1 / "sensitivities.html").read_text())
            window_text = (out1 / "windows/2019-01_2019-06.html").read_text()
            self.assertIn('href="2019-01_2019-01.html#numerator"', window_text)
            self.assertIn('href="2019-01_2019-01.html#denominator"', window_text)
            evidence_text = (out1 / "evidence/1903.02981v1.html").read_text()
            self.assertEqual(evidence_text.count("../windows/"), 21)
            compared = compare(out1 / "semantic-index.json", out2 / "semantic-index.json")
            self.assertTrue(compared["equal"])
            self.assertTrue(compared["execution_records_compared"])
            self.assertEqual(first["semantic_sha256"], second["semantic_sha256"])
            self.assertIn(first["status"], {"PASS", "NOT_MEASURED"})

            for page in out1.rglob("*.html"):
                parser = LinkCollector()
                parser.feed(page.read_text(encoding="utf-8"))
                for href in parser.hrefs:
                    parsed = urlsplit(href)
                    self.assertFalse(parsed.scheme or parsed.netloc, (page, href))
                    target = (page.parent / parsed.path).resolve()
                    self.assertTrue(target.is_relative_to(out1.resolve()), (page, href))
                    self.assertTrue(target.is_file(), (page, href))
            window = out1 / "windows/2019-01_2019-06.html"
            parser = LinkCollector()
            parser.feed(window.read_text(encoding="utf-8"))
            self.assertEqual(parser.circles, 6)

            style = out2 / "style.css"
            original_style = style.read_bytes()
            style.write_bytes(b"tampered")
            compared = compare(out1 / "semantic-index.json", out2 / "semantic-index.json")
            self.assertFalse(compared["equal"])
            self.assertTrue(any(row.get("run") == "b" and row.get("artifact") == "style.css"
                                for row in compared["differences"]))
            style.write_bytes(original_style)
            index_path = out2 / "semantic-index.json"
            index = json.loads(index_path.read_text())
            index["artifacts"][0]["origin"] = "untrusted"
            index_path.write_bytes(canonical_json(index))
            compared = compare(out1 / "semantic-index.json", index_path)
            self.assertFalse(compared["equal"])
            self.assertTrue(any(row.get("error") == "invalid artifact origin"
                                for row in compared["differences"]))

    def test_existing_or_symlink_output_and_corrupt_input_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, digest = evaluation_file(directory)
            existing = Path(directory) / "exists"
            existing.mkdir()
            with self.assertRaisesRegex(DemoError, "OUTPUT_EXISTS"):
                build(ROOT, F1, F1_DIGEST, evaluation, digest, existing)
            link = Path(directory) / "link"
            link.symlink_to(existing, target_is_directory=True)
            with self.assertRaisesRegex(DemoError, "OUTPUT_EXISTS"):
                build(ROOT, F1, F1_DIGEST, evaluation, digest, link)
            with self.assertRaisesRegex(DemoError, "OUTPUT_EXISTS"):
                launch_build(ROOT, F1, F1_DIGEST, evaluation, digest, link)
            with self.assertRaisesRegex(DemoError, "MANIFEST_DIGEST"):
                verify_inputs(ROOT, F1, "0" * 64, evaluation, digest)

    def test_private_worker_is_offline_and_cannot_mark_a_run_complete(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, digest = evaluation_file(directory)
            out = Path(directory) / "worker-only"
            with mock.patch("socket.socket.connect", side_effect=AssertionError("network forbidden")):
                execution = _build_worker(ROOT, F1, F1_DIGEST, evaluation, digest, out,
                                          write_complete=False)
            self.assertFalse((out / "COMPLETE").exists())
            self.assertIn(execution["status"], {"PASS", "NOT_MEASURED"})

    def test_evaluation_rejects_incomplete_tasks(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, _ = evaluation_file(directory)
            record = json.loads(evaluation.read_text())
            record["tasks"]["interpretation_items"] = []
            evaluation.write_bytes(canonical_json(record))
            digest = hashlib.sha256(evaluation.read_bytes()).hexdigest()
            with self.assertRaisesRegex(DemoError, "RUNTIME_PROFILE"):
                verify_inputs(ROOT, F1, F1_DIGEST, evaluation, digest)

    def test_independent_metadata_rejects_exposure_and_browser_placeholders(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, _ = evaluation_file(directory)
            record = json.loads(evaluation.read_text())
            profile = record["runtime_profile"]
            profile.update({"python": "3.14.7", "implementation": "CPython",
                            "pointer_bits": 64, "os": "Windows", "os_release": "11",
                            "machine": "AMD64", "processor": "Example CPU",
                            "ram_bytes": 16 * 1024**3, "cpu_count": 8,
                            "browser": "Microsoft Edge 141.0.3537.71"})
            record["mode"] = "INDEPENDENT"
            record["reviewer"] = {"identity": "reviewer-1", "role": "INDEPENDENT_REVIEWER",
                                  "prior_exposure": "FULL", "independent": True}
            record["claim"] = INDEPENDENT_CLAIM
            record["runtime_profile_sha256"] = hashlib.sha256(canonical_json(profile)).hexdigest()
            evaluation.write_bytes(canonical_json(record))
            digest = hashlib.sha256(evaluation.read_bytes()).hexdigest()
            with mock.patch("sites_demo.pipeline.runtime_identity", return_value=profile):
                with self.assertRaisesRegex(DemoError, "RUNTIME_PROFILE"):
                    verify_inputs(ROOT, F1, F1_DIGEST, evaluation, digest)

            record["reviewer"]["prior_exposure"] = "NONE"
            record["runtime_profile"]["browser"] = "Recorded Browser"
            record["runtime_profile_sha256"] = hashlib.sha256(
                canonical_json(record["runtime_profile"])).hexdigest()
            evaluation.write_bytes(canonical_json(record))
            digest = hashlib.sha256(evaluation.read_bytes()).hexdigest()
            with mock.patch("sites_demo.pipeline.runtime_identity",
                            return_value=record["runtime_profile"]):
                with self.assertRaisesRegex(DemoError, "RUNTIME_PROFILE"):
                    verify_inputs(ROOT, F1, F1_DIGEST, evaluation, digest)

    def test_cli_verify_build_compare(self):
        with tempfile.TemporaryDirectory() as directory:
            evaluation, digest = evaluation_file(directory)
            out1, out2 = Path(directory) / "cli-1", Path(directory) / "cli-2"
            common = ["--f1", str(F1), "--expected-f1-sha", F1_DIGEST,
                      "--evaluation", str(evaluation), "--expected-evaluation-sha", digest]
            for command in (["verify", *common], ["build", *common, "--out", str(out1)],
                            ["build", *common, "--out", str(out2)],
                            ["compare", str(out1 / "semantic-index.json"), str(out2 / "semantic-index.json")]):
                result = subprocess.run([sys.executable, "-m", "sites_demo", *command], cwd=ROOT,
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, (command, result.stdout, result.stderr))
            for output in (out1, out2):
                execution = json.loads((output / "execution.json").read_text())
                self.assertIn("Outer launcher plus fresh worker", execution["memory_method"])
                self.assertIn(execution["status"], {"PASS", "NOT_MEASURED"})


if __name__ == "__main__":
    unittest.main()
