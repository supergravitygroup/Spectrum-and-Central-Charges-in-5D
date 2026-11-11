# Coupled fermionic quadratic action

The [component inputs](fermionic_action_inputs.md) determine a reproducible
evaluation of the complete two-fermion action on the regular BPS product
background, in v109's primary-mode ansatz. Both the gravitino diagonal
block and the gravitino–compensator mixing are included, together with
the previously available compensator diagonal. The
[package guide](../../../computations/gb_ads3_sigma2_fermionic/README.md)
gives commands, stored matrices and their precision.

## Mode pairing and matrix extraction

In the local frame

```math
\begin{aligned}
E_0&=\frac z\ell\partial_t,&
E_1&=\frac z\ell\partial_x,&
E_2&=\frac z\ell\partial_z,\\
E_3&=wy\partial_{y_1},&
E_4&=wy\partial_y,& w^2&=-v,
\end{aligned}
\tag{F24.7}
```

take frame components independent of $`t,x,y_1`$, with the two
Grassmann amplitude sets multiplying $`z^Dy^S`$ and
$`z^{2-D}y^{1-S}`$. This is the manuscript's local mode evaluation;
it does not impose a transverse or gamma-traceless gravitino gauge.
The local harmonic parameter gives
$`\lambda_\Sigma=w^2S(1-S)`$, $`M^2=\ell^2\lambda_\Sigma`$;
on the sphere $`S=j+1`$, while the principal hyperbolic series uses
$`S=\tfrac12+i\nu_H`$. Global harmonic multiplicities are not fixed
by this local representative.

The source charge and Majorana pairing give

```math
\begin{aligned}
S^{(2)}_{n,q_R}&=\mathbf b^TK_{n,q_R}(D,S)\mathbf a,&
n&=\pm\frac12,\ \pm\frac32,\qquad q_R=\pm1,\\
K_{n,q_R}&=K^{LR}_{n,q_R}
 -\frac{k}{2g^2}\bigl(K^W_{n,q_R}+K^{\log}_{n,q_R}\bigr),\\
K_{-n,-q_R}(2-D,1-S)&=-K_{n,q_R}(D,S)^T .
\end{aligned}
\tag{F24.8}
```

The final identity uses the linear Majorana bar and Grassmann order,
not a Hermitian conjugation. For a bilinear with doublet pairing P,
extraction is explicitly

```math
K_{BA}=\sum_{i,j}P_{ij}
\left[X_B^{iT}C\Gamma Y_A^j-Y_B^{jT}(C\Gamma)^TX_A^i\right].
\tag{F24.9}
```

The two terms in (F24.9) are checked against a separately assembled
two-generator exterior algebra. The mode weights cancel the measure
in a total divergence, supplying the integration-by-parts pairing.

There are four $`10\times10`$ matrices at $`n=\pm\tfrac12`$:
eight gravitino amplitudes and two compensator amplitudes in each.
There are four $`2\times2`$ matrices at $`n=\pm\tfrac32`$, containing
only gravitino amplitudes. For the first set the retained blocks are

```math
K_{n,q_R}=
\begin{pmatrix}
K_{\psi\psi}&K_{\psi\varphi}\\
K_{\varphi\psi}&K_{\varphi\varphi}
\end{pmatrix}.
\tag{F24.10}
```

The JSON files record both bases, including light-cone frame labels,
four-component spinors and SU(2) doublets; their order is exactly the
row-b/column-a order of each matrix.

## Source coverage

The evaluator parses the current GB-FINAL-DENSITY directly. It identifies
1184 top-level summands: 52 in $`-2W`$ and 1132 in $`-4\log`$.
Distributing groups gives 1190 terms; applying the bosonic Leibniz rule
gives 1198: 871 explicit bilinears, two differentiated bilinears, and
325 bosonic-form terms whose implicit bilinears are expanded.
These counts describe the representation, not a count of independent
physical couplings. The pre-Leibniz and fully expanded counts refer to these
different representations.

[source_terms.json](../../../computations/gb_ads3_sigma2_fermionic/outputs/source_terms.json)
records each original expression, its original zero-based index, its
source summand and its expansion counts. IDs
GB-FINAL-DENSITY:0000 through GB-FINAL-DENSITY:1183 identify this
fingerprinted source ordering; no existing action term IDs are renamed.
[term_contributions.json](../../../computations/gb_ads3_sigma2_fermionic/outputs/term_contributions.json)
records every original term's sparse matrix at the first sample and
$`(n,q_R)=(\tfrac12,+1)`$, before multiplication by
$`\lambda_{\mathrm{GB}}`$. Empty entries mean a zero contribution.
The checker reruns every contraction and verifies their sum against
$`K^W+K^{\log}`$.

