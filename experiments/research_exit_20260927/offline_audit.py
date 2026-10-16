"""Offline field/identity audit of a frozen development acquisition. No network."""
import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import acquire
from acquire import NS, read_entries

FIELDS = ("work_id", "version_id", "title_v1", "published_at", "updated_at", "categories_v1", "categories_current")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked_bytes(path, expected):
    raw = path.read_bytes()
    if digest(raw) != expected:
        raise ValueError(f"Checksum mismatch: {path.name}")
    return raw


def identity(value):
    match = re.fullmatch(r"https?://arxiv.org/abs/(\d{4}\.\d{4,5})v([1-9]\d*)", value)
    if not match:
        raise ValueError(f"Invalid versioned work identity: {value!r}")
    return match.group(1), int(match.group(2))


def date_status(value):
    if not value:
        return "missing", None
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if date.tzinfo is None:
            return "invalid", None
        return "valid", date.astimezone(timezone.utc)
    except ValueError:
        return "invalid", None


def field_status(record):
    statuses = {field: "missing" if not record[field] else "valid" for field in FIELDS}
    for field in ("published_at", "updated_at"):
        statuses[field] = date_status(record[field])[0]
    for field in ("categories_v1", "categories_current"):
        if record[field] and any(not value or value != value.strip() for value in record[field]):
            statuses[field] = "invalid"
    published = date_status(record["published_at"])[1]
    updated = date_status(record["updated_at"])[1]
    if published and updated and updated < published:
        statuses["updated_at"] = "invalid"
    return statuses


