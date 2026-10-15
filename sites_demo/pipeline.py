from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import sysconfig
import time
import xml.etree.ElementTree as ET

from .contracts import (ArtifactRef, ContractError, DemoError, SignalPoint, SourceRef, VerifiedInputs, Work,
                        canonical_json, load_json_strict, require_exact_keys, require_sha,
                        validate_local_path)

F1_DIGEST = "bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a"
D09_DIGEST = "a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc"
RULE_ID = "RE-20260927-01-documented-word-boundary-v1"
RULE_PATTERN = r"\bfuzz(?:ing|er|ers)?\b"
MONTHS = tuple(f"2019-{month:02d}" for month in range(1, 7))
CLAIM_SCOPE = "OBSERVED_RETROSPECTIVE_LEXICAL_PREVALENCE"
NS = {"a": "http://www.w3.org/2005/Atom"}
NORMALIZED_KEYS = {"acquired_at", "availability_status", "available_at", "bin", "bin_source",
                   "categories_current", "categories_v1", "field_status", "published_at",
                   "published_current", "retrospective_exclusions", "source_ref", "title_current",
                   "title_v1", "updated_at", "updated_current", "validation_status",
                   "version_current", "version_id", "work_id"}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _require(condition, code, message):
    if not condition:
        raise DemoError(code, message)


def _utc(value, label, nullable=False):
    if value is None and nullable:
        return None
    _require(isinstance(value, str), "RAW_LINEAGE", f"{label} must be UTC text")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise DemoError("RAW_LINEAGE", f"invalid {label}") from error
    _require(parsed.tzinfo is not None, "RAW_LINEAGE", f"{label} lacks timezone")
    return parsed


def _entry_value(entry, name):
    value = entry.findtext(f"a:{name}", namespaces=NS)
    return value


def _entry_title(entry):
    value = _entry_value(entry, "title")
    return " ".join(value.split()) if value is not None else None


SCHEMA_IDENTITIES = {
    "artifact": "ArtifactRef-v1",
    "source": "SourceRef-v1",
    "work": "Work-v1",
    "signal_point": "SignalPoint-v1",
    "evidence_bundle": "EvidenceBundle-v1",
    "query_result": "QueryResult-v1",
    "semantic_index": "SemanticIndex-v1",
    "execution_record": "ExecutionRecord-v1",
}
INTERPRETATION_TASKS = [
    "select_rule_and_range",
    "state_n_N_and_share",
    "distinguish_observed_2026_from_event_2019",
    "distinguish_lexical_from_semantic",
    "reject_trend_and_historical_as_of_inference",
]
DEVELOPMENT_CLAIM = "Development execution only; not independent review, E7, E8, or scientific quality."
INDEPENDENT_CLAIM = (
    "Independent product-task evidence only; no original E3, directional, causal, forecasting, "
    "or scientific-quality claim."
)


