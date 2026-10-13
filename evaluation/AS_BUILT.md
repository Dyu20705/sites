# M1 offline slice — as built

Research dependency: exact `0673903c7cf8e4c6725af8a13f2ca4e40a1457a9`, supplied by Draft PR #75. Implementation branch `codex/m1-offline-slice` is stacked against `research/exit-evidence-20260927`; master does not implicitly supply these files. No merge or release is part of this work package.

D09 was accepted by the owner on 12 October 2026: [record](https://github.com/Dyu20705/sites/issues/71#issuecomment-6123995295), [exact proposal](D09-M1-20261012-v1.md), [machine-readable transcription](owner-acceptance.json). The proposal's historical PROPOSED text remains byte-identical; its acceptance is external.

| Component | Implemented responsibility |
| --- | --- |
| `sites_demo/contracts.py` | Exact anchors/schemas, canonical JSON, rational shares, strict local paths, exclusive publication |
| `sites_demo/pipeline.py` | All 122 F1 hashes before research import; strict current category; 598-work raw entry/field/identity/acquisition projection; frozen evaluator/oracle comparison; six sensitivities; pure 21-window query |
| `sites_demo/render.py` | Local HTML/SVG/CSS, monthly/pooled support, full denominator/numerator navigation, raw excerpts and separate v1/current evidence, explicit temporal/claim limits |
| `sites_demo/__main__.py` | Prospective runtime/evaluation verification, fresh-process measured build, complete artifact/link verification and comparison, allowlisted offline ZIP |
| `tests/test_demo.py` | Regression and boundary fixtures plus two complete offline builds, resource/native checks and navigation |

No runtime dependencies outside CPython's standard library. No DB, web server, API client invocation, browser JavaScript, new corpus/vocabulary/metric or scientific labels. The old acquisition module supplies its frozen Atom parser only; neither its CLI nor network functions are called. Its import closure is verified, loaded from source (not unverified bytecode), and a worker audit hook rejects socket/DNS/connection operations.

Logical records follow D09 v1. Work/source/evidence fields are checked at projection; query/window records retain exact rational pairs and sorted work IDs. Historical floating-point outputs remain unchanged and are used as oracles. Product interpretation does not convert null to zero. Controlled unknown-title and unassigned-event cases exercise abstention/bounds; the closed F1 corpus itself has valid required fields.

`COMPLETE` binds the output index and execution record. Semantic artifacts contain no runtime path, clock or reviewer identity; product commit/code digest and F1 identity live in the index. Process/profile/execution records remain outside the semantic digest. Publication refuses any existing destination; an interrupted run remains incomplete and must be retried in a new directory. This is not a crash-durability/atomic-directory or adversarial filesystem transaction guarantee.

Only known verified raw Atom feeds are parsed. All provider text is escaped; page paths come from validated IDs/months, never provider URLs. Displayed raw entry text is a reserialized subtree; raw-byte identity is the hash of the whole original file. Generated link validation covers every page and relative target; actual human browser/usability evidence belongs to #73.

Formal author and reviewer evaluation manifests are separate and prospectively anchored after the code commit, before measured runs. The product commit is the commit containing these source bytes; later evidence/documentation commits need not alter it. Tests use a clearly marked synthetic evaluation identity, not a formal author/reviewer record. F1 historical author runtime is never rewritten.

Open gate: independent human replay, five interpretation answers, match/nonmatch navigation and recorded browser task under #73. Scientific quality remains NOT MEASURED and original E3 NOT PASSED. The deadline is 15 October 2026; no features are added while waiting for that task.
