$ZipPath = 'C:\Users\Admin\sites\.worktrees\research-exit\dist\sites-m1-reviewer-v1.zip'
$ReviewRoot = Join-Path 'C:\Users\Admin\sites\build' ('reviewer-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
$ExpectedZipHash = '1f827f60ee8066c1a2d20f0890954a578d09425314f629eea8e004684d76270b'

$ActualZipHash = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256 -ErrorAction Stop).Hash
if ($ActualZipHash -ne $ExpectedZipHash) {
    throw 'ZIP không khớp hash. Dừng review.'
}
if (Test-Path -LiteralPath $ReviewRoot) {
    throw 'Thư mục review đã tồn tại. Chọn một tên mới.'
}

Expand-Archive -LiteralPath $ZipPath -DestinationPath $ReviewRoot -ErrorAction Stop
Set-Location -LiteralPath $ReviewRoot -ErrorAction Stop
Start-Transcript -Path (Join-Path $ReviewRoot 'reviewer-session.txt')

function Assert-DemoSuccess {
    if ($LASTEXITCODE -ne 0) {
        throw "Lệnh vừa chạy thất bại, exit code = $LASTEXITCODE. Dừng và giữ log."
    }
}

$BasePython = 'C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe'

& $BasePython -c "import sys; print(sys.version); assert sys.version_info[:3] == (3,14,7) and sys.maxsize > 2**32"
Assert-DemoSuccess

& $BasePython -m venv --without-pip .venv
Assert-DemoSuccess

$DemoPython = Join-Path $ReviewRoot '.venv\Scripts\python.exe'

$Anchor = Get-Content -Raw -LiteralPath evaluation/expected-sha256.json | ConvertFrom-Json

$F1 = 'experiments/research_exit_20260927/runs/20261012-research-exit-01/freeze-v1.json'

$ArgsCommon = @(
    '--f1', $F1,
    '--expected-f1-sha', $Anchor.freeze_sha256,
    '--evaluation', $Anchor.evaluation_path,
    '--expected-evaluation-sha', $Anchor.evaluation_sha256
)

& $DemoPython -B -m sites_demo verify @ArgsCommon |
    Tee-Object -FilePath verify-result.json
Assert-DemoSuccess

& $DemoPython -B -m unittest discover -s tests -p test_*.py -v
Assert-DemoSuccess

& $DemoPython -B -m sites_demo build @ArgsCommon --out build/reviewer-1
Assert-DemoSuccess

& $DemoPython -B -m sites_demo build @ArgsCommon --out build/reviewer-2
Assert-DemoSuccess

& $DemoPython -B -m sites_demo compare `
    build/reviewer-1/semantic-index.json `
    build/reviewer-2/semantic-index.json |
    Tee-Object -FilePath compare-result.json
Assert-DemoSuccess

foreach ($Run in @('reviewer-1', 'reviewer-2')) {
    $Record = Get-Content -Raw -LiteralPath "build/$Run/execution.json" |
        ConvertFrom-Json

    [pscustomobject]@{
        Run = $Run
        Status = $Record.status
        Seconds = $Record.elapsed_seconds
        PeakMiB = [math]::Round($Record.peak_process_bytes / 1MB, 2)
        LiveRequests = $Record.live_requests
        SemanticHash = $Record.semantic_sha256
    }
}

Invoke-Item build/reviewer-1/index.html

Stop-Transcript