def _strict_evaluation(value, root, manifest):
    top = {"schema_version", "evaluation_id", "mode", "d09", "f1", "product", "reviewer",
           "runtime_profile", "runtime_profile_sha256", "schemas", "tasks", "controls",
           "limits", "claim"}
    require_exact_keys(value, top, "evaluation")
    _require(value["schema_version"] == 1, "RUNTIME_PROFILE", "unknown evaluation schema")
    _require(isinstance(value["evaluation_id"], str) and value["evaluation_id"].startswith("D09-EVAL-v1"),
             "RUNTIME_PROFILE", "unknown evaluation identity")
    _require(value["mode"] in {"DEVELOPMENT_ONLY", "INDEPENDENT"}, "RUNTIME_PROFILE", "unknown evaluation mode")
    require_exact_keys(value["d09"], {"version", "sha256", "acceptance_url"}, "evaluation.d09")
    _require(value["d09"]["version"] == "D09-M1-20261012-v1" and value["d09"]["sha256"] == D09_DIGEST,
             "RUNTIME_PROFILE", "wrong D09 identity")
    _require(value["d09"]["acceptance_url"] ==
             "https://github.com/Dyu20705/sites/issues/71#issuecomment-6123995295",
             "RUNTIME_PROFILE", "wrong D09 acceptance URL")
    require_exact_keys(value["f1"], {"id", "sha256"}, "evaluation.f1")
    _require(value["f1"] == {"id": "F1-M1-R-20261012-v1", "sha256": F1_DIGEST},
             "RUNTIME_PROFILE", "wrong F1 identity")
    require_exact_keys(value["product"], {"commit", "code_sha256"}, "evaluation.product")
    _require(value["product"] == product_identity(root), "RUNTIME_PROFILE", "product identity differs")
    require_exact_keys(value["reviewer"], {"identity", "role", "prior_exposure", "independent"}, "evaluation.reviewer")
    if value["mode"] == "INDEPENDENT":
        _require(value["reviewer"]["independent"] is True and isinstance(value["reviewer"]["identity"], str)
                 and value["reviewer"]["identity"].strip()
                 and value["reviewer"]["role"] == "INDEPENDENT_REVIEWER"
                 and value["reviewer"]["prior_exposure"] == "NONE",
                 "RUNTIME_PROFILE", "independent reviewer identity/exposure required")
    else:
        _require(value["reviewer"] == {"identity": None, "role": "AUTOMATED_DEVELOPMENT_CHECK",
                                      "prior_exposure": "FULL", "independent": False},
                 "RUNTIME_PROFILE", "development reviewer boundary differs")
    profile_sha = require_sha(value["runtime_profile_sha256"], "runtime_profile_sha256")
    _require(sha(canonical_json(value["runtime_profile"])) == profile_sha,
             "RUNTIME_PROFILE", "runtime profile digest mismatch")
    observed = runtime_identity()
    require_exact_keys(value["runtime_profile"], set(observed), "evaluation.runtime_profile")
    for key in observed:
        if key != "browser":
            _require(value["runtime_profile"][key] == observed[key],
                     "RUNTIME_PROFILE", f"runtime profile differs: {key}")
    _require(value["schemas"] == SCHEMA_IDENTITIES,
             "RUNTIME_PROFILE", "schema identities differ")
    expected_tasks = {
        "interpretation_items": INTERPRETATION_TASKS,
        "navigation": {"open_match": True, "open_nonmatch": True},
        "replay": {"builds": 2, "semantic_compare": True},
    }
    _require(value["tasks"] == expected_tasks,
             "RUNTIME_PROFILE", "review tasks differ")
    controls_path = manifest["artifact_roles"]["controls"]
    expected_controls = {
        "control_artifact": {"path": controls_path,
                             "sha256": manifest["files"][controls_path]["sha256"]},
        "sensitivity_names": manifest["sensitivities"],
    }
    _require(value["controls"] == expected_controls,
             "RUNTIME_PROFILE", "control/sensitivity identities differ")
    require_exact_keys(value["limits"], {"works", "seconds", "peak_process_bytes", "network_requests"}, "evaluation.limits")
    _require(value["limits"] == {"works": 598, "seconds": 60, "peak_process_bytes": 268435456,
                                  "network_requests": 0}, "RUNTIME_PROFILE", "resource contract differs")
    expected_claim = INDEPENDENT_CLAIM if value["mode"] == "INDEPENDENT" else DEVELOPMENT_CLAIM
    _require(value["claim"] == expected_claim, "RUNTIME_PROFILE", "claim boundary differs")
    if value["mode"] == "INDEPENDENT":
        profile = value["runtime_profile"]
        browser = profile["browser"]
        _require(profile["python"] == "3.14.7" and profile["implementation"] == "CPython"
                 and profile["pointer_bits"] == 64 and profile["os"] == "Windows"
                 and profile["os_release"] == "11"
                 and profile["machine"] in {"AMD64", "x86_64"}
                 and isinstance(profile["ram_bytes"], int)
                 and 15 * 1024**3 <= profile["ram_bytes"] <= 17 * 1024**3
                 and isinstance(profile["processor"], str) and profile["processor"].strip()
                 and isinstance(profile["cpu_count"], int) and profile["cpu_count"] > 0
                 and isinstance(browser, str)
                 and re.fullmatch(r"[A-Za-z][A-Za-z0-9]*(?:[ _-][A-Za-z0-9][A-Za-z0-9]*)* "
                                  r"\d+(?:\.\d+){1,4}(?: \(64-bit\))?", browser.strip())
                 and not any(token in browser.casefold()
                             for token in ("unknown", "placeholder", "recorded browser", "not recorded")),
                 "RUNTIME_PROFILE", "independent target profile is incomplete or not accepted")


def _contained(root: Path, relative: str) -> Path:
    try:
        validate_local_path(relative)
    except ContractError as error:
        raise DemoError("ARTIFACT_DIGEST", str(error)) from error
    path = root / relative
    _require(path.resolve().is_relative_to(root), "ARTIFACT_DIGEST", f"artifact escapes root: {relative}")
    return path


def _verify_artifacts(root, manifest):
    rows = {}
    for relative, spec in sorted(manifest["files"].items()):
        require_exact_keys(spec, {"origin", "sha256"}, f"manifest.files[{relative}]")
        path = _contained(root, relative)
        try:
            raw = path.read_bytes()
        except OSError as error:
            raise DemoError("ARTIFACT_DIGEST", f"cannot read {relative}") from error
        _require(sha(raw) == spec["sha256"], "ARTIFACT_DIGEST", f"hash mismatch: {relative}")
        _require(spec["origin"] in {"research_source", "freeze_support"}, "ARTIFACT_DIGEST", "unknown origin")
        rows[relative] = raw
    return rows


