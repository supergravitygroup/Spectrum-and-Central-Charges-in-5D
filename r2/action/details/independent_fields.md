# Independent fields and dependent objects

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

The field inventory is defined for the total action in action.md,
on its current gauge slice and in the conventions of
[CONVENTIONS.md](../../../common/details/source_conventions.md).
As in the source actions, fermionic expressions are retained at the orders
required for two-fermion accuracy of the total action.

<a id="1-independent-field-inventory"></a>

## Independent-field inventory

```math
\boxed{
\begin{aligned}
\mathcal F_{\mathrm B}
&=\{e_\mu{}^a,\ C_\mu,\ B_{\mu\nu},\ L,\ N,\ E_{\mu\nu\rho},
       \ V_\mu,\ V_\mu^{\prime\,ij}\},\\
\mathcal F_{\mathrm F}
&=\{\psi_\mu{}^i,\ \varphi^i\}.
\end{aligned}}
```

In the current gauge

```math
\begin{gathered}
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\\
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,\qquad
V_\mu^{\prime\,ij}=V_\mu^{\prime\,ji},\qquad
\delta_{ij}V_\mu^{\prime\,ij}=0.
\end{gathered}
```

Here $`\psi^i`$ is the dilatino, $`\psi_\mu{}^i`$ the gravitino, $`\varphi^i`$ the linear-multiplet
fermion, and $`\phi_\mu{}^i`$ a dependent connection.

| Object | Status and determining independent fields |
|---|---|
| $`g_{\mu\nu},e,e_a{}^\mu`$ | Geometric objects calculated from the vielbein |
| $`L_{ij},L^{ij}`$ | Triplet calculated from $`L`$ in the current gauge |
| $`V_\mu^{ij}`$ | Combination of $`V_\mu,V_\mu^{\prime\,ij}`$ |
| $`E_a,E^{\mu\nu}`$ | The following representations of $`E_{\mu\nu\rho}`$; not additional independent fields |
| $`G,H,\widehat G,\widehat H`$ | Field strengths calculated from potentials and fermions |
| $`T_{ab},\chi^i,D`$ | Composites calculated from the gauged Dilaton–Weyl definitions |
| $`\omega_\mu{}^{ab},\phi_\mu{}^i,f_\mu{}^a`$ | Dependent connections |
| $`\widehat R(Q),\widehat R(V),\widehat R'(M),\widehat R(M)`$ | Curvatures calculated from the common connections and composites |
| $`\rho',\lambda'_i,Y'_{ij},A'_\mu,\widehat F'_{\mu\nu}`$ | Composite vector map of the same original linear multiplet |

<a id="2-counting-the-three-form-and-constrained-vector-as-one-field"></a>

## Counting the three-form and constrained vector as one field

Solving the three-form bridge for $`E^a`$ gives

```math
\begin{aligned}
E^a+\frac i2\bar\psi_b{}^i\gamma^{ba}\varphi_i
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
&=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda},\\[2pt]
E^a
&=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}
-\frac i2\bar\psi_b{}^i\gamma^{ba}\varphi_i
-\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij},\\
E_a&=\eta_{ab}E^b,\qquad
E^{\mu\nu}=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda}.
\end{aligned}
```

The variation of $`E_a`$ is therefore the variation of the right-hand side;
it is not chosen independently of $`E_3`$. The coordinate $`\varepsilon`$ here is a tensor;
if the density symbol is used, write
$`\varepsilon^{\mu\nu\rho\sigma\lambda} =e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}`$.

<a id="3-field-strengths-and-t_ab"></a>

## Field strengths and $`T_{ab}`$

The order for calculating the composites is fixed by these definitions:

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
\widehat G_{\mu\nu}
&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}
-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\\
8T_{ab}-\widehat G_{ab}
&=-\frac16\varepsilon_{abcde}\widehat H^{edc}
=\frac16\varepsilon_{abcde}\widehat H^{cde},\\
T_{ab}
&=\frac18\left(\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}\right).
\end{aligned}
```

<a id="4-spin-connection-and-s-connection"></a>

## Spin connection and $`S`$ connection

In the current $`b_\mu=0`$ gauge, the spin connection is

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c\\
&+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,
\qquad \psi^a=e^{a\mu}\psi_\mu
\end{aligned}
```

