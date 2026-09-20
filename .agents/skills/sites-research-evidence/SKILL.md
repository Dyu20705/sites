---
name: sites-research-evidence
description: Evidence-first research workflow for SITES. Use whenever the task involves literature review, prior art, research questions, methodology, novelty or gap claims, scholarly trend indicators, evaluation design, or synthesizing external evidence into a SITES research decision.
---

# SITES Research Evidence

Turn an open research question into a bounded, auditable evidence synthesis. Do not convert plausible explanations into findings.

## Start from the decision

Before searching, identify:

- the research question or claim being evaluated;
- which SITES decision/gate the evidence could unlock;
- the scope: population/domain, time range, evidence type, and exclusions;
- the minimum evidence needed to change the current decision.

If the task is exploratory, state the scope as a working assumption rather than silently fixing it.

## Source strategy

Prefer, in order:

1. original paper / official standard / official dataset or API documentation;
2. reproducible artifact or author-maintained technical material;
3. strong secondary synthesis for discovery or context;
4. informal/community sources only for leads or experience reports.

For every material claim, record enough identity to find the source again: title, authors/organization, year/version, URL/DOI where available, and the exact part supporting the claim.

Search broadly enough to find counterexamples and competing approaches. Do not claim research novelty until prior work has been searched specifically for the proposed contribution and close synonyms.

## Evidence ledger

For each material item, distinguish:

| Field | Meaning |
| --- | --- |
| Claim | What the source supports |
| Evidence type | empirical / theoretical / benchmark / design / opinion |
| Population & period | what was actually studied |
| Directness | direct evidence vs inference |
| Limitations | validity, coverage, confounders, missing information |
| SITES relevance | what decision or hypothesis it informs |
| Status | supports / contradicts / mixed / unresolved |

Do not use historical evidence from another population as if it directly measured the current SITES corpus.

## Synthesis rules

Separate the final synthesis into:

- **Established / well-supported**: convergent evidence within the studied scope.
- **Contested / method-dependent**: evidence changes with definitions, datasets, windows, or metrics.
- **Unknown for SITES**: plausible but not yet tested on the M1 corpus.
- **Research gap**: something prior work does not establish after a targeted search.
- **Proposed contribution**: what SITES may test or implement; never present it as novelty by default.

For causal language, require evidence that supports causality. Otherwise use descriptive language such as association, co-movement, or observed change.

## M1-specific checks

When the topic is trend detection, explicitly test whether the proposed method can distinguish signal from:

- overall corpus growth;
- provider coverage changes;
- terminology/name changes;
- sampling/query effects;
- publication/citation delay;
- temporal leakage.

Favor an interpretable deterministic baseline before a complex metric or LLM-derived score. A second signal is justified only if it contributes information the first signal demonstrably misses.

## Output contract

Return:

1. research question and scope;
2. evidence table/ledger;
3. synthesis with conflicting evidence;
4. implications for the relevant SITES decision;
5. recommendation labeled **PROPOSED**;
6. uncertainties and the smallest next validation.

A literature review or source count alone does not pass a SITES gate. State which empirical artifact is still required.
