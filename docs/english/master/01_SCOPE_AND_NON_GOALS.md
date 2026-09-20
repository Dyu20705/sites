# 01 — Scope and Non-Goals

The [M1 Definition](../baseline/M1.md) controls the Month-1 scope. This document explains that boundary; it does not expand it.

## 1. Three Scope Horizons

| Horizon | Content | Status |
| --- | --- | --- |
| Long term | Capability chain from evidence acquisition to automation and optimization | Direction, not an implementation commitment |
| Month 1 | Bounded corpus → provenance → minimal normalization → one or two signals → query → dashboard demo | M1 direction and D05/D06 accepted; D07–D09 details remain PROPOSED |
| After Month 1 | Forecasting, recommendation, optimization, automation, and additional data sources | DEFERRED |

## 2. Proposed M1 Scope

**ACCEPTED — D06:** one researcher surveying a technical topic.

**PROPOSED — D07–D09:**

- one technical field;
- one data source;
- no more than 5,000 records;
- no more than 24 completed months of historical data;
- one primary signal, with a second added only if supported by evidence;
- one historical evaluation case.

These figures are **experimental limits**, not a benchmark or a validated workload.

The minimum flow must still cross the full system:

~~~text
acquisition/export
→ observation
→ normalization
→ signal
→ evidence bundle
→ query
→ dashboard
~~~

A separate network API is not required. The minimum dashboard needs to show one result, the signals behind it, and the related evidence.

## 3. Corpus Requirements

The bounded corpus must disclose:

- the query or field definition;
- the applicable date or cutoff;
- the record-selection method;
- coverage and missing data;
- the sampling method if the source returns more records than the limit.

The project must not take the “first 5,000 records” and quietly treat them as representative of the field without assessing selection bias.

## 4. Outside the Month-1 Scope

Under **D03 — ACCEPTED**, M1 excludes:

- forecasting;
- recommendation;
- optimization;
- autonomous agents;
- large-scale distributed infrastructure;
- multiple data sources without evidence that they are necessary;
- opaque LLM-based trend scoring;
- claims that technology A is better than technology B based on paper counts;
- a general-purpose platform, real-time production monitoring, or production operation.

Under **D10 — DEFERRED**, the following also remain deferred:

- global entity resolution;
- a complete ontology;
- broad graph enrichment;
- large-scale full-text mining;
- composite ranking;
- public deployment by default;
- large-scale benchmarking.

## 5. Scope-Creep Control

Before adding a source, signal, or capability, answer four questions:

1. What is missing from the current slice?
2. What evidence shows that the omission affects the M1 objective?
3. What will the addition cost?
4. What work will be removed to protect the deadline?

Then update D06–D09 and implement the change only after human acceptance.

The WIP limit is two. If acquisition or temporal evidence proves infeasible, reduce the **corpus, time range, or number of signals** before expanding the architecture.
