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

**Status:** ACCEPTED — 20 September 2026, by the project owner.

**Problem:** preserve durable lessons from the earlier design without inheriting its schema or technology stack.

**Accepted principles:**

- conclusion-to-evidence lineage;
- separation of observations from derived results;
- temporal isolation;
- replay and reproducibility;
- idempotency;
- explainability.

Missing evidence may produce **insufficient evidence**. A deterministic calculation must reproduce the same semantic result from the same frozen input/configuration/code; replay must not duplicate contributions. Every conclusion must trace through derived results and signals to contributing observations and source evidence.

**Acceptance record:** in the 20 September 2026 Research Entry planning conversation, the project owner explicitly selected acceptance of D05, including idempotency and the existing E3 requirement, and then requested implementation of that plan. This record preserves that decision; it is not an experiment result.

**Basis:** the [Prior-Art Map](03_PRIOR_ART_MAP.md) and historical material; no M1 experiment exists yet.

**Consequence:** E1–E8 remain required for the M1 demo. If historical field availability cannot be established, use the term retrospective analysis; E3 remains NOT PASSED. This is not an automatic alternative route to passing M1. Metric formulas, reference labels, thresholds and sensitivity settings remain open under D08; no schema or stack is selected by D05.

**Alternatives and review:** deferring the evidence contract would leave research without clear correctness requirements; inheriting the old physical design would fix D09 prematurely. The accepted choice keeps only the invariants. Review scope with the owner if R4 cannot establish temporal evidence; do not relax E3 silently.

## 3. D06 — Primary User and Task

**Status:** ACCEPTED — 20 September 2026, by the project owner.

**Options:**

- a researcher surveying specialist literature;
- an engineer making a technology decision;
- a general user viewing trends.

**Accepted choice:** a researcher surveying a technical topic. Within a defined corpus, the researcher selects a concept/time range, inspects change, understands the signal, opens supporting evidence and understands the limits of the conclusion.

**Acceptance record:** the project owner explicitly accepted this user/task in the 20 September 2026 Research Entry planning conversation and requested implementation of the accepted plan. This enables bounded research; it does not validate user value.

This option matches the scholarly-evidence starting point directly and keeps the scope narrower than a technology-decision use case.

**Missing evidence:** user validation.

**Review point:** R8 after a usable prototype exists. Record a task walkthrough and misunderstandings; if the researcher cannot use or interpret the output, revisit the task with the owner. Engineers and general audiences remain alternatives, not additional M1 targets.

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
