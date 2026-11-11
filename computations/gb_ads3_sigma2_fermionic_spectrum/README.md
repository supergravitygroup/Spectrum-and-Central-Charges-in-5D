# GB product fermionic spectrum

This package extracts finite-point fermionic roots from the [coupled quadratic action](../gb_ads3_sigma2_fermionic/README.md), then compares them with a separately calculated [bosonic prediction](../gb_ads3_sigma2/README.md). It implements the numerical spectrum comparison in paper Section 4.6 and Table 12 (repository citation 26; `sec:GBprodferm`, `tab:GBferm`). The [spectrum derivation](../../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md) explains the operators, supersymmetry directions, charge convention and representation content.

Bosonic energies and target mode counts do not enter action interpolation or root extraction. They enter the final comparison only. All runtime inputs are included in the repository.

## Reproduction

Use the versions in [requirements.txt](requirements.txt), in an environment outside the repository. From the repository root, the full verification command is:

```sh
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/checks.py --workers 3
```

The current environment is Python 3.14.1 with NumPy 2.5.4, SciPy 1.18.1, SymPy 1.14.0, SymEngine 0.15.0 and mpmath 1.3.0. If these libraries live in a separate directory, prepend its location with `PYTHONPATH`; this does not change any scientific input.

This command is read-only. It verifies source and implementation fingerprints, reruns solver and matching controls, recomputes the bosonic prediction, checks both boost-sign spectra, and repeats root extraction with a new projection seed. It also calls the current action at one new off-grid value of $`D`$ in all 144 sectors and reconstructs the two independent SUSY columns there in all 72 half-spin sectors. The direct-action backward-error certificates at the saved roots are recalculated from the recorded direct-action singular values and disagreement; running the verifier does not repeat every root evaluation from scratch.

For a quicker, explicitly narrower review:

```sh
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/checks.py --stored-only
```

This skips the 144 fresh action holdouts and independent projected extractions. It still reruns the matching controls, polynomial regression tests, bosonic prediction, exact constant-torus ranks and small-$`k`$ comparison. It cannot replace the canonical full verification record.

The following commands deliberately regenerate this package's outputs:

```sh
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/derive.py --workers 3
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/checks.py --workers 3 --write-log
```

`derive.py --sample H2_3_2_s13 --workers 3` restricts generation to one background and its eight sectors. `--resume` reuses existing sector JSON files and computes missing ones; it does **not** itself establish that reused records match current inputs. Run the fingerprint-aware verifier after resuming. Generation also uses an interpolation cache in the system temporary directory, keyed by action source bytes, adapter/interpolation code, numerical-library versions and input parameters. The default verifier neither creates nor consumes that disk cache. The `--stored-only --write-log` combination is rejected.

### Certificate completeness and portable replay

Every root must have one correctly associated certificate, with a matching
multiplicity and finite required fields. Empty, truncated and misaligned
certificate lists are errors even if another root-extraction check passes.
The comparator in [certificates.py](certificates.py) keeps supplied root
coordinates, direct-action singular values and discrete nullities exact.
Derived floating diagnostics are compared with a `1024*float64_epsilon`
allowance in the coefficient scale `B=sum_j ||C_j||_F |D|^j`; scaled residuals
use the corresponding dimensionless allowance. The inverse-budget gap is
compared through the retained singular value it reconstructs, not a universal
relative tolerance on the ratio. This is a replay comparison policy, not a
change to the physical residual limits or the required gap of twenty.
Freshly recomputed certificates must still satisfy all original rank,
localization and error-budget tests. Run the passing and deliberately failing
controls with `python -B computations/gb_ads3_sigma2_fermionic_spectrum/test_reproduction.py`.

## Operators and output records

The action uses paired modes $`z^Dy^S`$ and $`z^{2-D}y^{1-S}`$, with

```math
\begin{aligned}
S^{(2)}_{n,q_R}&=\mathbf b^TK_{n,q_R}(D,S)\mathbf a,
&K_{n,q_R}(D,S)&=\sum_{j=0}^{d}C_jD^j,\\
n&=\pm\tfrac12,\ \pm\tfrac32,
&q_R&=\pm1.
\end{aligned}
```

