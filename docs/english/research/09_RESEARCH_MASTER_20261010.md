# 09 — Research Master and Research Exit Review (10 October 2026)

**Subsequent critical-path evidence:** [D08 real development evaluation](14_D08_DEVELOPMENT_EVALUATION_20261010.md) supersedes the missing real-corpus/signal and open-handoff claims in this earlier dated review. #65 completed; #64 has real count/share. Independent reference quality and as-of validity remain unresolved; D07/D08/D09 PROPOSED, E3/#70 NOT PASSED; demo-ready deadline 15 October. The prior literature synthesis remains useful historical evidence.

**Status: evidence synthesis complete for the inspected sources; empirical Research Exit NOT PASSED.** This is a dated, reviewable extension of the 27 September PR #75 evidence packet, not a D07/D08 acceptance, not a product result, and not a claim of exhaustive prior-art coverage. Research Entry #68 PASSED; #70 is the authoritative Research Exit gate. D05/D06 ACCEPTED, D07/D08/D09 PROPOSED. No holdout was inspected.

## Decision question, construct and boundary

M1 asks whether one or two simple, inspectable signals can describe a concept appearing more or less frequently in a bounded scholarly corpus, while making the corpus, calculation and supporting observations independently traceable and reproducible.

Operational candidate: document-level **first-version title lexical prevalence in a declared corpus**. For time bin b, N_b is the number of distinct eligible corpus works (including nonmatches), n_cb is the number whose eligible title matches a versioned concept rule, and p_cb = n_cb / N_b for N_b > 0. An incomplete denominator, missing required title, unknown historical membership or unverified cutoff availability means INSUFFICIENT EVIDENCE rather than zero. Retain counts beside proportions. This is a **candidate**, not a frozen D08 contract.

The allowed claim is a measured change in lexical prevalence within a declared population. It is not emergence, semantic novelty, importance, impact, adoption, market success, causal change or prediction. A historical time stamp on a present-day API record is not evidence that the present value was available at historical cutoff T.

## Focused prior-art synthesis (directly inspected or carried from PR #75)

