# 08 — Month-1 Gate Plan

**Deadline:** 17 October 2026.

**WIP limit:** no more than two active work items.

~~~text
define-ready → research-ready → preimplementation-ready
→ feature-ready → product-ready v1
~~~

A stage does not become complete merely because its date has arrived. Every status requires its corresponding artifact and evidence.

## Plan

| Period | Objective | Primary artifacts | Gate condition |
| --- | --- | --- | --- |
| 17–18 September — Define | Clean the repository and settle the M1 problem | Charter, M1 definition, decision log, current state | No M0 BLOCKER or MAJOR remains; user/task and required principles accepted |
| 19–20 September — Research entry | Turn the research questions into a bounded investigation plan | Research checklist, source-audit plan, candidate case, selection criteria | Reviewer confirms the questions, required evidence, and research boundary |
| 21–27 September — Research Gate | Select the corpus and signal from evidence | Reading notes, sample audit, coverage/temporal audit, signal comparison | Domain/provider/window, unit, formula, cutoff, minimum support, and quality threshold fixed before holdout |
| 28 September–1 October — Preimplementation | Design the smallest system that can satisfy the evaluation | Minimum contract, fixtures, expected values, runtime budget, D09 | Implementation choices accepted; E1–E8 shown to be feasible |
| 2–7 October — Feature | Build one end-to-end flow | Acquisition → evidence bundle/query/dashboard + tests | Real flow runs; core correctness, trace, and replay checks pass |
| 8–13 October — Evaluation/Demo | Test the case, control, and usability | E1–E8 reports, limitation/disagreement log, reviewer replay | Frozen criteria pass; no post-hoc tuning to hide failure |
| 14–16 October — Packaging | Make the demo reproducible | Replay guide, shareable data, environment record, demo package | Another reviewer completes the replay |
| 17 October — Final | Review M1 and answer the primary research question | Gate checklist, demo, research result, updated current state | Contract and E1–E8 confirmed within the M1 boundary |

## If a Gate Fails

When a gate fails:

1. stop work that depends on that gate;
2. continue only independent documentation or analysis;
3. first remove the second signal, narrow the domain/window/corpus, or defer hosting;
4. record how the reduced scope affects the claims and bias;
5. do not drop temporal-isolation or traceability requirements to rescue the demo.

If the minimum slice remains infeasible, conclude **M1 NOT PASSED** and retain the evidence. The deadline must not be rescued by changing the meaning of product-ready.
