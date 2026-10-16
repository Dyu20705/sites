# Repository Publication and Evidence Policy

Status: **Owner-accepted repository publication policy — 16 October 2026**. This policy governs the curated public tree; it does not retroactively change accepted scientific contracts, research gate outcomes, or frozen evidence.

## Purpose

The default branch should contain maintainable software, validated tests, authoritative English documentation and reproducible scientific artifacts. It is not a storage area for agent transcripts, scratchpad notes, duplicate run outputs or daily coordination reports.

## Publication classes

| Class | Default-branch treatment |
| --- | --- |
| Project definition, architecture, data model, accepted decisions, research protocol, results and limitations | Publish in English, with durable links and dated evidence |
| Source code, minimal fixtures, regression/integration tests and project-local skills | Publish when purposeful, tested and reviewed |
| Frozen raw/derived research artifacts and scripts needed for independent replay | Preserve exact bytes or use an approved separately verified immutable evidence package |
| Experimental execution logs, scratch reports, agent handoffs, intermediate review packets and repeated outputs | Keep in Git history or an evidence archive; publish only when essential to a scientific audit |
| Machine-specific reviewer profiles, reviewer identities, internal paths and local output directories | Do not publish by default; redact or parameterize before any public inclusion |
| Vietnamese translations | Do not add as new canonical documentation; pinned original evidence is an exception until packaging migration passes |

## Immutable research boundary

Research Exit F1 (`F1-M1-R-20261012-v1`, SHA-256 `bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`) pins 122 artifacts, including `docs/english/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md` **and** its Vietnamese counterpart. Removing, rewriting, renaming or line-ending-normalizing a pinned file can invalidate replay. A clean English default branch does not justify silently destroying that evidence.

Before externalizing a frozen evidence package, require: (1) an owner-approved storage/licensing decision; (2) a self-contained immutable package/manifest with published digest and retrieval instructions; (3) full artifact and raw-lineage verification; (4) two independent clean-directory offline replays with semantic equality; (5) updated test/CLI references; and (6) a documented rollback. Until these pass, preserve original bytes and report the language exception rather than claiming English-only success.

No Git history rewrite, force-push or unapproved data deletion is permitted. Reusable research source and the irreducible evidence required for a published result take precedence over superficial directory tidiness.

## Code and documentation quality

- English README is a short project overview with links, not a chronological narrative.
- Explain observed capability separately from proposed roadmap. Never describe unmerged draft code as functionality in `master`.
- State scope, data provenance, temporal limits, actual evaluation outcome and known negative findings. Do not claim historical availability, semantic effectiveness or scientific trend detection from lexical counts alone.
- Tests should check invariants, negative/failure paths and exact evidence identity. CI is a regression tool, not a substitute for an independent research reviewer.
- Project-local skills must define triggers, limits and verifiable outputs. Prompts do not themselves confer authorization.
- Reject unresolved security, evidence-integrity or correctness blockers before integration; avoid gratuitous architecture changes and dependency growth.

## Integration protocol

1. Inspect `master`, PR #75, PR #76, and separately divergent `codex/m1-offline-code` SHAs before selecting a product baseline.
2. Review and preserve the verified F1 contract and its original artifact bytes.
3. Consolidate a candidate code path only after comparing the alternative implementations and their tests; do not discard a code branch by silently copying modules.
4. Run CI against the *final* candidate SHA; replay on the required target independently where the contract requires it.
5. Make human acceptance explicit for evidence migration, conflicting implementations, ruleset policy and final merge.
6. Close historical issues only with disposition, retained limitations and successor references.

## Branch gate limitation

A GitHub PR template and workflow alone do not enforce approval. Required status checks, review conditions and bypass policy must be configured in repository rulesets and independently checked. CODEOWNERS must name a real eligible reviewer; assigning only the PR author can deadlock approvals. No fabricated reviewer identity or approval is acceptable.