def _source_ref(root, run_dir, manifest, record, role, xml_cache, raw_entries, raw_artifacts):
    ref = record["source_ref"][role]
    require_exact_keys(ref, {"entry_id", "entry_index", "file", "sha256"}, f"source_ref.{role}")
    _require(isinstance(ref["entry_index"], int) and not isinstance(ref["entry_index"], bool)
             and ref["entry_index"] >= 0, "RAW_LINEAGE", "entry index invalid")
    relative = (run_dir.relative_to(root) / validate_local_path(ref["file"])).as_posix()
    _require(relative in manifest["files"] and manifest["files"][relative]["sha256"] == ref["sha256"],
             "RAW_LINEAGE", f"unfrozen source ref: {relative}")
    raw = (root / relative).read_bytes()
    _require(sha(raw) == ref["sha256"], "RAW_LINEAGE", f"raw hash mismatch: {relative}")
    if relative not in xml_cache:
        try:
            xml_cache[relative] = ET.fromstring(raw).findall("a:entry", NS)
        except ET.ParseError as error:
            raise DemoError("RAW_LINEAGE", f"invalid Atom: {relative}") from error
    entries = xml_cache[relative]
    _require(ref["entry_index"] < len(entries), "RAW_LINEAGE", "entry index outside artifact")
    entry = entries[ref["entry_index"]]
    _require(_entry_value(entry, "id") == ref["entry_id"], "RAW_LINEAGE", "entry ID/index disagreement")
    raw_entries[(relative, ref["entry_index"])] = ET.tostring(entry, encoding="unicode")
    raw_artifacts[relative] = raw
    acquired = record["acquired_at"][role]
    acquired = _utc(acquired, f"acquired_at.{role}").astimezone(timezone.utc).isoformat()
    acquired = acquired.replace("+00:00", "Z")
    artifact = ArtifactRef(relative, ref["sha256"], len(raw), manifest["files"][relative]["origin"])
    return SourceRef(role, artifact, ref["entry_index"], ref["entry_id"], acquired), entry


def _validate_record(root, run_dir, manifest, record, xml_cache, raw_entries, raw_artifacts):
    require_exact_keys(record, NORMALIZED_KEYS, "normalized record")
    work_id, version_id = record["work_id"], record["version_id"]
    _require(isinstance(work_id, str) and re.fullmatch(r"\d{4}\.\d{4,5}", work_id),
             "IDENTITY_CONFLICT", "invalid work ID")
    _require(version_id == work_id + "v1", "IDENTITY_CONFLICT", "version is not exact v1")
    _require(isinstance(record["version_current"], int) and not isinstance(record["version_current"], bool)
             and record["version_current"] >= 1, "IDENTITY_CONFLICT", "invalid current version")
    require_exact_keys(record["source_ref"], {"current", "v1"}, "source_ref")
    require_exact_keys(record["acquired_at"], {"current", "v1"}, "acquired_at")
    v1_ref, v1 = _source_ref(root, run_dir, manifest, record, "v1", xml_cache, raw_entries, raw_artifacts)
    current_ref, current = _source_ref(root, run_dir, manifest, record, "current", xml_cache, raw_entries, raw_artifacts)
    _require(v1_ref.entry_id.endswith("/" + version_id), "IDENTITY_CONFLICT", "v1 entry identity differs")
    current_suffix = f"/{work_id}v{record['version_current']}"
    _require(current_ref.entry_id.endswith(current_suffix), "IDENTITY_CONFLICT", "current entry identity differs")
    v1_categories = tuple(sorted(node.get("term") for node in v1.findall("a:category", NS)))
    current_categories = tuple(sorted(node.get("term") for node in current.findall("a:category", NS)))
    _require(record["categories_v1"] == list(v1_categories) and record["categories_current"] == list(current_categories),
             "RAW_LINEAGE", "category projection differs")
    _require("cs.SE" in current_categories, "UNKNOWN_CATEGORY", "current cs.SE membership missing")
    _require(record["title_v1"] == _entry_title(v1) and record["title_current"] == _entry_title(current),
             "RAW_LINEAGE", "title projection differs")
    _require(record["published_at"] == _entry_value(v1, "published")
             and record["published_current"] == _entry_value(current, "published")
             and record["updated_current"] == _entry_value(current, "updated"),
             "RAW_LINEAGE", "date projection differs")
    event = _utc(record["published_at"], "published_at", nullable=True)
    event_status = "missing" if record["published_at"] is None else "valid" if event is not None else "invalid"
    month = event.astimezone(timezone.utc).strftime("%Y-%m") if event else None
    _require(month == record["bin"] and month in MONTHS, "RAW_LINEAGE", "event bin differs")
    _require(record["available_at"] is None and record["retrospective_exclusions"] == [],
             "RAW_LINEAGE", "closed corpus boundary differs")
    _require(all(value == "valid" for value in record["field_status"].values()),
             "RAW_LINEAGE", "real F1 fields must be valid")
    title_status = "missing" if record["title_v1"] is None or not record["title_v1"].strip() else "valid"
    return Work(work_id, version_id, record["version_current"], record["title_v1"], record["title_current"],
                v1_categories, current_categories, record["published_at"], record["updated_current"], None,
                month, title_status, event_status, "valid", v1_ref, current_ref)


