# SITES agent operating contract

This file governs AI/coding agents working in this repository. It complements the project documents; it does not replace accepted decisions or verified evidence.

## Current project boundary

SITES is on the Month-1 path from project definition to one reproducible vertical slice. The committed direction is scholarly evidence -> descriptive trend intelligence -> evidence-backed query/dashboard demo.

Do not silently expand Month 1 into forecasting, recommendation, optimization, autonomous-agent product features, multi-source infrastructure, distributed systems, or production-scale operation.

Read these before material work:

1. `docs/vietnamese/baseline/M1.md`
2. `docs/vietnamese/master/07_DECISION_LOG.md`
3. `docs/vietnamese/master/08_MONTH1_BACKLOG.md`
4. `docs/vietnamese/master/09_CURRENT_STATE.md`
5. the task-specific skill under `.agents/skills/`

The current-state document is a dated snapshot. When a state claim affects the task, verify repository/PR/issue state directly instead of treating an old snapshot as current.

## Evidence and status discipline

Keep these categories distinct:

- **FACT / VERIFIED**: supported by inspected source, executable evidence, or reproducible observation.
- **ASSUMPTION**: adopted temporarily so work can proceed; state it explicitly.
- **HYPOTHESIS**: claim to test, not a conclusion.
- **PROPOSED**: recommendation awaiting acceptance.
- **ACCEPTED**: explicitly approved in the decision log or by the project owner.
- **REJECTED / DEFERRED / SUPERSEDED**: historical decision state; do not resurrect silently.

Evidence priority for project claims:

```text
reproducible experiment / directly inspected primary evidence
> verified implementation + tests
> accepted decision/spec
> active issue/PR
> discussion
> assumption
```

Git history is historical evidence, not the current architecture.

## Human decision gates

Do not change the status of D05-D09, or make equivalent high-impact choices, without explicit human acceptance.

This includes material choices about:

- project/research scope and target user;
- data provider/corpus and temporal semantics;
- metric/threshold/reference-label protocol;
- architecture, physical data model, database/framework/dashboard/deployment;
- security boundary, new runtime dependency, irreversible migration, release, or production operation.

You may research, prototype, benchmark, or prepare a reversible proposal before acceptance. Label the result **PROPOSED** and stop before dependent implementation that would implicitly lock the decision.

## Execution boundaries

- WIP limit for SITES: at most 2 active work items.
- Prefer the smallest end-to-end artifact that advances the current gate.
- Never merge to the default branch, publish a release, deploy to production, rewrite Git history, force-push shared branches, handle real secrets, or perform destructive/irreversible migrations autonomously.
- Batch repository changes into logical commits and avoid repeated remote commit/push churn.
- Generated code, research synthesis, and reviews are unverified until checked.
- Do not claim tests, benchmarks, citations, or user validation that were not actually performed.
- For implementation tasks, define interfaces/invariants and acceptance checks before large code generation.

## Skill routing

Use the narrowest relevant skill:

- `sites-research-evidence`: literature/prior-art, methodology, novelty/gap, evidence synthesis.
- `sites-source-audit`: scholarly provider/API/corpus feasibility, field coverage, temporal availability, sampling and replay.
- `sites-decision-gate`: architecture/product/research choices that can lock scope or implementation.
- `sites-review`: PR/diff/docs/research/code review and gate verification.
- `sites-security-review`: defensive security guidance and review. Full vulnerability-audit workflows remain explicit opt-in work and require sandbox controls.

See `.agents/README.md` for provenance, deferred integrations, and activation guidance.

## Definition of useful completion

A task is complete only when its output is inspectable and its validation is stated.

For research: cite primary sources where possible and identify unresolved uncertainty.
For data/source work: record query/snapshot/cutoff/coverage/missingness and known bias.
For implementation: run the smallest relevant tests/checks and report exact results.
For review: account for reviewed scope and distinguish confirmed defects from unverified concerns.
For decisions: record alternatives, trade-offs, evidence, recommendation, and the explicit acceptance still required.

When the task is educationally important, explain the mechanism or decision rationale rather than only providing an artifact.
