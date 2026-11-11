# Defining-vector component anchor for the gauged two-derivative construction

> **Scope clarification, 2026-09-08:** the defining-vector Euler equations
> are used to construct the gauged Dilaton–Weyl multiplet and to reduce
> the Standard-Weyl parent. This is not an identity of the parent before
> imposing that map. No equation for an independent target auxiliary is
> used here. The word off-shell below refers to the target DW field content.
> This v2 changes the scope/provenance, not the relative 2g coefficient.

> **Status:** active defining-vector and component-addition anchor  
> **Lock:** `2DER-GAUGED-VDEFINING-COMPONENTS-v2`  
> **Linear-map parent:** `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`  
> **Action status:** no two-derivative Lagrangian is constructed here

<!-- ASSERT_VDEFINING_LOCK: 2DER-GAUGED-VDEFINING-COMPONENTS-v2 -->
<!-- ASSERT_LINEAR_MAP_PARENT: OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2 -->
<!-- ASSERT_ACTION_STATUS: not_constructed -->

## 1. Problem and Target

The completed single-linear-multiplet map is

```math
\left(L_{ij},\varphi_i,E_a,N\right)
\longmapsto
\left(
\rho_{\mathrm{linear}},
\lambda_{\mathrm{linear}\,i},
Y_{\mathrm{linear}\,ij},
\widehat F_{\mathrm{linear}\,\mu\nu}
\right).
\tag{1.1}
```

Its canonical anchor is
`03_single_linear_multiplet_linear_map_anchor.md`, lock
`OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`.

The remaining input needed before constructing the gauged two-derivative
action is the defining vector multiplet

```math
\boxed{
V_{\mathrm{defining}}
=
\left(\sigma,C_\mu,\psi^i,Y^{ij}\right).
}
\tag{1.2}
```

The goals of this document are:

1. anchor every component of (1.2) before gauge fixing;
2. anchor the gauged expression for the defining-vector auxiliary $`Y^{ij}`$;
3. define $`G_{\mu\nu}`$ and $`\widehat G_{\mu\nu}`$ without suppressing
   their fermion content;
4. define clearly $`E_\mu`$, $`E_{\mu\nu}`$, and $`E_{\mu\nu\rho}`$;
5. derive the componentwise addition of $`V_{\mathrm{defining}}`$ to the
   already certified linear map;
6. evaluate only this component data on the target gauge slice.

This is an off-shell component construction. No descendant Poincaré field
equation, auxiliary elimination, dualization, background restriction,
perturbative expansion, or integration by parts is used.

The bosonic definitions are exact. Fermionic expressions are retained
through the complete order displayed by the cited source equations:
$`Y^{ij}`$ and $`\widehat G_{\mu\nu}`$ through quadratic fermions, and
$`\mathcal D_\mu\psi^i`$ through the order required to retain the connection
term $`Y^{ij}\psi_{\mu j}`$.

## 2. Source and Provenance Ledger

| Required datum | Local source | Location |
| --- | --- | --- |
| defining vector multiplet | Coomans--Özkan, `Sources/2013-Coomans-Ozkan-Internally-Gauged-D5-N2-Supergravity.pdf` | Eq. (2.14), PDF p. 7 |
| vector transformations and $`\mathcal D_\mu\psi^i`$ | same | Eqs. (2.15)--(2.16), PDF pp. 7--8 |
| $`G_{\mu\nu}`$ and $`\widehat G_{\mu\nu}`$ | same | Eq. (2.17), PDF p. 8 |
| linear multiplet and constraint | same | Eqs. (2.19)--(2.22), PDF p. 8 |
| three-form and dual two-form representatives | same | Eqs. (2.23)--(2.25), PDF pp. 8--9 |
| $`P^a`$ used in the potential representative | same | Eqs. (3.2)--(3.3), PDF p. 9 |
| gauge-unfixed gauged parent | same | Eq. (5.1), PDF p. 16 |
| defining-vector auxiliary | same | Eq. (5.2), PDF p. 16 |
| gauged three-form completion | same | Eqs. (5.5)--(5.8), PDF pp. 16--17 |
| target BF multiplet identification | Gold et al. 2025, `Sources/2025-Gold-On five-dimensional curvature squared supergravity and holography.pdf` | Eqs. (3)--(4), PDF pp. 5--6 |
| target gauge direction | same | Eqs. (7) and (25), PDF pp. 6 and 14 |
| vector--linear density and boundary representative | corrected Özkan--Pang, `Sources/2013-Ozkan-Supersymmetric Completion of GB.pdf` | Eqs. (3.1)--(3.2), PDF p. 10 |

