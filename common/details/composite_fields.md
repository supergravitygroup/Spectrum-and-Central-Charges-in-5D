# Composite-field coefficients at fermion degrees zero, one, and two

By the [physical-degree definition](../fermion_order.md), $`X^{(q)}`$ is the degree-$`q`$ coefficient of $`X`$. The vielbein, $`C`$, $`B`$, $`E_3`$, $`L`$, $`N`$, and $`V`$ are independent bosonic fields. Their degree decomposition does not assign them values. The inputs are the [shared definitions](../fields_and_derivatives.md).

<a id="1-field-strengths-and-t"></a>

## Field strengths and T

The degree coefficients of the definitions are directly

```math
\begin{aligned}
\widehat G_{ab}^{(0)}&=G_{ab},&
\widehat G_{ab}^{(2)}&=\frac i2\bar\psi_{[a}\psi_{b]},\\
\widehat H_{abc}^{(0)}&=H_{abc},&
\widehat H_{abc}^{(2)}&=-\frac34\bar\psi_{[a}\gamma_b\psi_{c]}
\end{aligned}
```

Substituting these two identities into the definition of $`T`$ gives

```math
\begin{aligned}
T_{ab}^{(0)}&=\frac18G_{ab}
+\frac1{48}\varepsilon_{abcde}H^{cde},\\
T_{ab}^{(2)}
&=\frac18\left(\frac i2\bar\psi_{[a}\psi_{b]}\right)
+\frac1{48}\varepsilon_{abcde}
\left(-\frac34\bar\psi^{[c}\gamma^d\psi^{e]}\right)\\
&=\frac i{16}\bar\psi_{[a}\psi_{b]}
-\frac1{64}\varepsilon_{abcde}\bar\psi^c\gamma^d\psi^e.
\end{aligned}
```

The last step uses complete antisymmetry of epsilon; no spinors have been interchanged.

<a id="2-constrained-vector-of-the-linear-multiplet"></a>

## Constrained vector of the linear multiplet

The quantity $`P^\mu=e^{-1}\partial_\nu(eE^{\mu\nu})`$ contains only independent bosonic fields. The source current identity

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j
```

gives the algebraic solution for $`E^a`$:

```math
\begin{aligned}
E^{a(0)}&=e_\mu{}^a e^{-1}\partial_\nu(eE^{\mu\nu}),\\
E^{a(2)}&=-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j
\end{aligned}
```

Back-substitution gives $`P^{a(2)}=0`$. This does not mean that the two-fermion part of $`E^a`$ vanishes.

<a id="3-dependent-connections"></a>

## Dependent connections

The fermion-degree decomposition of the spin connection is

```math
\begin{aligned}
\omega_\mu{}^{ab(0)}&=\omega_\mu{}^{ab}(e),\\
\omega_\mu{}^{ab(2)}&=\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b
\end{aligned}
```

Below, $`\nabla^{(0)}`$ denotes the torsionless Lorentz derivative. Expanding the ordinary curvature definition gives

```math
\begin{aligned}
R_{\mu\nu}{}^{ab(2)}(\omega)
={}&2\partial_{[\mu}\omega_{\nu]}{}^{ab(2)}
+2\omega_{[\mu}{}^{ac(0)}\omega_{\nu]c}{}^{b(2)}
+2\omega_{[\mu}{}^{ac(2)}\omega_{\nu]c}{}^{b(0)}\\
={}&2\nabla^{(0)}_{[\mu}\omega_{\nu]}{}^{ab(2)}
\end{aligned}
```

The product $`\omega^{(2)}\omega^{(2)}`$ has degree four.

The degree-one coefficient of the gravitino curvature is

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{i(1)}(Q)
={}&2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}(e)\gamma_{ab}\psi_{\nu]}^i
-2V_{[\mu}^{ij}\psi_{\nu]j}\\
&+2i\left(\frac18G_{ab}
+\frac1{48}\varepsilon_{abcde}H^{cde}\right)
\gamma^{ab}\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^{i(1)}
={}&\frac i3\gamma^a\widehat R'_{\mu a}{}^{i(1)}(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^{i(1)}(Q),\\
\widehat R_{\mu\nu}{}^{i(1)}(Q)
={}&\widehat R'_{\mu\nu}{}^{i(1)}(Q)
-2i\gamma_{[\mu}\phi_{\nu]}^{i(1)}.
\end{aligned}
```

