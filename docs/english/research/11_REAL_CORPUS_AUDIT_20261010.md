# 11 — Issue #65 real-corpus audit, 10 October 2026

**VERIFIED:** AM-02 succeeded; 598 distinct current-query works and exactly 598 v1 records were acquired. Field, identity, completeness and same-host replay evidence is available. **INSUFFICIENT EVIDENCE for historical/as-of D07; E3 and Research Exit #70 remain NOT PASSED.** D07/D08/D09 remain PROPOSED. This is a local B → A handoff, not issue closure or owner acceptance.

## 01. Experiment identity and preregistration

[RE-20260927-01](../../../experiments/research_exit_20260927/preregistration.json), [20261010-development-01](../../../experiments/research_exit_20260927/runs/20261010-development-01/acquisition.json). Query: `cat:cs.SE AND submittedDate:[201901010000 TO 201906302359]`; ascending submission date; page size 500; 2,000-work bound; cutoff `2019-06-30T23:59:59Z`. January–June development only. Query, concept, cutoff and original contract bytes were preserved. No July–December holdout query or evaluation was run. Later ID months returned by this submission-date query are development-query exposure; any overlap must be reconciled before a future holdout freeze.

Session baseline: `3c23a44ce0f11e243b0e0ecafef2faa93866d123`, correct branch, initially clean tree; fetch verified 0 ahead/behind. Python 3.14.7, standard library only. [Preflight](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/preflight.json), [run declaration](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/development-plan.json), [offline acceptance contract](../../../experiments/research_exit_20260927/runs/20261010-preflight-01/offline-audit-contract.json). Config SHA-256: `f4ed7d7bca9c9665a9cb03437c79306f282e15ebb5ad9520bf6126deff61f1f7`.

## 02. Source access / AM-02

Host DNS and TCP 80/443 succeeded. Sandbox TCP EACCES was an environment restriction, not provider evidence. One logical [AM-02 count request](../../../experiments/research_exit_20260927/http-endpoint-diagnostic/acquisition.json) observed HTTP 301 from HTTP to HTTPS, then HTTP 200 `application/atom+xml; charset=utf-8`. Two HTTP exchanges occurred through the redirect, with a 3.1-second delay. Atom, one entry and totalResults=598 were verified. [Raw response](../../../experiments/research_exit_20260927/http-endpoint-diagnostic/raw/count.xml): 2,910 bytes, SHA-256 `5bbdec306856327b4bd5ae2892c9b08c4fefa6dedd1185f43975278863cdc80f`. AM-02 script hash: `331e07aeff70096fea36c877a8e226e2434431514fe4f910ac93a2316855c9bc`, local commit `d8e330b`.

