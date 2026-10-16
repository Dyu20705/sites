# 12 — Issue #65 reviewer replay and historical source screen

**VERIFIED:** the requested local replay and direct XML cross-check pass at baseline `670bcee8bc0f5a8883ff56979666fb614a1b5d44`. **INSUFFICIENT EVIDENCE:** the bounded historical source screen does not establish first-public timestamps or the complete historical cs.SE population. E3 and Research Exit #70 remain NOT PASSED; D07–D09 remain PROPOSED.

## 01. Review response and local validation

This responds to the [independent review checkpoint](https://github.com/Dyu20705/sites/issues/65#issuecomment-6097198637). The working tree was clean before fetch; the correct branch matched origin, and `pull --ff-only` was already up to date. All 17 tool unit tests passed in 0.281 seconds. No parser defect was demonstrated and no acquisition/audit code was changed.

The fresh [reviewer replay](../../../experiments/research_exit_20260927/runs/20261010-development-01/reviewer-replay-20261010-115331/verification.json) verifies 14 frozen manifest/config/code/raw inputs and reproduces the original bytes:

| Artifact | SHA-256 |
| --- | --- |
| audit.json | `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8` |
| normalized-records.json | `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1` |
| crosscheck.json | `0664d7dcd1ad3d1fd570696b47b254ce54329ffcc56c9b6416482830379c6591` |

The separate direct-XML parser again checks all 598 records and nine raw-file hashes. Its output also matches the original bytes. This is a fresh agent-driven execution on the producer host, not an independent human or second-machine replay. Original runs and frozen inputs are preserved. The existing [corpus audit](11_REAL_CORPUS_AUDIT_20261010.md) remains the measured acquisition report.

## 02. Bounded historical screen

[HA-20261010-01 plan](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-plan.json) was written before opening the nine record pages. Earlier exploratory help-document searches are explicitly separated in the [results/search log](../../../experiments/research_exit_20260927/runs/20261010-historical-screen-01/source-screen-results.json). The screen attempted each official abstract page once, inspected seven official help pages and used four targeted search queries in total. No API/OAI harvest, corpus reacquisition, PDF transfer or holdout query was performed.

| Official record page | Frozen v1 submission (UTC) | ID month | Page observation |
| --- | --- | --- | --- |
| [1907.00143](https://arxiv.org/abs/1907.00143) | 2019-06-29 04:32:14 | July | v1 submission matches |
| [1907.00172](https://arxiv.org/abs/1907.00172) | 2019-06-29 09:37:34 | July | v1 submission matches |
| [1907.00282](https://arxiv.org/abs/1907.00282) | 2019-06-29 21:39:03 | July | v1 submission matches |
| [1907.00298](https://arxiv.org/abs/1907.00298) | 2019-06-29 23:53:22 | July | v1 submission matches |
| [1907.00376](https://arxiv.org/abs/1907.00376) | 2019-06-30 13:04:27 | July | v1 submission matches |
| [1907.00468](https://arxiv.org/abs/1907.00468) | 2019-06-30 21:29:48 | July | v1 submission matches |
| [1907.00677](https://arxiv.org/abs/1907.00677) | 2019-06-28 07:21:51 | July | v1 submission matches |
| [1907.03773](https://arxiv.org/abs/1907.03773) | 2019-06-27 18:44:14 | July | v1 submission matches |
| [1908.04451](https://arxiv.org/abs/1908.04451) | 2019-03-07 08:37:23 | August | Web reader cache miss; page unverified |

Eight readable pages corroborate submission timestamps and display current Subjects. They do not supply a verified exact first-announcement timestamp or category-membership timeline. The ninth failure is a tool access observation, not proof the work is absent. Web-reader representations can be cached; no raw HTML capture/checksum or fresh-provider response claim is made. All nine exact announcement timestamps and cutoff memberships remain null.

## 03. Source fitness for the whole population

| Source | Inspected semantics | Historical fitness |
| --- | --- | --- |
| [Availability policy](https://info.arxiv.org/help/availability.html) | ID month follows first announcement, which may differ from submission | INFERENCE: July/August IDs challenge submission-based eligibility at June cutoff; no exact 2019 event time inferred |
| [Identifier policy](https://info.arxiv.org/help/arxiv_identifier.html), [cross-list policy](https://info.arxiv.org/help/cross.html) | ID carries no classification; membership can change | ID enumeration alone cannot recover historical cs.SE membership |
| [OAI documentation](https://info.arxiv.org/help/oa/index.html) | Latest item metadata; version history in arXivRaw; datestamp is last metadata modification | `until=2019-06-30` on a live harvest is not a snapshot of the state then |
| [API manual](https://info.arxiv.org/help/api/user-manual.html) | Published/updated describe version submission dates | Exact v1 retrieval does not prove historical public availability |
| [RSS](https://info.arxiv.org/help/rss.html), [bulk access](https://info.arxiv.org/help/bulk_data.html) | Daily feeds and live metadata/full-text routes | No qualifying dated 2019 capture with membership coverage/checksums verified in this screen |

These are current documents, not a frozen 2019 policy or event ledger. The search did not verify a compatible historical snapshot; this does not prove none exists. Third-party archive inventories, provider-held logs and historical email collections were not audited.

The 598 denominator is complete for the 2026 query. It cannot identify works removed from cs.SE before that query, or when current cross-lists were added. Resolving nine positive cases, subtracting nine, or comparing current/v1 categories does not reveal those missing members. Their count is **unknown**, not zero. Historical denominator/share and vocabulary validity remain unresolved.

## 04. PROPOSED owner decision and next acceptance check

**Recommendation:** preserve the frozen corpus as retrospective evidence and keep the as-of claim blocked. Two alternatives remain for explicit owner review:

1. Continue historical evidence research. Before another corpus transfer, identify one dated announcement/category capture with timestamp semantics, capture provenance, license/access constraints, coverage and immutable checksum. The next bounded check should validate the nine known anomalies **and** enumerate membership independently of the 2026 cs.SE positives, including removals/additions. A snapshot at cutoff alone also needs sufficient history for any claimed earlier monthly as-of state. Preregister request/byte budget and reconciliation checks once a concrete source is found. Stop if the source cannot support population coverage.
2. Propose a retrospective-only research target with the owner. This changes the estimand and claims, requires explicit scope/corpus/protocol acceptance, and does not turn the existing E3 historical test into a pass.

Neither alternative is accepted here. No real signal, reference labels, threshold, freeze, provider switch, D09 implementation or gate closure follows from this screen. The [latest #70 control checkpoint](https://github.com/Dyu20705/sites/issues/70#issuecomment-6096887546) sets demo-ready to 15 October 2026 (before 16 October), superseding the older 17 October execution milestone. Deadline pressure does not resolve the evidence gap.

## 05. Validation scope

Automated evidence covers the 17 unit tests, fresh replay, input hashes and direct raw-XML cross-check. The package report checks relative links, JSON/Python parsing and existing gate statuses; it does not validate external links, cached-page freshness or historical completeness. The paired reports were self-reviewed for matching counts, dates, null fields and proposal status. No independent human replay or historical ground truth is claimed.

## 06. Subsequent review: provenance limitations

The search record lacks complete service/timestamp/filter/result-count/URL execution metadata. The plan and results were pushed together after execution; the local plan timestamp is not independent evidence of pre-exposure existence. These limitations are acknowledged without reconstructing missing historical metadata. See the [review response and pending handoff/owner decisions](https://github.com/Dyu20705/sites/blob/0673903c7cf8e4c6725af8a13f2ca4e40a1457a9/docs/english/research/13_ISSUE65_REVIEW_HANDOFF_20261010.md).
