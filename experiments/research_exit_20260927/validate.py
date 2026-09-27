"""Offline artifact integrity/link checks; not a research-validity test."""
import ast
import hashlib
import json
import platform
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
paths = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=REPO, text=True).splitlines()
markdown = sorted(p for p in set(paths) if p.endswith(".md"))
broken = []
links = 0
for relative in markdown:
    path = REPO / relative
    content = path.read_text(encoding="utf-8-sig")
    for destination in re.findall(r"\]\(([^)]+)\)", content):
        target = destination.strip("<>").split("#", 1)[0]
        if not target or re.match(r"[a-z]+:", target) or target.startswith("/"):
            continue
        links += 1
        if not (path.parent / unquote(target)).exists():
            broken.append({"file": relative, "target": target})

parsed_json = []
for path in sorted(HERE.rglob("*.json")):
    if path.name == "validation.json":
        continue
    json.loads(path.read_text(encoding="utf-8"))
    parsed_json.append(str(path.relative_to(REPO)).replace("\\", "/"))
for path in HERE.glob("*.py"):
    ast.parse(path.read_text(encoding="utf-8"))

pairs = []
for name in ("06_RESEARCH_EXIT_EVIDENCE.md", "07_PROVIDER_AUDIT_RESULTS.md", "08_D07_D08_EXIT_PACKET.md"):
    en = (REPO / "docs/english/research" / name).read_text(encoding="utf-8")
    vi = (REPO / "docs/vietnamese/research" / name).read_text(encoding="utf-8")
    same = set(re.findall(r"EL-\d+", en)) == set(re.findall(r"EL-\d+", vi))
    pairs.append({"name": name, "evidence_ids_match": same})

one = (HERE / "results/run-1.json").read_bytes()
two = (HERE / "results/run-2.json").read_bytes()
report = json.loads(one)
stale_hashes = [name for name, digest in report["inputs"].items()
                if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != digest]
statuses = {}
for lang in ("english", "vietnamese"):
    decision = (REPO / "docs" / lang / "master/07_DECISION_LOG.md").read_text(encoding="utf-8")
    for number in range(5, 10):
        section = re.search(rf"^## \d+\. D0{number} .*?(?=^## |\Z)", decision, re.M | re.S).group()
        status = re.search(r"\*\*(?:Status|Trạng thái):\*\* (\w+)", section).group(1)
        statuses[f"{lang}/D0{number}"] = status
expected = {f"{lang}/D0{n}": "ACCEPTED" if n < 7 else "PROPOSED"
            for lang in ("english", "vietnamese") for n in range(5, 10)}
result = {"python": platform.python_version(), "platform": platform.platform(),
          "markdown_files_checked": len(markdown), "relative_links_checked": links,
          "broken_relative_links": broken, "json_files_parsed": parsed_json,
          "paired_evidence_ids": pairs, "decision_statuses": statuses,
          "replay_equal": one == two, "replay_sha256": hashlib.sha256(one).hexdigest(),
          "stale_input_hashes": stale_hashes,
          "scope": "Relative target existence, JSON/Python parsing, evidence-ID pairing, decision statuses and offline replay integrity. External links/anchors and translation semantics are not automatically validated."}
(HERE / "results/validation.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, indent=2))
if broken or stale_hashes or one != two or statuses != expected or not all(p["evidence_ids_match"] for p in pairs):
    sys.exit(1)
