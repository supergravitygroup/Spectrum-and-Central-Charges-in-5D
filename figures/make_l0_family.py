"""Reproduce Figure 2 using the existing Appendix C polynomials.

Plot conventions adapted from the supplied make_l0_family.py by Aksoy,
Okyay, Ozkan and Senisik (2026), MIT license.
"""
import argparse
from fractions import Fraction
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import sympy as s

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "computations/gb_ads3_sigma2"))
from model import L, k, D, M2, P2, P3, P4
from closed_forms import F, X, Y


def shading_grid():
    """Cubic discriminant, with exact arithmetic near cancellation or a locus."""
    constant_cubic = s.cancel(F.subs(M2, 0)/(D*(D-2)))
    assert s.Poly(constant_cubic, D).degree() == 3
    numerator = s.fraction(constant_cubic)[0]
    # Rescaling D by nonzero P3 does not change whether the roots are real.
    # It removes common P3 powers from the four coefficient evaluations.
    polynomial = s.Poly(s.cancel(numerator.subs(D, D/P3)), D)
    coeff = polynomial.all_coeffs()
    absolute = lambda e: sum(abs(c)*L**powers[0]*k**powers[1]
                             for powers, c in s.Poly(e, L, k).terms())
    values = s.lambdify((L, k), [s.horner(c, wrt=k) for c in coeff], "numpy")
    bounds = s.lambdify((L, k), [absolute(c) for c in coeff], "numpy")
    loci = (P2, P3, P4)
    locus_values = s.lambdify((L, k), loci, "numpy")
    locus_bounds = s.lambdify((L, k), [absolute(p) for p in loci], "numpy")
    exact_coeff = s.lambdify((L, k), coeff, "math")
    exact_loci = s.lambdify((L, k), loci, "math")
    lx = np.arange(1601, dtype=np.longdouble)/200
    ky = np.arange(-800, 1201, dtype=np.longdouble)/400
    lq = [Fraction(i, 200) for i in range(1601)]
    kq = [Fraction(i, 400) for i in range(-800, 1201)]
    states = np.zeros((len(ky), len(lx)), dtype=np.uint8)
    eps = np.finfo(np.longdouble).eps
    fallbacks = 0
    for start in range(0, len(ky), 80):
        ll, kk = np.meshgrid(lx, ky[start:start+80])
        a, b, c, d = np.asarray(values(ll, kk))
        terms = np.asarray([b*b*c*c, -4*a*c**3, -4*b**3*d, -27*a*a*d*d, 18*a*b*c*d])
        disc = terms.sum(axis=0)
        sensitivity = np.asarray([
            4*abs(c)**3 + 54*abs(a*d*d) + 18*abs(b*c*d),
            2*abs(b*c*c) + 12*abs(b*b*d) + 18*abs(a*c*d),
            2*abs(b*b*c) + 12*abs(a*c*c) + 18*abs(a*b*d),
            4*abs(b)**3 + 54*abs(a*a*d) + 18*abs(a*b*c)])
        error = 128*eps*(abs(terms).sum(axis=0)
                         + (sensitivity*np.asarray(bounds(abs(ll), abs(kk)))).sum(axis=0))
        near_locus = np.any(abs(np.asarray(locus_values(ll, kk)))
                            <= 64*eps*np.asarray(locus_bounds(abs(ll), abs(kk))), axis=0)
        uncertain = (abs(disc) <= error) | near_locus | (a == 0) | (ll == 0)
        slab = np.asarray(disc < 0, dtype=np.uint8)
        for row, col in zip(*np.where(uncertain)):
            lv, kv = lq[col], kq[start+row]
            if lv == 0 or any(p == 0 for p in exact_loci(lv, kv)):
                slab[row, col] = 2  # singular/non-AdS points are not classified as real
                continue
            aa, bb, cc, dd = exact_coeff(lv, kv)
            if aa == 0:
                slab[row, col] = 2 if bb == cc == dd == 0 else int(bb != 0 and cc*cc-4*bb*dd < 0)
            else:
                exact = bb*bb*cc*cc-4*aa*cc**3-4*bb**3*dd-27*aa*aa*dd*dd+18*aa*bb*cc*dd
                slab[row, col] = int(exact < 0)
            fallbacks += 1
        states[start:start+len(slab)] = slab
    print(f"PASS Figure 2 discriminant grid: {states.size} points; {fallbacks} exact fallbacks", flush=True)
    return lx.astype(float), ky.astype(float), states


def figure(output):
    lx, ky, states = shading_grid()
    numeric = lambda e: s.lambdify((L, k), e, "numpy")
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "cm", "font.family": "serif",
                         "pdf.fonttype": 42})
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(left=0.095, right=0.98, bottom=0.265, top=0.97)
    grey, red, blue, green = "#d4d4d4", "#c0392b", "#1f4fbf", "#1e8449"
    from matplotlib.colors import ListedColormap
    ax.pcolormesh(lx, ky, np.ma.masked_where(states == 2, states),
                  cmap=ListedColormap(["white", grey]), vmin=0, vmax=1,
                  shading="nearest", rasterized=True, antialiased=False)
    ll, kk = np.meshgrid(np.linspace(1e-5, 8, 1601), np.linspace(-2, 3, 1601))
    torus = 2*L - 8 + 3*k*L - k*L**2
    curves = [
        (torus, "black", "-", 1.65, r"$T^2$ ($v=0$)"),
        (P4, "black", "--", 1.2, r"$v\to\infty$"),
        (P3, blue, ":", 1.35, r"$P_3=0$"),
        (X, red, "-", 1.4, r"$c_L=0$"),
        (Y, green, "-", 1.4, r"$\kappa_{\rm eff}=0$"),
    ]
    handles = [Patch(facecolor=grey, edgecolor="none", label="complex energies at the constant level")]
    for expr, color, style, width, label in curves:
        with np.errstate(all="ignore"):
            ax.contour(ll, kk, numeric(expr)(ll, kk), levels=[0], colors=color,
                       linestyles=style, linewidths=width)
        handles.append(Line2D([], [], color=color, ls=style, lw=width, label=label))
    ax.axhline(2/3, color=red, ls="--", lw=1.4)
    handles.insert(-1, Line2D([], [], color=red, ls="--", lw=1.4, label=r"$c_R=0$"))
    ax.axhline(0, color="0.4", lw=0.6)
    ax.set(xlim=(0, 8), ylim=(-2, 3), xlabel=r"$L$", ylabel=r"$k=\lambda g^2$")
    ax.tick_params(direction="out", length=4)
    ax.text(1.0, -1.55, r"$H^2/\Gamma$", fontsize=17)
    ax.text(6.4, -1.55, r"$S^2$", fontsize=17)
    fig.legend(handles=handles[:1], loc="lower center", frameon=False, fontsize=11,
               bbox_to_anchor=(0.54, 0.145), handlelength=2.6)
    fig.legend(handles=handles[1:], loc="lower center", ncol=3, frameon=False, fontsize=11,
               bbox_to_anchor=(0.54, 0.045), handlelength=2.6, columnspacing=3, labelspacing=0.9)
    output.mkdir(parents=True, exist_ok=True)
    target = output / "figure_02_ads3_backgrounds.pdf"
    fig.savefig(target, dpi=260, metadata={"CreationDate": None, "ModDate": None})
    plt.close(fig)
    print(f"PASS Figure 2: {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    figure(parser.parse_args().output_dir)
