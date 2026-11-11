# Quadratic actions and physical reduction

The [engine](../../../computations/gb_ads3_sigma2/algebra.py) retains the
background, a, b and ab grades of every metric, connection, curvature and
form. The coefficient of ab in sqrt(-g) times the complete density gives

```math
S^{(2)}_n=\mathbf b^T K_n(D,S)\mathbf a.
```

The paired AdS powers are z^D and z^(2-D); the surface powers are S and 1-S.
The frame commutators are [E2,E0,1]=E0,1/ell and [E4,E3]=w E3.
The harmonic eigenvalue is M²=v ell² S(S-1). Thus S=j+1 (or -j) on S² and
S=1/2+i nu_H on H². The constant harmonic is reduced independently because
S=0 in this local paired ansatz does not make both partners constant.

For a nonzero torus momentum, the field-strength action is taken to r=0,
w=0 while w S is held equal to (g/sqrt(2)) S_flat. The six separate
`torus_momentum_*` matrices use M²=-S_flat²/9 and physical S_flat=3iM.
Their exact divisors reproduce the generic polynomials restricted to the
torus curve. Thus neither the constant-level matrix nor a singular curved
harmonic amplitude scaling is used as a substitute for the nonzero torus mode.

| Sector | Full matrix | Generic rank | Physical divisor degree |
|---|---|---|---|
| Neutral n=2 | [1 by 1](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n2.json) | 1 | 3 |
| Neutral n=1 | [11 by 11](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n1.json) | 7 | 10 |
| Neutral n=0 | [23 by 23](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n0.json) | 14 | 10, including shadows |
| Charged n=+1 | [1 by 1](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n1Z.json) | 1 | 1 |
| Charged n=0 | [3 by 3](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n0Z.json) | 3 | 0 |
| Charged n=-1 | [1 by 1](../../../computations/gb_ads3_sigma2/outputs/branch_raw_n-1Z.json) | 1 | 1 |

Each JSON gives the exact column `avars`, row `bvars`, and every entry of K.
The neutral n=1 order is

```math
\mathbf a_1=(h_{+2},h_{+3},h_{+4},c_+,V_+,b_{+2},b_{+3},b_{+4},
e_{+23},e_{+24},e_{+34})^T.
```

The n=0 order is h_pm,h_22,h_23,h_24,h_33,h_34,h_44;
C_2,C_3,C_4; V_2,V_3,V_4; B_pm,B_23,B_24,B_34;
E_pm2,E_pm3,E_pm4,E_234; L,N. Antisymmetric component order is retained in
the b basis. The neutral scalar matrix separates into a 12 by 12 rank-nine
physical block, a 10 by 10 rank-five constraint block and one zero row/column.
Both blocks and their gauge directions are verified; the constraint block
has no D-dependent physical divisor.

## Dimension-preserving normalization

The stored branch matrices are Khat = 2 Sb K Sa/g². With u=g/sqrt(2), the
amplitude scale is u for V,Z,N, an additional sqrt(2) for E,N, and
(w/u)^p for every field with p equal to the parity of its number of surface
indices. The torus uses the unscaled surface basis. These are explicit
invertible congruences on their domains; g cancels algebraically after the
BPS substitution. The off-shell `raw_*` files retain g and lambda themselves.
For charged n=0 an additional Hermitian phase Z4=i z4 makes the certificate
matrix rational. The original complex matrix remains available.

## Exact divisor certificate

Row denominators and row content independent of D are recorded before
reduction. Over Q(L,k,S)[D], a nonzero rank-r minor M determines
A=C M R, where the pivot rows of C and pivot columns of R are identity.
Both rank factorizations are checked entry by entry; they also provide the
left and right gauge kernels. Every maximal minor satisfies

```math
\det A_{I,J}=\det C_I\,\det M\,\det R_J.
```

The gcd G of exhibited actual minors is the full physical divisor if it is
coprime in D to the denominators of C and R. This proves divisibility for
**all** maximal minors. When a chart denominator meets a physical root, the
fallback enumerates every square minor of the non-identity parts of C and R.
Since each has an identity maximal minor, the gcd of their maximal minors is
the inverse lcm of the reduced denominators. This supplies the full divisor
also for the constant torus scalar block. No random-minor stability heuristic
is used. Multiplicities, including the double flat root, are retained.

The [certificates](../../../computations/gb_ads3_sigma2/outputs/physical_n1.json)
also store gauge-invariant observables and their propagators with the
discarded row prefactors restored. A divisor alone cannot determine a norm.
Matrices for chi=-1 are separately constructed with positive ell=-ell_s;
their certified divisors equal the chi=+1 expressions under D to 2-D.

## Numerical checks of the separate invariants

The six [standalone examples](generic_levels.md) use the same unreduced
metric/form engine. W and LOG use the representatives already compared
entry by entry against the current source blocks. The
[R² adapter](../../../computations/gb_ads3_sigma2/r2_density.py) implements
G-D12, G-D13 and G-R2 of [the combined action](../../../generic_combination/action.md).
In the fixed compensator gauge its neutral triplet component and strength are

```math
\begin{aligned}
Y_0={}&-\frac R2+\frac{G^2}4-2H^2-\frac{N^2+E^2}{L^2}
+\frac{\nabla^2L}{L}-\frac{(\partial L)^2}{2L^2}-2Z\cdot\bar Z,\\
X={}&\sqrt2 E^a Z_a+i\mathcal D^a(LZ_a),\qquad
\bar X=\sqrt2 E^a\bar Z_a-i\bar{\mathcal D}^a(L\bar Z_a),\\
\boldsymbol Y^{ij}\boldsymbol Y_{ij}={}&Y_0^2+4X\bar X/L^2,\qquad
\boldsymbol{\mathcal G}=2d(E/L)+\sqrt2\,dV.
\end{aligned}
```

The charged derivatives retain V. Integrating the triplet Laplacian in
G-R2 by parts uses
∇L^{ij}·∇L_ij=(∂L)²+4L²Z·bar Z; its connection term is retained.
The independent forms, N and L are varied before inserting background
values, without imposing their auxiliary equations.

The BPS conditions p=L/√2, r=-w²,
N=-3L²/2+L(p+4h)/√2 and ell⁻²=4(h-L/(2√2))² leave h,w,ell
to be determined from the full first variation. Two independent field
equations and the radius relation are solved at 125 digits; all seven
nonzero tadpoles and the BPS equation are then checked. Retaining 115
digits gives residuals below 3×10⁻¹¹⁴ in these six examples.

Polynomial coefficients are extracted directly from the action, before
numerical root finding. Two four-projection numerical pencils supply
candidates; independent maximal projections refine them at 115 digits.
The full source matrix must lose exactly the recorded rank and recover
its generic rank at nearby D. Generic gauge singular values must be below
10⁻⁹⁰, retained singular values above 10⁻²⁰, and the rank threshold is
10⁻⁵⁵, using the recorded coefficient-based scale. At each root the
discarded singular values must be below 10⁻⁶⁵. This rejects a background
rounded to 42 digits combined with an unjustifiably strict rank threshold.
Finite-pencil diagnostics are retained; this numerical procedure is not
the exact maximal-minor certificate used for the generic symbolic GB line.
