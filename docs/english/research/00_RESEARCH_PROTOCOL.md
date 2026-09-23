# 00 — Research Protocol

**Entry protocol:** approved for preparation by the project owner on 20 September 2026. D05/D06 are ACCEPTED; D07–D09 remain PROPOSED. This protocol organizes investigation; it does not freeze the corpus, metric, or evaluation thresholds.

## Question and boundary

Investigate [P0 and R1–R8](../master/02_RESEARCH_QUESTIONS.md) for a researcher inspecting descriptive change in a bounded scholarly corpus. Produce evidence for D07 (source/corpus) and D08 (signal/evaluation), within the [M1 definition](../baseline/M1.md). Treat one source, at most 5,000 records and 24 completed months as audit bounds, not an accepted corpus definition. No forecasting, recommendation, architecture selection, or claim of novelty is authorized here.

## Search and screening

Use Google Scholar and Semantic Scholar for discovery, then inspect original papers through publishers, author pages, or repositories. For provider claims, inspect current official API/dataset documentation and terms. Record the actual service, exact query, search date, filters, pages/results screened and access limitations. Query syntax must match the service; the examples below are search families, not guaranteed API expressions.

| Thread | Initial query families and synonyms | Evidence sought | Work package |
| --- | --- | --- | --- |
| Construct | `"emerging technology" bibliometric`, `"technology emergence" scientometric`, scientific activity / publication frequency / corpus share | Definitions, operationalizations, non-equivalence of activity and emergence | A: R1 |
| Signals | `"burst detection" "scientific literature"`, `"publication growth" normalization`, field normalization / denominator / persistence | Main method, serious alternative, assumptions and failure modes | A: R2/R6 |
| Concept definition | `"concept evolution" "scientific literature"`, terminology change / alias drift / vocabulary cutoff | Naming, counting and temporal validity | A+B: R2/R3/R4 |
| Provider/time | Provider name + historical snapshot / version / publication date / metadata update / coverage bias | Field-level availability, coverage, sampling and replay | B: R3/R4/R7 |
| Reproducibility | computational research reproducibility / provenance / idempotency | Trace and replay requirements, threats to validity | A+B: R5/R6 |

For every thread search explicitly for limitations, bias, counterexamples and competing methods, not only supporting evidence. Follow relevant references and citing work; log what was followed. Science mapping and knowledge graphs enter only to answer a specific unresolved RQ. Forecasting stays DEFERRED.

Include sources that define a relevant construct, compare a candidate method, expose a failure mode, or document required data semantics. Retain older foundational work; check current documentation for changing provider behavior. Retain evidence from other domains with its population and transfer limitations. Do not impose an arbitrary publication-year cutoff.

Exclude unrelated prediction/market-ranking work, opaque scores with no relevant inspectable method, and duplicate versions of the same evidence. Log exclusion reasons. Keep preprint/publication version relationships rather than counting them as independent support. A review may guide discovery but cannot replace inspection of the primary evidence for a material claim.

## Capture and synthesis

Use the [evidence ledger](01_EVIDENCE_LEDGER.md). Prefer directly inspected primary evidence and reproducible artifacts; identify secondary synthesis and opinion explicitly. If only an abstract is accessible, record only claims supported by that abstract. Mark inaccessible full text and secondhand citations unresolved; do not infer results from titles.

Capture disagreements as separate claims, including dataset, period, definition and method differences. Synthesize as well-supported within its studied scope, contested/method-dependent, or unknown for SITES. A proposed contribution is not an established research gap: any novelty claim requires a targeted search for the contribution and close synonyms, with its search record.

Stop a thread when the record covers the main method, a serious alternative, failure modes, relevance to the target population, remaining uncertainty and enough evidence to propose or reject a choice. Also stop and report insufficient evidence when access/data limitations prevent a conclusion. Before the 27 September Research Gate, each work package must produce either a supported proposal or an unresolved-evidence report with the smallest next test; the date does not pass the gate. Paper count is not a completion criterion.

## Work and handoff

The [operational backlog](../master/08_MONTH1_BACKLOG.md) defines A (signals) and B (source/corpus), with at most two active work items. A supplies field requirements to B; B returns coverage and temporal findings before A finalizes a D08 proposal. Both maintain R5 lineage. R8 remains a task-based walkthrough after a usable prototype exists; acceptance of D06 is not user validation.

Use the [source audit plan](02_SOURCE_AUDIT_PLAN.md), [case protocol](03_CASE_SELECTION_PROTOCOL.md) and [signal candidates](04_SIGNAL_CANDIDATES.md). No sample acquisition or signal experiment has been performed by creating these documents. Provider, corpus, formula, labels, thresholds and reference-label method still require human acceptance at D07/D08 before dependent implementation or holdout. D09 remains a later gate.

Research Entry is checked separately in the [entry checklist](05_RESEARCH_ENTRY_CHECKLIST.md). Missing historical availability permits retrospective analysis only; E3 remains NOT PASSED and this does not satisfy M1.