For an independent check of its gamma trace, temporarily define $`Q_b:=\gamma^a{\widehat R'}_{ab}^{(1)}(Q)`$ and $`Q:=\gamma^{ab}{\widehat R'}_{ab}^{(1)}(Q)`$. Antisymmetry gives $`\gamma^bQ_b=-Q`$. Therefore

```math
\begin{aligned}
\phi_b^{(1)}&=-\frac i3Q_b-\frac i{24}\gamma_bQ,\\
\gamma^b\phi_b^{(1)}&=\frac i3Q-\frac{5i}{24}Q=\frac i8Q,\\
\gamma^a\widehat R_{ab}^{(1)}(Q)
&=Q_b-i\left(5\phi_b^{(1)}-\gamma^a\gamma_b\phi_a^{(1)}\right)\\
&=Q_b-3i\phi_b^{(1)}-i\gamma_b\gamma^a\phi_a^{(1)}\\
&=Q_b-Q_b-\frac18\gamma_bQ+\frac18\gamma_bQ=0.
\end{aligned}
```

In the original fields, the checked result is $`\gamma^a\widehat R_{ab}^{i(1)}(Q)=0`$.

<a id="4-dilatino-derivative-and-composite-chi"></a>

## Dilatino derivative and composite chi

Although the dilatino vanishes in the source gauge, the degree-one coefficient of its full derivative is

```math
(\mathcal D_a\psi^i)^{(1)}
=\left(\frac18G_{bc}
-\frac1{48}\varepsilon_{bcdef}H^{def}\right)
\gamma^{bc}\psi_a^i
-\frac g2 L^{ij}\psi_{aj}-\phi_a^{i(1)}
```

Since the two terms surviving in the source spinor-composite definition in this gauge are $`i\gamma^a\mathcal D_a\psi^i/8+g\varphi^i/8`$,

```math
\begin{aligned}
\chi^{i(1)}
={}&\frac i8\gamma^a(\mathcal D_a\psi^i)^{(1)}
+\frac g8\varphi^i\\
={}&\frac i8\gamma^a
\left(\frac18G_{bc}-\frac1{48}\varepsilon_{bcdef}H^{def}\right)
\gamma^{bc}\psi_a^i
-\frac{ig}{16}L^{ij}\gamma^a\psi_{aj}
-\frac i8\gamma^a\phi_a^{i(1)}+\frac g8\varphi^i.
\end{aligned}
```

Substituting the definition of $`\phi^{(1)}`$ from the previous section gives

```math
\boxed{
\begin{aligned}
\chi^{i(1)}={}&
\frac i{64}G_{bc}\gamma^a\gamma^{bc}\psi_a^i
-\frac i{384}\varepsilon_{bcdef}H^{def}
\gamma^a\gamma^{bc}\psi_a^i
-\frac{ig}{16}L^{ij}\gamma^a\psi_{aj}\\
&+\frac1{64}\gamma^{ab}\widehat R'_{ab}{}^{i(1)}(Q)
+\frac g8\varphi^i.
\end{aligned}}
```

The curvature coefficient is explicitly checked as

```math
-\frac i8\gamma^a\left(
\frac i3\gamma^b{\widehat R'}_{ab}^{(1)}(Q)
-\frac i{24}\gamma_a\gamma^{bc}{\widehat R'}_{bc}^{(1)}(Q)
\right)
=\left(\frac1{24}-\frac5{192}\right)
\gamma^{ab}{\widehat R'}_{ab}^{(1)}(Q)
=\frac1{64}\gamma^{ab}{\widehat R'}_{ab}^{(1)}(Q)
```

The preceding section expressed $`\widehat R'^{(1)}(Q)`$ solely through independent fields and the torsionless connection.

<a id="5-primed-ricci-tensor-and-f-connection"></a>

## Primed Ricci tensor and f connection

