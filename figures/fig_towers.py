"""Reproduce Figure 3 from the existing certified spectrum and residue data.

Plot conventions adapted from the supplied fig_towers.py by Aksoy, Okyay,
Ozkan and Senisik (2026), MIT license. No external pickle is required.
"""
import argparse
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import sympy as s

PACKAGE = Path(__file__).resolve().parents[1] / "computations/gb_ads3_sigma2"
sys.path.insert(0, str(PACKAGE))
from model import L, k
from closed_forms import nuf


def tower_rows(recompute=False):
    if recompute:
        from norms import numerical_level
        levels = [numerical_level(10, s.Rational(1, 10), s.Integer(j+1), dps=80)
                  for j in range(2, 17)]
    else:
        stored = json.loads((PACKAGE / "outputs/norm_samples.json").read_text())
        levels = [row for row in stored["levels"]
                  if (row["L"], row["k"], row["chi"]) == ("10", "1/10", 1)]
    assert sorted(int(row["S"])-1 for row in levels) == list(range(2, 17))
    rows = []
    flat = nuf.subs({L: 10, k: s.Rational(1, 10)})
    assert flat == s.Rational(37, 7)
    for row in levels:
        j = int(row["S"])-1
        for family, name, count in (("spin2", "spin-2", 3), ("scalar", "(1,0)", 5)):
            assert len(row[family]) == count
            for entry in row[family]:
                root = mp.mpf(entry["D_chi_plus"])
                assert entry["norm"] in (-1, 1)
                energy = root if root > 1 else 2-root
                rows.append((j, name, float(energy), entry["norm"]))
        assert row["flat"]["charged_norm"] == -1
        assert row["flat"]["neutral_inertia"] == [-1, -1]
        rows.extend((j, "flat", float(flat), -1) for _ in range(2))
    assert len(rows) == 150
    return rows, float(flat)


def figure(output, recompute=False):
    rows, flat = tower_rows(recompute)
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    ax.axhline(flat, color="0.5", lw=0.9, ls=(0, (4, 3)), zorder=0)
    ax.text(16.75, flat, r"$\Delta_f$", va="center", ha="left", color="0.3", fontsize=8.5,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.6))
    for shift in (-1, 1):
        ax.axhline(flat+shift, color="0.65", lw=0.8, ls=(0, (1, 2)), zorder=0)
        label = r"$\Delta_f%s1$" % ("+" if shift > 0 else "-")
        ax.text(16.75, flat+shift+0.25*shift, label, va="center", ha="left", color="0.4",
                fontsize=7.5, bbox=dict(facecolor="white", edgecolor="none", pad=0.4))
    families = [("spin-2", "#2a6fc9", "o", "spin-2 multiplets"),
                ("(1,0)", "#d9622b", "s", r"$(1,0)$ multiplets"),
                ("flat", "#1a9a6c", "D", "flat multiplets")]
    for family, color, marker, label in families:
        for norm in (1, -1):
            pts = [(j, delta) for j, name, delta, sign in rows if name == family and sign == norm]
            if not pts:
                continue
            ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=20, marker=marker,
                       facecolors=color if norm == 1 else "white", edgecolors=color,
                       linewidths=1.2, zorder=3, label=label)
            label = None
    ax.set(xlabel=r"$S^2$ level $j$", ylabel=r"$\Delta$", xlim=(1.5, 17.6), ylim=(0, 22.5))
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    fig.tight_layout()
    output.mkdir(parents=True, exist_ok=True)
    target = output / "figure_03_kk_spectrum.pdf"
    fig.savefig(target, metadata={"CreationDate": None, "ModDate": None})
    plt.close(fig)
    print(f"PASS Figure 3: 150 plotted multiplets; {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--recompute", action="store_true", help="Recompute roots and residue signs without modifying stored data")
    args = parser.parse_args()
    figure(args.output_dir, args.recompute)