def verify_inputs(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha):
    root = Path(root).resolve()
    f1_path, evaluation = Path(f1_path).resolve(), Path(evaluation).resolve()
    _require(f1_path.is_relative_to(root), "MANIFEST_DIGEST", "F1 must be inside source root")
    require_sha(expected_f1_sha, "expected_f1_sha")
    require_sha(expected_evaluation_sha, "expected_evaluation_sha")
    _require(sha(f1_path.read_bytes()) == expected_f1_sha == F1_DIGEST,
             "MANIFEST_DIGEST", "F1 differs from external anchor")
    _require(sha(evaluation.read_bytes()) == expected_evaluation_sha,
             "RUNTIME_PROFILE", "evaluation differs from external anchor")
    try:
        manifest, evaluation_value = load_json_strict(f1_path), load_json_strict(evaluation)
    except ContractError as error:
        raise DemoError("MANIFEST_DIGEST", str(error)) from error
    _require(manifest["freeze_id"] == "F1-M1-R-20261012-v1" and manifest["schema_version"] == 1,
             "MANIFEST_DIGEST", "unknown F1 identity")
    _strict_evaluation(evaluation_value, root, manifest)
    _verify_artifacts(root, manifest)
    normalized_path = _contained(root, manifest["artifact_roles"]["normalized"])
    records = load_json_strict(normalized_path)
    _require(isinstance(records, list) and len(records) == 598, "IDENTITY_CONFLICT", "population is not 598")
    run_dir = normalized_path.parents[1]
    xml_cache, raw_entries, raw_artifacts, works = {}, {}, {}, []
    for record in records:
        try:
            works.append(_validate_record(root, run_dir, manifest, record, xml_cache, raw_entries, raw_artifacts))
        except ContractError as error:
            raise DemoError("RAW_LINEAGE", str(error)) from error
    ids = [work.work_id for work in works]
    _require(len(ids) == len(set(ids)) == 598 and ids == sorted(ids), "IDENTITY_CONFLICT", "IDs duplicate or unsorted")
    _require([work.version_id for work in works] == manifest["exposure"]["development_version_ids"],
             "IDENTITY_CONFLICT", "F1 exposure register differs")
    return VerifiedInputs(root, f1_path, manifest, evaluation_value, expected_evaluation_sha,
                          tuple(records), tuple(works), raw_entries, raw_artifacts)


def project(inputs: VerifiedInputs) -> tuple[Work, ...]:
    return inputs.projected_works


@lru_cache(maxsize=1)
def _evaluator():
    project_root = Path(__file__).resolve().parents[1]
    path = project_root / "experiments/research_exit_20260927"
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
    return importlib.import_module("signal_evaluator")


def _record(work: Work):
    return {"work_id": work.work_id, "version_id": work.version_id, "title_v1": work.title_v1,
            "title_current": work.title_current, "published_at": work.submitted_v1_at,
            "categories_current": list(work.categories_current), "categories_v1": list(work.categories_v1),
            "available_at": work.available_at,
            "source_ref": {"v1": work.v1_ref.evaluator_dict(), "current": work.current_ref.evaluator_dict()},
            "retrospective_exclusions": []}


def _ratio(n, denominator):
    return None if n is None or denominator is None or denominator == 0 else {"numerator": n, "denominator": denominator}


def measure(works: tuple[Work, ...]) -> tuple[SignalPoint, ...]:
    raw = _evaluator().evaluate([_record(work) for work in works], pattern=RULE_PATTERN)
    unassigned = tuple(sorted(row["work_id"] for row in raw["unassigned"]))
    points = []
    for row in raw["months"]:
        N, n = row["eligible_works"], row["count"]
        unknown = tuple(row["unknown_title_ids"])
        lower = _ratio(row["known_matches"], N)
        upper = _ratio(row["known_matches"] + len(unknown), N)
        points.append(SignalPoint(RULE_ID, (row["month"],), n, N, row["known_matches"], _ratio(n, N),
                                  lower, upper, row["status"], tuple(row["denominator_ids"]),
                                  tuple(row["matched_ids"]), unknown, unassigned))
    return tuple(points)


def _pooled(points):
    months = tuple(month for point in points for month in point.months)
    denominators = tuple(sorted({work for point in points for work in point.denominator_ids}))
    matches = tuple(sorted({work for point in points for work in point.matched_ids}))
    unknown = tuple(sorted({work for point in points for work in point.unknown_title_ids}))
    unassigned = tuple(sorted({work for point in points for work in point.unassigned_work_ids}))
    known = sum(point.known_matches for point in points)
    if unassigned:
        status, n, N = "UNRESOLVED_EVENT_TIME", None, None
    else:
        N = sum(point.N or 0 for point in points)
        if unknown:
            status, n = "UNRESOLVED_TITLE", None
        elif N == 0:
            status, n = "UNDEFINED_EMPTY_BIN", 0
        else:
            status, n = "DEFINED", sum(point.n or 0 for point in points)
    return SignalPoint(RULE_ID, months, n, N, known, _ratio(n, N), _ratio(known, N),
                       _ratio(known + len(unknown), N), status, denominators, matches, unknown, unassigned)


def query(monthly, works, concept="fuzzing", start=None, end=None):
    if concept != "fuzzing" or start not in MONTHS or end not in MONTHS or MONTHS.index(start) > MONTHS.index(end):
        raise DemoError("INVALID_QUERY", "only contiguous 2019-01..2019-06 fuzzing windows are valid")
    selected = tuple(monthly[MONTHS.index(start):MONTHS.index(end) + 1])
    pooled = _pooled(selected)
    evidence_ids = sorted(set(pooled.denominator_ids) | set(pooled.unassigned_work_ids))
    return {"concept": concept, "start": start, "end": end,
            "monthly": [point.logical_dict() for point in selected], "pooled": pooled.logical_dict(),
            "evidence_ids": evidence_ids, "freeze_sha256": F1_DIGEST, "claim_scope": CLAIM_SCOPE}


