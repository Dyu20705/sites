# 07 — Decision Log

**Created:** 18 September 2026.

Valid statuses: **PROPOSED, ACCEPTED, REJECTED, DEFERRED, SUPERSEDED**.

ACCEPTED means only that an authorized person approved the decision. It does **not** prove that an implementation exists or works correctly.

## 1. Accepted Decisions

| ID | Decision | Basis | Consequence |
| --- | --- | --- | --- |
| D01 | Preserve Git history; clean up HEAD; do not restore the old implementation. **ACCEPTED — 18 September 2026** | Project owner’s reset/M0 request | Do not restore old code or configuration merely to match documents; do not rewrite history |
| D02 | Historical documents and issues are reference material; the M0 baseline is not bound to the old architecture. **ACCEPTED** | Reset/M0 and retirement of issue graph #36–#61 | Re-evaluate every new stack or model choice |
| D03 | M1, from 17 September to 17 October, focuses on detection and descriptive intelligence. **ACCEPTED** | Month-1 objective | Forecasting, recommendation, optimization, agents, and large infrastructure remain outside M1 |
| D04 | Scholarly evidence is the starting domain; separate vision from current state and use an evidence hierarchy. **ACCEPTED** | M0 requirement | Do not select a provider by default; do not assume papers are the “best” source |

## 2. D05 — Evidence and Correctness

**Status:** PROPOSED.

**Problem:** preserve durable lessons from the earlier design without inheriting its schema or technology stack.

**Proposal:**

- conclusion-to-evidence lineage;
- separation of observations from derived results;
- temporal isolation;
- replay and reproducibility;
- idempotency;
- explainability.

**Basis:** the [Prior-Art Map](03_PRIOR_ART_MAP.md) and historical material; no M1 experiment exists yet.

**Current recommendation:** the demo must pass E1–E8 checks; a dashboard alone is insufficient.

**Review point:** Define/Research Gate. If the data cannot support temporal evidence, narrow the claims.

## 3. D06 — Primary User and Task

**Status:** PROPOSED.

**Options:**

- a researcher surveying specialist literature;
- an engineer making a technology decision;
- a general user viewing trends.

**Current recommendation:** a researcher surveying a technical topic.

This option matches the scholarly-evidence starting point directly and keeps the scope narrower than a technology-decision use case.

**Missing evidence:** user validation.

**Review point:** Define Gate, or when R8 shows that the task does not provide value.

## 4. D07 — Field, Data Source, and Corpus

**Status:** PROPOSED.

Previously mentioned sources such as arXiv, OpenAlex, Crossref, Semantic Scholar, and DBLP are **candidates** only. None has a fixed role.

**Current recommendation:**

- one technical field;
- one data source;
- no more than 5,000 records;
- no more than 24 completed months of history;
- one historical evaluation case.

Before selecting a provider, audit access and licensing, field coverage, missingness, and temporal availability.

If a source lacks a field, first change the signal or narrow the corpus before adding a second source.

## 5. D08 — Signals, Labels, and Evaluation

**Status:** PROPOSED.

**Directions under consideration:** count/share, burst/persistence, and citation dynamics.

**Current recommendation:** begin with one deterministic count/share-based signal if the data audit supports it. Add a second signal only when it provides demonstrated additional value.

Not yet decided:

- formula;
- bin/window;
- threshold;
- minimum support;
- label set;
- reference-label method;
- quality threshold.

A rising count alone must not be interpreted as emerging.

## 6. D09 — Minimum Implementation

**Status:** PROPOSED.

Options to consider:

- files versus an embedded database versus a database service;
- in-process queries versus an HTTP API;
- local versus hosted dashboard;
- dictionary/rules versus a learned model.

**Principle:** choose the smallest option that still supports replay, query, dashboard, and evaluation.

The current recommendation is a local demo with in-process queries unless a clear need for a network API appears.

The framework, database, dashboard stack, deployment, identity strategy, and use of ML or LLMs **have not been accepted**.

## 7. D10 — Deferred Work

**Status:** DEFERRED.

The following remain deferred:

- global canonical identity and schema;
- generic source registry;
- broad graph enrichment;
- distributed scaling;
- large benchmark;
- public deployment by default.

Earlier choices are not permanently prohibited; they are simply not inherited automatically.

## 8. Updating the Log

Every status change must record:

- who approved it;
- the date;
- the supporting evidence or artifact;
- the reason for the change.

No decision becomes ACCEPTED merely because an AI agent proposed it or because it appeared in project history.
