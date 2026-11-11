"""Run all nine paper check packages without regenerating stored results."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
PACKAGES = (
    ("r2_ads5_paper_checks", ()),
    ("ads5_paper_checks", ()),
    ("generic_ads5_massless", ()),
    ("central_charge_extremization", ()),
    ("paper_conventions", ()),
    ("composite_vector_correspondence", ()),
    ("gb_ads3_sigma2", ("--norms",)),
    ("gb_ads3_sigma2_fermionic", ()),
    ("gb_ads3_sigma2_fermionic_spectrum", ()),
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true",
                        help="also show the full output of successful packages")
    args = parser.parse_args(argv)
    failed = False
    for package, options in PACKAGES:
        command = [sys.executable, "-B",
                   str(ROOT / "computations" / package / "checks.py"), *options]
        print(f"Running {package}...", file=sys.stderr, flush=True)
        start = time.monotonic()
        # A temporary file bounds memory use even for lengthy diagnostic output.
        with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as output:
            try:
                result = subprocess.run(command, cwd=ROOT, stdout=output,
                                        stderr=subprocess.STDOUT, check=False)
                returncode = result.returncode
            except OSError as exc:
                output.write(f"Could not start this package: {exc}\n")
                returncode = 1
            passed = returncode == 0
            failed |= not passed
            elapsed = time.monotonic() - start
            print(f"{'PASS' if passed else 'FAIL'} {package} ({elapsed:.1f}s)", flush=True)
            if not passed or args.verbose:
                print(f"--- {package}: exit {returncode} ---", file=sys.stderr)
                output.seek(0)
                shutil.copyfileobj(output, sys.stderr)
                sys.stderr.flush()
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
