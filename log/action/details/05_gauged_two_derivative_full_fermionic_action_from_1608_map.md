---
title: Gauged two-derivative action from the 2016 single-linear-multiplet map
date: 2026-09-08
updated: 2026-09-27
status: source-component construction with scoped checks
method: vector-linear density, source-derived component sum, target Poincare gauge
fermion_order: complete through quadratic fermions
off_shell: true
---

# Gauged two-derivative full fermionic action from the 2016 map

> **Action lock:** `2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2`  
> **Linear-map parent:** `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`  
> **Defining-vector parent:** `2DER-GAUGED-VDEFINING-COMPONENTS-v2`  
> **Fermion order:** exact in bosons and complete through quadratic fermions in
> exact source-supercovariant notation. Sections 9–10 specify the checks.
> **Corrections, 2026-09-27:** the missing factor of (i) in (4.14),
> the ordinary current in (5.11), and the tensor/density factors in
> (3.5), (3.6), (3.8), (3.10) are corrected below with explicit checks.

<!-- ASSERT_ACTION_LOCK: 2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2 -->
<!-- ASSERT_LINEAR_MAP_PARENT: OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2 -->
<!-- ASSERT_VDEFINING_PARENT: 2DER-GAUGED-VDEFINING-COMPONENTS-v2 -->
<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=mostly_plus, index_positioning=NW-SE -->
<!-- ASSERT_FERMION_ORDER: quadratic -->
<!-- ASSERT_OFF_SHELL: true -->

<a id="1-problem-and-target"></a>

## Problem and Target

<a id="11-derivation-objective"></a>

### Derivation objective

**Goal.** Construct the gauged two-derivative off-shell action in the gauge

```math
\sigma=1,
\qquad
\psi^i=0,
\qquad
b_\mu=0,
\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},
\tag{1.1}
```

using the newly reconstructed single-linear-multiplet map rather than the
archived map.

**Starting point.** The calculation starts from:

1. the complete vector--linear density of corrected Özkan--Pang;
2. the four component slots constructed from Özkan 2016 Eq. (3.14);
3. the independently anchored defining vector of Coomans--Özkan;
4. the source-derived vector argument
   $`V_{\mathrm{linear}}+2gV_{\mathrm{defining}}`$;
5. the target density normalization fixed by the ungauged
   Özkan--Pang/Gold comparison.

**Expected result.** One vector--linear density,

```math
\boxed{
\mathcal L_{2\partial}^{\mathrm{Gold}}
=
-2\,
\mathcal L_{\mathrm{VL}}
\left[
V_{\mathrm{linear}}+2gV_{\mathrm{defining}};
\mathbb L
\right],
}
\tag{1.2}
```

followed by its complete target-gauge component expansion through quadratic
fermions.

**Method.** Insert the two vector maps component by component before gauge
fixing, apply the gauge only afterward, evaluate every slot, and substitute
the evaluated slots into the unchanged vector--linear density.

<a id="12-given-information-and-provenance"></a>

### Given information and provenance

| Input | Canonical source or active anchor | Location |
| --- | --- | --- |
| vector--linear density and boundary representative | corrected Özkan--Pang, [source bibliography](../../../references/bibliography.md) | Eqs. (3.1)--(3.2), PDF p. 10 |
| conformal d'Alembertian and target gauge | same | Eqs. (3.6), (4.1)--(4.3), PDF pp. 11 and 13--14 |
| single-multiplet local composite | Özkan 2016, [source bibliography](../../../references/bibliography.md) | Eqs. (2.15), (3.14), PDF pp. 6 and 9 |
| completed four-slot map | [03_single_linear_multiplet_linear_map_anchor.md](../../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/03_single_linear_multiplet_linear_map_anchor.md) | lock `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2` |
| defining vector, $`E`$-forms, and component sum | [04_defining_vector_component_anchor.md](../../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/04_defining_vector_component_anchor.md) | lock `2DER-GAUGED-VDEFINING-COMPONENTS-v2` |
| gauged Dilaton--Weyl composites | Coomans--Özkan, [source bibliography](../../../references/bibliography.md) | Eqs. (2.14)--(2.17), (5.2)--(5.8), PDF pp. 7--8 and 16--17 |
| target normalization and bosonic comparison | Gold et al. 2025, [source bibliography](../../../references/bibliography.md) | Eqs. (1), (3)--(4), (25)--(27), PDF pp. 4--6 and 14 |

Parent hashes:

| File | SHA-256 |
| --- | --- |
| [03_single_linear_multiplet_linear_map_anchor.md](../../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/03_single_linear_multiplet_linear_map_anchor.md) | `817cc20787c6730821e7e416551f2154adfc247f7dea37eb66147bbf1afd4975` |
| [04_defining_vector_component_anchor.md](../../../computations/two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/04_defining_vector_component_anchor.md) | `bdd22ef4d007db5a476b6828303a0bf74a0c0ab8ce496ca87d382938f7b75cec` |
| canonical ungauged v4 action | `140c5f9430adff18c173d95da29ae7433e9562b2d16d28050617160c8951c0ac` |

The archived gauged action is used only as the specified presentation model.
No coefficient below is taken from it. The component formulas come from the
two active anchors above.

<a id="13-fields-and-geometric-objects"></a>

### Fields and geometric objects

The independent fields retained after Eq. (1.1) are

```math
\begin{aligned}
&e_\mu{}^a,\quad \psi_\mu{}^i,\quad
C_\mu,\quad B_{\mu\nu},\quad
L,\quad\varphi^i,\\
&E_a\ \text{or equivalently}\ E_{\mu\nu\rho},
\quad N,\quad
V_\mu,\quad V_\mu^{\prime\,ij}.
\end{aligned}
\tag{1.3}
```

The dependent source objects retained in exact supercovariant notation are

```math
\omega_\mu{}^{ab},
\qquad
\phi_\mu{}^i,
\qquad
f_\mu{}^a,
\qquad
\widehat R_{\mu\nu}{}^i(Q),
\qquad
\widehat R_{\mu\nu}{}^{ij}(V).
\tag{1.4}
```

Here $`\psi^i`$, without a spacetime index, is the defining-vector gaugino
fixed to zero. It is distinct from the gravitino $`\psi_\mu{}^i`$.

<a id="14-assumptions-and-permitted-operations"></a>

### Assumptions and permitted operations

- **A1. Off shell:** no descendant field equation is used. The defining-vector
  Euler equations ARE used in constructing the gauged Dilaton–Weyl map and
  reducing the Standard-Weyl parent by homogeneity. The equality after this
  map is not an identity of the unconstrained parent functional. N, E3, V
  and V' remain independent target fields.
- **A2. Fermion order:** all terms containing zero or two fermions are
  retained. Cubic terms in $`\lambda_i`$ enter the density only at four
  fermions; quartic terms in $`Y_{ij}`$ are also action-quartic. They are
  displayed at the map level and then labelled $`O(\text{four fermions})`$.
- **A3. Bosons:** no bosonic truncation is made until the independent
  bosonic reconstruction.
- **A4. Gauge fixing:** only Eq. (1.1) and its compensating transformations
  are permitted.
- **A5. Boundary:** the field-strength representative is used with
  equality $`\doteq`$, meaning equality of integrated actions after the
  explicit vector--three-form boundary term is retained or set to zero.
- **A6. Forbidden operations:** no target-theory auxiliary elimination, dualization,
  background selection, perturbative expansion, diagonalization, or field
  redefinition is used.

The fermion-order restriction is an exact projection onto action terms of
order at most two. It is not a small-field approximation and has no numerical
error estimate.

<a id="2-convention-ledger"></a>

## Convention Ledger

<a id="21-spacetime-gamma-matrices-and-epsilon"></a>

### Spacetime, gamma matrices, and epsilon

The calculation uses

```math
D=5,
\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),
\qquad
\{\gamma_a,\gamma_b\}=2\eta_{ab}.
\tag{2.1}
```

Antisymmetrized gamma matrices and spacetime tensors have unit weight:

```math
\gamma^{a_1\ldots a_n}
=\gamma^{[a_1}\cdots\gamma^{a_n]},
\qquad
X_{[\mu\nu]}
=\frac12(X_{\mu\nu}-X_{\nu\mu}).
\tag{2.2}
```

The epsilon contraction is

```math
\varepsilon_{\mu\nu\rho\alpha\beta}
\varepsilon^{\mu\nu\rho\gamma\delta}
=-3!\,2!\,
\delta_{[\alpha}^{\gamma}\delta_{\beta]}^\delta.
\tag{2.3}
```

Spacetime $`\varepsilon`$ in this document is the epsilon tensor, as in
the project `CONVENTIONS.md`. Define its coordinate density symbol by

```math
\mathfrak e^{\mu\nu\rho\sigma\lambda}
:=e\varepsilon^{\mu\nu\rho\sigma\lambda},
\qquad
\partial_\tau\mathfrak e^{\mu\nu\rho\sigma\lambda}=0.
\tag{2.3a}
```

No numerical orientation is selected. Tensor epsilon in (3.5), (3.6)
and (3.10) therefore carries no additional external determinant factor.

<a id="22-nw--se-su2-convention"></a>

