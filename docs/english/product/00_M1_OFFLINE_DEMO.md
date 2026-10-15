# M1 Offline Evidence Demo

Vietnamese: [Bản tiếng Việt](../../vietnamese/product/00_M1_OFFLINE_DEMO.md)

**Implementation status — 16 October 2026:** candidate implementation for
[#72](https://github.com/Dyu20705/sites/issues/72). It implements the exact
[D09-M1-20261012-v1 proposal](https://github.com/Dyu20705/sites/issues/71#issuecomment-6123770080),
accepted by the owner with SHA-256
`a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc`.
This document does not mark FEATURE-READY, E7, E8, or PRODUCT-READY as passed.

## As-built boundary

The demo uses only the CPython standard library, frozen files, in-process
functions, and generated local HTML/SVG. It has no package installation,
database, listener, JavaScript, remote asset, live provider call, model, or
deployment path.

| Module | Public responsibility |
| --- | --- |
| `sites_demo/contracts.py` | Strict JSON/path contracts and immutable records |
| `sites_demo/pipeline.py` | `verify_inputs`, `project`, `measure`, `query`, `evidence`, `build`, and `compare` |
| `sites_demo/render.py` | Escaped static HTML/SVG, 21 window pages, and 598 evidence pages |
| `sites_demo/__main__.py` | `runtime`, `verify`, `build`, and `compare` CLI adapters |

The fixed input is F1-M1-R-20261012-v1,
SHA-256 `bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a`.
Verification fails closed on a manifest/artifact/runtime identity mismatch,
unexpected JSON fields, duplicate keys, a raw Atom index/ID/hash mismatch, an
unknown current category, an invalid query, or an unsafe path. The accepted
primary oracle remains monthly n=`0/1/2/1/4/1`,
N=`91/79/97/103/122/106`, with 9/598 pooled works.

`build` refuses an existing destination. A complete run contains:

- `index.html`, local `style.css`, and `sensitivities.html`;
- 21 `windows/*.html` files and 598 `evidence/*.html` files;
- canonical `data/works.json`, `data/windows.json`, and
  `data/sensitivities.json`;
- byte-identical admitted raw Atom artifacts under `raw/`;
- `semantic-index.json`, a separate `execution.json`, and a final `COMPLETE`
  marker.

Semantic replay excludes clocks and resource observations. `compare` refuses
incomplete runs and compares product/F1 identity, the complete path set,
per-file bytes, and the semantic root digest.

## Bootstrap and replay

No evaluation file is committed as an approval substitute. Before a real
evaluation, prepare and externally anchor an immutable `D09-EVAL-v1` record
containing the exact product commit/code digest, F1 and D09 identities,
reviewer/exposure status, runtime inventory, all eight accepted logical schema
identities, the exact control artifact and six sensitivity names, the five
named interpretation tasks, match/nonmatch navigation, two-build semantic
replay, and limits. The strict reader rejects omitted, extra, placeholder, or
substituted identities.

From the delivered source root, using that record:

~~~text
python -m sites_demo runtime --browser "RECORDED BROWSER VERSION" --out evaluation/runtime-candidate.json
python -m sites_demo verify --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256
python -m unittest discover -s tests -p "test_*.py" -v
python -m sites_demo build --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256 --out output/replay-1
python -m sites_demo build --f1 experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-f1-sha bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --evaluation evaluation/demo-v1.json --expected-evaluation-sha EVALUATION_SHA256 --out output/replay-2
python -m sites_demo compare output/replay-1/semantic-index.json output/replay-2/semantic-index.json
~~~

`runtime` records a candidate only; it does not approve the environment. An
independent record must identify the accepted Windows x64 / CPython 3.14.7
target, detected CPU/RAM inventory, and a non-placeholder browser version. Each
command exit must be checked before continuing. Each CLI `build` starts a fresh
worker process. Its outer monotonic timer includes worker interpreter startup;
on Windows the execution record captures worker and launcher peaks, enforces
their maximum against 256 MiB, and records their sum as context. The launcher
syncs every output file, stages the exact completion marker, writes and syncs
the outer execution record, and checks the budget again before atomically
publishing `COMPLETE`; an over-budget run remains incomplete. Recorded elapsed
time ends after the exact marker bytes and execution metadata are synced. The
later monotonic guard can only fail the run; the final atomic rename publishes
those already-synced bytes and is not treated as replay work.

## Development evidence and remaining gates

On Linux x86_64 with Python 3.12.14, the 14-test product suite passed on 16 October 2026.
They exercised the real 598-work freeze, two byte-identical semantic builds,
all local links, HTML escaping, strict JSON/path failures, invalid null/event
fixtures, ratio-of-sums, output refusal, CLI paths, and a build with socket
connection attempts blocked. This is development evidence, not an independent
Windows/browser review.

The Linux run deliberately records peak process memory as
`NOT_MEASURED_NON_WINDOWS_D09_BOUNDARY`; it cannot pass E8. #73 still requires
an externally anchored product/runtime evaluation record, an identified
independent human completing the five interpretation/navigation tasks on the
accepted Windows/browser target, and measured full-replay time and peak process
memory. Original historical E3 remains NOT PASSED; scientific quality remains
NOT MEASURED.
