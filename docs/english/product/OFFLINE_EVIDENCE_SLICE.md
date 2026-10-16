# Offline Evidence Slice

The reference implementation in `sites_demo/` computes a bounded, frozen title-frequency signal from the accepted 598-work corpus. It renders a local evidence explorer with 21 contiguous time windows and 598 record-level evidence pages, plus provenance, sensitivities and explicit limitations.

Use [the as-built architecture](../../../evaluation/AS_BUILT.md), [portable CLI replay protocol](../../../evaluation/REPLAY.md), and [original immutable F1 inputs](../../../experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json). This implementation uses only the Python standard library, not a web backend, database, LLM, or cloud service.

A clean checkout has **no automatically accepted formal reviewer evaluation profile**. Automated development tests and GitHub-hosted CI do not substitute for an identified independent human reviewer, a prospectively anchored machine profile or independent E7/E8 evidence.

Outputs describe observed retrospective *lexical* prevalence. They do not establish a concept's emergence, scientific importance, true semantic membership or public visibility in 2019.