### NW--SE $`SU(2)`$ convention

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
\tag{2.4}
```

For symmetric triplets,

```math
L^{ij}
=\varepsilon^{ik}\varepsilon^{j\ell}L_{k\ell},
\qquad
Y_{ij}
=Y^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}.
\tag{2.5}
```

One-index raising never converts an epsilon into a delta. On the gauge slice,

```math
L_k{}^\ell
=-\frac{L}{\sqrt2}\delta_{km}\varepsilon^{m\ell},
\qquad
L^k{}_i
=\frac{L}{\sqrt2}\varepsilon^{k\ell}\delta_{\ell i}.
\tag{2.6}
```

<a id="23-spinor-ordering-and-flip-rules"></a>

### Spinor ordering and flip rules

All fermions and the supersymmetry parameter are Grassmann odd and
symplectic Majorana. For fixed upper indices,

```math
\bar\alpha^i\gamma_{(n)}\beta^j
=t_n\bar\beta^j\gamma_{(n)}\alpha^i,
\qquad
t_0=t_1=+1,
\qquad
t_2=t_3=-1.
\tag{2.7}
```

For an NW--SE contraction,

```math
\begin{aligned}
\bar\alpha^i\gamma_{(n)}\beta_i
&=\bar\alpha^i\gamma_{(n)}\beta^j\varepsilon_{ji}\\
&=t_n\bar\beta^j\gamma_{(n)}\alpha^i\varepsilon_{ji}\\
&=-t_n\bar\beta^i\gamma_{(n)}\alpha_i.
\end{aligned}
\tag{2.8}
```

No Fierz rearrangement is used below. The 2016 source ordering is preserved.

The source bar is the **Majorana bar**, $`\bar\zeta^i=(\zeta^i)^TC`$,
not an antilinear operation on displayed coefficients. Thus
$`\overline{c\gamma_a\zeta^i}=c\bar\zeta^i\gamma_a`$,
$`\overline{c\gamma_{ab}\zeta^i}=-c\bar\zeta^i\gamma_{ab}`$, and
$`\overline{\zeta_i}=\bar\zeta^j\varepsilon_{ji}`$.
The exact anchor is the local 5D Weyl-multiplet paper, Appendix A,
Eqs. (A.4), (A.7), (A.9), printed pp. 31–32. In particular, the factorized
bar in (5.5) is evaluated this way. The previous Dirac-bar wording was
not a valid replacement without the full symplectic-Majorana conversion.

<a id="24-weights-derivatives-and-equality-symbols"></a>

### Weights, derivatives, and equality symbols

The relevant Weyl weights are

| Object | Weight |
| --- | ---: |
| $`L_{ij}`$, $`\varphi^i`$, $`E_a`$, $`N`$ | $`3,\frac72,4,4`$ |
| $`\rho`$, $`\lambda_i`$, $`Y_{ij}`$, $`\widehat F_{ab}`$ | $`1,\frac32,2,2`$ |
| $`\sigma`$, $`\psi^i`$, defining $`Y^{ij}`$, $`\widehat G_{ab}`$ | $`1,\frac32,2,2`$ |
| $`T_{ab}`$, $`\chi^i`$, $`D`$, $`g`$ | $`1,\frac32,2,0`$ |

The symbols mean:

- $`=`$: exact local equality at the displayed fermion order;
- $`\doteq`$: equality of integrated actions modulo the displayed boundary;
- $`O(\text{four fermions})`$: terms excluded by A2.

The explicit conventions in this section are therefore the operative lock.

<a id="3-definitions-and-required-identities"></a>

## Definitions and Required Identities

<a id="31-the-unchanged-vector--linear-density"></a>

### The unchanged vector--linear density

The potential representative is

Here (A_\mu) denotes the gauge potential of the vector argument inserted
into the density; it is not an additional field. In the boundary
representative only its ordinary field strength is needed.

```math
\begin{aligned}
e^{-1}\mathcal L_{\mathrm{VL}}
={}&Y^{ij}L_{ij}
+i\bar\lambda^i\varphi_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda^jL_{ij}\\
&-\frac1{12}
\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu\partial_\nu E_{\rho\sigma\lambda}\\
&+\rho\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{i}{4}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
\right).
\end{aligned}
\tag{3.1}
```

After one integration by parts,

```math
\begin{aligned}
e^{-1}\mathcal L_{\mathrm{VL}}
\doteq{}&
Y^{ij}L_{ij}
+i\bar\lambda^i\varphi_i
-\frac12\bar\psi_a{}^i\gamma^a\lambda^jL_{ij}\\
&+\frac12F_{\mu\nu}E^{\mu\nu}\\
&+\rho\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{i}{4}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
\right).
\end{aligned}
\tag{3.2}
```

The boundary conversion is

```math
\begin{aligned}
&-\frac1{12}\int_M d^5x\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu\partial_\nu E_{\rho\sigma\lambda}\\
&\qquad=
\frac12\int_M d^5x\,eF_{\mu\nu}E^{\mu\nu}\\
&\qquad\quad
-\frac1{12}\int_{\partial M}d\Sigma_\nu\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu E_{\rho\sigma\lambda}.
\end{aligned}
\tag{3.3}
```

<a id="32-e_mu-e_munu-and-e_munurho"></a>

### $`E_\mu`$, $`E_{\mu\nu}`$, and $`E_{\mu\nu\rho}`$

These are not three independent fields:

| Symbol | Definition and meaning |
| --- | --- |
| $`E_\mu`$ | constrained linear-multiplet vector |
| $`E_{\mu\nu}`$ | dual two-form representative |
| $`E_{\mu\nu\rho}`$ | three-form gauge potential solving the constraint |

Explicitly,

```math
\mathcal D_aE^a=0,
\qquad
E_\mu=e_\mu{}^aE_a=g_{\mu\nu}E^\nu,
\tag{3.4}
```

```math
E^\mu
=-\frac1{12}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}
=\mathcal D_\nu E^{\mu\nu},
\tag{3.5}
```

```math
E_{\mu\nu\rho}
=\varepsilon_{\mu\nu\rho\sigma\lambda}E^{\sigma\lambda},
\qquad
E_{\mu\nu}
=g_{\mu\rho}g_{\nu\sigma}E^{\rho\sigma},
\tag{3.6}
```

```math
\delta_\Lambda E_{\mu\nu\rho}
=3\partial_{[\mu}\Lambda_{\nu\rho]}.
\tag{3.7}
```

The complete supercovariant divergence is

```math
\begin{aligned}
\mathcal D_\nu E^{\mu\nu}
={}&e^{-1}\partial_\nu(eE^{\mu\nu})
+\frac{i}{2}
\bar\psi_\nu{}^i\gamma^{\mu\nu}\varphi_i\\
&+\frac14
\bar\psi_\rho{}^i\gamma^{\mu\nu\rho}
\psi_\nu{}^jL_{ij}.
\end{aligned}
\tag{3.8}
```

The density's potential representative uses

```math
P^a
=E^a
+\frac{i}{2}\bar\psi_b{}^i\gamma^{ba}\varphi_i
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij},
\tag{3.9}
```

which also equals

```math
P^a
=-\frac1{12}e_\mu{}^a
\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}.
\tag{3.10}
```

The determinant factors and the two-fermion current completion can be
checked without any field equation:

```math
\begin{aligned}
E^{\mu\nu}
&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda},\\
e^{-1}\partial_\nu(eE^{\mu\nu})
&=-\frac1{12}e^{-1}\partial_\nu
  (\mathfrak e^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda})\\
&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
  \partial_\nu E_{\rho\sigma\lambda}=P^\mu,\\
E^\mu
&=P^\mu-\frac i2\bar\psi_\nu\gamma^{\nu\mu}\varphi
 -\frac14\bar\psi_\nu^i\gamma^{\mu\nu\rho}\psi_\rho^jL_{ij}\\
&=P^\mu+\frac i2\bar\psi_\nu\gamma^{\mu\nu}\varphi
 +\frac14\bar\psi_\rho^i\gamma^{\mu\nu\rho}\psi_\nu^jL_{ij}.
\end{aligned}
\tag{3.10a}
```

In the last line, gamma antisymmetry and a dummy-index exchange suffice;
no spinor is commuted. The inverse form normalization follows from
$`(-1/12)(-3!2!)=1`$ acting on an antisymmetric two-form. These are the
tensor conventions already used by (3.1)--(3.3).

<a id="33-ordinary-and-supercovariant-vector-field-strengths"></a>

### Ordinary and supercovariant vector field strengths

For the defining vector,

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},
\tag{3.11}
```

```math
\widehat G_{\mu\nu}
=G_{\mu\nu}
-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\psi_i
+\frac{i}{2}\sigma
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\tag{3.12}
```

For a general vector multiplet,

```math
\widehat F_{\mu\nu}
=F_{\mu\nu}
-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\lambda_i
+\frac{i}{2}\rho
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\tag{3.13}
```

Therefore

```math
F_{\mu\nu}
=\widehat F_{\mu\nu}
+\bar\psi_{[\mu}{}^i\gamma_{\nu]}\lambda_i
-\frac{i}{2}\rho
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\tag{3.14}
```

<a id="34-dependent-curvatures-and-connections"></a>

### Dependent curvatures and connections

The $`Q`$-curvature before adding the $`S`$-connection is

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}{}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}{}^i
+b_{[\mu}\psi_{\nu]}{}^i\\
&-2V_{[\mu}{}^{ij}\psi_{\nu]j}
+2i\gamma\mathbin{\cdot}T
\gamma_{[\mu}\psi_{\nu]}{}^i.
\end{aligned}
\tag{3.15}
```

The dependent $`S`$-connection and full $`Q`$-curvature are

```math
\phi_\mu{}^i
=\frac{i}{3}\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac{i}{24}\gamma_\mu\gamma^{ab}
\widehat R'_{ab}{}^i(Q),
\tag{3.16}
```

```math
\widehat R_{\mu\nu}{}^i(Q)
=\widehat R'_{\mu\nu}{}^i(Q)
-2i\gamma_{[\mu}\phi_{\nu]}{}^i.
\tag{3.17}
```

The $`SU(2)`$ curvature is

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^{ij}(V)
={}&2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}\\
&-3i\bar\phi_{[\mu}{}^{(i}\psi_{\nu]}{}^{j)}
-8\bar\psi_{[\mu}{}^{(i}\gamma_{\nu]}\chi^{j)}\\
&-i\bar\psi_{[\mu}{}^{(i}
\gamma\mathbin{\cdot}T\psi_{\nu]}{}^{j)}.
\end{aligned}
\tag{3.18}
```

The project uses the corrected $`\chi`$-term in the primed Lorentz curvature,

```math
\boxed{
\widehat R'_{\mu\nu}{}^{ab}(M)\big|_\chi
=+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}
\gamma^{b]}\chi.
}
\tag{3.19}
```

This is a project-derived correction, not a published erratum. The
connection $`f_\mu{}^a`$ is obtained from this corrected curvature:

```math
f_\mu{}^a
=-\frac16R_\mu{}^a+\frac1{48}e_\mu{}^aR,
\qquad
f_a{}^a=-\frac1{16}R
\quad\text{bosonically}.
\tag{3.20}
```

The dependent $`\omega_\mu{}^{ab}`$ already contains the source gravitino
contorsion. It is not replaced by a separately defined hatted connection.

In a fermionic calculation the R in the definition of f means the Ricci
contraction of the complete primed Lorentz curvature, not the purely
bosonic Riemann scalar. In particular the corrected (3.19) gives

```math
\begin{aligned}
R\big|_\chi
&=8\frac{1-5-5+1}{4}\bar\psi_a\gamma^a\chi
=-16\bar\psi_a\gamma^a\chi,\\
f_a{}^a\big|_\chi&=+\bar\psi_a\gamma^a\chi.
\end{aligned}
\tag{3.20a}
```

This term must be retained in both conformal boxes and D. It is the
load-bearing contraction corrected in file 06 (12.16a)–(12.17).

<a id="4-detailed-derivation"></a>

## Detailed Derivation

<a id="41-the-two-maps-are-separate-before-their-sum"></a>

### The two maps are separate before their sum

The first vector argument is the active 2016 linear composite,

```math
V_{\mathrm{linear}}
=
\left(
\rho_{\mathrm{linear}},
\lambda_{\mathrm{linear}\,i},
Y_{\mathrm{linear}\,ij},
\widehat F_{\mathrm{linear}\,\mu\nu}
\right).
\tag{4.1}
```

The second is the defining vector,

```math
V_{\mathrm{defining}}
=
\left(
\sigma,C_\mu,\psi^i,Y^{ij}
\right),
\qquad
\text{field strength }\widehat G_{\mu\nu}.
\tag{4.2}
```

