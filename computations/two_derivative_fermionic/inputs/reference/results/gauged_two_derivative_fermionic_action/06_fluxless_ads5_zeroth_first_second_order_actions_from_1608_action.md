# Fluxless AdS5 zeroth-, first-, and second-order actions

> **Perturbation lock:** `2DER-GDW-FLUXLESS-ADS5-S0S1S2-OZKAN1608-v2`  
> **Nonlinear parent:** `05_gauged_two_derivative_full_fermionic_action_from_1608_map.md`  
> **Parent action lock:** `2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2`  
> **Status:** exact in the bosonic sector and complete through quadratic
> fermions, before any fluctuation gauge fixing or auxiliary elimination

<!-- ASSERT_PERTURBATION_LOCK: 2DER-GDW-FLUXLESS-ADS5-S0S1S2-OZKAN1608-v2 -->
<!-- ASSERT_PARENT_ACTION_LOCK: 2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2 -->
<!-- ASSERT_BACKGROUND: L=1, N=-3g/2, k=-g^2/2, fluxless=true -->
<!-- ASSERT_RAW_QUADRATIC_ACTION: gauge_unfixed=true, auxiliary_uneliminated=true -->
<!-- ASSERT_NEW_Y_TRACE: direct_2016_map=true, coefficient=-6 -->

## 1. What is calculated here

This document expands the current nonlinear gauged two-derivative action as

```math
S[\bar\Phi+\epsilon\Phi^{(1)}]
=S^{(0)}+\epsilon S^{(1)}+\epsilon^2S^{(2)}
+O(\epsilon^3).
\tag{1.1}
```

The bookkeeping number $`\epsilon`$ is not a new coupling or a new field.  It
is set to one after the coefficient of each order has been identified.  The
normalization is

```math
S^{(n)}
=\left.
\frac1{n!}\frac{d^n}{d\epsilon^n}
S[\bar\Phi+\epsilon\Phi^{(1)}]
\right|_{\epsilon=0}.
\tag{1.2}
```

The calculation stops at the raw quadratic action.  In particular, it does
not:

- impose de Donder, Lorenz, gamma-trace, transverse, or traceless gauges;
- eliminate $`N^{(1)}`$, $`E_a^{(1)}`$, $`V_a^{(1)}`$, or
  $`V_a^{\prime(1)ij}`$;
- dualize a form;
- redefine or diagonalize a field;
- use an inverse differential operator;
- infer a mass coefficient from a desired AdS representation;
- determine a spectrum.

The parent action omits cubic terms in fermionic composite slots when they
first enter the action at four-fermion order, and omits quartic action terms.
Those omissions cannot contribute to $`S^{(0)}`$, $`S^{(1)}`$, or the
quadratic-fermion part of $`S^{(2)}`$.

## 2. Source and provenance ledger

| Datum | Exact local source | Location |
| --- | --- | --- |
| nonlinear gauged action | `results/gauged_two_derivative_fermionic_action/05_gauged_two_derivative_full_fermionic_action_from_1608_map.md` | Eqs. (5.1), (5.10), and (6.21) |
| single-linear-multiplet map | `results/gauged_two_derivative_fermionic_action/03_single_linear_multiplet_linear_map_anchor.md` | lock `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2` |
| defining vector and component sum | `results/gauged_two_derivative_fermionic_action/04_defining_vector_component_anchor.md` | lock `2DER-GAUGED-VDEFINING-COMPONENTS-v2` |
| local composite used by the map | Özkan, `Sources/2016-Ozkan-Off-Shell N=2 Linear Multiplets in Five Dimensions.pdf` | Eqs. (2.15), (3.14), PDF pp. 6 and 9 |
| gauged Dilaton--Weyl data | Coomans--Özkan, `Sources/2013-Coomans-Ozkan-Internally-Gauged-D5-N2-Supergravity.pdf` | Eqs. (2.15)--(2.17), (5.2)--(5.8), PDF pp. 7--8 and 16--17 |
| density, derivatives, and dependent connections | corrected Özkan--Pang, `Sources/2013-Ozkan-Supersymmetric Completion of GB.pdf` | Eqs. (3.1)--(3.6), PDF pp. 10--11 |
| target normalization and bosonic check | Gold et al., `Sources/2025-Gold-On five-dimensional curvature squared supergravity and holography.pdf` | Eqs. (25)--(27), PDF p. 14 |

The SHA-256 hash of the nonlinear parent used in this calculation is

`6a05742d1c2bb798fcb10b973fa6045165f4ff77a302f02f42b23c3a20b7d2fe`.

## 3. Conventions

The metric and curvature conventions are

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),
\qquad
[\bar\nabla_\mu,\bar\nabla_\nu]\zeta
=\frac14\bar R_{\mu\nu}{}^{ab}\gamma_{ab}\zeta.
\tag{3.1}
```

Antisymmetrization has unit weight.  The maximally symmetric curvature is

```math
\bar R_{\mu\nu\rho\sigma}
=k\left(
\bar g_{\mu\rho}\bar g_{\nu\sigma}
-\bar g_{\mu\sigma}\bar g_{\nu\rho}
\right),
\tag{3.2}
```

```math
\bar R_{\mu\nu}=4k\bar g_{\mu\nu},
\qquad
\bar R=20k.
\tag{3.3}
```

The NW--SE convention is

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
\tag{3.4}
```

For fixed upper indices,

```math
\bar\alpha^i\gamma_{(n)}\beta^j
=t_n\bar\beta^j\gamma_{(n)}\alpha^i,
\qquad
t_0=t_1=+1,
\qquad
t_2=t_3=-1.
\tag{3.5}
```

For an NW--SE contraction, the epsilon exchange supplies one additional
minus sign:

```math
\bar\alpha^i\gamma_{(n)}\beta_i
=-t_n\bar\beta^i\gamma_{(n)}\alpha_i.
\tag{3.6}
```

