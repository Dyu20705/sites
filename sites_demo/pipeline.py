"""Verify F1 before importing its evaluator, then project and query exact evidence."""
from pathlib import Path
import re
import sys
from types import ModuleType
import xml.etree.ElementTree as ET

from .contracts import (DATA, F1_SHA, MONTHS, RESEARCH, RULE, SCOPE, WORK_RE,
                        DemoError, artifact, canonical, integer, local_path,
                        rational, read_json, require, sha, utc)


def verify_f1(root, manifest_path, expected_sha):
    raw = Path(manifest_path).read_bytes()
    require(expected_sha == F1_SHA and sha(raw) == expected_sha,
            "MANIFEST_DIGEST", "F1 differs from the accepted external anchor")
    manifest = read_json(raw)
    require(manifest["schema_version"] == 1 and manifest["freeze_id"] == "F1-M1-R-20261012-v1",
            "MANIFEST_DIGEST", "unsupported F1 identity")
    require(len(manifest["files"]) == 122, "MANIFEST_DIGEST", "expected all 122 F1 files")
    files = {}
    for name, spec in sorted(manifest["files"].items()):
        payload = local_path(root, name).read_bytes()
        require(sha(payload) == spec["sha256"], "ARTIFACT_DIGEST", name)
        files[name] = payload
    require(all(name in files for name in manifest["artifact_roles"].values()),
            "ARTIFACT_DIGEST", "unverified artifact role")
    return manifest, files


def load_evaluator(root):
    # Called only after all F1 bytes, including this complete import closure, match.
    directory = local_path(root, RESEARCH)
    names = ("acquire", "checks", "offline_audit", "signal_evaluator")
    for name in names:
        loaded = sys.modules.get(name)
        require(loaded is None or Path(loaded.__file__).resolve() == (directory / (name + ".py")).resolve(),
                "ARTIFACT_DIGEST", f"unexpected already-loaded research module: {name}")
    # Execute verified source, never an unverified __pycache__ bytecode file.
    for name in names:
        path = directory / (name + ".py")
        module = ModuleType(name)
        module.__file__ = str(path)
        sys.modules[name] = module
        exec(compile(path.read_bytes(), str(path), "exec"), module.__dict__)
    return sys.modules["signal_evaluator"]


def guard_records(records):
    require(isinstance(records, list), "IDENTITY_CONFLICT", "records must be a list")
    for record in records:
        require(isinstance(record, dict), "IDENTITY_CONFLICT", "record must be an object")
        categories = record.get("categories_current")
        require(isinstance(categories, list) and bool(categories)
                and all(isinstance(c, str) and bool(c.strip()) for c in categories)
                and len(categories) == len(set(categories)) and "cs.SE" in categories,
                "UNKNOWN_CATEGORY", f"current cs.SE membership invalid: {record.get('work_id')}")
        work, version = record.get("work_id"), record.get("version_id")
        require(isinstance(work, str) and WORK_RE.fullmatch(work) is not None
                and isinstance(version, str) and re.fullmatch(re.escape(work) + r"v[1-9][0-9]*", version),
                "IDENTITY_CONFLICT", "invalid work/version identity")


def evaluate_records(records, evaluator, **options):
    """The strict category boundary runs even for fixtures and diagnostic variants."""
    guard_records(records)
    try:
        return evaluator.evaluate(records, **options)
    except ValueError as error:
        raise DemoError("IDENTITY_CONFLICT", str(error)) from error