They are not identified. In particular,

```math
Y_{\mathrm{linear}\,ij}
\neq
Y^{ij}.
\tag{4.3}
```

The source-derived target-oriented sum is

```math
\boxed{
V_{\mathrm{linear}}+2gV_{\mathrm{defining}}.
}
\tag{4.4}
```

Componentwise, before gauge fixing,

```math
\boxed{
\begin{aligned}
\rho_{\mathrm{eff}}
&=\rho_{\mathrm{linear}}+2g\sigma,\\
\lambda_{\mathrm{eff}\,i}
&=\lambda_{\mathrm{linear}\,i}
+2g\psi^j\varepsilon_{ji},\\
Y_{\mathrm{eff}\,ij}
&=Y_{\mathrm{linear}\,ij}
+2gY^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j},\\
\widehat F_{\mathrm{eff}\,\mu\nu}
&=\widehat F_{\mathrm{linear}\,\mu\nu}
+2g\widehat G_{\mu\nu}.
\end{aligned}
}
\tag{4.5}
```

These labels describe one vector argument and introduce no new physical
field.

<a id="42-overall-density-normalization"></a>

### Overall density normalization

The corrected Özkan--Pang action is

```math
\mathcal L_{2\partial}^{\mathrm{OP}}
=-\mathcal L_{\mathrm{VL}}[V_{\mathrm{linear}};\mathbb L],
\tag{4.6}
```

and its ungauged bosonic Einstein term is

```math
e^{-1}\mathcal L_{2\partial}^{\mathrm{OP}}
\supset\frac12LR.
\tag{4.7}
```

Gold Eq. (26) uses

```math
e^{-1}\mathcal L_{2\partial}^{\mathrm{Gold}}
\supset LR.
\tag{4.8}
```

We calibrate the one overall normalization using the LR coefficient in
Gold Eq. (26). This coefficient is an input, not a prediction. The other
four ungauged ratios below test consistency with that single choice:

| Structure | Özkan--Pang | Gold | Ratio |
| --- | ---: | ---: | ---: |
| $`LR`$ | $`1/2`$ | $`1`$ | $`2`$ |
| $`LG^2`$ | $`-1/4`$ | $`-1/2`$ | $`2`$ |
| $`L^{-1}(\partial L)^2`$ | $`1/2`$ | $`1`$ | $`2`$ |
| $`L^{-1}N^2`$ | $`-1`$ | $`-2`$ | $`2`$ |
| $`LV'^2`$ | $`1`$ | $`2`$ | $`2`$ |

Hence the factor two is a single global density normalization fixed entirely
from the ungauged sector:

```math
\boxed{
\mathcal L_{2\partial}^{\mathrm{Gold}}
=-2\mathcal L_{\mathrm{VL}}
[V_{\mathrm{linear}}+2gV_{\mathrm{defining}};\mathbb L].
}
\tag{4.9}
```

It is not a second invariant.

<a id="43-target-gauge-and-compensating-transformations"></a>

### Target gauge and compensating transformations

Apply Eq. (1.1) only after forming Eq. (4.5). The defining-vector auxiliary
becomes

```math
Y^{ij}\big|_{\mathrm P}
=-\frac g2L^{ij}
=-\frac{gL}{2\sqrt2}\delta^{ij}.
\tag{4.10}
```

Lowering both indices,

```math
\begin{aligned}
Y_{ij}\big|_{\mathrm P}
&=Y^{k\ell}\big|_{\mathrm P}
\varepsilon_{ki}\varepsilon_{\ell j}\\
&=-\frac g2L^{k\ell}
\varepsilon_{ki}\varepsilon_{\ell j}\\
&=-\frac g2L_{ij}.
\end{aligned}
\tag{4.11}
```

The defining-gaugino transformation is

```math
\delta\psi^i
=-\frac14\gamma\mathbin{\cdot}\widehat G\,\epsilon^i
-\frac{i}{2}\not{\mathcal D}\sigma\,\epsilon^i
+\sigma\gamma\mathbin{\cdot}T\,\epsilon^i
-Y^{ij}\epsilon_j
+\sigma\eta^i.
\tag{4.12}
```

Therefore $`\delta\psi^i|_{\mathrm P}=0`$ gives

```math
\boxed{
\eta^i
=
\left(
-\gamma\mathbin{\cdot}T
+\frac14\gamma\mathbin{\cdot}\widehat G
\right)\epsilon^i
-\frac{gL}{2\sqrt2}\delta^{ij}\epsilon_j.
}
\tag{4.13}
```

The remaining compensators are

```math
\begin{aligned}
\lambda^{ij}
&=-\frac{i}{\sqrt2L}
S^{k(i}\delta^{j)\ell}\varepsilon_{k\ell},\\
S^{ij}
&=\bar\epsilon^{(i}\varphi^{j)}
-\frac12\delta^{ij}
\bar\epsilon^k\varphi^\ell\delta_{k\ell},\\
\Lambda_{K\mu}
&=-\frac{i}{4}\bar\epsilon\phi_\mu
-\frac{i}{4}\bar\eta\psi_\mu
+\bar\epsilon\gamma_\mu\chi.
\end{aligned}
\tag{4.14}
```

The factor $`i`$ in $`\lambda^{ij}`$ corrects the previous display.
Its sign and normalization follow from the same connection convention
used in the action:

```math
\mathcal D_\mu L^{ij}
=(\partial_\mu-3b_\mu)L^{ij}
+2V_\mu{}^{(i}{}_kL^{j)k}-i\bar\psi_\mu^{(i}\varphi^{j)},
\qquad
\delta_U L^{ij}=-2\lambda^{(i}{}_kL^{j)k}.
\tag{4.14a}
```

For a hand check, write $`J=(\varepsilon_{ij})`$ and
$`S=(S^{ij})=\left(\begin{smallmatrix}s&t\\t&-s\end{smallmatrix}\right)`$,
where $`s,t`$ are arbitrary symbolic bilinears. Define
$`\mathop{\mathrm{sym}}\nolimits M=(M+M^T)/2`$. Then

```math
\begin{aligned}
J&=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
&J^2&=-\mathbf1,\qquad
SJ=\begin{pmatrix}-t&s\\s&t\end{pmatrix}=(SJ)^T,\\
\lambda&=-\frac{i}{\sqrt2L}SJ,
&\delta_U L^{ij}\big|_{\mathrm{traceless}}
&=\left[-\sqrt2L\mathop{\mathrm{sym}}\nolimits(\lambda J)\right]^{ij}
=-iS^{ij},\\
(\delta_Q+\delta_U)L^{ij}\big|_{\mathrm{traceless}}
&=iS^{ij}-iS^{ij}=0.
\end{aligned}
\tag{4.14b}
```

Here $`L\ne0`$, as required by the original map. The old coefficient
$`-1/(\sqrt2L)`$ instead leaves $`(i-1)S^{ij}`$.
A parameter proportional to $`\delta^{ij}`$ generates the remaining
$`U(1)`$ symmetry; it is not fixed by triplet alignment. Equation (4.14)
specifies the compensating traceless part, without fixing that residual
gauge freedom. No coupling or field normalization is changed.

The $`SU(2)`$ connection is decomposed as

```math
V_\mu{}^{ij}
=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad
\delta_{ij}V_\mu^{\prime\,ij}=0.
\tag{4.15}
```

<a id="44-gauged-dilaton--weyl-data-on-the-gauge-slice"></a>

### Gauged Dilaton--Weyl data on the gauge slice

The supercovariant defining-vector strength is

```math
\boxed{
\widehat G_{\mu\nu}\big|_{\mathrm P}
=G_{\mu\nu}
+\frac{i}{2}\bar\psi_{[\mu}{}^i\psi_{\nu]i},
\qquad
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
}
\tag{4.16}
```

The gauging enters the three-form before any field equation is used:

```math
\boxed{
\begin{aligned}
\widehat H_{\mu\nu\rho}\big|_{\mathrm P}
={}&3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}\\
&-\frac34
\bar\psi_{[\mu}{}^i\gamma_\nu\psi_{\rho]i}.
\end{aligned}
}
\tag{4.17}
```

The term proportional to the defining gaugino in the source expression for
$`\widehat H`$ vanishes because $`\psi^i=0`$; the gravitino bilinear in
(4.17) remains.  The Standard-Weyl tensor auxiliary is therefore

```math
\boxed{
T_{ab}\big|_{\mathrm P}
=\frac18\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right).
}
\tag{4.18}
```

For later readability, every occurrence of the parenthesis in (4.18) is
written out in full.  It is not assigned a new symbol.

<a id="45-the-gauge-fixed-defining-gaugino-still-has-a-derivative"></a>

### The gauge-fixed defining gaugino still has a derivative

The source derivative was given in Eq. (4.5) of the defining-vector anchor.
After imposing the target gauge it gives

```math
\boxed{
\begin{aligned}
\mathcal D_\mu\psi^i\big|_{\mathrm P}
={}&\Bigg[
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg]\psi_\mu{}^i\\
&-\phi_\mu{}^i
-\frac{gL}{2\sqrt2}\delta^{ij}\psi_{\mu j}.
\end{aligned}
}
\tag{4.19}
```

The last term is the contribution of the defining-vector auxiliary.  It is
not erased by the gauge value $`\psi^i=0`$.  Lowering its free index shows
the NW--SE sign explicitly:

```math
\begin{aligned}
\left(\mathcal D_\mu\psi_i\right)_{g}
&=\left(
-\frac{gL}{2\sqrt2}\delta^{kj}\psi_{\mu j}
\right)\varepsilon_{ki}\\
&=+\frac{gL}{2\sqrt2}\delta_{ij}\psi_\mu{}^j.
\end{aligned}
\tag{4.20}
```

Thus the upper- and lower-index formulas must not be identified with the same
sign.

<a id="46-the-composites-chii-squarecsigma-and-d"></a>

### The composites $`\chi^i`$, $`\square^C\sigma`$, and $`D`$

At the retained fermion order, the gauged spinor composite is

```math
\boxed{
\begin{aligned}
\chi^i\big|_{\mathrm P}
={}&\frac{i}{8}\gamma^\mu
\Bigg\{
\Bigg[
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg]\psi_\mu{}^i\\
&\hspace{6em}
-\phi_\mu{}^i
-\frac{gL}{2\sqrt2}\delta^{ij}\psi_{\mu j}
\Bigg\}
+\frac g8\varphi^i
+O(\text{three fermions}).
\end{aligned}
}
\tag{4.21}
```

Its lower-index form is obtained only after the complete upper-index
expression is formed:

```math
\chi_i\big|_{\mathrm P}
=\left(\chi^r\big|_{\mathrm P}\right)\varepsilon_{ri}.
\tag{4.22}
```

The conformal d'Alembertian of the constant compensator is not zero.  From
the source definition,

