---
name: sites-decision-gate
description: Decision-gate protocol for SITES. Use whenever work could lock research scope, target user, provider/corpus, metric/threshold, architecture, data model, dependency, database, framework, dashboard, deployment, security boundary, or release behavior. Produce a decision proposal and stop before implicit acceptance.
---

# SITES Decision Gate

Make high-impact choices explicit, comparable, reversible where possible, and owned by the human project owner.

## Classify the decision

A decision needs a gate when changing it later would materially affect:

- the research question or validity of results;
- data meaning/provenance/temporal semantics;
- multiple downstream components;
- security/privacy or external cost;
- migration/compatibility;
- the Month-1 deadline or non-goals.

Low-impact, local, reversible implementation details may be chosen within an already accepted contract and should not be escalated unnecessarily.

## Decision record

### Decision
One sentence describing the choice.

### Status
`PROPOSED` unless an existing accepted decision already authorizes it.

### Goal and constraints
Include the relevant M1 gate, deadline/scope/resource constraints, and invariants.

### Evidence
Separate verified evidence from assumptions. Link experiments, source audits, docs, or benchmarks.

### Viable alternatives
Compare the smallest serious set. Include “do nothing / defer / simpler option” when viable.

Evaluate only relevant dimensions such as research validity, traceability, complexity, reproducibility, operational risk, local resource/cost, reversibility, learning value, and deadline impact. Do not hide a value judgment inside an arbitrary weighted score.

### Recommendation
Choose one **PROPOSED** option and state why under the current constraints.

### Falsifier / validation
Define what experiment or observation would make the recommendation wrong.

### Consequences
State downstream work enabled, debt introduced, migration/rollback concerns, and what is explicitly not decided.

### Acceptance required
Name the exact decision that needs the project owner's approval before dependent implementation.

## Gate behavior

You may build a throwaway spike or benchmark before acceptance if it is bounded and reversible. Label it as evidence, not architecture.

Do not:

- mark D05-D09 ACCEPTED because an agent recommended something;
- create production schema/migration or broad framework scaffolding that implicitly fixes D09;
- freeze thresholds after seeing holdout results;
- expand scope to preserve a preferred technology.

If evidence is insufficient, recommend the next discriminating test instead of manufacturing certainty.
