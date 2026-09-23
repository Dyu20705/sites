# 04 — Conceptual Architecture

**PROPOSED — D09.** This document divides responsibilities within the M1 slice. It does **not** prescribe microservices, package layout, queues, network topology, or a framework.

The entire flow may run in one program if that is the smallest design that meets the requirements.

~~~text
evidence source
→ acquisition
→ observation storage
→ normalization
→ signal calculation
→ descriptive assessment
→ evidence-bundle creation
→ query
→ presentation
~~~

## Responsibilities by Stage

| Stage | Responsibility | Proposed invariant | Open question |
| --- | --- | --- | --- |
| Evidence source | Supply records or snapshots under stated access conditions | Source data is not a SITES conclusion | Provider, license, snapshot availability |
| Acquisition | Convert a query or export into a corpus and acquisition metadata | Report truncation, missing pages, and errors; never imply completeness without evidence | API or export, retries, format |
| Observation storage | Preserve each record as supplied, with provenance and version information | Downstream processing must not silently overwrite what the source reported | Storage, snapshot identity, retention |
| Normalization | Produce the minimum required fields and report invalid, missing, or duplicate data | Unknown is not zero; excluded records need a reason | Time fields, alias rules, duplicate semantics |
| Signal calculation | Map corpus + definition/configuration/cutoff to a value | The same input and configuration must yield the same semantic result | Formula, window, denominator |
| Descriptive assessment | Map signal + rule to a label or insufficient evidence | Every label needs a reason, scope, and limitation | Labels, thresholds, minimum support |
| Evidence bundle | Package assessment and lineage into an inspectable artifact | Include input, definition, configuration, code version, and output | Serialization, hashing, canonicalization |
| Query | Read results by concept and window | Never return a score detached from its evidence | In-process or API |
| Presentation | Show a table or chart with evidence drill-down | Display corpus, cutoff, units, missingness, and limitations | Dashboard stack, local or hosted |

## Errors and Missing Data

- incomplete acquisition → publish a coverage and quality report;
- missing required time field → do not silently insert a fabricated value;
- signal prerequisites not met → return **insufficient evidence**, not declining;
- replay of the same snapshot → counts must not rise because of duplicate ingestion;
- upstream data changed → treat it as a new observation, not a replay of the same input.

## Open Architecture Decisions

Only the Research Gate or Preimplementation Gate may settle:

- data source;
- one source or multiple sources;
- storage or database;
- framework;
- query interface;
- dashboard;
- deployment;
- identity strategy;
- serialization.

M0 does not design distribution, a plugin registry, a service mesh, or a complete schema. Add a physical boundary only when a measured workload or failure case requires it.