For $`|n|=1/2`$, $`K`$ is $`10\times10`$ and contains eight gravitino and two compensator amplitudes. For $`|n|=3/2`$, it is $`2\times2`$ and contains gravitino amplitudes only. The row and column bases remain those of the coupled quadratic action; no gauge fixing removes the two local-supersymmetry columns.

The saved interpolation has degree two in all 96 nonzero-$`k`$ sectors and degree one in all 48 two-derivative sectors. These are the degrees measured at the recorded inputs, with the discarded higher coefficients retained in each interpolation diagnostic.

Each `outputs/<sample>_n[p|m][1|3]_q[+1|-1].json` stores:

- The input parameters, complete ordered `basis_a` and `basis_b`, and coefficient matrices `coefficients` as real/imaginary arrays. Their order is $`C_0,C_1,\ldots`$; rows multiply $`\mathbf b`$ and columns multiply $`\mathbf a`$.
- Interpolation degree, discarded high-coefficient sizes, off-grid residuals, generic-rank probes and projection/pencil diagnostics.
- The common rank-lowering roots with multiplicities, singular values, local rank-drop diagnostics, independent-seed differences and fresh direct-action checks at every retained root.
- In half-spin sectors, two SUSY columns at two distinct $`D`$ values, their projection residuals and the dimension of the intersection of the two numerical kernels.

Each `outputs/<sample>.json` combines its eight sectors, records the direct and predicted spectra, and gives the actual one-to-one matching. The positive-boost sectors supply one representative spectrum; the verifier independently compares the negative-boost sectors, without double-counting the Majorana-related modes. [The sample and operator index](outputs/index.md) links all 18 sample comparisons and their 144 sector matrices. The machine-readable [table.json](outputs/table.json) collects the summary values. [verification.json](outputs/verification.json) records the full fresh verification and versions; [verification.log](outputs/verification.log) is its compact summary. [small_k.json](outputs/small_k.json) records the direct light/heavy comparison.

## Numerical method and safeguards

1. Five complex interpolation nodes on a circle around $`D=1`$ reconstruct the action polynomial. Coefficients below $`2\times10^{-11}`$ of the largest coefficient are removed only at the high-degree end; the discarded sizes are recorded. Two off-grid action evaluations must agree within $`2\times10^{-9}`$. Selected first-point and small-$`k`$ sectors additionally use a different seven-node grid and radius.
2. Three generic probes determine the numerical normal rank: eight in each half-spin sector and two in each three-half-spin sector. At rank eight, four independent complex orthonormal left/right projections give square $`8\times8`$ polynomial matrices. At full rank, the identity projection suffices. A generalized companion pencil yields candidates, followed by determinant-derivative refinement.
3. A candidate is retained only if it lowers the rank of the original unprojected matrix and its small singular value is localized relative to four nearby probes. Candidate multisets must agree across four projections. Unique unmatched rank-lowering candidates cause failure; extra Newton copies of a retained root do not count as new modes. Close roots are separated using measured cross-projection uncertainty, rather than a fixed clustering radius. Multiplicity requires sufficient extra nullity.
4. The complete extraction is repeated with seeds 25 and 109 and different energy scalings. At every retained root, the action is evaluated directly, separately from its interpolant. Its backward-error-resolved rank must support the claimed multiplicity with a retained gap at least twenty times the error budget, which includes coefficient roundoff, action/interpolant disagreement and finite polynomial-root residual. The full verifier adds seed 2030, another scaling, a new action holdout in every sector and a fresh SUSY-column check in every half-spin sector.
5. Only after extraction, a minimum-cost **perfect matching** compares direct and predicted modes. Edges require identical spin and R-charge and energy error below $`10^{-6}`$. Duplicate entries remain separate, preserving multiplicity. Six incorrect spectra must fail; a case on which greedy nearest-neighbor matching fails must pass the global assignment.

The 18 checks in the [polynomial regression suite](test_polynomial.py) cover separated and close roots, semisimple repeated roots, complex roots, gauge-null polynomial matrices, rank localization, large-energy artifacts and the actual constant-torus double root. It fails rather than asserting a multiplicity that the available rank drop cannot resolve. Defective Jordan multiplicities are outside the supported census.

