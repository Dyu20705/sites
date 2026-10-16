"""Verify the externally anchored F1 manifest, artifacts and recorded local runtime.

Read-only, stdlib only. This checks integrity, not human approval authenticity or
scientific validity. Obtain the expected manifest digest from the G70 record.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

from verify_git_bytes import scoped_path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def runtime_identity():
    prefix = Path(sys.base_prefix)
    binaries = {}
    for path in sorted(prefix.iterdir()):
        if path.suffix.lower() in {".exe", ".dll"}:
            binaries[path.name] = sha(path.read_bytes())
    inventory = []
    for directory in (prefix / "Lib", prefix / "DLLs"):
        for path in sorted(directory.rglob("*")):
            if (path.is_file() and path.suffix.lower() in {".py", ".pyd", ".dll", ".zip"}
                    and not {"site-packages", "__pycache__"}.intersection(path.parts)):
                inventory.append([path.relative_to(prefix).as_posix(), sha(path.read_bytes())])
    inventory.sort()
    return {"python": platform.python_version(), "implementation": platform.python_implementation(),
            "cache_tag": sys.implementation.cache_tag, "platform": platform.platform(),
            "machine": platform.machine(), "pointer_bits": 64 if sys.maxsize > 2**32 else 32,
            "root_binaries_sha256": binaries, "stdlib_native_file_count": len(inventory),
            "stdlib_native_tree_sha256": sha(json.dumps(inventory, separators=(",", ":")).encode()),
            "method": "Sorted [relative POSIX path,SHA256] compact UTF-8 JSON over Lib and DLLs .py/.pyd/.dll/.zip; exclude site-packages and __pycache__; root .exe/.dll separately. OS, caches and system DLLs are not hermetically frozen."}


REQUIRED = {
    "schema_version", "freeze_id", "created_utc", "research_source_commit", "contract",
    "owner_approval", "files", "artifact_roles", "runtime", "runtime_scope", "criteria",
    "corpus", "temporal", "signal", "sensitivities", "exposure", "reviewers",
    "holdout", "future_evaluation", "budget", "immutability", "verification_commands",
}
ROLES = {"contract_en", "contract_vi", "owner_approval", "normalized", "config",
         "declaration", "measurements", "controls", "simulation", "pilot",
         "verifier", "independent_verifier", "replay_harness"}
CONTRACT_HASHES = {
    "contract_en": "da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122",
    "contract_vi": "164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0",
}


def require(condition, description):
    if not condition:
        raise ValueError(description)


def contained(root, name):
    path = root / scoped_path(name)
    require(path.resolve().is_relative_to(root), f"Outside artifact root: {name}")
    return path


def verify(manifest_path, expected_sha256, root, repo):
    require(re.fullmatch(r"[0-9a-f]{64}", expected_sha256) is not None, "Invalid external digest")
    raw = manifest_path.read_bytes()
    require(sha(raw) == expected_sha256, "Manifest differs from external SHA-256 anchor")
    m = json.loads(raw)
    require(isinstance(m, dict) and REQUIRED <= m.keys(), "Missing mandatory manifest section")
    require(all(m[key] for key in REQUIRED), "Empty mandatory manifest section")
    require(m["schema_version"] == 1 and m["freeze_id"] == "F1-M1-R-20261012-v1", "Unknown freeze schema/identity")
    require(m["contract"]["version"] == "M1-R-20261010-v1", "Wrong accepted contract")
    require(m["contract"]["status"] == "ACCEPTED_EXTERNALLY", "Contract has no external acceptance")
    require(re.fullmatch(r"[0-9a-f]{40}", m["research_source_commit"]) is not None, "Source commit must be exact")
    require(ROLES <= m["artifact_roles"].keys(), "Missing required artifact role")
    require(all(p in m["files"] for p in m["artifact_roles"].values()), "Unhashed artifact reference")
    require(m["exposure"]["independent_preregistration"] is False, "Exposed data cannot be preregistration")
    require(m["holdout"]["authorized"] is False, "Holdout authorization is outside F1")
    require(m["reviewers"]["real_annotations"] == 0, "No real annotations were performed")
    require(m["reviewers"]["independent_scientific_quality"] == "NOT_MEASURED", "Scientific quality not established")
    require(m["criteria"]["original_E3"] == "NOT_PASSED", "Historical E3 cannot pass")
    require(m["criteria"]["D09"] == "PROPOSED", "F1 does not accept D09")
    require(m["budget"]["measured_product_E8"] is False, "Product budget has not been measured")
    root = root.resolve()
    rows = []
    for name, spec in sorted(m["files"].items()):
        actual = contained(root, name).read_bytes()
        require(sha(actual) == spec["sha256"], f"Artifact SHA-256 mismatch: {name}")
        require(spec["origin"] in {"research_source", "freeze_support"}, f"Unknown origin: {name}")
        if spec["origin"] == "research_source":
            blob = subprocess.check_output(["git", "-C", str(repo), "cat-file", "blob",
                                            m["research_source_commit"] + ":" + name], stderr=subprocess.PIPE)
            require(sha(blob) == spec["sha256"], f"Git blob SHA-256 mismatch: {name}")
        rows.append({"path": name, "sha256": spec["sha256"], "origin": spec["origin"], "status": "PASS"})
    for role, digest in CONTRACT_HASHES.items():
        require(m["files"][m["artifact_roles"][role]]["sha256"] == digest, "Accepted packet identity changed")

    def artifact(role):
        return json.loads(contained(root, m["artifact_roles"][role]).read_bytes())

    owner = artifact("owner_approval")
    require(owner["author"] == "Dyu20705" and owner["url"] == m["owner_approval"]["url"]
            and owner["id"] == 6119490874 and owner["created_at"] == m["owner_approval"]["utc"], "Owner record identity mismatch")
    records = artifact("normalized")
    ids = sorted(r["version_id"] for r in records)
    require(len(records) == len(set(ids)) == 598, "Frozen population/version uniqueness failed")
    require(ids == m["exposure"]["development_version_ids"], "Incomplete development exposure register")
    require(all(r["version_id"] == r["work_id"] + "v1" and r["available_at"] is None
                and r["field_status"]["categories_current"] == "valid" and "cs.SE" in r["categories_current"]
                and all(v == "valid" for v in r["field_status"].values()) for r in records), "Closed-input identity/field boundary failed")
    late = sorted(r["work_id"] for r in records if r["work_id"][:4] > "1906")
    require(len(late) == 9 and late == m["exposure"]["late_work_ids"], "Late-ID exposure register differs")
    pilot = artifact("pilot")["records"]
    require(sorted(r["version_id"] for r in pilot) == m["exposure"]["pilot_version_ids"], "Pilot exposure differs")
    require(len(pilot) == 27 and all(r[k] is None for r in pilot for k in ("annotator_a", "annotator_b", "adjudication")), "Real pilot must remain unexecuted")
    require(runtime_identity() == m["runtime"], "Runtime inventory differs; record a separate prospective runtime before evaluation")
    return {"status": "PASS", "freeze_id": m["freeze_id"], "manifest_sha256": expected_sha256,
            "research_source_commit": m["research_source_commit"], "verified_files": rows,
            "development_exposed": len(ids), "late_ids": late, "unannotated_pilot": len(pilot),
            "runtime": "MATCH", "scope": "Integrity and closed-population checks only; no scientific quality, human review or product E8 claim"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = verify(args.manifest, args.expected_sha256, args.root, args.repo)
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(json.dumps({"status": "FAIL", "reason": str(error)}))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