```math
\begin{aligned}
\square^C\sigma\big|_{\mathrm P}
={}&-\frac{i}{2}\bar\psi_a{}^i
\left(\mathcal D^a\psi^r\big|_{\mathrm P}\right)
\varepsilon_{ri}\\
&-2\bar\psi_a{}^i\gamma^a
\left(\chi^r\big|_{\mathrm P}\right)\varepsilon_{ri}
+2f_a{}^a.
\end{aligned}
\tag{4.23}
```

Substituting (4.21) into (4.23) and then into the complete source formula
for $`D`$ gives

```math
\boxed{
\begin{aligned}
D\big|_{\mathrm P}
={}&\frac12f_a{}^a
-\frac1{16}\widehat G_{ab}\widehat G^{ab}\\
&-\frac{13}{96}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\left(
\widehat G^{ab}
+\frac16\varepsilon^{abfgh}\widehat H_{fgh}
\right)\\
&+\frac14\widehat G^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
+\frac g4N
+\frac{g^2}{16}L^2\\
&-\frac{i}{8}\bar\psi_a{}^i
\Bigg\{
\Bigg[
\frac14\gamma^{bc}\widehat G_{bc}
-\frac18\gamma^{bc}\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)
\Bigg]\psi^{ar}\\
&\hspace{8em}
-\phi^{ar}
-\frac{gL}{2\sqrt2}\delta^{rs}\psi^a{}_s
\Bigg\}\varepsilon_{ri}\\
&-\frac{i}{16}\bar\psi_a{}^i\gamma^a\gamma^\mu
\Bigg\{
\Bigg[
\frac14\gamma^{bc}\widehat G_{bc}
-\frac18\gamma^{bc}\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)
\Bigg]\psi_\mu{}^r\\
&\hspace{8em}
-\phi_\mu{}^r
-\frac{gL}{2\sqrt2}\delta^{rs}\psi_{\mu s}
\Bigg\}\varepsilon_{ri}\\
&-\frac g{16}\bar\psi_a{}^i\gamma^a\varphi_i
+O(\text{four fermions}).
\end{aligned}
}
\tag{4.24}
```

The coefficient $`-13/96`$ is not imported from the final action.  It is
obtained directly from

```math
-\frac{26}{3}T^2
=-\frac{26}{3}\left(\frac18\right)^2
\left(
\widehat G+\frac16\varepsilon\widehat H
\right)^2
=-\frac{13}{96}
\left(
\widehat G+\frac16\varepsilon\widehat H
\right)^2.
\tag{4.25}
```

The two explicit bosonic gauging terms in (4.24) will generate

```math
-8L\left(\frac g4N+\frac{g^2}{16}L^2\right)
=-2gLN-\frac12g^2L^3
\tag{4.26}
```

inside the Gold-normalized action.  This observation is a forward
substitution check, not a fit to the final potential.

<a id="47-linear-multiplet-derivatives"></a>

### Linear-multiplet derivatives

The gauge-fixed derivative of the triplet is

```math
\boxed{
\begin{aligned}
\mathcal D_\mu L_{ij}\big|_{\mathrm P}
={}&\frac1{\sqrt2}\delta_{ij}\partial_\mu L
-\sqrt2L\,V'_{\mu(i}{}^k\delta_{j)k}\\
&-i\bar\psi_{\mu(i}\varphi_{j)}.
\end{aligned}
}
\tag{4.27}
```

The connection sign in (4.27) is corrected to agree with the
upper-index derivative in CONVENTIONS.md and with (GC24) of the
Weyl-square source. With the same NW--SE rules as §2.2,

```math
\begin{aligned}
\varepsilon_{ki}\varepsilon_{\ell j}
 \left(2V_\mu{}^{(k}{}_mL^{\ell)m}\right)
&=-2V_{\mu(i}{}^kL_{j)k},\\
\mathcal D_\mu L_{ij}
&=(\partial_\mu-3b_\mu)L_{ij}
 -2V_{\mu(i}{}^kL_{j)k}
 -i\bar\psi_{\mu(i}\varphi_{j)},\\
-2V_{\mu(i}{}^kL_{j)k}\big|_{\mathrm P}
&=-\sqrt2L\,V'_{\mu(i}{}^k\delta_{j)k}.
\end{aligned}
\tag{4.27a}
```

The same correction is made in the bosonic copy (6.1). All appearances
of this derivative in (4.30), (4.32), the composite slots, and the
two-fermion density (5.10) use corrected (4.27). The explicit
upper-index connection term in (4.32) retains its plus sign.

All raised versions are generated from (4.27):

```math
\boxed{
\begin{aligned}
\mathcal D_\mu L^{ij}\big|_{\mathrm P}
&=\varepsilon^{ik}\varepsilon^{j\ell}
\mathcal D_\mu L_{k\ell}\big|_{\mathrm P},\\
\mathcal D_\mu L_j{}^k\big|_{\mathrm P}
&=\varepsilon^{k\ell}
\mathcal D_\mu L_{j\ell}\big|_{\mathrm P}.
\end{aligned}
}
\tag{4.28}
```

The source formula for $`\mathcal D_\mu\varphi^i`$ must be lowered before
the gauge is inserted.  The nontrivial rule is

```math
L^{rj}\varepsilon_{ri}\Psi_j=-L_{ij}\Psi^j.
\tag{4.29}
```

It follows that

```math
\boxed{
\begin{aligned}
\mathcal D_\mu\varphi_i\big|_{\mathrm P}
={}&\left(
\partial_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}
\right)\varphi_i
-V_{\mu i}{}^j\varphi_j\\
&-\frac{i}{2}\gamma^a
\left(
\mathcal D_aL_{ij}\big|_{\mathrm P}
\right)\psi_\mu{}^j
+\frac{i}{2}\gamma^aE_a\psi_{\mu i}
-\frac12N\psi_{\mu i}\\
&-\frac{L}{8\sqrt2}\delta_{ij}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\psi_\mu{}^j\\
&+\frac{3L}{\sqrt2}\delta_{ij}\phi_\mu{}^j.
\end{aligned}
}
\tag{4.30}
```

For example, the last sign follows without analogy:

```math
\begin{aligned}
-3L^{rj}\phi_{\mu j}\varepsilon_{ri}
&=-3\frac{L}{\sqrt2}\delta^{rj}
\phi_{\mu j}\varepsilon_{ri}\\
&=+\frac{3L}{\sqrt2}\delta_{ij}\phi_\mu{}^j.
\end{aligned}
\tag{4.31}
```

The contracted conformal d'Alembertian is retained in the legal source-index
form

```math
\boxed{
\begin{aligned}
L_{ij}\square^CL^{ij}\big|_{\mathrm P}
={}&\frac{L}{\sqrt2}\delta_{ij}
(\partial^a+\omega_b{}^{ba})
\mathcal D_aL^{ij}\big|_{\mathrm P}\\
&+\sqrt2L\,\delta_{ij}V_a{}^i{}_k
\mathcal D^aL^{jk}\big|_{\mathrm P}
+6L^2f_a{}^a\\
&-\frac{iL}{\sqrt2}\delta_{ij}
\bar\psi^{ai}\mathcal D_a\varphi^j\big|_{\mathrm P}
-6L^2\bar\psi_a{}^i\gamma^a\chi_i\big|_{\mathrm P}\\
&-\frac{L}{8\sqrt2}\delta_{ij}
\bar\varphi^i\gamma^{bc}
\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)\gamma^a\psi_a{}^j\\
&+\frac{L}{\sqrt2}\delta_{ij}
\bar\varphi^i\gamma^a\phi_a{}^j.
\end{aligned}
}
\tag{4.32}
```

Every repeated index in the second line is legally paired.  In particular,
no expression of the malformed form
$`\delta^{ij}V_a{}^i{}_k\mathcal D^aL_j{}^k`$ is used.

<a id="48-the-unchanged-2016-single-linear-multiplet-map"></a>

### The unchanged 2016 single-linear-multiplet map

This subsection records the complete map before its fermion-order projection.
It is the active map certified by
`OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`.

The scalar slot is

```math
\boxed{
\rho_{\mathrm{linear}}
=2L^{-1}N
+iL^{-3}L_{ij}\bar\varphi^i\varphi^j.
}
\tag{4.33}
```

The spinor slot is

```math
\boxed{
\begin{aligned}
\lambda_{\mathrm{linear}\,i}
={}&-2iL^{-1}\not{\mathcal D}\varphi_i
+L^{-1}\left(
16L_{ij}\chi^j
+4\gamma\mathbin{\cdot}T\,\varphi_i
\right)\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}\left(
\not{\mathcal D}L_{ij}L^{jk}\varphi_k
-\not E\,L_{ij}\varphi^j
\right)\\
&+2iL^{-3}\varphi^j\bar\varphi_i\varphi_j\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_l
L^{kl}L_{ij}.
\end{aligned}
}
\tag{4.34}
```

Here

```math
\not{\mathcal D}=\gamma^a\mathcal D_a,
\qquad
\not E=\gamma^aE_a,
\qquad
\gamma\mathbin{\cdot}T=\gamma^{ab}T_{ab}.
\tag{4.35}
```

Also, (T^2=T_{ab}T^{ab}).  The symbol $`\mathbb L`$ used in the density
denotes the already listed external linear multiplet
$`(L_{ij},\varphi^i,E_a,N)`$; it is not a new multiplet.

The final two lines of (4.34) are cubic.  Each occurrence of
$`\lambda_i`$ in the density is multiplied by one further fermion, so these
terms produce only action-quartic contributions.  They are displayed here
to certify the map and omitted from the quadratic-fermion action below.

The 2016 source-ordered triplet slot is

```math
\boxed{
\begin{aligned}
Y_{\mathrm{linear}\,ij}
={}&L^{-1}\square^cL_{ij}
-L^{-3}L^{km}
\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2
-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2
+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-3iNL^{-5}L_{ij}L^{kl}
\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}
+16iL^{-3}L_{ij}L_{kl}
\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k
\not{\mathcal D}L_{j)l}\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\varphi_m\\
&+2iL^{-3}L_{ij}
\bar\varphi\gamma\mathbin{\cdot}T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}
\left(L^{kl}\bar\varphi_k\varphi_l\right)^2\\
&-3L^{-5}
\left(L^{kl}\bar\varphi_k\varphi_l\right)
\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}
\left(\bar\varphi_m\varphi_n\right)
\left(\bar\varphi^m\varphi^n\right).
\end{aligned}
}
\tag{4.36}
```

The last three lines of (4.36) are action-quartic and are omitted below.
They are not replaced by the older 2013 vector-bilinear basis: doing so
would require an additional five-dimensional Fierz derivation.

The supercovariant field-strength slot is

```math
\boxed{
\begin{aligned}
\widehat F_{\mathrm{linear}\,\mu\nu}
={}&4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+2L^{-1}\widehat R_{\mu\nu}{}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^\ell
\mathcal D_{[\mu}L^{kp}
\mathcal D_{\nu]}L_{\ell p}\\
&-2\mathcal D_{[\mu}\left(
L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)\\
&-iL^{-1}\bar\varphi^i
\widehat R_{\mu\nu i}(Q).
\end{aligned}
}
\tag{4.37}
```

