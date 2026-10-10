"""Bounded arXiv feasibility probe. Run explicitly; never called by offline checks."""
import hashlib
import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}


def stamp():
    return datetime.now(timezone.utc).isoformat()


def read_entries(raw):
    feed = ET.fromstring(raw)
    if feed.tag != "{" + NS["a"] + "}feed":
        raise ValueError("Response is not an Atom feed")
    entries = []
    for node in feed.findall("a:entry", NS):
        def value(tag):
            return " ".join((node.findtext("a:" + tag, "", NS)).split())
        entries.append({
            "id": value("id"), "title": value("title"),
            "published": value("published"), "updated": value("updated"),
            "categories": sorted(x.get("term", "") for x in node.findall("a:category", NS)),
        })
    total = feed.findtext("o:totalResults", None, NS)
    return entries, int(total) if total is not None else None


class DiagnosticRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Retain observed redirects, including a redirect followed by HTTP failure."""

    def __init__(self, redirects):
        super().__init__()
        self.redirects = redirects

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirects.append({"url": req.full_url, "status": code, "location": newurl})
        time.sleep(3.1)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--accept-atom-diagnostic", action="store_true")
    parser.add_argument("--http-endpoint-diagnostic", action="store_true")
    args = parser.parse_args()
    if args.accept_atom_diagnostic and args.http_endpoint_diagnostic:
        raise SystemExit("Choose only one diagnostic mode")
    config_bytes = (ROOT / "preregistration.json").read_bytes()
    config = json.loads(config_bytes)
    if args.http_endpoint_diagnostic:
        run_root = ROOT / "http-endpoint-diagnostic"
    elif args.accept_atom_diagnostic:
        run_root = ROOT / "accept-atom-diagnostic"
    else:
        run_root = ROOT
    run_root.mkdir(exist_ok=True)
    target = run_root / "raw"
    target.mkdir(exist_ok=True)
    manifest_path = run_root / "acquisition.json"
    if manifest_path.exists():
        raise SystemExit("Existing acquisition preserved. Use a separately preregistered run for another attempt.")
    manifest = {"started_at": stamp(), "preregistration_sha256": hashlib.sha256(config_bytes).hexdigest(),
                "acquire_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "requests": [], "status": "RUNNING", "unique_bound": config["max_unique_works"],
                "amendment": "AM-02" if args.http_endpoint_diagnostic else ("AM-01" if args.accept_atom_diagnostic else None)}

    def save():
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    def fetch(name, params):
        if manifest["requests"]:
            time.sleep(3.1)
        base_url = "http://export.arxiv.org/api/query?" if args.http_endpoint_diagnostic else "https://export.arxiv.org/api/query?"
        url = base_url + urllib.parse.urlencode(params)
        entry = {"url": url, "started_at": stamp(), "file": "raw/" + name, "redirects": []}
        manifest["requests"].append(entry)
        save()
        headers = {"User-Agent": "SITES-research-audit/0.1 (https://github.com/Dyu20705/sites)"}
        if args.accept_atom_diagnostic:
            headers["Accept"] = "application/atom+xml"
        request = urllib.request.Request(url, headers=headers)
        entry["request_headers"] = headers
        try:
            opener = urllib.request.build_opener(DiagnosticRedirectHandler(entry["redirects"]))
            with opener.open(request, timeout=45) as response:
                raw = response.read(20_000_001)
                if len(raw) > 20_000_000:
                    raise ValueError("Response exceeds 20 MB bound")
                entry["status"] = response.status
                entry["final_url"] = response.url
                entry["content_type"] = response.headers.get("Content-Type")
            with (target / name).open("xb") as output:
                output.write(raw)
            entry.update(sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), ended_at=stamp())
            save()
            return read_entries(raw)
        except Exception as error:
            entry.update(error=type(error).__name__ + ": " + str(error), ended_at=stamp())
            if isinstance(error, urllib.error.HTTPError):
                entry["status"] = error.code
                entry["final_url"] = error.geturl()
                entry["content_type"] = error.headers.get("Content-Type") if error.headers else None
                # This is a bounded excerpt, not a full provider response.
                excerpt = error.read(2048)
                error.close()
                excerpt_path = "raw/" + name + ".error.txt"
                with (run_root / excerpt_path).open("xb") as output:
                    output.write(excerpt)
                entry.update(response_excerpt=excerpt.decode("utf-8", errors="replace"),
                             error_excerpt_file=excerpt_path, error_excerpt_bytes=len(excerpt),
                             error_excerpt_sha256=hashlib.sha256(excerpt).hexdigest())
            save()
            raise

    try:
        params = {"search_query": config["query"], "sortBy": config["sort_by"],
                  "sortOrder": config["sort_order"], "start": 0, "max_results": 1}
        count_entries, total = fetch("count.xml", params)
        manifest["reported_total"] = total
        if args.http_endpoint_diagnostic:
            if total is None or total < 0:
                raise ValueError("Diagnostic requires a nonnegative totalResults")
            if len(count_entries) != min(1, total):
                raise ValueError("Diagnostic count response has inconsistent entries")
            manifest["status"] = "HTTP_ENDPOINT_DIAGNOSTIC_SUCCEEDED"
            manifest["final_url"] = manifest["requests"][-1].get("final_url")
            return
        if total is None or total <= 0 or total > config["max_unique_works"]:
            manifest["status"] = "STOPPED_COUNT_OR_BOUND"
            return
        current = []
        for offset in range(0, total, config["page_size"]):
            params.update(start=offset, max_results=min(config["page_size"], total-offset))
            page, reported = fetch(f"current-{offset:04d}.xml", params)
            if reported != total or len(page) != params["max_results"]:
                raise ValueError("Count drift or incomplete page; no completeness claim")
            current.extend(page)
        ids = [r["id"].rsplit("/abs/", 1)[-1].rsplit("v", 1)[0] for r in current]
        if len(set(ids)) != total:
            raise ValueError("Duplicate work IDs across pages; stop before v1 acquisition")
        manifest["current_records"] = len(current)
        versions = []
        for offset in range(0, len(ids), 100):
            batch = [identifier + "v1" for identifier in ids[offset:offset+100]]
            records, _ = fetch(f"v1-{offset:04d}.xml", {"id_list": ",".join(batch), "max_results": len(batch)})
            if sorted(r["id"].rsplit("/abs/", 1)[-1] for r in records) != sorted(batch):
                raise ValueError("Version endpoint did not return exactly requested v1 IDs")
            versions.extend(records)
        manifest.update(status="ACQUIRED_NOT_TEMPORALLY_VERIFIED", v1_records=len(versions))
    except Exception as error:
        manifest.update(status="ACCESS_OR_RESPONSE_FAILURE", error=type(error).__name__ + ": " + str(error))
    finally:
        manifest["ended_at"] = stamp()
        save()
        print(json.dumps({k: v for k, v in manifest.items() if k != "requests"}, indent=2))


if __name__ == "__main__":
    main()
