# Verified Current State

**Snapshot: 16 October 2026.** This page is a dated status record; check exact GitHub branch/issue/CI state before claiming a newer release or gate result.

## Accepted scientific scope

- D05/D06 and bounded retrospective D07/D08/F1 have owner acceptance; D09 minimal offline evidence-slice contract was accepted in [#71](https://github.com/Dyu20705/sites/issues/71).
- The frozen arXiv cs.SE observation contains 598 distinct works from a current 2026 query, classified into January–June 2019 UTC submission months.
- Title-only lexical matches by month: n = 0, 1, 2, 1, 4, 1 and denominator N = 91, 79, 97, 103, 122, 106; pooled n/N = 9/598.
- [Research Exit #70](https://github.com/Dyu20705/sites/issues/70) passed **only for descriptive retrospective claims**. Original historical-as-of E3 is NOT PASSED; scientific semantic accuracy is NOT MEASURED.
- F1 `F1-M1-R-20261012-v1` SHA-256: `bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`. All 122 pinned artifact references, including the original English and Vietnamese scope contracts, must remain exact.

## Engineering integration boundary

The curated reference implementation derives from `codex/m1-offline-code@0d3e5ab` (product source originally `6c08a956`), rather than combining that codebase with the separate PR #76 implementation. This is an engineering baseline selection; it does **not** rewrite product/reviewer evaluations or claim equivalence between divergent codebases. The machine-specific `runs.ps1` and unverified reviewer ZIP were not included in the public curated tree; portable replay instructions remain under `evaluation/REPLAY.md`.

CI and repository-policy verification on the exact integration SHA are required before claiming merge readiness. The intended historical demonstration deadline of 15 October 2026 elapsed without independent product-ready approval. Independent reviewer E7/E8 and interpretation tasks remain under [#73](https://github.com/Dyu20705/sites/issues/73).

## Post-M1 direction

See [master roadmap #78](https://github.com/Dyu20705/sites/issues/78). Forecasting, decision optimization, multi-source orchestration and distributed infrastructure are not part of accepted M1 functionality.
