# 02 — Source Audit Plan

**Status:** audit procedure ready; all provider fitness claims are UNVERIFIED. No sample has been acquired or corpus frozen. Owner: work package B, with field requirements from A in the [backlog](../master/08_MONTH1_BACKLOG.md).

## Candidate screening

Screen these existing D07 candidates against the same requirements. Names identify candidates, not endorsements or verified capabilities. Locate and record current official documentation during execution.

| Candidate | Required screening record | Current outcome |
| --- | --- | --- |
| arXiv | Access/export, terms, exact fields, coverage, versions, dates, historical availability and replay | NOT AUDITED |
| OpenAlex | Access/export, terms, exact fields, coverage, versions, dates, historical availability and replay | NOT AUDITED |
| Crossref | Access/export, terms, exact fields, coverage, versions, dates, historical availability and replay | NOT AUDITED |
| Semantic Scholar | Access/export, terms, exact fields, coverage, versions, dates, historical availability and replay | NOT AUDITED |
| DBLP | Access/export, terms, exact fields, coverage, versions, dates, historical availability and replay | NOT AUDITED |

Do a documentation screen for all five; perform a sample audit only for a candidate whose documented fields, permitted use and access could satisfy the bounded task. If several qualify, audit the one with the clearest historical availability and replay evidence first, then the lowest documented acquisition burden; record the rationale, without accepting D07. Stop expanding the audit when one candidate has sufficient measured evidence for a D07 proposal and the alternatives have explicit screening outcomes. Audit another only to resolve a material gap or tradeoff. A documentation claim is not measured coverage.

## Field contract to inspect

For every logical requirement below, record the exact provider field/path, documentation section, type/null behavior, observed sample values and whether the field is required by the candidate signal. This mapping is an audit artifact, not a physical schema.

| Logical requirement | Purpose and checks |
| --- | --- |
| Work ID, source URL, version/revision ID | Reopen observations; inspect duplicate and revision behavior; do not equate work and version |
| Title and any required abstract/category text | Concept assignment; missingness and changes in text/vocabulary |
| Publication/submission dates | Record the event represented, precision and possible revision; do not treat different events as interchangeable |
| Update/index/acquisition dates and historical snapshots | Separate event time from availability time; establish when each used value was knowable |
| Scope fields and corpus totals | Reproduce query membership and denominator, including nonmatching concept records for share |
| Citation/reference observations, only if needed | Historical value at each cutoff; current cumulative values cannot reconstruct past values |
| Query, export identity and provenance | Reconstruct acquisition, cutoff, configuration and raw observation references |

## Access, sampling and temporal audit

1. Record official evidence with URL, section/version and inspection date for authentication, API/bulk/snapshot access, quotas, rate limits, version changes, storage/redistribution/demo permissions and expected request/time/storage costs. Unknown terms remain unresolved; do not assume a public API grants redistribution rights. Never put credentials in artifacts.
2. Before acquisition, write the candidate domain/query, completed period, cutoff, acquisition time and sampling rule. Keep within 5,000 records and 24 completed months. If results exceed the bound, specify deterministic sampling across relevant time strata, including seed/order and inclusion rule, and disclose its bias. Do not interpret the first N results as representative. Do not run signals to choose a sample.
3. Check pagination ordering, truncation, count consistency and query completeness. Report requested versus returned records, duplicates, revisions, invalid values and missingness with numerator/denominator by field and time stratum. Distinguish fields absent from schema, absent from records and invalid values. Record coverage exclusions and publication/indexing delay.
4. For each field used at cutoff T, record its event meaning, mutability, evidence that the specific value was available by T, and whether the source can reproduce that state. Today’s retrieval timestamp or an old publication date alone does not establish historical availability. Include vocabulary and later metadata corrections in this assessment.
5. Test retention of permitted raw observations, stable snapshot/export identity and provenance. Define the smallest subsequent replay/idempotency checks on frozen input; report separately which checks actually ran. A live query that changes is not a replay snapshot.

## Decision handoff and failure

Return a comparison separating VERIFIED evidence, ASSUMPTION and unknowns; measured sample coverage/missingness; temporal availability by field; allowed retention/sharing; cost and sampling bias; disqualifying gaps; and a **PROPOSED D07** or an insufficient-evidence report. Link the sample/query/snapshot and each supporting source in the [ledger](01_EVIDENCE_LEDGER.md).

Send A the feasible fields, counting/denominator limitations and time semantics before it finalizes D08. First narrow the candidate signal or corpus if a field is missing; a second provider requires a measured need and human acceptance. If historical availability cannot be established, label the result retrospective, **E3 NOT PASSED**, and request scope review; do not silently pass M1. No provider selection, live-data integration or implementation stack is authorized by this plan.
