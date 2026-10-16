"""One-shot assembly of F1; refuses overwrite. No network and no new corpus evaluation."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
BASE = Path("experiments/research_exit_20260927")
HERE = BASE / "runs/20261012-research-exit-01"
DATA = BASE / "runs/20261010-development-01"
SIGNAL = BASE / "runs/20261010-signal-01"
SOURCE = "97bf499718c13166667a8e5da09b201065d9e117"
sys.path.insert(0, str(ROOT / BASE))
from verify_freeze import runtime_identity, sha


def read(path):
    return json.loads((ROOT / path).read_bytes())


roles = {
    "contract_en": "docs/english/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md",
    "contract_vi": "docs/vietnamese/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md",
    "owner_approval": HERE / "owner-approval.json",
    "normalized": DATA / "replay-1/normalized-records.json",
    "config": DATA / "inputs/preregistration.json",
    "declaration": SIGNAL / "declaration-corrected.json",
    "measurements": SIGNAL / "corrected-replay-1/measurements.json",
    "controls": SIGNAL / "corrected-replay-1/controlled-checks.json",
    "simulation": BASE / "runs/20261010-amendment-01/simulated-workflow.json",
    "pilot": SIGNAL / "reference-pilot-plan.json",
    "verifier": BASE / "verify_freeze.py",
    "independent_verifier": BASE / "runs/20261011-final-audit-01/independent_verify.py",
    "replay_harness": BASE / "runs/20261011-final-audit-01/run_checks.py",
}
roles = {key: str(value).replace("\\", "/") for key, value in roles.items()}
paths = {row["path"] for row in read(BASE / "runs/20261012-remediation-01/frozen-byte-verification.json")["files"]}
tracked = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", SOURCE, "--", str(BASE)], cwd=ROOT, text=True).splitlines()
paths.update(path for path in tracked if path.endswith(".py"))
paths.update(roles.values())
paths.update(str(path).replace("\\", "/") for path in (BASE / "test_freeze.py", HERE / "create_freeze.py"))
files = {}
for path in sorted(paths):
    raw = (ROOT / path).read_bytes()
    origin = "research_source" if path in tracked or path.startswith("docs/") else "freeze_support"
    if origin == "research_source":
        blob = subprocess.check_output(["git", "cat-file", "blob", SOURCE + ":" + path], cwd=ROOT)
        if raw != blob:
            raise ValueError("Exact artifact/Git bytes differ: " + path)
    files[path] = {"sha256": sha(raw), "origin": origin}

records = read(roles["normalized"])
pilot = read(roles["pilot"])["records"]
manifest = {
    "schema_version": 1, "freeze_id": "F1-M1-R-20261012-v1",
    "created_utc": datetime.now(timezone.utc).isoformat(), "research_source_commit": SOURCE,
    "contract": {"version": "M1-R-20261010-v1", "status": "ACCEPTED_EXTERNALLY",
                 "identity": "Exact EN/VI Git blobs pinned under contract_en/contract_vi; old PROPOSED text is historical and is not rewritten"},
    "owner_approval": {"owner": "Dyu20705", "utc": "2026-10-12T07:10:14Z",
                       "url": "https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874",
                       "accepted": ["A1", "A2", "A3", "D07", "D08", "F1 contract"],
                       "G70": "Conditional on verified F1 and all accepted research criteria; not automatic"},
    "files": files, "artifact_roles": roles, "runtime": runtime_identity(),
    "runtime_scope": {"executable": sys.executable, "base_prefix": sys.base_prefix,
                      "dependencies": "Python standard library; Git for object verification; no new package",
                      "git": subprocess.check_output(["git", "--version"], text=True).strip(),
                      "evaluation": "Author same-host offline integrity/replay verification. Not independent reviewer replay or a hermetic OS image.",
                      "new_reviewer_runtime": "Before a new product evaluation, append a separately versioned runtime/task/personnel record; do not mutate this author inventory."},
    "criteria": {
        "research_gate": ["Explicit A1/A2/A3/D07/D08/F1 approval", "All F1 references and runtime match external SHA256 anchor",
                          "598 distinct exact-v1 works and 100% raw lineage", "Zero arithmetic/replay/identity mismatches",
                          "All fixed case/control, boundary and sensitivity checks reproduced", "SYN-only workflow and zero real annotations",
                          "Limits, exposure and null/abstention explicit; original E3 not passed"],
        "E2_R_research": "Fixed fuzzing case; constant-share control; all declared sensitivities; synthetic workflow correctness",
        "E3_R_research": "Exact offline population/v1/event/window/config; out-of-window/future event exclusion; no availability claim",
        "product_pending": {"E1": "Integrated fixtures", "E2_R": "Independent reviewer interpretation",
                            "E3_R": "Integrated demo replay", "E4": "Author plus independent reviewer replay",
                            "E5": "Displayed evidence navigation", "E6": "Integrated idempotency",
                            "E7": "Five of five interpretation answers, one match and one nonmatch opened; no code edits",
                            "E8": "Measure bounded wall time and peak process memory on recorded reviewer environment"},
        "independent_reference_retained_for_G70": False, "original_E3": "NOT_PASSED", "D09": "PROPOSED",
        "scientific_quality": "NOT_MEASURED; no precision/recall/trend threshold or scientific novelty claim"},
    "corpus": {"provider": "arXiv", "query": "cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]",
               "population": "Observed frozen 2026 current cs.SE query; not historically complete cs.SE", "works": 598,
               "inclusion": "Distinct work with exact v1, valid v1 event inside accepted six UTC months, in frozen current cs.SE query; all nonmatches included",
               "exclusion": "Outside event window/current cs.SE or non-v1 observations; conflicts fail closed. Invalid event leaves monthly denominator unresolved, never silently drops a work.",
               "denominator": "All eligible distinct works, including unknown titles; never concept-filtered",
               "boundary": "Only these 598 exact hashed records are admitted. Frozen evaluator is not a general fail-closed importer; missing current-category hazard is contained by verified complete fields. New inputs require separately versioned strict validation after D09.",
               "bias": ["Current index membership and removals unknown", "Title vocabulary and alias coverage", "Sparse monthly support", "Selection and submission/public-availability delay"],
               "retention": "Metadata/raw Atom only; no paper PDFs or inferred full-text redistribution rights"},
    "temporal": {"retrieved_utc": ["2026-10-10T11:27:47Z", "2026-10-10T11:28:24Z"],
                 "start_utc": "2019-01-01T00:00:00Z", "end_utc": "2019-06-30T23:59:59Z",
                 "bins": [f"2019-{n:02}" for n in range(1, 7)], "event": "v1 submission UTC calendar month",
                 "available_at": None, "historical_as_of_claim": False,
                 "distinct_times": "Acquisition, v1 submission, version update and public availability must never be conflated"},
    "signal": {"rule_id": "RE-20260927-01-documented-word-boundary-v1", "pattern": r"\bfuzz(?:ing|er|ers)?\b",
               "flags": "Python re.IGNORECASE, Unicode", "field": "title_v1", "counting_unit": "distinct work",
               "formula": "N=eligible distinct works; n=sum of title-rule matches; p=n/N if defined. Aggregate windows use ratio of sums.",
               "n": [0, 1, 2, 1, 4, 1], "N": [91, 79, 97, 103, 122, 106], "total_n": 9, "total_N": 598,
               "null_policy": "Unknown/invalid title stays in N; n/p=null; retain known-match count and bounds. Invalid event makes monthly N unresolved. Empty N makes share null.",
               "support": "n>=0; defined share needs N>=1 and known required fields; not a statistical-adequacy threshold",
               "labels": "NONE at every support value; no growth/emergence/decline or scientific relevance claim"},
    "sensitivities": ["exact fuzzing", "current title", "v1 category subset", "exclude nine late IDs as perturbation only",
                      "adjacent Jan-Feb/Mar-Apr/May-Jun ratio of sums", "decoded-pattern equality/literal transport diagnostic"],
    "exposure": {"independent_preregistration": False,
                 "statement": "All 598 development metadata, bins, counts/shares, sensitivities and nine late-ID cases inspected before this freeze. Local declaration and post-output metadata correction preserved. No rule/value change.",
                 "development_version_ids": sorted(r["version_id"] for r in records),
                 "pilot_version_ids": sorted(r["version_id"] for r in pilot),
                 "late_work_ids": sorted(r["work_id"] for r in records if r["work_id"][:4] > "1906"),
                 "prospective_only": "Freeze unchanged replay and future disclosed reviewer tasks, not untouched scientific validation"},
    "reviewers": {"author": "Codex producing agent; same-host verification, not independent human",
                  "independent_reviewer": None, "reviewer_exposure": "UNASSIGNED; disclose identity, prior exposure and environment before product task",
                  "simulation": "SIMULATED_A/B/C on SYN-001..SYN-027; 54 judgments, 18 agreements, 9 adjudications, final 9/9/9 are designed fixtures",
                  "real_annotations": 0, "independent_scientific_quality": "NOT_MEASURED",
                  "future_task": "Five correct answers: n/N, share, 2026 observed vs 2019 event, lexical vs semantic, no trend/as-of inference; open match/nonmatch; replay without code edits; preserve raw answers/failures; disclose retest exposure"},
    "holdout": {"authorized": False, "period": "July-December 2019", "policy": "No query/read/write/acquisition/evaluation under this authorization. Existing nine late IDs remain exposed development, not a new holdout read."},
    "future_evaluation": {"predeclare": ["Separately accepted population/query/event semantics", "Semantic reference, thresholds and vocabulary",
                                         "Personnel and exposure", "Code/config/input/runtime identities", "Criteria and resource budgets"],
                          "overlap": "Reconcile exact work AND version identity against all 598, 27 pilot and nine late IDs; quarantine overlap; record prior source-evidence exposure",
                          "unknown_untouched_status": "Label development, never holdout", "authorization": "Separate owner approval required before acquisition"},
    "budget": {"max_works": 598, "replay_wall_seconds": 60, "peak_process_MiB": 256, "live_corpus_requests": 0,
               "target_laptop_RAM_GiB": 16, "measured_product_E8": False,
               "status": "Prospective engineering limits from accepted packet; post-development exposure; measure product/reviewer boundary after D09, no scalability claim"},
    "immutability": {"policy": "Never edit this version or old development evidence. New version explicitly supersedes with reason, exposure and external approval/digest.",
                     "anchor": "Manifest SHA256 recorded outside manifest in receipt and G70; new bundle commit recorded externally to avoid self-hash cycle",
                     "source_split": "research_source entries verified against exact source commit; freeze_support entries are newly created and pinned by manifest, then bundle commit",
                     "reopen": ["Any digest/identity conflict", "Invalid denominator", "Owner requires historical-as-of or scientific detection quality", "Reviewer misinterpretation", "New input/rule/runtime/scope requires prospective change"]},
    "verification_commands": ["python experiments/research_exit_20260927/verify_freeze.py --manifest <freeze-v1.json> --expected-sha256 <external-G70-digest> --root <absolute-artifact-root> --repo <source-Git-repo>",
                              "python -m unittest discover -s experiments/research_exit_20260927 -p test_*.py -v",
                              "python experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py --output <new-path>",
                              "Historical run_checks.py validates original PROPOSED status docs: run against source commit export. New accepted decision state is verified separately."]
}
raw = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
with (ROOT / HERE / "freeze-v1.json").open("xb") as stream:
    stream.write(raw)
with (ROOT / HERE / "freeze-v1.sha256").open("x", encoding="ascii", newline="\n") as stream:
    stream.write(sha(raw) + "  freeze-v1.json\n")
print(json.dumps({"freeze_id": manifest["freeze_id"], "sha256": sha(raw), "files": len(files)}))
