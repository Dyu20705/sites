# 14 — D08 development evaluation and owner decision packet

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

All evaluator/test/replay work was offline; literature-page inspection was separate from corpus measurement. Same-host agent verification and bilingual self-review do not constitute independent scientific validation, user validation, a product benchmark or E1–E8 acceptance. Relative links/parsing are automated; external freshness, anchors and translation meaning are separately limited. See [paired Vietnamese report](../../vietnamese/research/14_D08_DEVELOPMENT_EVALUATION_20261010.md).
