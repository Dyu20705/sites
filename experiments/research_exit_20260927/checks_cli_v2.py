"""Preserving CLI for frozen checks.py; changes output handling, not calculations."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New report path; existing files are never overwritten")
    args = parser.parse_args(argv)
    if args.output.exists():
        parser.error("Output already exists; choose a new report path")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # The historical checker writes only inside this newly created private directory.
    with tempfile.TemporaryDirectory(prefix="checks-cli-v2-", dir=args.output.parent) as directory:
        temporary = Path(directory) / "report.json"
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("checks.py")),
             "--output", str(temporary)], capture_output=True, text=True)
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        if result.returncode:
            return result.returncode
        try:
            with args.output.open("xb") as output:
                output.write(temporary.read_bytes())
        except FileExistsError:
            parser.error("Output already exists; choose a new report path")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
