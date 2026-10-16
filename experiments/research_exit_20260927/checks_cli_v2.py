"""Preserving CLI for frozen checks.py; changes output handling, not calculations."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New report path; existing files are never overwritten")
    args = parser.parse_args(argv)
    if os.path.lexists(args.output):
        parser.error("Output already exists; choose a new report path")
    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        # Keep preparation on the destination filesystem, invisible at the final path.
        with tempfile.TemporaryDirectory(prefix="checks-cli-v2-", dir=args.output.parent) as directory:
            temporary = Path(directory) / "report.json"
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("checks.py")),
                 "--output", str(temporary)], capture_output=True, text=True)
            sys.stdout.write(result.stdout)
            sys.stderr.write(result.stderr)
            if result.returncode:
                return result.returncode
            # Successful checker exit follows write_text's flush/close. Linking those
            # complete bytes is atomic and cannot clobber a concurrent destination.
            # No fsync/directory-fsync durability guarantee or copy/replace fallback.
            try:
                os.link(temporary, args.output)
            except FileExistsError:
                parser.error("Output already exists; choose a new report path")
            except OSError as error:
                parser.exit(1, f"Atomic no-clobber publication failed (hard links required): {error}\n")
    except OSError as error:
        parser.exit(1, f"Report preparation or temporary cleanup failed: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
