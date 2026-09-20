# 05 — Conceptual Data Model

**PROPOSED — D05/D09.** The concepts below form a vocabulary for research and design. They are **not** accepted classes, tables, or a SQL schema.

Implement only the concepts required by the M1 signal.

## Core Concepts

| Concept | Minimum meaning | Boundary |
| --- | --- | --- |
| EvidenceSource | The source that publishes data, its query or export method, and its conditions of use | One source may produce many observations; it is not absolute truth |
| Observation | What a source reported at a specific time or version, with a source reference, snapshot or payload reference, acquisition time, and availability evidence where available | An observation is distinct from a derived claim |
| ScholarlyWork | The scholarly unit analyzed within the corpus | Cross-source canonical identity is DEFERRED; do not automatically merge a preprint and publication |
| Concept / Technology | The tracked concept together with its definition and vocabulary version | Alias matching is a versioned transformation, not a global ontology |
| TemporalMetric | A measured value with units, period, timestamp semantics, and missingness | Distinguish source-supplied metrics from system-calculated metrics |
| Signal | An indicator calculated from a definition, version, and configuration, with a window and denominator | A signal is not automatically a “trend” |
| TrendAssessment | A descriptive conclusion with a rule version, cutoff, signal references, and limitations | It may be insufficient evidence |
| EvidenceLink | A link from assessment → signal → observation → transformation | Lineage must cover every contribution, not only a few representative papers |

Input snapshots and execution records support replay. They do not need separate physical entities unless a concrete requirement calls for them.

## Time Semantics

| Time type | Question answered | Risk if misused |
| --- | --- | --- |
| Appearance / submission | When did this version appear or get submitted? | Not necessarily the publication date |
| Publication | When does the source say it was formally published? | May be precise only to the year or may be revised later |
| Revision | When did the version change? | A revision after the cutoff can leak future information into the past |
| Observation | When did the source or collector observe the value? | Does not prove the value existed at publication time |
| Ingestion | When did SITES ingest the data? | Does not reflect research chronology |
| Metric observation | When was a citation count or other metric measured? | A current total is not the total at a historical cutoff |

Preserve unknown values, timestamp precision, and provenance. Do not manufacture a date for a year-only record without disclosing that policy.

An event date before the cutoff is **not enough** to prove that a field was available at the cutoff. A dataset downloaded today may support only retrospective analysis even when its records carry historical dates.

## Minimum Identity and Deferred Work

**OPEN — Research Gate:** is the counting unit a source record, a version, or a work?

D07/D08 must settle duplicate and version handling because that choice changes the denominator.

The current proposal favors source-local identity within one corpus to keep the scope bounded, while still testing for duplicates and revisions.

**DEFERRED — D10:**

- global canonical identity;
- surrogate-key algorithm;
- fuzzy entity resolution;
- typed relation graph;
- complete citation topology.

If the chosen signal requires any of these capabilities, return to the scope gate instead of silently expanding the data model.
