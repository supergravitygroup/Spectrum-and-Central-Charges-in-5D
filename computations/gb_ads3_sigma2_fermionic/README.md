# GB AdS3 × Sigma2 fermionic action

This package evaluates the complete LR + GB action through two fermions
on the regular BPS family, in the primary-mode ansatz of paper Section 4.6
(repository citation 25). It supplies the
coupled gravitino and compensator matrices with full supercovariant
derivatives. Read the [component input definitions](../../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_action_inputs.md)
and [quadratic-action derivation](../../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md)
for conventions, normalization and limits.

## Reproduction

Use Python with the pinned [requirements](requirements.txt) installed in
an environment outside the repository. From the repository root:

~~~bash
python3 -B computations/gb_ads3_sigma2_fermionic/checks.py
~~~

This command is read-only. It reparses the current action, verifies source
fingerprints, reruns all 96 stored matrices and their checks, and prints
its result. A complete run takes several minutes. No external source directory,
manuscript file, executable pickle, or on-disk import cache is required.

The explicit regeneration commands write only this package's outputs:

~~~bash
python3 -B computations/gb_ads3_sigma2_fermionic/derive.py
python3 -B computations/gb_ads3_sigma2_fermionic/checks.py --write-log
~~~

Adding --sample H2_3_2_s13 to derive.py regenerates one background's
eight sectors and the term trace; --help lists the other labels.
The default regenerates all twelve points. Updating scientific outputs
requires updating their repository hash entries separately.

For another numerical point, run from this package directory:

~~~python
from action import evaluate, gauge_columns
r = evaluate(L="3", k="2", g="1", n="1/2", q_R=1,
             D=0.37+0.11j, S="1/3", trace=True)
K = r["K"]
G_epsilon, projection_error = gauge_columns(r)
~~~

All parameters are explicit caller inputs. Supply L and k as rational
values, using integer or fraction strings as above; g and S may also
contain numerical algebraic expressions. The background function can
retain symbolic L, k, g with an explicit chirality; action2.K2 uses
exact algebra. The full GB evaluate interface requires numerical
parameters and uses complex128. It does not return an analytic
all-parameter GB matrix.

## Inputs and implementation

| Files | Responsibility |
|---|---|
| [source manifest](source_manifest.json), [sources.py](sources.py), [parse_density.py](parse_density.py) | Origin and current input hashes, direct action parsing, zero-based source IDs |
| [background.py](background.py), [bgfields.py](bgfields.py) | Exact regular-family formulas and background tensors |
| [clifford.py](clifford.py), [fengine.py](fengine.py), [action2.py](action2.py) | Exact Clifford/Majorana algebra, paired mode bases and LR quadratic action |
| [ferm2.py](ferm2.py), [objects2.py](objects2.py) | Numerical Grassmann bilinears, linear spinor composites and implicit even-field bilinears |
| [deriv2.py](deriv2.py), [bderiv2.py](bderiv2.py), [second2.py](second2.py) | Q/S/K connections, corrected H02, ordered derivatives and commutators |
| [evalbg.py](evalbg.py), [eval2.py](eval2.py), [action.py](action.py) | Complete GB term contraction and normalization-preserving LR + GB assembly |
| [gauge_modes.py](gauge_modes.py) | Gauge columns from SUSY rules, without fitting a matrix kernel |
| [derive.py](derive.py), [check_derivatives.py](check_derivatives.py), [checks.py](checks.py) | Output generation, derivative identities and read-only verification |

The engine loads the current repository inputs directly. The manifest
records their hashes and the numerical implementation used for the component
contractions. Shared action code has the same evidential role in both
the action and spectrum calculations.

## Saved results

Each sample JSON contains all eight $`(n,q_R)`$ sectors, the row/column
bases, and matrices LR, W, LOG, K as real and imaginary arrays.
W is the raw $`-2W`$ contribution and LOG the raw $`-4\log`$
contribution; multiply their sum by $`-k/(2g^2)`$.
Half-spin sectors also store the two SUSY columns and residuals.

All samples use $`g=1,\ D=0.37+0.11i`$. They reproduce the background
and level choices of paper Table 12 (`tab:GBferm`), not its spectral roots:

| Output | L | k | S |
|---|---|---|---|
| [H2_3_2_s13](outputs/H2_3_2_s13.json) | 3 | 2 | 1/3 |
| [H2_3_2_s14](outputs/H2_3_2_s14.json) | 3 | 2 | 1/4 |
| [H2_5_1_algebraic](outputs/H2_5_1_algebraic.json) | 5 | 1 | 3; algebraic check only |
| [H2_7o2_1o2](outputs/H2_7o2_1o2.json) | 7/2 | 1/2 | 1/2 |
| [H2_3_1o10](outputs/H2_3_1o10.json) | 3 | 1/10 | 1/3 |
| [H2_3_1o100](outputs/H2_3_1o100.json) | 3 | 1/100 | 1/3 |
| [H2_3_1o1000](outputs/H2_3_1o1000.json) | 3 | 1/1000 | 1/3 |
| [H2_3_1o10_principal](outputs/H2_3_1o10_principal.json) | 3 | 1/10 | 1/2+1.3i |
| [H2_7o2_1_principal](outputs/H2_7o2_1_principal.json) | 7/2 | 1 | 1/2+1.3i |
| [H2_7o4_12o5_principal](outputs/H2_7o4_12o5_principal.json) | 7/4 | 12/5 | 1/2+1.3i |
| [S2_10_1o10](outputs/S2_10_1o10.json) | 10 | 1/10 | 3 |
| [S2_5_minus1](outputs/S2_5_minus1.json) | 5 | -1 | 3 |

[source_terms.json](outputs/source_terms.json) maps all 1184 original
GB terms to their expansions. [term_contributions.json](outputs/term_contributions.json)
gives all 1184 matrix contributions at the first point and
$`(n,q_R)=(1/2,+1)`$. Entries are [row_b, column_a, real, imag],
without magnitude thresholding; roundoff-sized entries remain visible.
The LR summand is organized by the (5.10) slots in lr_parts.

## Verification scope

[verification.json](outputs/verification.json) records each check's
method, residual and tolerance; [verification.log](outputs/verification.log)
is the compact run summary. The default numerical criterion is
$`\max|A-B|/\max(1,\max|A|,\max|B|)\le2\times10^{-10}`$.
Gauge products are first divided by the product of Frobenius norms.
The six/ten-node interpolation and two holdouts use $`2\times10^{-8}`$.
Four intentionally incorrect rules must instead produce a normalized
gauge residual greater than $`10^{-7}`$.

Exact checks cover background correspondence, finite Clifford and
Grassmann algebra, and the LR field-strength-block identity with free
background parameters. Numerical checks cover source-by-source GB
evaluation, all saved matrices, full derivative identities, the
FQ.26 diagonal, Majorana pairing and local-SUSY columns.
Additional points test both signs of chi, both surface curvatures and
g=3/2. A finite sample check is not a universal symbolic proof.

This package computes the quadratic action (repository citation 25). Physical roots, maximal minors, an exact generic
kernel-dimension claim, multiplet matching and fermion norms belong to
the separately stated spectrum scope. No bosonic spectrum output is used to infer
the matrices or fit their gauge directions.
