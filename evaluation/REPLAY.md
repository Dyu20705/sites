# Offline replay — SITES M1

Accepted scope: `M1-R-20261010-v1`, D09 `D09-M1-20261012-v1`. Only the 598 frozen arXiv works, exact v1 titles and six 2019 UTC bins are admitted. The corpus was observed in 2026. Scientific quality remains NOT MEASURED; original E3 NOT PASSED.

This package uses Windows, preinstalled CPython **3.14.7 x64** and an installed browser. It contains no runtime installer and needs no pip packages, Git, server, API key or live corpus request. A different runtime or machine requires a separate prospective profile/evaluation record; never replace F1's historical author profile to make a replay pass.

Verify the ZIP's SHA-256 against the external delivery report before extracting it to a **new directory**. `package-index.json` inventories the packaged bytes; `evaluation/expected-sha256.json` supplies command arguments within the externally verified ZIP. These files are integrity references, not digital signatures or evidence that a reviewer performed a task. From a source checkout, use the corresponding external evaluation digest in the delivery report.

Open PowerShell in the extracted package root. These commands use only preinstalled Python and its standard library:

```powershell
python -c "import sys; assert sys.version_info[:3] == (3,14,7) and sys.maxsize > 2**32"
python -m venv --without-pip .venv
$DemoPython = '.\.venv\Scripts\python.exe'
$Anchor = Get-Content -Raw -LiteralPath evaluation/expected-sha256.json | ConvertFrom-Json
$F1 = 'experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json'
$ArgsCommon = @('--f1', $F1, '--expected-f1-sha', $Anchor.freeze_sha256,
  '--evaluation', $Anchor.evaluation_path, '--expected-evaluation-sha', $Anchor.evaluation_sha256)
& $DemoPython -B -m sites_demo verify @ArgsCommon
& $DemoPython -B -m unittest discover -s tests -p test_*.py -v
& $DemoPython -B -m sites_demo build @ArgsCommon --out build/reviewer-1
& $DemoPython -B -m sites_demo build @ArgsCommon --out build/reviewer-2
& $DemoPython -B -m sites_demo compare build/reviewer-1/semantic-index.json build/reviewer-2/semantic-index.json
Invoke-Item build/reviewer-1/index.html
```

Check **each exit code** (`$LASTEXITCODE`) and stop on failure. `verify` must report 122 artifacts / 598 works / 21 windows. Both builds and comparison must report PASS. Reusing an output directory exits 2 and preserves it; use another new directory for a new attempt. Failed runs have no `COMPLETE` marker. Do not edit code or frozen inputs to resolve a failure. Record the command, error and profile difference under #73.

`build` is the single end-to-end demo command; `verify`, tests and the second run provide additional verification. It verifies the prospective evaluation/profile, all F1 hashes, raw lineage and research oracles; computes all queries/sensitivities; creates 621 HTML pages (home + 21 windows + 598 evidence + sensitivities); validates local links; measures native process peaks; then writes `semantic-index.json`, `execution.json` and `COMPLETE`. Open the output only when its execution says PASS.

The build worker cannot create sockets, resolve DNS or connect to a server. Python's local `gethostname` metadata call is permitted. Pages use ordinary relative links and local CSS/SVG/raw evidence; no JavaScript, remote assets or API. The reviewer should record whether the machine was disconnected during the walkthrough. No network configuration changes are required by the software.

The 60-second boundary starts before the fresh worker interpreter starts and ends after verification, all computation/rendering, navigation validation and artifact/index writes. Native Windows `PeakWorkingSetSize` is read separately for worker and launcher. The budget is **max(each process peak) ≤256 MiB**; their peak sum is also reported, without claiming simultaneous aggregate peak. Browser use is outside that process budget and must be recorded separately. Runtime identity hashing is inside the measured replay. Metadata/completion-marker serialization is outside the computational boundary. No scalability claim follows from this one 598-work run.

Comparison checks both completion markers, execution success/budgets, full artifact sets/hashes, F1/product/schema identities and the semantic root. Execution timestamps, paths, resource values and reviewer profiles remain separate evidence and may differ. A comparison PASS is not an independent human result.

Candidate profiles can be inspected without accepting them:

```powershell
& $DemoPython -B -m sites_demo runtime --reviewer 'your identity' --role 'reviewer' --exposure 'describe prior exposure' --out evaluation/runtime-candidate-new.json
```

Do not overwrite the prospective profile/evaluation. New profiles need separately anchored evaluation records before formal runs. See [reviewer task](reviewer-task.md) for the human portion; the agent must not fill its answers on the reviewer's behalf.
