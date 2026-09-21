# 08 — Month-1 Gate Plan

**Deadline:** 17 October 2026.

**WIP limit:** no more than two active work items.

~~~text
define-ready → Research Entry → research phase → research-ready → preimplementation-ready
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

## Research work queue

Entry preparation is one work item. Finish its review before activating research execution. The two new issues below are the complete initial queue; historical #36–#61 remain reference material.

| Package | Issue | Deliverables and completion boundary |
| --- | --- | --- |
| A — Evidence and candidate signals | [#64](https://github.com/Dyu20705/sites/issues/64) — OPEN, queued | R1/R2/R6 ledger, definitions and counterevidence, signal comparison, case/control and freeze proposal, limitations, supported D08 proposal or explicit insufficient-evidence report |
| B — Source and corpus feasibility | [#65](https://github.com/Dyu20705/sites/issues/65) — OPEN, queued | R3/R4/R7 provider screening, bounded sample/query/snapshot record, field mapping, missingness/coverage, temporal and access/replay evidence, supported D07 proposal or explicit insufficient-evidence report |

Research Entry was reviewed on 21 September, one day after its planned 20 September target. The 27 September Research Gate remains a target, not a verified completion forecast. Both issues are ready to start after entry closeout; their creation does not mean research execution has begun. Keep at most two active work items.

A first shares signal field requirements from [signal candidates](../research/04_SIGNAL_CANDIDATES.md); B returns feasible fields, denominator constraints and time semantics from the [audit plan](../research/02_SOURCE_AUDIT_PLAN.md). A cannot finalize D08 without B's findings. R5 lineage is required in both packages. R8 remains a later prototype walkthrough with a misunderstanding log; it is not validated by D06 acceptance and is not a third active item.

Follow the [research protocol](../research/00_RESEARCH_PROTOCOL.md) and [entry checklist](../research/05_RESEARCH_ENTRY_CHECKLIST.md). Each issue is complete when its evidence or negative findings are reviewable, limitations and next action are explicit, and its proposal is ready for the owner. Closing an investigation does not accept D07/D08 or pass research-ready. That gate also requires empirical artifacts, a freeze proposal and explicit owner acceptance of D07/D08. D09 remains a later decision.

## If a Gate Fails

When a gate fails:

1. stop work that depends on that gate;
2. continue only independent documentation or analysis;
3. first remove the second signal, narrow the domain/window/corpus, or defer hosting;
4. record how the reduced scope affects the claims and bias;
5. do not drop temporal-isolation or traceability requirements to rescue the demo.

If the minimum slice remains infeasible, conclude **M1 NOT PASSED** and retain the evidence. The deadline must not be rescued by changing the meaning of product-ready.