The LR implementation separately evaluates all relevant slots of (5.10).
Its full field-strength block vanishes on this background after the
allowed total divergences are removed: it is the integrated form of
$`A_\mu P^\mu`$, with $`P^\mu=0`$. The code evaluates the block before
checking this cancellation with free $`\ell,w,g,L,N,p,h,r,D,S`$.
Replacing the derivative of the compensator bilinear by an ordinary
one leaves a nonzero symbolic residual.

## Analytic diagonal cross-check

The existing [compensator calculation, FQ.26](details/compensator_fermion.md)
is recovered as the diagonal entry, with

```math
\begin{aligned}
\ell_{\varphi\varphi}^{(2)}
 &=2A_\varphi\,\bar\varphi\mathord{\not{D}}^R\varphi
   +iP_\varphi\,\bar\varphi\gamma^{34}\varphi
   +iM_\varphi\,\delta_{ij}\bar\varphi^i\varphi^j,\\
A_\varphi&=\frac1L+\lambda_{\mathrm{GB}}g^2,\\
P_\varphi&=\frac{p-2h}{L}
          +2\lambda_{\mathrm{GB}}g^2(p-3h),\\
M_\varphi&=\sqrt2\left(2g-\frac N{L^2}\right)
          +\frac7{\sqrt2}\lambda_{\mathrm{GB}}g^3L .
\end{aligned}
\tag{F24.11}
```

Here $`D^R`$ includes the background R connection.
The checker compares (F24.11) with the extracted $`2\times2`$
compensator subblock at all stored half-spin sectors.
Setting the gravitino to zero is used only to read this entry;
it is not used in (F24.8) or (F24.10).

## Numerical results and verification

The package evaluates all eight sectors at each of the twelve
background/level choices in paper Table 12 (`tab:GBferm`): 96 full matrices,
each stored with its LR, W and LOG contributions. The common probe
is $`D=0.37+0.11i`$, not a spectral root. The API accepts other
explicit rational L, k and numerical g, D, S values in the stated domain.
The samples set $`g=1`$ explicitly. An additional check at $`g=3/2`$
verifies the expected scaling: $`K^{LR}`$ and K scale as g,
while the raw higher-derivative contributions scale as $`g^3`$.
There is no expansion in small k.

The GB contractions use double precision (complex128). The exact
LR algebra, symbolic background comparison and Clifford identities
are separately labelled. The [verification report](../../../computations/gb_ads3_sigma2_fermionic/outputs/verification.json)
records absolute residuals, scales and tolerances; its
[short log](../../../computations/gb_ads3_sigma2_fermionic/outputs/verification.log)
lists the tested groups.

The numerical checks include the full derivative identities used
by the engine, the independent ordinary-current expression (F24.6),
an alternate torsion-retaining construction of the LR scalar block,
(F24.11), Majorana pairing, and action null columns constructed directly
from the SUSY transformations. Four negative controls change the
relative GB normalization, restore the old H02 sign, omit its gauging
term, or replace the derivative in source term 17 by an ordinary one;
each must spoil the SUSY check.

A polynomial-in-D consistency check compares six-node and ten-node
numerical interpolations and two independent off-grid evaluations.
This is a finite numerical check, not a symbolic polynomial certificate.
The derivative checks share some component machinery; they do not
constitute a second independent construction of the full nonlinear action.

The $`(L,k)=(5,1)`$ hyperbolic sample with $`S=3`$ has $`M^2<0`$
and is labelled an algebraic operator check, as in the manuscript.
The three principal-series samples include both $`\chi=-1`$ cases.
The stored SUSY columns verify the required gauge directions at the
tested points; they do not certify that the generic kernel has exactly
dimension two.

The spectrum calculation (repository citation 26) remains separate: no maximal-minor root census, completeness
proof, fermion–boson multiplet matching, or fermion norm calculation
is claimed here. The matrices provide its action input. The calculation
also does not establish global multiplicities, boundary conditions,
the $`k\ne0`$ torus sector, or the excluded critical loci.
