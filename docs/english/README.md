# SITES — Scholar Intelligent Trend Evolution System

English · [Tiếng Việt](../vietnamese/README.md)

**SITES** is a research project in scholarly intelligence. It aims to analyze how scientific and technological concepts change over time using evidence that can be inspected.

The long-term vision extends beyond research papers and trend dashboards. Scholarly literature is the starting domain; later work may cover other evidence sources and more advanced analytical or decision-support capabilities.

~~~text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
~~~

## Current focus

The repository is on the **Month-1 path from project definition to one reproducible vertical slice**. The current tree does not contain a product implementation or its executable test suite.

For **Month 1 (17 September–17 October 2026)**, the committed scope is intentionally narrow:

- begin with scholarly evidence;
- focus on detection and descriptive trend intelligence;
- build one small, reproducible end-to-end flow;
- exclude forecasting, recommendation, optimization, autonomous agents, and large-scale infrastructure unless a later decision explicitly accepts them into M1.

D05 evidence/correctness principles and D06's primary user—a researcher surveying a technical topic—were accepted on 20 September 2026. User value remains unvalidated. The data source, corpus, signal definition and implementation technology still require evidence and approval at the relevant decision gates.

## Documentation

Start with the [documentation index](../README.md).

The English M0/M1 documentation set includes:

- [Month-1 definition](baseline/M1.md)
- [Project charter](master/00_PROJECT_CHARTER.md)
- [Scope and non-goals](master/01_SCOPE_AND_NON_GOALS.md)
- [Research questions](master/02_RESEARCH_QUESTIONS.md)
- [Prior-art map](master/03_PRIOR_ART_MAP.md)
- [Conceptual architecture](master/04_SYSTEM_ARCHITECTURE.md)
- [Conceptual data model](master/05_DATA_MODEL.md)
- [Evaluation protocol](master/06_EVALUATION_PROTOCOL.md)
- [Decision log](master/07_DECISION_LOG.md)
- [Month-1 gate plan](master/08_MONTH1_BACKLOG.md)
- [Verified current state](master/09_CURRENT_STATE.md)

Research preparation:

- [Research protocol](research/00_RESEARCH_PROTOCOL.md)
- [Evidence ledger](research/01_EVIDENCE_LEDGER.md)
- [Source audit plan](research/02_SOURCE_AUDIT_PLAN.md)
- [Case selection protocol](research/03_CASE_SELECTION_PROTOCOL.md)
- [Signal candidates](research/04_SIGNAL_CANDIDATES.md)
- [Research Entry checklist](research/05_RESEARCH_ENTRY_CHECKLIST.md)

The English and Vietnamese sets are equivalent in meaning, not sentence-by-sentence wording. Decision IDs, dates, statuses, requirements, and technical meaning must remain consistent across both versions.

## Repository status and history

Historical code, designs, and issues remain in Git history. They can inform current work, but they do not automatically become the current architecture or roadmap.

The new baseline does not assume that an earlier implementation, data source, schema, metric, or technology remains suitable. Any reuse must be evaluated against the current requirements and evidence.

See [PR #62](https://github.com/Dyu20705/sites/pull/62) for the repository reset and M0 documentation review.