Old HTTPS 406 manifests were preserved. Today's success does not identify their historical cause; HTTPS is today's successful final path. Instrumentation retains redirects, final URL and a hashed error excerpt bounded to 2,048 bytes. [Manual](https://info.arxiv.org/help/api/user-manual.html) and [terms](https://info.arxiv.org/help/api/tou.html) were checked on 10 October: descriptive metadata is CC0; requests remain serial and at least three seconds apart. No PDFs were fetched.

## 03. Bounded corpus acquisition

[Acquisition](../../../experiments/research_exit_20260927/runs/20261010-development-01/acquisition.json): 11:27:47–11:28:24 UTC, 18:27:47–18:28:24 Asia/Bangkok. Nine serial HTTPS responses: one count, two current pages (500/98), six v1 batches (100/100/100/100/100/98). Current-query total stayed 598. All raw checksums and byte counts verified. Script hash: `cf46527ec6b034afad7d531cb50ffc799ca5accc6ef959694a90fc16e0d4d5e9`; exact code/config/AM-02 bytes are frozen under [inputs](../../../experiments/research_exit_20260927/runs/20261010-development-01/inputs/acquire.py). Runs must use new directories; raw files cannot be overwritten.

## 04. Field mapping and fitness

[Normalized records](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/normalized-records.json) retain work_id, explicit version_id, v1/current titles and categories, published/updated dates, request acquisition timestamps, raw file/entry-index/entry-ID/checksum and validation statuses. `available_at=null`; availability remains unresolved. The [manual](https://info.arxiv.org/help/api/user-manual.html) defines published as v1 submission and updated as submission of the retrieved version. Neither is automatically public availability.

Checked fields: work_id, version_id, title_v1, published_at, updated_at, categories_v1, categories_current. Dates must parse with timezone; update cannot precede publication. Category validation means nonempty terms, not independent taxonomy correctness. Identity/v1/completeness fail closed before normalization. Provenance is retained for every record. Schema presence does not establish semantic accuracy or representativeness.

## 05. Missingness / invalidity by UTC month

| Month | Inspected / distinct | Missing title | Missing dates | Invalid dates | Missing categories | Unresolved v1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2019-01 | 91 / 91 | 0 | 0 | 0 | 0 | 0 |
| 2019-02 | 79 / 79 | 0 | 0 | 0 | 0 | 0 |
| 2019-03 | 97 / 97 | 0 | 0 | 0 | 0 | 0 |
| 2019-04 | 103 / 103 | 0 | 0 | 0 | 0 | 0 |
| 2019-05 | 122 / 122 | 0 | 0 | 0 | 0 | 0 |
| 2019-06 | 106 / 106 | 0 | 0 | 0 | 0 | 0 |

[Audit JSON](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-1/audit.json) separates missing/invalid counts, inspected denominators and rates for every field/bin. Seven fields have 0 missing and 0 invalid in all six bins: measured 0%, not unmeasured. Missing titles never become nonmatches. Historical availability is unresolved for 598/598 separately from metadata missingness.

## 06. Work identity and revisions

Zero duplicate current work IDs; exactly requested v1 IDs returned. 161 current IDs are v2 or later; 55 title differences, four category-set differences, zero published-date conflicts. Only current/v1 were observed, not intermediate history. Example: 1901.02633 title differs between v1/current v2. Category changes: 1901.07910, 1902.10056, 1903.07712, 1904.08337. Each difference is traceable through source_ref. Each work contributes once. 112 current update timestamps exceed cutoff; current metadata cannot silently replace cutoff metadata.

## 07. Denominator completeness

Current-query completeness verified against query/sort settings, startIndex/itemsPerPage, contiguous offsets, exact counts, distinct IDs, matching current/v1 populations and hashes. Retrospective denominators: 91/79/97/103/122/106. All 598 works are eligible in the declared current-category retrospective corpus; no exclusions were needed. No concept filter was used; nonmatches remain in the population. This cannot enumerate works removed from today's cs.SE category. As-of denominators and shares remain null; no real signal or trend labels were calculated.

## 08. Historical cutoff / availability matrix

| Component at T | Evidence | Conclusion |
| --- | --- | --- |
| Public availability | Submission before T; nine IDs have July/August ID month | Unresolved / counterevidence to submission = public availability |
| v1 title | Exact v1 bytes retrieved in 2026 | Version content verified; public existence at T not independently timestamped |
| Category | Current/v1 sets; four differences | Returned set measured; historical population unresolved |
| Vocabulary | Pre-cutoff survey context in preregistration | Exact alias/rule availability and reference protocol not frozen/accepted |
| Denominator membership | Complete current query | Historical completeness unresolved |
| Source state | Frozen 2026 XML/code/config/hashes | Offline replay verified; not a 2019 snapshot |

[Direct XML cross-check](../../../experiments/research_exit_20260927/runs/20261010-development-01/crosscheck.json) lists nine IDs with an ID month after June but published before T. Example: 1908.04451 reports `2019-03-07T08:37:23Z`. [Official policy](https://info.arxiv.org/help/availability.html) assigns IDs in first-announcement month and distinguishes submission from public posting. **INFERENCE:** applying that documented policy to these IDs is counterevidence to treating every returned work as public by T; exact historical announcement timestamps remain unverified. Do not subtract nine and claim a repaired historical denominator. [OAI datestamp](https://info.arxiv.org/help/oa/index.html) is last metadata modification, not original submission/public availability. No OAI requests were made. **E3 NOT PASSED.**

## 09. Frozen input and replay

Two separate Python processes produced byte-identical audit.json (SHA-256 `53a5aff1d8ea577e5789c7dc96a784f9f3c46339495e38ea78d266b41158dbd8`) and normalized-records.json (`a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1`): [verification](../../../experiments/research_exit_20260927/runs/20261010-development-01/replay-verification.json). Same-host replay only, not independent human replay. A separate direct-XML parser checked 598 records, nine hashes, monthly counts and source references without importing acquisition/audit parsers.

17 tool unit tests and 15 existing synthetic checks passed. Synthetic output still reports the two preserved legacy access manifests; its real_sample status does not describe this new corpus. Real-corpus evidence is in audit.json/crosscheck.json. Package checks are recorded separately in package-validation.json under the run. These checks do not establish product E1–E8.

Replay from repository root into a new directory:

```powershell
py -3 experiments/research_exit_20260927/offline_audit.py --run experiments/research_exit_20260927/runs/20261010-development-01 --output experiments/research_exit_20260927/runs/20261010-development-01/reviewer-replay
py -3 -m unittest discover -s experiments/research_exit_20260927 -p "test_*.py" -v
```

Do not overwrite a run or replay directory. Offline audit makes no API calls.

## 10. Bias, limitations and unresolved claims

cs.SE is not all software testing literature. Live query state is not an atomic provider-wide snapshot despite consistent observed counts/pages. Withdrawals/reclassification/removal and announcement delays affect membership. Zero missingness applies to returned records and syntactic checks only. No independent field annotations, real signal comparison, reference labels, accepted threshold, product demo, benchmark or user validation were performed. Reproducibility in 2026 does not establish validity at a 2019 cutoff.

## 11. B → A handoff (#64)

A can inspect v1 titles, measured retrospective population and every raw reference. The lexical pattern was checked only on a synthetic title, not as a corpus signal. Before D08/freeze, address temporal/membership gaps, development/holdout overlap from late ID months, versioned vocabulary and independent reference/quality protocol. Next discriminating test: locate a bounded dated category/announcement snapshot covering T, starting with the nine contradictory IDs; preregister query/transfer budget/checksums before new acquisition. Current OAI datestamp is insufficient. A provider or temporal-resolution change needs separate proposal/preregistration.

## 12. PROPOSED D07 / insufficient evidence

**PROPOSED:** retain arXiv as a feasible bounded retrospective candidate; do not accept it as an as-of 2019 corpus. Alternatives: obtain dated membership/public-availability evidence; propose retrospective-only scope to the owner; or preregister compatible historical DBLP evidence (April alone cannot cover six months). Recommendation: preserve this run and investigate historical evidence before dependent product/holdout work. A complete historical field/membership/vocabulary packet would falsify the insufficient-evidence conclusion. D07/D08/freeze need explicit owner acceptance at #70; D09 remains later. No issue was closed, gate accepted, merge/release/deployment performed.
