# Independent fields and dependent objects

This inventory applies to the current gauge of the total action
in action.md:

```math
\begin{gathered}
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\\
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,\qquad
\delta_{ij}V_\mu^{\prime\,ij}=0 .
\end{gathered}
\tag{P}
```

```math
S_{\rm total}^{(\le2)}
=S_{2\text{-der}}^{(\le2)}
+\alpha S_{\mathrm{Weyl}^2}^{(\le2)},\qquad
\alpha\ne0,\qquad \partial_\mu\alpha=0 .
\tag{F0}
```

$`\alpha`$ is a generic constant, not a perturbative expansion parameter.
The action is exact in bosonic fields and couplings and extends through
second order in fermions. The inventory is determined without using
the target theory's equations of motion.

Conventions agree with [CONVENTIONS.md](../../../common/details/source_conventions.md).
Equations (I1)–(I6) below belong to this file. Labels (A8), (A10),
(B-GA03), (B-GC...), (C-GC...), and references to §§5–8 refer to
the common definitions in action.md. In particular, $`\psi^i`$ is the
gauge-fixed vanishing dilatino; $`\psi_\mu^i`$ the independent gravitino;
$`\varphi^i`$ the independent compensator fermion; and $`\phi_\mu^i`$ the dependent
$`S`$ connection.

<a id="1-independent-field-inventory-in-the-current-gauge"></a>

## Independent-field inventory in the current gauge

On (P), the independent field variables are exactly

```math
\boxed{
\left\{
e_\mu{}^a,\ C_\mu,\ B_{\mu\nu},\ L,\ N,\ E_{\mu\nu\rho},\quad
V_\mu,\ V_\mu^{\prime\,ij},\ \psi_\mu{}^i,\ \varphi^i
\right\}.
}
\tag{I1}
```

| Independent field | Type and index condition |
|---|---|
| $`e_\mu{}^a`$ | Vielbein; $`g_{\mu\nu}`$ and $`e`$ are calculated from it. |
| $`C_\mu`$ | One-form potential. |
| $`B_{\mu\nu}`$ | Antisymmetric two-form potential. |
| $`L,N`$ | Two distinct bosonic scalars; the source map is defined on the $`L\ne0`$ patch. |
| $`E_{\mu\nu\rho}`$ | Totally antisymmetric three-form potential; the independent representative selected instead of $`E_a`$. |
| $`V_\mu`$ | Trace component of the $`V_\mu^{ij}`$ connection at (P). |
| $`V_\mu^{\prime\,ij}`$ | $`V_\mu^{\prime\,ij}=V_\mu^{\prime\,ji}`$, $`\delta_{ij}V_\mu^{\prime\,ij}=0`$. |
| $`\psi_\mu{}^i`$ | Grassmann-odd symplectic–Majorana gravitino. |
| $`\varphi^i`$ | Grassmann-odd symplectic–Majorana compensator fermion. |

This list gives field coordinates with gauge symmetries retained;
it is not a count of propagating physical degrees of freedom.
$`V_\mu,V_\mu^{\prime\,ij}`$ are independent connection components. In contrast, $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$
are connections calculated from the definitions below.
$`\varphi^i`$ and $`\phi_\mu^i`$ are distinct objects.

Objects fixed by gauge or reconstructed algebraically from the inventory:

```math
\begin{gathered}
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\\
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,\qquad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
e=\det(e_\mu{}^a).
\end{gathered}
\tag{I2}
```

These are not additional independent fields beyond (I1).
$`g`$ and $`\alpha\ne0`$ are constant parameters.

<a id="2-counting-the-three-form-and-constrained-vector-as-one-field"></a>

## Counting the three-form and constrained vector as one field

Substituting the definitions in (A10) and (P) gives

