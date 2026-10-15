import argparse
import json
from pathlib import Path
import sys

from .contracts import ContractError, DemoError, canonical_json
from .pipeline import (_build_worker, compare, launch_build, product_identity, project,
                       runtime_identity, verify_inputs)


def parser():
    result = argparse.ArgumentParser(prog="python -m sites_demo")
    commands = result.add_subparsers(dest="command", required=True)
    runtime = commands.add_parser("runtime")
    runtime.add_argument("--out", type=Path, required=True)
    runtime.add_argument("--browser", default="NOT_RECORDED_CANDIDATE")
    for name in ("verify", "build", "_build-worker"):
        command = commands.add_parser(name)
        command.add_argument("--f1", type=Path, required=True)
        command.add_argument("--expected-f1-sha", required=True)
        command.add_argument("--evaluation", type=Path, required=True)
        command.add_argument("--expected-evaluation-sha", required=True)
        if name in {"build", "_build-worker"}:
            command.add_argument("--out", type=Path, required=True)
    comparison = commands.add_parser("compare")
    comparison.add_argument("index_a", type=Path)
    comparison.add_argument("index_b", type=Path)
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "runtime":
            if args.out.exists() or args.out.is_symlink():
                raise DemoError("OUTPUT_EXISTS", f"refusing existing runtime record: {args.out}")
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with args.out.open("xb") as stream:
                stream.write(canonical_json(runtime_identity(args.browser)))
            output = {"status": "CANDIDATE_NOT_APPROVED", "path": str(args.out)}
        elif args.command == "verify":
            root = Path.cwd()
            verified = verify_inputs(root, args.f1, args.expected_f1_sha, args.evaluation,
                                     args.expected_evaluation_sha)
            output = {"status": "PASS", "freeze_id": verified.manifest["freeze_id"],
                      "works": len(project(verified)), "scope": "Integrity and strict projection only"}
        elif args.command == "build":
            execution = launch_build(Path.cwd(), args.f1, args.expected_f1_sha, args.evaluation,
                                     args.expected_evaluation_sha, args.out)
            output = {"status": execution["status"], "semantic_sha256": execution["semantic_sha256"],
                      "elapsed_seconds": execution["elapsed_seconds"], "error_codes": execution["error_codes"]}
        elif args.command == "_build-worker":
            execution = _build_worker(Path.cwd(), args.f1, args.expected_f1_sha, args.evaluation,
                                      args.expected_evaluation_sha, args.out, write_complete=False)
            output = {"status": execution["status"], "semantic_sha256": execution["semantic_sha256"],
                      "elapsed_seconds": execution["elapsed_seconds"], "error_codes": execution["error_codes"]}
        else:
            output = compare(args.index_a, args.index_b)
            if not output["equal"]:
                print(json.dumps(output, ensure_ascii=False, sort_keys=True))
                return 1
        print(json.dumps(output, ensure_ascii=False, sort_keys=True))
        return 0
    except DemoError as error:
        print(json.dumps({"status": "FAIL", "error_code": error.code, "reason": str(error)},
                         ensure_ascii=False, sort_keys=True))
        return 2 if error.code in {"OUTPUT_EXISTS", "INVALID_QUERY"} else 1
    except (ContractError, OSError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"status": "FAIL", "error_code": "CONTRACT", "reason": str(error)},
                         ensure_ascii=False, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