def evidence(work_id, inputs: VerifiedInputs, works):
    by_id = {work.work_id: work for work in works}
    if work_id not in by_id:
        raise DemoError("IDENTITY_CONFLICT", f"unknown work: {work_id}")
    work = by_id[work_id]
    matched = None if work.title_status != "valid" else bool(re.search(RULE_PATTERN, work.title_v1, re.IGNORECASE))
    contribution = "UNASSIGNED_EVENT" if work.event_status != "valid" else "UNKNOWN_TITLE" if matched is None else "MATCH" if matched else "NONMATCH"
    return {"work": work.logical_dict(), "rule_id": RULE_ID, "matched": matched, "contribution": contribution,
            "freeze_id": "F1-M1-R-20261012-v1", "freeze_sha256": F1_DIGEST,
            "contract_version": "M1-R-20261010-v1",
            "current_entry_text": inputs.raw_entry_text[(work.current_ref.artifact.path, work.current_ref.entry_index)],
            "v1_entry_text": inputs.raw_entry_text[(work.v1_ref.artifact.path, work.v1_ref.entry_index)]}


def _variant_outputs(works):
    evaluator, records = _evaluator(), [_record(work) for work in works]
    raw = {
        "archived_literal_transport_diagnostic": evaluator.evaluate(records, RULE_PATTERN),
        "exact_fuzzing": evaluator.evaluate(records, r"\bfuzzing\b"),
        "current_title_diagnostic": evaluator.evaluate(records, title_field="title_current"),
        "v1_category_subset": evaluator.evaluate(records, require_v1_category=True),
        "exclude_nine_late_ids_diagnostic_not_as_of": evaluator.evaluate(records, exclude_late_ids=True)}
    return {name: {"months": [{key: row[key] for key in ("month", "count", "eligible_works", "share", "title_missing", "title_invalid")}
                              for row in result["months"]],
                   "matched_ids": [row["work_id"] for row in result["matches"]], "excluded": result["excluded"]}
            for name, result in raw.items()}


def _sensitivity_outputs(works):
    evaluator = _evaluator()
    primary = evaluator.evaluate([_record(work) for work in works], pattern=RULE_PATTERN)
    return {
        "variants": _variant_outputs(works),
        "adjacent_bimonth": evaluator.bimonth(primary["months"]),
    }


def _validate_oracles(inputs, works, points, sensitivities):
    oracle = load_json_strict(_contained(inputs.root, inputs.manifest["artifact_roles"]["measurements"]))
    rows = oracle["result"]["months"]
    for point, row in zip(points, rows, strict=True):
        _require((point.n, point.N, list(point.denominator_ids), list(point.matched_ids)) ==
                 (row["count"], row["eligible_works"], row["denominator_ids"], row["matched_ids"]),
                 "IDENTITY_CONFLICT", f"primary oracle differs: {point.months[0]}")
    _require(sensitivities["variants"] == oracle["sensitivity"],
             "IDENTITY_CONFLICT", "variant oracle differs")
    _require(sensitivities["adjacent_bimonth"] == oracle["adjacent_bimonth"],
             "IDENTITY_CONFLICT", "adjacent bimonth oracle differs")


def product_identity(root):
    root = Path(root).resolve()
    paths = sorted((root / "sites_demo").glob("*.py"))
    rows = [[path.relative_to(root).as_posix(), sha(path.read_bytes())] for path in paths]
    try:
        commit = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True,
                                         stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "UNAVAILABLE"
    return {"commit": commit, "code_sha256": sha(canonical_json(rows))}


def _ram_bytes():
    if os.name == "nt":
        import ctypes
        class MemoryStatus(ctypes.Structure):
            _fields_ = [("length", ctypes.c_ulong), ("memory_load", ctypes.c_ulong),
                        ("total_physical", ctypes.c_ulonglong), ("available_physical", ctypes.c_ulonglong),
                        ("total_page_file", ctypes.c_ulonglong), ("available_page_file", ctypes.c_ulonglong),
                        ("total_virtual", ctypes.c_ulonglong), ("available_virtual", ctypes.c_ulonglong),
                        ("available_extended_virtual", ctypes.c_ulonglong)]
        status = MemoryStatus()
        status.length = ctypes.sizeof(status)
        return int(status.total_physical) if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)) else None
    try:
        return int(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES"))
    except (AttributeError, OSError, ValueError):
        return None


@lru_cache(maxsize=8)
def runtime_identity(browser="NOT_RECORDED_CANDIDATE"):
    executable = Path(sys.executable).resolve()
    stdlib = Path(sysconfig.get_paths()["stdlib"])
    rows = []
    if stdlib.is_dir():
        for path in sorted(stdlib.rglob("*")):
            if (path.is_file() and path.suffix.lower() in {".py", ".pyd", ".so", ".dll", ".zip"}
                    and "site-packages" not in path.parts and "__pycache__" not in path.parts):
                rows.append([path.relative_to(stdlib).as_posix(), sha(path.read_bytes())])
    return {"python": platform.python_version(), "implementation": platform.python_implementation(),
            "cache_tag": sys.implementation.cache_tag, "platform": platform.platform(),
            "os": platform.system(), "os_release": platform.release(), "machine": platform.machine(),
            "processor": platform.processor(), "pointer_bits": 64 if sys.maxsize > 2**32 else 32,
            "executable_sha256": sha(executable.read_bytes()), "stdlib_native_file_count": len(rows),
            "stdlib_native_tree_sha256": sha(canonical_json(rows)), "cpu_count": os.cpu_count(),
            "browser": browser, "ram_bytes": _ram_bytes(),
            "scope": "Prospective candidate profile; not approval, hermetic image, browser task, E7 or E8."}


def _peak_windows_bytes():
    if os.name != "nt":
        return None, "NOT_MEASURED_NON_WINDOWS_D09_BOUNDARY"
    import ctypes
    from ctypes import wintypes
    class Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]
    counters = Counters(); counters.cb = ctypes.sizeof(counters)
    ok = ctypes.windll.psapi.GetProcessMemoryInfo(ctypes.windll.kernel32.GetCurrentProcess(),
                                                  ctypes.byref(counters), counters.cb)
    return (int(counters.PeakWorkingSetSize), "Windows GetProcessMemoryInfo PeakWorkingSetSize") if ok else (None, "WINDOWS_MEASUREMENT_FAILED")


