"""Accepted-boundary and integrated offline checks; no scientific validation claim."""
from copy import deepcopy
import io
from contextlib import redirect_stdout
import json
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import Mock, patch
import urllib.request

from sites_demo import render
from sites_demo.contracts import (D09_SHA, F1_PATH, F1_SHA, MONTHS, ROOT, SCHEMAS, QUESTION_IDS, DemoError,
                                 canonical, create_output, integer, local_path, percent,
                                 read_json, sha, write_new)
from sites_demo.pipeline import (evaluate_records, load_evaluator, point, prepare,
                                 product_digest, project, query, verify_f1)
from sites_demo.__main__ import (check_navigation, compare, main, network_disabled,
                                 runtime_profile, verify_evaluation, verify_index)


class DemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT / "build").mkdir(exist_ok=True)
        cls.temp = tempfile.TemporaryDirectory(prefix="tests-", dir=ROOT / "build")
        cls.directory = Path(cls.temp.name).absolute()
        with patch.object(urllib.request, "urlopen", side_effect=AssertionError("network request")), \
             patch.object(socket, "socket", side_effect=AssertionError("socket creation")):
            cls.snapshot = prepare(ROOT, ROOT / F1_PATH)
        cls.evaluator = load_evaluator(ROOT)
        cls.records = read_json(cls.snapshot["files"][cls.snapshot["manifest"]["artifact_roles"]["normalized"]])
        cls.profile = runtime_profile("automated fixture", "AUTHOR_ENGINEERING_TEST", "all development records and code")
        profile_path = cls.directory / "runtime.json"
        profile_path.write_bytes(canonical(cls.profile))
        cls.evaluation = {"schema_version": 1, "evaluation_id": "D09-EVAL-TEST-ONLY", "freeze_sha256": F1_SHA,
                          "d09_sha256": D09_SHA, "product_commit": "0" * 40, "product_code_sha256": product_digest(ROOT),
                          "budget": {"max_works": 598, "wall_seconds": 60, "peak_process_bytes": 256 * 1024 * 1024, "live_requests": 0},
                          "schemas": SCHEMAS, "protocol": {"question_ids": QUESTION_IDS, "questions_required": 5, "independent_scientific_quality": "NOT_MEASURED"},
                          "protocol_artifacts": {name: sha((ROOT / name).read_bytes()) for name in ("evaluation/reviewer-task.md", "evaluation/REPLAY.md", "evaluation/owner-acceptance.json")},
                          "reviewer": cls.profile["reviewer"], "runtime_profile": {"path": profile_path.relative_to(ROOT).as_posix(), "sha256": sha(profile_path.read_bytes())}}
        cls.evaluation_path = cls.directory / "evaluation.json"
        cls.evaluation_path.write_bytes(canonical(cls.evaluation))
        cls.evaluation_sha = sha(cls.evaluation_path.read_bytes())
        cls.args = ["--root", str(ROOT), "--f1", str(ROOT / F1_PATH), "--expected-f1-sha", F1_SHA,
                    "--evaluation", str(cls.evaluation_path), "--expected-evaluation-sha", cls.evaluation_sha]
        cls.outputs = []
        for name in ("one", "two"):
            output = cls.directory / name
            with redirect_stdout(io.StringIO()) as log:
                status = main(["build", *cls.args, "--out", str(output)])
            if status:
                raise AssertionError(log.getvalue())
            cls.outputs.append(output)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def assertCode(self, code, callback, *args, **kwargs):
        with self.assertRaises(DemoError) as caught:
            callback(*args, **kwargs)
        self.assertEqual(caught.exception.code, code)

    def synthetic(self, index, **changes):
        return self.evaluator.synthetic_record(index, **changes)

    def points(self, records):
        result = evaluate_records(records, self.evaluator)
        return [point(row, [r["work_id"] for r in result["unassigned"]]) for row in result["months"]]

    def test_full_frozen_population_oracles_and_sensitivities(self):
        self.assertEqual(len(self.snapshot["files"]), 122)
        self.assertEqual(len(self.snapshot["works"]), 598)
        self.assertEqual([[p["n"], p["N"]] for p in self.snapshot["points"]], [[0, 91], [1, 79], [2, 97], [1, 103], [4, 122], [1, 106]])
        self.assertEqual(len(self.snapshot["sensitivities"]), 6)
        self.assertEqual(len(self.snapshot["sensitivities"]["exact_fuzzing"]["matched_ids"]), 5)

    def test_wrong_external_f1_rejected(self):
        self.assertCode("MANIFEST_DIGEST", verify_f1, ROOT, ROOT / F1_PATH, "0" * 64)

    def test_changed_artifact_rejected_before_import(self):
        original = Path.read_bytes
        target = ROOT / self.snapshot["manifest"]["artifact_roles"]["contract_en"]
        def corrupt(path):
            return original(path) + b"\n" if path == target else original(path)
        with patch.object(Path, "read_bytes", corrupt), patch("sites_demo.pipeline.load_evaluator") as called:
            self.assertCode("ARTIFACT_DIGEST", prepare, ROOT, ROOT / F1_PATH)
            called.assert_not_called()

    def test_bad_categories_rejected_before_evaluator(self):
        spy = Mock()
        for value in (None, [], "cs.SE", ["cs.LG"], ["cs.SE", None], ["cs.SE", "cs.SE"]):
            with self.subTest(value=value):
                self.assertCode("UNKNOWN_CATEGORY", evaluate_records, [self.synthetic(1, categories_current=value)], spy)
        row = self.synthetic(1)
        del row["categories_current"]
        self.assertCode("UNKNOWN_CATEGORY", evaluate_records, [row], spy)
        spy.evaluate.assert_not_called()

    def test_work_and_version_identity_rejected(self):
        for changes in ({"work_id": "../evil"}, {"version_id": "1901.00002v1"}, {"version_id": True}):
            self.assertCode("IDENTITY_CONFLICT", evaluate_records, [self.synthetic(1, **changes)], self.evaluator)

    def test_duplicates_and_revisions_do_not_add_contributions(self):
        row = self.synthetic(1, title="Fuzzing")
        result = evaluate_records([row, deepcopy(row), dict(row, version_id=row["work_id"] + "v2")], self.evaluator)
        self.assertEqual([result["months"][0][k] for k in ("count", "eligible_works")], [1, 1])
        self.assertEqual(result["duplicate_observations_ignored"], 1)
        self.assertEqual(result["non_v1_observations_ignored"], 1)

    def test_conflicting_v1_fails(self):
        row = self.synthetic(1)
        self.assertCode("IDENTITY_CONFLICT", evaluate_records, [row, dict(row, title_v1="Fuzzing")], self.evaluator)

    def test_unknown_title_kept_in_N_and_bounds(self):
        points = self.points([self.synthetic(1, title="Fuzzing"), self.synthetic(2, title=None), self.synthetic(3, title=42)])
        p = points[0]
        self.assertEqual([p["n"], p["N"], p["known_matches"], p["share"]], [None, 3, 1, None])
        self.assertEqual(p["lower_share"], {"numerator": 1, "denominator": 3})
        self.assertEqual(p["upper_share"], {"numerator": 3, "denominator": 3})
        self.assertEqual(query(points, "fuzzing", MONTHS[0], MONTHS[-1])["pooled"]["status"], "UNRESOLVED_TITLE")

    def test_missing_event_propagates_to_all_months_and_windows(self):
        for value in (None, "not-a-date", "2019-01-01T00:00:00"):
            points = self.points([self.synthetic(1, published_at=value), self.synthetic(2, title="Fuzzing")])
            for p in points:
                self.assertEqual([p["n"], p["N"], p["share"], p["lower_share"]], [None] * 4)
                self.assertEqual(p["unassigned_work_ids"], ["1901.00001"])
            self.assertIsNone(query(points, "fuzzing", "2019-02", "2019-05")["pooled"]["N"])

    def test_empty_bin_is_not_zero_share(self):
        p = self.points([])[0]
        self.assertEqual([p["n"], p["N"], p["share"], p["lower_share"], p["upper_share"]], [0, 0, None, None, None])
        self.assertEqual(p["status"], "UNDEFINED_EMPTY_BIN")

    def test_future_event_excluded_and_utc_boundary_used(self):
        records = [self.synthetic(1, title="Fuzzing", published_at="2019-07-01T01:00:00+02:00"),
                   self.synthetic(2, title="Fuzzing", published_at="2019-07-01T00:00:00Z")]
        p = self.points(records)[-1]
        self.assertEqual([p["n"], p["N"]], [1, 1])
        self.assertEqual(p["matched_ids"], ["1901.00001"])

    def test_pooled_ratio_of_sums_all_21_windows_and_lineage(self):
        self.assertEqual(len(self.snapshot["windows"]), 21)
        for window in self.snapshot["windows"]:
            rows, pooled = window["monthly"], window["pooled"]
            n, total = sum(r["n"] for r in rows), sum(r["N"] for r in rows)
            self.assertEqual(pooled["share"], {"numerator": n, "denominator": total})
            self.assertEqual(len(pooled["denominator_ids"]), total)
            self.assertEqual(len(pooled["matched_ids"]), n)
        pair = query(self.snapshot["points"], "fuzzing", "2019-01", "2019-02")["pooled"]
        self.assertEqual(pair["share"], {"numerator": 1, "denominator": 170})
        self.assertNotEqual(1 / 170, (0 / 91 + 1 / 79) / 2)

    def test_invalid_queries_fail_without_fallback(self):
        for concept, start, end in (("other", "2019-01", "2019-02"), ("fuzzing", "2019-06", "2019-01"),
                                     ("fuzzing", "2018-12", "2019-01"), ("fuzzing", "2019-01", "2019-07")):
            self.assertCode("INVALID_QUERY", query, self.snapshot["points"], concept, start, end)

    def test_raw_lineage_wrong_index_role_identity_hash_and_fields(self):
        mutations = [lambda r: r["source_ref"]["v1"].update(entry_index=True),
                     lambda r: r["source_ref"]["v1"].update(entry_index=99999),
                     lambda r: r["source_ref"]["v1"].update(sha256="0" * 64),
                     lambda r: r["source_ref"].update(v1=r["source_ref"]["current"]),
                     lambda r: r.update(title_v1="changed"),
                     lambda r: r["source_ref"]["v1"].update(entry_id="http://arxiv.org/abs/1901.00000v1")]
        for mutate in mutations:
            records = deepcopy(self.records)
            mutate(records[0])
            self.assertCode("RAW_LINEAGE", project, ROOT, self.snapshot["manifest"], self.snapshot["files"], records, self.evaluator)

    def test_population_must_be_exact_598(self):
        for records in (self.records[:-1], self.records + [self.records[0]]):
            self.assertCode("IDENTITY_CONFLICT", project, ROOT, self.snapshot["manifest"], self.snapshot["files"], records, self.evaluator)

    def test_safe_paths(self):
        for path in ("../escape", "/absolute", "C:/temp/x", "a\\b", "a//b", "a/./b", "a:b", "https://x", "a%2fb", "CON.txt", "a.", "a?"):
            self.assertCode("UNSAFE_PATH", local_path, self.directory, path)
        self.assertEqual(local_path(self.directory, "safe/file.json"), self.directory / "safe/file.json")

    def test_json_canonical_and_strict_values(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":Infinity}', b'{"x":1e999}'):
            self.assertCode("INVALID_JSON", read_json, raw)
        self.assertEqual(canonical({"b": 2, "a": "é"}), '{"a":"é","b":2}\n'.encode())
        self.assertFalse(integer(True))
        self.assertEqual(percent({"numerator": 1, "denominator": 598}), "0.1672%")

    def test_html_escapes_provider_markup_and_urls(self):
        bundle = deepcopy(next(iter(self.snapshot["bundles"].values())))
        payload = '<script>alert("x")</script><img src="https://evil.example/x" onerror="x">'
        bundle["work"]["title_v1"] = payload
        bundle["v1_entry_text"] = payload
        html = render.evidence(bundle).decode()
        self.assertNotIn(payload, html)
        self.assertIn('&lt;script&gt;alert(&quot;x&quot;)', html)
        self.assertNotIn('src="https://', html)

    def test_no_network_in_runtime_guard(self):
        self.assertCode("NETWORK_DISABLED", network_disabled, "socket.connect", ())
        self.assertCode("NETWORK_DISABLED", network_disabled, "socket.getaddrinfo", ())
        network_disabled("open", ())
        network_disabled("socket.gethostname", ())

    def test_redirected_output_directory_rejected(self):
        target, link = self.directory / "link-target", self.directory / "redirected"
        target.mkdir()
        try:
            link.symlink_to(target, target_is_directory=True)
        except OSError:
            # Windows supports junctions without the symlink privilege.
            import subprocess
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        try:
            self.assertCode("UNSAFE_PATH", local_path, self.directory, "redirected/data.json")
            self.assertCode("UNSAFE_PATH", create_output, link / "new-output")
        finally:
            link.rmdir() if link.is_junction() else link.unlink()

    def test_failed_worker_leaves_incomplete_run(self):
        output = self.directory / "failed-run"
        with redirect_stdout(io.StringIO()):
            args = list(self.args)
            args[args.index("--expected-evaluation-sha") + 1] = "0" * 64
            self.assertEqual(main(["build", *args, "--out", str(output)]), 1)
        self.assertFalse((output / "COMPLETE").exists())
        self.assertEqual(read_json((output / "execution.json").read_bytes())["error_codes"], ["EVALUATION_DIGEST"])

    def test_replay_identical_semantics_and_full_navigation(self):
        a, b = self.outputs
        result = compare(a / "semantic-index.json", b / "semantic-index.json")
        self.assertEqual(result["status"], "PASS")
        index = verify_index(a / "semantic-index.json")
        checked = check_navigation(a, {v["path"] for v in index["artifacts"]})
        self.assertEqual(checked["html_pages"], 621)
        self.assertGreater(checked["local_links"], 7000)

    def test_no_overwrite_preserves_bytes(self):
        output = self.outputs[0]
        before = (output / "semantic-index.json").read_bytes()
        self.assertCode("OUTPUT_EXISTS", create_output, output)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(main(["build", *self.args, "--out", str(output)]), 2)
        self.assertEqual(before, (output / "semantic-index.json").read_bytes())
        with self.assertRaises(FileExistsError):
            write_new(output, "index.html", b"overwrite")

    def test_incomplete_output_rejected(self):
        path = self.directory / "incomplete"
        path.mkdir()
        (path / "semantic-index.json").write_bytes((self.outputs[0] / "semantic-index.json").read_bytes())
        self.assertCode("INCOMPLETE_RUN", verify_index, path / "semantic-index.json")

    def test_tampered_output_and_unlisted_file_rejected(self):
        output = self.outputs[1]
        page = output / "index.html"
        original = page.read_bytes()
        page.write_bytes(original + b"tampered")
        try:
            self.assertCode("ARTIFACT_DIGEST", verify_index, output / "semantic-index.json")
        finally:
            page.write_bytes(original)
        extra = output / "unexpected.json"
        extra.write_bytes(b"{}")
        try:
            self.assertCode("ARTIFACT_DIGEST", verify_index, output / "semantic-index.json")
        finally:
            extra.unlink()

    def test_runtime_profile_is_separate_and_mismatch_fails(self):
        altered = deepcopy(self.profile["identity"])
        altered["python"] = "0.0.0"
        self.assertCode("RUNTIME_PROFILE", verify_evaluation, ROOT, self.evaluation_path, self.evaluation_sha, altered)
        self.assertCode("EVALUATION_DIGEST", verify_evaluation, ROOT, self.evaluation_path, "0" * 64)

    def test_resource_measurements_are_native_and_within_budget(self):
        for output in self.outputs:
            record = read_json((output / "execution.json").read_bytes())
            self.assertEqual(record["status"], "PASS")
            self.assertGreater(record["worker_peak_bytes"], 0)
            self.assertGreater(record["launcher_peak_bytes"], 0)
            self.assertLessEqual(record["peak_process_bytes"], 256 * 1024 * 1024)
            self.assertLessEqual(record["elapsed_seconds"], 60)
            self.assertEqual(record["live_requests"], 0)


if __name__ == "__main__":
    unittest.main()
