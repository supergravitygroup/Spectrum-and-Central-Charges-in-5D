# Shared fields, notation, and covariant definitions

This dictionary defines the fields and derivatives in the [component action](details/component_action.md). Transcribing definitions does not reverify the underlying multiplet/SUSY construction; the [check scope](../references/component_records/02_action_family.md) still applies. The [common conventions](conventions.md) are authoritative for signs and indices.

The [degree-zero, one, and two coefficients](details/composite_fields.md) of these definitions have been derived explicitly. The [compensating parameters](details/gauge_compensations.md) preserving the existing gauge under SUSY are solved from the gauge conditions.

## Field content and current representation

The independent bosonic fields are $`e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho}, L,N,V_\mu,V_\mu^{\prime ij}`$, and the independent physical fermions are $`\psi_\mu^i,\varphi^i`$. The objects $`T,D,\chi,Y`$ are composites, while $`\omega,\phi,f`$ are dependent connections. This list is not a spectrum result classifying fields as dynamical or auxiliary.

The source densities use the following existing Poincaré representation. No new gauge is chosen here. In addition to the common conventions' general domain $`L\ne0`$, the branch $`L>0`$ used by the recorded action is explicitly retained; this record does not establish an extension to the negative branch.

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad L>0,\qquad g\ne0,
\qquad V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad \delta_{ij}V_\mu^{\prime\,ij}=0.
```

The defining dilatino is $`\psi^i`$, the gravitino is $`\psi_\mu^i`$, the independent linear-multiplet fermion is $`\varphi^i`$, and the dependent $`S`$ connection is $`\phi_\mu^i`$. Derivatives are constructed before substituting gauge values; $`\psi^i=0`$ does not imply $`\mathcal D_a\psi^i=0`$.

## Field strengths and currents

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
H_{\mu\nu\rho}&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho},\\
\widehat G_{\mu\nu}&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=H_{\mu\nu\rho}
-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\\
E^{\mu\nu}&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda},\qquad
E^\mu=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda},\\
P^a&=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j,\\
P^\mu&=e^{-1}\partial_\nu(eE^{\mu\nu}),\\
\varepsilon^{\mu\nu\rho\sigma\lambda}
&=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
\varepsilon^{abcdf}.
\end{aligned}
```

## Composite fields and ordered derivatives

```math
\begin{aligned}
T_{ab}&=\frac18\widehat G_{ab}
+\frac1{48}\varepsilon_{abcde}\widehat H^{cde},\\
\mathcal D_a\psi^i&=
\left(\frac14\widehat G_{bc}-T_{bc}\right)\gamma^{bc}\psi_a^i
-\frac g2L^{ij}\psi_{aj}-\phi_a^i,\\
\mathcal D_a\psi_i&=
\left(\frac14\widehat G_{bc}-T_{bc}\right)\gamma^{bc}\psi_{ai}
+\frac g2L_{ij}\psi_a^j-\phi_{ai},\\
\chi^i&=\Bigg[
\frac i8\left(\frac14\widehat G_{bc}-T_{bc}\right)\gamma^{abc}\psi_a^i
+\frac i4\left(\frac14\widehat G^{ab}-T^{ab}\right)\gamma_b\psi_a^i
-\frac{ig}{16}L^{ij}\gamma^a\psi_{aj}
-\frac i8\gamma^a\phi_a^i+\frac g8\varphi^i
\Bigg]_1,\\
\mathcal D_a\mathcal D_b\sigma&=
2f_{ab}-\frac i2\bar\psi_a\mathcal D_b\psi
-2\bar\psi_a\gamma_b\chi,\\
\Box^c\sigma&=2f_a{}^a-\frac i2\bar\psi_a\mathcal D^a\psi
-2\bar\psi_a\gamma^a\chi,\\
D&=\Bigg[
\frac12 f_a{}^a-\frac1{16}\widehat G_{ab}\widehat G^{ab}
-\frac{26}{3}T_{ab}T^{ab}+2\widehat G^{ab}T_{ab}
+\frac g4N+\frac{g^2}{16}L^2\\
&\hspace{12mm}
-\frac i8\left(\frac14\widehat G_{bc}-T_{bc}\right)
\bar\psi_a^i\gamma^{bc}\psi^a_i
-\frac{ig}{16}L_{ij}\bar\psi_a^i\psi^{aj}
+\frac i8\bar\psi_a^i\phi^a_i
-\frac12\bar\psi_a\gamma^a\chi
\Bigg]_{\le2}.
\end{aligned}
```