def _write_synced(path: Path, raw: bytes):
    with path.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def _sync_output_files(directory: Path):
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        with path.open("rb") as stream:
            os.fsync(stream.fileno())


def _build_worker(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha, out,
                  *, write_complete):
    from .render import render, render_sensitivities
    root, out = Path(root).resolve(), Path(out)
    if out.exists() or out.is_symlink():
        raise DemoError("OUTPUT_EXISTS", f"refusing existing destination: {out}")
    started_utc, started = datetime.now(timezone.utc).isoformat(), time.perf_counter()
    inputs = verify_inputs(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha)
    works, points = project(inputs), None
    points = measure(works)
    sensitivities = _sensitivity_outputs(works)
    _validate_oracles(inputs, works, points, sensitivities)
    queries = [query(points, works, "fuzzing", start, end)
               for i, start in enumerate(MONTHS) for end in MONTHS[i:]]
    bundles = [evidence(work.work_id, inputs, works) for work in works]
    artifacts = render(queries, bundles)
    artifacts["data/sensitivities.json"] = canonical_json(sensitivities)
    artifacts["sensitivities.html"] = render_sensitivities(sensitivities)
    seen_names = {}
    for relative, raw in inputs.raw_artifacts.items():
        name = Path(relative).name
        if name in seen_names and seen_names[name] != sha(raw):
            raise DemoError("RAW_LINEAGE", f"raw basename collision: {name}")
        seen_names[name] = sha(raw)
        artifacts[f"raw/{name}"] = raw
    out.mkdir(parents=True, exist_ok=False)
    for relative, raw in sorted(artifacts.items()):
        target = out / validate_local_path(relative)
        _require(target.resolve().is_relative_to(out.resolve()), "OUTPUT_EXISTS", "output path escape")
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)
    identity = product_identity(root)
    refs = [{"path": path, "sha256": sha(raw), "size_bytes": len(raw),
             "origin": "research_source" if path.startswith("raw/") else "product"}
            for path, raw in sorted(artifacts.items())]
    semantic = sha(canonical_json([[row["path"], row["sha256"]] for row in refs]))
    index = {"schema_version": 1, "freeze_sha256": F1_DIGEST, "product_commit": identity["commit"],
             "product_code_sha256": identity["code_sha256"], "artifacts": refs, "semantic_sha256": semantic}
    (out / "semantic-index.json").write_bytes(canonical_json(index))
    _verify_artifacts(root, inputs.manifest)
    elapsed = time.perf_counter() - started
    peak, memory_method = _peak_windows_bytes()
    errors = []
    if elapsed > inputs.evaluation["limits"]["seconds"]:
        errors.append("BUDGET_EXCEEDED")
    if peak is None:
        errors.append("MEMORY_NOT_MEASURED")
    elif peak > inputs.evaluation["limits"]["peak_process_bytes"]:
        errors.append("BUDGET_EXCEEDED")
    status = "FAIL" if "BUDGET_EXCEEDED" in errors else "NOT_MEASURED" if errors else "PASS"
    execution = {"schema_version": 1, "evaluation_sha256": inputs.evaluation_sha256,
                 "semantic_sha256": semantic,
                 "runtime_profile_sha256": inputs.evaluation["runtime_profile_sha256"],
                 "started_utc": started_utc, "ended_utc": datetime.now(timezone.utc).isoformat(),
                 "argv": list(sys.argv), "elapsed_seconds": elapsed, "peak_process_bytes": peak,
                 "memory_method": memory_method, "status": status, "error_codes": errors}
    (out / "execution.json").write_bytes(canonical_json(execution))
    if status == "FAIL":
        raise DemoError("BUDGET_EXCEEDED", "resource budget exceeded; output remains incomplete")
    if write_complete:
        (out / "COMPLETE").write_bytes(canonical_json({"semantic_sha256": semantic, "status": status}))
    return execution


def build(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha, out):
    return launch_build(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha, out)