More explicitly, let $`r`$ be the generic rank, $`m`$ the candidate multiplicity, $`A=\|K_{\rm action}-K_{\rm poly}\|_2`$, $`R=\sigma_{r-m+1}(K_{\rm poly})`$ with singular values ordered decreasingly, and $`B=\sum_j\|C_j\|_F|D|^j`$. The absolute budget is

```math
\varepsilon_{\rm rank}
=\max\bigl(4(A+R)+128\varepsilon_{\rm machine}B,\ 10^{-13}\bigr).
```

The certificate requires $`A/B\le2\times10^{-9}`$, $`R/B\le2\times10^{-8}`$, a localized rank drop, exactly $`r-m`$ direct-action singular values above this budget, and the smallest retained one at least $`20\varepsilon_{\rm rank}`$. This is a numerical backward-error certificate, not an exact rank computation.

Small singular values alone do not certify a physical root: large-$`D`$ ill-conditioning can persist over a neighborhood. Likewise, unresolved homogeneous pencil pairs are not an analytic proof that no very large finite roots exist. Their counts, local diagnostics, backward errors and projection spreads are retained. Agreement of the resolved spectra is numerical evidence at the stated samples, not an exact polynomial-gcd certificate or an all-parameter completeness theorem.

## Background and level coverage

All stored points set $`g=1`$ explicitly. The harmonic coordinate is $`M^2=-v\ell^2S(1-S)`$; sphere levels have $`S=j+1`$, and the principal hyperbolic series has $`S=1/2+i\nu_H`$.

