# SITES — Agent operating contract

These repository rules apply to all AI and coding assistants. An agent's statement is not verification, scientific acceptance, or authorization to merge.

## Authoritative sources

1. Inspect the actual task issue, the branch SHA, and the relevant current PR diff.
2. Read [English project scope](docs/english/baseline/M1.md), [decision log](docs/english/master/07_DECISION_LOG.md), [evaluation protocol](docs/english/master/06_EVALUATION_PROTOCOL.md), and [current-state snapshot](docs/english/master/09_CURRENT_STATE.md).
3. Follow [repository publication policy](docs/english/governance/REPOSITORY_POLICY.md) and the task-specific skill in `.agents/skills/`.
4. Validate any dated status against GitHub issues and the checked-out commit. A historical document is not the current source of truth.

## Authority and decision gates

Human acceptance is required before modifying research questions, claim boundaries, D05–D09 contracts, corpus selection, metric/thresholds, temporal meaning, security boundaries, major architecture/dependencies, public distribution, or deployment. Do not infer acceptance from a checked box or an AI review.

Permitted without a new decision: bounded, reversible improvements within an accepted task contract, tests, lint fixes, read-only research, draft proposals, and reproducibility improvements that preserve frozen bytes and scientific claims.

Never autonomously merge to `master`, force-push, rewrite shared history, publish releases, deploy, migrate irreversibly, expose secrets, impersonate a human reviewer, or mark a scientific gate passed.

## Execution procedure

- Maintain at most two active execution work items; governance trackers and future epics are not extra implementation lanes.
- State the input contracts, invariants, expected outputs, risks and tests before modifying code.
- Keep research evidence provenance; prohibit leakage from future observations into historical-as-of claims.
- Do not modify or delete hash-pinned evidence without a separately accepted packaging and replay migration.
- Work on a review branch; batch logical changes and publish once rather than repeated push churn.
- Record verified test command, environment, result and remaining gaps; never fabricate CI runs or independent human observations.
- Do not turn a passing unit test into a claim of E3, E7, E8, scientific accuracy, or Product-ready status.
- Keep published English docs concise, factual, discoverable, and free of temporary agent handoffs.

## Skill routing

- `sites-research-evidence`: prior art, method critique and novelty checks.
- `sites-source-audit`: provider/field/corpus/temporal evidence.
- `sites-decision-gate`: impactful choices requiring an owner decision.
- `sites-review`: PR and scientific/engineering evidence review.
- `sites-security-review`: security boundaries and defensive review.
- `sites-implementation-verification`: code, tests, reproducibility and runtime acceptance.
- `sites-publication-review`: code/docs/evidence curation before PR or release.

Review [the skills index](.agents/README.md). Use only the skills necessary for a task.

## Definition of done

Every completed task links to the exact changed files and verification. Separate VERIFIED, ACCEPTED, PROPOSED, UNKNOWN, NOT MEASURED, and NOT PASSED. An unresolved major defect or a missing mandatory gate means BLOCKED, not READY.