The third term has the project-verified mixed-index sign.  On the gauge
slice,

```math
-2L^{-3}L_k{}^\ell
\longrightarrow
+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}.
\tag{4.38}
```

<a id="49-gauge-fixed-linear-map-slots"></a>

### Gauge-fixed linear-map slots

Substituting (4.18)--(4.32) into (4.33)--(4.37), while retaining action
terms through two fermions, gives the following four slots.

The scalar slot is

```math
\boxed{
\rho_{\mathrm{linear}}\big|_{\mathrm P}
=2L^{-1}N
+\frac{i}{\sqrt2}L^{-2}\delta_{ij}
\bar\varphi^i\varphi^j.
}
\tag{4.39}
```

The spinor slot is

```math
\boxed{
\begin{aligned}
\lambda_{\mathrm{linear}\,i}\big|_{\mathrm P}
={}&-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_i\big|_{\mathrm P}\\
&+i\sqrt2\,\delta_{ij}\gamma^\mu
\Bigg\{
\Bigg[
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg]\psi_\mu{}^j\\
&\hspace{7em}
-\phi_\mu{}^j
-\frac{gL}{2\sqrt2}\delta^{jk}\psi_{\mu k}
\Bigg\}\\
&+\frac1{2L}\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi_i\\
&-\sqrt2NL^{-2}\delta_{ij}\varphi^j\\
&+2iL^{-3}\Bigg[
\left(\not{\mathcal D}L_{ij}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{jk}\varphi_k\\
&\hspace{7em}
-\frac{L}{\sqrt2}\delta_{ij}\not E\,\varphi^j
\Bigg]\\
&+\sqrt2g\,\delta_{ij}\varphi^j
+O(\text{three fermions}).
\end{aligned}
}
\tag{4.40}
```

Two separate mechanisms generate the explicit $`g`$-terms in (4.40):

```math
\begin{aligned}
i\sqrt2\delta_{ij}\gamma^\mu
\left(-\frac{gL}{2\sqrt2}\delta^{jk}\psi_{\mu k}\right)
&=-\frac{igL}{2}\gamma^\mu\psi_{\mu i},\\
8\sqrt2\delta_{ij}\left(\frac g8\varphi^j\right)
&=\sqrt2g\delta_{ij}\varphi^j.
\end{aligned}
\tag{4.41}
```

For the barred density term we define the scope once and do not reverse
Grassmann order by inspection:

```math
\boxed{
\bar\lambda_{\mathrm{linear}}{}^i\big|_{\mathrm P}
=\overline{\left(
\varepsilon^{ir}
\lambda_{\mathrm{linear}\,r}\big|_{\mathrm P}
\right)}.
}
\tag{4.42}
```

The complete triplet slot through quadratic fermions is

```math
\boxed{
\begin{aligned}
Y_{\mathrm{linear}\,ij}\big|_{\mathrm P}
={}&L^{-1}\square^C\left(
\frac{L}{\sqrt2}\delta_{ij}
\right)\\
&-\frac1{\sqrt2}L^{-2}\delta^{km}
\mathcal D_aL_{k(i}\big|_{\mathrm P}
\mathcal D^aL_{j)m}\big|_{\mathrm P}\\
&-\frac1{\sqrt2}L^{-2}\delta_{ij}N^2
-\frac1{\sqrt2}L^{-2}\delta_{ij}E_aE^a\\
&+\sqrt2L^{-2}E_a\delta_{k(i}
\mathcal D^aL_{j)}{}^k\big|_{\mathrm P}\\
&+\frac1{24\sqrt2}\delta_{ij}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\left(
\widehat G^{ab}
+\frac16\varepsilon^{abfgh}\widehat H_{fgh}
\right)\\
&+2\sqrt2\delta_{ij}D\big|_{\mathrm P}\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l\\
&+\frac32L^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\big|_{\mathrm P}\varphi_{j)}
+8iL^{-1}\delta_{ij}\delta_{kl}
\bar\chi^k\big|_{\mathrm P}\varphi^l\\
&+\sqrt2L^{-2}\delta_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\big|_{\mathrm P}\\
&-\frac32L^{-3}\delta_{k(i}\delta^{lm}
\bar\varphi^k
\not{\mathcal D}L_{j)l}\big|_{\mathrm P}\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\big|_{\mathrm P}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\big|_{\mathrm P}\varphi_m\\
&+\frac{i}{4\sqrt2}L^{-2}\delta_{ij}
\bar\varphi\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi\\
&+O(\text{four fermions}).
\end{aligned}
}
\tag{4.43}
```

Each numerical coefficient in (4.43) follows by substituting
$`L_{ij}=L\delta_{ij}/\sqrt2`$ into (4.36).  Three representative steps are

```math
\begin{aligned}
-3iNL^{-5}L_{ij}L^{kl}
&\longrightarrow
-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl},\\
16iL^{-3}L_{ij}L_{kl}
&\longrightarrow
+8iL^{-1}\delta_{ij}\delta_{kl},\\
-3L^{-5}L_{k(i}L^{lm}
&\longrightarrow
-\frac32L^{-3}\delta_{k(i}\delta^{lm}.
\end{aligned}
\tag{4.44}
```

The field-strength slot is

```math
\boxed{
\begin{aligned}
\widehat F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
={}&4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+\sqrt2\delta_{ij}
\widehat R_{\mu\nu}{}^{ij}(V)\\
&+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\big|_{\mathrm P}
\mathcal D_{\nu]}L_{\ell p}\big|_{\mathrm P}\\
&-\sqrt2\mathcal D_{[\mu}\left(
L^{-2}\delta_{ij}
\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)\\
&-iL^{-1}\bar\varphi^i
\widehat R_{\mu\nu i}(Q).
\end{aligned}
}
\tag{4.45}
```

Its ordinary field strength is obtained from (3.14):

```math
\boxed{
\begin{aligned}
F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
={}&\widehat F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
+\bar\psi_{[\mu}{}^i\gamma_{\nu]}
\lambda_{\mathrm{linear}\,i}\big|_{\mathrm P}\\
&-iL^{-1}N
\bar\psi_{[\mu}{}^i\psi_{\nu]i}
+O(\text{four fermions}).
\end{aligned}
}
\tag{4.46}
```

The bilinear part of $`\rho_{\mathrm{linear}}`$ in the last supercovariant
completion would be quartic and is the only part dropped in (4.46).

<a id="410-gauge-fixed-effective-slots"></a>

### Gauge-fixed effective slots

Now, and only now, add the separately evaluated defining vector.  Equations
(4.5), (4.10), and (4.16) give

```math
\boxed{
\begin{aligned}
\rho_{\mathrm{eff}}\big|_{\mathrm P}
&=\rho_{\mathrm{linear}}\big|_{\mathrm P}+2g,\\
\lambda_{\mathrm{eff}\,i}\big|_{\mathrm P}
&=\lambda_{\mathrm{linear}\,i}\big|_{\mathrm P},\\
Y_{\mathrm{eff}\,ij}\big|_{\mathrm P}
&=Y_{\mathrm{linear}\,ij}\big|_{\mathrm P}
-g^2L_{ij},\\
\widehat F_{\mathrm{eff}\,\mu\nu}\big|_{\mathrm P}
&=\widehat F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
+2g\widehat G_{\mu\nu}\big|_{\mathrm P}.
\end{aligned}
}
\tag{4.47}
```

The third line follows from

```math
2gY_{ij}\big|_{\mathrm P}
=2g\left(-\frac g2L_{ij}\right)
=-g^2L_{ij}.
\tag{4.48}
```

The ordinary effective field strength contains a useful cancellation:

```math
\begin{aligned}
F_{\mathrm{eff}\,\mu\nu}\big|_{\mathrm P}
={}&\widehat F_{\mathrm{linear}\,\mu\nu}
+2g\left(
G_{\mu\nu}
+\frac{i}{2}\bar\psi_{[\mu}{}^i\psi_{\nu]i}
\right)\\
&+\bar\psi_{[\mu}{}^i\gamma_{\nu]}
\lambda_{\mathrm{linear}\,i}
-\frac{i}{2}\left(
\rho_{\mathrm{linear}}+2g
\right)
\bar\psi_{[\mu}{}^i\psi_{\nu]i}\\
={}&F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
+2gG_{\mu\nu}
+O(\text{four fermions}).
\end{aligned}
\tag{4.49}
```

Thus the $`+ig\bar\psi_{[\mu}\psi_{\nu]}`$ from
$`2g\widehat G_{\mu\nu}`$ cancels the same term in
$`-\tfrac{i}{2}(2g)\bar\psi_{[\mu}\psi_{\nu]}`$.  The boundary
representative must use the ordinary result in the final line of (4.49).

<a id="5-the-gauged-two-derivative-action"></a>

## The Gauged Two-Derivative Action

<a id="51-compact-one-density-form"></a>

### Compact one-density form

Inserting the effective slots into the unchanged density gives

```math
\boxed{
\begin{aligned}
e^{-1}\mathcal L_{2\partial}^{\mathrm{Gold}}
\doteq-2\Bigg\{&
\frac{L}{\sqrt2}\delta^{ij}
Y_{\mathrm{eff}\,ij}\big|_{\mathrm P}\\
&+i\left(
\bar\lambda_{\mathrm{eff}}{}^i\big|_{\mathrm P}
\varphi_i
\right)\\
&-\frac{L}{2\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^a
\lambda_{\mathrm{eff}}{}^j\big|_{\mathrm P}\\
&+\frac12F_{\mathrm{eff}\,\mu\nu}\big|_{\mathrm P}
E^{\mu\nu}\\
&+\rho_{\mathrm{eff}}\big|_{\mathrm P}
\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\right)
\Bigg\}.
\end{aligned}
}
\tag{5.1}
```

The bar in the second line acts only on the complete raised spinor
$`\lambda_{\mathrm{eff}}{}^i`$.  The prefactor $`i`$ multiplies the entire
NW--SE contraction with $`\varphi_i`$.

Equation (5.1), together with the explicit slot equations (4.39)--(4.49),
is the compact exact answer at the certified order.  To make every term
visible without searching backward, the next subsections expand its five
density contributions.

<a id="52-triplet-contribution"></a>

### Triplet contribution

The triplet part of (5.1) is

