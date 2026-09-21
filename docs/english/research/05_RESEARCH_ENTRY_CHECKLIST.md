# 05 — Research Entry Checklist

**Review target:** `docs/research-entry`, based on `dev` commit `0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`; preparation commit `fc0dba983458dbef7523227451e368cfd5bcef17` plus this closeout's issue links and review records. Review completed: 21 September 2026. Reviewer: Codex, author self-review using `sites-review`; not an independent replay or user validation.

**Current result:** define-ready PASSED; Research Entry PASSED. No unresolved BLOCKER or MAJOR found in the reviewed scope. Gate status applies to this branch's reviewed artifacts, not automatically to remote `master`. Research-ready remains NOT PASSED.

| Criterion | Evidence | Status / finding / remaining work |
| --- | --- | --- |
| D05 and D06 accepted by the owner | [Decision log](../master/07_DECISION_LOG.md) | PASS — acceptance and remaining decisions consistent across baseline documents |
| P0 and R1–R8 have constructs, evidence, falsifiers and owners | [Research questions](../master/02_RESEARCH_QUESTIONS.md) | PASS — P0 unchanged; all eight RQs covered |
| Claims stay descriptive and bounded | [M1](../baseline/M1.md), [scope](../master/01_SCOPE_AND_NON_GOALS.md) | PASS — no provider or metric selected |
| Search, exclusions, counterevidence and stopping rules exist | [Research protocol](00_RESEARCH_PROTOCOL.md) | PASS — no completed literature review claimed |
| Claim/source capture preserves inspection limits | [Ledger](01_EVIDENCE_LEDGER.md), [prior-art map](../master/03_PRIOR_ART_MAP.md) | PASS — no new findings or measurements |
| Provider selection has an audit procedure | [Audit plan](02_SOURCE_AUDIT_PLAN.md) | PASS — procedure only; all five candidates NOT AUDITED |
| Case/control selection precedes output and holdout tuning | [Case protocol](03_CASE_SELECTION_PROTOCOL.md) | PASS — rules exist; no selected or frozen case claimed |
| Signals remain candidates; D07–D09 stay open | [Candidates](04_SIGNAL_CANDIDATES.md), [decision log](../master/07_DECISION_LOG.md) | PASS — formulas/thresholds/stack not frozen |
| Temporal limitation cannot silently pass M1 | [Evaluation protocol](../master/06_EVALUATION_PROTOCOL.md) | PASS — E3 criterion unchanged; E3 NOT PASSED when availability evidence is missing |
| Two issues form a bounded queue; R5/R8 accounted for | [Backlog](../master/08_MONTH1_BACKLOG.md) | PASS — #64/#65 OPEN and read back; queued, not executing; WIP at most two |
| Current and historical state are distinct | [Current state](../master/09_CURRENT_STATE.md) | PASS — 21 September snapshot; 18 September history retained separately |
| Both language sets agree and links resolve | [Documentation policy](../../README.md) | PASS — structural checks and bilingual meaning review completed |

## Gate meanings

- **define-ready:** D05/D06 accepted and no unresolved M0/definition BLOCKER or MAJOR in reviewed scope.
- **Research Entry:** define-ready plus an inspectable research protocol, capture/audit/case/signal procedures and operational queue, with no unresolved entry BLOCKER or MAJOR.
- **research-ready:** later literature and sample/temporal evidence, signal comparison, case/control and freeze proposal, followed by explicit D07/D08 acceptance. NOT PASSED by these preparation documents.
- Preimplementation, feature and product gates remain NOT PASSED. E1–E8 are not marked as passing by a documentation review.

## Review record

Reviewed all 36 changed files against the `dev` baseline: two repository/documentation indexes, two language READMEs, two M1 definitions, 18 master documents and 12 research documents. No changed file was excluded. Bilingual review compared decision status, scope, dates, RQ ownership, evidence boundaries, stop conditions and temporal/case rules. The two unchanged conceptual-architecture documents were not re-reviewed as new designs; D09 remains open.

Validation results:

- Strict UTF-8 decoding, local file-link targets, balanced code fences and table column counts: 38 Markdown files, 18 language pairs, 169 local links and 51 tables; zero reported problems. These are targeted structural checks, not a full Markdown renderer or external-source audit.
- Decision-state checks: D05/D06 ACCEPTED, D07–D09 PROPOSED, D10 DEFERRED in both languages. P0 and the E3 acceptance row match the original baseline. All R1–R8 have evidence/decision and construct/falsifier/owner rows.
- `git diff --check` against the baseline: passed. No product tests were run because this changeset contains documentation only.
- GitHub readback at 07:57 +07:00 on 21 September: #64 and #65 OPEN, bodies match the prepared drafts; all seven distinct linked document paths exist in published preparation commit `fc0dba9`.

Resolved during preparation: stale D05/D06 proposal references, missing RQ ownership/falsifiers, absent research procedures, stale current state and missing operational issues. No unresolved entry BLOCKER/MAJOR remains. Provider sampling, full-paper re-review, runtime tests, independent replay and user validation are outside this entry review and remain outstanding. They must not be inferred from an entry PASS.
