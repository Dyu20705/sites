# 07 — Provider screening and access results

**27 September 2026 — #65, screening completed; measured corpus audit blocked.** No provider is accepted. The documentation screen below is not a field-coverage measurement. Cost means documented access conditions; runtime and transfer costs are unmeasured.

## Five-candidate screen

| Candidate / evidence ID | VERIFIED from inspected official documentation | Inference, unknowns and screening outcome |
| --- | --- | --- |
| arXiv / EL-101 | [API manual](https://info.arxiv.org/help/api/user-manual.html), QuickStart/§3.1/§3.3/§5.1.1: the documented query endpoint is `http://export.arxiv.org/api/query`; Atom IDs/titles, versioned retrieval, submission dates, paging and totals are described. [Terms](https://info.arxiv.org/help/api/tou.html): descriptive metadata CC0; one connection, ≥3 seconds between requests. | **First bounded probe** remains reasonable, but both executed probes used HTTPS rather than the inspected manual HTTP endpoint. Their 406s are endpoint-confounded and do not establish failure of the documented path. Public availability and historical category membership still need verification. Not disqualified as a provider. |
| OpenAlex / EL-102 | [Attributes](https://help.openalex.org/data/works/attributes/): `id`, `title`, `publication_date`, `created_date`, `updated_date`; update time concerns the current work object. [Authentication](https://help.openalex.org/api/authentication/): keyless basic queries; cursor paging beyond basic limits. [Snapshot](https://help.openalex.org/access/snapshot/): free anonymous public dump and separate paid daily snapshots. | Current metadata does not itself reconstruct historical field values. A bounded historical partition/extract has not been demonstrated. **Reserve candidate**, no sample acquired. Data is CC0 per [API reference](https://help.openalex.org/api/); document access does not measure coverage. |
| Crossref / EL-103 | [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) and [schema](https://github.com/CrossRef/rest-api-doc/blob/master/api_format.md): DOI, title, publication/deposit/index dates and cursor retrieval. [Licensing](https://www.crossref.org/documentation/retrieve-metadata/): bibliographic metadata generally reusable; abstracts may remain copyrighted. [Snapshots](https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads): see public-data-file route; monthly snapshots require Metadata Plus. | Current deposit/index timestamps do not supply past field values. Free annual dump feasibility remains unmeasured; monthly paid route conflicts with this sprint. **Reserve**, not sampled. Quotas must be read from response headers before any acquisition; no rate figure assumed. |
| Semantic Scholar / EL-104 | [Graph documentation](https://api.semanticscholar.org/api-docs/snippets): `paperId`, `externalIds`, `title`, nullable `publicationDate`, `year`. [Official tutorial](https://webflow.semanticscholar.org/product/api/tutorial): release-specific datasets exist, but download links require an API key. | **Historical-download path blocked under no-credentials assumption.** Not evidence of no historical support. Service terms and dataset-specific redistribution permission remain unresolved; no records downloaded. Missing exact dates may prevent monthly bins; no measured missingness. |
| DBLP / EL-105 | [Snapshot guidance](https://dblp.org/faq/4621382.html): persistent monthly releases rather than the mutable daily dump. The exact [April-2019 DROPS artifact](https://drops.dagstuhl.de/entities/artifact/10.4230/dblp.xml.2019-04-01) verifies DOI/version `2019-04-01`, CC0, file `dblp-2019-04-01.xml.gz` (468.04 MB), MD5 `cdf6416c27ab24eaef5aa4560e38aa3c`, and schema DOI. [XML guidance](https://dblp.org/faq/1474681.html) documents streaming parsing/local DTD. | **Snapshot identity is now verified**, but no bounded venue/domain extract or field fitness has been measured. XML work key/title/year can support title-level annual analysis; month precision must not be invented. The earlier legacy-path HEAD reset is retained as an access observation, not evidence that the snapshot is absent. |

DBLP's key/title/year description is supported by [Ley (2009), §2, pp.1–2](https://www.vldb.org/pvldb/vol2/vldb09-98.pdf), linked from its XML guide. This is a historical schema description, not measured fitness of a current or historical extract. The paper's historical-log discussion is not proof that such a log remains accessible today.

## Field mapping for the attempted arXiv audit

| Logical field | Documented path | Measured fitness |
| --- | --- | --- |
| Identity/version | Atom `entry/id`, explicit `id_list=<id>v1` | NOT MEASURED |
| Concept-bearing text | `entry/title` (string); abstract excluded from signal | NOT MEASURED; no missingness estimate |
| Event time | `entry/published`; `entry/updated` relates to retrieved version | NOT MEASURED |
| Scope | `entry/category/@term`, `cat:cs.SE` query | Historical membership UNKNOWN |
| Denominator/completeness | `opensearch:totalResults`, `start`, `max_results` | Total UNKNOWN; no page succeeded |
| Availability | Version/announcement evidence, not retrieval timestamp | NOT VERIFIED |

[Version policy](https://info.arxiv.org/help/versions.html) describes permanent public versions; [availability policy](https://info.arxiv.org/help/availability.html) distinguishes submission from public announcement and permits moderation delay. These strengthen the need to audit the exact fields rather than infer availability from `published`. Current documentation is not proof of the 2019 state for a particular record.

## Predeclared sample and observed access failures

The shared [preregistration](../../../experiments/research_exit_20260927/preregistration.json) fixes the six-month cs.SE query, ascending submission order, pages ≤500, all requested `v1` IDs, and a 2,000-work stop bound. No first-N sample or signal-based selection was substituted.

| Observation | Result / reproducible artifact |
| --- | --- |
| Initial HTTPS request, 12:46:11–12:46:12 UTC | HTTP 406; [initial manifest](../../../experiments/research_exit_20260927/acquisition.json). Endpoint differs from the HTTP base shown in the inspected manual. |
| AM-01 HTTPS request, 12:47:33–12:47:34 UTC | Same query with explicit Atom Accept; HTTP 406, empty diagnostic response excerpt; [manifest](../../../experiments/research_exit_20260927/accept-atom-diagnostic/acquisition.json). Same endpoint-scheme confound. |
| AM-02 documented-HTTP diagnostic | **NOT RUN in this changeset.** `acquire.py --http-endpoint-diagnostic` writes to a separate manifest, records redirect/final URL, and stops after one request. |
| DBLP legacy-path HEAD, 12:51:08 UTC | Connection reset, no HTTP status/size obtained; [probe](../../../experiments/research_exit_20260927/dblp-access.json). Exact snapshot metadata was later verified through the DOI-backed DROPS artifact. |
| Returned usable corpus records | **0**; this does not mean the query has zero matches |
| Total, missingness, duplicates, revisions, invalid values, coverage, truncation | **NOT MEASURED**, not 0% |
| Real frozen snapshot, real-data replay, real signal comparison | **NOT AVAILABLE / NOT RUN** |

Requests followed the declared stop behavior; no alternate identity, proxy, credential or bulk download was used. Acquisition manifests are access evidence, not a sample dataset. The arXiv 406s are additionally confounded by using HTTPS instead of the HTTP base shown in the inspected manual, so provider/network/client construction is not localized. The DBLP reset concerns only the legacy direct path; the DOI-backed snapshot artifact is independently verified.

## B → A handoff and next discriminating test

Return **INSUFFICIENT EVIDENCE**: no measured field fitness, denominator or temporal-valid corpus can yet support D08. Keep all real-signal, support and quality claims unresolved.

Run the smallest clean access test first: exactly one AM-02 request against the HTTP endpoint shown in the inspected arXiv manual, recording redirect/final URL/status without acquiring the holdout. A successful response still requires version-specific text, historical membership and announcement evidence before D07. If that path still fails or temporal semantics remain inadequate, preregister a bounded streaming extract from the verified DBLP snapshot `10.4230/dblp.xml.2019-04-01`. Before downloading/scanning the 468.04 MB upstream artifact, declare transfer/storage/scan budget and an exact ≤5,000-work venue/domain/period extraction rule; the complete archive is much broader than the M1 corpus. Use annual bins if only publication year is supported. Do not silently replace the original preregistration or pretend a live DBLP API query reproduces that archive.

There is no evidence here that all five providers fail E3. There is presently no **verified accessible bounded sample** that passes it. No second source is being integrated.