so the dependence includes gravitino contorsion. One then calculates

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}{}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}{}^i
-2V_{[\mu}^{ij}\psi_{\nu]j}
+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}{}^i,\\
\phi_\mu{}^i
={}&\frac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)
={}&\widehat R'_{\mu\nu}{}^i(Q)-2i\gamma_{[\mu}\phi_{\nu]}{}^i
\end{aligned}
```

as follows.

<a id="5-the-chii-composite"></a>

## The $`\chi^i`$ composite

Let $`\Psi`$ count degree in the independent fermions $`(\psi_\mu{}^i,\varphi^i)`$.
Even though the dilatino field vanishes,

```math
\begin{aligned}
\mathcal D_a\psi^i\big|_{\mathrm P}
&=\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)
\psi_a{}^i-\frac g2L^{ij}\psi_{aj}-\phi_a{}^i,\\
\chi^i
&=\frac i8\gamma^a\mathcal D_a\psi^i\big|_{\mathrm P}
+\frac g8\varphi^i+O(\Psi^3)\\
&=\frac i8\gamma^a
\left[
\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)
\psi_a{}^i-\frac g2L^{ij}\psi_{aj}-\phi_a{}^i
\right]
+\frac g8\varphi^i+O(\Psi^3).
\end{aligned}
```

This expression does not add $`\chi^i`$ to the inventory of independent fermions.

<a id="6-k-connection-and-d-composite"></a>

## $`K`$ connection and $`D`$ composite

Using definition (A.15) in action.md,
after calculating $`\widehat R'(M)`$, whose explicit $`\chi`$ term is
$`+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi`$,

```math
\begin{aligned}
\mathcal R_\mu{}^a
&:=\widehat R'_{\mu\nu}{}^{ab}(M)e_b{}^\nu,\qquad
\mathcal R:=e_a{}^\mu\mathcal R_\mu{}^a,\\
f_\mu{}^a
&=-\frac16\mathcal R_\mu{}^a+\frac1{48}e_\mu{}^a\mathcal R,\\
f_a{}^a
&=\left(-\frac16+\frac5{48}\right)\mathcal R
=-\frac1{16}\mathcal R
\end{aligned}
```

follows. Here $`\mathcal R`$ is the contraction of the primed curvature,
including fermionic contributions.

Finally,

```math
\begin{aligned}
\Box_c\sigma\big|_{\mathrm P}
&=2f_a{}^a-\frac i2\bar\psi_a{}^i
\mathcal D^a\psi_i\big|_{\mathrm P}
-2\bar\psi_a{}^i\gamma^a\chi_i,\\
D
&=\frac14\Box_c\sigma\big|_{\mathrm P}
-\frac1{16}\widehat G^2-\frac{26}{3}T^2
+2\widehat G^{ab}T_{ab}
+\frac g4N+\frac{g^2}{16}L^2+O(\Psi^4)\\
&=\frac12f_a{}^a-\frac1{16}\widehat G^2-\frac{26}{3}T^2
+2\widehat G^{ab}T_{ab}
+\frac g4N+\frac{g^2}{16}L^2\\
&\quad-\frac i8\bar\psi_a{}^i\mathcal D^a\psi_i\big|_{\mathrm P}
-\frac12\bar\psi_a{}^i\gamma^a\chi_i+O(\Psi^4),\\
\widehat G^2&:=\widehat G_{ab}\widehat G^{ab},\qquad
T^2:=T_{ab}T^{ab}.
\end{aligned}
```

<a id="7-dependency-order-and-the-auxiliary-field-distinction"></a>

## Dependency order and the auxiliary-field distinction

The dependency order is thus

```math
\boxed{
\mathcal F_{\mathrm B},\mathcal F_{\mathrm F}
\;\longrightarrow\;
(E_a,\widehat G,\widehat H,\omega)
\;\longrightarrow\;
T
\;\longrightarrow\;
\phi
\;\longrightarrow\;
\chi
\;\longrightarrow\;
f
\;\longrightarrow\;
D
}
```

At each stage, the independent fields and objects calculated at earlier
stages remain among the inputs.

**Independence is not an auxiliary-field classification.** $`N,E_3,V,V'`$ are the
independent variables of the total action. Whether they are auxiliary,
constraining, or dynamical in the full theory follows from its derivative
and constraint structure after substituting the composite definitions.
Auxiliary-field labels from the two-derivative theory do not transfer
automatically to this inventory; $`T,D,\chi,\omega,\phi,f`$ are not separately varied fields
because they are dependent by definition.
