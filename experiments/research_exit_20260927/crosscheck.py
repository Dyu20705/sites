"""Independent direct-XML cross-check of the real audit; no audit parser imports."""
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run = args.run
    ns = {"a": "http://www.w3.org/2005/Atom"}
    current, first = {}, {}
    raw_hashes = {}
    manifest = json.loads((run / "acquisition.json").read_text())
    for request in manifest["requests"]:
        raw = (run / request["file"]).read_bytes()
        raw_hashes[request["file"]] = hashlib.sha256(raw).hexdigest()
        assert raw_hashes[request["file"]] == request["sha256"]
        if "current-" in request["file"]:
            target = current
        elif "v1-" in request["file"]:
            target = first
        else:
            continue
        for index, entry in enumerate(ET.fromstring(raw).findall("a:entry", ns)):
            identifier = entry.findtext("a:id", namespaces=ns).split("/abs/")[1]
            work = identifier.rsplit("v", 1)[0]
            assert work not in target
            target[work] = {"id": identifier, "title": " ".join(entry.findtext("a:title", "", ns).split()),
                            "published": entry.findtext("a:published", "", ns), "updated": entry.findtext("a:updated", "", ns),
                            "categories": sorted(node.get("term", "") for node in entry.findall("a:category", ns)),
                            "file": request["file"], "entry_index": index}
    records = json.loads((run / "replay-1/normalized-records.json").read_text(encoding="utf-8"))
    audit = json.loads((run / "replay-1/audit.json").read_text())
    assert set(current) == set(first) == {record["work_id"] for record in records}
    months = Counter(datetime.fromisoformat(row["published"].replace("Z", "+00:00")).strftime("%Y-%m") for row in first.values())
    assert dict(months) == {month: row["returned"] for month, row in audit["months"].items()}
    for record in records:
        work = record["work_id"]
        assert record["title_v1"] == first[work]["title"]
        assert record["title_current"] == current[work]["title"]
        assert record["published_at"] == first[work]["published"]
        assert record["updated_at"] == first[work]["updated"]
        assert record["categories_v1"] == first[work]["categories"]
        assert record["categories_current"] == current[work]["categories"]
        for kind, lookup in (("current", current), ("v1", first)):
            ref = record["source_ref"][kind]
            assert ref["file"] == lookup[work]["file"] and ref["entry_index"] == lookup[work]["entry_index"]
            assert ref["sha256"] == raw_hashes[ref["file"]]
        assert record["available_at"] is None
    late_ids = [{"work_id": work, "published_at": row["published"], "id_month": "20" + work[:2] + "-" + work[2:4],
                 "source_ref": {"file": row["file"], "entry_index": row["entry_index"]}}
                for work, row in sorted(first.items()) if work[:4] > "1906"]
    result = {"status": "PASS", "method": "Direct ElementTree parse; no acquire/offline_audit imports", "records_checked": len(records),
              "raw_files_hashed": len(raw_hashes), "months": dict(sorted(months.items())),
              "late_id_month_count": len(late_ids), "late_id_month_records": late_ids,
              "interpretation": "Observed ID month after cutoff while published precedes cutoff. Public-availability conflict inferred using official arXiv ID-month policy; no exact announcement timestamp inferred.",
              "policy": "https://info.arxiv.org/help/availability.html", "E3": "NOT_PASSED"}
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "records_checked", "raw_files_hashed", "late_id_month_count")}))


if __name__ == "__main__":
    main()