| Evidence | Supported claim within source scope | Counterpoint / transfer risk for SITES |
| --- | --- | --- |
| Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/html/1503.00673), sections 3–4 | Emergence is multidimensional; a count trend is not its definition | Conceptual review, not a validation of SITES |
| Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/bhs.pdf), sections 2, 4 (as recorded in EL-002) | Bursts are a credible alternative to simple frequency/share | More parameters and interpretation; not measured on target data |
| Sandve et al. (2013), [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285), rules 1–3 | Workflow/input/parameter preservation is necessary for replay | Reproducible wrong conclusions remain possible |
| Nelis et al. (2022), [General Growth Tendency](https://doi.org/10.1371/journal.pone.0268433), introduction/methods (EL-004) | Overall publication growth is a confound worth checking against topic growth | Different population and formulation; no corpus-specific quality proof |
| Štimec et al. (2026), [Identifying and evaluating emerging scientific trends through temporal n-gram analysis](https://doi.org/10.1007/s11192-026-05744-5), full HTML methods/evaluation/discussion, published 30 September 2026 | OpenAlex title/abstract n-grams, quarterly series, Kleinberg/MACD, corpus normalization and human pairwise/graded judgments form substantial prior art for interpretable lexical trend detection | Authors explicitly note synonym fragmentation, observer disagreement and the difference between lexical bursts and conceptual novelty. This invalidates any novelty claim based merely on transparent n-gram/frequency detection. Their measured population and task are not SITES M1 evidence. |

The 2026 paper is a high-priority **new prior-art finding** after the original 27 September packet. SITES M1's potential contribution should be framed as rigorous, narrow validation of temporal evidence, denominator provenance, abstention and replay for one corpus. This is a **proposed contribution**, NOT a demonstrated research gap or novelty claim.

## Five-provider feasibility summary

Documentation screening is not empirical data fitness.

- **arXiv:** API manual documents a query endpoint using HTTP in examples, Atom metadata and explicit version retrieval. The preserved PR #75 HTTPS requests returned HTTP 406; because they used a different endpoint scheme from the inspected manual, those negative observations are confounded. AM-02 is available as a separate one-request diagnostic, but has not been executed with a provider response in this review. Official [OAI-PMH guidance](https://info.arxiv.org/help/oa/index.html) documents arXivRaw version history and that OAI record datestamps reflect subsequent modification, not necessarily original availability; OAI cannot select by submission date. Historical membership/announcement evidence remains UNKNOWN.
- **DBLP:** precise official CC0 DOI-backed monthly snapshots EXIST: [2019-04-01](https://doi.org/10.4230/dblp.xml.2019-04-01), [2019-07-01](https://doi.org/10.4230/dblp.xml.2019-07-01), [2020-01-01](https://doi.org/10.4230/dblp.xml.2020-01-01). The April file is 468.04 MB (published MD5 cdf6416c27ab24eaef5aa4560e38aa3c). No file was downloaded or hash verified locally. April 2019 cannot establish a complete July–December 2019 candidate holdout or the entire January–June 2019 development window. July and January snapshots are possible **audit candidates**, not silently substituted experiment inputs. DBLP usually supports publication year; do not invent publication month, and distinguish year of publication from date indexed into the snapshot.
- **OpenAlex:** official [snapshot documentation](https://help.openalex.org/access/snapshot/) provides a complete downloadable corpus with release identity, but current public releases and present-day record dates do not reconstruct historical metadata values automatically. Size and partition strategy are excessive for an unfiltered M1 corpus; no bounded historical extract audited.
- **Crossref:** DOI/publication/deposit/index metadata and bulk routes are documented, but historical field-state reconstruction and bounded sample fitness remain unmeasured.
- **Semantic Scholar:** work metadata and release-based datasets are documented; access/keys, rights and cutoff-specific field-state evidence remain unverified in this project.

**Important snapshot semantics:** A frozen 2019 database release supports inspecting what that database contained at its release date, within its own known limitations. It does not prove original publication dates equal first public availability, field-level immutability, or completeness of works not yet indexed. A single snapshot does not certify another date or provider.

## Execution evidence and reproducibility

- Original PR #75 artifacts: 15 synthetic test methods reportedly passed in each of two same-host runs; no independent machine replay or successful real acquisition is claimed.
- New 10 October review: the seven hand-calculated series cases in the existing immutable fixtures were independently recomputed using the repository fixture values: **7/7 match expected arithmetic**. This is an arithmetic cross-check only, not a rerun of the 15 Python tests or E1–E8 product acceptance.
- A direct bounded arXiv HTTP request from the current execution environment failed before any HTTP response because DNS name resolution failed. This is an **environment constraint**, not an arXiv service result and not an AM-02 acquisition manifest. No corpus, provider missingness, reference labels or real signals were measured.
- No holdout, no database implementation, no user walkthrough and no independent dataset replay were performed.

## RQ and Research Exit audit

| Item | Finding |
| --- | --- |
| R1: construct / claim | Defined narrowly; supported by several prior-art families and reinforced by the 2026 paper |
| R2: count/share vs alternatives | Synthetic arithmetic and qualitative confound comparison only; real corpus comparison MISSING |
| R3: provider schema/access | Five-provider documentation screen; measured field coverage MISSING |
| R4: historical availability | UNVERIFIED; snapshot existence is not enough; E3 NOT PASSED |
| R5: evidence/lineage | Synthetic structure and proposed contract; real source-to-output lineage MISSING |
| R6: evaluation and holdout | Case/control candidates present; independent annotation rubric, support, numeric threshold and freeze MISSING |
| R7: one-source sufficiency | UNPROVEN; adding source two not justified |
| R8: user task | D06 accepted but no task-based user validation |
| #70: D07 + D08 accepted / frozen | **NOT DONE**, authoritative gate **NOT PASSED** |

The resulting failure is informative: no measured corpus means no supported denominator, temporal coverage or empirical signal quality. Do not rescue it by inventing thresholds, labelling retrospective plots as historical backtests, moving to D09, or using a later snapshot to claim an earlier as-of state.

## Smallest discriminating test and decision branches

1. Run **one** permitted AM-02 arXiv endpoint diagnostic from an environment that can reach the provider, preserving URL, redirect/final URL, request headers, HTTP status, response hash and error. Do not touch the original two manifests. Stop on access/rate-limit errors; no proxy or identity rotation.
2. If it succeeds, audit a **predeclared development-only**, <=2,000-work extract. Measure exact ID/version/title/category/announcement semantics; numerator and denominator completeness, missingness and membership at cutoff T. Keep all nonmatching records.
3. If it fails or temporal membership remains unprovable, prepare a **separate preregistration** for the exact DBLP monthly snapshot, extraction predicate/venue, publication-year binning, transfer/scan budget, <=5,000 retained works, published checksum verification, and matched snapshot/cutoff definitions. Evaluate indexing delay and whether the original case/holdout must be replaced *before* any holdout exposure.
4. Only after measured development evidence, propose numerical minimum support, independent blinded title-relevance reference protocol, detection-quality rubric, labels/abstention behavior and sensitivity ranges. Freeze D07/D08 with owner acceptance before confirmatory holdout.

**Decision outcomes:** a clean accessible and cutoff-valid corpus plus defensible evaluation can support a future D07/D08 proposal. A successful HTTP request alone cannot. If the only workable study is retrospective, record a scope-change proposal; the already-accepted E3 requirement does not automatically relax.

## Authoritative gate disposition

**Research Exit #70: NOT PASSED / INSUFFICIENT EMPIRICAL EVIDENCE — 10 October 2026 review.** This document is an agent research handoff, not the owner's acceptance/rejection of D07/D08. Do not open the #71 preimplementation execution lane, #72 build, or #73 evaluation as passed dependencies. A reversible, explicitly conditional design sketch may be prepared separately. The M1 deadline remains 17 October 2026 and no schedule date passes a gate.

