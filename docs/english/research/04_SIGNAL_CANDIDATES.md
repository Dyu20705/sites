# 04 — Signal Candidates

**Status:** candidates for investigation, not accepted metrics. Work package A owns R1/R2/R6 and receives field/temporal findings from B. Formula, counting unit, bin/window, threshold, minimum support and output labels remain open at D08.

| Candidate / construct | Formula family and required data | Confounders and failure modes | Discriminating checks |
| --- | --- | --- | --- |
| Absolute count / observed scholarly activity | Number of matching units in a time bin; requires IDs, concept text/definition and dated observations | Corpus growth, coverage shift, duplicate versions, query selection and publication delay; increasing count does not prove emergence | Independent expected counts; duplicates/revisions; zero versus missing; fixed concept share in a growing corpus |
| Corpus share / relative activity | Matching units divided by eligible corpus units in the same bin; requires a reproducible denominator including nonmatching records | Denominator drift, incomplete retrieval, small support, alias changes and changing provider coverage; normalized values do not remove all bias | Same numerator with changed denominator; stable share despite rising count; empty denominator must not silently become zero |
| Burst / temporary intensity change | Candidate frequency-change model compared with count/share; needs ordered observations and sufficient history | Window/parameter sensitivity, small samples, delayed indexing and one-off spikes | Synthetic spike versus sustained change; vary only preregistered parameters; compare with the simpler baseline |
| Persistence / sustained activity | Candidate repeated-support measure across bins; needs consistent counting and temporal coverage | Arbitrary duration, missing bins mistaken for inactivity, repeated revisions | Sustained activity versus isolated spike; missing-bin scenarios; demonstrate information not already supplied by the baseline |
| Citation dynamics / change in recorded citation activity | Historical citation observations or dated events with demonstrated availability | Censoring, age/cohort bias, citation delay and later values leaking into earlier cutoffs | First establish historical observations; without them do not reconstruct past velocity from current cumulative totals |

Count and share are comparison baselines, not two preselected production signals. Investigate burst/persistence only if literature and data fitness identify a gap; citation dynamics requires the additional historical evidence above. Do not expand to a large metric collection.

For every candidate, record the operational construct, unit, required fields, temporal assumptions, expected benefit, failure evidence and related ledger IDs. The table lists tests to design, not tests already run. All candidates depend on cutoff-valid concept definitions and source observations. Retrospective-only evidence does not pass E3.

## Comparison and D08 handoff

Use independent expected results for increase, decrease, stable, zero/missing, duplicate/revision and future-dated cases. Compare corpus-growth, coverage, alias, query/sampling and publication-delay effects. Define development and holdout use through the [case protocol](03_CASE_SELECTION_PROTOCOL.md); retain negative findings and avoid tuning on holdout.

After B establishes feasible fields and time semantics, propose one primary signal and justify a second only with demonstrated additional information. Submit a D08 proposal containing construct, exact formula/unit/denominator, bin/window, cutoff, minimum support, labels or insufficient-evidence behavior, reference-label method, quality threshold and sensitivity protocol. Cite the supporting literature and empirical artifacts and list unresolved uncertainty. None of those choices is frozen by this document; human acceptance is required before dependent implementation/evaluation.
