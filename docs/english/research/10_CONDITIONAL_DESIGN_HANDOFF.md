# 10 — Conditional Design Handoff (NOT AN ACCEPTED D09)

**Status: PROPOSED / NON-BINDING.** Prepared alongside the 10 October 2026 Research Exit review to reduce future design latency; it does not satisfy #71, approve D09 or authorize dependent product implementation. **#70 Research Exit remains NOT PASSED.** All provider-specific mappings, temporal behavior, bins, signal, thresholds, storage and UI/runtime choices are candidates until D07/D08/D09 receive explicit owner acceptance.

## Required invariant-first slice

bounded frozen source extract → immutable raw observation + provenance → cutoff-valid eligible-work projection → deterministic lexical match/count/share → evidence bundle → in-process query → minimal local dashboard → snapshot replay.

Keep the scientific meaning separate from the data plumbing. No LLM/embedding-based classification, forecasting, recommender, multi-provider identity platform, graph DB, distributed queue, public hosting or agent subsystem in M1.

## Provisional logical contracts (provider-neutral)

- **SourceSnapshot**: provider, source_release_uri, source_release_date, published_checksum, verified_download_hash, access/license notes, acquisition timestamp, freeze_id.
- **RawObservation**: source_snapshot_ref, raw_locator, raw_hash, provider_work_key, provider_version_key if available, raw fields and parsing diagnostics. Store bytes only when permission allows, otherwise record reproducible reference and limitations.
- **EligibleWork**: work_key, version_basis, title_value, event_time and precision, observed_available_at with evidence, membership_definition + membership_available_at and evidence, inclusion/exclusion reason, raw observation refs.
- **ConceptDefinition**: concept_id, lexical rule/version, allowed aliases, vocabulary_available_at and supporting independent evidence; no term introduced after target cutoff.
- **SignalPoint**: concept_id, bin, n_matches, n_eligible, share or INSUFFICIENT_EVIDENCE with typed reason, contributor_ids, denominator_ids, method_version.
- **EvidenceBundle**: signal_ref, exact contributing work IDs and all denominator IDs (or immutable complete membership file + hash), observation provenance, raw/snapshot/config/code hashes, cutoff interpretation, inclusion rules, missingness, sensitivity report and limitations.
- **ReplayManifest**: input snapshot hashes, config/code/runtime versions, deterministic seed if any, freeze record, semantic output hash, validation outcomes.

## Temporal contract must be selected before coding

**Option A — fixed-snapshot as-of:** claim only what the verified provider release at its stated snapshot time contains, with a declared indexing-lag and membership limitation. One snapshot can show its own population; older publication dates alone do not reconstruct earlier observable states. Suitable only if D07 verifies required fields and cutoff.

**Option B — retrospective event-time series:** use a fixed later snapshot but describe event dates of its records, explicitly avoid a historical as-of/backtest claim; with the currently accepted D05/E3, this option **does not by itself pass M1**. Owner scope change required if selected as the final objective.

Never infer monthly bins from DBLP records that only have year precision. Never apply a present-day category/ontology to a 2019 as-of claim without qualifying the change.

## D09 candidate comparison (not selected)

| Dimension | Minimal candidate | Alternative and trigger |
| --- | --- | --- |
| Storage | Files (raw snapshot + normalized JSONL + immutable manifests); use SQLite only if query/replay measurements require indexing | Server DB only when measured, not for presumed scalability |
| Runtime | Python standard library deterministic batch execution | Add a library only if it reduces tested complexity |
| Query | In-process function reading frozen results/evidence | HTTP API only when remote client requirement is accepted |
| Dashboard | Local read-only HTML view with one concept/time plot and evidence links | Framework UI only if manual usability task fails |
| ML/LLM | None | Separate post-M1 hypothesis and evaluation |
| Security | No secrets, public metadata only, bounded requests, input-size limits, read-only demo | Revisit with actual protected data |
| Deployment | Clean local replay/package, no public service | Publish only after explicit deployment gate |

## Acceptance and test hooks

Before product code: accepted D07/D08 raw contract, historical cutoff semantics, formula and vocabulary, numerical support and quality rule, development/holdout freeze, and budget. Gate #71 then chooses D09 explicitly.

Verification should test zero vs missing, duplicate versions, record eligibility, changed vocabulary, late-indexed observations, cutoff boundary, null titles, denominator completeness, idempotency, semantic replay, evidence trace and clear user-facing abstention. Prepare E1–E8 as validation targets, never assert they passed from synthetic fixtures alone.

## Stop conditions

- **No data**: do not start platform build; finish bounded acquisition audit.
- **Only retrospective data**: request explicit D05/E3 scope review; do not relabel it as as-of evidence.
- **No independent evaluation protocol**: do not freeze D08 or inspect holdout.
- **No accepted D09**: do not create production schema, API, package framework or dashboard on the authoritative implementation branch.

**Next authorized work:** #64/#65 complete measured evidence → owner reviews #70 D07/D08 and frozen contract → #71 evaluates this candidate and selects D09 → #72 implements only the accepted slice.

