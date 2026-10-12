# PR #75 final remediation — 12 October 2026

Baseline: clean `research/exit-evidence-20260927@0eea1360a100d21a190034cadf2c9f21a1f2a4bc`, matching fetched origin; PR #75 OPEN/Draft. Master remains `0a853636ef6d1be9d3bb85058f34faf368fcb6ce`; main checkout remains clean `dev@0e457fd146c1fe0d67b60f92ebe5d989be4c2b67`. No newer exact owner acceptance was found. This bounded correction changes report publication and verification tooling plus tracker accuracy. It does not change the research contract. Deadline: **15 October 2026**, Asia/Bangkok; risk remains HIGH.

## Corrections and validation

- **Publication:** [v2 CLI](../../checks_cli_v2.py) links the completed, closed private report on the destination filesystem into the requested name. The link cannot replace a concurrent winner. Unsupported linking fails explicitly; temporary files are removed on normal error/success exits. No fsync/crash-persistence claim. This uses the existing stdlib [Python hard-link API](https://docs.python.org/3.14/library/os.html#os.link); [Windows documentation](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-createhardlinkw) describes same-volume hard links. No new dependency. The historical checker stays unchanged and remains unsafe when invoked directly on an existing output.
- **Reproducible bytes:** [new CLI](../../verify_git_bytes.py) accepts an explicit revision and literal paths, reads Git blobs, reports SHA-256 and exact/explicit-documentation-EOL/mismatch states, and returns nonzero for unexpected mismatches. It never normalizes experiment artifacts or writes verified files. [18 historical blob digests](historical-git-blobs.json) reproduce the older manifest. [Actual documentation comparison](documentation-eol-explicit-root.json) reproduces its sole CRLF/LF exception, retaining both hashes. [112 frozen files](frozen-byte-verification.json) match exact baseline bytes.
- **Tracker:** one body update and fresh readback per [#64](https://github.com/Dyu20705/sites/issues/64), [#66](https://github.com/Dyu20705/sites/issues/66), [#69](https://github.com/Dyu20705/sites/issues/69). [Before/after audit](governance-corrections.json) preserves original bodies, dates, changes and owner records. #66 is **0/7 independently demo-complete**, with the two available research artifacts documented separately. #64 is 18/22 investigation boxes checked: three unsupported completion indicators reverted; search provenance already unchecked. Two ambiguous testing/reference clauses remain explicitly flagged, not redefined. #69 is 12/13 after unchecking exact search provenance. No issue closed or gate accepted.
- **Executed suites:** Windows 11 build 26200 / Python 3.14.7: **50/50 tests**. Ubuntu WSL2 Linux 6.6.87.2 / Python 3.12.3 / Git 2.43.0, native `/tmp`: **50/50 tests**. Includes six publication and seven verifier tests; two child processes wait with complete reports before racing to publish, yielding exactly one success and one refusal. Existing replay harness: 13 commands, two 15-test legacy runs, paired corpus/signal/SYN replays, ten controls per signal replay, and **13/13 byte comparisons**. Fresh [raw recount](independent-verification.json) uses no project parser/evaluator imports. These are same-host checks, including WSL, not independent clean-machine or human verification.

[Execution record](execution.json) contains exact argv, environment, exits, output references and hashes. First restricted-sandbox publication run: six tests, two failures because Windows denied `os.link` (WinError 5); unchanged code passed outside the sandbox. A later `--compare-root .` resolved incorrectly inside that sandbox and reported missing documentation; [failed attempt](failed-validation.json) and [failed comparison](documentation-eol-verification.json) are retained. Explicit absolute root passed without modifying code/files. These are resolved environment failures, not scientific failures. Final whitespace, scope and package checks are recorded separately at closeout.

To replay the suite, run from the checkout root on a filesystem supporting hard links (use a fresh writable temporary location if the execution sandbox restricts the OS temporary directory):

```text
python experiments/research_exit_20260927/runs/20261011-final-audit-01/run_checks.py
python experiments/research_exit_20260927/runs/20261011-final-audit-01/independent_verify.py --output <fresh-directory>/independent.json
```

The committed byte verifier's exact scopes/revisions are in `execution.json`. Its reports omit timestamps and absolute comparison paths, making the same inputs deterministic. New validation reports use fresh filenames; historical evidence is preserved. Git verification of the remediation commit is a subsequent report, excluding that report's own future bytes.

## Research integrity and remaining findings

All **598 observed current-query works**, **598 denominator identities** and **nine numerator identities** reconcile. Monthly **N = [91,79,97,103,122,106]**, **n = [0,1,2,1,4,1]**, total **9/598**. Measurement SHA-256 remains `214c103f82784665907f76925ea56763fd2e46644ce52ccf6950b08e807cc818`; normalized corpus remains `a3aff4868b176dcbb30622563d61241c5850eff2b9350d94443af281b2bee6f1`. Original raw/config/evaluator/output bytes are unchanged. No new acquisition, holdout exposure, vocabulary, denominator, formula or threshold.

Historical public membership/availability and cutoff-valid vocabulary are unresolved; no as-of claim. Support is 0–4 matches/month. Real independent annotations: **zero; NOT MEASURED**. SYN-001–027 / SIMULATED_A/B/C are fictional workflow evidence, not human labels. Original **E3 NOT PASSED**.

- **BLOCKER for dependent work:** exact owner amendment/D07/D08/F1 acceptance and G70 disposition absent. #70 remains NOT PASSED; D09 and product work remain gated.
- **MAJOR tracker discrepancy requiring owner reconciliation:** #70 currently has eight checked boxes, including acceptance/freeze, but its latest explicit record still leaves the exact decisions pending. This task documents the discrepancy in #64/#66 and preserves #70 without inventing acceptance or changing owner decisions.
- **MAJOR before broader evaluator reuse:** the existing missing-current-category limitation remains contained by all 598 pinned valid records. The frozen evaluator is unchanged; broader reuse requires its separately gated guard.
- **INFORMATIONAL:** #64's two ambiguous clauses, incomplete historical search metadata and unmeasured independent reference/usability/product evidence remain explicit. Tests do not resolve these scientific or acceptance gaps.

## Owner handoff — unchanged M1-R-20261010-v1

Both packet files are unchanged. Git-blob SHA-256:

- [English packet](../../../../docs/english/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md): `da80e30a4fb07ad7722cf4d845ce0feb7da28a1b84336710697f358cd30b8122`.
- [Vietnamese packet](../../../../docs/vietnamese/research/15_RETROSPECTIVE_SCOPE_AMENDMENT_20261010.md): `164535e1d50fd6f01e26aaadb639d7a89f67dadfc2dd4412b75d93bd05b677b0`.

Each row refers to those exact packet identities and the existing [detailed seven-decision matrix](../../../../docs/english/research/16_CRITICAL_PATH_HANDOFF_20261012.md#2-owner-decision-matrix--unchanged-packet-separate-decisions). Record owner, UTC date, ACCEPT/REJECT/REVISE, row and packet hash externally; approval of one row does not approve another.

| Row / actual state | Recommendation and evidence | Alternative / residual uncertainty | Exact consequence of approval |
| --- | --- | --- | --- |
| A1 — PROPOSED | Accept finite observed-corpus retrospective lexical estimand if it meets owner intent; 598-work audit and historical negative finding support the boundary | Retain broader question/defer; user value and historical population unverified | Amend only the exact M1/D05 estimand/claim clauses; no as-of or product authorization |
| A2 — PROPOSED | Accept explicit E2-R/E3-R scope for that descriptive route; controls/lineage/replay exist | Retain original E2/E3; independent interpretation/product checks absent | Activate named replacement obligations for amended scope; original E3 stays NOT PASSED |
| A3 — PROPOSED | Explicitly choose limited descriptive acceptance with scientific quality NOT MEASURED; zero real judgments is verified | Retain independent-reference requirement and await qualified humans/justified criteria | Change only the explicitly selected scientific-quality acceptance obligation; simulation never satisfies retained human criteria |
| D07 — PROPOSED | Accept exact 598 observed works, frozen query/provenance and v1 UTC event bins; raw identities reconcile | Defer or separately scope historical reconstruction; selection/coverage bias remains | Pin population/time/sharing boundary; no new acquisition or holdout permission |
| D08 — PROPOSED | Accept fixed lexical n/N/share, uncertainty/support/sensitivities and no directional labels; 9/598 reproduced | Count with N disclosed or defer; sparse support/alias bias and helper limit remain | Pin formula/evaluation boundary; no validated detector or UI authorization |
| F1 — PROPOSED | Accept prospective replay/task freeze with exact hashes/exposure/personnel/criteria; existing identities are available | No new evaluation; signed freeze and reviewer resources absent | Require immutable accepted manifest before dependent evaluation; cannot reclassify exposed work as holdout |
| G70 — NOT PASSED | Keep NOT PASSED now; six prerequisite rows lack exact acceptance | Later explicit PASS only with accepted, evidenced criteria | A justified PASS permits #71 design review only, never D09 acceptance or #72/#73 completion |

**Exactly one next task:** owner disposition of the seven rows against the unchanged packet and this audit. Prerequisites: inspect hashes/evidence and resolve the two #64 wording ambiguities plus #70's checkbox contradiction. Done when each row has an explicit authoritative disposition, retained requirements have named evidence/gaps, and G70 accurately records NOT PASSED or a justified PASS. Validate the record against packet identities, the accepted decision log and every retained research criterion. The future sequence remains **#70 → #71 D09 acceptance → #72 vertical slice → #73 independent demo verification**; this execution stops before #71/#72 work.
