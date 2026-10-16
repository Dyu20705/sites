# 14 — D08 development evaluation and owner decision packet

**Latest audit, 11 October 2026:** [final #64 DoD audit](#final-64-dod-audit--11-october-2026) below verifies the frozen result and records remaining owner decisions and a standalone-helper limitation. The dated development report is preserved.

**Later owner disposition:** [#70](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) accepts this development-only evidence and selects retrospective-only direction. [Packet 15](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) now carries the exact PROPOSED amendment and D07/D08/quality decisions; the earlier A/B choice discussion below is historical. Independent scientific quality remains NOT MEASURED, including after the separately authorized synthetic workflow test. No measurement/configuration/declaration here is changed.

**VERIFIED, 10 October 2026:** #65 closed `completed` after [owner acceptance](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097421846), [A acknowledgment](https://github.com/Dyu20705/sites/issues/64#issuecomment-6097520949) and [completion record](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097523060). #64 now has actual exploratory count/share evidence. **D07/D08/D09 PROPOSED; E3/#70 NOT PASSED.** This packet supports an owner choice; it is not a frozen confirmatory contract or permission to implement D09. Demo-ready deadline: **15 October 2026**.

## Declaration, unit and claim boundary

Starting branch `research/exit-evidence-20260927`, clean and aligned with origin at `53a50ec806b2d6d5fee4112554a6826aeaea852b`; PR #75 OPEN/Draft. Issues #64/#65/#70 were OPEN before this execution. Owner accepted only #65's negative investigation disposition, conditional on A acknowledgment. A reran 17 existing tests and reproduced audit/normalized/crosscheck bytes; this is same-host agent verification, not independent human approval.

Research question: what do count and normalized share describe under the existing fuzzing title rule, and which artifacts defeat interpretation? Construct: **observed first-version title lexical prevalence in the frozen retrospective development query**. Distinct scholarly work is the unit. Query `cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]`, Jan–Jun 2019, monthly UTC bins by v1 submission. All 598 observed current-category works, including nonmatches, are eligible; no exclusions or unknown title/date values in the actual run. This does not measure complete historical cs.SE, all software-testing research, emergence, importance, adoption, causality or independent detection quality.

[Local declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration.json) preceded real signal execution; [corrected declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json) preserves its conditions and exposes a metadata error. The agent misread nested tool-output JSON escaping and initially alleged a regex transport mismatch. Direct decoded comparison disproved that allegation: root/frozen config and existing `checks.PATTERN` are identical. No lexical rule changed. Original declaration and first outputs remain inspectable; corrected reports change provenance text only. The literal-config diagnostic returns the same nine matches. This correction was made after initial output inspection and is disclosed as such.

Rule version `RE-20260927-01-documented-word-boundary-v1`: `\bfuzz(?:ing|er|ers)?\b`, case-insensitive, v1 titles. Fuzzing was selected in the original proposal from independent 2018 context, without an assumed direction. Prior exposure includes corpus metadata, earlier synthetic outputs, and the nine late-ID development works. Neither the local declaration nor an after-execution push independently proves preregistration timing. No July–December holdout was queried, inspected or written; the candidate split remains unaccepted.

## Formula and actual development observations

For eligible distinct works C_b, `N(b)=|C_b|`, `n(c,b)=sum(match(c,w) for w in C_b)`, and `p(c,b)=n(c,b)/N(b)` for `N(b)>0`. Missing/invalid title remains in N but makes n/p null; known matches and [lower, upper] share bounds are retained. Missing/invalid event time makes monthly denominators unresolved rather than silently dropping unknown-bin works. Duplicate v1 observations collapse; conflicting v1 observations fail; revised observations do not contribute again. Empty N gives undefined share. These are research interfaces, not a product schema.

| UTC month | Eligible N | Matches n | Share (%) | Missing / invalid titles |
| --- | ---: | ---: | ---: | ---: |
| 2019-01 | 91 | 0 | 0.0000 | 0 / 0 |
| 2019-02 | 79 | 1 | 1.2658 | 0 / 0 |
| 2019-03 | 97 | 2 | 2.0619 | 0 / 0 |
| 2019-04 | 103 | 1 | 0.9709 | 0 / 0 |
| 2019-05 | 122 | 4 | 3.2787 | 0 / 0 |
| 2019-06 | 106 | 1 | 0.9434 | 0 / 0 |

Total **9/598 = 1.5050%**. Support is only 0–4 works/month. February, April and June each have count=1, but different shares because N differs. Share contributes denominator context; it does not establish a stronger substantive trend. One title changing match status changes share by approximately 0.82–1.27 percentage points, depending on monthly N. January zero means no rule match among observed titles, not no fuzzing research.

Matched works: `1902.09334`, `1903.02981`, `1903.08483`, `1904.07280`, `1905.01405`, `1905.06944`, `1905.07147`, `1905.10499`, `1906.00621`. Each [measurement](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/measurements.json) includes the title and exact raw file/entry index/entry ID/SHA-256; all 598 denominator IDs link through the [frozen normalized corpus](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/normalized-records.json). No AI relevance labels were created.

Predeclared sensitivities, all reported: exact `fuzzing` gives **0/0/1/1/2/1 = 5 matches**; current-title and v1-category-subset variants retain nine matches and all six denominators. This is local stability, not proof of historical categories or vocabulary completeness. Excluding nine late IDs leaves n unchanged but N becomes **91/79/96/103/122/98**; March/June shares become **2.0833%/1.0204%**. This is a perturbation of observed real records, **not repaired as-of membership**. Adjacent two-month aggregation gives **1/170, 3/200, 5/228** (0.5882%, 1.5000%, 2.1930%); this smoother appearance is not a growth label or evidence for selecting that window. As-of n/N/p remain null.

## Controlled failure modes and prior art

The [ten controlled checks](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/controlled-checks.json) use synthetic data with hand-specified expectations; they do not measure provider behavior.

| Controlled check | Executed result / implication |
| --- | --- |
| Corpus growth | 10/100 → 20/200: count doubles, share stays 0.1 |
| Denominator drift | 10/100 → 10/200: share halves although matching count is fixed |
| Duplicates/revisions | Repeated v1 and an added v2 preserve 1/10 |
| Missing/invalid title | Two unknowns among three: n/p null, known match=1, bounds 1/3..1 |
| Sparse/small/empty | 1/1 vs 1/2 is unstable; 0/0 share null |
| Alias drift | Stipulated same topic changes “Fuzzing” to “AFL software testing”: lexical count 1→0 |
| Delayed availability | Retrospective bin includes late-public synthetic item; existing as-of fixture excludes stipulated late availability |
| Query selection | Concept-selected subset changes 10/100 to 10/10 |
| Category mutation | Current cs.SE vs v1 outside cs.SE changes inclusion 1→0 |
| Cutoff leakage | Future event excluded; existing fixture rejects future vocabulary and excludes late membership/availability |

Real-data evidence remains separate: [B audit](11_REAL_CORPUS_AUDIT_20261010.md) reports 161 revised works, 55 title differences, four category differences and nine late-ID anomalies. Neither synthetic leakage checks nor exact-v1 replay supplies the missing real historical availability.

Prior-art checks on 10 October: [Manès et al. (2018), v1](https://arxiv.org/abs/1812.00140v1), abstract/history, supplies pre-cutoff topic context, not a reference trend label or complete dictionary. [Štimec et al. (2026)](https://link.springer.com/article/10.1007/s11192-026-05744-5), abstract/introduction, describes title/abstract n-grams, normalization, burst models and plot-based human evaluation; lexical methods alone are not a novelty claim. Their plot judgments do not provide an independent evidence-based reference for this SITES corpus. Kleinberg's burst alternative remains supported by the earlier EL-002 inspection; this execution's PDF fetch failed, so no new full-text verification is claimed. No observed requirement justifies adding burst, persistence or citations. Inspection depth and failures are in the [source log](../../../experiments/research_exit_20260927/runs/20261010-signal-01/source-inspection.json).

## Independent reference protocol — PROPOSED, NOT EXECUTED

Detection quality, independent annotations and researcher agreement are **NOT MEASURED**. A 2018 survey, the regex itself and plots of its output are not trend ground truth. A finite frozen corpus is not an independent random sample of a field.

The [27-work pilot manifest](../../../experiments/research_exit_20260927/runs/20261010-signal-01/reference-pilot-plan.json) is PROPOSED/NOT EXECUTED, with null annotations; its selection strata are organizer-only and must be removed from the blinded review view.

1. Retain fuzzing as the development case and synthetic constant-share corpus growth as the computational control. Record exposure before any new case/control choice; do not choose a replacement concept to improve support. The control cannot establish real-world trend validity.
2. Smallest discriminating pilot: two owner-designated researchers inspect the nine matched works and 18 nonmatches, three per month chosen by a fixed hash order (seed `D08-REF-20261010-01`). Selection occurs **after** signal inspection and is disclosed. Blind annotators to month, match status, counts, plots and each other's decisions; the producing agent is not an independent rater. This balanced pilot detects false positives and some misses; it cannot estimate population recall from 18 negatives or prove trend quality.
3. Rubric: positive = permitted paper evidence establishes fuzzing as a substantive method or research subject; negative = evidence establishes another subject with incidental/irrelevant terminology; uncertain = inaccessible, ambiguous or conflicting evidence. Record exact version/source/section, evidence date, annotator and rationale. Use paper abstracts/method sections and independent context, not presence of the candidate token. No automatic/LLM labels. Historical references need cutoff-valid evidence; otherwise they are retrospective-only.
4. Preserve both raw judgments. A third designated researcher adjudicates disagreements while retaining original uncertainty; missing evidence is not negative. Report pairwise agreement, positive/negative/uncertain totals and TP/FP/FN only against adjudicated independent semantic relevance; describe stratification and uncertainty. A full 598-work independent relevance census would be needed before claiming complete topic recall or reference monthly prevalence; semantic relevance remains distinct from lexical prevalence.
5. Reference trend directions require independent time-indexed substantive evidence with an explicitly aligned construct, population and interval; two researchers may assign positive change / negative change / uncertain with citations. When evidence only gives topic context, all direction labels remain uncertain. Neither count/share nor subjective reading of their plots can generate this reference.
6. Leakage prevention: no Jul–Dec exposure now; keep pilot/rubric outputs development-only, record source versions, hide signal metadata and reconcile the nine exposed IDs before any future accepted split. Freeze the full case/control/rubric/sensitivity/support/quality protocol and owner acceptance before a genuinely unexposed holdout.

**Proposed numeric computational criteria:** zero mismatches in the defined hand-calculated cases; 100% contributing-ID/source lineage; zero replay byte differences in semantic artifacts; zero duplicate contributions. Justification is deterministic correctness, not a statistical quality target. Counts may be reported at n=0, share only when N>0 and fields are known; no finite minimum-support or precision threshold is claimed sufficient for a trend label. **Independent semantic/trend quality threshold and minimum support remain UNRESOLVED, requiring pilot evidence and owner acceptance.** Nine matches cannot justify a confident performance target. If the pilot exposes misses/ambiguity or no aligned independent temporal evidence exists, report INSUFFICIENT EVIDENCE; do not change the regex/threshold after exposure to hide it.

## D08 recommendation and #70 alternatives

**PROPOSED D08:** use normalized lexical share with count and N as mandatory context; retain raw count as the serious simpler alternative. Evidence: real equal-count/different-N months and controlled growth null. Reversal conditions: incomplete denominator, material vocabulary/selection sensitivity, independent relevance disagreement, or inability of reviewers to interpret this narrow construct. These can require abstention, a new prospective development proposal or rejection; they do not authorize burst/LLM scoring. No directional labels or product stack are selected.

| #70 option | Missing evidence / smallest test | Deadline and claim consequences |
| --- | --- | --- |
| A — historical as-of | A specific dated category/announcement capture with provenance, coverage including removals/additions, cutoff-valid field/vocabulary state and enough history for monthly cutoffs; preregister request/byte budget before acquisition; reconcile the nine anomalies and enumerate membership independently of current positives | No qualifying capture verified in B's bounded screen. Test cost is unknown until a source is identified; further abstract pages cannot resolve completeness. High risk to 15 October; retain unchanged E3 and stop dependent work if unmet |
| B — retrospective-only scope proposal | Explicit owner amendment of target/estimand and affected D05/E3/M1/E2 requirements; approve frozen observed 2026-query population and v1-submission bins, lexical rule, reference/support/quality behavior, and new exposure/freeze contract | Most feasible path to a narrow evidence-backed demonstration because frozen data and descriptive evaluation now exist. It abandons claims of historical public availability, complete historical membership and cutoff-valid vocabulary. Original E3 remains NOT PASSED; a new retrospective requirement can check development boundaries/version/lineage but cannot be called original E3 PASS |

**Recommendation: propose Option B for owner review immediately**, given the verified evidence gap and five-day demo horizon. This is a value/feasibility judgment, not acceptance or proof a demo can pass. If the owner retains Option A, locate the specified capture first; if unavailable, preserve M1 NOT PASSED under the existing contract. A demonstrated complete cutoff-valid capture would reverse this recommendation. Option B preserves descriptive corpus comparison, abstention, lineage and replay research value; it loses historical-as-of validity and does not validate user value. No new provider, corpus, physical model, dependency, dashboard or deployment choice follows.

Required owner decisions: A vs B and exact scope amendment; D07 population/time semantics; D08 rule/formula and no-label claim boundary, pilot/rubric and supported quality criteria; any new experiment freeze and exposure-safe split; explicit #70 disposition. D09 is a later decision after accepted Research Exit. GO: owner review and development-only independent pilot once personnel/protocol are agreed. STOP: holdout, #71/#72 dependent implementation, E3/#70 pass, merge, release and deployment.

## Validation and inspectable artifacts

Source: [evaluator](../../../experiments/research_exit_20260927/signal_evaluator.py), [11 new unit tests](../../../experiments/research_exit_20260927/test_signal_evaluator.py), [read-only verifier](../../../experiments/research_exit_20260927/validate_signal.py). **28/28 tool tests + 15/15 legacy synthetic tests + 10/10 controlled cases PASS**. Initial fixture ID conflict was corrected before real measurement. Two corrected processes reproduce semantic artifacts; timestamps/environment remain in separate execution manifests. Independent direct-XML arithmetic verifies all 598 inputs and all nine matching source references. [Verification](../../../experiments/research_exit_20260927/runs/20261010-signal-01/verification.json) retains input/output hashes, parsing/link checks and unchanged D05–D09 statuses; [execution manifest](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/execution.json) retains runtime 3.14.7, code/config SHA-256 and UTC timestamps. Frozen config SHA-256: `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`.

Exact commands from repository root (use an existing Python; this host required escalation because sandbox hid its runtime):

```powershell
python -m unittest discover -s experiments/research_exit_20260927 -p "test_*.py" -v
python experiments/research_exit_20260927/checks.py --output <new-directory>/legacy-checks.json
python experiments/research_exit_20260927/signal_evaluator.py --declaration experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json --output <new-directory>/replay-1
python experiments/research_exit_20260927/signal_evaluator.py --declaration experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json --output <new-directory>/replay-2
python experiments/research_exit_20260927/validate_signal.py --run experiments/research_exit_20260927/runs/20261010-signal-01 --output <new-directory>/verification.json
git diff --check
```

All evaluator/test/replay work was offline; literature-page inspection was separate from corpus measurement. Same-host agent verification and bilingual self-review do not constitute independent scientific validation, user validation, a product benchmark or E1–E8 acceptance. Relative links/parsing are automated; external freshness, anchors and translation meaning are separately limited. See [paired Vietnamese report](https://github.com/Dyu20705/sites/blob/0673903c7cf8e4c6725af8a13f2ca4e40a1457a9/docs/vietnamese/research/14_D08_DEVELOPMENT_EVALUATION_20261010.md).

## Final #64 DoD audit — 11 October 2026

**Verdict: #64 READY FOR OWNER REVIEW as a bounded descriptive proposal with explicit insufficient-evidence outcomes.** This is not issue closure, scientific-quality acceptance, or Research Exit. **Original E3 and #70 remain NOT PASSED.** No threshold, formula, case, corpus, holdout or decision status changed.

Baseline: clean `research/exit-evidence-20260927` at `ed2a21f36b8b0b05efd889279717b61dbe777eda`, upstream equal (0 ahead/0 behind); live PR head and later `git ls-remote` agree. The initial parent checkout is clean `dev@0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`; work was performed only in its existing research worktree. PR #75 is OPEN/Draft with no submitted reviews or inline review threads; #65 CLOSED/completed; #64/#69/#70 OPEN. [Live-state/source inspection record](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/context.json). Owner direction on 10 October authorizes the retrospective proposal, not exact clause acceptance. WIP: #64 only; #70 is a decision gate.

### Findings and bounded correction

- **P0 scientific blockers retained:** historical population/public availability/vocabulary not established; independent semantic/trend quality NOT MEASURED. No human raters designated, zero real annotations. Synthetic A/B/C on SYN-001…027 cannot resolve these gaps.
- **P1 fixed — unsafe validator output:** `validate.py` formerly overwrote historical `results/validation.json`. It now requires a new `--output` and uses exclusive creation. Two subprocess regressions verify existing bytes survive and an omitted path exits 2. README replay commands now point at new paths. Historical validation/checks/evaluator/config/raw/results are unchanged.
- **P1 limited to reuse on other inputs — confirmed membership boundary:** standalone `evaluate()` with a missing `categories_current` field excludes the work and returns an empty-bin n=0, N=0, p=null, instead of identifying unknown membership. [Reproducer and observed output](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary-probe.json). It is not a general fail-closed ingestion interface. The frozen CLI verifies exact input hashes, and all 598 real records have valid cs.SE membership and no exclusions; the published arithmetic is unaffected. Preserve the pinned evaluator. Before broader reuse, require a separately versioned membership guard/correction and regression, or retain the exact fixed-input boundary. This audit does not silently change the experiment contract.
- **P2 clarified — evidence scope:** verification is a different calculation method on the same host, not an independent scientist/machine. The existing packet's seven owner rows remain unfilled; its bytes and version are preserved.

### Requirement → evidence → disposition

Paths below are relative links into the same branch. VERIFIED means only the stated observation; PARTIAL/UNKNOWN/BLOCKED are not converted to PASS by the proposed amendment.

| Requirement | Evidence path | Verification method | Status | Finding | Smallest corrective action |
| --- | --- | --- | --- | --- | --- |
| A1 construct/claims | [14](14_D08_DEVELOPMENT_EVALUATION_20261010.md), [15 §1](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Read EN/VI against actual n/N | VERIFIED | Lexical prevalence of v1 titles among 598 observed works returned by frozen 2026 cs.SE query, retrospectively binned by 2019 submission month; no emergence/causality/semantic recall | Owner decides exact estimand |
| A1 prior art/alternatives/gap | [ledger](01_EVIDENCE_LEDGER.md), [EL-001–005](06_RESEARCH_EXIT_EVIDENCE.md), [09](09_RESEARCH_MASTER_20261010.md), [source review](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/context.json) | Primary abstract/introduction/manual reinspection; prior search provenance reviewed | PARTIAL | Main lexical method and serious count comparator covered; burst is a documented alternative, new Kleinberg PDF fetch failed; historical search metadata incomplete; no novelty established | Keep access limits; targeted novelty search only if a future novelty claim is sought |
| A2 arithmetic/unit/denominator | [independent recount](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/independent-verification.json) | Direct XML parse + independent token-set scanner, no project imports | VERIFIED | 598 distinct works, all nonmatches retained; N=91/79/97/103/122/106, n=0/1/2/1/4/1; 598 source refs and 9 match refs | None for fixed experiment |
| A2 confounders/sensitivity/negative results | [measurements](../../../experiments/research_exit_20260927/runs/20261010-signal-01/corrected-replay-1/measurements.json), [11](11_REAL_CORPUS_AUDIT_20261010.md), [execution](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/execution.json) | Recount all five variants + two-month sums; replay ten synthetic controls | VERIFIED | Corpus growth/denominator/query/alias/revisions/delay/cutoff checks reproduced; late-ID exclusion gives N=91/79/96/103/122/98; exact fuzzing=5; these do not remove selection bias | Preserve all outputs; no new signal justified |
| A2 uncertain input/missing bins | [tests](../../../experiments/research_exit_20260927/test_signal_evaluator.py), [boundary probe](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary-probe.json) | Missing/invalid title/date, empty vs zero, conflict/duplicate/partial-acquisition tests; missing-category probe | PARTIAL | n=0 differs from unknown n and empty N; six bins always explicit for complete input; partial acquisition rejected; general membership helper limitation above | Guard before broader input reuse; do not infer a missing retrieval bin is empty |
| A3 case/control independence/exposure | [03](03_CASE_SELECTION_PROTOCOL.md), [preregistration](../../../experiments/research_exit_20260927/preregistration.json), [15 §7](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Check recorded 2018 context, candidate/exclusion log and chronology | PARTIAL | Fuzzing context independent of plot; synthetic null is computational only; local pre-output timing not independently proven; all 598 exposed; pilot selected after output | Prospective immutable freeze; never relabel development as holdout |
| A3 annotation/roles/uncertainty | [pilot](../../../experiments/research_exit_20260927/runs/20261010-signal-01/reference-pilot-plan.json), [15 §5–6](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Reproduce 27 IDs from seed; inspect null fields, simulator/tests/manifests | BLOCKED | 9 matches + 18 nonmatches, no real labels/personnel; 54 synthetic judgments are fixture choices; scientific accuracy/recall/agreement NOT MEASURED | Owner designates qualified humans and accepts rubric if this route retained; otherwise explicitly chooses limited route |
| A4 exact D08 definition | [corrected declaration](../../../experiments/research_exit_20260927/runs/20261010-signal-01/declaration-corrected.json), [15 §4–6](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Decode pattern/config; 18 boundary cases incl Unicode/underscore; raw recount | VERIFIED | Python Unicode IGNORECASE word boundaries; distinct v1 work, UTC month, n/N; n/N mandatory with share; no directional labels at any support | Accept exact rule/contract; no current approval |
| A4 support/quality/alternatives | [14 reference protocol](14_D08_DEVELOPMENT_EVALUATION_20261010.md), [15 §6/8](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) | Compare mathematical criteria with absent scientific evidence | UNKNOWN | N≥1 defines share, not adequate support; 0–4 matches/month; scientific precision/agreement/minimum-support targets UNRESOLVED; count remains serious alternative | No arbitrary numeric scientific target; pilot and justified prospective criteria if retained |
| A4 decision readiness/freeze | [15 §2/7/9](15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md), [#70](https://github.com/Dyu20705/sites/issues/70) | Compare exact clauses with D05/D06, original M1/E1–E8 and owner direction | BLOCKED for acceptance; VERIFIED proposal exists | Original obligations still authoritative; E2-R/E3-R are proposed substitutions; product E4/E7/E8 outstanding; no accepted freeze | Owner records each choice against immutable packet bytes and this audit limitation |

**Scope of measured science:** exact lexical counts/proportions, field/identity checks and sensitivity perturbations are observations. Scientific field growth, semantic coverage, independent detector accuracy, user value, effect size and human agreement have not been measured. Software tests establish only their tested arithmetic/workflow properties. Proposed E2-R would defer original independent scientific-reference acceptance only by explicit owner choice; E3-R would replace the demo's temporal obligation without repairing historical E3. Neither deferral is active now.

### Claim and reference integrity

Reports 14/15 restrict every substantive conclusion to the finite observed population. Equal-count/different-N months demonstrate normalization's arithmetic effect; a selection-biased denominator remains biased. Five exact-fuzzing matches versus nine broad-rule matches demonstrate vocabulary sensitivity, not semantic recall. Current-title stability on this rule does not negate 55 observed title changes. Nine late IDs remain included under v1 event semantics; subtracting them cannot recover removed/unindexed historical members. Sparse support and only six months support no trend label or causal interpretation.

Reinspection on 11 October: [Manès v1 abstract/history](https://arxiv.org/abs/1812.00140v1) supports pre-2019 topic context only; [Štimec abstract/introduction](https://link.springer.com/article/10.1007/s11192-026-05744-5) supports the lexical/normalization/burst/plot-evaluation comparison, not SITES accuracy. [arXiv manual](https://info.arxiv.org/help/api/user-manual.html), [availability policy](https://info.arxiv.org/help/availability.html), and [terms](https://info.arxiv.org/help/api/tou.html) support the stated version/time distinctions and metadata-versus-paper rights. No dataset API or holdout content was accessed. Kleinberg remains a carried EL-002 inspection, not newly verified full text. No source establishes research novelty; this is not a systematic review or a claim that no historical archive exists.

Real-human follow-up remains minimal and conditional: two qualified owner-designated researchers, third adjudicator for disagreements; fixed 27 IDs, post-output selection disclosed; opaque IDs/random ordering and hidden strata/month/plots; visible words prevent perfect rule blinding. Lock first-pass judgments before revealing source links, log exposure, retain both raw labels and uncertain/pending cases. Evidence-based substantive-topic rubric must not use the regex or plot as truth. Report stratum-specific judgments/uncertainty; do not infer population recall/trend accuracy. No personnel, labels or scientific thresholds are invented here.

### Owner choices — all still PROPOSED except G70 NOT PASSED

| Row / exact packet choice | Alternative | Benefit / cost and scientific limit | Verified evidence / reversal condition |
| --- | --- | --- | --- |
| A1 — §1/2 finite observed-2026 v1-title estimand | Retain original broader question; defer M1 | Reproducible bounded description; relinquishes historical/semantic/detector claims | Recount + #65 negative evidence; reverse if owner requires broader validity or obtains qualifying historical evidence |
| A2 — §2 E2-R/E3-R replacements | Keep original E2/E3 obligations | Testable descriptive demo; does not satisfy original reference/availability requirements | Original E3 unresolved, controls/replay exist; reverse if replacements do not meet research objective |
| A3 — §5/6 limited acceptance with quality NOT MEASURED | Retain independent-reference condition at #70 | Earlier narrow decision; sacrifices scientific accuracy acceptance, not honesty | Zero real labels; reverse on misleading reviewer interpretation or requirement for validated quality |
| D07 — §3 exact 598 observed works, query, v1 UTC event bins, frozen retrieval/provenance/bias | Defer or separately investigate historical capture | Existing complete observed denominator; no historical completeness or field-wide representativeness | 14 hashes/598 refs; reverse on failed identity/completeness checks |
| D08 — §4–6 fixed lexical n/N/share, no labels, null/support/sensitivity/reference contract | Count alone or defer | Share adds denominator context; selection/alias/small-support limits remain | 9/598, all sensitivities; reverse on invalid denominator or misinterpretation; broader helper reuse needs guard above |
| F1 — §7 immutable prospective manifest and exposure discipline | No confirmatory evaluation | Exact replay/reviewer protocol; cannot erase prior exposure | Packet/input/code/output identities exist; acceptance/personnel/task freeze absent; revise on any changed approved bytes or overlap |
| G70 — §9 explicit disposition after accepted criteria have evidence | Keep NOT PASSED | Separates research contract from product readiness; no automatic pass | Acceptance rows unfilled; change only after explicit D07/D08/amendment/freeze acceptance plus every retained research criterion |

The existing packet `M1-R-20261010-v1` is not edited or activated by this audit. Its original Git-blob SHA-256 values remain EN `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`, VI `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`. Acceptance must identify exact version/hash and any revision explicitly. The proposed 5/5 interpretation rubric and 60-second/256-MiB budget are unaccepted/unmeasured engineering/task criteria, not scientifically calibrated thresholds. D09 remains separate.

### Actual validation and review coverage

[Execution record](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/execution.json) retains exact argv, environment, stdout/stderr, exit codes and 13 byte comparisons. Python 3.14.7; Windows; standard library only. **37/37 unit tests PASS** (35 existing + two preservation regressions), **15/15 legacy checks in each of two processes**, **10/10 controls in each signal replay**, two synthetic workflow processes, two corpus audit processes, direct crosscheck and both validators. All successful commands exit 0; deliberately reusing a validator output exits 2 and preserves bytes. The initial default-temp run ran 35 tests with 27 setup/cleanup PermissionErrors (exit 1); setting TEMP/TMP to a writable workspace directory resolved it. No failing assertion was hidden.

Reproduce from repository root (each runner invocation makes fresh ignored scratch directories; no corpus network calls):

```powershell
python experiments/research_exit_20260927/runs/20261011-final-audit-01/run_checks.py
python experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py --output <new-directory>/independent.json
python experiments/research_exit_20260927/runs/20261011-final-audit-01/boundary_probe.py --output <new-directory>/boundary.json
git diff --check
```

| Reproduced frozen artifact | SHA-256 |
| --- | --- |
| audit.json | `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8` |
| normalized-records.json | `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1` |
| measurements.json | `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818` |
| crosscheck.json | `0664d7dcd1ad3d1fd570696b47b254ce54329ffcc56c9b6416482830379c6591` |

The [recount script](../../../experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py) shares no evaluator/parser imports. It compares every v1/current source reference with raw XML, checks all 14 inputs against committed bytes, tests flags/escaping/word boundaries, all sensitivities and exact pilot selection. Separate processes alone are not called independent verification. All frozen input/history files remain unchanged; new run records are separate. Review covers protocols 00/01/03/04, D05/D06/M1/evaluation, paired reports 11–15, declarations/source logs/pilot/measurements, evaluator/audit/crosscheck/simulator/tests/validators and live issues/comments/PR state. Other PR #75 files receive inventory/hash or contextual review only, not an exhaustive security/provider-capability review; historical negative results are preserved. Relative-link existence/parsing and paired numeric tables are checked automatically; EN/VI claim/decision meaning is self-reviewed, not independent translation review.

**Smallest next action:** owner reviews the unchanged exact packet plus this audit, chooses A1/A2/A3/D07/D08/F1 separately, and records a justified G70 disposition. If independent scientific-reference acceptance is retained, designate the humans and justify/freeze prospective criteria before that evaluation. Until then #64 stays open, #70 stays NOT PASSED, and no product/holdout/merge action follows.