The form conventions inherited from the parent are

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},
\tag{3.7}
```

```math
H_{\mu\nu\rho}
=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho},
\tag{3.8}
```

```math
H_{ab}^{\rm Gold}
=-\frac1{12}\varepsilon_{abcde}H^{cde},
\qquad
E^\mu
=-\frac1{12}e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}.
\tag{3.9}
```

## 4. Nonlinear parent kept visible

The exact bosonic density of the current parent is

```math
\boxed{
\begin{aligned}
e^{-1}\mathcal L_{\rm B}={}&
L\left(
R-\frac12G_{ab}G^{ab}
+4H_{ab}^{\rm Gold}H_{\rm Gold}^{ab}
+2V_a^{\prime\,ij}V^{\prime a}_{ij}
\right)\\
&+L^{-1}\partial_aL\partial^aL
-2L^{-1}E_aE^a
-2\sqrt2E^aV_a
-2L^{-1}N^2\\
&-4gE^aC_a
-2gLN
-4gN
-\frac12g^2L^3
+2g^2L^2.
\end{aligned}}
\tag{4.1}
```

The fermionic density is not replaced by a guessed AdS action.  Its compact
source is the one-vector BF expression

```math
\mathcal L_{2\partial}^{\rm Gold}
=-2\mathcal L_{\rm VL}
[V_{\rm linear}+2gV_{\rm defining};\mathbb L],
\tag{4.2}
```

with the four slots displayed in the nonlinear parent.  For the pure
quadratic-fermion Hessian, the field-strength slot is multiplied by
$`E^{(1)\mu\nu}`$.  Its fermion bilinear therefore starts at third
fluctuation order and does not enter the calculation below.

## 5. Fluxless maximally symmetric background

### 5.1 Ansatz

Take

```math
\begin{aligned}
&\bar G_{\mu\nu}=0,
\qquad
\bar H_{\mu\nu\rho}=0,
\qquad
\bar E_a=0,\\
&\bar V_a=0,
\qquad
\bar V_a^{\prime\,ij}=0,
\qquad
\bar C_\mu=\bar B_{\mu\nu}=\bar E_{\mu\nu\rho}=0,\\
&\bar\psi_\mu{}^i=0,
\qquad
\bar\varphi^i=0,
\qquad
\partial_\mu\bar L=0,
\qquad
\partial_\mu\bar N=0.
\end{aligned}
\tag{5.1}
```

On this ansatz, all non-curvature bosonic terms are contained in

```math
U(L,N)
=-2L^{-1}N^2
-2gLN
-4gN
-\frac12g^2L^3
+2g^2L^2.
\tag{5.2}
```

### 5.2 The $`N`$ equation

The auxiliary equation is

```math
0=\frac{\partial U}{\partial N}
=-4L^{-1}N-2gL-4g.
\tag{5.3}
```

Therefore

```math
N=-\frac g2L(L+2).
\tag{5.4}
```

No fluctuating auxiliary field has been eliminated here.  Equation (5.4) is
used only to classify the constant background.

### 5.3 The scalar equation

Varying $`L`$ before substituting (5.4) gives

```math
0
=R+2L^{-2}N^2
-2gN
-\frac32g^2L^2
+4g^2L.
\tag{5.5}
```

Using $`R=20k`$ and (5.4),

```math
0=20k+2g^2(4L+1).
\tag{5.6}
```

### 5.4 The metric equation

For constant $`L`$ and $`N`$, the metric equation is

```math
L\left(
R_{\mu\nu}-\frac12g_{\mu\nu}R
\right)
-\frac12g_{\mu\nu}U=0.
\tag{5.7}
```

After (5.4),

```math
U\big|_{N=-gL(L+2)/2}
=2g^2L(2L+1).
\tag{5.8}
```

Since the Einstein tensor of (3.2) is $`-6k\bar g_{\mu\nu}`$, Eq. (5.7)
becomes

```math
-6Lk-g^2L(2L+1)=0.
\tag{5.9}
```

For the nondegenerate branch $`g\ne0`$ and $`L\ne0`$, Eqs. (5.6) and
(5.9) give

```math
\boxed{
\bar L=1,
\qquad
\bar N=-\frac{3g}{2},
\qquad
k=-\frac{g^2}{2}.}
\tag{5.10}
```

Thus

```math
\bar R_{\mu\nu}=-2g^2\bar g_{\mu\nu},
\qquad
\bar R=-10g^2,
\qquad
\ell^2=\frac2{g^2}.
\tag{5.11}
```

The remaining bosonic equations vanish term by term on (5.1): each contains
at least one factor of $`G`$, $`H`$, $`E`$, $`V`$, $`V'`$, $`C`$, or a
derivative of a constant.  The fermionic equations are homogeneous and are
satisfied by the vanishing background fermions.

## 6. Fundamental fluctuations

No fluctuation gauge is imposed.  Expand the independent fields as

```math
g_{\mu\nu}=\bar g_{\mu\nu}+\epsilon h_{\mu\nu},
\qquad
L=1+\epsilon L^{(1)},
\qquad
N=-\frac{3g}{2}+\epsilon N^{(1)}.
\tag{6.1}
```

All fields with zero background start at first order:

```math
\begin{aligned}
C_\mu&=\epsilon C_\mu^{(1)},
&B_{\mu\nu}&=\epsilon B_{\mu\nu}^{(1)},
&E_{\mu\nu\rho}&=\epsilon E_{\mu\nu\rho}^{(1)},\\
V_\mu&=\epsilon V_\mu^{(1)},
&V'_\mu{}^{ij}&=\epsilon V_\mu^{\prime(1)ij},
&\psi_\mu{}^i&=\epsilon\psi_\mu^{(1)i},\\
&&\varphi^i&=\epsilon\varphi^{(1)i}.
\end{aligned}
\tag{6.2}
```

The first-order field strengths are

```math
G_{\mu\nu}^{(1)}
=2\bar\nabla_{[\mu}C_{\nu]}^{(1)},
\tag{6.3}
```

```math
H_{\mu\nu\rho}^{(1)}
=3\bar\nabla_{[\mu}B_{\nu\rho]}^{(1)}
+\frac g2E_{\mu\nu\rho}^{(1)},
\tag{6.4}
```

```math
E^{(1)a}
=-\frac1{12}\bar\varepsilon^{abcde}
\bar\nabla_bE_{cde}^{(1)}.
\tag{6.5}
```

The $`C\wedge G`$ term in the nonlinear $`H`$ is second order.  Because
$`\bar H=0`$, it first affects $`H^2`$ at third order and is absent from
$`S^{(2)}`$.

The resulting order ledger is:

