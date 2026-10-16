# F1 acceptance and Research Exit verification

Source: `97bf499718c13166667a8e5da09b201065d9e117`. [Owner approval](https://github.com/Dyu20705/sites/issues/70#issuecomment-6119490874) accepts the exact unchanged packet `M1-R-20261010-v1`; [English handoff](../../../../docs/english/research/17_RESEARCH_EXIT_20261012.md) and [Vietnamese handoff](../../../../docs/vietnamese/research/17_RESEARCH_EXIT_20261012.md) explain the gate allocation and limitations. The delivery commit is recorded externally in #70.

`freeze-v1.json` / `F1-M1-R-20261012-v1` SHA-256:

```text
bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a
```

Compare this digest with #70 before trusting the local receipt. All 122 referenced artifacts match exact bytes; pre-existing artifacts also match pinned source Git blobs. The manifest pins the author Python runtime inventory and all exposed work/version IDs. An expected digest stored only alongside editable artifacts cannot authenticate them; the external owner/commit record is the trust anchor. No digital signature or hermetic OS image is claimed.

Run from the repository root using the recorded Python 3.14.7 environment (PowerShell):

```powershell
python experiments/research_exit_20260927/verify_freeze.py --manifest experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json --expected-sha256 bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a --root (Get-Location).Path --repo (Get-Location).Path
python -m unittest discover -s experiments/research_exit_20260927 -p 'test_*.py' -v
python experiments/research_exit_20260927/runs/20261012-research-exit-01/validate_accepted_state.py --output "$env:TEMP/sites-accepted-state-new.json"
```

Use a fresh output path for the last command. The integrity verifier only reads and writes its JSON result to stdout, exiting 1 on any mismatch. A different runtime fails the exact author inventory; record a separately versioned prospective reviewer runtime before new product evaluation. Do not change F1 to make a different environment pass.

`execution.json` records four fresh checks, including all **56 unit tests**, raw XML/token recount and a second verification in a new copied artifact tree. The clean run uses a separate process on the same machine and reads source Git objects from the original checkout; it is not a reviewer or independent machine result. `baseline-regressions.json` records 13 earlier commands and 13 byte-identical replay outputs at the pre-acceptance document state, including the two historical validators. Their expected D07/D08 PROPOSED assertions remain historical. `accepted-state-validation.json` replaces only that status check for the new canonical state and also checks links, metrics, lineage and preserved artifacts.

Research verification checks passed. A precommit whitespace check reported ten trailing spaces in new canonical authority paragraphs; these were removed and the check rerun. The historical overwrite-refusal check deliberately returns 2; that is a passed rejection test. Expected integrity attacks in six new regressions are also passed rejection tests. Git LF/CRLF notices concern documentation checkout policy, not changed frozen experiment bytes.

F1 is prospective replay/task discipline for already exposed development evidence. Historical E3 remains NOT PASSED; scientific quality NOT MEASURED; reviewer tasks, integrated demo and measured E8 remain pending. No live acquisition, new holdout access or product build occurs. `create_freeze.py` is the preserved one-shot assembler and refuses an existing freeze; do not rerun it to replace this version. `run_verification.py` is the recorded one-shot audit harness and likewise preserves its outputs.
