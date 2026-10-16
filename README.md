# SITES — Scholarly Intelligence for Technology Evolution

SITES is an evidence-first research system for inspecting concept prevalence in scholarly literature. It provides an offline, reproducible **retrospective lexical** case study, not a validated emerging-technology detector or forecast.

The M1 reference slice analyzes **598 frozen arXiv works** (cs.SE, January–June 2019 event bins, data observed in October 2026). The documented title rule has nine matches; results provide exact n/N counts, source-lineage evidence and explicit limitations.

## Navigate

- [Documentation](docs/english/README.md) — scope, research decisions, architecture and evaluation.
- [Offline replay guide](evaluation/REPLAY.md) — Windows reference environment, frozen input and CLI.
- [Research evidence](experiments/research_exit_20260927/README.md) — manifest, source snapshots, verifier and negative findings.
- [Repository policy](docs/english/governance/REPOSITORY_POLICY.md) — publication, provenance, immutable evidence.
- [Agent contract](AGENTS.md) — owner decision gates, reproducibility and code review.
- [Five-year roadmap](https://github.com/Dyu20705/sites/issues/78) — proposals, not implemented functionality.

## Run and verify

Uses CPython standard library only. A formal replay needs a **prospectively anchored evaluation manifest** matching the accepted F1/D09 and runtime; it is not generated or silently approved by this repository. See the [replay protocol](evaluation/REPLAY.md) and [implementation notes](evaluation/AS_BUILT.md). For development regression tests:

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest discover -s experiments/research_exit_20260927 -p 'test_*.py' -v
python tools/check_repository.py
```

## Claims and status

**Research-ready:** accepted only for this bounded retrospective descriptive claim. Original historical-as-of E3: **NOT PASSED**. Scientific semantic accuracy: **NOT MEASURED**. Independent final reviewer interpretation, browser E7 and full E8 are tracked under [#73](https://github.com/Dyu20705/sites/issues/73); source/tests alone do not establish Product-ready or Production-ready status.

Development and scientific evidence are distinct from a release decision. Follow the [PR template](.github/pull_request_template.md); do not merge, change frozen data, or deploy without explicit owner approval.
