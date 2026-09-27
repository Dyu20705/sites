# 08 — D07/D08 decision packets and Research Exit review

**PROPOSED — 27 September 2026. Recommendation: keep #70 NOT PASSED.** This packet is reviewable as an insufficient-evidence outcome. It is **not** ready for approval as a frozen experiment contract. D05/D06 remain ACCEPTED; D07/D08/D09 remain PROPOSED.

## D07 — Domain/source/corpus

**Goal:** one reproducible, cutoff-valid scholarly corpus for the accepted researcher task, within one source, ≤5,000 works and ≤24 completed months.

**Exploratory candidate:** software engineering/testing, arXiv `cat:cs.SE`, January–June 2019 development, July–December 2019 candidate holdout, distinct work IDs with explicit first-version titles. Six-month acquisition has a tighter 2,000-work stop bound. Query membership is currently defined by today's category index, which is an unresolved historical-membership risk. Scope does not generalize to all software-testing literature.

**Evidence:** [EL-101–105 and access logs](07_PROVIDER_AUDIT_RESULTS.md). Neither attempted arXiv request returned records. DBLP's persistent-archive path is documented but the access probe failed. Missingness, counts, cutoff-valid membership and input snapshot are not established.

**Alternatives and trade-offs:**

1. Recover the declared arXiv access path and measure version/membership/announcement fitness. Smallest change to the investigation, but temporal evidence may still fail even after access works.
2. Preregister a DBLP historical-snapshot venue extract. Stronger documented snapshot identity; broader upstream transfer/scan and coarser publication time require a separate bounded audit, not automatic acceptance.
3. Current OpenAlex/Crossref/DBLP metadata for retrospective analysis. May help descriptive exploration, but does not satisfy unchanged E3 by itself. Semantic Scholar historical downloads also need a currently unavailable key.

**Recommendation:** do not select a final provider or freeze a corpus. Preserve the access failures and run the next bounded test in the provider report. No evidence supports declaring every provider impossible.

**Falsifier:** a permitted, complete, ≤5,000-work extract with required field coverage and field/vocabulary/membership evidence at T would overturn the present insufficient-evidence outcome. A successful HTTP response alone would not.

**Acceptance required later:** exact provider/domain/query/period, temporal interpretation, inclusion/version/sampling rules, sharing rights and verified snapshot identity. This packet does not ask the owner to approve an incomplete corpus.

## D08 — Signal/evaluation

**Candidate definition, not an accepted formula:** for month b, let C_b be distinct eligible first-version works in the corpus and M_c(w) the frozen lexical match. Then `N_b = |C_b|`, `n_cb = sum(M_c(w) for w in C_b)`, `p_cb = n_cb/N_b` when N_b>0. Retain both n and N beside p. Missing/incomplete inputs produce insufficient evidence, not zero. Count is the baseline comparator; share is the provisional primary candidate.

**Evidence:** [EL-001–005 and executed synthetic checks](06_RESEARCH_EXIT_EVIDENCE.md). Share cancels proportional corpus growth in the constructed null but cannot cancel changing composition, alias drift or selection bias. No empirical superiority or detection quality is established. The serious alternatives are unnormalized count, inflation-adjusted growth and burst; none is selected for production.

| Contract element | Current proposal / unresolved evidence |
| --- | --- |
| Unit/text | Distinct work; first-version title. Missing title must not silently become nonmatch. |
| Vocabulary | Exploratory fuzzing pattern in preregistration; completeness and all historical variants unverified. |
| Time | Monthly submission bins; historical cutoff candidate 2019-06-30T23:59:59Z. Actual availability must be proved separately. |
| Support/labels | **UNRESOLVED**. No growing/stable/declining/emerging label issued. Corpus data is needed to justify support and abstention rules. |
| Case/control | Fuzzing case from independent 2018 context; synthetic constant-share null. Context is not a reference trend label. |
| Reference protocol | **PROPOSED:** owner-designated reviewer labels concept relevance from permitted evidence without candidate outputs; record uncertain/disagreement cases. Researcher and annotator availability not yet confirmed. |
| Quality threshold | **UNRESOLVED**. Lexical agreement is not trend validity; do not invent a precision target or use the same formula as its own reference. |
| Sensitivity | **PROPOSED dimensions:** monthly vs adjacent two-month aggregation; exact “fuzzing” vs candidate variants; declared missing-field treatment. Numerical support/threshold ranges wait for development evidence. |
| Holdout | Candidate July–December 2019; unseen, not acquired or run. No freeze or confirmatory claim. |

**Recommendation:** retain count/share as the smallest exploratory baseline; finish measured data fitness and an independent evaluation rubric before acceptance. Do not code burst to compensate for absent data. Negative outcomes remain visible.

**Falsifier:** if a bounded corpus cannot support an independent denominator, lexical relevance or stable interpretation under declared sensitivity checks, narrow the construct or reject the candidate. Do not lower thresholds after holdout.

**Acceptance required later:** complete formula/unit/window/vocabulary/support/labels, case/reference protocol, quality threshold, numerical sensitivity ranges and exact development/holdout split. Owner approval of this investigation plan was not acceptance of these unknown values.

## Freeze record — deliberately NOT FROZEN

`RE-20260927-01` is an **audit preregistration**, not the M1 evaluation freeze. A future freeze must identify corpus/raw hashes, query/snapshot, case/control, period/cutoff, vocabulary version, formula/unit/denominator, support, reference rubric/threshold, sensitivity values, exposure log, code/config/environment and owner/date. Missing values above prevent that freeze. Never overwrite the audit preregistration to conceal access failure.

## Gate checklist and review findings

| Check | Status / evidence |
| --- | --- |
| D05/D06 and Research Entry | PASS — existing decision log and #68; not reopened |
| Bounded protocol, search log, construct/alternative notes | PRESENT — focused coverage only; no comprehensive-literature claim |
| Measured sample/denominator/field fitness | **BLOCKER — missing** |
| Historical availability, membership, vocabulary | **BLOCKER — unverified; E3 NOT PASSED** |
| Development signal comparison and quality/support justification | **BLOCKER — no real input** |
| Independent case/reference rubric and quality threshold frozen | **BLOCKER — incomplete** |
| Synthetic arithmetic, duplicate/version/cutoff/lineage checks | 15 methods pass in each of two processes; local evidence only |
| D07/D08 acceptance and versioned experiment freeze | NOT DONE |
| Holdout/product/user validation | NOT RUN; belongs after required gates |

Self-review uses `sites-review`: reviewed the changed docs, script/fixture behavior, acquisition manifests, replay output and bilingual status/ID alignment. No independent human review has occurred. Exact mechanical checks and remaining limitations are in the experiment README; no broad claim of product E1–E8 completion.

**Disposition:** prepare a draft PR as the evidence handoff; do not merge or close #64/#65/#70 automatically. The plan's insufficient-evidence branch has been reached, so downstream D09/build work remains blocked. The owner can review this result without accepting D07/D08.

## Schedule consequence

The 17 October M1 deadline stays unchanged. The accelerated 28 September D09 / 29 September–2 October build / 3–5 October demo schedule remains conditional on Research Exit. No elapsed date passes a gate. Keep current WIP at two; new directions wait for the existing slice's gate decision.