def project(root, manifest, files, records, evaluator):
    guard_records(records)
    require(len(records) == 598 and len({r["work_id"] for r in records}) == 598,
            "IDENTITY_CONFLICT", "expected 598 distinct works")
    require(sorted(r["version_id"] for r in records) == manifest["exposure"]["development_version_ids"],
            "IDENTITY_CONFLICT", "frozen population differs")
    acquisition = read_json(files[DATA + "/acquisition.json"])
    requests = {r["file"]: r for r in acquisition["requests"]}
    feeds, nodes = {}, {}
    works, bundles = [], {}
    for record in records:
        work = record["work_id"]
        require(record["version_id"] == work + "v1" and record["available_at"] is None
                and integer(record["version_current"], 1), "IDENTITY_CONFLICT", work)
        refs, excerpts = {}, {}
        for role in ("current", "v1"):
            ref = record["source_ref"][role]
            name = DATA + "/" + ref["file"]
            require(name in files and ref["file"].startswith("raw/" + role + "-"),
                    "RAW_LINEAGE", f"unverified role/file: {work}/{role}")
            payload = files[name]
            require(sha(payload) == ref["sha256"] and integer(ref["entry_index"]),
                    "RAW_LINEAGE", f"hash/index: {work}/{role}")
            if name not in feeds:
                require(b"<!DOCTYPE" not in payload.upper() and b"<!ENTITY" not in payload.upper(),
                        "RAW_LINEAGE", "XML declarations outside frozen Atom contract")
                feeds[name] = evaluator.acquire.read_entries(payload)[0]
                nodes[name] = ET.fromstring(payload).findall("{http://www.w3.org/2005/Atom}entry")
            index = ref["entry_index"]
            require(index < len(feeds[name]), "RAW_LINEAGE", f"index outside feed: {work}/{role}")
            entry = feeds[name][index]
            version = 1 if role == "v1" else record["version_current"]
            require(entry["id"] == ref["entry_id"]
                    and evaluator.offline_audit.identity(entry["id"]) == (work, version),
                    "RAW_LINEAGE", f"entry identity: {work}/{role}")
            expected = {"title": record["title_" + role], "categories": record["categories_" + role],
                        "published": record["published_at" if role == "v1" else "published_current"],
                        "updated": record["updated_at" if role == "v1" else "updated_current"]}
            require(all(entry[key] == value for key, value in expected.items()),
                    "RAW_LINEAGE", f"entry fields: {work}/{role}")
            request = requests[ref["file"]]
            acquired = utc(record["acquired_at"][role])
            require(acquired is not None and acquired == utc(request["ended_at"])
                    and request["sha256"] == ref["sha256"], "RAW_LINEAGE", f"acquisition: {work}/{role}")
            refs[role] = {"role": role, "artifact": artifact(name, payload, manifest["files"][name]["origin"]),
                          "entry_index": index, "entry_id": entry["id"], "acquired_at": acquired}
            excerpts[role] = ET.tostring(nodes[name][index], encoding="unicode")
        title = record["title_v1"]
        submitted, updated = utc(record["published_at"]), utc(record["updated_current"])
        title_status = "missing" if title is None or isinstance(title, str) and not title.strip() else "valid" if isinstance(title, str) else "invalid"
        event_status = "valid" if submitted else "missing" if not record["published_at"] else "invalid"
        require(title_status == event_status == "valid" and updated is not None
                and submitted[:7] == record["bin"] and record["bin"] in MONTHS
                and record["bin_source"] == "published_v1" and not record["retrospective_exclusions"],
                "RAW_LINEAGE", f"closed-population field contract: {work}")
        projected = {"work_id": work, "version_id": work + "v1", "current_version": record["version_current"],
                     "title_v1": title, "title_current": record["title_current"],
                     "categories_v1": record["categories_v1"], "categories_current": record["categories_current"],
                     "submitted_v1_at": submitted, "updated_current_at": updated,
                     "available_at": None, "event_month": record["bin"],
                     "title_status": title_status, "event_status": event_status, "category_status": "valid",
                     "current_ref": refs["current"], "v1_ref": refs["v1"]}
        works.append(projected)
        bundles[work] = {"work": projected, "rule_id": RULE, "freeze_id": manifest["freeze_id"],
                         "freeze_sha256": F1_SHA, "contract_version": manifest["contract"]["version"],
                         "current_entry_text": excerpts["current"], "v1_entry_text": excerpts["v1"]}
    audited, _ = evaluator.offline_audit.audit(local_path(root, DATA))
    require(audited == records, "RAW_LINEAGE", "raw audit differs from frozen normalized records")
    return sorted(works, key=lambda w: w["work_id"]), bundles


def point(row, unassigned):
    n, total, known = row["count"], row["eligible_works"], row["known_matches"]
    return {"rule_id": RULE, "months": [row["month"]], "n": n, "N": total, "known_matches": known,
            "share": rational(n, total), "lower_share": rational(known, total),
            "upper_share": rational(known + len(row["unknown_title_ids"]), total), "status": row["status"],
            "denominator_ids": sorted(row["denominator_ids"]), "matched_ids": sorted(row["matched_ids"]),
            "unknown_title_ids": sorted(row["unknown_title_ids"]), "unassigned_work_ids": sorted(unassigned)}