The relevant source hashes are:

| File | SHA-256 |
| --- | --- |
| Coomans--Özkan PDF | `c65ea0f165ff73a9562a3acdde69c29b7af36206085ef1fa488a0d014c9f367d` |
| Gold et al. 2025 PDF | `027e822a36d6d3c465db44569d393e36577ae80290982158d5f393d4b3af82f5` |
| corrected Özkan--Pang PDF | `4cc005cc0dbd96246e709ef267cf6956d08e64fa8b5910b20cf0549e50e29d20` |
| canonical linear-map anchor | `817cc20787c6730821e7e416551f2154adfc247f7dea37eb66147bbf1afd4975` |

## 3. Convention Ledger

The source is five-dimensional Lorentzian supergravity with

```math
D=5,
\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+).
\tag{3.1}
```

Curved indices are $`\mu,\nu,\ldots=0,\ldots,4`$, tangent indices are
$`a,b,\ldots=0,\ldots,4`$, and $`SU(2)`$ indices are $`i,j=1,2`$.

Antisymmetrization has unit weight:

```math
X_{[\mu\nu]}
=\frac12
\left(X_{\mu\nu}-X_{\nu\mu}\right),
\qquad
X_{[\mu\nu\rho]}
=\frac1{3!}
\sum_{\pi\in S_3}\mathop{\mathrm{sgn}}\nolimits(\pi)
X_{\pi(\mu)\pi(\nu)\pi(\rho)}.
\tag{3.2}
```

