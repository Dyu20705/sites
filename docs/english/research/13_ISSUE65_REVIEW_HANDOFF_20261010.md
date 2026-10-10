# 13 — Issue #65 review response and B → A handoff

**Investigation outcome proposed: INSUFFICIENT EVIDENCE.** The reviewed corpus and historical screen are inspectable; historical population remains unresolved. Closing #65 as an investigation is a separate owner decision from accepting D07 or passing #70. No issue closure or scope change is authorized by this response.

## 01. Findings and disposition

| Finding | Disposition |
| --- | --- |
| P0: historical population cannot be reconstructed | Scientific blocker retained; historical denominator/share stay null; E3 NOT PASSED |
| P1: search log lacks execution metadata | Acknowledged; prospective execution template prepared, not executed |
| P1: A has not acknowledged B handoff | [Handoff sent to #64](https://github.com/Dyu20705/sites/issues/64#issuecomment-6097343828); acknowledgment remains pending |
| P2: preregistration lacks independent timing evidence | Limitation retained; future confirmatory plans require a pre-execution commit or timestamped immutable record |

The review found no new serious code defect. No parser change, acquisition, abstract-page retry, signal computation or holdout inspection follows. The [review-response record](../../../experiments/research_exit_20260927/runs/20261010-review-response-01/review-response.json) records unresolved items explicitly.

## 02. Search and preregistration provenance

The original [search log](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-results.json) retains four queries and their exploratory/preregistered distinction. It lacks a complete committed record of service, exact execution timestamps, filters, screened result counts and each result URL. These omissions limit independent reconstruction of the search; they do not demonstrate that a historical archive is absent. Missing metadata is not invented or backdated.

The historical plan's local timestamp and agent-recorded execution order do not independently prove pre-exposure existence. Plan and results were pushed together after execution. This is a provenance limitation, not evidence of a protocol violation or confirmatory acceptance.

The [future search execution template](../../../experiments/research_exit_20260927/runs/20261010-review-response-01/future-search-execution-template.json) is **TEMPLATE_NOT_EXECUTED**. At the next actual screen, record service/tool, start/end UTC timestamps, exact query, all filters, returned/screened/opened counts and per-result URLs/dispositions/access depth/source locations. Distinguish unavailable counts from zero and unknown filters from no filter. Preserve permissible response/capture references and their checksums when captured. Search rankings may still change; complete metadata improves auditability without guaranteeing identical future results.

Before confirmatory exposure, commit the complete plan before execution or use a timestamped immutable record; record the freeze reference and its timing evidence. Prefer an independent time anchor. An after-execution push cannot establish this timing retroactively. Required owner-approved D07/D08 and experiment freeze still precede holdout.

## 03. Handoff delivered, acknowledgment pending

The #64 comment links fixed-commit corpus audit, normalized records, missingness/revisions, raw anomaly references, temporal limitations and replay verification. A can inspect 598 distinct works with exact v1 versions and monthly retrospective denominators 91/79/97/103/122/106. Seven core fields have zero missing/invalid values under the declared syntactic checks; 161 current versions are v2+, 55 titles differ and four category sets differ.

For D08 as-of, `published_at`/`updated_at` are submission times, not verified first-public times. `available_at` is null for 598/598; historical membership and denominator are unresolved. Versioned titles/categories retrieved in 2026 do not establish knowability at T. The nine July/August ID anomalies and development-query exposure must be reconciled before any holdout freeze. Vocabulary, reference rubric, support/quality threshold and signal are not accepted or measured by this handoff.

A was asked to acknowledge receipt and identify fields/denominators unfit for D08 as-of, missing requirements, or conditions for a retrospective-only proposal. Sending B's comment is not A acknowledgment; no acknowledgment is fabricated here.

## 04. Concrete owner review packet

The [corpus audit](11_REAL_CORPUS_AUDIT_20261010.md) and [historical screen](12_HISTORICAL_AVAILABILITY_SCREEN_20261010.md) support two distinct decisions:

1. **Investigation disposition:** accept #65's insufficient-evidence report for investigation completion after A acknowledgment, or require an additional bounded historical-capture test. #65 remains OPEN until the conditions and explicit owner instruction to close it are present.
2. **Research scope at #70:** continue historical as-of reconstruction, or request a controlled retrospective-only scope proposal. Choosing to prepare a proposal does not accept its corpus/protocol, make E3 pass or authorize dependent implementation.

If continuing historical reconstruction, the next test is source-specific: first identify a concrete dated category/announcement capture with provenance and coverage, then preregister its request/byte bounds and reconcile both known anomalies and membership independently of current positives. No qualifying capture was identified in the prior screen, so exact acquisition parameters remain unselected. Additional abstract pages alone do not answer population completeness.

D07/D08/D09 remain PROPOSED; #70 remains NOT PASSED. Owner review and A acknowledgment remain pending. Validation of this response covers documentation links, JSON parsing and unchanged gate statuses; prior 17-test/replay results are existing evidence, not newly executed checks.