```math
\begin{aligned}
&-2\frac{L}{\sqrt2}\delta^{ij}
Y_{\mathrm{eff}\,ij}\big|_{\mathrm P}\\
&=-2\frac{L}{\sqrt2}\delta^{ij}
\Bigg\{
L^{-1}\square^C\left(
\frac{L}{\sqrt2}\delta_{ij}
\right)\\
&\quad-\frac1{\sqrt2}L^{-2}\delta^{km}
\mathcal D_aL_{k(i}\big|_{\mathrm P}
\mathcal D^aL_{j)m}\big|_{\mathrm P}\\
&\quad-\frac1{\sqrt2}L^{-2}\delta_{ij}N^2
-\frac1{\sqrt2}L^{-2}\delta_{ij}E_aE^a\\
&\quad+\sqrt2L^{-2}E_a\delta_{k(i}
\mathcal D^aL_{j)}{}^k\big|_{\mathrm P}\\
&\quad+\frac1{24\sqrt2}\delta_{ij}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\left(
\widehat G^{ab}
+\frac16\varepsilon^{abfgh}\widehat H_{fgh}
\right)\\
&\quad+2\sqrt2\delta_{ij}D\big|_{\mathrm P}\\
&\quad+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l\\
&\quad+\frac32L^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&\quad-16iL^{-1}\bar\chi_{(i}\big|_{\mathrm P}\varphi_{j)}
+8iL^{-1}\delta_{ij}\delta_{kl}
\bar\chi^k\big|_{\mathrm P}\varphi^l\\
&\quad+\sqrt2L^{-2}\delta_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\big|_{\mathrm P}\\
&\quad-\frac32L^{-3}\delta_{k(i}\delta^{lm}
\bar\varphi^k
\not{\mathcal D}L_{j)l}\big|_{\mathrm P}\varphi_m\\
&\quad+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\big|_{\mathrm P}\varphi_{j)}\\
&\quad+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\big|_{\mathrm P}\varphi_m\\
&\quad+\frac{i}{4\sqrt2}L^{-2}\delta_{ij}
\bar\varphi\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi\\
&\quad-g^2\frac{L}{\sqrt2}\delta_{ij}
\Bigg\}
+O(\text{four fermions}).
\end{aligned}
\tag{5.2}
```

The final line is precisely the defining-vector auxiliary contribution to
the effective triplet.  Contracting it gives

```math
-2\frac{L}{\sqrt2}\delta^{ij}
\left(-g^2\frac{L}{\sqrt2}\delta_{ij}\right)
=+2g^2L^2,
\tag{5.3}
```

where $`\delta^{ij}\delta_{ij}=2`$.

<a id="53-barred-spinor-contribution"></a>

### Barred-spinor contribution

There is no defining-gaugino remainder after $`\psi^i=0`$.  The complete
barred-spinor contribution is

```math
\boxed{
-2i\left[
\overline{\left(
\varepsilon^{ir}
\lambda_{\mathrm{linear}\,r}\big|_{\mathrm P}
\right)}\varphi_i
\right],
}
\tag{5.4}
```

where the entire unbarred spinor inside the overline is

```math
\begin{aligned}
\varepsilon^{ir}\Bigg\{&
-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_r\big|_{\mathrm P}\\
&+i\sqrt2\delta_{rs}\gamma^\mu
\Bigg[
\Bigg(
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg)\psi_\mu{}^s\\
&\hspace{8em}
-\phi_\mu{}^s
-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}
\Bigg]\\
&+\frac1{2L}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi_r\\
&-\sqrt2NL^{-2}\delta_{rs}\varphi^s\\
&+2iL^{-3}\left[
\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{st}\varphi_t
-\frac{L}{\sqrt2}\delta_{rs}\not E\,\varphi^s
\right]\\
&+\sqrt2g\delta_{rs}\varphi^s
\Bigg\}.
\end{aligned}
\tag{5.5}
```

Equations (5.4)--(5.5) are intentionally factorized at the Majorana bar. This
is not an omitted term: it is the unambiguous expansion of
$`\bar\lambda^i`$.  Expanding the bar further requires reversing every
Grassmann product and applying the fixed-index or contracted flip rule term
by term; no physical information is gained by hiding that operation in one
long line.

<a id="54-gravitino--spinor-contribution"></a>

### Gravitino--spinor contribution

The third density term gives

```math
\begin{aligned}
&+\frac{L}{\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^a\varepsilon^{jr}
\Bigg\{
-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_r\big|_{\mathrm P}\\
&\quad+i\sqrt2\delta_{rs}\gamma^\mu
\Bigg[
\Bigg(
\frac14\gamma^{bc}\widehat G_{bc}
-\frac18\gamma^{bc}\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)
\Bigg)\psi_\mu{}^s\\
&\hspace{10em}
-\phi_\mu{}^s
-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}
\Bigg]\\
&\quad+\frac1{2L}\gamma^{bc}
\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)\varphi_r\\
&\quad-\sqrt2NL^{-2}\delta_{rs}\varphi^s\\
&\quad+2iL^{-3}\left[
\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{st}\varphi_t
-\frac{L}{\sqrt2}\delta_{rs}\not E\,\varphi^s
\right]\\
&\quad+\sqrt2g\delta_{rs}\varphi^s
\Bigg\}
+O(\text{four fermions}).
\end{aligned}
\tag{5.6}
```

The overall plus sign in (5.6) is the product of the outer $`-2`$ and the
$`-1/2`$ in the density.

<a id="55-field-strength-contribution"></a>

### Field-strength contribution

Using the ordinary field strength (4.49), the fourth density term is

```math
\begin{aligned}
&-E^{\mu\nu}\Bigg\{
4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+\sqrt2\delta_{ij}\widehat R_{\mu\nu}{}^{ij}(V)\\
&\quad+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\big|_{\mathrm P}
\mathcal D_{\nu]}L_{\ell p}\big|_{\mathrm P}\\
&\quad-\sqrt2\mathcal D_{[\mu}\left(
L^{-2}\delta_{ij}
\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)
-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)\\
&\quad+\bar\psi_{[\mu}{}^i\gamma_{\nu]}
\lambda_{\mathrm{linear}\,i}\big|_{\mathrm P}
-iL^{-1}N\bar\psi_{[\mu}{}^i\psi_{\nu]i}\\
&\quad+2gG_{\mu\nu}
\Bigg\}
+O(\text{four fermions}).
\end{aligned}
\tag{5.7}
```

The remaining $`\lambda_{\mathrm{linear}\,i}|_{\mathrm P}`$ in (5.7) is
exactly the full expression (4.40).  Writing it again would merely duplicate
all six lines inside the same braces; no component is suppressed.

Modulo the boundary in (3.3), its explicit gauging term is

```math
-2gG_{\mu\nu}E^{\mu\nu}
\doteq-4gE^aC_a.
\tag{5.8}
```

<a id="56-scalar-slot-contribution"></a>

### Scalar-slot contribution

The last density term can be multiplied out without ambiguity.  Through
quadratic fermions it is

```math
\begin{aligned}
&-2\left(
2L^{-1}N
+\frac{i}{\sqrt2}L^{-2}\delta_{ij}
\bar\varphi^i\varphi^j
+2g
\right)\\
&\quad\times\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\right)\\
={}&-4L^{-1}N^2
-2L^{-1}N\bar\psi_a{}^i\gamma^a\varphi_i\\
&-\frac{iN}{\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
-i\sqrt2L^{-2}N\delta_{ij}
\bar\varphi^i\varphi^j\\
&-4gN
-2g\bar\psi_a{}^i\gamma^a\varphi_i
-\frac{igL}{\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\\
&+O(\text{four fermions}).
\end{aligned}
\tag{5.9}
```

The last line is the quadratic-fermion part of the defining-vector BF
remainder.  Its bars and its factors of $`i`$ have explicit scope.

<a id="57-one-continuous-explicit-lagrangian"></a>

### One continuous explicit Lagrangian

Collecting (5.2), (5.4), (5.6), (5.7), and the unmultiplied form of (5.9)
gives the specified file-04-style expression.  The first large brace is the
2016 linear composite evaluated on the gauged Dilaton--Weyl data.  The final
brace is the component expansion of the $`2gV_{\mathrm{defining}}`$ part of
the same vector argument.

```math
\boxed{
\begin{aligned}
e^{-1}\mathcal L_{2\partial}^{\mathrm{Gold}}
\doteq-2\Bigg\{&
\frac{L}{\sqrt2}\delta^{ij}
\Bigg[
L^{-1}\square^C\left(
\frac{L}{\sqrt2}\delta_{ij}
\right)\\
&-\frac1{\sqrt2}L^{-2}\delta^{km}
\mathcal D_aL_{k(i}\big|_{\mathrm P}
\mathcal D^aL_{j)m}\big|_{\mathrm P}\\
&-\frac1{\sqrt2}L^{-2}\delta_{ij}N^2
-\frac1{\sqrt2}L^{-2}\delta_{ij}E_aE^a\\
&+\sqrt2L^{-2}E_a\delta_{k(i}
\mathcal D^aL_{j)}{}^k\big|_{\mathrm P}\\
&+\frac1{24\sqrt2}\delta_{ij}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\left(
\widehat G^{ab}
+\frac16\varepsilon^{abfgh}\widehat H_{fgh}
\right)\\
&+2\sqrt2\delta_{ij}D\big|_{\mathrm P}\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l\\
&+\frac32L^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\big|_{\mathrm P}\varphi_{j)}
+8iL^{-1}\delta_{ij}\delta_{kl}
\bar\chi^k\big|_{\mathrm P}\varphi^l\\
&+\sqrt2L^{-2}\delta_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\big|_{\mathrm P}\\
&-\frac32L^{-3}\delta_{k(i}\delta^{lm}
\bar\varphi^k
\not{\mathcal D}L_{j)l}\big|_{\mathrm P}\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\big|_{\mathrm P}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\big|_{\mathrm P}\varphi_m\\
&+\frac{i}{4\sqrt2}L^{-2}\delta_{ij}
\bar\varphi\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi
\Bigg]\\[2pt]
&+i\left[
\overline{\left(
\varepsilon^{ir}\lambda_{\mathrm{linear}\,r}
\big|_{\mathrm P}
\right)}\varphi_i
\right]\\[2pt]
&-\frac{L}{2\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^a\varepsilon^{jr}
\Bigg[
-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_r\big|_{\mathrm P}\\
&\quad+i\sqrt2\delta_{rs}\gamma^\mu
\Bigg\{
\Bigg[
\frac14\gamma^{bc}\widehat G_{bc}
-\frac18\gamma^{bc}\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)
\Bigg]\psi_\mu{}^s\\
&\qquad\qquad
-\phi_\mu{}^s
-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}
\Bigg\}\\
&\quad+\frac1{2L}\gamma^{bc}
\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)\varphi_r\\
&\quad-\sqrt2NL^{-2}\delta_{rs}\varphi^s\\
&\quad+2iL^{-3}\Bigg[
\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{st}\varphi_t\\
&\qquad\qquad
-\frac{L}{\sqrt2}\delta_{rs}\not E\,\varphi^s
\Bigg]
+\sqrt2g\delta_{rs}\varphi^s
\Bigg]\\[2pt]
&+\frac12E^{\mu\nu}\Bigg[
4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+\sqrt2\delta_{ij}\widehat R_{\mu\nu}{}^{ij}(V)\\
&\quad+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\big|_{\mathrm P}
\mathcal D_{\nu]}L_{\ell p}\big|_{\mathrm P}\\
&\quad-\sqrt2\mathcal D_{[\mu}\left(
L^{-2}\delta_{ij}
\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)
-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)\\
&\quad+\bar\psi_{[\mu}{}^i\gamma_{\nu]}
\Bigg\{
-2iL^{-1}\gamma^\rho
\mathcal D_\rho\varphi_i\big|_{\mathrm P}\\
&\qquad+i\sqrt2\delta_{ij}\gamma^\rho
\Bigg[
\Bigg(
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg)\psi_\rho{}^j\\
&\hspace{13em}
-\phi_\rho{}^j
-\frac{gL}{2\sqrt2}\delta^{jk}\psi_{\rho k}
\Bigg]\\
&\qquad+\frac1{2L}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi_i\\
&\qquad-\sqrt2NL^{-2}\delta_{ij}\varphi^j\\
&\qquad+2iL^{-3}\Bigg[
\left(\not{\mathcal D}L_{ij}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{jk}\varphi_k\\
&\hspace{12em}
-\frac{L}{\sqrt2}\delta_{ij}\not E\,\varphi^j
\Bigg]
+\sqrt2g\delta_{ij}\varphi^j
\Bigg\}\\
&\quad-iL^{-1}N
\bar\psi_{[\mu}{}^i\psi_{\nu]i}
\Bigg]\\[2pt]
&+\left(
2L^{-1}N
+\frac{i}{\sqrt2}L^{-2}\delta_{ij}
\bar\varphi^i\varphi^j
\right)\\
&\quad\times\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\right)
\Bigg\}\\[2pt]
&-4g\Bigg\{
\frac12G_{\mu\nu}E^{\mu\nu}
+N-\frac g2L^2\\
&\qquad+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\Bigg\}\\
&+O(\text{four fermions}).
\end{aligned}
}
\tag{5.10}
```

