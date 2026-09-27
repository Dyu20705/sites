# Research Exit evidence spike

Exploratory evidence for #64/#65, not a product runtime or D09 choice. Baseline: `0a853636ef6d1be9d3bb85058f34faf368fcb6ce`. D07/D08 remain PROPOSED. The preregistration precedes record acquisition and defines both the field handoff and bounded development sample. No holdout is run.

Only Python standard-library modules are used (Python 3.10+). The host already has Python 3.14.7; this does not select a product dependency. Git preserves JSON bytes without newline conversion so manifest/config checksums survive checkout; generated replay reports explicitly use LF. Acquisition manifests retain their original bytes.

Acquisition is a separate, explicit network action. Offline audit and synthetic checks must never silently fetch data. Raw metadata is CC0 under [arXiv API terms](https://info.arxiv.org/help/api/tou.html); papers are not redistributed. The raw metadata snapshot is an acquisition-time snapshot, not proof of historical availability.

The final report must distinguish empty/missing/inaccessible data, retrospective evidence and as-of evidence. A failed acquisition is retained as an access observation, not invented missingness measurements.

## Recorded outcome

Both preserved arXiv count attempts returned HTTP 406, but post-run review found that they used HTTPS while the inspected arXiv API manual presents the query endpoint over HTTP. The 406s are retained as exact request observations but are **endpoint-confounded** and do not establish failure of the documented API path. AM-02 adds an isolated one-request HTTP diagnostic mode that records redirect/final URL; it has not been executed in this changeset. The legacy DBLP archive HEAD request was reset, but the exact April-2019 snapshot is now independently verified as the official DROPS artifact `10.4230/dblp.xml.2019-04-01` (CC0, 468.04 MB, published MD5 and schema DOI). No raw corpus file was obtained: `raw/count.xml` in a failed request manifest is the **intended** output path, not a claim that this file exists. No missingness percentage, real signal value or historical-availability pass is recorded.

`search-log.json` records inspected sources, search limitations and the deviation from the planned Scholar interfaces. `fixtures.json` contains only hand-specified synthetic inputs and expected values. The `available_at` and `membership_available_at` fields are synthetic stipulations, not provider fields that have been measured.

## Offline replay

From the repository root, using an existing Python 3 interpreter:

```text
python experiments/research_exit_20260927/checks.py --output experiments/research_exit_20260927/results/run-1.json
python experiments/research_exit_20260927/checks.py --output experiments/research_exit_20260927/results/run-2.json
```

These commands do not use the network. Each runs 15 test methods, with seven hand-calculated series scenarios. Compare the two output hashes. Outputs include expected/actual values, lineage IDs, input/code hashes and a real-sample status explicitly marked NOT_MEASURED_ACCESS_FAILURE.

Coverage includes arithmetic, empty/missing bins, invalid counts, denominator drift, duplicates, revisions, conflicting observations, future/late availability, unknown availability, vocabulary cutoff, missing title, unknown coverage, alias false-negative risk and order independence. The successful acquisition/pagination path has **not** been exercised against a real response. No benchmark, product test suite, independent human replay, reference annotation or holdout is claimed.

Run the separate offline package check from the repository root:

```text
python experiments/research_exit_20260927/validate.py
```

The saved [validation report](results/validation.json) records relative-link target checks, JSON/Python parsing, paired evidence IDs, decision statuses and replay/input hashes. It does not check external URL availability, Markdown anchors or translation meaning. Translation meaning and source attribution were self-reviewed manually. The matching [first](results/run-1.json) and [second](results/run-2.json) outputs establish same-host replay only.

Precommit verification compared Git index blob IDs with unfiltered working-file hashes for all 17 experiment artifacts; all matched after applying the byte-preservation attributes. `git diff --cached --check` passed. This checks stored bytes, not an independent machine's execution.

## Self-review scope and unresolved findings

Review target: `research/exit-evidence-20260927` against `0a853636ef6d1be9d3bb85058f34faf368fcb6ce`, for an insufficient-evidence handoff, not a passed Research Exit. Reviewed groups comprise all files in this experiment directory, the three new paired research reports, paired ledger/decision/backlog/current-state changes and four documentation indexes. Input/config declarations were compared with access manifests and replay output. Existing source documents were consulted for changed claims; no full audit of unchanged repository content was performed.

- **BLOCKER for #70:** no real frozen corpus or field/denominator measurements; see [provider report](../../docs/english/research/07_PROVIDER_AUDIT_RESULTS.md). Smallest next check: run exactly one AM-02 request against the HTTP endpoint shown in the inspected arXiv manual and record redirect/final URL/status. If that clean path still fails or temporal semantics remain inadequate, preregister a bounded streaming extract from the verified April-2019 DBLP DROPS snapshot before any large transfer/scan.
- **BLOCKER for #70:** historical field/membership/vocabulary availability is unverified. Exact versions or old publication dates alone cannot repair this; inspect the availability evidence at the declared cutoff.
- **BLOCKER for #70:** no real development comparison, independent reference trend rubric, justified support/quality threshold or accepted freeze; see [decision packet](../../docs/english/research/08_D07_D08_EXIT_PACKET.md). Complete these before any holdout.
- **Needs validation before reuse:** successful acquisition pagination/version handling is unexercised; the original run lacks an execution-time code hash. These limits prevent treating the acquisition spike as a verified data pipeline.

The blockers remain open research findings; they are not concealed by passing synthetic checks. No independent reviewer or user validation is claimed.

`acquire.py` and `probe_snapshot.py` are separate opt-in network tools. They refuse to overwrite existing manifests. Do not delete recorded failures to retry. The initial/AM-01 manifests were produced with HTTPS requests; AM-02 uses its own `http-endpoint-diagnostic/` directory so the corrected endpoint test cannot rewrite history. The original acquisition run still lacks an execution-time code hash; preserve that provenance limitation rather than inventing one retroactively. The old DBLP HEAD probe is also historical evidence and must not be rewritten now that an exact DOI-backed snapshot artifact has been located.

See paired reports [English](../../docs/english/research/08_D07_D08_EXIT_PACKET.md) / [Tiếng Việt](../../docs/vietnamese/research/08_D07_D08_EXIT_PACKET.md). Research-ready remains NOT PASSED.
