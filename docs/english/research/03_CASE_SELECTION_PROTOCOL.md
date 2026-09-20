# 03 — Case Selection Protocol

**Status:** selection procedure prepared; no concept, corpus, period, reference label or quality threshold has been frozen. Work package A owns R6; B supplies feasibility evidence. See the [backlog](../master/08_MONTH1_BACKLOG.md).

## Eligibility before signal output

Shortlist a historical concept and a control using independent literature/context and source coverage, before inspecting SITES signal output. Record all candidates, reasons for inclusion/exclusion, selector, date, sources inspected and any prior exposure to outputs. Do not select the concept with the most attractive graph.

The historical case must fit the candidate D07 domain, have a completed and identifiable period, enough records under a support criterion proposed from the audit, and independent literature to contextualize activity in that period. Context is not automatically a reference label or ground truth. Domain and minimum support require acceptance at D07/D08; eligibility now is conditional.

The control must test a failure mode: for example, an independently motivated stable-activity concept, or a synthetic null with fixed share while corpus size grows. Record why it is a meaningful comparator and what it cannot validate. A synthetic control can test calculation/confounding but cannot establish real-world detection quality. At least one historical case and one control are required for E2; the actual choice remains open.

## Development, freeze and holdout

1. Log candidate selection rules before inspecting system output. B may inspect coverage and missingness for feasibility without using signal performance to select the case.
2. Propose a development/holdout separation with exact periods or records, permitted uses and access/exposure history. Use development evidence to compare methods; never tune using holdout results. Previously viewed outputs cannot later be presented as unseen holdout.
3. Before holdout, obtain human acceptance of D07/D08 and record a versioned freeze: selected case/control and exclusions, query/corpus/snapshot, period/cutoff, vocabulary/version, unit/denominator, formula/bin/window, minimum support, reference-label method, quality threshold, sensitivity ranges and software/config references when available. Nothing is frozen by this entry document.
4. Specify who creates reference labels, which independent evidence they may see, how disagreements are retained and how uncertainty is represented. Avoid deriving the reference from the signal being assessed. The method and rubric require D08 acceptance; no user study or annotation has occurred yet.
5. Retain failures, counterexamples and disagreement. Sensitivity analysis must use the ranges frozen before holdout and disclose all evaluated variants.

## Changes and temporal limits

Every amendment records date, author, reason, affected decisions and whether outputs or holdout were already inspected. After exposure, label revised analysis exploratory; seek a new accepted protocol and genuinely unexposed holdout before making confirmatory claims. Do not overwrite the original freeze or hide failed runs.

Availability must cover every input field and the vocabulary at cutoff T. Without that evidence, the case is retrospective only; **E3 NOT PASSED** remains in force. A historical story, a control, or an old publication date does not establish temporal isolation.

Deliver a selection log, independent context sources, proposed case/control, freeze proposal, exposure/amendment log and unresolved limitations for D08. Research Entry checks that these rules exist; it does not claim a selected case or successful evaluation.
