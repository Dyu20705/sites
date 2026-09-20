# 02 — Research Questions

Every question below is **OPEN**. These are claims to test, not conclusions.

The [M1 Definition](../baseline/M1.md) sets the scope; the [Evaluation Protocol](06_EVALUATION_PROTOCOL.md) defines how it will be assessed.

## Primary Research Question — P0

> Within a corpus of scholarly documents from a specific technical field, are one or two simple signals sufficient to determine whether a concept is appearing more or less often over time, while preserving the ability to inspect the source data and calculation and reproduce the result?

The aim is to test a limited claim before applying broad labels such as “emerging technology.”

The minimum evidence includes:

- a corpus audit;
- a signal definition;
- synthetic examples with independently calculated expected results;
- one historical case and one negative or control case;
- an evidence bundle;
- a replay report.

## Supporting Questions

| ID | Question | Required evidence | Decision enabled |
| --- | --- | --- | --- |
| R1 | What does “trend” measure within the corpus: frequency, share, novelty, or impact? | Definitions from the literature, examples, and counterexamples | Claim boundary and D08 output labels |
| R2 | Which signal is feasible with M1 data, and how sensitive is it to noise? | Comparison of count/share with burst/persistence; missingness, sensitivity analysis, and negative controls | D08 signal, formula, and threshold |
| R3 | Which minimum fields are required, and what coverage is sufficient? | Data sample, missingness over time, access/license review, and query completeness | D07 source, corpus, and period |
| R4 | Can the project establish which fields existed at cutoff T? | Snapshot or version availability, timestamp audit, and future-data tests | As-of evaluation or retrospective analysis only |
| R5 | Can a result be traced to the records and transformations that produced it? | Walkthrough from output to signal to observation; input/configuration/code references | D05/D09 evidence contract |
| R6 | Can the historical case be evaluated without hindsight tuning? | Rule frozen before holdout, independent annotation, control, and disagreement log | D08 evaluation protocol |
| R7 | Is one source sufficient, or does a second source correct a measurable deficiency? | Coverage audit, reconciliation cost, and temporal consistency | D07 one-source or multi-source decision |
| R8 | Can the primary user understand and use the output for a literature-survey task? | Task-based walkthrough and misunderstanding log | D06 user and use case |

## Operational checks and ownership

The evidence and decision mappings above remain open research questions. Acceptance of D05/D06 sets requirements and a target user, not answers to R5/R8. A and B refer to the two [research work packages](08_MONTH1_BACKLOG.md); the [research protocol](../research/00_RESEARCH_PROTOCOL.md) governs evidence capture.

| RQ | Construct to operationalize | Failure / falsifier to investigate | Owner and handoff |
| --- | --- | --- | --- |
| R1 | Activity/frequency/share versus novelty/impact | The chosen definition infers emergence or impact from count alone | A → D08 claim boundary |
| R2 | Sensitivity of the candidate signal to activity and confounders | The conclusion changes mainly because of denominator, coverage, alias, query or window choices | A with B field evidence → D08 |
| R3 | Field fitness and corpus coverage | Essential fields are missing, invalid or uneven across time, so the intended metric cannot be supported | B → D07 and A requirements |
| R4 | Availability of each value at cutoff T | Only present-day metadata or event dates exist; historical knowability cannot be established | B → D07/D08; retrospective only, E3 NOT PASSED |
| R5 | Traceability and reproducibility of a claim | A contributing record, transformation or input/configuration version cannot be reconstructed | A+B throughout; later executable D05 checks and D09 design |
| R6 | Independent evaluation without hindsight selection/tuning | Case or reference labels depend on signal output, or thresholds change after holdout exposure | A with B feasibility → D08 |
| R7 | Sufficiency of one source | A required deficit persists after narrowing the signal/corpus; another source must have a measured benefit | B → D07; no automatic multi-source expansion |
| R8 | Task comprehension and utility | The researcher cannot explain the signal, locate evidence or recognize the claim boundary | Later prototype walkthrough → revisit D06 if needed; not completed by acceptance |

P0 fails within the tested scope if no feasible signal survives these checks while retaining trace/replay and temporal evidence. Preserve that negative result rather than changing the question after evaluation.

## Signal Hypothesis

**HYPOTHESIS:** count/share over time is an inspectable baseline, but it may produce a false trend when corpus size or concept naming changes.

Alternatives such as burst and persistence may add information, but neither has been selected.

Citation velocity, acceleration, and influential growth require historical observations of the metric. A current cumulative citation count cannot reconstruct citation state at a past cutoff.

Concept emergence, diffusion across venues or institutions, and frontier papers come from earlier designs and are not automatically part of M1.

**Insufficient evidence** is a valid result. The system does not need to force every concept into emerging, growing, stable, or declining.