def launch_build(root, f1_path, expected_f1_sha, evaluation, expected_evaluation_sha, out):
    """Run one build in a fresh worker and finalize its outer-process E8 record."""
    root, out = Path(root).resolve(), Path(out)
    if out.exists() or out.is_symlink():
        raise DemoError("OUTPUT_EXISTS", f"refusing existing destination: {out}")
    out = out.resolve()
    started_utc, started = datetime.now(timezone.utc).isoformat(), time.perf_counter()
    command = [
        sys.executable, "-m", "sites_demo", "_build-worker",
        "--f1", str(Path(f1_path).resolve()),
        "--expected-f1-sha", expected_f1_sha,
        "--evaluation", str(Path(evaluation).resolve()),
        "--expected-evaluation-sha", expected_evaluation_sha,
        "--out", str(out),
    ]
    try:
        worker = subprocess.run(command, cwd=root, capture_output=True, text=True,
                                timeout=65, check=False)
    except subprocess.TimeoutExpired as error:
        raise DemoError("BUDGET_EXCEEDED",
                        "fresh worker exceeded the outer 60-second replay boundary") from error
    if worker.returncode != 0:
        reason = worker.stdout.strip() or worker.stderr.strip() or f"exit {worker.returncode}"
        try:
            worker_error = json.loads(worker.stdout)["error_code"]
        except (json.JSONDecodeError, KeyError, TypeError):
            worker_error = "RUNTIME_PROFILE"
        raise DemoError(worker_error, f"fresh worker failed: {reason}")
    execution_path = out / "execution.json"
    try:
        execution = load_json_strict(execution_path)
    except (OSError, ContractError) as error:
        raise DemoError("INCOMPLETE_RUN", "fresh worker did not write a valid execution record") from error
    require_exact_keys(
        execution,
        {"schema_version", "evaluation_sha256", "semantic_sha256", "runtime_profile_sha256",
         "started_utc", "ended_utc", "argv", "elapsed_seconds", "peak_process_bytes",
         "memory_method", "status", "error_codes"},
        "worker execution",
    )
    pending_complete = out / ".COMPLETE.pending"
    _write_synced(pending_complete, canonical_json(
        {"semantic_sha256": execution["semantic_sha256"], "status": "FINALIZING"}
    ))
    _sync_output_files(out)
    launcher_peak, launcher_method = _peak_windows_bytes()
    worker_peak = execution["peak_process_bytes"]
    errors = [code for code in execution["error_codes"] if code != "MEMORY_NOT_MEASURED"]
    if worker_peak is None or launcher_peak is None:
        measured_peak = None
        errors.append("MEMORY_NOT_MEASURED")
        memory_method = (
            "Outer launcher plus fresh worker; process peaks unavailable under the accepted "
            f"Windows-only method ({launcher_method}; worker={execution['memory_method']})."
        )
    else:
        measured_peak = max(worker_peak, launcher_peak)
        memory_method = (
            "Outer launcher plus fresh worker; Windows GetProcessMemoryInfo PeakWorkingSetSize; "
            f"worker_peak_process_bytes={worker_peak}; "
            f"launcher_peak_process_bytes={launcher_peak}; "
            f"sum_context_bytes={worker_peak + launcher_peak}"
        )
    errors = sorted(set(errors))
    status = "NOT_MEASURED" if errors else "PASS"
    outer_elapsed = time.perf_counter() - started
    execution.update({
        "started_utc": started_utc,
        "ended_utc": datetime.now(timezone.utc).isoformat(),
        "argv": list(sys.argv),
        "elapsed_seconds": outer_elapsed,
        "peak_process_bytes": measured_peak,
        "memory_method": memory_method,
        "status": status,
        "error_codes": errors,
    })
    _write_synced(execution_path, canonical_json(execution))
    _write_synced(pending_complete, canonical_json(
        {"semantic_sha256": execution["semantic_sha256"], "status": status}
    ))
    completed_elapsed = time.perf_counter() - started
    execution.update({"ended_utc": datetime.now(timezone.utc).isoformat(),
                      "elapsed_seconds": completed_elapsed})
    _write_synced(execution_path, canonical_json(execution))
    final_elapsed = time.perf_counter() - started
    if final_elapsed > 60 or (measured_peak is not None and measured_peak > 268435456):
        errors.append("BUDGET_EXCEEDED")
        execution.update({"ended_utc": datetime.now(timezone.utc).isoformat(),
                          "elapsed_seconds": final_elapsed, "status": "FAIL",
                          "error_codes": sorted(set(errors))})
        _write_synced(execution_path, canonical_json(execution))
        pending_complete.unlink(missing_ok=True)
        raise DemoError("BUDGET_EXCEEDED", "outer replay budget exceeded; output remains incomplete")
    os.replace(pending_complete, out / "COMPLETE")
    return execution