The NW--SE convention is

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
\tag{3.3}
```

For a symmetric triplet,

```math
Y_{ij}
=Y^{kl}\varepsilon_{ki}\varepsilon_{lj},
\qquad
L^{ij}
=\varepsilon^{ik}\varepsilon^{j\ell}L_{k\ell}.
\tag{3.4}
```

The vielbein and determinant conventions are

```math
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},
\qquad
e=\det(e_\mu{}^a),
\qquad
e_\mu{}^ae_a{}^\nu=\delta_\mu{}^\nu.
\tag{3.5}
```

The epsilon contraction inherited from the corrected project convention is

```math
\varepsilon_{\mu\nu\rho\alpha\beta}
\varepsilon^{\mu\nu\rho\gamma\delta}
=-3!\,2!\,
\delta_{[\alpha}^{\gamma}
\delta_{\beta]}^{\delta}.
\tag{3.6}
```

All spinors are Grassmann odd and symplectic Majorana. For fixed upper
$`SU(2)`$ indices, the rank-zero flip has sign $`+1`$:

```math
\bar\alpha^i\beta^j
=\bar\beta^j\alpha^i.
\tag{3.7}
```

Thus $`\bar\psi^i\psi^j`$ is symmetric under $`i\leftrightarrow j`$.

Throughout this anchor, $`g`$ denotes the Coomans--Özkan gauging parameter
carried into the target orientation without introducing a second coupling
symbol. Before compensator gauge fixing it is a dimensionless,
Weyl-weight-zero constant:

```math
w(g)=0.
\tag{3.8}
```

## 4. Definitions and Required Identities

### 4.1 Defining-vector components

Coomans--Özkan Eq. (2.14) gives

```math
V_{\mathrm{defining}}
=
\left(\sigma,C_\mu,\psi^i,Y^{ij}\right),
\qquad
Y^{ij}=Y^{ji}.
\tag{4.1}
```

The fields have Weyl weights

```math
w(C_\mu)=0,
\qquad
w(\sigma)=1,
\qquad
w(\psi^i)=\frac32,
\qquad
w(Y^{ij})=2.
\tag{4.2}
```

Here $`\psi^i`$ is the defining-vector gaugino. It is not the gravitino
$`\psi_\mu{}^i`$.

### 4.2 Ordinary and supercovariant field strengths

The ordinary Abelian field strength is

```math
\boxed{
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
}
\tag{4.3}
```

Coomans--Özkan Eq. (2.17) gives

```math
\boxed{
\widehat G_{\mu\nu}
=G_{\mu\nu}
-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\psi_i
+\frac{i}{2}\sigma
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
}
\tag{4.4}
```

The spinor on the right of the gamma matrix in the second term is the
defining gaugino $`\psi_i`$. Both spinors in the final term are gravitini.
The factor $`i/2`$ multiplies that entire gravitino bilinear.

### 4.3 Covariant derivative of the defining gaugino

Coomans--Özkan Eq. (2.16) is

```math
\begin{aligned}
\mathcal D_\mu\psi^i
={}&
\left(
\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}
\right)\psi^i
-V_\mu{}^{ij}\psi_j
\\
&+\frac14\gamma\mathbin{\cdot}\widehat G\,\psi_\mu{}^i
+\frac{i}{2}\not{\mathcal D}\sigma\,\psi_\mu{}^i
+Y^{ij}\psi_{\mu j}
\\
&-\sigma\gamma\mathbin{\cdot}T\,\psi_\mu{}^i
-\sigma\phi_\mu{}^i.
\end{aligned}
\tag{4.5}
```

The $`Y^{ij}\psi_{\mu j}`$ term is part of the definition. It must not be
dropped when the gauge value of $`\psi^i`$ is zero.

### 4.4 The linear-multiplet forms

The fields $`E_a`$, $`E_{\mu\nu}`$, and $`E_{\mu\nu\rho}`$ do not belong to
the defining vector. They are three equivalent presentations associated with
the constrained-vector sector of the external linear multiplet.

| Symbol | Meaning | Independent object? |
| --- | --- | --- |
| $`E_a`$, $`E_\mu`$ | supercovariant constrained vector of the linear multiplet | the original constrained component |
| $`E^{\mu\nu}`$, $`E_{\mu\nu}`$ | two-form dual representative satisfying $`E^\mu=\mathcal D_\nu E^{\mu\nu}`$ | no; a local representative of the same constrained sector |
| $`E_{\mu\nu\rho}`$ | three-form gauge potential whose exterior derivative is dual to $`E^\mu`$ | no; a local solution of the constraint |
| $`P_a`$, $`P_\mu`$ | ordinary-exterior-derivative representative used in the potential form of the density | no; differs from $`E_a`$ by fixed fermion bilinears |
| $`B_{\mu\nu}`$ | dilaton-Weyl two-form | yes, but it is a different field |
| $`C_\mu`$ | defining-vector gauge field | yes, and it is unrelated to the $`E`$-form gauge redundancy |

The tangent-space constrained vector obeys

```math
\boxed{
\mathcal D_aE^a=0.
}
\tag{4.6}
```

Its curved components are defined by the vielbein:

```math
\boxed{
E^\mu=e_a{}^\mu E^a,
\qquad
E_\mu=e_\mu{}^aE_a
=g_{\mu\nu}E^\nu.
}
\tag{4.7}
```

Thus $`E_\mu`$ is a constrained vector. It is not a one-form gauge
potential and it is not the graviphoton $`C_\mu`$.

Locally the constraint is solved by the three-form gauge potential
$`E_{\mu\nu\rho}=E_{[\mu\nu\rho]}`$:

```math
\boxed{
E^\mu
=-\frac1{12}e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}.
}
\tag{4.8}
```

Equivalently,

```math
E^a
=-\frac1{12}e_\mu{}^a e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}.
\tag{4.9}
```

The three-form has the gauge invariance

```math
\boxed{
\delta_\Lambda E_{\mu\nu\rho}
=3\partial_{[\mu}\Lambda_{\nu\rho]}.
}
\tag{4.10}
```

The dual two-form $`E^{\mu\nu}=E^{[\mu\nu]}`$ is defined by

```math
\boxed{
E_{\mu\nu\rho}
=e\,
\varepsilon_{\mu\nu\rho\sigma\lambda}
E^{\sigma\lambda}.
}
\tag{4.11}
```

The lower-index two-form requested for later use is

```math
\boxed{
E_{\mu\nu}
=g_{\mu\rho}g_{\nu\sigma}E^{\rho\sigma}.
}
\tag{4.12}
```

It must not be confused with the independent two-form $`B_{\mu\nu}`$ of the
dilaton-Weyl multiplet. The source also gives

```math
\boxed{
E^a
=e_\mu{}^a
\mathcal D_\nu E^{\mu\nu}.
}
\tag{4.13}
```

The supercovariant divergence appearing here is

```math
\boxed{
\begin{aligned}
\mathcal D_\nu E^{\mu\nu}
={}&
\partial_\nu E^{\mu\nu}
+\frac{i}{2}
\bar\psi_\nu{}^i\gamma^{\mu\nu}\varphi_i
\\
&+\frac14
\bar\psi_\rho{}^i
\gamma^{\mu\nu\rho}
\psi_\nu{}^jL_{ij}.
\end{aligned}
}
\tag{4.14}
```

Equation (4.14) fixes the fermionic completion; it is not permissible to
replace $`\mathcal D_\nu E^{\mu\nu}`$ by
$`\partial_\nu E^{\mu\nu}`$ in a fermionic action.

For completeness, the two-form representative transforms as

```math
\begin{aligned}
\delta E^{\mu\nu}
={}&
-\frac{i}{2}\bar\epsilon^i\gamma^{\mu\nu}\varphi_i
-\frac12
\bar\psi_\rho{}^i
\gamma^{\mu\nu\rho}
\epsilon^jL_{ij}
\\
&-\partial_\rho\widetilde\Lambda^{\mu\nu\rho}.
\end{aligned}
\tag{4.15}
```

The source writes $`\widetilde\Lambda^{\mu\nu\rho}`$ for the dual
three-index gauge parameter. With Eqs. (4.10)--(4.11) and the epsilon
normalization (3.6), its purely bosonic local representative is

```math
\boxed{
\widetilde\Lambda^{\mu\nu\rho}
=
\frac14e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\Lambda_{\sigma\lambda}.
}
\tag{4.15a}
```

Indeed, applying the inverse of Eq. (4.11) to
$`\delta_\Lambda E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]}`$
gives

```math
\delta_\Lambda E^{\mu\nu}
=-\partial_\rho\widetilde\Lambda^{\mu\nu\rho}.
\tag{4.15b}
```

The factor $`1/4`$, rather than $`1/2`$, follows from the source convention
in Eq. (4.11), which writes the duality relation without a separate
$`1/2!`$.

### 4.5 The $`P^a`$ representative

The potential form of the vector--linear density uses the object $`P^a`$.
It is defined by Coomans--Özkan Eq. (3.2):

```math
\boxed{
P^a
=E^a
+\frac{i}{2}\bar\psi_b{}^i\gamma^{ba}\varphi_i
+\frac14
\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}.
}
\tag{4.16}
```

When the solution (4.8) is used, these fermionic terms precisely convert the
supercovariant derivative into the ordinary exterior derivative:

```math
\boxed{
P^a
=-\frac1{12}e_\mu{}^a e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}.
}
\tag{4.17}
```

Accordingly,

```math
P_\mu=e_\mu{}^aP_a
\tag{4.18}
```

is distinct from the supercovariant constrained vector $`E_\mu`$ whenever
fermions are retained.

## 5. Detailed Derivation

### 5.1 Consistency of the three-form and dual-two-form definitions

Insert Eq. (4.11) into Eq. (4.8):

```math
\begin{aligned}
E^\mu
&=-\frac1{12}e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu
\left(
e\varepsilon_{\rho\sigma\lambda\alpha\beta}
E^{\alpha\beta}
\right)
\\
&=-\frac1{12}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\varepsilon_{\rho\sigma\lambda\alpha\beta}
\mathcal D_\nu E^{\alpha\beta}.
\end{aligned}
\tag{5.1}
```

The second line uses covariant constancy of the volume form. Apply the
epsilon contraction (3.6):

```math
\begin{aligned}
E^\mu
&=-\frac1{12}
\left(-3!\,2!\right)
\delta_{[\alpha}^{\mu}
\delta_{\beta]}^\nu
\mathcal D_\nu E^{\alpha\beta}
\\
&=
\delta_{[\alpha}^{\mu}
\delta_{\beta]}^\nu
\mathcal D_\nu E^{\alpha\beta}.
\end{aligned}
\tag{5.2}
```

Because $`E^{\alpha\beta}=-E^{\beta\alpha}`$,

```math
\begin{aligned}
\delta_{[\alpha}^{\mu}
\delta_{\beta]}^\nu E^{\alpha\beta}
&=
\frac12
\left(
\delta_\alpha^\mu\delta_\beta^\nu
-\delta_\beta^\mu\delta_\alpha^\nu
\right)E^{\alpha\beta}
\\
&=\frac12
\left(E^{\mu\nu}-E^{\nu\mu}\right)
\\
&=E^{\mu\nu}.
\end{aligned}
\tag{5.3}
```

Therefore

```math
\boxed{
E^\mu=\mathcal D_\nu E^{\mu\nu},
}
\tag{5.4}
```

which is exactly Eq. (4.13) after conversion to a tangent index. This
derivation fixes the sign and the factor $`1/12`$.

### 5.2 Gauged defining-vector auxiliary

Coomans--Özkan Eq. (5.2), independently reproduced in Gold Eq. (4), is

```math
\boxed{
Y^{ij}
=
\frac{i}{4}\sigma^{-1}\bar\psi^i\psi^j
-\frac g2\sigma^{-1}L^{ij}.
}
\tag{5.5}
```

The source does not need to print an explicit $`(ij)`$ on the bilinear.
Using Eq. (3.7),

```math
\bar\psi^i\psi^j
=\bar\psi^j\psi^i,
\tag{5.6}
```

so Eq. (5.5) is symmetric and has the correct triplet index structure.

The object in Eq. (5.5) is the defining-vector auxiliary. It is not the
linear-map composite slot $`Y_{\mathrm{linear}\,ij}`$.

### 5.3 Gauge-slice value and explicit lowering

The target gauge is

```math
\sigma=1,
\qquad
\psi^i=0,
\qquad
b_\mu=0,
\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij}.
\tag{5.7}
```

Raising both indices gives

```math
\begin{aligned}
L^{ij}
&=\varepsilon^{ik}\varepsilon^{j\ell}L_{k\ell}
\\
&=\frac{L}{\sqrt2}
\varepsilon^{ik}\varepsilon^{j\ell}\delta_{k\ell}
\\
&=\frac{L}{\sqrt2}\delta^{ij}.
\end{aligned}
\tag{5.8}
```

Equation (5.5) therefore becomes

```math
\boxed{
Y^{ij}\big|_{\mathrm P}
=-\frac g2L^{ij}
=-\frac{gL}{2\sqrt2}\delta^{ij}.
}
\tag{5.9}
```

Lowering both indices one step at a time,

```math
\begin{aligned}
Y_{ij}\big|_{\mathrm P}
&=
Y^{k\ell}\big|_{\mathrm P}
\varepsilon_{ki}\varepsilon_{\ell j}
\\
&=
-\frac g2L^{k\ell}
\varepsilon_{ki}\varepsilon_{\ell j}
\\
&=
-\frac g2L_{ij}
\\
&=
-\frac{gL}{2\sqrt2}\delta_{ij}.
\end{aligned}
\tag{5.10}
```

There is no additional sign because both $`SU(2)`$ indices are lowered.

### 5.4 Nonzero derivative of the gauge-fixed gaugino

Set $`\sigma=1`$, $`\psi^i=0`$, $`b_\mu=0`$ in Eq. (4.5), but do not set its
connection terms to zero:

```math
\begin{aligned}
\mathcal D_\mu\psi^i\big|_{\mathrm P}
={}&
\frac14\gamma\mathbin{\cdot}\widehat G\,
\psi_\mu{}^i
+Y^{ij}\big|_{\mathrm P}\psi_{\mu j}
\\
&-\gamma\mathbin{\cdot}T\,\psi_\mu{}^i
-\phi_\mu{}^i.
\end{aligned}
\tag{5.11}
```

The part produced specifically by the gauging is

```math
\boxed{
\left(
\mathcal D_\mu\psi^i\big|_{\mathrm P}
\right)_{\!g}
=-\frac{gL}{2\sqrt2}
\delta^{ij}\psi_{\mu j}.
}
\tag{5.12}
```

Now lower the free index:

```math
\begin{aligned}
\left(
\mathcal D_\mu\psi_i\big|_{\mathrm P}
\right)_{\!g}
&=
\left(
\mathcal D_\mu\psi^k\big|_{\mathrm P}
\right)_{\!g}
\varepsilon_{ki}
\\
&=
-\frac{gL}{2\sqrt2}
\delta^{kj}\psi_{\mu j}\varepsilon_{ki}
\\
&=
+\frac{gL}{2\sqrt2}
\delta_{ij}\psi_\mu{}^j.
\end{aligned}
\tag{5.13}
```

Thus the upper- and lower-index gauging contributions have opposite displayed
signs. This is a direct NW--SE consequence, not a convention-free visual
replacement.

### 5.5 Gauge-slice field strength

In Eq. (4.4), the term containing the defining gaugino vanishes, but the
gravitino bilinear does not:

```math
\boxed{
\widehat G_{\mu\nu}\big|_{\mathrm P}
=
G_{\mu\nu}
+\frac{i}{2}
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
}
\tag{5.14}
```

The ordinary field strength remains

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
\tag{5.15}
```

