"""Build Figure 1 from the supplied manuscript's unchanged TikZ source.

Requires Tectonic (with its TeX bundle) or pdflatex with standalone, amsmath
and TikZ. Only the requested output directory is written; no manuscript is
needed at runtime. Exit 77 means the TeX dependency is unavailable.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    engine = shutil.which("tectonic") or shutil.which("pdflatex")
    if engine is None:
        print("NOT RUN Figure 1: install Tectonic or pdflatex with standalone/amsmath/TikZ.")
        return 77
    output = args.output_dir.resolve()
    if output == HERE.parent or output.is_relative_to(HERE.parent):
        raise ValueError("Choose an output directory outside the repository.")
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ads5-figure-") as temporary:
        work = Path(temporary)
        shutil.copy2(HERE / "figure_01_ads5_phases.tex", work / "phases.tex")
        wrapper = work / "figure_01_ads5_phases.tex"
        wrapper.write_text("\\documentclass[tikz,border=3pt]{standalone}\n"
                           "\\usepackage{amsmath}\n\\begin{document}\n"
                           "\\input{phases.tex}\n\\end{document}\n")
        if Path(engine).name == "tectonic":
            command = [engine, "--untrusted", "--keep-logs", "--outdir", str(work), str(wrapper)]
        else:
            command = [engine, "-interaction=nonstopmode", "-halt-on-error", str(wrapper)]
        subprocess.run(command, cwd=work, check=True)
        target = output / "figure_01_ads5_phases.pdf"
        shutil.copy2(work / target.name, target)
        print(f"PASS Figure 1: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
