---
name: sites-review
description: Evidence-first reviewer for SITES pull requests, diffs, research documents, experiment artifacts, datasets, and gate readiness. Use for review/QA, merge-readiness checks, research critique, implementation verification, or when deciding whether define-ready, research-ready, preimplementation-ready, feature-ready, or product-ready evidence is sufficient.
---

# SITES Review

Review for correctness and decision integrity, not for volume of comments. A confident false positive is worse than a clearly bounded concern.

## Establish the review target

Record:

- exact branch/commit/PR or document version;
- claimed purpose and acceptance criteria;
- files/artifacts in scope;
- relevant accepted decisions and gate.

Account for every changed/reviewable file or explicitly state what was skipped and why.

## Evidence hierarchy

Verify claims against current source and executable evidence. Do not treat:

- old Git history as current implementation;
- a design document as proof that code exists;
- a passing unrelated test as proof of a changed contract;
- an agent-generated citation as valid without checking the source;
- an accepted decision as evidence that implementation is correct.

When a concern depends on an unverified runtime/provider fact, label it **needs validation** instead of asserting a defect.

## Review dimensions

### Scope and decision integrity

Check for hidden M1 scope expansion, silently accepted D05-D09 choices, new dependencies/architecture/schema without a decision record, and stale or contradictory status claims.

### Research and data validity

Check for unsupported novelty or causal claims, missing counterevidence, temporal leakage, provider/query/sampling bias, denominator/corpus-growth confounding, post-hoc threshold tuning, and missing provenance/snapshot/units/limitations.

### Implementation

Check invariants, boundary/error cases, idempotency/replay, deterministic expected values for core metrics, data lineage/evidence bundles, tests that fail for the intended reason, bounded resource behavior, and relevant secret/security handling.

Do not demand distributed systems, abstractions, or production infrastructure that M1 does not require.

### Documentation

Check that FACT / HYPOTHESIS / PROPOSED / ACCEPTED / VERIFIED language matches evidence. Verify internal links and user-visible commands where feasible.

## Severity

- **BLOCKER**: invalidates the research result, risks data/security integrity, violates an accepted hard boundary, or makes the claimed gate impossible.
- **MAJOR**: material correctness/reproducibility/traceability issue that should be fixed before the claimed milestone/merge.
- **MINOR**: useful improvement that does not invalidate the current claim.

Do not inflate style preferences into MAJOR issues.

## Gate checks

When a task claims M1 implementation/evaluation readiness, map evidence to E1-E8 from `docs/vietnamese/master/06_EVALUATION_PROTOCOL.md`:

- E1 deterministic correctness
- E2 historical/control case + explainability
- E3 temporal isolation
- E4 reproducibility
- E5 traceability
- E6 idempotency
- E7 usability
- E8 bounded operation

A missing applicable criterion is a gap, not automatically proof of failure. State exactly what evidence is absent.

## Output

Lead with findings, ordered BLOCKER -> MAJOR -> MINOR. For each finding include location/artifact, observed evidence, why it matters, and the smallest effective correction or validation.

Then give reviewed/skipped scope, validation actually run, unresolved needs-validation items, and gate status supported by the evidence.

Do not auto-merge or auto-release after review.