### 5.6 Source coefficient of the defining-vector addition

Coomans--Özkan Eq. (5.1) is the gauge-unfixed relation

```math
S_g^{\mathrm{CO}}
=S_L-3S_V-3gS_{VL}.
\tag{5.16}
```

The explicit component formula for $`S_V`$ is not transcribed or used as the
later Lagrangian. Only its degree-three homogeneity under a common scaling of
all defining-vector components is needed:

```math
S_V[tV_{\mathrm{defining}}]
=t^3S_V[V_{\mathrm{defining}}],
\qquad
S_{VL}[tV_{\mathrm{defining}};\mathbb L]
=tS_{VL}[V_{\mathrm{defining}};\mathbb L].
\tag{5.17}
```

Euler's theorem gives

```math
\left\langle
V_{\mathrm{defining}},
\frac{\delta S_V}{\delta V_{\mathrm{defining}}}
\right\rangle
=3S_V,
\qquad
\left\langle
V_{\mathrm{defining}},
\frac{\delta S_{VL}}{\delta V_{\mathrm{defining}}}
\right\rangle
=S_{VL}.
\tag{5.18}
```

Contracting the defining-vector equation obtained from (5.16) gives

```math
\begin{aligned}
0
&=
-3
\left\langle
V_{\mathrm{defining}},
\frac{\delta S_V}{\delta V_{\mathrm{defining}}}
\right\rangle
-3g
\left\langle
V_{\mathrm{defining}},
\frac{\delta S_{VL}}{\delta V_{\mathrm{defining}}}
\right\rangle
\\
&=-9S_V-3gS_{VL}.
\end{aligned}
\tag{5.19}
```