| Sample label | $`L`$ | $`k`$ | $`S`$ | Direct/predicted count | Maximum energy difference |
|---|---:|---:|---|---:|---:|
| [H2_3_2_s13](outputs/index.md#sample-h2-3-2-s13) | 3 | 2 | $`1/3`$ | 20/20 | $`4.62\times10^{-13}`$ |
| [H2_3_2_s14](outputs/index.md#sample-h2-3-2-s14) | 3 | 2 | $`1/4`$ | 20/20 | $`4.96\times10^{-13}`$ |
| [H2_5_1_algebraic](outputs/index.md#sample-h2-5-1-algebraic) | 5 | 1 | 3 | 20/20 | $`3.74\times10^{-12}`$ |
| [H2_7o2_1o2](outputs/index.md#sample-h2-7o2-1o2) | $`7/2`$ | $`1/2`$ | $`1/2`$ | 20/20 | $`1.03\times10^{-10}`$ |
| [H2_3_1o10](outputs/index.md#sample-h2-3-1o10) | 3 | $`1/10`$ | $`1/3`$ | 20/20 | $`3.51\times10^{-12}`$ |
| [H2_3_1o100](outputs/index.md#sample-h2-3-1o100) | 3 | $`1/100`$ | $`1/3`$ | 20/20 | $`7.58\times10^{-11}`$ |
| [H2_3_1o1000](outputs/index.md#sample-h2-3-1o1000) | 3 | $`1/1000`$ | $`1/3`$ | 20/20 | $`1.11\times10^{-8}`$ |
| [H2_3_1o10_principal](outputs/index.md#sample-h2-3-1o10-principal) | 3 | $`1/10`$ | $`1/2+1.3i`$ | 20/20 | $`3.35\times10^{-12}`$ |
| [H2_7o2_1_principal](outputs/index.md#sample-h2-7o2-1-principal) | $`7/2`$ | 1 | $`1/2+1.3i`$ | 20/20 | $`4.73\times10^{-12}`$ |
| [H2_7o4_12o5_principal](outputs/index.md#sample-h2-7o4-12o5-principal) | $`7/4`$ | $`12/5`$ | $`1/2+1.3i`$ | 20/20 | $`3.23\times10^{-11}`$ |
| [S2_10_1o10](outputs/index.md#sample-s2-10-1o10) | 10 | $`1/10`$ | 3 | 20/20 | $`8.47\times10^{-10}`$ |
| [S2_5_minus1](outputs/index.md#sample-s2-5-minus1) | 5 | $`-1`$ | 3 | 20/20 | $`9.48\times10^{-13}`$ |
| [k0_H2_3_s13](outputs/index.md#sample-k0-h2-3-s13) | 3 | 0 | $`1/3`$ | 12/12 | $`7.51\times10^{-15}`$ |
| [k0_H2_3_s14](outputs/index.md#sample-k0-h2-3-s14) | 3 | 0 | $`1/4`$ | 12/12 | $`4.49\times10^{-15}`$ |
| [k0_H2_7o2](outputs/index.md#sample-k0-h2-7o2) | $`7/2`$ | 0 | $`1/2`$ | 12/12 | $`2.81\times10^{-14}`$ |
| [k0_S2_5_j2](outputs/index.md#sample-k0-s2-5-j2) | 5 | 0 | 3 | 12/12 | $`1.11\times10^{-13}`$ |
| [k0_S2_5_j3](outputs/index.md#sample-k0-s2-5-j3) | 5 | 0 | 4 | 12/12 | $`7.17\times10^{-14}`$ |
| [k0_T2_constant](outputs/index.md#sample-k0-t2-constant) | 4 | 0 | 0 | 14/14 | $`2.80\times10^{-14}`$ |

The first twelve rows reproduce the background/level choices of manuscript Table 12 (`tab:GBferm`); the six $`k=0`$ rows test the two-derivative statements following it. There are eight sectors per row, hence 144 sector polynomials. `H2_5_1_algebraic` has $`M^2<0`$ and is an algebraic operator check, not a physical hyperbolic harmonic. The two principal-series rows with $`L=7/2,7/4`$ use $`\chi=-1`$. Complex energies are retained and compared as complex numbers.

The displayed differences are rounded values from this implementation's current [combined table](outputs/table.json), using the positive-boost representatives. They are new numerical measurements, not a transcription of the manuscript's residual column. Both boost signs are tested in the verification record.

The full recorded verification passed: 18 polynomial regressions, six rejected incorrect spectra and two accepted matching controls, all 18 sample bijections in both boost signs, exact constant-torus ranks, and the direct small-$`k`$ comparisons. Across 144 fresh action holdouts the largest scaled disagreement is $`1.38\times10^{-14}`$; across 72 fresh SUSY-column checks the largest normalized residual is $`3.51\times10^{-15}`$. A third projection seed changes root energies by at most $`1.35\times10^{-8}`$. Including both boost signs, the largest prediction discrepancy is $`1.63\times10^{-8}`$, below $`10^{-6}`$. The smallest retained direct-root gap is $`200.55`$ times its measured error budget, above the required factor of twenty.

## Scope

The package supports the recorded finite numerical census and its independently specified multiplet prediction. Exact checks of the constant-$`T^2`$ LR ranks and the bosonic heavy-scale limit are labelled separately. It does not compute fermion norms, global harmonic multiplicities or boundary conditions, resolve the excluded critical loci, or analyze $`k\ne0`$ on $`T^2`$. The two SUSY directions are sampled polynomial-in-$`D`$ gauge directions; rank tests at finitely many generic probes do not establish a symbolic generic-rank theorem for all couplings.

The [source manifest](source_manifest.json) identifies the current repository inputs and implementation. The shared action machinery supplies the matrices; root extraction and final matching provide the spectrum checks.

## Provenance of the Table 12 residual column

The current `outputs/table.json` and per-sample records identify the repository
extraction by its parameters, interpolation and projection settings. The
saved `verification.json` identifies its checking environment and reports
positive- and negative-boost matches separately. At `(L,k)=(3,1/1000)`, the
retained positive-boost maximum is about `1.11e-8` and the all-boost maximum
about `1.63e-8`; these satisfy the unchanged `1e-6` matching criterion but
are not the paper's printed `5.2e-10`. The exact run producing that printed
column is not identified here. Alignment of the manuscript column remains
an author decision; a fresh verifier PASS does not establish reproduction
of the literal printed residuals. New run logs must retain their measured
values and environment rather than replace the historical records.