def query(points, concept, start, end):
    require(concept == "fuzzing" and start in MONTHS and end in MONTHS and start <= end,
            "INVALID_QUERY", "use fuzzing and an ordered range within 2019-01..2019-06")
    rows = [p for p in points if start <= p["months"][0] <= end]
    require([p["months"][0] for p in rows] == list(MONTHS[MONTHS.index(start):MONTHS.index(end) + 1]),
            "INVALID_SIGNAL", "missing or duplicate month")
    pooled = {"rule_id": RULE, "months": [p["months"][0] for p in rows]}
    for field in ("denominator_ids", "matched_ids", "unknown_title_ids", "unassigned_work_ids"):
        pooled[field] = sorted({work for row in rows for work in row[field]})
    total = sum(p["N"] for p in rows) if all(p["N"] is not None for p in rows) else None
    n = sum(p["n"] for p in rows) if all(p["n"] is not None for p in rows) else None
    known = sum(p["known_matches"] for p in rows)
    pooled.update(n=n, N=total, known_matches=known, share=rational(n, total),
                  lower_share=rational(known, total), upper_share=rational(known + len(pooled["unknown_title_ids"]), total),
                  status="UNRESOLVED_EVENT_TIME" if total is None else "UNRESOLVED_TITLE" if n is None else "UNDEFINED_EMPTY_BIN" if total == 0 else "DEFINED")
    return {"concept": concept, "start": start, "end": end, "monthly": rows, "pooled": pooled,
            "evidence_ids": pooled["denominator_ids"], "freeze_sha256": F1_SHA, "claim_scope": SCOPE}


def prepare(root, manifest_path, expected_sha=F1_SHA):
    manifest, files = verify_f1(root, manifest_path, expected_sha)
    roles = manifest["artifact_roles"]
    records = read_json(files[roles["normalized"]])
    # Validate malformed categories before any evaluator call or research audit.
    guard_records(records)
    evaluator = load_evaluator(root)
    works, bundles = project(root, manifest, files, records, evaluator)
    primary = evaluate_records(records, evaluator)
    oracle = read_json(files[roles["measurements"]])
    require(primary == oracle["result"], "ORACLE_MISMATCH", "primary frozen result")
    declaration = read_json(files[roles["declaration"]])
    variants = {
        "archived_literal_transport_diagnostic": evaluate_records(records, evaluator, pattern=declaration["archived_literal_pattern"]),
        "exact_fuzzing": evaluate_records(records, evaluator, pattern=r"\bfuzzing\b"),
        "current_title_diagnostic": evaluate_records(records, evaluator, title_field="title_current"),
        "v1_category_subset": evaluate_records(records, evaluator, require_v1_category=True),
        "exclude_nine_late_ids_diagnostic_not_as_of": evaluate_records(records, evaluator, exclude_late_ids=True),
    }
    compact = {name: {"months": [{key: row[key] for key in ("month", "count", "eligible_works", "share", "title_missing", "title_invalid")} for row in value["months"]],
                      "matched_ids": [r["work_id"] for r in value["matches"]], "excluded": value["excluded"]}
               for name, value in variants.items()}
    require(compact == oracle["sensitivity"] and evaluator.bimonth(primary["months"]) == oracle["adjacent_bimonth"],
            "ORACLE_MISMATCH", "declared sensitivities")
    require(all(c["status"] == "PASS" for c in evaluator.controlled_checks()), "ORACLE_MISMATCH", "frozen controls")
    matched = {r["work_id"] for r in primary["matches"]}
    for work, bundle in bundles.items():
        bundle.update(matched=work in matched, contribution="MATCH" if work in matched else "NONMATCH")
    points = [point(r, [u["work_id"] for u in primary["unassigned"]]) for r in primary["months"]]
    windows = [query(points, "fuzzing", start, end) for start in MONTHS for end in MONTHS if start <= end]
    sensitivity = {name: {"points": [point(row, [u["work_id"] for u in value["unassigned"]]) for row in value["months"]],
                          "matched_ids": sorted(r["work_id"] for r in value["matches"]), "excluded": value["excluded"]}
                   for name, value in variants.items()}
    sensitivity["adjacent_bimonth"] = [query(points, "fuzzing", MONTHS[i], MONTHS[i + 1])["pooled"] for i in (0, 2, 4)]
    return {"manifest": manifest, "files": files, "works": works, "bundles": bundles,
            "points": points, "windows": windows, "sensitivities": sensitivity}


def product_inventory(root):
    names = ["sites_demo/" + n for n in ("__init__.py", "contracts.py", "pipeline.py", "render.py", "__main__.py")]
    names += ["tests/test_demo.py"]
    return [artifact(name, local_path(root, name).read_bytes()) for name in sorted(names)]


def product_digest(root):
    return sha(canonical([[a["path"], a["sha256"]] for a in product_inventory(root)]))