Hence

```math
3S_V=-gS_{VL}.
\tag{5.20}
```

Substituting only this defining-multiplet relation into Eq. (5.16),

```math
\begin{aligned}
S_g^{\mathrm{CO}}
&=S_L-3S_V-3gS_{VL}
\\
&=S_L+gS_{VL}-3gS_{VL}
\\
&=S_L-2gS_{VL}.
\end{aligned}
\tag{5.21}
```

Because $`S_L`$ is the vector--linear density evaluated on the locked
linear map, BF linearity gives the Coomans-oriented vector argument

```math
\boxed{
V_{\mathrm{linear}}^{\mathrm{CO}}
-2gV_{\mathrm{defining}}.
}
\tag{5.22}
```

Equation (5.22) is derived before any compensator gauge. It does not use a
descendant Poincaré equation and does not use Gold's final bosonic
Lagrangian.

### 5.7 Conversion to the target linear-multiplet orientation

Coomans--Özkan subsequently choose
$`L_{ij}^{\mathrm{CO}}=-\delta_{ij}/\sqrt2`$, whereas the target project
direction is $`L_{ij}=+L\delta_{ij}/\sqrt2`$. The multiplet-wide orientation
conversion is

```math
\begin{aligned}
L_{ij}^{\mathrm{CO}}&=-L_{ij},
&
\varphi_{\mathrm{CO}}^i&=-\varphi^i,
\\
E_{\mathrm{CO}\,a}&=-E_a,
&
N_{\mathrm{CO}}&=-N.
\end{aligned}
\tag{5.23}
```

