# 01 — Evidence Ledger

**Status:** capture format ready; no new literature findings or provider measurements recorded. The [prior-art map](../master/03_PRIOR_ART_MAP.md) remains the source for the limited checks recorded on 18 September. Those checks have not been upgraded to new full-text reviews.

## Claim record

Use one record per material claim, with a stable ID such as `EL-001`. Several claims may reference one source; they are not independent studies. Record `unknown`, `not inspected`, or `not applicable` explicitly instead of filling gaps by inference.

| Field | Required content |
| --- | --- |
| Source/version/location | Title, authors/organization, year, DOI/URL, version, section/page/table; inspection date and access depth |
| Claim | Narrow statement actually supported or challenged |
| Evidence type | Empirical / theoretical / benchmark / design / opinion |
| Population and period | Domain, dataset, unit and time period studied |
| Method | Method, comparison and relevant assumptions |
| Directness | Directly inspected evidence versus inference or secondhand citation |
| Limitations | Bias, confounders, missing information, access limits and applicability |
| SITES relevance | RQ, D07/D08 or verification of D05; work package A/B |
| Status | supports / contradicts / mixed / unresolved, relative to the named claim |
| Provenance | Search-record ID, extractor, artifact/snapshot reference if any, and changes to this record |

For long records, use a two-column table under the claim ID rather than an unreadably wide table. Link both language versions by the same ID and preserve technical meaning.

## Search and exclusion records

For each search record retain service, exact query, date, filters, pages/results screened, relevant source IDs and limitations. For each excluded item retain source/version and exclusion reason. Distinguish duplicate versions from independent evidence. Keep conflicting results and inaccessible sources visible.

## Existing leads — not new ledger findings

| Lead from the prior-art map | Recorded inspection boundary | Next action |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015) | Abstract only; no full critical review | A: inspect full paper before expanding the supported claim |
| Kleinberg (2002) | Author description and paper checked; no SITES experiment | A: extract assumptions and compare with a simpler baseline |
| Sandve et al. (2013) | Relevant rules checked; no SITES experiment | A+B: map rules to trace/replay evidence without claiming implementation |

No empirical population, exact paper location or new finding is invented for these leads. Create a claim record only after inspecting the relevant source and preserving its access limits. No source count or completed table establishes corpus fitness or passes the Research Gate.
