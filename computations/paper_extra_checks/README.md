# Exceptional backgrounds and the large-level norm rule

These checks cover the exceptional backgrounds stated in Sections 4.1 and
4.3, and the spin-2 norm rule at the end of Section 4.5. They use the
[existing bosonic package](../gb_ads3_sigma2/README.md) and introduce no
additional spectrum or physical claim.

From the repository root:

```sh
python3 -B computations/paper_extra_checks/exceptional_points.py
python3 -B computations/paper_extra_checks/tower_norm_rule.py
```

Both commands assert their results, print PASS lines, and leave the
repository unchanged. The first needs SymPy and SymEngine; the second
needs SymPy and mpmath. Use the environment documented in the
[front page](../../README.md).

## Exceptional backgrounds

At $`(L,k)=(2,2)`$, the regular parametrization (4.4) is undefined. The first
check substitutes the upper-sign supersymmetry conditions (4.3) into the
five undivided equations. Their only nonzero common factor is

```math
(g-2\sqrt2\,q)v-2g^2(g+2\sqrt2\,q).
```

Its zero gives the one-parameter family after Table 8. The script checks
the excluded values of $`q`$, the torus member, and the direction-dependent
limit of (4.4). The equations and coupling $`g`$ stay symbolic. An independent
check uses the complete existing action to verify its first variations at
six members, including a sphere, a hyperbolic surface and a torus; these
finite checks use $`g=1`$. Three off-family variations confirm that this
check detects non-solutions. The spectrum of this family is not computed,
as stated in the paper.

The same script checks the two regular points in Section 4.3 where
$`\mu\ell_s=\nu_f=0`$. At each, none of $`P_1,\ldots,P_5`$ vanishes and the
cubic (4.10) is exactly

```math
(D-1)\bigl[D(D-2)-M^2\bigr].
```

## Spin-2 tower

For $`L>0`$, $`k\ne0`$ and away from the excluded loci, the Section 4.5 rule
concerns **positive norm together with positive weights**. It is not a
criterion for the sign of the primary's norm alone. The script checks the
large-$`M^2`$ root and cubic derivative, and the identities

```math
\nu_f-1=\frac{2P_1P_2}{kP_3},\qquad
\nu_f+1=\frac{8(P_1+k)}{kP_3}.
```

For $`\nu_f\ne0`$, the norm has sign $`\chi k\nu_f`$ and positive weights
require $`|\nu_f|>1`$. In that domain the norm's sign is the sign of $`P_1`$.
Since $`P_2=P_1+2`$, both conditions hold precisely when $`P_1>0`$ and
$`P_1+k>0`$, equivalently $`kL<2`$ and $`k(L-1)<2`$. The script also checks the
subleading expansion at $`\nu_f=0`$ and the negative norm at $`(L,k)=(3,2)`$.
It tests the rule at 400 regular rational points with a fixed random seed,
$`M^2=10^8`$ and 60-digit arithmetic. These finite tests supplement the
algebraic sign argument.

## Inputs and provenance

The formulas are imported from [model.py](../gb_ads3_sigma2/model.py) and
[closed_forms.py](../gb_ads3_sigma2/closed_forms.py). The full-action check
calls [sectors.py](../gb_ads3_sigma2/sectors.py), which uses the existing
bosonic action. Figure scripts are documented [here](../../figures/README.md).

The checks are adapted from the supplied `extra_checks_for_student_repo`
scripts by Erol Aksoy, Cagatay Okyay, Mehmet Ozkan and Cemal Berfu Senisik
(2026), provided under MIT for code and CC BY 4.0 for documentation and
data. They are arranged around this repository's existing inputs; no
external checkout, stored pickle, or manuscript file is needed to run them.

## First-order central charges

Run `python -B computations/paper_extra_checks/first_order_vs_PRL.py` to
compare the current action-derived a and c with Gold et al.,
arXiv:2309.07637v2, Eq. (19), using the action-normalization check against
Gold et al. (2025), Eqs. (32)–(34). The
[central-charge guide](../../references/central_charge_guide.md#first-order-literature-check)
states the coupling conversion and first-order scope. The read-only command
prints exact residual checks and detection of an intentionally wrong
conversion; it runs in the normal reproduction suite.
