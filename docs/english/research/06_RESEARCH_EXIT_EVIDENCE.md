# 06 — Research Exit evidence, 27 September 2026

**Outcome: INSUFFICIENT EVIDENCE; research-ready NOT PASSED.** This is an investigation result for #64/#65, not acceptance of D07/D08, not a final M1 failure, and not a claim that no provider could work.

Baseline: `master@0a853636ef6d1be9d3bb85058f34faf368fcb6ce`. [#68 passed](https://github.com/Dyu20705/sites/issues/68#issuecomment-5795799412); D05/D06 remain ACCEPTED. #70 is the Research Exit authority. WIP remains #64 + #65; #69 is an evidence index. This package does not close issues or change the authoritative gate.

## Questions and field handoff

P0 remains unchanged. **RQ-measurement:** can a bounded lexical count/share distinguish changes from corpus growth and documented observation artifacts? **RQ-evidence:** can each value be reconstructed from cutoff-valid records, vocabulary, membership and transformations? Success on one does not imply success on the other.

The exploratory construct is **lexical prevalence in first-version titles within a declared corpus**, not all work on a topic, emergence, impact or adoption. Title-only matching is inspectable but misses aliases and topic mentions outside titles. No research novelty is claimed.

| A → B requirement | Purpose / acceptance evidence |
| --- | --- |
| Work ID + version + source URL | Distinct-work count; retain revisions without double counting |
| First-version title | Concept match; missing/changed text must be measured |
| Event time and public availability evidence | Event time assigns a bin; availability governs admissibility at T |
| Corpus membership, including nonmatches | Reconstruct denominator; concept-only retrieval cannot measure share |
| Historical membership and vocabulary state | A present-day category or later synonym must not enter an as-of claim silently |
| Query, ordering, snapshot/hash, acquisition time | Separate reproducible input from a mutable live query |

These are audit interfaces, not product schema. Concept text, date, membership and version must be usable at the relevant cutoff; today's retrieval time is not that proof.

## Literature evidence ledger additions

Extraction: Codex, 27 September 2026. Read depth is deliberately limited to the sections named. Source identities and exact discovery queries are in the shared [search log](../../../experiments/research_exit_20260927/search-log.json). These are critical notes, not an exhaustive systematic review.

| ID / source and inspected location | Evidence, population and interpretation | Limit / decision |
| --- | --- | --- |
| EL-001 — Rotolo, Hicks & Martin (2015), [What Is an Emerging Technology?](https://arxiv.org/html/1503.00673), §§3–4, Table 2 | Conceptual review; its multidimensional construct is broader than frequency. Directly inspected full-text sections, rather than the earlier abstract-only check. **supports** a narrow claim boundary. | Literature synthesis, not SITES validation; its search scope constrains coverage. R1/D08: do not name count growth “emergence”. |
| EL-002 — Kleinberg (2002), [Bursty and Hierarchical Structure in Streams](https://www.cs.cornell.edu/home/kleinber/bhs.pdf), §§2,4, pp.13–16 | Method plus conference-title examples; batched model uses relevant/total documents and penalized state transitions. Reports terminology effects. **mixed**: serious alternative to simple prevalence. | Conference series differ from six months of cs.SE. Parameters and vocabulary matter; no incremental benefit measured here. R2/R6: defer implementation of burst. |
| EL-003 — Sandve et al. (2013), [Ten Simple Rules](https://doi.org/10.1371/journal.pcbi.1003285), Rules 1–3 | Methodological guidance, not an empirical SITES study. **supports** retaining workflow, inputs, parameters, versions and intermediate evidence. | A reproducible mistake remains a mistake. R5: hashes and reruns support provenance, not detection validity. |
| EL-004 — Nelis et al. (2022), [General Growth Tendency](https://doi.org/10.1371/journal.pone.0268433), Introduction, Methods: GGT calculation/data collection | Empirical method comparing field growth with total publication growth; life-science topics, reviews and patents. **supports** testing denominator confounding; also supplies an alternative growth-rate formulation. | Not validated on this corpus; subtraction of growth rates differs from share. Low bases destabilize relative growth. Post-2019 methodology may guide research today, not historical vocabulary or labels. R2/R6. |
| EL-005 — Manès et al. (2018), [Fuzzing: Art, Science, and Engineering, v1](https://arxiv.org/abs/1812.00140v1), abstract and submission history only | Pre-2019 independent context identifies fuzzing as an established research subject. **supports** a candidate case, not expected growth. | Full-text critical review of this version not completed. No reference trend label or complete lexical dictionary follows from the abstract. R6. |

**Synthesis:** counting, prevalence and burst address related but different questions. Our synthetic evidence demonstrates that share can stay constant while count rises; it also changes when denominator composition changes. Neither quantity alone validates technological emergence. Unknown for SITES: usable historical corpus, lexical recall, minimum support, temporal validity and substantive detection quality. No gap/novelty claim has been established.

## Pre-output domain and case selection

The [preregistration](../../../experiments/research_exit_20260927/preregistration.json) was written before provider acquisition and signal output. It records software engineering/testing as the first audit domain; automated reasoning and distributed systems are deferred because this sprint lacks equally inspected pre-cutoff case context, **not** because their data quality was measured and found worse.

- Historical candidate: fuzzing, using EL-005 independently of signal attractiveness; no assumed direction.
- Development candidate: `cat:cs.SE`, submissions January–June 2019, monthly bins, at most 2,000 distinct works; attempt the complete query, stop if over bound.
- Holdout candidate: July–December 2019; neither acquired nor evaluated. Corpus and case remain unaccepted.
- Control: synthetic constant-share/corpus-growth null. It checks confounding and arithmetic, not external detection quality.
- Exposure: synthetic outputs inspected; real corpus outputs unavailable. Record all future amendments; never relabel inspected output as unseen holdout.

The lexical pattern `\bfuzz(?:ing|er|ers)?\b` is an exploratory proposal. EL-005 establishes pre-cutoff use of “fuzzing”; it does not independently establish every variant or the completeness of this pattern. Historical vocabulary validity remains unresolved.

## Executed experiments and limits

See [provider audit](07_PROVIDER_AUDIT_RESULTS.md), [decision packets](08_D07_D08_EXIT_PACKET.md) and shared [experiment artifacts](../../../experiments/research_exit_20260927/README.md).

- Initial arXiv count request: HTTP 406; zero successful record responses. AM-01 content-negotiation diagnostic: HTTP 406 again. The web tool also could not access the count URL.
- DBLP historical archive HEAD probe: connection reset; no archive downloaded. This is an environment-specific access observation, not evidence that DBLP lacks snapshots.
- **15 synthetic test methods passed in each of two separate processes**, including seven hand-calculated series scenarios; output hashes match. No real-corpus signal comparison, annotation, sample missingness estimate or holdout evaluation ran.
- Actual numeric examples: `10/100 = 20/200 = 0.1`; with the numerator fixed, `10/100 = 0.1` but `10/200 = 0.05`. Empty denominator and missing bins produce null, not zero.

The shared outputs retain expected/actual values and input hashes. Synthetic availability fields are stipulated. They do not establish E3, production correctness, independent reviewer replay or user value.