The corresponding form representatives obey

```math
E_{\mathrm{CO}\,\mu}=-E_\mu,
\qquad
E_{\mathrm{CO}\,\mu\nu}=-E_{\mu\nu},
\qquad
E_{\mathrm{CO}\,\mu\nu\rho}=-E_{\mu\nu\rho}.
\tag{5.24}
```

The norm $`L^2=L_{ij}L^{ij}`$ is unchanged. Direct substitution into the four
component formulas locked in the parent map gives

```math
V_{\mathrm{linear}}^{\mathrm{CO}}
=-V_{\mathrm{linear}}.
\tag{5.25}
```

The sign check by component is:

| Slot | Sign under (5.23) |
| --- | --- |
| $`\rho`$ | both $`N`$ and $`L_{ij}\bar\varphi^i\varphi^j`$ terms are odd |
| $`\lambda_i`$ | every term contains an odd total number of fields from the signed linear multiplet |
| $`Y_{ij}`$ | every bosonic, bilinear, and quartic term is odd |
| $`\widehat F_{\mu\nu}`$ | every term contains one or three signed linear-multiplet factors and is odd |

The vector--linear density is linear in each of its two multiplet arguments.
Consequently,

```math
\begin{aligned}
S_{VL}
\big[
V_{\mathrm{linear}}^{\mathrm{CO}}
-2gV_{\mathrm{defining}};
\mathbb L_{\mathrm{CO}}
\big]
&=
S_{VL}
\big[
-V_{\mathrm{linear}}
-2gV_{\mathrm{defining}};
-\mathbb L
\big]
\\
&=
S_{VL}
\big[
V_{\mathrm{linear}}
+2gV_{\mathrm{defining}};
\mathbb L
\big].
\end{aligned}
\tag{5.26}
```

