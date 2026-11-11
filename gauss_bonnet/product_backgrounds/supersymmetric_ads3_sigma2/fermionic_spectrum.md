# Fermionic spectrum on the BPS product

The spectrum calculation starts from the [coupled quadratic action](fermionic_quadratic_action.md) and keeps its gravitino–compensator mixing and full inherited supercovariant derivatives. It supplies the operators, rank-lowering roots and bosonic-multiplet comparison referenced in paper Section 4.6 and Table 12 (repository citation 26; `sec:GBprodferm`, `tab:GBferm`). The [computation guide](../../../computations/gb_ads3_sigma2_fermionic_spectrum/README.md) gives reproduction commands, the complete sample list and the numerical qualifications.

## From the action to physical roots

For paired frame modes $`z^Dy^S`$ and $`z^{2-D}y^{1-S}`$, use

```math
\begin{aligned}
S^{(2)}_{n,q_R}
 &=\mathbf b^TK_{n,q_R}(D,S)\mathbf a,
 & n&=\pm\tfrac12,\ \pm\tfrac32,
 &q_R&=\pm1,\\
K_{n,q_R}
 &=K^{LR}_{n,q_R}-\frac{k}{2g^2}
       \left(K^W_{n,q_R}+K^{\log}_{n,q_R}\right),
 &M^2&=-v\ell^2S(1-S).
\end{aligned}
\tag{F25.1}
```

The labels $`W`$ and $`\log`$ denote the already normalized raw $`-2W`$ and $`-4\log`$ contributions of the coupled quadratic action. Equation (F25.1) keeps their accepted relative normalization; it does not fit it to the spectrum. The half-spin matrices have eight gravitino and two compensator amplitudes; the three-half-spin matrices have two gravitino amplitudes. Every saved sector contains its ordered row/column basis and all coefficients of $`K(D)=\sum_jC_jD^j`$.

The physically relevant invariant is loss of the matrix's normal rank, equivalently common roots of its maximal minors. A determinant of a half-spin $`10\times10`$ matrix would vanish identically because of gauge freedom. At the numerical generic probes the expected ranks are

```math
\begin{array}{c|cc}
|n|&\dim K&\mathop{\mathrm{rank}}\nolimits_{\rm generic}K\\ \hline
\tfrac12&10&8\\
\tfrac32&2&2
\end{array}
\tag{F25.2}
```

The two half-spin null columns are constructed from the background supersymmetry transformations, not obtained by fitting a kernel. Their entries depend on $`D`$ because the gauge parameter has the same mode dependence. Generation checks their independence and $`K(D)G_\epsilon(D)=0`$ at two distinct values of $`D`$ and records the intersection of the two kernels; full verification reconstructs them at an additional off-grid value in all 72 half-spin sectors. A constant two-column projection is therefore not a general substitute for the gauge modes. These tests and the generic-rank probes are finite numerical evidence, not a proof of normal rank eight at all parameters. The action-level normalization negative control checks that rescaling the fermionic GB contribution destroys the SUSY-null relation.

In the saved two-probe comparisons, the kernel intersection has dimension zero in 70 half-spin sectors and dimension one in two. Thus the two-dimensional null plane varies with $`D`$ in every tested sector; this does not imply that every individual null direction changes in every case.

Numerically, four square projections of the rank-eight polynomial matrix generate candidate roots. A candidate must lower the rank of the full unprojected matrix, have a localized singular-value minimum, survive independent projections and energy scalings, and pass a fresh direct-action evaluation. The retained gap must exceed by a factor of twenty a budget incorporating coefficient roundoff, action/interpolant disagreement and finite polynomial-root residual. This resolves rank in the numerical backward-error sense; multiplicity is retained only when supported by extra nullity. The code records rather than hides unresolved homogeneous pencil pairs and large-energy conditioning diagnostics. This procedure supplies a numerical common-root census at the tested points; it is not an exact calculation of the gcd of every maximal minor.

## Reading one sector record

The [sample record](../../../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/H2_3_2_s13_np3_q+1.json)
uses `(L,k,g,S)=(3,2,1,1/3)`, boost `n=3/2` and `q_R=+1`.
Here D is the exponent in the frame-mode ansatz, not the auxiliary scalar D;
k is the dimensionless coupling `lambda*g^2`, not the curvature denoted by
k in the generic AdS5 code. S specifies the surface-mode ansatz and enters
M² through (F25.1).