def _inspect_run(index_path, label):
    path = Path(index_path).resolve()
    complete_path = path.parent / "COMPLETE"
    if not complete_path.is_file():
        raise DemoError("INCOMPLETE_RUN", f"missing COMPLETE beside {path}")
    value = load_json_strict(path)
    require_exact_keys(value, {"schema_version", "freeze_sha256", "product_commit",
                               "product_code_sha256", "artifacts", "semantic_sha256"},
                       f"semantic index {label}")
    _require(value["schema_version"] == 1 and value["freeze_sha256"] == F1_DIGEST,
             "INCOMPLETE_RUN", f"invalid semantic index identity: {label}")
    require_sha(value["product_code_sha256"], f"product_code_sha256 {label}")
    require_sha(value["semantic_sha256"], f"semantic_sha256 {label}")
    _require(isinstance(value["artifacts"], list), "INCOMPLETE_RUN",
             f"artifact list missing: {label}")
    integrity, rows, artifact_map = [], [], {}
    for position, row in enumerate(value["artifacts"]):
        require_exact_keys(row, {"path", "sha256", "size_bytes", "origin"},
                           f"semantic index {label} artifact {position}")
        try:
            relative = validate_local_path(row["path"])
            require_sha(row["sha256"], f"artifact sha256 {label}")
        except ContractError as error:
            integrity.append({"run": label, "artifact": row.get("path"), "error": str(error)})
            continue
        if (not isinstance(row["size_bytes"], int) or isinstance(row["size_bytes"], bool)
                or row["size_bytes"] < 0):
            integrity.append({"run": label, "artifact": relative,
                              "error": "invalid artifact size"})
            continue
        if row["origin"] not in {"research_source", "freeze_support", "product"}:
            integrity.append({"run": label, "artifact": relative,
                              "error": "invalid artifact origin"})
            continue
        if relative in artifact_map:
            integrity.append({"run": label, "artifact": relative, "error": "duplicate artifact path"})
            continue
        expected = (row["sha256"], row["size_bytes"], row["origin"])
        artifact_map[relative] = expected
        rows.append([relative, row["sha256"]])
        target = path.parent / relative
        if not target.resolve().is_relative_to(path.parent) or not target.is_file():
            integrity.append({"run": label, "artifact": relative, "error": "missing or escaping artifact"})
            continue
        raw = target.read_bytes()
        actual = (sha(raw), len(raw), row["origin"])
        if actual != expected:
            integrity.append({"run": label, "artifact": relative,
                              "expected": expected, "actual": actual})
    if [row[0] for row in rows] != sorted(row[0] for row in rows):
        integrity.append({"run": label, "field": "artifacts", "error": "paths are not sorted"})
    calculated = sha(canonical_json(rows))
    if calculated != value["semantic_sha256"]:
        integrity.append({"run": label, "field": "semantic_sha256",
                          "expected": value["semantic_sha256"], "actual": calculated})
    complete = load_json_strict(complete_path)
    require_exact_keys(complete, {"semantic_sha256", "status"}, f"COMPLETE {label}")
    if complete["status"] not in {"PASS", "NOT_MEASURED"}:
        integrity.append({"run": label, "field": "COMPLETE.status",
                          "error": "invalid complete status", "actual": complete["status"]})
    if complete["semantic_sha256"] != value["semantic_sha256"]:
        integrity.append({"run": label, "field": "COMPLETE.semantic_sha256",
                          "expected": value["semantic_sha256"],
                          "actual": complete["semantic_sha256"]})
    execution_path = path.parent / "execution.json"
    execution = load_json_strict(execution_path) if execution_path.is_file() else None
    if execution is None:
        integrity.append({"run": label, "artifact": "execution.json", "error": "missing execution record"})
    else:
        require_exact_keys(
            execution,
            {"schema_version", "evaluation_sha256", "semantic_sha256", "runtime_profile_sha256",
             "started_utc", "ended_utc", "argv", "elapsed_seconds", "peak_process_bytes",
             "memory_method", "status", "error_codes"},
            f"execution {label}",
        )
        if (execution["semantic_sha256"] != value["semantic_sha256"]
                or execution["status"] != complete["status"]):
            integrity.append({"run": label, "artifact": "execution.json",
                              "error": "execution identity/status differs from completed run"})
    return value, artifact_map, integrity, execution


def compare(index_a, index_b):
    inspected = [_inspect_run(index_a, "a"), _inspect_run(index_b, "b")]
    values = [row[0] for row in inspected]
    maps = [row[1] for row in inspected]
    differences = [finding for row in inspected for finding in row[2]]
    for key in ("schema_version", "freeze_sha256", "product_commit", "product_code_sha256", "semantic_sha256"):
        if values[0].get(key) != values[1].get(key):
            differences.append({"field": key, "a": values[0].get(key), "b": values[1].get(key)})
    for path in sorted(set(maps[0]) | set(maps[1])):
        if maps[0].get(path) != maps[1].get(path):
            differences.append({"artifact": path, "a": maps[0].get(path), "b": maps[1].get(path)})
    executions = [row[3] for row in inspected]
    execution_differences = []
    if all(execution is not None for execution in executions):
        for key in sorted(set(executions[0]) | set(executions[1])):
            if executions[0].get(key) != executions[1].get(key):
                execution_differences.append(
                    {"field": key, "a": executions[0].get(key), "b": executions[1].get(key)})
    return {"equal": not differences, "differences": differences,
            "execution_records_compared": True,
            "execution_differences": execution_differences,
            "note": "Execution differences are reported separately and do not change semantic equality."}