| Nonlinear structure | Order zero | Order one | Order two |
| --- | --- | --- | --- |
| $`eLR`$ | $`\bar e\,\bar R`$ | metric and $`L^{(1)}`$ tadpoles | metric Hessian and $`L^{(1)}R^{(1)}`$ |
| $`eU(L,N)`$ | $`\bar e\,U_0`$ | $`h`$ and $`L^{(1)}`$ tadpoles | $`h^2`$, $`hL^{(1)}`$, $`L^{(1)2}`$, $`L^{(1)}N^{(1)}`$, $`N^{(1)2}`$ |
| $`eL^{-1}(\partial L)^2`$ | zero | zero | $`(\bar\nabla L^{(1)})^2`$ |
| $`G^2,H^2,E^2,E\cdot V,E\cdot C,V'^2`$ | zero | zero | squares or bilinear mixings of first-order fields |
| every retained fermion bilinear | zero | zero | background coefficient times two first-order fermions |

Metric or scalar corrections multiplying a row that already begins at
second order contribute only at third order.  This is why no hidden
$`h\bar\varphi\varphi`$, $`L^{(1)}G^{(1)2}`$, or
$`N^{(1)}\bar\psi^{(1)}\psi^{(1)}`$ term belongs to $`S^{(2)}`$.

## 7. Metric expansion without a gauge choice

Indices on fluctuations are raised with $`\bar g_{\mu\nu}`$, and
$`h=\bar g^{\mu\nu}h_{\mu\nu}`$.  Direct multiplication gives

```math
g^{\mu\nu}
=\bar g^{\mu\nu}
-\epsilon h^{\mu\nu}
+\epsilon^2h^\mu{}_{\rho}h^{\rho\nu}
+O(\epsilon^3).
\tag{7.1}
```

Using $`\delta\ln e=\tfrac12g^{\mu\nu}\delta g_{\mu\nu}`$,

```math
e=\bar e\left[
1+\frac\epsilon2h
+\epsilon^2\left(
\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}
\right)
\right]+O(\epsilon^3).
\tag{7.2}
```

The connection coefficients are

```math
\Gamma^{(1)\rho}_{\mu\nu}
=\frac12\left(
\bar\nabla_\mu h^\rho{}_\nu
+\bar\nabla_\nu h^\rho{}_\mu
-\bar\nabla^\rho h_{\mu\nu}
\right),
\tag{7.3}
```

```math
\Gamma^{(2)\rho}_{\mu\nu}
=-\frac12h^{\rho\lambda}\left(
\bar\nabla_\mu h_{\lambda\nu}
+\bar\nabla_\nu h_{\lambda\mu}
-\bar\nabla_\lambda h_{\mu\nu}
\right).
\tag{7.4}
```

Hence

```math
R_{\mu\nu}^{(1)}
=\bar\nabla_\rho\Gamma^{(1)\rho}_{\mu\nu}
-\bar\nabla_\nu\Gamma^{(1)\rho}_{\mu\rho},
\tag{7.5}
```

```math
\begin{aligned}
R_{\mu\nu}^{(2)}={}&
\bar\nabla_\rho\Gamma^{(2)\rho}_{\mu\nu}
-\bar\nabla_\nu\Gamma^{(2)\rho}_{\mu\rho}\\
&+\Gamma^{(1)\rho}_{\rho\lambda}
\Gamma^{(1)\lambda}_{\mu\nu}
-\Gamma^{(1)\rho}_{\nu\lambda}
\Gamma^{(1)\lambda}_{\mu\rho}.
\end{aligned}
\tag{7.6}
```

The scalar-curvature coefficients are

```math
R^{(1)}
=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h
-4kh,
\tag{7.7}
```

```math
R^{(2)}
=\bar g^{\mu\nu}R_{\mu\nu}^{(2)}
-h^{\mu\nu}R_{\mu\nu}^{(1)}
+4k h_{\mu\nu}h^{\mu\nu}.
\tag{7.8}
```

For later compactness, the explicitly defined linearized cosmological
Einstein tensor is

```math
\mathcal G_{\mu\nu}^{(1)}(h)
=R_{\mu\nu}^{(1)}
-\frac12\bar g_{\mu\nu}R^{(1)}
-4k h_{\mu\nu}.
\tag{7.9}
```

This is only the standard local tensor written out in (7.9).  It is not a
new field, a projection operator, or an inverse operator.

## 8. Zeroth-order action

At the background,

```math
\bar L\bar R=-10g^2,
\qquad
U(1,-3g/2)=6g^2.
\tag{8.1}
```

All other terms in (4.1) vanish.  Therefore

```math
\boxed{
S^{(0)}=-4g^2\int d^5x\,\bar e.}
\tag{8.2}
```

This is the unrenormalized bulk value.  No AdS boundary counterterm is being
added in this local fluctuation calculation.

## 9. First-order action and tadpole cancellation

The curvature block gives

```math
\left.eLR\right|_{\epsilon}
=\bar e\left[
R^{(1)}+\bar R L^{(1)}+\frac12\bar R h
\right].
\tag{9.1}
```

The potential derivatives on the background are

```math
U_N\big|_0=0,
\qquad
U_L\big|_0=10g^2,
\qquad
U\big|_0=6g^2.
\tag{9.2}
```

Thus

```math
\left.eU\right|_{\epsilon}
=\bar e\left[
10g^2L^{(1)}+3g^2h
\right].
\tag{9.3}
```

Since $`\bar R=-10g^2`$, the $`L^{(1)}`$ terms cancel.  The remainder is

```math
\bar e\left(R^{(1)}-2g^2h\right).
\tag{9.4}
```

Using $`k=-g^2/2`$ in (7.7),

```math
R^{(1)}-2g^2h
=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h.
\tag{9.5}
```

Hence

```math
\boxed{
S^{(1)}
=\int d^5x\,\bar e\left(
\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h
\right)
\doteq0.}
\tag{9.6}
```

The equality $`\doteq0`$ means equality modulo the displayed total
derivative.  Every other bosonic field has zero background and occurs at
least quadratically.  Every retained fermion term is bilinear, so fermions
also make no contribution to $`S^{(1)}`$.

## 10. Bosonic second-order action

### 10.1 Potential Hessian

Substituting (6.1) directly into (5.2) gives

```math
\begin{aligned}
U={}&6g^2
+10\epsilon g^2L^{(1)}\\
&+\epsilon^2\left[
-4g^2\left(L^{(1)}\right)^2
-8gL^{(1)}N^{(1)}
-2\left(N^{(1)}\right)^2
\right]
+O(\epsilon^3).
\end{aligned}
\tag{10.1}
```

