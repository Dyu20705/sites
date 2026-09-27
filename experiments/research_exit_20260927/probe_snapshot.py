"""One HEAD request to the official persistent DBLP archive; no corpus download."""
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

target = Path(__file__).resolve().parent / "dblp-access.json"
if target.exists():
    raise SystemExit("Preserve the existing probe")
record = {"url": "https://dblp.org/xml/release/dblp-2019-04-01.xml.gz", "method": "HEAD",
          "started_at": datetime.now(timezone.utc).isoformat(), "purpose": "archive reachability/size only, not a sample audit"}
try:
    req = urllib.request.Request(record["url"], method="HEAD", headers={"User-Agent": "SITES-research-audit/0.1 (https://github.com/Dyu20705/sites)"})
    with urllib.request.urlopen(req, timeout=30) as response:
        record.update(status=response.status, final_url=response.url,
                      headers={key: response.headers.get(key) for key in ("Content-Type", "Content-Length", "Last-Modified", "ETag")})
except Exception as error:
    record["error"] = type(error).__name__ + ": " + str(error)
    if isinstance(error, urllib.error.HTTPError):
        record["status"] = error.code
record["ended_at"] = datetime.now(timezone.utc).isoformat()
target.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