The degree-two primed Lorentz curvature is

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab(2)}(M)
={}&2\nabla^{(0)}_{[\mu}\omega_{\nu]}{}^{ab(2)}
+i\bar\phi_{[\mu}^{(1)}\gamma^{ab}\psi_{\nu]}\\
&+iT_{cd}^{(0)}\bar\psi_{[\mu}\gamma^{abcd}\psi_{\nu]}
+2iT^{ab(0)}\bar\psi_{[\mu}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b](1)}(Q)
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab(1)}(Q)\\
&+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi^{(1)}.
\end{aligned}
```

All degree-zero and degree-one objects appearing here were given above. Since the metric and vielbein in the definitions carry no physical fermion degree,

```math
\begin{aligned}
\mathcal R_{\mu\nu}^{(2)}
&=\widehat R'_{\mu\rho}{}^{ab(2)}(M)e_b{}^\rho e_{\nu a},\\
\mathcal R^{(2)}&=g^{\mu\nu}\mathcal R_{\mu\nu}^{(2)},\\
f_\mu{}^{a(2)}&=-\frac16\mathcal R_\mu{}^{a(2)}
+\frac1{48}e_\mu{}^a\mathcal R^{(2)},\\
f_a{}^{a(2)}&=\left(-\frac16+\frac5{48}\right)\mathcal R^{(2)}
=-\frac1{16}\mathcal R^{(2)}.
\end{aligned}
```

No symmetry of the primed Ricci tensor is assumed. The trace of the full curvature is

```math
\begin{aligned}
\widehat R_{ab}{}^{cb(2)}(M)
&=\mathcal R_a{}^{c(2)}+6f_a{}^{c(2)}
+2\delta_a{}^c f_b{}^{b(2)}\\
&=\mathcal R_a{}^{c(2)}-\mathcal R_a{}^{c(2)}
+\left(\frac18-\frac18\right)\delta_a{}^c\mathcal R^{(2)}=0
\end{aligned}
```

which verifies the identity.

<a id="6-explicit-flux-contributions-to-the-d-composite"></a>

## Explicit flux contributions to the D composite

In the input definition of $`D`$, the flux block

```math
-\frac1{16}\widehat G^2-\frac{26}{3}T^2
+2\widehat G\cdot T
=\frac5{96}\widehat G^2
-\frac1{288}\varepsilon_{abcde}\widehat G^{ab}\widehat H^{cde}
+\frac{13}{288}\widehat H^2
```

takes this form using the [epsilon contraction](action_normalizations.md). The degree-two coefficients are

```math
\begin{aligned}
(\widehat G^2)^{(2)}
&=iG^{ab}\bar\psi_a\psi_b,\\
(\varepsilon\widehat G\widehat H)^{(2)}
&=\frac i2\varepsilon_{abcde}H^{cde}\bar\psi^a\psi^b
-\frac34\varepsilon_{abcde}G^{ab}\bar\psi^c\gamma^d\psi^e,\\
(\widehat H^2)^{(2)}
&=-\frac32H^{abc}\bar\psi_a\gamma_b\psi_c
\end{aligned}
```

selected directly from the product. Consequently,

```math
\boxed{
\begin{aligned}
D^{(2)}={}&-\frac1{32}\mathcal R^{(2)}
+\frac{5i}{96}G^{ab}\bar\psi_a\psi_b
-\frac i{576}\varepsilon_{abcde}H^{cde}\bar\psi^a\psi^b\\
&+\frac1{384}\varepsilon_{abcde}G^{ab}\bar\psi^c\gamma^d\psi^e
-\frac{13}{192}H^{abc}\bar\psi_a\gamma_b\psi_c\\
&-\frac i{64}G_{bc}\bar\psi_a^i\gamma^{bc}\psi_i^a
+\frac i{384}\varepsilon_{bcdef}H^{def}
\bar\psi_a^i\gamma^{bc}\psi_i^a\\
&-\frac{ig}{16}L_{ij}\bar\psi_a^i\psi^{aj}
+\frac i8\bar\psi_a^i\phi_i^{a(1)}
-\frac12\bar\psi_a\gamma^a\chi^{(1)}.
\end{aligned}}
```

Here $`\mathcal R^{(2)}`$, $`\phi^{(1)}`$, and $`\chi^{(1)}`$ are the explicit finite composites from the preceding sections. The coefficient checks use

```math
\frac5{96}i=\frac{5i}{96},\quad
-\frac1{288}\frac i2=-\frac i{576},\quad
-\frac1{288}\left(-\frac34\right)=\frac1{384},\quad
\frac{13}{288}\left(-\frac32\right)=-\frac{13}{192}
```

The remaining two flux–spinor coefficients come from the degree-zero coefficient of $`-i(\widehat G_{bc}/4-T_{bc})/8`$:

```math
-\frac i8\left(\frac14G_{bc}-\frac18G_{bc}
-\frac1{48}\varepsilon_{bcdef}H^{def}\right)
=-\frac i{64}G_{bc}
+\frac i{384}\varepsilon_{bcdef}H^{def}.
```

The identities in this file give the fermion-degree coefficients of the defined composites and the dependent-connection constraints. Free couplings remain symbolic; no independent auxiliary-field equation is used.
