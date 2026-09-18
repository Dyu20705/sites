# SITES — Scholar Intelligent Trend Evolution System

**SITES** is a research-oriented scholarly intelligence project for studying how scientific and technological concepts evolve from evidence.

The long-term vision is broader than scientific papers or trend dashboards. Scholarly literature is the starting domain, while future work may expand to additional evidence sources and higher-level capabilities.

~~~text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
~~~

## Current focus

The repository is currently at **M0 — project definition**. The active tree does not contain a current product implementation or executable test suite.

For **Month 1 (17 Sep–17 Oct 2026)**, the committed direction is deliberately narrower:

- start from scholarly evidence;
- focus on detection and descriptive trend intelligence;
- build one small, reproducible end-to-end slice;
- keep forecasting, recommendation, optimization, autonomous agents, and large-scale infrastructure outside the committed M1 scope unless a later decision explicitly changes that boundary.

Specific choices such as the target user, data provider, corpus, signal definition, storage, framework, dashboard technology, and deployment model remain subject to evidence and decision gates.

## Documentation

The repository documentation separates long-term vision, proposed decisions, accepted decisions, and verified current state so that plans are not mistaken for implemented capabilities.

- **English:** this README is the public project introduction. A full English documentation mirror will live under **docs/english/** as the documentation set stabilizes.
- **Tiếng Việt:** [docs/vietnamese/README.md](docs/vietnamese/README.md) is the Vietnamese translation of this README and links to the current detailed M0/M1 documents.
- **日本語:** a Japanese mirror is planned under **docs/japanese/**; it will be added when an actual reviewed translation exists rather than as empty scaffolding.

Current detailed project-definition documents are available in Vietnamese:

- [Month-1 definition](docs/vietnamese/baseline/M1.md)
- [Project charter](docs/vietnamese/master/00_PROJECT_CHARTER.md)
- [Scope and non-goals](docs/vietnamese/master/01_SCOPE_AND_NON_GOALS.md)
- [Research questions](docs/vietnamese/master/02_RESEARCH_QUESTIONS.md)
- [Prior-art map](docs/vietnamese/master/03_PRIOR_ART_MAP.md)
- [Conceptual architecture](docs/vietnamese/master/04_SYSTEM_ARCHITECTURE.md)
- [Conceptual data model](docs/vietnamese/master/05_DATA_MODEL.md)
- [Evaluation protocol](docs/vietnamese/master/06_EVALUATION_PROTOCOL.md)
- [Decision log](docs/vietnamese/master/07_DECISION_LOG.md)
- [Month-1 backlog](docs/vietnamese/master/08_MONTH1_BACKLOG.md)
- [Verified current state](docs/vietnamese/master/09_CURRENT_STATE.md)

## Repository status and history

Historical code, design documents, and issues remain available through Git history. They are useful evidence and design material, but they are **not automatically the current architecture or roadmap**.

The current baseline intentionally avoids claiming that an old implementation, provider choice, schema, metric, or technology stack is still valid. Reuse is allowed only after it is re-evaluated against the active requirements and evidence.

See [PR #62](https://github.com/Dyu20705/sites/pull/62) for the M0 repository reset and documentation review.