| Record entry | How to read it |
|---|---|
| `basis_a`, `basis_b`, `coefficients` | Ordered column and row amplitudes and C₀, C₁, … in K(D); this sector is 2×2, with generic rank two. |
| First `roots` entry | D = `-0.538092344655 -3.634e-15i`, multiplicity 1; retain its complex part in the calculation. |
| Corresponding `direct_root_checks` entry | `resolved_extra_nullity=1` and retained-gap/error-budget ratio `9.1737e+12`; these test numerical rank loss at that root. |
| `local_rank_drop` and independent-seed record | Check that the small singular value is localized and the extraction is stable under a different projection. |
| Sample-level `direct_modes` and matching | Apply the shadow rule (F25.4), retaining its spin and charge reversal, then compare the complete multisets. |

The values above quote an existing saved record; they are not replacements
for fresh verification. A certificate is not a norm calculation. Continue
with the prediction below only after the direct operator's root test; the
bosonic prediction is not an input to that test.

## Independent supersymmetry prediction

The bosonic prediction comes from the previously checked cubic $`C(d)`$, quintic $`F(d)`$ and flat-multiplet parameter $`\nu_f`$ in the [bosonic spectrum package](../../../computations/gb_ads3_sigma2/README.md). None of those roots enters construction, interpolation, candidate selection or rank testing of (F25.1).

Let $`d`$ denote the roots in the $`\chi=+1`$ convention used by those polynomials. Construct the following **raw fermionic** labels, with both $`q_R=\pm1`$ in every entry:

```math
\begin{aligned}
C(d)=0:&\quad
 (s,D,q_R)=\bigl(\tfrac32,\ 1+\chi(d-\tfrac32),\ \pm1\bigr),\\
F(d)=0:&\quad
 (s,D,q_R)=\bigl(\tfrac12,\ 1+\chi(d-\tfrac12),\ \pm1\bigr),\\
\nu_{f,\chi}&=1+\chi(\nu_f-1),\\
\text{flat lower}:&\quad
 (s,D,q_R)=\bigl(1-\tfrac\chi2,\ \nu_{f,\chi}-\tfrac12,\ \pm1\bigr),\\
\text{flat upper}:&\quad
 (s,D,q_R)=\bigl(1+\tfrac\chi2,\ \nu_{f,\chi}+\tfrac12,\ \pm1\bigr).
\end{aligned}
\tag{F25.3}
```

After these supersymmetry shifts, choose the shadow representative by

```math
(s,\Delta,q_R)=
\begin{cases}
(s,D,q_R),&\mathop{\mathrm{Re}}\nolimits D\ge1,\\
(-s,2-D,-q_R),&\mathop{\mathrm{Re}}\nolimits D<1.
\end{cases}
\tag{F25.4}
```

Applying the shadow operation to a bosonic root before its fermionic shift changes the prediction and is not the implemented rule. The charge reversal in (F25.4) is fixed; the comparison does not try several charge conventions and select a successful one. Complex roots are retained without replacing them by their real parts. The AdS$`_3`$ weights are $`h=(\Delta+s)/2`$ and $`\bar h=(\Delta-s)/2`$.

For nonzero $`k`$, the cubic and quintic give six and ten fermions, and the two flat multiplets give four, for twenty in total. At $`k=0`$ the lower-degree limits of $`kC`$ and $`kF`$ give twelve at generic hyperbolic and spherical levels. Degeneracies are counted with multiplicity.

The direct calculation and the prediction are compared by a one-to-one assignment with identical spin and charge and $`|\Delta_{\rm direct}-\Delta_{\rm pred}|<10^{-6}`$. It checks the complete multisets, so an omitted mode, extra copy, incorrect multiplicity, spin or R-charge causes failure. Majorana-related negative-boost sectors are checked separately rather than being added to the physical count.

## Constant torus level and the two-derivative limit

The $`k=0`$, $`L=4`$, constant-$`T^2`$ level is a separate calculation, not a continuation of a nonzero-curvature harmonic basis. The two massive bosonic roots are

```math
d_\pm=\frac{1\pm\sqrt{33}}3.
\tag{F25.5}
```

They give four fermions by $`(s,D,q_R)=(1/2,d_\pm+1/2,\pm1)`$ and (F25.4). The other ten entries are, for each charge,

```math
(s,\Delta)=
\left(\tfrac32,\tfrac32\right),\quad
2\times\left(\tfrac12,\tfrac52\right),\quad
\left(-\tfrac32,\tfrac52\right),\quad
\left(-\tfrac12,\tfrac32\right).
\tag{F25.6}
```

