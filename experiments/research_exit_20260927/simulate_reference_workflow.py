"""Offline synthetic annotation workflow; never labels SITES corpus works."""

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path


LABELS = {"POSITIVE", "NEGATIVE", "UNCERTAIN"}


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n"


def validate_judgment(judgment, role):
    if judgment["role"] != role or judgment["mode"] != "SIMULATED":
        raise ValueError("Only explicitly simulated roles are permitted")
    if judgment["label"] not in LABELS or not judgment["rationale"].strip():
        raise ValueError("A valid label and rationale are required")
    if judgment["label"] != "UNCERTAIN" and not judgment["evidence_refs"]:
        raise ValueError("Positive/negative requires evidence; missing is uncertain")
    if any(not ref.startswith("synthetic://") for ref in judgment["evidence_refs"]):
        raise ValueError("Real scholarly evidence is outside this simulation")


def reconcile(records):
    """Retain raw A/B judgments; C resolves only disagreements, including uncertainty."""
    if len({r["work_id"] for r in records}) != len(records):
        raise ValueError("Duplicate synthetic work")
    results = []
    agreements = 0
    for record in records:
        if not record["synthetic"] or not record["work_id"].startswith("SYN-"):
            raise ValueError("Fictional IDs only")
        a, b, c = (record[key] for key in ("a", "b", "c"))
        validate_judgment(a, "SIMULATED_A")
        validate_judgment(b, "SIMULATED_B")
        agreement = a["label"] == b["label"]
        if agreement:
            if c is not None:
                raise ValueError("No adjudication on an agreement")
            agreements += 1
            final = a["label"]
        else:
            if c is None:
                raise ValueError("Unresolved disagreement must remain pending")
            validate_judgment(c, "SIMULATED_C")
            final = c["label"]
        results.append({"work_id": record["work_id"], "agreement": agreement,
                        "raw_judgments": deepcopy({"a": a, "b": b}),
                        "adjudication": deepcopy(c), "final_label": final})
    return {"mode": "SIMULATED", "status": "WORKFLOW_COMPLETED",
            "independent_scientific_quality": "NOT_MEASURED",
            "real_corpus_works_annotated": 0, "work_count": len(records),
            "raw_judgment_count": len(records) * 2, "agreements": agreements,
            "disagreements": len(records) - agreements,
            "adjudications": sum(r["adjudication"] is not None for r in results),
            "final_label_counts": dict(sorted(Counter(r["final_label"] for r in results).items())),
            "records": results}


def fixture():
    p, n, u = "POSITIVE", "NEGATIVE", "UNCERTAIN"
    cases = [(p, p, None)] * 7 + [(n, n, None)] * 7 + [(u, u, None)] * 4
    cases += [(p, n, p), (p, n, n), (p, n, u), (p, n, u)]
    cases += [(p, u, p), (p, u, u), (p, u, u), (n, u, n), (u, n, u)]
    records = []
    for index, labels in enumerate(cases, 1):
        work_id = f"SYN-{index:03}"
        def judgment(label, role):
            if label is None:
                return None
            return {"mode": "SIMULATED", "role": f"SIMULATED_{role}", "label": label,
                    "evidence_refs": [] if label == u else [f"synthetic://workflow/{work_id}"],
                    "rationale": "Constructed workflow case; ambiguous/missing evidence retained"
                    if label == u else "Constructed workflow case with stipulated sufficient evidence"}
        records.append({"work_id": work_id, "synthetic": True,
                        "a": judgment(labels[0], "A"), "b": judgment(labels[1], "B"),
                        "c": judgment(labels[2], "C")})
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = fixture()
    before = canonical(records)
    result = reconcile(records)
    assert canonical(records) == before
    assert (result["work_count"], result["raw_judgment_count"], result["agreements"],
            result["disagreements"], result["adjudications"]) == (27, 54, 18, 9, 9)
    assert result["final_label_counts"] == {"NEGATIVE": 9, "POSITIVE": 9, "UNCERTAIN": 9}
    result["fixture_sha256"] = hashlib.sha256(before.encode()).hexdigest()
    result["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["claim_boundary"] = "Synthetic workflow checks only; no human or real-paper judgments"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write(canonical(result))
    print(canonical({key: value for key, value in result.items() if key != "records"}))


if __name__ == "__main__":
    main()