## Full supercovariant derivative

```math
\begin{aligned}
\mathcal D_\mu\Phi&=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\\
\mathcal D_a&=e_a{}^\mu\mathcal D_\mu,\qquad
\Box^c\Phi=\mathcal D^a\mathcal D_a\Phi,\\
\mathcal D_\mu L^{ij}&=(\partial_\mu-3b_\mu)L^{ij}
+2V_\mu^{(i}{}_kL^{j)k}-i\bar\psi_\mu^{(i}\varphi^{j)},\\
\mathcal D_\mu\varphi^i&=
\left(\partial_\mu-\frac72b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi^i
-V_\mu^{ij}\varphi_j
+\frac i2\gamma^a\mathcal D_aL^{ij}\psi_{\mu j}
+\frac i2E_a\gamma^a\psi_\mu^i\\
&\quad-\frac12N\psi_\mu^i+T_{ab}\gamma^{ab}L^{ij}\psi_{\mu j}
-3L^{ij}\phi_{\mu j},\\
\mathcal D_\mu E_a&=(\partial_\mu-4b_\mu)E_a-\omega_\mu{}^b{}_aE_b
+\frac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
+2T_{ba}\bar\psi_\mu\gamma^b\varphi+2\bar\phi_\mu\gamma_a\varphi,\\
\mathcal D_\mu N&=(\partial_\mu-4b_\mu)N
-\frac12\bar\psi_\mu\gamma^a\mathcal D_a\varphi
-\frac{3i}{2}T_{ab}\bar\psi_\mu\gamma^{ab}\varphi
-4iL_{ij}\bar\psi_\mu^i\chi^j
-\frac{3i}{2}\bar\phi_\mu\varphi,\\
\mathcal D_\mu T_{ab}&=(\partial_\mu-b_\mu)T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}
-\frac i2\bar\psi_\mu\gamma_{ab}\chi
+\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
\end{aligned}
```

## Dependent connections and curvatures

```math
\begin{aligned}
\omega_\mu{}^{ab}&=
2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,\\
R_{\mu\nu}{}^{ab}(\omega)&=
2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
\widehat R'_{\mu\nu}{}^i(Q)&=
2\partial_{[\mu}\psi_{\nu]}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
-2V_{[\mu}^{ij}\psi_{\nu]j}
+2iT_{ab}\gamma_{[\mu}{}^{ab}\psi_{\nu]}^i
-4iT_{[\mu|b|}\gamma^b\psi_{\nu]}^i,\\
\phi_\mu^i&=\frac i4\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac i{24}\gamma_\mu{}^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)&=
\widehat R'_{\mu\nu}{}^i(Q)-2i\gamma_{[\mu}\phi_{\nu]}^i,\\
\widehat R'_{\mu\nu}{}^{ab}(M)&=
R_{\mu\nu}{}^{ab}(\omega)+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+iT_{cd}\bar\psi_{[\mu}\gamma^{abcd}\psi_{\nu]}
+2iT^{ab}\bar\psi_{[\mu}\psi_{\nu]}\\
&\quad+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\mathcal R_{\mu\nu}&=
\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},\qquad
\mathcal R=\mathcal R_\mu{}^\mu,\\
f_\mu{}^a&=-\frac16\mathcal R_\mu{}^a
+\frac1{48}e_\mu{}^a\mathcal R,\qquad
f_a{}^a=-\frac1{16}\mathcal R,\\
\widehat C_{abcd}&=\widehat R'_{abcd}(M)+8f_{[a[c}\eta_{b]d]},\\
\widehat R_{\mu\nu}^{ij}(V)&=
2\partial_{[\mu}V_{\nu]}^{ij}-2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-iT_{ab}\bar\psi_{[\mu}^{(i}\gamma^{ab}\psi_{\nu]}^{j)}.
\end{aligned}
```

