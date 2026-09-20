# 00 — Project Charter

## Summary

**SITES — Scholar Intelligent Trend Evolution System** aims to turn evidence into inspectable knowledge about how science and technology change over time.

Four distinctions matter:

- this is the **project objective**, not a description of a finished system;
- scholarly evidence is the starting data domain, not a permanent limit;
- Month 1 covers only detection and descriptive intelligence;
- broader capabilities remain part of the long-term vision until a new decision accepts them.

## 1. Problem

**HYPOTHESIS:** people surveying a technical field may struggle to separate genuine changes in research activity from noise introduced by corpus size, concept naming, or source coverage.

Month 1 must test this hypothesis with one primary user group. It must not assume that SITES serves every audience.

The intended value is to help a user answer:

- what is changing;
- within which corpus and period;
- according to which signal;
- which evidence produced the result;
- where the conclusion stops being valid.

An observed change in scholarly literature does **not by itself establish** industrial adoption, technical superiority, or business value.

## 2. Long-Term Vision

~~~text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
~~~

This sequence describes the long-term capability space.

- **D03 — ACCEPTED:** M1 is limited to detection and descriptive intelligence.
- **D04 — ACCEPTED:** scholarly evidence is the starting domain.

D04 sets a scope boundary; it does not conclude that papers are always the best source. Patents, software, and market signals have not been evaluated for M1.

## 3. Month-1 Objective

By 17 October 2026, SITES should have a small, reproducible demo that moves from a bounded corpus to an evidence-backed descriptive conclusion.

The [M1 Definition](../baseline/M1.md) specifies the inputs, outputs, and completion criteria. The primary user, corpus, signal, and implementation technology remain undecided.

## 4. Proposed Principles

**PROPOSED — D05:**

- every conclusion must be traceable to its evidence;
- source observations and system-derived claims must remain distinct;
- timestamp semantics must be preserved;
- a result must be reproducible from its input, configuration, code, and metric definition;
- replaying the same input must not duplicate contributions;
- signals must be explainable.

These candidate requirements come from historical material and related research. No current implementation has demonstrated that SITES satisfies them.

## 5. Evidence Priority

When documents or technical claims conflict, use this order:

~~~text
inspectable experiment / empirical evidence
> verified implementation
> accepted ADR or specification
> active issue
> discussion
> assumption
~~~

The order applies only within the version, scope, and time covered by the evidence. An old test does not establish a current capability after the code or contract changes.

External data sources are not absolute sources of truth either. A scholarly API supplies observations within its own coverage and limitations.

## 6. Status Governance

- The [Decision Log](07_DECISION_LOG.md) records decisions and their approvers.
- [Current State](09_CURRENT_STATE.md) records only verified facts.
- The [Prior-Art Map](03_PRIOR_ART_MAP.md) records research sources and lessons from historical designs.
- Git history preserves earlier code and designs for reference, but history does not define the new baseline.

Every project document must distinguish among **vision**, **proposal**, **accepted decision**, and **verified state**.