def audit(run_dir):
    manifest_bytes = (run_dir / "acquisition.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest["status"] != "ACQUIRED_NOT_TEMPORALLY_VERIFIED":
        raise ValueError("Complete acquisition required; failed/partial input is not a corpus")
    config_bytes = checked_bytes(run_dir / "inputs/preregistration.json", manifest["preregistration_sha256"])
    checked_bytes(run_dir / "inputs/acquire.py", manifest["acquire_sha256"])
    access_bytes = checked_bytes(run_dir / "inputs/am02-acquisition.json", manifest["access_evidence"]["sha256"])
    access = json.loads(access_bytes)
    checked_bytes(run_dir / "inputs/am02-count.xml", access["requests"][0]["sha256"])
    if access["status"] != "HTTP_ENDPOINT_DIAGNOSTIC_SUCCEEDED" or access["preregistration_sha256"] != manifest["preregistration_sha256"] or access["reported_total"] != manifest["reported_total"]:
        raise ValueError("AM-02/config/count evidence mismatch")
    config = json.loads(config_bytes)
    total = manifest["reported_total"]
    if not 0 < total <= min(2000, config["max_unique_works"]):
        raise ValueError("Count outside preregistered development bound")
    current, versions, inputs, pages = [], [], {}, []
    inputs["acquisition.json"] = digest(manifest_bytes)
    inputs["inputs/preregistration.json"] = digest(config_bytes)
    inputs["inputs/acquire.py"] = manifest["acquire_sha256"]
    inputs["inputs/am02-acquisition.json"] = digest(access_bytes)
    inputs["inputs/am02-count.xml"] = access["requests"][0]["sha256"]
    count_requests = 0
    offset = 0
    requested_versions = []
    for request in manifest["requests"]:
        if request["status"] != 200:
            raise ValueError("Non-success response in acquired corpus")
        relative = request["file"].replace("\\", "/")
        path = (run_dir / relative).resolve()
        if not path.is_relative_to((run_dir / "raw").resolve()):
            raise ValueError("Raw input escaped run directory")
        raw = checked_bytes(path, request["sha256"])
        if len(raw) != request["bytes"]:
            raise ValueError("Response byte count mismatch")
        inputs[relative] = digest(raw)
        entries, reported = read_entries(raw)
        params = parse_qs(urlparse(request["url"]).query)
        tagged = []
        for index, entry in enumerate(entries):
            entry = dict(entry)
            entry["source_ref"] = {"file": relative, "entry_index": index, "entry_id": entry["id"], "sha256": request["sha256"]}
            entry["acquired_at"] = request["ended_at"]
            tagged.append(entry)
        if path.name == "count.xml" or path.name.startswith("current-"):
            if params.get("search_query") != [config["query"]] or reported != total:
                raise ValueError("Query/count drift")
            if params.get("sortBy") != [config["sort_by"]] or params.get("sortOrder") != [config["sort_order"]]:
                raise ValueError("Sort settings differ from preregistration")
            requested_start = int(params["start"][0])
            requested_size = int(params["max_results"][0])
            feed = ET.fromstring(raw)
            if int(feed.findtext("o:startIndex", "-1", NS)) != requested_start or int(feed.findtext("o:itemsPerPage", "-1", NS)) != requested_size or len(entries) != requested_size:
                raise ValueError("Pagination metadata/entry count mismatch")
            if path.name == "count.xml":
                count_requests += 1
                if requested_start != 0 or requested_size != 1:
                    raise ValueError("Invalid count request")
            else:
                if requested_start != offset or requested_size != min(config["page_size"], total - offset):
                    raise ValueError("Noncontiguous or incomplete page")
                offset += len(entries)
                current.extend(tagged)
                pages.append({"file": relative, "start": requested_start, "entries": len(entries), "reported_total": reported})
        elif path.name.startswith("v1-"):
            requested = params["id_list"][0].split(",")
            observed = [identity(entry["id"])[0] + "v" + str(identity(entry["id"])[1]) for entry in entries]
            if len(requested) > 100 or int(params["max_results"][0]) != len(requested) or sorted(observed) != sorted(requested) or any(identity(entry["id"])[1] != 1 for entry in entries):
                raise ValueError("Version batch did not return exactly requested v1 IDs")
            requested_versions.extend(requested)
            versions.extend(tagged)
        else:
            raise ValueError("Unrecognized input response")
    current_ids = [identity(entry["id"])[0] for entry in current]
    version_ids = [identity(entry["id"])[0] for entry in versions]
    if (count_requests != 1 or offset != total or len(set(current_ids)) != total
            or len(versions) != total or len(set(version_ids)) != total or set(current_ids) != set(version_ids)
            or sorted(requested_versions) != sorted(identifier + "v1" for identifier in current_ids)
            or manifest["current_records"] != total or manifest["v1_records"] != total):
        raise ValueError("Population, deduplication or v1 completeness failure")
    lookup = {identity(entry["id"])[0]: entry for entry in versions}
    records = []
    for entry in current:
        work_id, current_version = identity(entry["id"])
        first = lookup[work_id]
        record = {"work_id": work_id, "version_id": work_id + "v1", "version_current": current_version,
                  "title_v1": first["title"], "title_current": entry["title"],
                  "published_at": first["published"], "updated_at": first["updated"],
                  "published_current": entry["published"], "updated_current": entry["updated"],
                  "categories_v1": first["categories"], "categories_current": entry["categories"],
                  "acquired_at": {"current": entry["acquired_at"], "v1": first["acquired_at"]},
                  "source_ref": {"current": entry["source_ref"], "v1": first["source_ref"]},
                  "available_at": None, "availability_status": "unresolved"}
        record["field_status"] = field_status(record)
        record["validation_status"] = "unresolved_availability" if all(status == "valid" for status in record["field_status"].values()) else "missing_or_invalid_fields"
        date = date_status(record["published_at"])[1]
        fallback = date_status(record["published_current"])[1]
        record["bin"] = (date or fallback).strftime("%Y-%m") if date or fallback else "UNRESOLVED"
        record["bin_source"] = "published_v1" if date else "published_current_fallback" if fallback else "unresolved"
        record["retrospective_exclusions"] = []
        if date is None or not datetime(2019, 1, 1, tzinfo=timezone.utc) <= date <= datetime(2019, 6, 30, 23, 59, 59, tzinfo=timezone.utc):
            record["retrospective_exclusions"].append("missing_invalid_or_out_of_window_published_v1")
        if "cs.SE" not in record["categories_current"]:
            record["retrospective_exclusions"].append("current_category_not_cs.SE")
        if record["published_current"] != record["published_at"]:
            record["retrospective_exclusions"].append("published_date_conflict")
        records.append(record)
    records.sort(key=lambda record: record["work_id"])
    months = {}
    for month in sorted({f"2019-{number:02d}" for number in range(1, 7)} | {record["bin"] for record in records}):
        inspected = [record for record in records if record["bin"] == month]
        count = len(inspected)
        fields = {}
        for field in FIELDS:
            missing = sum(record["field_status"][field] == "missing" for record in inspected)
            invalid = sum(record["field_status"][field] == "invalid" for record in inspected)
            fields[field] = {"missing": missing, "invalid": invalid, "inspected": count,
                             "missing_rate": missing / count if count else None,
                             "invalid_rate": invalid / count if count else None}
        months[month] = {"returned": count, "distinct_ids": count, "fields": fields,
                         "unresolved_v1": 0, "availability_unresolved": count, "missing_titles_are_nonmatches": False,
                         "retrospective_denominator": sum(not record["retrospective_exclusions"] for record in inspected),
                         "as_of_denominator": None, "share": None}
    excluded = [record for record in records if record["retrospective_exclusions"]]
    summary = {"status": "RETROSPECTIVE_AUDIT_ONLY", "query": config["query"], "cutoff": config["cutoff_probe"],
               "inputs": inputs, "audit_code_sha256": digest(Path(__file__).read_bytes()),
               "parser_code_sha256": digest(Path(acquire.__file__).read_bytes()),
               "reported_total": total, "current_records": len(current), "v1_records": len(versions),
               "duplicate_current_work_ids": len(current_ids) - len(set(current_ids)), "pages": pages,
               "current_query_completeness": "VERIFIED_AGAINST_FROZEN_RESPONSES_NOT_HISTORICAL_POPULATION",
               "months": months, "excluded_retrospective_work_ids": [record["work_id"] for record in excluded],
               "exclusion_reasons": dict(sorted(Counter(reason for record in excluded for reason in record["retrospective_exclusions"]).items())),
               "identity": {"revised_current_versions": sum(record["version_current"] > 1 for record in records),
                            "title_changes": sum(record["title_current"] != record["title_v1"] for record in records),
                            "category_changes": sum(record["categories_current"] != record["categories_v1"] for record in records),
                            "published_conflicts": sum(record["published_current"] != record["published_at"] for record in records),
                            "observed_version_scope": "current and v1 only; intermediate versions not acquired"},
               "temporal": {"E3": "NOT_PASSED", "field_public_availability": "UNRESOLVED",
                            "historical_membership": "UNRESOLVED", "vocabulary_state": "UNRESOLVED",
                            "published_is_available_at": False},
               "limitations": ["Current-category query cannot enumerate removed historical members.",
                               "Metadata schema/date validity is not independent evidence of public availability.",
                               "Missingness measured only inside the returned corpus, not all software testing literature.",
                               "No indicator, threshold, reference annotation or holdout evaluation performed."]}
    return records, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records, summary = audit(args.run.resolve())
    args.output.mkdir(parents=True, exist_ok=False)
    for name, content in (("normalized-records.json", records), ("audit.json", summary)):
        with (args.output / name).open("x", encoding="utf-8", newline="\n") as output:
            output.write(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": summary["status"], "records": len(records), "E3": summary["temporal"]["E3"]}))


if __name__ == "__main__":
    main()