Multiplying by (7.2), the complete quadratic potential density is

```math
\begin{aligned}
\left.eU\right|_{\epsilon^2}
=\bar e\Bigg[&
-4g^2\left(L^{(1)}\right)^2
-8gL^{(1)}N^{(1)}
-2\left(N^{(1)}\right)^2\\
&+5g^2hL^{(1)}
+\frac34g^2h^2
-\frac32g^2h_{\mu\nu}h^{\mu\nu}
\Bigg].
\end{aligned}
\tag{10.2}
```

### 10.2 Curvature and scalar blocks

The exact second-order coefficient of $`eLR`$ is

```math
\begin{aligned}
\left.eLR\right|_{\epsilon^2}
=\bar e\Bigg[&
R^{(2)}
+\left(L^{(1)}+\frac12h\right)R^{(1)}\\
&+\bar R\left(
\frac12hL^{(1)}
+\frac18h^2
-\frac14h_{\mu\nu}h^{\mu\nu}
\right)
\Bigg].
\end{aligned}
\tag{10.3}
```

The $`hL^{(1)}`$ term in (10.3) is
$`-5g^2hL^{(1)}`$, and it cancels the corresponding
$`+5g^2hL^{(1)}`$ term in (10.2).  The remaining pure-metric terms combine,
after one integration by parts, as

```math
\left.(eLR+eU)\right|_{h^2}
\doteq
-\frac12\bar e\,
h^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h).
\tag{10.4}
```

The metric--scalar mixing is not removed:

```math
\left.(eLR+eU)\right|_{hL^{(1)}}
=\bar e\,L^{(1)}R^{(1)}.
\tag{10.5}
```

Finally,

```math
\left.eL^{-1}(\partial L)^2\right|_{\epsilon^2}
=\bar e\,
\bar\nabla_\mu L^{(1)}\bar\nabla^\mu L^{(1)}.
\tag{10.6}
```

### 10.3 Vector, form, and connection blocks

Because every field in this subsection has zero background, corrections
from $`e`$, $`L`$, and the inverse metric would raise the order beyond two.
Thus

```math
\left.-\frac12eLG^2\right|_{\epsilon^2}
=-\frac12\bar e\,
G_{\mu\nu}^{(1)}G^{(1)\mu\nu},
\tag{10.7}
```

```math
\left.2eLV'^2\right|_{\epsilon^2}
=2\bar e\,
V_a^{\prime(1)ij}V^{\prime(1)a}_{ij},
\tag{10.8}
```

```math
\left.-2eL^{-1}E^2\right|_{\epsilon^2}
=-2\bar e\,E_a^{(1)}E^{(1)a},
\tag{10.9}
```

```math
\left.-2\sqrt2eE\mathbin{\cdot}V\right|_{\epsilon^2}
=-2\sqrt2\bar e\,E^{(1)a}V_a^{(1)},
\tag{10.10}
```

```math
\left.-4geE\mathbin{\cdot}C\right|_{\epsilon^2}
=-4g\bar e\,E^{(1)a}C_a^{(1)}.
\tag{10.11}
```

For the three-form, use (3.9) and the Lorentzian epsilon contraction:

```math
\begin{aligned}
4H_{ab}^{\rm Gold(1)}H_{\rm Gold}^{(1)ab}
={}&\frac4{12^2}
\varepsilon_{abcde}\varepsilon^{abfgh}
H^{(1)cde}H_{fgh}^{(1)}\\
={}&\frac4{144}(-2!\,3!)
H_{cde}^{(1)}H^{(1)cde}\\
={}&-\frac13
H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}.
\end{aligned}
\tag{10.12}
```

Therefore

```math
\left.4eLH_{ab}^{\rm Gold}H_{\rm Gold}^{ab}\right|_{\epsilon^2}
=-\frac13\bar e\,
H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}.
\tag{10.13}
```

### 10.4 Collected bosonic result

