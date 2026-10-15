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

Current status and accepted amendment: see §9; dated historical statements below remain preserved.

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

**Status:** ACCEPTED — 12 October 2026, Dyu20705, [owner record](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874); exact M1-R-20261010-v1.

**Accepted choice:** One frozen arXiv current cs.SE observed-query population: 598 distinct works, exact v1 titles, January–June 2019 UTC v1-submission bins, current category membership and null public availability. No historical population claim; preserve all raw evidence and denominator members.

See [F1 and Research Exit evidence](../research/17_RESEARCH_EXIT_20261012.md).

**Historical proposal below (superseded for current scope):**

**27 September evidence update:** [D07/D08 packet](../research/08_D07_D08_EXIT_PACKET.md) records an insufficient-evidence outcome, documented access failures and remaining temporal/sample gaps. No provider/corpus acceptance or evaluation freeze is recorded.

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

**Status:** ACCEPTED — 12 October 2026, Dyu20705, [owner record](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874); exact M1-R-20261010-v1.

**Accepted choice:** Exact versioned fuzzing title rule; n, N and n/N, mandatory support/null/bounds, all declared sensitivities, no directional labels. E2-R/E3-R limited demo route accepted; real independent quality NOT MEASURED. Original E3 NOT PASSED; product reviewer and budget measurements remain pending.

See [F1 and Research Exit evidence](../research/17_RESEARCH_EXIT_20261012.md).

**Historical proposal below (superseded for current scope):**

**27 September evidence update:** [synthetic comparison and literature notes](../research/06_RESEARCH_EXIT_EVIDENCE.md) support further count/share investigation, not real-corpus quality. Support, labels and quality thresholds remain unresolved in the [packet](../research/08_D07_D08_EXIT_PACKET.md).

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

**Status:** ACCEPTED — 12 October 2026, Dyu20705,
[owner record](https://github.com/Dyu20705/sites/issues/71#issuecomment-6123995295);
exact D09-M1-20261012-v1, SHA-256
`a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc`.

**Accepted choice:** CPython standard library, immutable files, strict
in-process projection/query, and generated local HTML/SVG for the 21 fixed
windows. No database, HTTP service, third-party dependency, JavaScript, ML/LLM,
live provider access, hosted deployment, or silent expansion beyond the
retrospective descriptive M1 scope. See the
[as-built demo contract](../product/00_M1_OFFLINE_DEMO.md).

Acceptance passed PREIMPLEMENTATION-READY and authorizes #72. It does not pass
FEATURE-READY, E7, E8, independent scientific quality, release, or deployment.

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

## 8. Owner scope direction — 10 October 2026 — historical, superseded by §9

**ACCEPTED direction, not D07/D08 acceptance:** [owner #70 decision](https://github.com/Dyu20705/sites/issues/70#issuecomment-6097713689) accepts #65's completed negative investigation and development-only empirical evidence, selects retrospective-only M1 direction and authorizes a controlled exact amendment proposal. D05/D06 remain ACCEPTED; their original obligations remain until an exact amendment is accepted. Original E3 and #70 remain NOT PASSED. D07/D08/D09 statuses above remain PROPOSED.

The [M1-R-20261010-v1 packet](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md) proposes the exact estimand, clause impacts, D07/D08, separate E2-R/E3-R and freeze/quality choices. The owner's subsequent session instruction permits SIMULATED A/B/C and synthetic workflow testing; independent scientific quality stays NOT MEASURED. Permission to simulate is not scientific-reference acceptance or an implicit waiver at #70. No thresholds, freeze, architecture or Research Exit pass are recorded as accepted here.

## 9. Exact amendment acceptance and verified Research Exit — 12 October 2026

**Current authority — 12 October 2026:** [owner approval](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874) accepts A1/A2/A3/D07/D08/F1 in [M1-R-20261010-v1](../research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md). D05/D06 remain ACCEPTED; only the specified M1/D05 temporal application and E2/E3 demo obligations are amended. The accepted output is retrospective lexical n/N/share for the frozen 598-work corpus; no trend labels or historical-as-of claim. Original E3 remains **NOT PASSED**; independent scientific quality **NOT MEASURED**.

[Verified Research Exit](../research/17_RESEARCH_EXIT_20261012.md): **RESEARCH-READY PASSED — RETROSPECTIVE DESCRIPTIVE SCOPE ONLY**. D09 was separately accepted later through the #71 owner record above; PREIMPLEMENTATION-READY passed and #72 was authorized. Deadline: **15 October 2026**.

F1 verified under SHA-256 `bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`. Owner acceptance is external to the unchanged packet-15 bytes. This supersedes the pending-decision statements in the historical entries above, without upgrading original E3 or scientific quality. G70 itself did not accept an architecture, dependency, or product gate; the separate #71 record accepts only the exact D09 boundary and preimplementation gate.

## 10. Updating the Log

Every status change must record:

- who approved it;
- the date;
- the supporting evidence or artifact;
- the reason for the change.

No decision becomes ACCEPTED merely because an AI agent proposed it or because it appeared in project history.
