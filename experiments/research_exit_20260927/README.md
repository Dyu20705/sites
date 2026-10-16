# M1 Frozen Research Evidence

The experiment supports **retrospective descriptive title-lexical prevalence only**, for 598 observed arXiv cs.SE works in January–June 2019 event bins, acquired in October 2026. It is not historical as-of verification or a scientific semantic trend classifier.

## Frozen identities

- [F1 manifest](runs/20261012-research-exit-01/freeze-v1.json) — external SHA-256: `bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`.
- 122 declared research artifacts must match exact hashes; no checkout EOL conversion is allowed for pinned bytes.
- [Accepted research contract](../../docs/english/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md), including explicit negative findings and constraints.
- [Research Exit evaluation](../../docs/english/research/17_RESEARCH_EXIT_20261012.md).
- [Original audit and source evidence](runs/20261010-development-01/replay-1/audit.json).

## Verify locally

Run from repository root:

```sh
python tools/check_repository.py --freeze-only
python experiments/research_exit_20260927/verify_freeze.py --help
python -m unittest discover -s experiments/research_exit_20260927 -p 'test_*.py' -v
```

The helper `--help` command documents verifier arguments; its success is not a complete scientific evaluation. Only call live `acquire.py` as a separately authorized source experiment. Offline replay requires no provider API calls.

## Publication boundary

This curated tree retains the full frozen F1 dependency closure and original hash-bound Vietnamese scope contract as evidence. Non-pinned progress snapshots and duplicate intermediate reports remain accessible on [the Research Exit history](https://github.com/Dyu20705/sites/tree/0673903c7cf8e4c6725af8a13f2ca4e40a1457a9/experiments/research_exit_20260927). Never reinterpret simulated judgments as human labels. Original E3: NOT PASSED; semantic quality: NOT MEASURED.
