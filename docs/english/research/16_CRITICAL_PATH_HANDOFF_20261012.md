# 16 — Critical-path audit and conditional demo handoff

**12 October 2026; handoff version CP-20261012-v1.** Research Exit **#70 NOT PASSED**; #64 remains **OPEN / READY FOR OWNER REVIEW**. This is a targeted audit and a **PROPOSED** design addendum, not acceptance, a product implementation, or independent scientific evaluation. Deadline: demo-ready **15 October 2026**, before 16 October, Asia/Bangkok.

## 1. Verified checkpoint and findings

Audited `research/exit-evidence-20260927@7ef28119b125c6bcb9f0372516cc0ebe3200326d`, base `master@0a853636ef6d1be9d3bb85058f34faf368fcb6ce`: clean existing research worktree, aligned with freshly fetched origin, 14 commits ahead of base and zero behind. Main checkout remains on clean `dev@0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`. [PR #75](https://github.com/Dyu20705/sites/pull/75) is OPEN/Draft; no submitted reviews, review threads, conversation comments or status-check rollup entries were returned. Absence of CI is not a PASS.

Read live #64–#67, #69–#73, all #64/#70 comments, the #66 comment and PR discussions. #65 is CLOSED/completed; the others are OPEN. [Owner direction 6097713689](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) accepts retrospective direction and proposal preparation only. [Audit 6104422817](https://github.com/Dyu20705/sites/issues/64#issuecomment-6104422817) does not close #64 or accept #70. D05/D06 ACCEPTED; exact amendment/D07/D08/D09 and prospective freeze PROPOSED. WIP: #64 audit/correction plus its bounded decision/design handoff; no #72 lane.

| Severity / scope | Confirmed mechanism and evidence | Minimal remedy / disposition |
| --- | --- | --- |
| **BLOCKER — #70/#71 authorization** | Packet 15 §9 has no exact owner acceptance; original historical E3 remains NOT PASSED. #71 requires #70 and owner D09 acceptance. | Owner decides the separate rows below, creates the applicable accepted freeze, then explicitly records #70 disposition. Do not infer acceptance from checkboxes or this review. |
| **MAJOR — legacy output preservation; corrected at the current entry point** | [checks.py](../../../experiments/research_exit_20260927/checks.py), line 154, uses `write_text` on any requested path. A fresh sentinel was overwritten, exit 0, by a passing 15-test run; [disposable-file reproduction](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01/legacy-overwrite-probe.json). | Added [checks_cli_v2.py](../../../experiments/research_exit_20260927/checks_cli_v2.py): run unchanged checker in a private temporary directory, publish only after success with exclusive creation. Three regressions cover preserving old bytes without execution, frozen-output equality/repeat refusal, and failed-run nonpublication. README now routes replay through v2. Frozen v1 remains unsafe if invoked directly on existing output; historical runner is contained by its fresh private output directory. |
| **MAJOR before broader helper reuse; contained for this corpus** | [signal_evaluator.py](../../../experiments/research_exit_20260927/signal_evaluator.py), line 53, maps absent `categories_current` to `[]`, then excludes the record. A synthetic positive becomes an empty bin: n=0, N=0, p=null instead of unknown membership. [Repeated probe](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01/boundary-probe.json). | All 598 frozen works have valid current membership containing cs.SE, verified from raw Atom. Preserve evaluator bytes. Proposed separately versioned strict projection below must reject unknown/invalid membership and include regressions before any product reuse. Containment depends on verifying accepted input/config/code hashes, not merely calling the helper. |
| **MAJOR — tracker reliability; unresolved** | The live #66 body has all seven demo boxes checked while its prose says 0/7 independently verified. No view, independent replay or #73 pass is supplied. #64 describes six partial original obligations while most corresponding boxes are checked; #69 checks exact-search metadata although the preserved audit records gaps. Snapshot excerpts and body hashes are in the [audit directory](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01). | Reconcile each box to linked evidence and a dated status when the owner records the gate. This audit does not overwrite recent owner edits or use them to authorize implementation. #71–#73 remain unpassed. |
| **INFORMATIONAL — evidence boundary** | Reproduced arithmetic and lineage; zero independent real annotations. Fictional SYN judgments, code cross-checks and same-host processes are not independent scientific evaluation. | Keep the five evidence levels in §3 separate. No new defect invalidating the frozen nine-match result was found. |

No separate MINOR defect was confirmed. The old [conditional handoff 10](10_CONDITIONAL_DESIGN_HANDOFF.md) remains historical, provider-neutral proposal context; §4 below is the more specific retrospective design candidate. Neither document selects D09.

## 2. Owner decision matrix — unchanged packet, separate decisions

The existing packet is adequate for owner review; **do not rewrite or sign it**. Every row below refers to **M1-R-20261010-v1** at the immutable [reviewed commit](https://github.com/Dyu20705/sites/tree/7ef28119b125c6bcb9f0372516cc0ebe3200326d). Its Git-blob SHA-256 identities remain:

- [English packet 15](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md): `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`.
- [Vietnamese packet 15](../../vietnamese/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md): `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`.

The version and both hashes apply to **each** row. Acceptance is an external record naming owner, UTC timestamp, row, choice and packet hash; revising a row requires a separately versioned addendum. Approval of one row does not approve the others.

| ID / status / exact proposal | Verified support; residual uncertainty | Serious alternative | Recommendation, consequences and authorization |
| --- | --- | --- | --- |
| **A1 PROPOSED**, §§1–2: observed-2026 corpus, v1-title lexical prevalence in Jan–Jun 2019 event bins; exact M1/D05 clause changes | 598-work raw recount and #65 negative historical outcome. User value and historical population remain unverified. | Retain broader scientific question and defer M1 completion. | Recommend ACCEPT only if this limited descriptive value meets owner intent. ACCEPT changes the declared estimand; REJECT retains original unmet obligations; REVISE needs exact new clauses. Enables a compatible research contract, not product work. |
| **A2 PROPOSED**, §2: E2-R/E3-R obligations while original E3 stays NOT PASSED | Frozen-boundary/control/lineage evidence exists; independent interpretation and product checks are absent. | Retain original E2/E3 and await qualifying evidence. | Recommend ACCEPT the explicit replacement scope for the descriptive route. ACCEPT activates these obligations only in the amended scope; REJECT leaves original requirements; REVISE must remap criteria before evaluation. No original E3 PASS is authorized. |
| **A3 PROPOSED**, §§5–6: explicitly choose limited descriptive acceptance with scientific quality NOT MEASURED | Zero real judgments; 27 SYN workflow cases are reproducible. No semantic/trend accuracy threshold is justified. | Retain independent-reference requirement; designate qualified humans and freeze justified criteria before evaluation. | Recommend the limited route if acceptable to the owner. ACCEPT removes scientific-quality acceptance only as explicitly amended; REJECT/retained-reference route keeps #70 blocked for real evidence; REVISE requires an exact criterion. Simulation never substitutes for independent labels. |
| **D07 PROPOSED**, §3: exact frozen 598 observed works, identity, v1 UTC event time, denominator, query and sharing boundary | 14 inputs hash-verified; 598 current/v1 pairs and all denominator IDs reconcile. Current-query selection and missing historical membership remain. | Defer; separately scope historical reconstruction if the owner requires as-of validity. | Recommend ACCEPT this finite observed population. ACCEPT pins eligibility and permitted metadata; REJECT/REVISE requires a new bounded corpus proposal. No new provider, acquisition or holdout becomes authorized. |
| **D08 PROPOSED**, §§4–6: unchanged lexical rule, n/N/share, null/support behavior, all sensitivities, no direction labels | n=0/1/2/1/4/1, N=91/79/97/103/122/106; exact-fuzzing variant has five hits. Sparse support/alias bias and broader helper limitation remain. | Count alone, with N still disclosed, or defer. | Recommend ACCEPT count plus share as a descriptive result; require the strict projection before reuse. ACCEPT pins formula and evaluation boundary; REJECT/REVISE needs a new version and exposure disclosure. Does not certify a detector or authorize UI implementation. |
| **F1 PROPOSED**, §7: prospective freeze, full exposure register, reviewer/replay and budget protocol | Existing input/config/code/output identities exist; corpus, plots and pilot selection already exposed. Signed freeze and reviewer identity/session are absent. | Permit no new evaluation; preserve development-only results. | Recommend ACCEPT a prospective replay/task freeze. ACCEPT requires immutable manifest plus owner evidence, personnel/exposure and applicable criteria; REJECT permits no dependent evaluation; REVISE must precede new evaluation. Research freeze pins current research code; later product code is pinned separately before reviewer tasks. No holdout authorization. |
| **G70 BLOCKED / NOT PASSED**, §9: disposition only after accepted, evidenced criteria | A1/A2/A3/D07/D08/F1 remain unsigned; no accepted replacement contract. | Keep NOT PASSED with named gaps. | Recommend NOT PASSED now. A later explicit PASS authorizes #71 design acceptance work only, after every retained research criterion is met. REJECT keeps downstream work blocked; REVISE lists missing evidence. It never implies D09, feature or demo readiness. |

## 3. Validation and scientific interpretation

[Initial execution record](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01/execution.json) and [correction tests](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01/correction-validation.json) retain argv, stdout/stderr, environment and exit codes. Current environment: Windows 11, Python **3.14.7**, standard library; TEMP/TMP explicitly set to writable workspace scratch.

- Initial current-checkpoint suite: **37/37 PASS**. After the isolated v2 entry point: **40/40 PASS**, zero failures/errors, unittest reported **1.367 seconds**. This is test timing, not E8.
- Existing runner: **13 commands**, twelve exit 0 and one expected exit 2 when reusing a validator output. Fifteen legacy checks in each of two processes; ten controlled cases per signal replay; paired corpus/signal/SYN replays; **13/13 byte comparisons match historical artifacts**.
- [Raw Atom/token recount](../../../experiments/research_exit_20260927/runs/20261012-critical-path-01/independent-verification.json): 14 frozen inputs also match Git bytes; 598 v1/current lineages, nine numerator refs, 18 lexical boundary cases, five sensitivity variants, adjacent two-month ratios and exact 27-work real pilot selection verified. Pilot annotations remain null.
- Missing/invalid title, missing/invalid event, true zero, empty denominator, duplicate/conflicting version, UTC boundary and future-event behavior are covered by executed tests. Missing current membership is the separately reproduced limitation above.
- Network-restricted initial `gh` calls failed; connected GitHub tools and an approved read-only `gh pr view` confirmed state, and `git fetch` confirmed alignment. Offline research commands did not query the corpus. Python emitted “Failed to find real location” warnings but all expected command outcomes were obtained; portability to a clean independent host remains untested.
- Final link/hash/whitespace checks and preservation inventory are recorded in the audit directory. Core evaluator/audit/crosscheck/checker/simulator/validators, tests, packet 15 and report 14 were inspected. The full 143-file incoming PR inventory explicitly distinguishes source/semantic review, programmatic raw/lineage checks, and preservation-only or contextual review. Earlier provider/literature searches were not rerun; no exhaustive security audit or independent translation review is claimed.

Reproduce from the research worktree root, using fresh output paths:

```powershell
New-Item -ItemType Directory -Force -Path "experiments/research_exit_20260927/__pycache__/audit-temp" | Out-Null
$env:TEMP = (Resolve-Path "experiments/research_exit_20260927/__pycache__/audit-temp").Path
$env:TMP = $env:TEMP
python -m unittest discover -s experiments/research_exit_20260927 -p "test_*.py" -v
python experiments/research_exit_20260927/checks_cli_v2.py --output <fresh-directory>/legacy.json
python experiments/research_exit_20260927/runs/20261011-final-audit-01/run_checks.py
python experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py --output <fresh-directory>/independent.json
python experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary_probe.py --output <fresh-directory>/boundary.json
python experiments/research_exit_20260927/validate_signal.py --run experiments/research_exit_20260927/runs/20261010-signal-01 --output <fresh-directory>/signal-validation.json
python experiments/research_exit_20260927/validate.py --output <fresh-directory>/package-validation.json
git diff --check
```

Create the writable scratch directory first on a fresh checkout. Angle-bracket output placeholders must be replaced, not pasted literally. The historical runner creates unique scratch directories itself and therefore safely contains its original checker invocation.

| Evidence level | Current conclusion |
| --- | --- |
| Arithmetic and workflow correctness | VERIFIED within exercised cases; v2 output preservation tested |
| Reproducible descriptive corpus analysis | VERIFIED development result: **9/598**, monthly N **91/79/97/103/122/106**, n **0/1/2/1/4/1** |
| Independent semantic quality | **NOT MEASURED**; zero real annotations, no independent human assessment |
| Validated scientific trend detection | **NOT ESTABLISHED**; no emergence/adoption/impact/causality/as-of claim |
| Product/demo readiness | **NOT PASSED**; no accepted D09, integrated view, independent clean-environment replay, E7 or measured product E8 |

Normalized corpus SHA-256: `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1`; config: `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`; measurements: `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818`.

Negative findings remain: historical available_at unresolved for 598/598; nine late-ID anomalies; 161 revised current records, 55 changed titles, four category-set changes. Exact-fuzzing gives five hits versus nine under the frozen broader rule. Excluding late IDs changes N but does not repair historical completeness. Support is 0–4/month. The 27 fictional records yield 54 designed judgments, 18 agreements and nine adjudications, not observed human agreement.

## 4. Conditional D09 addendum — CP-D09-R-20261012-v1, PROPOSED ONLY

**Not implemented.** Requires #70 PASS, then explicit owner D09 acceptance at #71. Accept this version by the committed file identity/hash recorded in the audit artifacts; no choice below is implied by this audit.

Proposed flow: **frozen real input → strict validated projection → deterministic count/share → evidence bundle → local read-only view → offline replay**.

| Choice | Recommended candidate and reason | Serious alternative / revisit trigger |
| --- | --- | --- |
| Files/JSONL vs SQLite | Keep the original JSON/raw Atom immutable; derived sorted JSON or JSONL plus manifests. Six bins/598 works do not yet demonstrate a need for indexing. | SQLite if measured query/render cost or accepted editing needs justify it; do not migrate frozen evidence. |
| Standard library vs dependencies | Python batch processing using the existing tested rule; no new runtime package. | A specific library only after a measured missing requirement and owner acceptance. |
| In-process vs HTTP | Read immutable results within the batch/query functions; no listening service. | Local HTTP only if a required browser behavior cannot be met by a file view. |
| Static view vs frontend framework | Generate local HTML/SVG/tables with ordinary links, embedded data and no remote assets or runtime fetch. | Framework only after a documented usability failure that a small static change cannot solve. |

No PostgreSQL/server DB, Kubernetes, workers, microservices, agent orchestration, graph platform, ML/LLM classifier or repository split is proposed.

### Logical interfaces and invariants

| Contract | Minimum fields and behavior |
| --- | --- |
| AcceptedInputManifest | Owner acceptance reference, packet hash, query, acquisition interval, 14 raw/config input hashes, 598 exact work IDs, rule/code identities, criteria/exposure, permitted metadata and fresh output location. Verify accepted bytes before parsing; an arbitrary caller-supplied replacement hash list is not approval. |
| ValidatedProjection-v1 | One work ID with exact v1 identity/title/event, typed current/v1 categories, explicit field statuses, both current/v1 raw file/hash/entry-index/entry-ID references. Verify all 598 memberships, no conflicting pair, no orphan or unaccounted ID. Never use current-title/event fallback silently. |
| SignalPoint-v1 | Six fixed UTC bins; n, N, p, known matches, missing/invalid/unassigned IDs, typed status, full denominator and numerator IDs, rule version. Query supports only the accepted concept and contiguous whole-month ranges; range share is ratio of sums. |
| EvidenceBundle-v1 | Results → rule/config → complete denominator IDs (including nonmatches) → projection → both raw Atom entries and hashes. Local match/nonmatch detail pages expose version, event/retrieval distinction, missingness and claim limits; external source link is optional, never required for demo. |
| ReplayRecord-v1 | Accepted manifest and software/runtime identities, canonical semantic output hashes, exact commands/exit codes, environment, wall time and peak process memory, failures and exposure. Timestamps/paths/timings belong outside the semantic digest. |

Identity/time: count each distinct work once; identical repeats are idempotent, conflicting v1 rows fail closed, current versions never add contributions. UTC v1 submission window is 2019-01-01T00:00:00Z through 2019-06-30T23:59:59Z. Current-category membership is a 2026 selection fact, not historical membership. Keep available_at null. [arXiv's manual](https://info.arxiv.org/help/api/user-manual.html) distinguishes first-version and retrieved-version timestamps; [availability policy](https://info.arxiv.org/help/availability.html) distinguishes submission from public announcement. These documents were rechecked on 12 October; no historical announcement capture was obtained.

**Proposed correction boundary:** introduce a new strict projection/guard version under #72 after #71, preserving frozen `signal_evaluator.py`. Required regression cases: missing key, null, empty list, wrong type and invalid category token → typed unresolved-membership diagnostic and no successful numeric result; valid known nonmembership in a pure eligibility fixture → explicit exclusion. An unexpected record/field/hash in the exact frozen input fails the whole import. Tests of missing fields operate on disposable fixtures, not mutated historical files.

Error semantics: valid n=0 with N>0 gives p=0; valid N=0 gives p=null. Missing/invalid titles stay in known N, with n/p null and disclosed bounds. Missing/invalid event makes affected population/bin accounting unresolved; do not silently shrink N. Unknown membership cannot become excluded or negative. Integrity/identity/conflict failures abort publication of a successful bundle; retain diagnostics in a new run location. Do not render null as zero. Disable scientific direction labels at every support level.

Determinism: sort IDs/keys, UTF-8/LF canonical JSON, preserve exact integer n/N and the accepted division/rounding rule; display rounding never enters calculations. Compare semantic bytes separately from observational execution metadata. The accepted output must reproduce the frozen six n/N pairs, nine matched IDs and all 598 source lineages. Subsequent code fixes require a new version and run directory with declared exposure.

### Minimal commands and security boundary

These are **proposed interfaces, currently nonexistent**, to accept at #71:

```text
python -m sites_demo build --manifest <accepted-manifest.json> --out <new-directory>
python -m sites_demo compare --expected <frozen-semantic.json> --actual <new-directory>/semantic.json
python -m unittest discover -s tests -v
```

`build` verifies/imports/calculates/renders in one offline process and writes semantic.json, evidence pages, index.html, diagnostics and execution metadata. A pre-existing output directory is refused. Exit 0 means successful command, 2 invalid input/contract or existing output, 3 semantic mismatch, 1 unexpected failure. None of these means #73 passed. Open index.html locally; ordinary links choose the fixed concept/time range and open every contributing record. The 21 possible contiguous ranges can be precomputed from six monthly bins without JavaScript or a server.

Treat titles and metadata as untrusted text: escape HTML, allow only validated local paths and explicit https arxiv.org source links, no remote scripts/assets, no dynamic evaluation, credentials or writable web interface. Check size/hash before XML parsing; resolve input paths under the fixed corpus root and refuse traversal/symlinks escaping it. Use exclusive outputs; retain failed-run diagnostics without overwriting past runs.

The [API terms](https://info.arxiv.org/help/api/tou.html), rechecked 12 October, permit descriptive metadata under CC0 and distinguish e-print redistribution rights. The proposed bundle contains permitted metadata/raw Atom and provenance; it does not include PDFs/full text under assumed metadata rights. A later request for other material requires its own rights check.

### Tests, resources and clean-environment procedure

Unit checks: frozen lexical boundaries/case/Unicode behavior, UTC start/end and future-event exclusion, duplicate/revision/conflict, zero/missing/invalid distinctions, unknown-category guard, complete denominator and ratio-of-sums, HTML escaping and path/output preservation. Avoid tests that only restate generated templates.

Integration: actual 598-work frozen input through build; exact n/N, nine IDs, every denominator/current/v1 reference and all five retained sensitivities match research evidence. Duplicate input replay changes no contribution. Corrupted input/config/code or truncated population must fail before success publication. No live provider call; synthetic fixtures supplement the real integration.

End to end: local view opens offline, fixed concept/range is selectable, n/N/share and limits are visible, one match and one nonmatch can be reached, and a programmatic link inventory covers all 598 IDs. Human E7 interpretation remains a separate check.

**Budget PROPOSED**, inherited from packet 15: ≤598 works, ≤60 seconds offline build/replay, peak batch-process memory ≤256 MiB. Record disk input/output bytes and browser observations separately. Single-process design makes the memory boundary explicit; measure peak working set on Windows or documented equivalent, with wall clock from process start through complete bundle. Record OS/CPU/RAM/Python and exact measurement method. Unavailable memory evidence leaves E8 NOT MEASURED; do not infer compliance from test speed or lack of a crash. Accept criteria before measuring the product.

After gates, package accepted manifest, permitted input, source revision, canonical outputs and instructions. On a clean independent reviewer environment: verify package hashes; record identity/prior exposure and environment; use the pinned existing Python runtime with no network installation; run unit/integration checks and build twice into new directories; compare semantic bytes to the accepted result; open local view while offline; record timing/memory and the five packet-15 interpretation answers. Reviewer must also open match/nonmatch evidence without changing code. Failed answers require disclosed correction/retest, not deleted attempts or silent threshold changes. Same-author fresh processes do not satisfy independent reviewer requirements.

## 5. Post-approval tasks and deadline

| Gate / next executable task | Prerequisites and completion evidence |
| --- | --- |
| **#71 PREIMPLEMENTATION-READY** | After explicit #70 PASS, owner accepts D09 version and logical contracts above (or a specific revision), membership-guard behavior, output identity/rounding, reviewer protocol and budget. Freeze acceptance separately from document bytes. No component without an accepted requirement. |
| **#72 FEATURE-READY** | After #71, implement one real-input path: import → strict projection → fixed count/share → complete evidence → static read-only view → replay. Add the proposed guard in new code, not frozen evaluator bytes. Unit/integration/real-data end-to-end checks pass; preserve null/limits; record as-built design and exact implementation identities. |
| **#73 DEMO GATE** | After #72, independent clean-environment offline replay, complete displayed traceability, fixed interpretation task if retained, actual wall/memory evidence and every accepted criterion. Scientific quality stays NOT MEASURED on the limited route. A retained independent-reference criterion requires real evidence; otherwise record NOT PASSED. Stop building immediately when accepted demo criteria pass. |

**Single smallest next action:** owner decides A1/A2/A3/D07/D08/F1 against the unchanged packet hashes and this audit, then records G70 against the selected research criteria. No further corpus search or product work can substitute for that decision. If independent-reference acceptance is retained, the next bounded work is designated-human, prospectively frozen reference evaluation; neither simulation nor this audit completes it.

**Deadline risk: HIGH.** A narrow retrospective descriptive demo remains conditionally plausible by 15 October if #70/#71 are accepted promptly and a real reviewer is available for the independent task/replay; this is a planning judgment, not a delivery guarantee. Three gated stages remain. The current evidence does not support promising a scientifically validated trend-detection product by that date. If retained criteria remain unmet, report NOT PASSED with the reusable evidence; keep scope and thresholds honest.

Review preparation and the output-preservation correction are complete within current authorization. The [SITES decision-gate skill](../../../.agents/skills/sites-decision-gate/SKILL.md) says to “stop before implicit acceptance”; the repository contract and owner request also require explicit #70/#71 acceptance. This is why implementation stops at the concrete decision package.