```math
\begin{aligned}
P^a
&=-\frac1{12}e_\mu{}^a
 \varepsilon^{\mu\nu\rho\sigma\lambda}
 \partial_\nu E_{\rho\sigma\lambda}\\
&=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
 +\frac{L}{4\sqrt2}\delta_{ij}
   \bar\psi_b^i\gamma^{abc}\psi_c^j,\\
E^a
&=P^a-\frac i2\bar\psi_b\gamma^{ba}\varphi
 -\frac{L}{4\sqrt2}\delta_{ij}
   \bar\psi_b^i\gamma^{abc}\psi_c^j\\
&=-\frac1{12}e_\mu{}^a
 \varepsilon^{\mu\nu\rho\sigma\lambda}
 \partial_\nu E_{\rho\sigma\lambda}
 -\frac i2\bar\psi_b\gamma^{ba}\varphi
 -\frac{L}{4\sqrt2}\delta_{ij}
   \bar\psi_b^i\gamma^{abc}\psi_c^j,\qquad
E_a=\eta_{ab}E^b .
\end{aligned}
\tag{I3}
```

Thus $`E_a`$ is calculated once $`E_{\mu\nu\rho},e_\mu{}^a,L,\psi_\mu^i,\varphi^i`$ is specified.
$`P^a`$ and $`E^{\mu\nu}=-\varepsilon^{\mu\nu\rho\sigma\lambda} E_{\rho\sigma\lambda}/12`$ are also dependent objects.
$`E_a`$ is not independently varied. This choice uses the supplied
three-form representation of the constrained vector; it does not solve
an equation of motion of the total action. The linear-multiplet
constraint $`\mathcal D^aE_a=0`$ uses the same supercovariant definitions;
$`E_a`$ is not identified with the ordinary $`P_a`$.

<a id="3-composites-and-dependent-connections"></a>

## Composites and dependent connections

| Dependent object | Defining equation used |
|---|---|
| $`G,H,\widehat G,\widehat H`$ | (A8), (B-GC03), followed by (P). |
| $`Y^{ij}`$ | Defining-vector component (B-GA03); gauge value in (I4). |
| $`T_{ab}`$ | (B-GC12); (I4). |
| $`\omega_\mu{}^{ab}`$ | First line of (C-GC18), $`b_\mu=0`$; gravitino contorsion retained. |
| $`\phi_\mu^i,\widehat R'(Q),\widehat R(Q)`$ | (C-GC18) with the same $`\omega,T,V`$. |
| $`\chi^i`$ | (B-GC08), (B-GC14); (I5). |
| $`\widehat R(V),\widehat R'(M)`$ | (C-GC19), (C-GC20); the same $`T,\chi,\phi,\widehat R(Q)`$. |
| $`f_\mu{}^a,\widehat R(M),\widehat C`$ | Primed Ricci contractions and the full traceless curvature of (C-GC20). |
| $`D`$ | (B-GC11), (B-GC16); (I6). |
| $`\rho_{\rm linear},\lambda_{\rm linear},Y_{\rm linear},F_{\rm linear}`$ | Compensator map in §6; not a new independent vector multiplet. |
| $`L_W,\varphi_W,E_W,N_W`$ | Components of the Weyl-composite map, explicitly substituted into the action in §7; not a second independent linear multiplet. |

For $`T,D,\chi`$, (P) is substituted into the pregauge definitions
in the following order:

```math
\begin{aligned}
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL^{ij}=0
&\ \xrightarrow{\mathrm P}\quad
2Y^{ij}+\frac{gL}{\sqrt2}\delta^{ij}=0,\\
Y^{ij}\big|_{\rm P}
&=-\frac{gL}{2\sqrt2}\delta^{ij},\\
T_{ab}
&=\frac1{8\sigma^2}
\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right)
\ \xrightarrow{\mathrm P}\quad
\frac18\left(\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}\right).
\end{aligned}
\tag{I4}
```

In (B-GC14), calculate the supercovariant derivative first:

```math
\begin{aligned}
\mathcal D_\mu\psi^i\big|_{\rm P}
&=\left(\frac14\gamma\!\cdot\widehat G-\gamma\!\cdot T\right)
 \psi_\mu^i-\phi_\mu^i
-\frac{gL}{2\sqrt2}\delta^{ij}\psi_{\mu j},\\
\chi^i\big|_{\rm P}
&=\frac i8\gamma^\mu\mathcal D_\mu\psi^i\big|_{\rm P}
+\frac g8\varphi^i\\
&=\frac i8\gamma^\mu
\left[
\left(\frac14\gamma\!\cdot\widehat G-\gamma\!\cdot T\right)
\psi_\mu^i-\phi_\mu^i
-\frac{gL}{2\sqrt2}\delta^{ij}\psi_{\mu j}
\right]+\frac g8\varphi^i .
\end{aligned}
\tag{I5}
```

