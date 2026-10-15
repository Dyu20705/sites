from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
from typing import Any


class ContractError(ValueError):
    pass


class DemoError(RuntimeError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(f"{code}: {message}")


def _reject_constant(value: str):
    raise ContractError(f"non-finite JSON number: {value}")


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json_strict(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_object,
                          parse_constant=_reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ContractError(f"invalid JSON: {path}") from error


def canonical_json(value: Any) -> bytes:
    try:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                          allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ContractError(f"non-canonical JSON value: {error}") from error
    return (text + "\n").encode("utf-8")


def validate_local_path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "//" in value:
        raise ContractError("local path must be a non-empty canonical POSIX path")
    path = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if path.is_absolute() or windows.is_absolute() or windows.drive or "://" in value:
        raise ContractError("absolute, drive, or URL paths are forbidden")
    if any(part in {"", ".", ".."} for part in path.parts) or path.as_posix() != value:
        raise ContractError("local path escapes or is not canonical")
    return value


def require_exact_keys(value: Any, expected: set[str], label: str):
    if not isinstance(value, dict) or set(value) != expected:
        actual = sorted(value) if isinstance(value, dict) else type(value).__name__
        raise ContractError(f"{label} keys differ: {actual}")


def require_sha(value: Any, label: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ContractError(f"{label} must be lowercase SHA-256")
    return value


@dataclass(frozen=True)
class ArtifactRef:
    path: str
    sha256: str
    size_bytes: int
    origin: str


@dataclass(frozen=True)
class SourceRef:
    role: str
    artifact: ArtifactRef
    entry_index: int
    entry_id: str
    acquired_at: str

    def logical_dict(self):
        return asdict(self)

    def evaluator_dict(self):
        return {"file": self.artifact.path.split("/runs/20261010-development-01/", 1)[-1],
                "sha256": self.artifact.sha256, "entry_index": self.entry_index,
                "entry_id": self.entry_id}


@dataclass(frozen=True)
class Work:
    work_id: str
    version_id: str
    current_version: int
    title_v1: str | None
    title_current: str | None
    categories_v1: tuple[str, ...]
    categories_current: tuple[str, ...]
    submitted_v1_at: str | None
    updated_current_at: str | None
    available_at: None
    event_month: str | None
    title_status: str
    event_status: str
    category_status: str
    v1_ref: SourceRef
    current_ref: SourceRef

    def logical_dict(self):
        result = asdict(self)
        result["categories_v1"] = list(self.categories_v1)
        result["categories_current"] = list(self.categories_current)
        return result


@dataclass(frozen=True)
class SignalPoint:
    rule_id: str
    months: tuple[str, ...]
    n: int | None
    N: int | None
    known_matches: int
    share: dict[str, int] | None
    lower_share: dict[str, int] | None
    upper_share: dict[str, int] | None
    status: str
    denominator_ids: tuple[str, ...]
    matched_ids: tuple[str, ...]
    unknown_title_ids: tuple[str, ...]
    unassigned_work_ids: tuple[str, ...]

    def logical_dict(self):
        result = asdict(self)
        for name in ("months", "denominator_ids", "matched_ids", "unknown_title_ids", "unassigned_work_ids"):
            result[name] = list(result[name])
        return result


@dataclass(frozen=True)
class VerifiedInputs:
    root: Path
    manifest_path: Path
    manifest: dict
    evaluation: dict
    evaluation_sha256: str
    normalized_records: tuple[dict, ...]
    projected_works: tuple[Work, ...]
    raw_entry_text: dict[tuple[str, int], str]
    raw_artifacts: dict[str, bytes]
