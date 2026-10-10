# Local evidence review — 10 October 2026

Reviewed branch: `research/exit-evidence-20260927`, session baseline `3c23a44ce0f11e243b0e0ecafef2faa93866d123`; diagnostic instrumentation committed at `d8e330b`. Later output isolation, audit and evidence are reviewed in the working tree before the next logical local commit.

No confirmed BLOCKER/MAJOR remains for the **claimed bounded retrospective audit**. **Historical/as-of suitability remains insufficient evidence; E3 and #70 are NOT PASSED.** This review does not approve D07/D08/D09 or product/holdout work.

Reviewed scope:

- `acquire.py`: count-only diagnostic, redirect/error provenance, serial request delay, output isolation, same-config AM-02 guard, count bound/drift, page lengths, duplicate IDs and explicit-v1 matching. The two old acquisition manifests and preregistration remain byte-identical to the session baseline.
- `test_acquire.py`, `offline_audit.py`, `test_offline_audit.py`, `crosscheck.py`: offline field normalization, missing/invalid separation, checksum failure, date/identity validation, exhaustive frozen pagination and v1 population, trace references, null historical availability and independent direct-XML comparison.
- `.gitattributes`: JSON/XML bytes preserved; provider XML whitespace exempted from whitespace lint because the frozen response contains one trailing space. Raw response bytes were not edited.
- AM-02 and development manifests, all ten newly acquired raw XML responses, frozen input copies, preflight/config/code hashes, pre-execution development and offline audit declarations: inspected against request/response contents; hashes checked.
- Both replay outputs and verification: separate processes, matching semantic and byte results; cross-check validates all 598 normalized records. No independent human replay claimed.
- Paired English/Vietnamese real-corpus reports, provider/exit update notes and current-state snapshots, experiment README and amendment log: technical meaning/numbers aligned; historical versus current and local versus remote claims separated. All changed documentation is in the reviewed scope.
- Existing synthetic checks and package validator: run, with old probe-only status explicitly distinguished from the new real-corpus audit. Historical validation output retained; current validation saved in this run.

Validation performed: 17 tool tests PASS, 15 existing synthetic tests PASS; direct XML cross-check PASS (598 records, nine development raw files); two audit replays byte-identical; package JSON/Python/link/status/input checks PASS; diff whitespace check PASS. These checks are research-tool evidence, not product E1–E8 verification.

Needs validation: precise historical public announcement timestamps, missing historical members outside the current query, exact historical vocabulary/rule state, independent field/reference annotation and quality criteria. Nine IDs with post-cutoff ID months are documented temporal counterevidence, with the announcement interpretation explicitly identified as inference from current official policy.

Skipped: intermediate version acquisition, new OAI/provider requests, holdout, real signal/threshold evaluation, product implementation, benchmark and user validation. They are outside this run's contract or depend on unresolved evidence/owner acceptance. No remote posting, push, merge, issue closure, release or deployment was performed.