No sign redefinition of $`g`$ is used in Eq. (5.26). Therefore the target
component addition is

```math
\boxed{
V_{\mathrm{linear}}
+2gV_{\mathrm{defining}}.
}
\tag{5.27}
```

### 5.8 Componentwise sum before gauge fixing

Using only original source components, Eq. (5.27) means the vector argument

```math
\boxed{
\begin{aligned}
\Big(
&\rho_{\mathrm{linear}}+2g\sigma,
\\
&\lambda_{\mathrm{linear}\,i}
+2g\psi^j\varepsilon_{ji},
\\
&Y_{\mathrm{linear}\,ij}
+2gY^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j},
\\
&\widehat F_{\mathrm{linear}\,\mu\nu}
+2g\widehat G_{\mu\nu}
\Big).
\end{aligned}
}
\tag{5.28}
```

This is a sum of component mappings, not a new multiplet field and not a sum
of independently selected Lagrangians.

### 5.9 Componentwise sum on the target gauge slice

Insert Eqs. (5.7), (5.9)--(5.10), and (5.14) into (5.28):

```math
\boxed{
\begin{aligned}
\Big(
&\rho_{\mathrm{linear}}\big|_{\mathrm P}+2g,
\\
&\lambda_{\mathrm{linear}\,i}\big|_{\mathrm P},
\\
&Y_{\mathrm{linear}\,ij}\big|_{\mathrm P}
-g^2L_{ij},
\\
&\widehat F_{\mathrm{linear}\,\mu\nu}\big|_{\mathrm P}
+2gG_{\mu\nu}
+ig\,\bar\psi_{[\mu}{}^i\psi_{\nu]i}
\Big).
\end{aligned}
}
\tag{5.29}
```

For the auxiliary entry,

```math
2g
\left(
Y^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j}
\right)_{\mathrm P}
=2g
\left(-\frac g2L_{ij}\right)
=-g^2L_{ij}.
\tag{5.30}
```

For the field-strength entry,

```math
\begin{aligned}
2g\widehat G_{\mu\nu}\big|_{\mathrm P}
&=
2g
\left(
G_{\mu\nu}
+\frac{i}{2}
\bar\psi_{[\mu}{}^i\psi_{\nu]i}
\right)
\\
&=
2gG_{\mu\nu}
+ig\,\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\end{aligned}
\tag{5.31}
```

No overall density normalization has been applied in Eqs. (5.28)--(5.31).
That normalization belongs to the later action construction.

## 6. Consistency Checks

### 6.1 Free indices and Grassmann parity

- $`Y^{ij}`$ and $`L^{ij}`$ are symmetric in $`i,j`$.
- $`G_{\mu\nu}`$, $`\widehat G_{\mu\nu}`$, and $`E^{\mu\nu}`$ are
  antisymmetric in their spacetime indices.
- $`E_{\mu\nu\rho}`$ is totally antisymmetric.
- Every entry added to a bosonic vector slot is Grassmann even.
- Every entry added to the gaugino slot is Grassmann odd.

### 6.2 Weyl weights

The defining-vector entries have the required weights:

```math
w(\sigma,\psi^i,Y^{ij},\widehat G_{\mu\nu})
=
\left(1,\frac32,2,1\right).
\tag{6.1}
```

Since $`w(g)=0`$, the additions in Eq. (5.28) have weights

```math
w(2g\sigma,2g\psi_i,2gY_{ij},2g\widehat G_{\mu\nu})
=
\left(1,\frac32,2,1\right),
\tag{6.2}
```

matching the weights of the linear-map vector slots. A dimensionful gauge
scale appears only after the compensator gauge fixes the local dilatation;
it must not be inserted as a pre-gauge Weyl weight for $`g`$.

### 6.3 Form-definition check

Equations (5.1)--(5.4) explicitly reproduce

```math
E^\mu=\mathcal D_\nu E^{\mu\nu}
\tag{6.3}
```

from the three-form definition, including the sign and $`1/12`$.

### 6.4 Gauge-slice checks

