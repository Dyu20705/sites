# 06 — Evaluation Protocol

**PROPOSED — D05/D08.** This is a validation plan, not a test result.

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