Combining (10.2)--(10.13) gives

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{\rm B}^{(2)}\doteq{}&
-\frac12h^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h)
+L^{(1)}R^{(1)}
+\bar\nabla_\mu L^{(1)}\bar\nabla^\mu L^{(1)}\\
&-4g^2\left(L^{(1)}\right)^2
-8gL^{(1)}N^{(1)}
-2\left(N^{(1)}\right)^2\\
&-\frac12G_{\mu\nu}^{(1)}G^{(1)\mu\nu}
-\frac13H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}\\
&-2E_a^{(1)}E^{(1)a}
-2\sqrt2E^{(1)a}V_a^{(1)}
-4gE^{(1)a}C_a^{(1)}\\
&+2V_a^{\prime(1)ij}V^{\prime(1)a}_{ij}.
\end{aligned}}
\tag{10.14}
```

No algebraic equation for a first-order field has been used in (10.14).

## 11. Fermionic ingredients at first fluctuation order

Every fermion bilinear in the nonlinear action contributes to
$`S^{(2)}`$ with its bosonic coefficient evaluated on (5.10).  Metric,
scalar, and auxiliary fluctuations multiplying an existing fermion bilinear
would be third order.

### 11.1 Dependent $`S`$-connection

At zero form flux,

```math
\widehat R_{\mu\nu}^{\prime(1)i}(Q)
=2\bar\nabla_{[\mu}\psi_{\nu]}^{(1)i}.
\tag{11.1}
```

The source connection is

```math
\phi_\mu^{(1)i}
=\frac i3\gamma^a
\widehat R_{\mu a}^{\prime(1)i}(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}
\widehat R_{ab}^{\prime(1)i}(Q).
\tag{11.2}
```

Taking its gamma trace gives

```math
\begin{aligned}
\gamma^\mu\phi_\mu^{(1)i}
&=i\left(\frac13-\frac5{24}\right)
\gamma^{\mu\nu}\widehat R_{\mu\nu}^{\prime(1)i}(Q)\\
&=\frac i8\gamma^{\mu\nu}
\left(
\bar\nabla_\mu\psi_\nu^{(1)i}
-\bar\nabla_\nu\psi_\mu^{(1)i}
\right)\\
&=\frac i4\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)i}.
\end{aligned}
\tag{11.3}
```

### 11.2 The gauge-fixed defining gaugino has a nonzero derivative

The defining-vector auxiliary is

```math
Y^{ij}\big|_0
=-\frac g2L^{ij}\big|_0
=-\frac{g}{2\sqrt2}\delta^{ij}.
\tag{11.4}
```

Although the defining gaugino itself is gauge fixed to zero, its derivative
contains $`+Y^{ij}\psi_{\mu j}`$.  Hence

```math
\boxed{
\mathcal D_\mu\psi^i\big|^{(1)}
=-\phi_\mu^{(1)i}
-\frac{g}{2\sqrt2}\delta^{ij}
\psi_{\mu j}^{(1)}.}
\tag{11.5}
```

Lowering must be done with epsilon:

```math
\begin{aligned}
\left(
-\frac{g}{2\sqrt2}\delta^{rj}\psi_{\mu j}^{(1)}
\right)\varepsilon_{ri}
&=+\frac{g}{2\sqrt2}\delta_{ij}
\psi_\mu^{(1)j}.
\end{aligned}
\tag{11.6}
```

### 11.3 $`\chi^i`$, $`\mathcal D_\mu\varphi_i`$, and
$`\lambda_{{\rm linear}\,i}`$

Equations (11.3) and (11.5) give

```math
\boxed{
\chi^{(1)i}
=\frac1{32}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)i}
-\frac{ig}{16\sqrt2}\delta^{ij}
\gamma^\mu\psi_{\mu j}^{(1)}
+\frac g8\varphi^{(1)i}.}
\tag{11.7}
```

The correctly lowered linear-multiplet derivative is

```math
\boxed{
\mathcal D_\mu\varphi_i\big|^{(1)}
=\bar\nabla_\mu\varphi_i^{(1)}
+\frac{3g}{4}\psi_{\mu i}^{(1)}
+\frac3{\sqrt2}\delta_{ij}\phi_\mu^{(1)j}.}
\tag{11.8}
```

The upper-index formula is not obtained by copying the last sign.  Raising
the complete lower-index equation gives

```math
\boxed{
\mathcal D_\mu\varphi^i\big|^{(1)}
=\bar\nabla_\mu\varphi^{(1)i}
+\frac{3g}{4}\psi_\mu^{(1)i}
-\frac3{\sqrt2}\delta^{ij}\phi_{\mu j}^{(1)}.}
\tag{11.9}
```

The two non-derivative coefficients in (11.8) follow from

```math
-\frac12\bar N=\frac{3g}{4},
\qquad
-3L^{rj}\phi_{\mu j}\varepsilon_{ri}
=+\frac3{\sqrt2}\delta_{ij}\phi_\mu{}^j.
\tag{11.10}
```

Insert (11.7)--(11.8) into the active 2016 spinor slot.  The result is

```math
\boxed{
\begin{aligned}
\lambda_{{\rm linear}\,i}^{(1)}={}&
-2i\not{\bar\nabla}\varphi_i^{(1)}
+\sqrt2\delta_{ij}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-2ig\gamma^\mu\psi_{\mu i}^{(1)}
+\frac{5g}{\sqrt2}\delta_{ij}\varphi^{(1)j}.
\end{aligned}}
\tag{11.11}
```

The coefficients are obtained before using any fermion equation:

```math
-2i\left(\frac{3g}{4}\right)
-\frac{ig}{2}
=-2ig,
\tag{11.12}
```

```math
-2i\left(\frac3{\sqrt2}\right)
-i\sqrt2
=-4\sqrt2i,
\tag{11.13}
```

```math
-4\sqrt2i\,\delta_{ij}\gamma^\mu\phi_\mu^{(1)j}
=\sqrt2\delta_{ij}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j},
\tag{11.14}
```

```math
-\sqrt2\bar N+\sqrt2g
=\frac{3g}{\sqrt2}+\frac{2g}{\sqrt2}
=\frac{5g}{\sqrt2}.
\tag{11.15}
```

## 12. Direct trace of the active 2016 triplet slot

This section is the point at which the current calculation differs from the
alternative representation. No Fierz-reordered $`Y_{ij}`$ is used.

At the background, the triplet density is

```math
\left.
-2\frac{L}{\sqrt2}\delta^{ij}
Y_{{\rm linear}\,ij}
\right|_0
=-\sqrt2\,\delta^{ij}
Y_{{\rm linear}\,ij}.
\tag{12.1}
```

### 12.1 The two explicit $`N\varphi^2`$ terms

The active 2016 map contains

```math
iN\bar\varphi_{(i}\varphi_{j)}
-\frac{3i}{2}N\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l.
\tag{12.2}
```

The two trace identities are

```math
\delta^{ij}\bar\varphi_{(i}\varphi_{j)}
=\delta_{kl}\bar\varphi^k\varphi^l,
\tag{12.3}
```

```math
\delta^{ij}\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l
=2\delta_{kl}\bar\varphi^k\varphi^l.
\tag{12.4}
```

Therefore (12.1) gives

```math
\begin{aligned}
&-\sqrt2\delta^{ij}
\left[
i\bar N\bar\varphi_{(i}^{(1)}\varphi_{j)}^{(1)}
-\frac{3i}{2}\bar N\delta_{ij}\delta^{kl}
\bar\varphi_k^{(1)}\varphi_l^{(1)}
\right]\\
&=-\sqrt2\left(i\bar N-3i\bar N\right)
\delta_{kl}\bar\varphi^{(1)k}\varphi^{(1)l}\\
&=2\sqrt2i\bar N\,
\delta_{kl}\bar\varphi^{(1)k}\varphi^{(1)l}\\
&=-\frac{6ig}{\sqrt2}\,
\delta_{kl}\bar\varphi^{(1)k}\varphi^{(1)l}.
\end{aligned}
\tag{12.5}
```

The coefficient $`-6`$ has thus been calculated directly from the active
2016 map.  It is not imposed as a representation-theory consistency
condition.

### 12.2 The two $`\chi\varphi`$ terms cancel in the trace

The relevant terms are

```math
-16i\bar\chi_{(i}\varphi_{j)}
+8i\delta_{ij}\delta_{kl}\bar\chi^k\varphi^l.
\tag{12.6}
```

First derive, rather than assume, the equality of their scalar contractions:

```math
\begin{aligned}
\delta^{ij}\bar\chi_i\varphi_j
&=\delta^{ij}
\left(\bar\chi^m\varepsilon_{mi}\right)
\left(\varphi^n\varepsilon_{nj}\right)\\
&=\delta_{mn}\bar\chi^m\varphi^n.
\end{aligned}
\tag{12.7}
```

Consequently,

```math
\begin{aligned}
\delta^{ij}\Big(
-16i\bar\chi_{(i}\varphi_{j)}
+8i\delta_{ij}\delta_{kl}\bar\chi^k\varphi^l
\Big)
&=(-16i+16i)
\delta_{kl}\bar\chi^k\varphi^l\\
&=0.
\end{aligned}
\tag{12.8}
```

Thus no $`\chi\varphi`$ term is left in the traced density.  This
cancellation must be performed before inserting (11.7).

### 12.3 The explicit derivative-of-$`\varphi`$ term

The active triplet contains

```math
\sqrt2\delta_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}.
\tag{12.9}
```

Its contribution to (12.1) is

```math
-2\bar\varphi^{(1)i}
\not{\mathcal D}\varphi_i\big|^{(1)}.
\tag{12.10}
```

Using (11.8), the contracted rank-one flip (3.6), and (11.3),

```math
\begin{aligned}
(12.10)={}&
-2\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+\frac{3g}{2}
\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}\\
&-\frac{3i\sqrt2}{4}\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}.
\end{aligned}
\tag{12.11}
```

For example, the last coefficient is

```math
-2\left(\frac3{\sqrt2}\right)
\left(\frac i4\right)
=-\frac{3i\sqrt2}{4}.
\tag{12.12}
```

### 12.4 Conformal-box and $`D`$ block

The remaining fermionic trace comes only from the conformal box and the
$`2\sqrt2\delta_{ij}D`$ term.  Before reduction, their contribution is

```math
-2\left[
L_{ij}\square^CL^{ij}+4D
\right]_{\bar L=1,\;\text{two fermions}}.
\tag{12.13}
```

The two source expressions inserted into (12.13) are, with all background
values already shown,

```math
\begin{aligned}
\left.L_{ij}\square^CL^{ij}\right|_{\text{two fermions}}
={}&\frac1{\sqrt2}\delta_{ij}\bar\nabla^a
\left[
-i\varepsilon^{ik}\varepsilon^{j\ell}
\bar\psi_{a(k}^{(1)}\varphi_{\ell)}^{(1)}
\right]\\
&+6f_a{}^{a(2)}
-\frac i{\sqrt2}\delta_{ij}
\bar\psi^{(1)ai}
\mathcal D_a\varphi^j\big|^{(1)}\\
&-6\bar\psi_a^{(1)i}\gamma^a\chi_i^{(1)}
+\frac1{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\gamma^a\phi_a^{(1)j}.
\end{aligned}
\tag{12.14}
```

After substituting (11.5) into the parent expression for $`D`$,

```math
\begin{aligned}
D\big|_{\text{two fermions}}={}&
\frac12f_a{}^{a(2)}
+\frac i8\bar\psi_a^{(1)i}\phi^{(1)ar}\varepsilon_{ri}\\
&+\frac i{16}\bar\psi_a^{(1)i}
\gamma^a\gamma^\mu\phi_\mu^{(1)r}\varepsilon_{ri}\\
&+\frac{ig}{16\sqrt2}
\bar\psi_a^{(1)i}\delta^{rs}
\psi^{(1)a}{}_s\varepsilon_{ri}\\
&+\frac{ig}{32\sqrt2}
\bar\psi_a^{(1)i}\gamma^a\gamma^\mu
\delta^{rs}\psi_{\mu s}^{(1)}\varepsilon_{ri}\\
&-\frac g{16}
\bar\psi_a^{(1)i}\gamma^a\varphi_i^{(1)}.
\end{aligned}
\tag{12.15}
```

Now insert (11.2), (11.7), (11.8)--(11.9), (12.14), and (12.15) into
(12.13).  The dependent $`f_\mu{}^a`$ is replaced by its source definition
in terms of the project-corrected primed Lorentz curvature.  The reductions
use

```math
\gamma^\mu\gamma^{\alpha\beta}
=\gamma^{\mu\alpha\beta}
+2\bar g^{\mu[\alpha}\gamma^{\beta]},
\qquad
\gamma^\mu\phi_\mu^{(1)i}
=\frac i4\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)i}.
\tag{12.16}
```

The algebraic part requires the full Ricci contraction, not a guessed
gravitino mass coefficient. With the project-corrected chi curvature,

```math
R'|_\chi=8\frac{1-5-5+1}{4}\bar\psi_a\gamma^a\chi
=-16\bar\psi_a\gamma^a\chi,
\qquad f_a{}^a|_\chi=+\bar\psi_a\gamma^a\chi.
\tag{12.16a}
```

The f and explicit box-chi terms in (12.13) therefore combine to
$`(-16+12)\bar\psi\gamma\chi=-4\bar\psi\gamma\chi`$.
In units ig/sqrt(2), their rank-two and scalar gravitino coefficients are
(-1/4,-1/4). The explicit terms in -8D give (+1/4,+3/4), while the
N-dependent box derivative gives (0,+3/2). Thus their sum is (0,2).
The mixed coefficient is (-4)(g/8)+g/2=0. Equations (A10)–(A12) of
`08_claude_audit_corrections_and_verification.md` display every contraction.

Keeping the fermion order fixed and integrating only total derivatives gives

```math
\begin{aligned}
(12.13)\doteq{}&
+\bar\psi^{(1)\mu i}\gamma^\nu
\bar\nabla_\mu\psi_{\nu i}^{(1)}
-\bar\psi^{(1)\mu i}
\not{\bar\nabla}\psi_{\mu i}^{(1)}\\
&+\frac{15i\sqrt2}{4}\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\bar\nabla^\mu
\psi_\mu^{(1)j}\\
&+\frac{2ig}{\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\psi^{(1)\mu j}.
\end{aligned}
\tag{12.17}
```

No fermion equation, gamma-trace gauge, or representation input is used in
(12.17). Its mixed coefficient vanishes only after the explicit -g/16
term in D is included. Setting the defining-gaugino derivative to zero
would not reproduce the individual contributions above.

### 12.5 Complete triplet contribution

Adding (12.5), (12.8), (12.11), and (12.17) gives

```math
\boxed{
\begin{aligned}
\mathcal L_{Y}^{(2)}/\bar e\doteq{}&
+\bar\psi^{(1)\mu i}\gamma^\nu
\bar\nabla_\mu\psi_{\nu i}^{(1)}
-\bar\psi^{(1)\mu i}
\not{\bar\nabla}\psi_{\mu i}^{(1)}\\
&-2\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+3i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\bar\nabla^\mu
\psi_\mu^{(1)j}\\
&+\frac{2ig}{\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\psi^{(1)\mu j}\\
&+\frac{3g}{2}
\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}
-\frac{6ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{12.18}
```

This is the direct trace of the new triplet slot, not a coefficient inferred
from the final quadratic action.

## 13. The other three fermionic density blocks

### 13.1 The Majorana-barred composite-gaugino block

Raise the lower index of (11.11) before taking the source Majorana bar:

```math
\bar\lambda_{\rm linear}{}^i
=\overline{\left(
\varepsilon^{ir}\lambda_{{\rm linear}\,r}
\right)}.
\tag{13.1}
```

The source bar is transpose times C, not an antilinear operation on the
displayed coefficients. In particular,

```math
\overline{-2ig\gamma^\mu\psi_\mu^i}
=-2ig\bar\psi_\mu^i\gamma^\mu,
\qquad (-2i)(-2ig)=-4g.
\tag{13.1a}
```

This follows from the source Appendix A (A.4), (A.9), detailed in the audit
correction note (A6)–(A9). Term-by-term conjugation gives

```math
\boxed{
\begin{aligned}
-2i\bar\lambda_{\rm linear}^{(1)i}
\varphi_i^{(1)}\doteq{}&
+4\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&-2i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-4g\bar\psi_\mu^{(1)i}
\gamma^\mu\varphi_i^{(1)}\\
&+\frac{10ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{13.2}
```

The last sign can be seen without any spinor flip:

```math
\varepsilon^{ir}\varepsilon_{ki}
=-\delta^r{}_k,
\tag{13.3}
```

```math
\begin{aligned}
-2i\,
\overline{\left(
\varepsilon^{ir}\frac{5g}{\sqrt2}
\delta_{rj}\varphi^{(1)j}
\right)}
\varphi^{(1)k}\varepsilon_{ki}
=\frac{10ig}{\sqrt2}\delta_{jk}
\bar\varphi^{(1)j}\varphi^{(1)k}.
\end{aligned}
\tag{13.4}
```

### 13.2 The explicit gravitino--gaugino block

Inserting (11.11) into

```math
\frac1{\sqrt2}\delta_{ij}
\bar\psi_a^{(1)i}\gamma^a
\lambda_{\rm linear}^{(1)j}
\tag{13.5}
```

and using

```math
\gamma^\mu\gamma^{\alpha\beta}
=\gamma^{\mu\alpha\beta}
+\bar g^{\mu\alpha}\gamma^\beta
-\bar g^{\mu\beta}\gamma^\alpha
\tag{13.6}
```

gives

```math
\boxed{
\begin{aligned}
\mathcal L_{\psi\lambda}^{(2)}/\bar e\doteq{}&
-\bar\psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}^{(1)}\\
&-\bar\psi^{(1)\mu i}\gamma^\nu
\bar\nabla_\mu\psi_{\nu i}^{(1)}
+\bar\psi^{(1)\mu i}
\not{\bar\nabla}\psi_{\mu i}^{(1)}\\
&+i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&+i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\bar\nabla^\mu
\psi_\mu^{(1)j}\\
&-\frac{2ig}{\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\gamma^{\mu\nu}
\psi_\nu^{(1)j}\\
&-\frac{2ig}{\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\psi^{(1)\mu j}\\
&-\frac{5g}{2}
\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}.
\end{aligned}}
\tag{13.7}
```

For clarity, the two derivative terms in the third and fourth lines arise
from

```math
\bar\psi_\mu\gamma^\mu\gamma^\nu
\bar\nabla_\nu\varphi
=\bar\psi^\nu\bar\nabla_\nu\varphi
+\bar\psi_\mu\gamma^{\mu\nu}
\bar\nabla_\nu\varphi,
\tag{13.8}
```

followed by integration by parts and the rank-zero and rank-two fixed-index
flip rules.  This produces the displayed
$`\bar\varphi\bar\nabla\mathbin{\cdot}\psi`$ and
$`\bar\varphi\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu`$ terms with the same
sign.

### 13.3 The scalar-slot block

At the background,

```math
\rho_{\rm eff}^{(0)}
=2\bar N+2g=-g,
\qquad
\rho_{\rm eff}^{(2)}\big|_{\varphi^2}
=\frac i{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\tag{13.9}
```

The scalar-slot part of the density is

```math
-2\rho_{\rm eff}
\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\right).
\tag{13.10}
```

Keeping only pure fermion bilinears gives

```math
\boxed{
\begin{aligned}
\mathcal L_\rho^{(2)}/\bar e={}&
+g\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}\\
&+\frac{ig}{2\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\gamma^{\mu\nu}
\psi_\nu^{(1)j}\\
&+\frac{3ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{13.11}
```

For the last line,

```math
-2\left(\frac i{\sqrt2}\right)\bar N
=-2\left(\frac i{\sqrt2}\right)
\left(-\frac{3g}{2}\right)
=\frac{3ig}{\sqrt2}.
\tag{13.12}
```

## 14. Fermionic coefficient collection

The four independently calculated blocks are (12.18), (13.2), (13.7), and
(13.11).  Their coefficient sums are displayed before the final result.

The non-Rarita--Schwinger gravitino derivatives cancel:

```math
\begin{aligned}
&\left(+1\right)
\bar\psi^\mu\gamma^\nu\bar\nabla_\mu\psi_\nu
+\left(-1\right)
\bar\psi^\mu\gamma^\nu\bar\nabla_\mu\psi_\nu=0,\\
&\left(-1\right)
\bar\psi^\mu\not{\bar\nabla}\psi_\mu
+\left(+1\right)
\bar\psi^\mu\not{\bar\nabla}\psi_\mu=0.
\end{aligned}
\tag{14.1}
```

The spinor kinetic coefficient is

```math
-2+4=2.
\tag{14.2}
```

The rank-two derivative mixing coefficient is

```math
3i\sqrt2-2i\sqrt2+i\sqrt2
=2i\sqrt2.
\tag{14.3}
```

The divergence mixing cancels:

```math
-i\sqrt2+i\sqrt2=0.
\tag{14.4}
```

The gamma-trace gravitino mass coefficient is

```math
0-\frac{2ig}{\sqrt2}
+\frac{ig}{2\sqrt2}
=-\frac{3ig}{2\sqrt2}.
\tag{14.5}
```

The algebraic trace $`\delta_{ij}\bar\psi_\mu^i\psi^{\mu j}`$ cancels:

```math
\frac{2ig}{\sqrt2}
-\frac{2ig}{\sqrt2}=0.
\tag{14.6}
```

The algebraic gravitino--spinor mixing does not cancel:

```math
+\frac{3g}{2}-4g-\frac{5g}{2}+g=-4g.
\tag{14.7}
```

Finally, the algebraic spinor coefficient is

```math
\boxed{
-\frac{6ig}{\sqrt2}
+\frac{10ig}{\sqrt2}
+\frac{3ig}{\sqrt2}
=\frac{7ig}{\sqrt2}.}
\tag{14.8}
```

The three entries in (14.8) come respectively from the directly traced
2016 $`Y_{ij}`$, the Majorana-barred $`\lambda_i`$ slot, and the
$`\rho N`$ slot.  This is a forward expansion of the nonlinear action.

Therefore

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{\rm F}^{(2)}\doteq{}&
-\bar\psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}^{(1)}\\
&+2\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+2i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\gamma^{\mu\nu}
\psi_\nu^{(1)j}\\
&-4g\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}\\
&+\frac{7ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{14.9}
```

Equation (14.9) is raw: no gamma-trace gauge, fermionic field redefinition,
or fermionic equation has been used.

## 15. Complete zeroth-, first-, and second-order actions

The answers are

```math
\boxed{
S^{(0)}=-4g^2\int d^5x\,\bar e,}
\tag{15.1}
```

```math
\boxed{
S^{(1)}
=\int d^5x\,\bar e\left(
\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h
\right)
\doteq0,}
\tag{15.2}
```

and

```math
\boxed{
S^{(2)}
=\int d^5x\,\bar e\left(
\bar e^{-1}\mathcal L_{\rm B}^{(2)}
+\bar e^{-1}\mathcal L_{\rm F}^{(2)}
\right),}
\tag{15.3}
```

where the complete expressions are

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L^{(2)}\doteq{}&
-\frac12h^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h)
+L^{(1)}R^{(1)}
+\bar\nabla_\mu L^{(1)}\bar\nabla^\mu L^{(1)}\\
&-4g^2\left(L^{(1)}\right)^2
-8gL^{(1)}N^{(1)}
-2\left(N^{(1)}\right)^2\\
&-\frac12G_{\mu\nu}^{(1)}G^{(1)\mu\nu}
-\frac13H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}\\
&-2E_a^{(1)}E^{(1)a}
-2\sqrt2E^{(1)a}V_a^{(1)}
-4gE^{(1)a}C_a^{(1)}\\
&+2V_a^{\prime(1)ij}V^{\prime(1)a}_{ij}\\
&-\bar\psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}^{(1)}\\
&+2\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+2i\sqrt2\delta_{ij}
\bar\varphi^{(1)i}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\gamma^{\mu\nu}
\psi_\nu^{(1)j}\\
&-4g\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}\\
&+\frac{7ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{15.4}
```

The definitions accompanying (15.4) are

```math
\begin{aligned}
R^{(1)}={}&
\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h+2g^2h,\\
\mathcal G_{\mu\nu}^{(1)}(h)={}&
R_{\mu\nu}^{(1)}
-\frac12\bar g_{\mu\nu}R^{(1)}
+2g^2h_{\mu\nu},\\
G_{\mu\nu}^{(1)}={}&2\bar\nabla_{[\mu}C_{\nu]}^{(1)},\\
H_{\mu\nu\rho}^{(1)}={}&
3\bar\nabla_{[\mu}B_{\nu\rho]}^{(1)}
+\frac g2E_{\mu\nu\rho}^{(1)},\\
E^{(1)a}={}&
-\frac1{12}\bar\varepsilon^{abcde}
\bar\nabla_bE_{cde}^{(1)}.
\end{aligned}
\tag{15.5}
```

No symbol in (15.4) denotes an inverse operator or an unannounced field.

## 16. Checks

### 16.1 Background residuals

At $`(L,N,k)=(1,-3g/2,-g^2/2)`$,

```math
-4L^{-1}N-2gL-4g=0,
\tag{16.1}
```

```math
20k+2L^{-2}N^2-2gN
-\frac32g^2L^2+4g^2L=0,
\tag{16.2}
```

```math
-6Lk-\frac12U=0.
\tag{16.3}
```

### 16.2 Tadpole and ungauged checks

Equation (15.2) is a pure boundary term.  Formally setting $`g\to0`$ gives
the fluxless Minkowski raw quadratic action associated with the same
Gold-normalized 2016-map density: every algebraic bosonic and fermionic AdS
term disappears, while the kinetic and derivative-mixing terms remain.

### 16.3 Dimensions and field order

Every term in (15.4) has the same five-dimensional Lagrangian dimension.
Every first-order field appears exactly twice.  Terms such as
$`hG^{(1)2}`$, $`L^{(1)}H^{(1)2}`$, and
$`E^{(1)}\bar\psi^{(1)}\varphi^{(1)}`$ are cubic and are correctly absent.

### 16.4 Reproducible verification boundary

The component checker derives the symmetric F Hessian and traces it,
Taylor-expands the nonlinear potential, solves the background equations,
and expands non-diagonal metric matrices. It also assembles the algebraic
fermion kernel directly from the four source slots using explicit Clifford
matrices and the Majorana bar.

Run:

    python3 -B computations/two_derivative_fermionic/src/kernels/audit_exact_checks.py

The corrected tuple, ordered as RS kinetic, spinor kinetic, derivative
mixing in i sqrt(2), RS mass in ig/sqrt(2), mixed mass in g, and spinor
mass in ig/sqrt(2), is

    (-1, 2, 2, -3/2, -4, 7)

The [component check guide](../../../../README.md) states the executable scope.
The same checker verifies the local field shift and both Euler rows.
The nonlinear Pauli terms outside this fluxless projection are not
certified by that finite matrix calculation.

## 17. Certification boundary

This file certifies the fluxless AdS5 background, the vanishing bulk
tadpole, and the complete raw $`S^{(2)}`$ following from the active
2016-map action at its retained fermion order.  It does not certify a
gauge-fixed action, diagonal fields, equations for eliminated auxiliaries,
AdS energies, masses, degrees of freedom, or a supermultiplet assignment.
