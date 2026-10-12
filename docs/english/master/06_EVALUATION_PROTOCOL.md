# 06 — Evaluation Protocol

**Current authority — 12 October 2026:** [owner approval](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874) accepts A1/A2/A3/D07/D08/F1 in [M1-R-20261010-v1](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md). D05/D06 remain ACCEPTED; only the specified M1/D05 temporal application and E2/E3 demo obligations are amended. The accepted output is retrospective lexical n/N/share for the frozen 598-work corpus; no trend labels or historical-as-of claim. Original E3 remains **NOT PASSED**; independent scientific quality **NOT MEASURED**.

[Verified Research Exit](../research/17_RESEARCH_EXIT_20261012.md): **RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY**. D09 remains **PROPOSED**; #71 design is allowed, #72 build awaits separate owner acceptance. Deadline: **15 October 2026**.

**Gate allocation now accepted:** G70 covers owner decisions, F1, frozen corpus/arithmetic/lineage, synthetic workflow, controls and research E2-R/E3-R. Product E1/E3-R/E5/E6 integration, E2-R interpretation, E4 independent replay, E7 five-of-five task/navigation and measured E8 remain later demo obligations after D09. Budget: ≤598 works, ≤60 seconds, ≤256 MiB peak process memory, zero live corpus requests. Reviewer identity/exposure/runtime must be recorded before a new task; no reviewer result or measured E8 yet.

## Historical baseline — retained for comparison

The text below records earlier decisions/plans. The exact accepted amendment and current section above supersede conflicting scope, status and execution dates; preserved obligations still apply.

**Amendment pending, 10 October:** owner selected retrospective-only direction and authorized [M1-R-20261010-v1](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md). Its E2-R/E3-R and quality/support/budget choices remain PROPOSED; the original matrix below is not silently replaced. SIMULATED workflow checks do not satisfy independent scientific-reference quality. Original E3 remains NOT PASSED; an accepted retrospective contract would not make it original E3 PASS.

**D05 principles ACCEPTED; D08 evaluation choices PROPOSED.** This is a validation plan, not a test result. E1–E8 remain required; formulas, reference labels, thresholds and sensitivity settings still require D08 acceptance. Calling an analysis retrospective does not pass E3 or M1.

The protocol must be fixed **before implementation and before inspecting holdout results**.

## 1. What M1 Evaluates

M1 evaluates only whether SITES can describe change within a defined corpus.

M1 does **not** evaluate:

- future prediction;
- which technology is better;
- market success;
- production scalability.

The evaluation must separate four questions:

1. Is the calculation correct?
2. Is the evidence complete and appropriate?
3. Can the result be explained?
4. Does the detection match the defined evaluation case?

A running demo does not establish that the detection is useful.

## 2. Evaluation Design

1. Decide the user task, domain/query, corpus/window, counting unit, signal, threshold, and minimum support; freeze them before the holdout run.
2. Build synthetic examples with independently calculated expected results: increase, decrease, no change, zero/missing, duplicate/revision, and a future-dated observation.
3. Select one historical case and one control case; record the selection criteria before viewing system output.
4. For an **as-of evaluation**, every field used at cutoff T needs evidence that it was available no later than T.
5. Without availability evidence, describe the work only as a **retrospective case analysis**, not a backtest.
6. Run sensitivity analysis for reasonable changes to the window and threshold and for removal of records with missing fields; retain negative results.
7. Replay must use frozen input and must not depend on a live API.

## 3. Acceptance Matrix

| ID | Check | Evidence to retain | Pass condition |
| --- | --- | --- | --- |
| E1 | Deterministic correctness | Small fixture, independently calculated expected value, actual value, and diff | Every defined case is correct; floating-point tolerance fixed in advance |
| E2 | Historical case + explainability | Case protocol, control, components, annotation, disagreement, and sensitivity results | At least one case and one control; reviewer can explain every label; quality threshold fixed in advance |
| E3 | Temporal isolation | Availability audit, cutoff/configuration/vocabulary record, and injected future records | No input violates the cutoff; future records do not change output before T; missing availability evidence ⇒ NOT PASSED |
| E4 | Reproducibility | Snapshot identity, configuration, code version, metric definition, environment, and output | Two independent runs produce the same semantic output |
| E5 | Traceability | Complete lineage and evidence bundle | Every demo assessment traces to its signal and all contributing observations |
| E6 | Idempotency | Replay on the same input with count and signal comparison | No contribution is duplicated; semantic output is unchanged |
| E7 | Usability | Task-based walkthrough | A reviewer selects a concept/window, reads the result, understands the signal, and opens the evidence without editing code |
| E8 | Bounded operation | Corpus size, coverage, missingness, runtime, and resource use where measurable | Meets a budget fixed in advance; makes no scalability claim |

## 4. E2 Caveat

Completing a report does **not** establish acceptable detection quality.

Before evaluation, the Research Gate must define:

- the metric or rubric;
- how reference labels will be created;
- limitations;
- the pass/fail threshold.

Precision and recall are meaningful only when the reference labels are sufficiently independent and appropriate. An annotation must not be called “trend truth.”

## 5. Demo Acceptance

A reviewer other than the author must:

- replay the system from an approved snapshot;
- inspect at least one evidence bundle;
- complete E7;
- record the environment and result.

M1 passes when:

- the required gates have been accepted;
- every applicable E1–E8 criterion passes;
- a demo exists by 17 October 2026;
- no BLOCKER or MAJOR issue remains in correctness, temporal semantics, or traceability.

If the data is inadequate or the signal fails the frozen criterion, record **M1 NOT PASSED / scope review required**. Do not change the threshold after evaluation to rescue the demo.
