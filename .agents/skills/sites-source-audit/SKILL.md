---
name: sites-source-audit
description: Audit candidate scholarly data providers, APIs, exports, datasets, corpus definitions, and sampling plans for SITES. Use before selecting arXiv, OpenAlex, Crossref, Semantic Scholar, DBLP, or any other source, and whenever field coverage, temporal availability, provenance, licensing, replay, missingness, rate limits, or sampling bias affect D07 or the M1 corpus.
---

# SITES Source Audit

Evaluate whether a source can support the M1 research claim before designing around it. Provider popularity is not evidence of suitability.

## Access and operational use

Verify from official material where possible:

- access mechanism and authentication;
- license/terms relevant to storage, redistribution, and demo artifacts;
- quotas/rate limits and expected acquisition cost;
- bulk/snapshot availability versus live API only;
- versioning/deprecation policy when documented.

Do not copy private credentials into artifacts.

## Field fitness

Map the exact fields needed by the candidate indicator and evidence bundle:

- work/source identifier;
- title/abstract or other concept-bearing text if needed;
- publication/submission/update dates with documented semantics;
- venue/type/category fields if used for scope;
- citation/reference fields only if the proposed signal actually needs them;
- provenance needed to reopen the source observation.

Sample real records. Measure missingness/invalid values instead of assuming schema availability means data coverage.

## Temporal validity

For every time field, answer:

- what event it represents;
- whether it can change after first observation;
- whether the value was knowable at historical cutoff T;
- whether the source can reproduce what was available at T;
- whether later corrections/revisions can leak into a retrospective run.

If historical availability cannot be established, label the analysis retrospective and narrow the claim. Do not call it temporally isolated.

## Corpus and sampling bias

Record:

- domain/query definition;
- cutoff and acquisition timestamp;
- ordering/pagination behavior;
- source coverage and known exclusions;
- sampling rule when results exceed the M1 bound;
- duplicate/revision behavior;
- missingness by important strata/time bins where feasible.

Never use “first N records” as a representative sample without checking ordering bias.

## Replay and bounded operation

For M1, test whether the source can support:

- <= 5,000 records and <= 24 months unless a later accepted decision changes these limits;
- stable snapshot identity or a reproducible export;
- idempotent re-ingestion;
- raw observation + provenance retention;
- two independent runs from the same allowed input/config;
- a shareable/replayable demo within the project resource budget.

## Comparative output

For each candidate, report **verified evidence**, **assumptions**, and **unknowns** separately. Compare only dimensions relevant to the M1 claim.

End with:

- feasible candidates;
- disqualifying gaps;
- a **PROPOSED** choice if evidence supports one;
- the smallest sample experiment/audit that would unlock D07;
- what still requires human acceptance.

Do not add a second source merely to repair a poorly chosen metric. First consider narrowing the metric or corpus.