Here $`\phi_\mu^i`$ is calculated from (C-GC18); the condition $`\psi^i=0`$
does not set $`\mathcal D_\mu\psi^i`$ to zero. While the dilatino terms in (B-GC11)
vanish, the conformal-box contribution is retained:

```math
\begin{aligned}
\Box^c\sigma\big|_{\rm P}
&=-\frac i2\bar\psi_a\mathcal D^a\psi\big|_{\rm P}
-2\bar\psi_a\gamma^a\chi+2f_a{}^a,\\
D\big|_{\rm P}
&=\frac14\Box^c\sigma\big|_{\rm P}
-\frac1{16}\widehat G_{ab}\widehat G^{ab}
-\frac{26}{3}T_{ab}T^{ab}
+2\widehat G_{ab}T^{ab}+\frac g4N+\frac{g^2}{16}L^2\\
&=\frac12f_a{}^a
-\frac1{16}\widehat G_{ab}\widehat G^{ab}
-\frac{26}{3}T_{ab}T^{ab}
+2\widehat G_{ab}T^{ab}+\frac g4N+\frac{g^2}{16}L^2\\
&\quad-\frac i8\bar\psi_a\mathcal D^a\psi\big|_{\rm P}
-\frac12\bar\psi_a\gamma^a\chi .
\end{aligned}
\tag{I6}
```

In $`f_\mu{}^a=-\mathcal R_\mu{}^a/6+ e_\mu{}^a\mathcal R/48`$, $`\mathcal R_\mu{}^a`$ is a contraction of the full $`\widehat R'(M)`$ in (C-GC20),
not an independent Ricci field. These definitions are evaluated
in the following order:

| Order | Objects calculated from preceding data |
|---|---|
| 1 | $`E^{\mu\nu},P^a,E^a,G,H,\widehat G,\widehat H,T,Y,\omega`$ from (I1). |
| 2 | $`\widehat R'(Q)`$ from $`\omega,T,V,\psi_\mu`$; then $`\phi_\mu,\widehat R(Q)`$. |
| 3 | $`(\mathcal D_\mu\psi^i)_{\rm P},\chi^i`$ from these objects and $`\varphi,L`$. |
| 4 | $`\widehat R(V),\widehat R'(M)`$; then $`\mathcal R,f,\widehat R(M),\widehat C`$. |
| 5 | $`(\Box^c\sigma)_{\rm P},D`$; then the full derivatives of §5 and the action's map components. |

Thus defining $`D`$ does not require the equation of motion of $`\chi`$,
and defining $`\chi`$ does not require that of $`D`$. In §8, the fermion-order
coefficients of these composites follow from their definitions, and
$`\Pi_{\le2}`$ is applied to the total density. Defining $`T,D,\chi,\omega,\phi,f`$ does not
eliminate any field in (I1) from the total action.

<a id="4-distinguishing-dependence-from-auxiliary-field-character"></a>

## Distinguishing dependence from auxiliary-field character

Independence of the fields in (I1) identifies the input variables of the
action. “Auxiliary field” instead refers to dynamical character in the
given total action. The classification used in the two-derivative theory
does not automatically extend to $`S_{2\text{-der}}+\alpha S_{\mathrm{Weyl}^2}`$ for generic $`\alpha\ne0`$.
In particular, $`N,E_{\mu\nu\rho},V_\mu,V_\mu^{\prime\,ij},\varphi^i`$ remain independent inputs; this inventory
does not decide whether any of them can be eliminated algebraically
or whether it propagates in the total theory.

The off-shell scope retains the fields in (I1) without using target-theory
equations of motion. Dependent objects are calculated from the supplied
definitions; no smallness assumption on $`\alpha`$, substitution using
two-derivative equations of motion, or reduction of derivative order is made.
