"""Run the paper checks; --all also runs component, replay and regression checks.

Stored scientific outputs are read only. Figures and LOG replay products are
written outside the repository. Every child failure contributes to the exit code.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
PACKAGES = (
    ("r2_ads5_paper_checks", ()), ("ads5_paper_checks", ()),
    ("generic_ads5_massless", ()), ("central_charge_extremization", ()),
    ("paper_conventions", ()), ("composite_vector_correspondence", ()),
    ("gb_ads3_sigma2", ("--norms",)), ("gb_ads3_sigma2_fermionic", ()),
    ("gb_ads3_sigma2_fermionic_spectrum", ()),
)


def tasks(extended, figure_dir, workspace):
    tasks = [(name, ROOT, [str(ROOT / "computations" / name / "checks.py"), *options])
             for name, options in PACKAGES]
    for name in ("exceptional_points", "tower_norm_rule", "first_order_vs_PRL"):
        tasks.append((name, ROOT, [str(ROOT / "computations/paper_extra_checks" / (name + ".py"))]))
    for name in ("make_l0_family", "fig_towers"):
        options = ["--recompute"] if extended and name == "fig_towers" else []
        tasks.append((name, ROOT, [str(ROOT / "figures" / (name + ".py")),
                                  "--output-dir", str(figure_dir), *options]))
    if extended:
        for name, script in (
            ("repository_integrity", "tools/validate_repository.py"),
            ("auxiliary_identities", "tools/check_symbolic_identities.py"),
            ("computation_inventory", "tools/computation_inventory.py"),
            ("certificate_and_runner_regressions", "computations/gb_ads3_sigma2_fermionic_spectrum/test_reproduction.py"),
            ("navigation_regressions", "tools/test_validate_repository.py"),
            ("two_derivative_components", "computations/two_derivative_fermionic/src/kernels/audit_exact_checks.py"),
            ("r2_components", "computations/r2_fermionic/checks/run_component_checks.py"),
            ("weyl_components", "computations/weyl_fermionic/checks/reference_suite.py"),
        ):
            tasks.append((name, ROOT, [str(ROOT / script)]))
        tasks.append(("separate_product_models", ROOT,
                      [str(ROOT / "computations/gb_ads3_sigma2/product_checks.py"), "--verify", "--fresh"]))
        tasks.append(("gb_ads5_reproduction", ROOT / "gauss_bonnet/ads5/code",
                      ["-m", "unittest", "checks.test_reproduction"]))
        # LOG contract checks and replay can write intermediate files. Copy
        # only this self-contained package, never mutate retained results.
        log = workspace / "log_fermionic"
        shutil.copytree(ROOT / "computations/log_fermionic", log,
                        ignore=shutil.ignore_patterns("__pycache__"))
        for name, module in (("log_contract", "checks.test_contract"),
                             ("log_preflight_regressions", "checks.test_rebuild"),
                             ("log_replay", "calculations.rebuild_from_standard")):
            tasks.append((name, log, ["-m", module]))
        tasks.append(("figure_01", ROOT, [str(ROOT / "figures/make_ads5_phases.py"),
                                         "--output-dir", str(figure_dir)]))
    return tasks


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="show full output from successful checks too")
    parser.add_argument("--all", action="store_true", help="also run component/replay/regression checks and build Figure 1")
    parser.add_argument("--output-dir", type=Path, help="external directory for figures and per-command logs")
    args = parser.parse_args(argv)
    if sys.flags.optimize:
        raise RuntimeError("Run without -O: scientific checks use assertions.")
    output = args.output_dir.resolve() if args.output_dir else None
    if output and (output == ROOT or output.is_relative_to(ROOT)):
        raise ValueError("Choose an output directory outside the repository.")
    if output:
        output.mkdir(parents=True, exist_ok=True)
    failed = False
    with tempfile.TemporaryDirectory(prefix="sugra-reproduction-") as temporary:
        workspace = Path(temporary)
        destination = output or workspace / "results"
        destination.mkdir(parents=True, exist_ok=True)
        for name, cwd, options in tasks(args.all, destination, workspace):
            command = [sys.executable, "-B", *options]
            print(f"Running {name}...", file=sys.stderr, flush=True)
            start = time.monotonic()
            with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as stream:
                try:
                    result = subprocess.run(command, cwd=cwd, stdout=stream,
                                            stderr=subprocess.STDOUT, check=False)
                    returncode = result.returncode
                except OSError as exc:
                    stream.write(f"Could not start this check: {exc}\n")
                    returncode = 1
                state = "PASS" if returncode == 0 else "NOT RUN" if returncode == 77 else "FAIL"
                failed |= returncode != 0
                print(f"{state} {name} ({time.monotonic()-start:.1f}s)", flush=True)
                if output:
                    stream.seek(0)
                    with (output / (name + ".log")).open("w") as retained:
                        retained.write(f"Command: {command!r}\nWorking directory: {cwd}\nExit code: {returncode}\n")
                        shutil.copyfileobj(stream, retained)
                if returncode != 0 or args.verbose:
                    print(f"--- {name}: exit {returncode} ---", file=sys.stderr)
                    stream.seek(0)
                    shutil.copyfileobj(stream, sys.stderr)
                    sys.stderr.flush()
        if output and args.all and not failed:
            shutil.copy2(workspace / "log_fermionic/outputs/downstream_summary.json",
                         output / "log_replay_summary.json")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
