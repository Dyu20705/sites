# SITES — Scholar Intelligent Trend Evolution System

[Tiếng Việt](docs/vietnamese/README.md)

**SITES** is a research project that studies how scientific and technological concepts change over time using evidence that can be inspected and reproduced.

The project begins with scholarly literature. Its longer-term direction may extend to other evidence sources and more advanced analytical or decision-support capabilities, but those capabilities are not part of the current implementation commitment.

~~~text
evidence acquisition → monitoring → mining → trend detection
→ forecasting → recommendation / decision support → automation / optimization
~~~

## Current focus

SITES is currently on the **Month-1 path from project definition to one reproducible vertical slice**. The active repository does not yet contain a current product implementation or executable product test suite.

For **Month 1 (17 September–17 October 2026)**, the accepted direction is deliberately narrow:

- begin with scholarly evidence;
- focus on detection and descriptive trend intelligence;
- build one small, reproducible end-to-end slice;
- keep forecasting, recommendation, optimization, autonomous agents, and large-scale infrastructure outside the committed M1 scope unless a later accepted decision changes that boundary.

D05 evidence/correctness principles and D06's primary user—a researcher surveying a technical topic—were accepted on 20 September 2026. User value remains unvalidated. The data provider, corpus, signal definition and implementation technology remain subject to evidence and explicit decision gates.

## Documentation

The complete English documentation starts at [docs/english/README.md](docs/english/README.md). It includes the Month-1 definition, project charter, research questions, conceptual design, evaluation protocol, decision log, backlog, and verified current state.

The [Research Entry checklist](docs/english/research/05_RESEARCH_ENTRY_CHECKLIST.md) links the research protocol, evidence ledger, source audit plan, case selection rules and signal candidates. Research Entry is preparation for investigation; it is distinct from the later research-ready gate.

For the Vietnamese introduction and documentation, see [docs/vietnamese/README.md](docs/vietnamese/README.md). Translation rules and document-set status are recorded in the [documentation index](docs/README.md).

## Repository status and history

Historical code, design documents, and issues remain available through Git history. They are useful evidence and design material, but they do not define the current architecture or roadmap.

An earlier implementation, provider choice, schema, metric, or technology stack may be reused only after it has been evaluated against the current requirements and evidence.

See [PR #62](https://github.com/Dyu20705/sites/pull/62) for the M0 repository reset and documentation review.
