# Paper figures

The Figure 2 and 3 scripts redraw the Section 4 figures from the repository's
existing formulas and checked data. Run them from the repository root,
choosing an output directory:

```sh
python3 -B figures/make_l0_family.py --output-dir /tmp/sugra-figures
python3 -B figures/fig_towers.py --output-dir /tmp/sugra-figures
```

The output files are `figure_02_ads3_backgrounds.pdf` and
`figure_03_kk_spectrum.pdf`. The scripts need Matplotlib, NumPy, SymPy and
mpmath in the environment documented on the [front page](../README.md).
They do not modify the paper or the stored computation outputs.

| Figure | Inputs and meaning |
| --- | --- |
| 2: background family | Imports $`P_i`$, $`X`$, $`Y`$ and the constant-level cubic from [the bosonic package](../computations/gb_ads3_sigma2/closed_forms.py). The curves are the loci of Table 8. The shaded region has negative cubic discriminant and hence two complex energies at the constant level. The plot is not a count of all unstable modes. |
| 3: bosonic towers | Reads [norm_samples.json](../computations/gb_ads3_sigma2/outputs/norm_samples.json), selecting $`(L,k)=(10,1/10)`$ and $`j=2,\ldots,16`$ from Table 11. The plotted energies and norm signs come from the existing certified propagators. Filled markers mean positive norm, open markers negative norm. The lines are $`\Delta_f`$ and $`\Delta_f\pm1`$, with $`\Delta_f=37/7`$. |

To recompute all 150 Figure 3 entries from the existing polynomials and
propagator residues, without replacing the stored results:

```sh
python3 -B figures/fig_towers.py --recompute --output-dir /tmp/sugra-figures
```

This mode also needs python-flint. It uses the same residue calculation
as the main bosonic checks. The two coincident flat multiplets are retained
as separate entries at each level.

Figure 2 evaluates the cubic coefficients on the paper's grid. Near
cancellation or a special locus it uses exact rational arithmetic for
the discriminant. Singular and non-AdS points are masked rather than
assigned a real spectrum.

The plotting conventions are adapted from the supplied
`extra_checks_for_student_repo` scripts by Erol Aksoy, Cagatay Okyay,
Mehmet Ozkan and Cemal Berfu Senisik (2026), provided under MIT for code
and CC BY 4.0 for documentation and data. The curve equations, spectra and
norms are taken from this repository rather than copied into a second
computation pipeline. Figure 2 uses the layout of the final supplied
paper; pixel-level rendering can vary with plotting-library versions.

## Figure 1: AdS5 parameter ranges

The author-supplied [TikZ source](figure_01_ads5_phases.tex) is copied unchanged
from the draft_v109 manuscript bundle. It draws the analytic classifications
of Section 3; it is a diagram of those results, not a new parameter scan.
The shaded intervals, exceptional-point symbols and printed coupling labels
are retained. Their derivations are the [R²](../r2/ads5/README.md),
[Weyl](../weyl2/ads5/README.md), [GB](../gauss_bonnet/ads5/README.md) and
[LOG](../log/ads5/README.md) chapters.

```sh
python3 -B figures/make_ads5_phases.py --output-dir /tmp/sugra-figures
```

This writes `figure_01_ads5_phases.pdf` from a temporary standalone wrapper.
Install Tectonic (which may download its TeX bundle), or pdflatex with the
standalone, amsmath and TikZ packages. Python requirements alone do not
supply TeX. Missing TeX is reported as NOT RUN with a nonzero exit status.
All three builds run in `python -B reproduce.py --all`; the Figure 3 build
then also recomputes its 150 entries. Use `--output-dir` with an external
path to keep the PDFs and per-command logs. No external manuscript is a
runtime dependency.

Source SHA-256: `deea47811a27be3582c5358b08c4954480eb9a935afda9a9986b67fd9b47e164`.