These ten light entries should not all be called massless bulk fermions. Together with (F25.5) they give fourteen modes. The repeated $`(1/2,5/2)`$ entry is kept as a double occurrence; exact LR matrix ranks provide an additional check of the associated nullity increase.

At $`L=3`$, $`S=1/3`$, the recorded $`k=1/10,1/100,1/1000`$ spectra are compared directly with the $`k=0`$ spectrum. A label-preserving assignment selects twelve light modes; the other eight form the heavy set. The expected scale follows from the bosonic flat parameter,

```math
\lim_{k\to0^+}k\nu_f=\frac8{L+2},
\qquad
k\mathop{\mathrm{Re}}\nolimits\Delta_{\rm heavy}\longrightarrow\frac85
\quad(L=3).
\tag{F25.7}
```

The exact limit in (F25.7) is checked separately from the three numerical fermion samples. The latter record the light energy differences, those differences divided by $`k`$, and all eight heavy values of $`k\mathop{\mathrm{Re}}\nolimits\Delta`$. Decreasing deviations support the stated small-$`k`$ behavior at this fixed level; three samples do not prove a uniform asymptotic estimate over all harmonics.

The current [direct comparison](../../../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/small_k.json) finds twelve light and eight heavy modes at every one of these points:

| $`k`$ | Largest light $`\lvert\Delta(k)-\Delta(0)\rvert`$ | Light difference divided by $`k`$ | Largest heavy $`\lvert k\mathop{\mathrm{Re}}\nolimits\Delta-1.6\rvert`$ |
|---:|---:|---:|---:|
| $`10^{-1}`$ | $`0.206314`$ | $`2.06314`$ | $`0.167582`$ |
| $`10^{-2}`$ | $`0.0182162`$ | $`1.82162`$ | $`0.0166223`$ |
| $`10^{-3}`$ | $`0.00185612`$ | $`1.85612`$ | $`0.00166024`$ |

## Records and scope of the conclusion

The [sample and operator index](../../../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/index.md) links twelve nonzero-$`k`$ manuscript points, five generic $`k=0`$ surface levels and the constant torus level: eighteen samples, each with eight directly linked sector files. Each sample has a complete spectrum and matching record, and each sector file contains its operator coefficients, roots and diagnostics. The [combined table](../../../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/table.json) stores their machine-readable summary. The [verification record](../../../computations/gb_ads3_sigma2_fermionic_spectrum/outputs/verification.json) separates saved direct-root checks, fresh action holdouts, independently projected roots, exact torus ranks and deliberately incorrect spectra. These are current repository calculations; the manuscript's printed residuals are not relabelled as new measurements.

In the generated direct spectra, all twelve nonzero-$`k`$ points have 20/20 matched modes, the five generic two-derivative points have 12/12, and the constant torus has 14/14. The largest positive-boost energy differences in these three groups are respectively $`1.11\times10^{-8}`$, $`1.11\times10^{-13}`$ and $`2.80\times10^{-14}`$, below the $`10^{-6}`$ matching criterion. The largest of these occurs at $`k=10^{-3}`$, where heavy energies make numerical conditioning more demanding. The package guide lists the separately measured error at every point.

The full verification also passes in the negative-boost sectors; the largest error over both signs is $`1.63\times10^{-8}`$. Fresh action holdouts in all 144 sectors have maximum scaled residual $`1.38\times10^{-14}`$, and the additional 72 SUSY-column checks have maximum normalized residual $`3.51\times10^{-15}`$. A third projection seed reproduces the roots within $`1.35\times10^{-8}`$. All direct-root backward-error certificates retain a nonzero singular-value gap of at least $`200.55`$ times their error budget. Solver regressions and deliberately wrong spectra test the rejection mechanisms separately from these physical samples.

The $`M^2<0`$ row at $`(L,k)=(5,1)`$ is only an algebraic operator test. The principal-series rows include both $`\chi=-1`$ cases, and the matching includes complex-energy pairs. Global multiplicities on $`\Sigma_2`$, boundary conditions and fermion norms are not computed. Neither $`k\ne0`$ on $`T^2`$ nor the excluded critical loci are included.

The result is a numerical comparison at the examined regular backgrounds and levels. The localization and backward-error tests distinguish resolved rank-lowering roots from common numerical artifacts, but unresolved pencil pairs and ill-conditioned large-$`D`$ regions are not an analytic exclusion of every possible additional finite root. An all-coupling symbolic completeness theorem is not claimed.
