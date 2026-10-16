"""Shared, fail-closed file and value contracts; no network or optional packages."""
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = "experiments/research_exit_20260927"
DATA = RESEARCH + "/runs/20261010-development-01"
F1_PATH = RESEARCH + "/runs/20261012-research-exit-01/freeze-v1.json"
# Keep the externally accepted anchor literal, independent of input manifests.
F1_SHA = "bba628101ca0e2e0689c41dc364cbcbc4457dd90f187865373edc49b0a9d289a"
D09_SHA = "a6c84f4b54523acd7f6121408c4889978003b9afc6c94dd4069fbd71b572cfbc"
MONTHS = tuple(f"2019-{month:02d}" for month in range(1, 7))
RULE = "RE-20260927-01-documented-word-boundary-v1"
SCOPE = "OBSERVED_RETROSPECTIVE_LEXICAL_PREVALENCE"
SCHEMAS = {name: 1 for name in ("ArtifactRef", "SourceRef", "Work", "SignalPoint", "EvidenceBundle", "QueryResult", "SemanticIndex", "ExecutionRecord")}
QUESTION_IDS = ["count_share", "denominator", "evidence", "temporal", "claim_limits"]
WORK_RE = re.compile(r"[0-9]{4}\.[0-9]{4,5}\Z")
SHA_RE = re.compile(r"[0-9a-f]{64}\Z")


class DemoError(ValueError):
    def __init__(self, code, detail):
        self.code = code
        super().__init__(f"{code}: {detail}")


def require(condition, code, detail):
    if not condition:
        raise DemoError(code, detail)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                       allow_nan=False) + "\n").encode("utf-8")


def read_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "INVALID_JSON", f"duplicate key: {key}")
            result[key] = value
        return result

    def nonfinite(value):
        raise DemoError("INVALID_JSON", f"non-finite value: {value}")

    def finite_float(value):
        number = float(value)
        require(math.isfinite(number), "INVALID_JSON", "non-finite number")
        return number

    try:
        return json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite, parse_float=finite_float)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise DemoError("INVALID_JSON", str(error)) from error


def local_path(root, name):
    """Reject traversal, Windows aliases/ADS, URL syntax and redirected paths."""
    require(isinstance(name, str) and bool(name), "UNSAFE_PATH", "empty/non-string path")
    parts = name.split("/")
    require(not any(c in name for c in "\\:%?#\x00"), "UNSAFE_PATH", name)
    require(not PurePosixPath(name).is_absolute() and all(p not in {"", ".", ".."} for p in parts),
            "UNSAFE_PATH", name)
    require(all(not p.endswith((" ", ".")) and not re.fullmatch(
        r"(?i)(CON|PRN|AUX|NUL|COM[0-9]|LPT[0-9])(?:\..*)?", p) for p in parts),
        "UNSAFE_PATH", name)
    root = Path(root).absolute()
    require(not any(p.is_symlink() or p.is_junction() for p in (root, *root.parents)), "UNSAFE_PATH", str(root))
    path = root
    for part in parts:
        path = path / part
        require(not path.is_symlink() and not path.is_junction(), "UNSAFE_PATH", name)
    require(path.resolve().is_relative_to(root.resolve()), "UNSAFE_PATH", name)
    return path


def write_new(root, name, raw):
    path = local_path(root, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)


def create_output(path):
    path = Path(path).absolute()
    require(not path.exists() and not path.is_symlink(), "OUTPUT_EXISTS", str(path))
    for parent in (path, *path.parents):
        require(not parent.is_symlink() and not parent.is_junction(), "UNSAFE_PATH", str(parent))
    path.mkdir(parents=True, exist_ok=False)
    return path


def artifact(name, raw, origin="product"):
    return {"path": name, "sha256": sha(raw), "size_bytes": len(raw), "origin": origin}


def integer(value, minimum=0):
    return type(value) is int and value >= minimum


def utc(value):
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return None
        return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    except ValueError:
        return None


def rational(n, total):
    if n is None or total is None or total == 0:
        return None
    require(integer(n) and integer(total, 1) and n <= total, "INVALID_SIGNAL", "invalid n/N")
    return {"numerator": n, "denominator": total}


def percent(value):
    if value is None:
        return "UNKNOWN / undefined"
    number = Decimal(value["numerator"]) * 100 / Decimal(value["denominator"])
    return str(number.quantize(Decimal("0.0001"), rounding=ROUND_HALF_EVEN)) + "%"