In the second density term of (5.10), the complete expression inside the
bar is Eq. (5.5).  In every unconjugated occurrence it is written out in
full.  The objects $`D|_{\mathrm P}`$, $`\chi|_{\mathrm P}`$,
$`\mathcal D_\mu L_{ij}|_{\mathrm P}`$,
$`\mathcal D_\mu\varphi_i|_{\mathrm P}`$, and
$`L_{ij}\square^CL^{ij}|_{\mathrm P}`$ are explicitly given in
(4.21), (4.24), (4.27), (4.30), and (4.32).  Thus (5.10) is continuous and
contains no unlisted composite slot.

The last brace in (5.10) is worth reading on its own:

```math
\boxed{
\begin{aligned}
-4g\,e^{-1}\mathcal L_{\mathrm{VL}}
[V_{\mathrm{defining}};\mathbb L]
\doteq{}&-4gP^aC_a-4gN+2g^2L^2\\
&-2g\bar\psi_a{}^i\gamma^a\varphi_i\\
&-\frac{igL}{\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j.
\end{aligned}
}
\tag{5.11}
```

The ordinary current $`P^a`$ is (3.9)--(3.10). To compare (5.11)
with the $`-2gG_{\mu\nu}E^{\mu\nu}`$ term in (5.10), the exact local
boundary identity and the completion are

```math
\begin{aligned}
-4geC_aP^a
&=-2geG_{\mu\nu}E^{\mu\nu}
 +\frac g3\partial_\nu
  (e\varepsilon^{\mu\nu\rho\sigma\lambda}C_\mu E_{\rho\sigma\lambda}),\\
-4gC_a(P^a-E^a)
&=-2igC_a\bar\psi_b\gamma^{ba}\varphi
 -gC_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
\tag{5.11a}
```

The earlier $`-4gC_aE^a`$ display omitted the second line of (5.11a).
Equation (5.10) and the coefficients of the defining-vector density
already contain the correct contribution and are unchanged.

It is not an independently added cosmological invariant.  It is the
algebraic expansion of the $`2gV_{\mathrm{defining}}`$ component of the one
effective vector in (4.4).

<a id="58-precisely-what-complete-means-here"></a>

### Precisely what “complete” means here

Equation (5.10) is exact in all bosons and complete through quadratic
fermions.  The following are present but retained in exact source-
supercovariant notation:

```math
\omega_\mu{}^{ab},\qquad
\phi_\mu{}^i,\qquad
f_\mu{}^a,\qquad
\widehat R_{\mu\nu}{}^i(Q),\qquad
\widehat R_{\mu\nu}{}^{ij}(V).
\tag{5.12}
```

Their source definitions, including the project-corrected curvature sign,
are fixed in Section 3.4.  Therefore the action is not described as a fully
elementary expansion in ordinary derivatives.

The only omitted terms are:

1. the two cubic terms in (4.34), because the density makes them quartic;
2. the final three quartic terms in (4.36);
3. the bilinear part of $`\rho`$ in the gravitino completion of
   $`F_{\mu\nu}`$, because it is quartic;
4. source terms denoted $`O(\text{three fermions})`$ in $`\chi^i`$, which
   first contribute at four-fermion order in this action.

No zero-fermion or two-fermion term is omitted.

<a id="6-independent-bosonic-reconstruction"></a>

## Independent Bosonic Reconstruction

Fermions are set to zero only in this section.  The calculation starts from
the evaluated slots, not from Gold Eq. (26).

<a id="61-derivative-and-curvature-blocks"></a>

### Derivative and curvature blocks

At bosonic order,

```math
\begin{aligned}
\mathcal D_\mu L_{ij}
={}&\frac1{\sqrt2}\delta_{ij}\partial_\mu L
-\sqrt2L\,V'_{\mu(i}{}^k\delta_{j)k},\\
\mathcal D_\mu L_{ij}\mathcal D^\mu L^{ij}
={}&(\partial L)^2
+2L^2V_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu},\\
L_{ij}\mathcal D_\mu L^{ij}
={}&L\partial_\mu L,\\
\delta^{ij}\delta^{km}
\mathcal D_\mu L_{k(i}\mathcal D^\mu L_{j)m}
={}&(\partial L)^2
-2L^2V_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu}.
\end{aligned}
\tag{6.1}
```

Using (4.28) to raise corrected (4.27), the connection term in
(4.32) evaluates to

```math
\sqrt2\delta_{ij}V_a{}^i{}_k\mathcal D^aL^{jk}
=-2LV_a^{\prime\,ij}V_{ij}^{\prime\,a}.
```

The traced first derivative is $`\partial_aL`$, so the bosonic
conformal d'Alembertian is

```math
\begin{aligned}
L^{-1}L_{ij}\square^CL^{ij}\big|_{\rm bos,P}
&=\Box L+\sqrt2\delta_{ij}V_a{}^i{}_k\mathcal D^aL^{jk}
 +6Lf_a{}^a\\
&=\Box L-2LV_a^{\prime\,ij}V_{ij}^{\prime\,a}+6Lf_a{}^a.
\end{aligned}
```

Here $`\Box L`$ is the ordinary Levi-Civita divergence, and the
same boundary convention used elsewhere in this section gives

```math
L^{-1}L_{ij}\square^CL^{ij}
\doteq-2LV_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu}
+6Lf_a{}^a.
\tag{6.2}
```

The second derivative term of the triplet contributes

```math
-\frac1{2L}\delta^{ij}\delta^{km}
\mathcal D_\mu L_{k(i}\mathcal D^\mu L_{j)m}
=-\frac12L^{-1}(\partial L)^2
+LV_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu}.
\tag{6.3}
```

Using $`f_a{}^a=-R/16`$, the derivative block inside one unnormalized BF
density is

```math
-\frac38LR
-\frac12L^{-1}(\partial L)^2
-LV_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu}.
\tag{6.4}
```

Multiplication by the target factor $`-2`$ gives

```math
\frac34LR
+L^{-1}(\partial L)^2
+2LV_\mu^{\prime\,ij}V_{ij}^{\prime\,\mu}.
\tag{6.5}
```

Thus (6.2)--(6.5) and the $`+2LV'^2`$ term in (6.21) retain their
displayed coefficients after the derivative-sign correction.
The two-derivative product in (6.17) also retains its coefficient:
the $`V'V'`$ part contains two connection factors, and its
$`\partial L\,V'`$ cross contractions vanish by tracelessness.

<a id="62-the-t--d-block"></a>

### The $`T`$--$`D`$ block

The bosonic part of the relevant trace of (4.43) is

```math
\frac83LT^2+4LD.
\tag{6.6}
```

For completeness, derive the following equation directly from
[source bibliography](../../../references/bibliography.md),
Eq. (5.4), PDF p. 16. Before gauge fixing, its bosonic part reads

```math
\begin{aligned}
D={}&\frac14\sigma^{-1}\square^C\sigma
+\frac18\sigma^{-2}(\mathcal D\sigma)^2
-\frac1{16}\sigma^{-2}G^2\\
&-\frac{26}{3}T^2+2\sigma^{-1}G\mathbin{\cdot}T
+\frac14\sigma^{-2}Y^{ij}Y_{ij}
+\frac g4\sigma^{-2}N.
\end{aligned}
\tag{6.6a}
```

The defining-vector auxiliary is CO Eq. (5.2), not the composite triplet
slot. On the target slice Y=-gL/2, so Y²=g²L²/4. Also
$`\mathcal D_a\sigma=0`$ bosonically but
$`\square^C\sigma=2f_a{}^a=-R/8`$, by OP (2.10), PDF p. 7.
Thus the first, penultimate and last terms give respectively
−R/32, g²L²/16 and gN/4, yielding

```math
D\big|_{\mathrm{bos,P}}
=-\frac1{32}R
-\frac1{16}G^2
-\frac{26}{3}T^2
+2G\mathbin{\cdot}T
+\frac g4N
+\frac{g^2}{16}L^2,
\tag{6.7}
```

its ungauged tensor part is

```math
\begin{aligned}
\frac83LT^2+4LD\big|_{g=0}
={}&-\frac18LR-\frac14LG^2
-32LT^2+8LG\mathbin{\cdot}T.
\end{aligned}
\tag{6.8}
```

Substitute (4.18):

```math
\begin{aligned}
-32T^2+8G\mathbin{\cdot}T
={}&-\frac12\left(
G+\frac16\varepsilon H
\right)^2\\
&+G\mathbin{\cdot}\left(
G+\frac16\varepsilon H
\right)\\
={}&\frac12G^2
-\frac12\left(\frac16\varepsilon H\right)^2.
\end{aligned}
\tag{6.9}
```

The epsilon identity (2.3) implies

```math
\left(\frac16\varepsilon_{abcde}H^{cde}\right)
\left(\frac16\varepsilon^{abfgh}H_{fgh}\right)
=-\frac13H_{abc}H^{abc}.
\tag{6.10}
```

Hence

```math
\frac83LT^2+4LD\big|_{g=0}
=-\frac18LR+\frac14LG^2+\frac16LH_{abc}H^{abc}.
\tag{6.11}
```

After the outer $`-2`$, (6.11) combines with (6.5) to give the Einstein,
vector, and three-form terms in the target normalization.  Gold's two-form
dual is