## Bosonic dictionary

In bosonic files, $`\mathscr D`$ is the fermion-degree-zero part of the full supercovariant derivative. The notation $`\Box_{\mathrm B}^c=\mathscr D^a\mathscr D_a`$ is used. The $`K`$ connection acting on derivative descendants is retained.

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}
 +\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho},\\
E^{\mu\nu}&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
 E_{\rho\sigma\lambda},\\
E^\mu&=e^{-1}\partial_\nu(eE^{\mu\nu})
=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
 \partial_\nu E_{\rho\sigma\lambda},\\
R_{\mu\nu}^{ij}(V)
&=2\partial_{[\mu}V_{\nu]}^{ij}
 -2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)},\\
f_{ab}&=-\frac16R_{ab}+\frac1{48}\eta_{ab}R,
\qquad f_a{}^a=-\frac1{16}R,\\
T_{ab}&=\frac18G_{ab}+\frac1{48}\varepsilon_{abcde}H^{cde},\\
D&=-\frac1{32}R-\frac1{16}G_{ab}G^{ab}
 -\frac{26}{3}T_{ab}T^{ab}+2G^{ab}T_{ab}
 +\frac g4N+\frac{g^2}{16}L^2\\
&=-\frac1{32}R+\frac5{96}G_{ab}G^{ab}
 -\frac1{288}\varepsilon_{abcde}G^{ab}H^{cde}
 +\frac{13}{288}H_{abc}H^{abc}
 +\frac g4N+\frac{g^2}{16}L^2.
\end{aligned}
```

```math
\begin{aligned}
\varepsilon_{abcde}\varepsilon^{abfgh}H^{cde}H_{fgh}
&=-12H_{abc}H^{abc},\\
T_{ab}T^{ab}
&=\frac1{64}G_{ab}G^{ab}
 +\frac1{192}\varepsilon_{abcde}G^{ab}H^{cde}
 -\frac1{192}H_{abc}H^{abc}.
\end{aligned}
```

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}
&=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
 +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
R_{abcd}&=e_a{}^\mu e_b{}^\nu R_{\mu\nu cd},\qquad
R_{bd}=\eta^{ac}R_{abcd},\qquad R=\eta^{bd}R_{bd},\\
C_{abcd}
&=R_{abcd}
 -\frac13(\eta_{ac}R_{bd}-\eta_{bc}R_{ad}
           -\eta_{ad}R_{bc}+\eta_{bd}R_{ac})
 +\frac R{12}(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}).
\end{aligned}
```

```math
\begin{aligned}
\mathscr D_\mu\Phi
&=\left[\partial_\mu-\delta_D(b_\mu)
 -\delta_M(\omega_\mu(e))-\delta_U(V_\mu)
 -\delta_K(f_\mu)\right]\Phi,\qquad b_\mu=0,\\
\mathscr D_a&=e_a{}^\mu\mathscr D_\mu,\qquad
\Box_{\mathrm B}^{c}=\mathscr D^a\mathscr D_a.
\end{aligned}
```

```math
\begin{aligned}
\mathscr D_\mu L^{ij}
&=\partial_\mu L^{ij}+2V_\mu^{(i}{}_kL^{j)k},\\
\mathscr D_\mu T_{ab}
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c},\\
\mathscr D_\mu L&=\partial_\mu L,\qquad
\mathscr D_\mu N=\partial_\mu N.
\end{aligned}
```

```math
\begin{aligned}
\mathscr D_a\sigma&=0,\\
\mathscr D_a\mathscr D_b\sigma
&=2f_{ab}=-\frac13R_{ab}+\frac1{24}\eta_{ab}R,\\
\Box_{\mathrm B}^{c}\sigma&=2f_a{}^a=-\frac18R.
\end{aligned}
```

## Covariant meaning of the dictionary

The full $`Q/S/K`$ action of higher supercovariant derivatives on each descendant is part of the compact operator meaning of this dictionary. The dictionary specifies the source definitions; the action and spectrum chapters state their evaluated expressions and checks.
