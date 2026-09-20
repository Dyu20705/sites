# 05 — Research Entry Checklist

**Review target:** `docs/research-entry`, based on `dev` commit `0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`; the research-entry-v1 document set and related baseline edits. Review date: 20 September 2026. Reviewer: Codex, author self-review using `sites-review`; not an independent replay or user validation.

**Current result:** REVIEW PENDING. Gate status applies to this branch's reviewed artifacts, not automatically to remote `master`.

| Criterion | Evidence | Status / finding / remaining work |
| --- | --- | --- |
| D05 and D06 accepted by the owner | [Decision log](../master/07_DECISION_LOG.md) | Recorded; verify consistency across baseline documents |
| P0 and R1–R8 have constructs, evidence, falsifiers and owners | [Research questions](../master/02_RESEARCH_QUESTIONS.md) | Prepared; review coverage |
| Claims stay descriptive and bounded | [M1](../baseline/M1.md), [scope](../master/01_SCOPE_AND_NON_GOALS.md) | Prepared; no provider or metric selected |
| Search, exclusions, counterevidence and stopping rules exist | [Research protocol](00_RESEARCH_PROTOCOL.md) | Prepared; no completed literature review claimed |
| Claim/source capture preserves inspection limits | [Ledger](01_EVIDENCE_LEDGER.md), [prior-art map](../master/03_PRIOR_ART_MAP.md) | Prepared; no new findings or measurements |
| Provider selection has an audit procedure | [Audit plan](02_SOURCE_AUDIT_PLAN.md) | Prepared; all five candidates NOT AUDITED |
| Case/control selection precedes output and holdout tuning | [Case protocol](03_CASE_SELECTION_PROTOCOL.md) | Prepared; no selected or frozen case claimed |
| Signals remain candidates; D07–D09 stay open | [Candidates](04_SIGNAL_CANDIDATES.md), [decision log](../master/07_DECISION_LOG.md) | Prepared; formulas/thresholds/stack not frozen |
| Temporal limitation cannot silently pass M1 | [Evaluation protocol](../master/06_EVALUATION_PROTOCOL.md) | E3 NOT PASSED when availability evidence is missing |
| Two issues form a bounded queue; R5/R8 accounted for | [Backlog](../master/08_MONTH1_BACKLOG.md) | Pending issue publication and readback; WIP at most two |
| Current and historical state are distinct | [Current state](../master/09_CURRENT_STATE.md) | Pending final state refresh |
| Both language sets agree and links resolve | [Documentation policy](../../README.md) | Pending mechanical checks and bilingual review |

## Gate meanings

- **define-ready:** D05/D06 accepted and no unresolved M0/definition BLOCKER or MAJOR in reviewed scope.
- **Research Entry:** define-ready plus an inspectable research protocol, capture/audit/case/signal procedures and operational queue, with no unresolved entry BLOCKER or MAJOR.
- **research-ready:** later literature and sample/temporal evidence, signal comparison, case/control and freeze proposal, followed by explicit D07/D08 acceptance. NOT PASSED by these preparation documents.
- Preimplementation, feature and product gates remain NOT PASSED. E1–E8 are not marked as passing by a documentation review.

## Review record

Pending: account for all changed files, check UTF-8/Markdown/internal links and translation meaning, verify issue bodies, list findings and exact validation results. Provider sampling, full-paper re-review, runtime tests, independent replay and user validation are outside this entry review and remain outstanding.
