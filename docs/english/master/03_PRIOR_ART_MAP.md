# 03 — Prior-Art Map

This document is a **survey map**, not a complete literature review.

**Sources checked:** 18 September 2026.

Here, **VERIFIED** means only that the citation and the described content were checked against the source. It does not mean that the method has been shown to work for SITES.

## 1. Scholarly Sources Checked So Far

| Source | What was checked | Relevance to SITES |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/abs/1503.00673) | The abstract identifies five attributes of emerging technologies: radical novelty, relatively fast growth, coherence, prominent impact, and uncertainty or ambiguity | R1: a rising count should not be treated as equivalent to an “emerging technology” |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/kdd02.html) | The author’s page describes a burst as a bounded period in which a feature appears with high intensity; the algorithm models changes in frequency over time | R2: burst detection is a candidate signal, but it does not prove that a technology is important or superior |
| Sandve et al. (2013), [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | The rules call for recording how results were produced, including inputs, parameters, workflows, and software versions | R5/R6: supports replay records and provenance requirements |

Limits of the current reading:

- **Rotolo:** only the abstract has been checked; the full paper has not received a critical review;
- **Kleinberg:** the descriptive page and paper have been checked, but the algorithm has not been tested on a SITES corpus;
- **Sandve:** the relevant rules have been checked, but SITES has not run an experiment against them.

None of these sources establishes that a particular metric is suitable for SITES.

## 2. Research Areas Requiring Further Study

| Area | Evidence to produce | Relevance | Status |
| --- | --- | --- | --- |
| Scientometrics / bibliometrics | Coverage bias, field and age normalization, limits of counts and citations | R1–R3 | TO RESEARCH |
| Science mapping | Co-word and co-citation methods, unit of analysis, and risks when interpreting clusters | R1/R3 | TO RESEARCH |
| Emerging-technology detection | Full reading of Rotolo and methods that operationalize emergence | R1/R2 | TO RESEARCH |
| Burst detection | Kleinberg paper, assumptions, tuning, and a simple baseline | R2/R6 | TO RESEARCH |
| Temporal citation dynamics | Censoring, delay, as-of availability, and cohort bias | R2/R4 | TO RESEARCH |
| Topic and concept evolution | Alias drift, vocabulary cutoff, and dictionary-based versus learned topics | R3/R4 | TO RESEARCH |
| Technology forecasting | Clear separation between detection and prediction | After M1 | DEFERRED |
| Scholarly knowledge graphs | Work/version identity and provenance | R3/R5/R7 | TO RESEARCH; full graph DEFERRED |
| Reproducible computational research | Turn the principles into executable replay and trace checks | R5/R6 | TO RESEARCH |

Each subsequent research note should record the source and version, question, original method and data, finding, limitation, applicability to SITES, and related decision.

## 3. Lessons from Historical Designs

**HISTORICAL — not academic prior art.**

The README, four design/academy documents at snapshot [9b9f8ee](https://github.com/Dyu20705/sites/tree/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7), and issues #36–#61 were inspected.

Historical documents:

- [English design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/design/scholarly-data-platform.md)
- [English academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/english/academy/scholarly-data-model.md)
- [Vietnamese design](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/design/scholarly-data-platform.md)
- [Vietnamese academy](https://github.com/Dyu20705/sites/blob/9b9f8ee1dabde0df26c42e0f9d5feb11a4fd1bb7/docs/vietnamese/academy/scholarly-data-model.md)

| Historical lesson | Evidence | Use in M0 |
| --- | --- | --- |
| Observations must remain separate from derived claims, with traceable provenance | [#47](https://github.com/Dyu20705/sites/issues/47), [#57](https://github.com/Dyu20705/sites/issues/57), [#59](https://github.com/Dyu20705/sites/issues/59) | PROPOSED D05 requirement; do not inherit old dataclasses or tables |
| Timestamp types differ and can introduce look-ahead leakage | [#46](https://github.com/Dyu20705/sites/issues/46) | PROPOSED temporal invariant; the new dataset still requires an audit |
| Replay must bind input, configuration, code, metric, and output; reruns must not duplicate contributions | [#45](https://github.com/Dyu20705/sites/issues/45), [#55](https://github.com/Dyu20705/sites/issues/55) | PROPOSED reproducibility and idempotency requirement |
| Identifiers, versions, relations, and identity are not interchangeable | [#48](https://github.com/Dyu20705/sites/issues/48), [#60](https://github.com/Dyu20705/sites/issues/60) | Minimum semantics are required; global canonical identity is DEFERRED |
| Velocity, acceleration, influential growth, emergence, persistence, diffusion, and frontier papers | [#52](https://github.com/Dyu20705/sites/issues/52), [#53](https://github.com/Dyu20705/sites/issues/53), [#54](https://github.com/Dyu20705/sites/issues/54) | Candidate/HYPOTHESIS; do not treat a composite score as ground truth |
| Extensibility and performance require empirical evidence | [#56](https://github.com/Dyu20705/sites/issues/56), [#58](https://github.com/Dyu20705/sites/issues/58), [#61](https://github.com/Dyu20705/sites/issues/61) | Test only the M1 workload; generic registries and large benchmarks are DEFERRED |

## 4. Historical Choices Not Carried Forward

**HISTORICAL CANDIDATE — NOT ACCEPTED IN CURRENT BASELINE:**

DuckDB, the Medallion pattern (Bronze/Silver/Gold), Parquet, uv, a 13-table schema, canonical UUIDv5 identifiers, a stub lifecycle, the Source Authority Priority Matrix, earlier canonical schemas, a four-provider architecture, arXiv-first, fixed roles for OpenAlex/Crossref/Semantic Scholar, SourceRegistry, Observation dataclasses, and earlier provider adapters.

This does **not** mean that these choices were wrong. It means they are not inherited automatically by the new baseline.

The #36–#61 issue graph is historical material. The fact that #57 was once marked complete does not establish that its implementation still exists.
