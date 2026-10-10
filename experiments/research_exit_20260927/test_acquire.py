"""Offline diagnostic regression tests; no provider requests."""
import contextlib
import hashlib
import io
import json
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from unittest.mock import patch, Mock

import acquire


class DiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config = (acquire.ROOT / "preregistration.json").read_bytes()
        (self.root / "preregistration.json").write_bytes(self.config)

    def invoke(self, raw=None, error=None):
        response = io.BytesIO(raw or b"")
        response.status = 200
        response.url = "https://export.arxiv.org/api/query?test"
        response.headers = {"Content-Type": "application/atom+xml"}
        opener = Mock()
        opener.open.side_effect = error
        opener.open.return_value = response
        with patch.object(acquire, "ROOT", self.root), \
             patch("sys.argv", ["acquire.py", "--http-endpoint-diagnostic"]), \
             patch.object(acquire.urllib.request, "build_opener", return_value=opener), \
             contextlib.redirect_stdout(io.StringIO()):
            acquire.main()
        opener.open.assert_called_once()
        return json.loads((self.root / "http-endpoint-diagnostic/acquisition.json").read_text())

    def feed(self, total="1", entries=1):
        count = "" if total is None else f'<totalResults xmlns="{acquire.NS["o"]}">{total}</totalResults>'
        return (f'<feed xmlns="{acquire.NS["a"]}">' + count + '<entry><id>http://arxiv.org/abs/1901.00001v1</id></entry>' * entries + '</feed>').encode()

    def test_success_stops_after_count_and_hashes_raw(self):
        raw = self.feed()
        manifest = self.invoke(raw)
        self.assertEqual(manifest["status"], "HTTP_ENDPOINT_DIAGNOSTIC_SUCCEEDED")
        self.assertEqual(manifest["reported_total"], 1)
        self.assertEqual(manifest["requests"][0]["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertTrue(manifest["requests"][0]["url"].startswith("http://export.arxiv.org/"))

    def test_zero_count_is_access_success_only(self):
        self.assertEqual(self.invoke(self.feed("0", 0))["status"], "HTTP_ENDPOINT_DIAGNOSTIC_SUCCEEDED")

    def test_bad_feed_or_count_never_claims_success(self):
        original_root = self.root
        for index, raw in enumerate([b"<html/>", b"broken", self.feed(None), self.feed("-1"), self.feed("x"), self.feed("1", 0)]):
            with self.subTest(raw=raw):
                # Each test response gets an isolated evidence directory.
                self.root = original_root / str(index)
                self.root.mkdir()
                (self.root / "preregistration.json").write_bytes(self.config)
                self.assertEqual(self.invoke(raw)["status"], "ACCESS_OR_RESPONSE_FAILURE")

    def test_http_error_preserves_url_excerpt_and_hash(self):
        body = b"blocked" * 1000
        error = urllib.error.HTTPError("https://export.arxiv.org/api/query?test", 406, "Not Acceptable", {"Content-Type": "text/plain"}, io.BytesIO(body))
        manifest = self.invoke(error=error)
        entry = manifest["requests"][0]
        self.assertEqual(manifest["status"], "ACCESS_OR_RESPONSE_FAILURE")
        self.assertEqual(entry["status"], 406)
        self.assertEqual(entry["final_url"], error.url)
        self.assertEqual(entry["error_excerpt_bytes"], 2048)
        self.assertEqual(entry["error_excerpt_sha256"], hashlib.sha256(body[:2048]).hexdigest())
        self.assertEqual((self.root / "http-endpoint-diagnostic" / entry["error_excerpt_file"]).read_bytes(), body[:2048])
        self.assertFalse((self.root / "http-endpoint-diagnostic/raw/count.xml").exists())

    def test_network_error_is_single_attempt(self):
        manifest = self.invoke(error=urllib.error.URLError("DNS failure"))
        self.assertEqual(manifest["status"], "ACCESS_OR_RESPONSE_FAILURE")
        self.assertNotIn("status", manifest["requests"][0])

    def test_redirect_is_recorded_and_rate_limited(self):
        redirects = []
        handler = acquire.DiagnosticRedirectHandler(redirects)
        with patch.object(acquire.time, "sleep") as sleep:
            request = handler.redirect_request(urllib.request.Request("http://export.arxiv.org/api/query"), None, 301, "Moved", {}, "https://export.arxiv.org/api/query")
        self.assertEqual(request.full_url, "https://export.arxiv.org/api/query")
        self.assertEqual(redirects[0]["status"], 301)
        sleep.assert_called_once_with(3.1)

    def test_existing_manifest_is_preserved_without_request(self):
        directory = self.root / "http-endpoint-diagnostic"
        directory.mkdir()
        target = directory / "acquisition.json"
        target.write_bytes(b"old evidence")
        with patch.object(acquire, "ROOT", self.root), patch("sys.argv", ["acquire.py", "--http-endpoint-diagnostic"]), patch.object(acquire.urllib.request, "build_opener") as opener:
            with self.assertRaises(SystemExit):
                acquire.main()
        opener.assert_not_called()
        self.assertEqual(target.read_bytes(), b"old evidence")


if __name__ == "__main__":
    unittest.main()