The defining-vector auxiliary gives

```math
2gY_{ij}\big|_{\mathrm P}
=-g^2L_{ij},
\tag{6.4}
```

and the supercovariant field strength gives

```math
2g\widehat G_{\mu\nu}\big|_{\mathrm P}
=2gG_{\mu\nu}
+ig\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
\tag{6.5}
```

The upper and lower defining-gaugino derivative contributions are

```math
-\frac{gL}{2\sqrt2}
\delta^{ij}\psi_{\mu j},
\qquad
+\frac{gL}{2\sqrt2}
\delta_{ij}\psi_\mu{}^j,
\tag{6.6}
```

so their relative sign is fixed.

### 6.5 What was not checked here

The following are deliberately not claimed:

- a complete two-derivative Lagrangian;
- an overall Gold/Özkan--Pang density normalization;
- a gauge-fixed action;
- cancellation of action terms;
- auxiliary equations of the descendant theory;
- a vacuum or spectrum.

### 6.6 Component identities and checks

The epsilon-duality, antisymmetric projection, Euler homogeneity and
orientation identities are derived above. The [component check guide](../../../../README.md)
gives the current executable checks for the linear-map derivatives,
gauging, background and fermion kernels, with their stated scope.
Run from the repository root:

```bash
python3 -B computations/two_derivative_fermionic/src/kernels/audit_exact_checks.py
```

## 7. Final Result

The defining-vector input is

```math
\boxed{
V_{\mathrm{defining}}
=
\left(\sigma,C_\mu,\psi^i,Y^{ij}\right),
\qquad
\widehat G_{\mu\nu}
=G_{\mu\nu}
-\bar\psi_{[\mu}{}^i\gamma_{\nu]}\psi_i
+\frac{i}{2}\sigma
\bar\psi_{[\mu}{}^i\psi_{\nu]i}.
}
\tag{7.1}
```

Its gauged auxiliary is

```math
\boxed{
Y^{ij}
=
\frac{i}{4}\sigma^{-1}\bar\psi^i\psi^j
-\frac g2\sigma^{-1}L^{ij}.
}
\tag{7.2}
```

The external linear-multiplet form definitions are

```math
\boxed{
\begin{aligned}
E^\mu
&=e_a{}^\mu E^a
=-\frac1{12}e^{-1}
\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}
\\
&=\mathcal D_\nu E^{\mu\nu},
\\
E_\mu&=g_{\mu\nu}E^\nu,
\\
E_{\mu\nu}
&=g_{\mu\rho}g_{\nu\sigma}E^{\rho\sigma},
\\
E_{\mu\nu\rho}
&=e\varepsilon_{\mu\nu\rho\sigma\lambda}
E^{\sigma\lambda}.
\end{aligned}
}
\tag{7.3}
```

The target component mapping to be inserted later into the vector--linear
density is

```math
\boxed{
\begin{aligned}
\Big(
&\rho_{\mathrm{linear}}+2g\sigma,
\\
&\lambda_{\mathrm{linear}\,i}
+2g\psi^j\varepsilon_{ji},
\\
&Y_{\mathrm{linear}\,ij}
+2gY^{k\ell}\varepsilon_{ki}\varepsilon_{\ell j},
\\
&\widehat F_{\mathrm{linear}\,\mu\nu}
+2g\widehat G_{\mu\nu}
\Big).
\end{aligned}
}
\tag{7.4}
```

Equation (7.4) is the sum of the separately anchored linear map and defining
vector. It is not itself a Lagrangian.

## 8. Convention Dependence and Remaining Uncertainties

The signs in Eqs. (4.8), (4.11), and (5.1)--(5.4) are tied to the source
Lorentzian epsilon contraction (3.6). Changing the orientation or treating
the alternating symbol as the Levi-Civita tensor without the displayed
factor of $`e`$ would change intermediate signs or density factors.

The relation between $`E_{\mu\nu\rho}`$ and $`E^{\mu\nu}`$ is therefore to be
used exactly as written in Eq. (7.3). The $`e`$ and $`e^{-1}`$ factors must
not be silently deleted when returning to the source-density convention.

The defining-vector component data and addition rule feed the
[gauged action derivation](../../../../../../common/two_derivative_action/details/construction.md),
which fixes the overall normalization, inserts the full vector--linear density
and expands the action through quadratic fermions. The
[component checks](../../../../README.md#exact-component-checks) cover the retained
bosonic and fermionic coefficients; they do not establish nonlinear supersymmetry.