```math
H_{ab}^{\mathrm{Gold}}
=-\frac1{12}\varepsilon_{abcde}H^{cde},
\qquad
\frac16\varepsilon_{abcde}H^{cde}
=-2H_{ab}^{\mathrm{Gold}}.
\tag{6.12}
```

Therefore

```math
-\frac13LH_{abc}H^{abc}
=4L H_{ab}^{\mathrm{Gold}}H_{\mathrm{Gold}}^{ab}.
\tag{6.13}
```

The explicit gauging part of (6.7) yields exactly

```math
-8L\left(\frac g4N+\frac{g^2}{16}L^2\right)
=-2gLN-\frac12g^2L^3.
\tag{6.14}
```

<a id="63-the-n-e-and-connection-blocks"></a>

### The $`N`$, $`E`$, and connection blocks

Before the target outer factor is applied, the triplet and scalar slots give

```math
-L^{-1}N^2+\rho_{\mathrm{linear}}N
=-L^{-1}N^2+2L^{-1}N^2
=+L^{-1}N^2.
\tag{6.15}
```

Thus the target action contains $`-2L^{-1}N^2`$.

The trace of the $`SU(2)`$ curvature and the mixed-index term in (4.45)
combine as

```math
\begin{aligned}
&\sqrt2\delta_{ij}R_{\mu\nu}{}^{ij}(V)
+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{\ell p}\\
&\qquad=2\sqrt2\partial_{[\mu}V_{\nu]}.
\end{aligned}
\tag{6.16}
```

The $`V'V'`$ pieces cancel because

```math
\delta_{km}\varepsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{\ell p}
=2L^2\delta_{ij}V_{[\mu}^{\prime\,k(i}
V_{\nu]k}^{\prime\ \ j)}.
\tag{6.17}
```

The remaining trace-connection coupling is

```math
-2\sqrt2E^{\mu\nu}\partial_\mu V_\nu
\doteq-2\sqrt2E^aV_a.
\tag{6.18}
```

The remaining $`E_a`$ terms reduce to $`-2L^{-1}E_aE^a`$.  Finally, the
ordinary field-strength addition in (4.49) gives

```math
-2gG_{\mu\nu}E^{\mu\nu}
\doteq-4gE^aC_a.
\tag{6.19}
```

The defining-vector scalar and auxiliary terms give

```math
-4gN+2g^2L^2.
\tag{6.20}
```

<a id="64-reconstructed-bosonic-action"></a>

### Reconstructed bosonic action

Adding (6.5), (6.11), and (6.14)--(6.20) gives

```math
\boxed{
\begin{aligned}
e^{-1}\mathcal L_{2\partial}^{\mathrm{Gold}}
\big|_{\mathrm{bos,P}}
={}&L\left(
R-\frac12G_{ab}G^{ab}
+4H_{ab}^{\mathrm{Gold}}H_{\mathrm{Gold}}^{ab}
+2V_a^{\prime\,ij}V^{\prime a}_{ij}
\right)\\
&+L^{-1}\partial_aL\partial^aL
-2L^{-1}E_aE^a
-2\sqrt2E^aV_a
-2L^{-1}N^2\\
&-4gE^aC_a
-2gLN
-4gN\\
&-\frac12g^2L^3
+2g^2L^2.
\end{aligned}
}
\tag{6.21}
```

Here the three-form entering (6.12) is the gauged one,

```math
H_{\mu\nu\rho}
=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}.
\tag{6.22}
```

Equation (6.21) agrees term by term with Gold Eq. (26). The overall
normalization is an input calibrated in §4.2; its agreement is not an
independent test. The relative gauging coefficients are then derived
from the defining-vector remainder and (6.6a), not fitted to a potential.
No relative gauging coefficient in
Sections 4 or 5 was chosen from (6.21).

<a id="7-ungauged-limit"></a>

## Ungauged Limit

Set $`g=0`$ before imposing any field equation.  Then

```math
\begin{aligned}
\widehat H_{\mu\nu\rho}
&\longrightarrow
3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
-\frac34\bar\psi_{[\mu}{}^i\gamma_\nu\psi_{\rho]i},\\
\mathcal D_\mu\psi^i\big|_{\mathrm P}
&\longrightarrow
\left(
\frac14\gamma\mathbin{\cdot}\widehat G
-\gamma\mathbin{\cdot}T
\right)\psi_\mu{}^i-\phi_\mu{}^i,\\
\chi^i\big|_{\mathrm P}
&\longrightarrow
\frac{i}{8}\gamma^\mu
\mathcal D_\mu\psi^i\big|_{\mathrm P},\\
D\big|_{\mathrm P}
&\longrightarrow D\big|_{\mathrm{ungauged,P}}.
\end{aligned}
\tag{7.1}
```

All explicit residual terms in (5.11) vanish, and (5.1) becomes

```math
\boxed{
\left.\mathcal L_{2\partial}^{\mathrm{Gold}}\right|_{g=0}
=-2\mathcal L_{\mathrm{VL}}
[V_{\mathrm{linear}};\mathbb L].
}
\tag{7.2}
```

This is twice the corrected Özkan--Pang density normalization. At the slot level:

| Gauged object | $`g\to0`$ result | Ungauged match |
| --- | --- | --- |
| $`\rho_{\mathrm{eff}}`$ | $`\rho_{\mathrm{linear}}`$ | scalar slot |
| $`\lambda_{\mathrm{eff}\,i}`$ | ungauged (4.40) | spinor slot |
| $`Y_{\mathrm{eff}\,ij}`$ | ungauged 2016 source-ordered (4.43) | triplet slot |
| $`\widehat F_{\mathrm{eff}}`$ | ungauged (4.45) | field-strength slot |
| density | $`-2\mathcal L_{\mathrm{VL}}`$ | twice OP normalization |

<a id="8-algebraic-and-convention-audits"></a>

## Algebraic and Convention Audits

<a id="81-weyl-weights"></a>

### Weyl weights

Before gauge fixing every density monomial has weight five:

| Monomial | Weight |
| --- | ---: |
| $`Y^{ij}L_{ij}`$ | $`2+3=5`$ |
| $`i\bar\lambda^i\varphi_i`$ | $`3/2+7/2=5`$ |
| $`\bar\psi_a\gamma^a\lambda L`$ | $`1/2+3/2+3=5`$ |
| $`A_aE^a`$ | $`1+4=5`$ |
| $`\rho N`$ | $`1+4=5`$ |
| $`\rho\bar\psi_a\gamma^a\varphi`$ | $`1+1/2+7/2=5`$ |
| $`\rho\bar\psi_a\gamma^{ab}\psi_bL`$ | $`1+1/2+1/2+3=5`$ |

Representative composite checks are

```math
\begin{aligned}
w(2L^{-1}N)&=-3+4=1=w(\rho),\\
w(L^{-1}\not{\mathcal D}\varphi)
&=-3+1+\frac72=\frac32=w(\lambda),\\
w(L^{-1}\square^CL_{ij})&=-3+2+3=2=w(Y),\\
w\left(\mathcal D_{[\mu}(L^{-1}E_{\nu]})\right)
&=1-3+4=2=w(\widehat F).
\end{aligned}
\tag{8.1}
```

<a id="82-index-and-grassmann-checks"></a>

### Index and Grassmann checks

- Every free index of (4.40) is lower, as required by the density.
- The two $`Y`$ objects are never identified: defining $`Y^{ij}`$ enters
  only through (4.10), while composite $`Y_{\mathrm{linear}\,ij}`$ is
  (4.43).
- The mixed-index field-strength sign follows (2.6) and (4.38).
- Every retained action monomial is Grassmann even.
- The factorized bar (5.4) prevents an unrecorded reversal of Grassmann
  order.
- Fixed-index and NW--SE flip identities are separated in (2.7)--(2.8).

<a id="83-gauge-preservation-check"></a>

### Gauge-preservation check

Substitute (4.13) and (4.10) into (4.12):

```math
\begin{aligned}
\delta\psi^i\big|_{\mathrm P}
={}&-\frac14\gamma\mathbin{\cdot}\widehat G\,\epsilon^i
+\gamma\mathbin{\cdot}T\,\epsilon^i
+\frac{gL}{2\sqrt2}\delta^{ij}\epsilon_j\\
&+\left(
-\gamma\mathbin{\cdot}T
+\frac14\gamma\mathbin{\cdot}\widehat G
\right)\epsilon^i
-\frac{gL}{2\sqrt2}\delta^{ij}\epsilon_j\\
=0.
\end{aligned}
\tag{8.2}
```

Thus the dilatino gauge is preserved. The corrected SU(2) compensator
preserves the triplet direction by (4.14a)--(4.14b). For the K compensator,

```math
\begin{aligned}
\delta b_\mu
&=\frac i2\bar\epsilon\phi_\mu-2\bar\epsilon\gamma_\mu\chi
 +\frac i2\bar\eta\psi_\mu+2\Lambda_{K\mu}\\
&=\frac i2\bar\epsilon\phi_\mu-2\bar\epsilon\gamma_\mu\chi
 +\frac i2\bar\eta\psi_\mu
 -\frac i2\bar\epsilon\phi_\mu-\frac i2\bar\eta\psi_\mu
 +2\bar\epsilon\gamma_\mu\chi=0.
\end{aligned}
\tag{8.2a}
```

Preserving $`\psi^i=0`$ does not imply
$`\mathcal D_\mu\psi^i=0`$; Eq. (4.19) remains in the action.

<a id="84-dimensional-and-limiting-checks"></a>

### Dimensional and limiting checks

After $`\sigma=1`$ fixes dilatations, $`g`$ carries the physical inverse-
length scale.  Every line of (6.21) has the same mass dimension.  The limit
$`g\to0`$ is regular and is taken directly in the action, not in a divided
field equation.

<a id="10-final-result-and-certification-boundary"></a>

## Final Result and Certification Boundary

The separate mappings are (4.1) and (4.2), their component sum is (4.5),
and their gauge-fixed effective value is (4.47).  The compact action is
(5.1), while the readable continuous component action is (5.10).

The final certification is

```math
\boxed{
\mathcal L_{2\partial}^{\mathrm{Gold}}
=-2\mathcal L_{\mathrm{VL}}
[V_{\mathrm{linear}}+2gV_{\mathrm{defining}};\mathbb L],
}
\tag{10.1}
```

evaluated with the 2016 map (4.33)--(4.37), the gauged composites
(4.16)--(4.24), and the target gauge (1.1).

This is the quadratic-fermion source-supercovariant construction, exact
bosonically, conditional on the explicitly recorded project source repairs.
The correction note §§4,8 gives the matrix-level check of the fluxless
quadratic descendant. Dependent connections retain their defined
supercovariant form at the stated physical fermion order.
The defining-vector equations are used only for the DW construction;
no target auxiliary is eliminated in this nonlinear file. The descendants
in files 06 and 07 carry separate v2 locks and their own assumptions.
