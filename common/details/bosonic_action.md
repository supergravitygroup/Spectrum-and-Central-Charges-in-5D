# Bosonic action

The bosonic density is defined by setting all physical fermions to zero in the [combined component action](component_action.md). The explicit density is obtained by applying the bosonic projection below to the zero-explicit-fermion part of the [combined action](component_action.md) specified there. The conventions agree with [CONVENTIONS.md](source_conventions.md).

## Bosonic projection

```math
\begin{gathered}
\psi_\mu^i=\varphi^i=0,
\qquad \chi^i=\phi_\mu^i=\widehat R_{\mu\nu}{}^i(Q)=0,\\
\widehat G_{\mu\nu}\longmapsto G_{\mu\nu},\qquad
\widehat H_{\mu\nu\rho}\longmapsto H_{\mu\nu\rho},\qquad
\widehat C_{abcd}\longmapsto C_{abcd},\qquad
\widehat R_{ab}^{ij}(V)\longmapsto R_{ab}^{ij}(V),\\
\mathcal D_a\longmapsto\mathscr D_a,\qquad
\Box^c\longmapsto\Box_{\mathrm B}^{c}.
\end{gathered}
```

Under this projection, all terms with explicit fermions vanish. The hatted and composite objects in the source expression named $`\mathscr L^{[0]}_{\mathrm a}`$ are also made bosonic by the rule above:

```math
\begin{aligned}
\mathscr P_{\mathrm B}\mathscr L^{[2]}_{\mathrm a}&=0,\\
\ell_{\mathrm B}
&=\mathscr P_{\mathrm B}\mathscr L^{[0]}_{\mathrm a}
=\ell_{2\partial}^{\mathrm B}
 +\alpha\ell_{\mathrm{Weyl}^2}^{\mathrm B}
 +\beta\ell_{\mathrm{LOG}}^{\mathrm B}
 +\zeta\ell_{R^2}^{\mathrm B}.
\end{aligned}
```

## Fields and bosonic definitions

The source's existing gauge conditions are retained:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac L{\sqrt2}\delta_{ij},\qquad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad \delta_{ij}V_\mu^{\prime\,ij}=0.
```

```math
\begin{gathered}
\Phi_{\mathrm B}
=\{e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},
L,N,V_\mu,V_\mu^{\prime\,ij}\},\\
L^{ij}L_{ij}=L^2,\qquad L\ne0,\qquad g\ne0,\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad e=\sqrt{-g}.
\end{gathered}
```

$`\alpha,\beta,\zeta,g,\kappa_5`$ is symbolic. The fields $`L,N,E_3,V,V'`$ are retained. The notation $`T,D,f,E^a,E^{ab}`$ below does not introduce new independent fields; their explicit bosonic definitions are:

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

Contraction used in the last equality:

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

$`\omega_\mu{}^{ab}(e)`$ is the torsion-free spin connection. The curvatures are:

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

All indices are converted using the same vielbein; $`\varepsilon^{\mu\nu\rho\sigma\lambda}`$ is the epsilon tensor and $`\epsilon^{\mu\nu\rho\sigma\lambda} =e\varepsilon^{\mu\nu\rho\sigma\lambda}`$ is the density symbol.

## Bosonic covariant derivative

$`\mathscr D`$ is the source superconformal derivative after setting fermions to zero. It contains only bosonic connections:

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

Here $`\delta_D,\delta_M,\delta_U,\delta_K`$ are the actions of the source dilatation, Lorentz, internal-symmetry and special-conformal generators, respectively, on the relevant field or derivative descendant. For example

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

The source's ordered covariant derivatives are constructed before imposing gauge conditions. The bosonic $`f_{ab}`$ connection is retained in second and higher derivatives. In particular, in the existing $`\sigma=1`$ notation

```math
\begin{aligned}
\mathscr D_a\sigma&=0,\\
\mathscr D_a\mathscr D_b\sigma
&=2f_{ab}=-\frac13R_{ab}+\frac1{24}\eta_{ab}R,\\
\Box_{\mathrm B}^{c}\sigma&=2f_a{}^a=-\frac18R.
\end{aligned}
```

$`\Box_{\mathrm B}^{c}\mathscr D_a\sigma`$ and $`\mathscr D_a\Box_{\mathrm B}^{c}\sigma`$ are also these ordered bosonic conformal derivatives. These descendants are not discarded by prematurely setting the first derivative's gauge value to zero. Every $`T,D,f`$ and its derivatives below use the bosonic definition above and contain no implicit fermions.

## Full bosonic density and action

```math
\boxed{
S_{\mathrm B}
=\frac1{2\kappa_5^2}\int d^5x\,e\,\ell_{\mathrm B}.
}
```

Retaining the source's total derivatives, parentheses and derivative order:

```math
\begin{aligned}
\ell_{\mathrm B}={}&C_{a}\Big[\beta H_{bcd}\Big[\frac{1}{248832} H_{efg}\Big[\varepsilon^{defg}{}_{h}\Big[27648 \mathscr D^{h}(H^{abc})\\
&+7632 C^{abch}\\
&+504 C^{ahbc}\\
&-6480 C^{bhac}\\
&-6408 G^{ab} G^{ch}\\
&+19823 G^{ah} G^{bc}\Big]\\
&+5 \varepsilon^{efg}{}_{hm}\Big[2725 H^{abc} H^{dhm}\\
&-2032 H^{abh} H^{cdm}\\
&-1247 H^{ahm} H^{bcd}\Big]\\
&+1152 \varepsilon^{bcdef}\Big[7 \mathscr D^{a}\mathscr D^{g}(\sigma)\\
&-37 \mathscr D^{g}\mathscr D^{a}(\sigma)\Big]\\
&-4752 \varepsilon^{ahefg} C^{b}{}_{h}{}^{cd}\\
&+23027 \varepsilon^{cdefg} G^{a}{}_{h} G^{hb}\Big]\\
&+\frac{1}{497664} G_{ef}\Big[H^{a}{}_{gh}\Big[-8770 \varepsilon^{efbcd} G^{gh}\\
&-92108 \varepsilon^{fhbcd} G^{eg}\\
&+23027 \varepsilon^{ghbcd} G^{ef}\Big]\\
&+4385 G_{gh}\Big[3 \varepsilon^{efghd} H^{abc}\\
&+4 \varepsilon^{fhbcd} H^{aeg}\Big]\\
&+2\Big[13824 \varepsilon^{bcdf}{}_{g}\Big[-\mathscr D^{a}(G^{eg})\\
&-4 \mathscr D^{e}(G^{ag})\Big]\\
&+6912 \varepsilon^{abcd}{}_{g}\Big[4 \mathscr D^{e}(G^{fg})\\
&-\mathscr D^{g}(G^{ef})\Big]\\
&-41472 \mathscr D^{g}(G^{a}{}_{g}) \varepsilon^{efbcd}\\
&-13824 \mathscr D^{g}(G^{e}{}_{g}) \varepsilon^{afbcd}\\
&+26677 H^{aef} H^{bcd}\Big]\Big]\\
&+\frac{1}{576} G^{a}{}_{e}\Big[32 \varepsilon^{bcd}{}_{fg}\Big[-5 \mathscr D^{e}(G^{fg})\\
&+3 \mathscr D^{f}(G^{eg})\Big]\\
&-192 \mathscr D^{b}(H^{ecd})\\
&+64 \mathscr D^{e}(H^{bcd})\\
&+53 C^{bced}\\
&-5 C^{ebcd}\\
&+160 \mathscr D^{f}(G_{fg}) \varepsilon^{egbcd}\Big]\\
&+\frac{1}{82944} H^{a}{}_{ef}\Big[192 \varepsilon^{bcd}{}_{gh}\Big[-18 C^{egfh}\\
&-11 C^{ghef}\Big]\\
&+11520 \Box_{\mathrm B}^{c}(\sigma) \varepsilon^{efbcd}\\
&-26677 G^{bc} H^{efd}\\
&-53354 G^{eb} H^{fcd}\Big]\\
&+\frac{1}{18} \mathscr D_{e}(H_{fgh})\Big[-2 \varepsilon^{adfgh} H^{bce}\\
&+\varepsilon^{aefgh} H^{bcd}\\
&-2 \varepsilon^{defgh} H^{abc}\Big]\\
&+\frac{1}{576} G^{d}{}_{e}\Big[-165 C^{abec}\\
&+133 C^{aebc}\\
&-21 C^{bcae}\\
&-485 C^{ebac}\Big]\\
&+\frac{1}{20736} G^{b}{}_{e}\Big[27648 \mathscr D^{c}(H^{aed})\\
&-6912 \mathscr D^{e}(H^{acd})\\
&+26677 H^{ac}{}_{f} H^{efd}\Big]\\
&+\frac{1}{1152} C_{efgh}\Big[5 \varepsilon^{aefgh} H^{bcd}\\
&+6 \varepsilon^{efghd} H^{abc}\Big]\\
&+\frac{1}{576} H^{cd}{}_{e}\Big[-192 \mathscr D^{e}(G^{ab})\\
&+5 \varepsilon^{afghe} C^{b}{}_{fgh}\Big]\\
&+\frac{1}{6} H^{ad}{}_{e}\Big[-10 \mathscr D^{b}(G^{ec})\\
&+\mathscr D^{e}(G^{bc})\Big]\\
&+\frac{1}{6} G^{bc}\Big[\mathscr D^{a}\mathscr D^{d}(\sigma)\\
&+3 \mathscr D^{d}\mathscr D^{a}(\sigma)\Big]\\
&+\frac{1}{9} G^{ab}\Big[5 \mathscr D^{c}\mathscr D^{d}(\sigma)\\
&-3 \mathscr D^{e}(H^{cd}{}_{e})\Big]\\
&+\varepsilon^{abcd}{}_{e}\Big[\frac{2}{9} \Box_{\mathrm B}^{c}\mathscr D^{e}(\sigma)\\
&+\frac{L g^{2}}{18} \mathscr D^{e}(L)\\
&+\frac{g}{9} \mathscr D^{e}(N)\\
&-\frac{1}{9} \mathscr D^{e}\Box_{\mathrm B}^{c}(\sigma)\\
&-\frac{55}{864} \mathscr D^{f}\mathscr D^{g}(H_{fg}{}^{e})\Big]\\
&+\frac{1}{864}\Big[\varepsilon^{bcd}{}_{ef}\Big[25 \mathscr D^{e}\mathscr D^{g}(H^{a}{}_{g}{}^{f})\\
&+72 \mathscr D^{g}(C^{ae}{}_{g}{}^{f})\\
&+36 \mathscr D^{g}(C^{a}{}_{g}{}^{ef})\\
&-55 \mathscr D^{g}\mathscr D^{e}(H^{a}{}_{g}{}^{f})\Big]\\
&+\varepsilon^{cd}{}_{efg}\Big[8 \mathscr D^{a}\mathscr D^{b}(H^{efg})\\
&+25 \mathscr D^{b}\mathscr D^{a}(H^{efg})\Big]\\
&+3\Big[3 \varepsilon^{ad}{}_{efg}\Big[8 \mathscr D^{b}\mathscr D^{c}(H^{efg})\\
&-11 \mathscr D^{e}\mathscr D^{f}(H^{bcg})\Big]\\
&+16\Big[-4 \mathscr D^{a}\mathscr D^{b}(G^{cd})\\
&+10 \mathscr D^{b}\mathscr D^{a}(G^{cd})\\
&-2 \mathscr D^{b}\mathscr D^{c}(G^{ad})\\
&+\mathscr D^{e}(G^{a}{}_{e}) H^{bcd}\\
&+6 \mathscr D^{e}(G_{e}{}^{b}) H^{acd}\Big]\Big]\Big]\Big]\\
&+\frac{\beta}{82944} G_{bc}\Big[G_{de}\Big[G_{fg}\Big[-4408 \varepsilon^{acefg} G^{bd}\\
&+1102 \varepsilon^{adefg} G^{bc}\\
&-86015 \varepsilon^{cdefg} G^{ab}\Big]\\
&+72\Big[112 \varepsilon^{bcde}{}_{f}\Big[\mathscr D^{a}\mathscr D^{f}(\sigma)\\
&-4 \mathscr D^{f}\mathscr D^{a}(\sigma)\Big]\\
&+\varepsilon^{ade}{}_{fg}\Big[-C^{bcfg}\\
&-31 C^{bfcg}\Big]\\
&+2\Big[\varepsilon^{ace}{}_{fg}\Big[5 C^{bdfg}\\
&-41 C^{bfdg}\Big]\\
&+168 \Box_{\mathrm B}^{c}(\sigma) \varepsilon^{abcde}\Big]\Big]\Big]\\
&+36\Big[G^{a}{}_{d}\Big[2 \varepsilon^{cd}{}_{efg}\Big[-320 \mathscr D^{b}(H^{efg})\\
&+9 C^{befg}\Big]\\
&+3\Big[\varepsilon^{bc}{}_{efg}\Big[-128 \mathscr D^{d}(H^{efg})\\
&+25 C^{defg}\Big]\\
&+896\Big[2 \mathscr D^{b}(G^{dc})\\
&-\mathscr D^{d}(G^{bc})\Big]\Big]\Big]\\
&+2 H^{a}{}_{de}\Big[384 \mathscr D^{b}(H^{cde})\\
&-19 C^{bcde}\\
&-16 C^{bdce}\\
&+59 C^{debc}\Big]\\
&+128 \mathscr D_{d}(H_{efg})\Big[-\varepsilon^{acefg} G^{bd}\\
&+\varepsilon^{adefg} G^{bc}\\
&+\varepsilon^{cdefg} G^{ab}\Big]\\
&+256 H^{ab}{}_{d}\Big[4 \mathscr D^{c}\mathscr D^{d}(\sigma)\\
&-7 \mathscr D^{d}\mathscr D^{c}(\sigma)\\
&+12 \mathscr D^{e}(H^{cd}{}_{e})\Big]\\
&+C_{defg}\Big[35 \varepsilon^{adefg} G^{bc}\\
&+12 \varepsilon^{defgc} G^{ab}\Big]\\
&+4\Big[2 \varepsilon^{bc}{}_{def}\Big[-5 \mathscr D^{a}\mathscr D^{d}(G^{ef})\\
&+23 \mathscr D^{d}\mathscr D^{a}(G^{ef})\\
&+24 \mathscr D^{d}\mathscr D^{e}(G^{af})\Big]\\
&+8 \varepsilon^{ac}{}_{def}\Big[-2 \mathscr D^{b}\mathscr D^{d}(G^{ef})\\
&+5 \mathscr D^{d}\mathscr D^{b}(G^{ef})\\
&-9 \mathscr D^{d}\mathscr D^{e}(G^{bf})\Big]\\
&+4 \varepsilon^{abc}{}_{de}\Big[-21 \Box_{\mathrm B}^{c}(G^{de})\\
&-5 \mathscr D^{d}\mathscr D^{f}(G_{f}{}^{e})\\
&-25 \mathscr D^{f}\mathscr D^{d}(G_{f}{}^{e})\Big]\\
&-32 \mathscr D^{a}\mathscr D^{d}(H^{bc}{}_{d})\\
&+160 \mathscr D^{b}\mathscr D^{d}(H^{ac}{}_{d})\\
&-144 \mathscr D^{d}(C^{ab}{}_{d}{}^{c})\\
&-72 \mathscr D^{d}(C^{a}{}_{d}{}^{bc})\\
&+32 \mathscr D^{d}\mathscr D^{a}(H^{bc}{}_{d})\\
&-352 \mathscr D^{d}\mathscr D^{b}(H^{ac}{}_{d})\\
&-384 \Box_{\mathrm B}^{c}(\sigma) H^{abc}\\
&+384 \mathscr D^{d}(G^{ac}) G^{b}{}_{d}\\
&-96 \mathscr D^{d}(G^{a}{}_{d}) G^{bc}\\
&-384 \mathscr D^{d}(G^{c}{}_{d}) G^{ab}\\
&-43 \varepsilon^{adefg} C^{b}{}_{def} G^{c}{}_{g}\Big]\Big]\Big]\\
&+\beta \mathscr D_{b}(H_{cde})\Big[\frac{1}{4608} \varepsilon^{cde}{}_{fg}\Big[191 \mathscr D^{a}(H^{bfg})\\
&-191 \mathscr D^{b}(H^{afg})\\
&-561 \mathscr D^{f}(H^{abg})\Big]\\
&+\frac{1}{1536} \varepsilon^{bcde}{}_{f}\Big[-64 \mathscr D^{a}\mathscr D^{f}(\sigma)\\
&+320 \mathscr D^{f}\mathscr D^{a}(\sigma)\\
&+241 \mathscr D^{g}(H^{a}{}_{g}{}^{f})\Big]\\
&+\frac{1}{4608} \varepsilon^{acde}{}_{f}\Big[1920 \mathscr D^{b}\mathscr D^{f}(\sigma)\\
&-384 \mathscr D^{f}\mathscr D^{b}(\sigma)\\
&-431 \mathscr D^{g}(H_{g}{}^{bf})\Big]\\
&+\varepsilon^{abcde}\Big[-\frac{g (L^{2} g + 4 N)}{36}\\
&-\frac{5}{18} \Box_{\mathrm B}^{c}(\sigma)\Big]\\
&+\frac{431}{1536} \mathscr D^{f}(H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}\Big]\\
&+\frac{\beta}{1536} \mathscr D_{b}(G_{cd})\Big[\varepsilon^{bcd}{}_{ef}\Big[-415 \mathscr D^{a}(G^{ef})\\
&+113 \mathscr D^{e}(G^{af})\Big]\\
&+\varepsilon^{abd}{}_{ef}\Big[1105 \mathscr D^{c}(G^{ef})\\
&-2078 \mathscr D^{e}(G^{cf})\Big]\\
&+1728 \mathscr D^{a}(H^{bcd})\\
&-704 \mathscr D^{b}(H^{acd})\\
&+2432 \mathscr D^{c}(H^{abd})\\
&-353 \mathscr D^{b}(G_{ef}) \varepsilon^{aefcd}\\
&+525 \mathscr D^{e}(G_{ef}) \varepsilon^{afbcd}\Big]\\
&+\frac{4 \alpha}{9} T_{bc}\Big[64 T^{a}{}_{d}\Big[-6 \mathscr D^{b}(T^{dc})\\
&-\mathscr D^{d}(T^{bc})\Big]\\
&+24 \varepsilon^{ac}{}_{def}\Big[-2 \mathscr D^{d}\mathscr D^{b}(T^{ef})\\
&+3 \mathscr D^{d}\mathscr D^{e}(T^{bf})\Big]\\
&+9 \mathscr D^{d}(C^{a}{}_{d}{}^{bc})\\
&+384 T^{ab} \mathscr D^{d}(T^{c}{}_{d})\\
&-32 T^{bc} \mathscr D^{d}(T^{a}{}_{d})\\
&-384 T^{b}{}_{d} \mathscr D^{d}(T^{ac})\Big]\\
&+\frac{\beta}{864} H^{a}{}_{bc}\Big[2 \varepsilon^{c}{}_{defg}\Big[67 \mathscr D^{b}\mathscr D^{d}(H^{efg})\\
&+44 \mathscr D^{d}\mathscr D^{b}(H^{efg})\Big]\\
&+3\Big[96 \Box_{\mathrm B}^{c}(G^{bc})\\
&-32 \mathscr D^{b}\mathscr D^{d}(G_{d}{}^{c})\\
&-160 \mathscr D^{d}\mathscr D^{b}(G_{d}{}^{c})\\
&-11 \Box_{\mathrm B}^{c}(H_{efg}) \varepsilon^{bcefg}\Big]\Big]\\
&+\frac{\beta}{12} \mathscr D_{b}\mathscr D_{c}(\sigma)\Big[6 \mathscr D^{a}(G^{bc})\\
&+6 \mathscr D^{b}(G^{ac})\\
&+6 \mathscr D^{c}(G^{ab})\\
&+\mathscr D^{a}(H_{def}) \varepsilon^{defbc}\Big]\\
&+\beta G^{a}{}_{b}\Big[\frac{2}{3} \Box_{\mathrm B}^{c}\mathscr D^{b}(\sigma)\\
&-\frac{4 L g^{2}}{3} \mathscr D^{b}(L)\\
&-\frac{5 g}{3} \mathscr D^{b}(N)\\
&-\frac{1}{3} \mathscr D^{b}\Box_{\mathrm B}^{c}(\sigma)\\
&-\frac{1}{18} \mathscr D^{c}\mathscr D^{d}(H^{b}{}_{cd})\\
&+\frac{7}{144} \mathscr D^{c}\mathscr D^{d}(G_{ef}) \varepsilon^{b}{}_{cd}{}^{ef}\Big]\\
&+\frac{4 \alpha}{3} \mathscr D_{b}(T_{cd})\Big[8 \varepsilon^{abd}{}_{ef}\Big[2 \mathscr D^{c}(T^{ef})\\
&-3 \mathscr D^{e}(T^{cf})\Big]\\
&+3 C^{abcd}\Big]\\
&+\frac{\beta}{12} \mathscr D_{b}(G^{b}{}_{c})\Big[3 \mathscr D^{a}\mathscr D^{c}(\sigma)\\
&-15 \mathscr D^{c}\mathscr D^{a}(\sigma)\\
&+4 \mathscr D^{d}(H^{ac}{}_{d})\Big]\\
&+\frac{\beta}{12} \mathscr D_{b}(H_{cd}{}^{b})\Big[7 \mathscr D^{a}(G^{cd})\\
&-18 \mathscr D^{c}(G^{ad})\Big]\\
&+\beta \mathscr D_{b}(G^{ab})\Big[-\frac{g (2 L^{2} g + 5 N)}{3}\\
&-\frac{2}{3} \Box_{\mathrm B}^{c}(\sigma)\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[\frac{\beta}{6} \Box_{\mathrm B}^{c}\mathscr D^{b}(H^{cde})\\
&+\frac{\alpha}{16} C^{bc}{}_{fg} C^{defg}\\
&-\frac{\alpha + \beta}{12} R^{bc}{}_{ij}(V) R^{deij}(V)\Big]\\
&-\frac{64 D \alpha}{3} \mathscr D^{b}(T^{a}{}_{b})\\
&+\beta g L^{ij} \mathscr D^{b}(R^{a}{}_{bij}(V))\\
&-\frac{64 \alpha}{3} T^{a}{}_{b} \mathscr D^{b}(D)\\
&+\beta g \mathscr D^{b}(L^{ij}) R^{a}{}_{bij}(V)\Big]\\
&+G_{ab}\Big[\beta H_{cde}\Big[\frac{1}{12} G_{fg}\Big[-2 \varepsilon^{bgcde} G^{af}\\
&+\varepsilon^{fgcde} G^{ab}\Big]\\
&+\frac{1}{3456} \varepsilon^{cde}{}_{fg}\Big[225 \mathscr D^{f}(H^{abg})\\
&-136 C^{afbg}\\
&-92 C^{fgab}\Big]\\
&+\frac{7}{27} \varepsilon^{acde}{}_{f}\Big[-\mathscr D^{b}\mathscr D^{f}(\sigma)\\
&+\mathscr D^{f}\mathscr D^{b}(\sigma)\Big]\\
&+\varepsilon^{abcde}\Big[\frac{g (L^{2} g + 4 N)}{36}\\
&+\frac{1}{9} \Box_{\mathrm B}^{c}(\sigma)\Big]\\
&+\frac{1}{6912}\Big[-278 \mathscr D^{f}(H^{a}{}_{fg}) \varepsilon^{bcdeg}\\
&-267 \mathscr D^{f}(H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}\\
&-192 G^{ab} H^{cde}\\
&+1152 G^{ac} H^{bde}\\
&-2304 G^{cd} H^{abe}\Big]\Big]\\
&+L^{ij}\Big[\frac{\zeta}{L^{3}} \mathscr D_{c}(L_{j}{}^{k}) \mathscr D_{d}(L_{ik}) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{2 L} E^{e}\\
&-\frac{\sqrt{2}}{4} V^{e}\Big]\\
&+\frac{\zeta}{L} R_{cdij}(V) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{2 L} E^{e}\\
&-\frac{\sqrt{2}}{4} V^{e}\Big]\\
&-\big(\frac{\beta g}{3} + \frac{N \zeta}{L^{2}}\big) R^{ab}{}_{ij}(V)\\
&+\frac{N \zeta}{L^{4}} \mathscr D^{a}(L_{ki}) \mathscr D^{b}(L^{k}{}_{j})\Big]\\
&+\frac{\beta}{144} G_{cd}\Big[-96 \mathscr D^{a}(H^{bcd})\\
&+17 C^{abcd}\\
&+22 C^{acbd}\\
&+12 \mathscr D^{e}(G_{ef}) \varepsilon^{abcdf}\\
&+9 G^{ab} G^{cd}\\
&-54 G^{ac} G^{bd}\Big]\\
&+\frac{\beta}{6912} \mathscr D_{c}(H_{def})\Big[456 \varepsilon^{bgdef} H^{ac}{}_{g}\\
&-1129 \varepsilon^{gcdef} H^{ab}{}_{g}\Big]\\
&+\frac{\zeta}{L} \mathscr D_{c}(E_{d}) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{L} E^{e}\\
&-\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\frac{\beta}{3} H^{b}{}_{cd}\Big[-2 \mathscr D^{a}(G^{cd})\\
&+\mathscr D^{c}(G^{ad})\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V^{b}\Big[-\frac{N}{L} \mathscr D^{a}(L)\\
&+\mathscr D^{a}(N)\Big]\\
&+\frac{\beta}{432} \varepsilon^{b}{}_{cdef}\Big[-27 \mathscr D^{a}(C^{cdef})\\
&+112 \mathscr D^{a}\mathscr D^{c}(H^{def})\\
&-27 \mathscr D^{c}(C^{adef})\\
&+8 \mathscr D^{c}\mathscr D^{a}(H^{def})\Big]\\
&+\varepsilon^{ab}{}_{cde}\Big[-\frac{3 \beta}{32} \mathscr D^{f}(C_{f}{}^{cde})\\
&-\frac{\sqrt{2} \zeta}{2 L^{2}} E^{c} V^{e} \mathscr D^{d}(L)\Big]\\
&+\frac{16 N^{2} \zeta}{L^{2}} T^{ab}\\
&+\frac{\beta}{3} \Box_{\mathrm B}^{c}(G^{ab})\\
&-\frac{2 N \zeta}{L^{2}} \mathscr D^{a}(E^{b})\\
&+\frac{2 \beta}{9} \mathscr D^{a}\mathscr D^{c}(G^{b}{}_{c})\\
&+\frac{\beta}{9} \mathscr D^{c}\mathscr D^{a}(G^{b}{}_{c})\\
&+\frac{\beta g (3 L^{2} g + 4 N)}{8} G^{ab}\\
&-\frac{2 \zeta}{L^{2}} E^{a} \mathscr D^{b}(N)\\
&-\frac{\beta}{3} \mathscr D^{c}(G_{cd}) H^{abd}\\
&-\frac{4 \beta}{3} \mathscr D^{c}\mathscr D^{b}(\sigma) G^{a}{}_{c}\\
&+\frac{563 \beta}{6912} \mathscr D^{b}(H_{cde}) \varepsilon^{fgcde} H^{a}{}_{fg}\Big]\\
&+\frac{1}{L} E_{a}\Big[\frac{2}{L} \mathscr D_{b}(L)\Big[\frac{\zeta}{L} \mathscr D^{b}(L)\Big[\frac{2}{L} E^{a}\\
&+\sqrt{2} V^{a}\Big]\\
&+\frac{\zeta}{L} \mathscr D^{a}(L)\Big[-\frac{2}{L} E^{b}\\
&-\sqrt{2} V^{b}\Big]\\
&+\frac{\zeta}{L} L^{ij}\Big[R^{ab}{}_{ij}(V)\\
&-\frac{5}{L^{2}} \mathscr D^{a}(L_{ki}) \mathscr D^{b}(L^{k}{}_{j})\Big]\\
&-2 E^{ab}\\
&+\frac{\zeta}{L} \mathscr D^{a}(E^{b})\\
&-\frac{2 \zeta}{L} \mathscr D^{b}(E^{a})\Big]\\
&+E^{a}\Big[2 (- \frac{4 D \zeta}{L} + 1 + \frac{N \zeta (g + \frac{N}{L^{2}})}{L})\\
&-\frac{4 \zeta}{L^{2}} \Box_{\mathrm B}^{c}(L)\\
&+\frac{\zeta}{L^{3}} E^{b} E_{b}\\
&-\frac{16 \zeta}{3 L} T^{bc} T_{bc}\\
&+\frac{\zeta}{L^{3}} \mathscr D^{b}(L^{ij}) \mathscr D_{b}(L_{ij})\Big]\\
&+\frac{\zeta}{L}\Big[2 L^{ij}\Big[\frac{1}{L^{2}} \mathscr D^{a}(L_{ik})\Big[3 \Box_{\mathrm B}^{c}(L^{k}{}_{j})\\
&-\frac{1}{L^{2}} E_{b} L^{kl} \mathscr D^{b}(L_{jl})\Big]\\
&-\mathscr D^{b}(R^{a}{}_{bij}(V))\\
&-\frac{1}{L^{2}} \mathscr D^{b}\mathscr D^{a}(L^{k}{}_{j}) \mathscr D_{b}(L_{ki})\Big]\\
&+\mathscr D^{a}\mathscr D_{b}(L)\Big[\frac{2}{L} E^{b}\\
&+\sqrt{2} V^{b}\Big]\\
&+\mathscr D_{b}(L^{ij})\Big[-2 R^{ab}{}_{ij}(V)\\
&+\frac{1}{L^{2}} E^{b} \mathscr D^{a}(L_{ij})\Big]\\
&+2 \Box_{\mathrm B}^{c}(E^{a})\\
&+32 N \mathscr D^{b}(T^{a}{}_{b})\\
&-2 N \mathscr D^{b}(G^{a}{}_{b})\\
&-2 \mathscr D^{b}\mathscr D^{a}(E_{b})\\
&+32 T^{a}{}_{b} \mathscr D^{b}(N)\\
&-\sqrt{2} V^{a} \Box_{\mathrm B}^{c}(L)\\
&+\frac{2}{L} \mathscr D^{a}(L) \mathscr D^{b}(E_{b})\Big]\Big]\\
&+\beta H_{abc}\Big[H^{abc}\Big[\frac{g (L^{2} g - 2 N)}{12}\\
&+\frac{1}{9} \Box_{\mathrm B}^{c}(\sigma)\\
&-\frac{1}{72} H^{def} H_{def}\Big]\\
&+\frac{1}{72} H^{c}{}_{de}\Big[11 C^{abde}\\
&+10 C^{adbe}\Big]\\
&+\varepsilon^{abc}{}_{de}\Big[-\frac{1}{9} \Box_{\mathrm B}^{c}(G^{de})\\
&+\frac{2}{27} \mathscr D^{d}\mathscr D^{f}(G_{f}{}^{e})\\
&+\frac{1}{27} \mathscr D^{f}\mathscr D^{d}(G_{f}{}^{e})\\
&-\frac{g}{18} L^{ij} R^{de}{}_{ij}(V)\Big]\\
&+\frac{1}{36}\Big[4 \Box_{\mathrm B}^{c}(H^{abc})\\
&+4 \mathscr D^{a}\mathscr D^{d}(H^{bc}{}_{d})\\
&+9 \mathscr D^{d}(C^{ab}{}_{d}{}^{c})\\
&-16 \mathscr D^{d}\mathscr D^{a}(H^{bc}{}_{d})\\
&+24 \mathscr D^{d}(H^{ebc}) H^{a}{}_{de}\\
&-12 \mathscr D^{d}\mathscr D^{c}(\sigma) H^{ab}{}_{d}\\
&-\mathscr D^{d}(G_{d}{}^{a}) \varepsilon^{bcefg} H_{efg}\Big]\Big]\\
&+\mathscr D_{a}(L_{ij})\Big[\mathscr D^{a}(L^{ij})\Big[-\big(\frac{4 D \zeta}{L^{2}} + \frac{\beta g^{2}}{4} - \frac{1 + \frac{N \zeta (g + \frac{N}{L^{2}})}{L}}{L}\big)\\
&+\frac{\zeta}{L^{3}} \Box_{\mathrm B}^{c}(L)\\
&-\frac{8 \zeta}{3 L^{2}} T^{bc} T_{bc}\\
&-\frac{3 \zeta}{4 L^{4}} \mathscr D^{b}(L^{kl}) \mathscr D_{b}(L_{kl})\Big]\\
&+\frac{1}{L^{3}}\Big[L^{jk}\Big[\mathscr D_{b}(L^{i}{}_{k})\Big[2 E^{ab}\\
&-\frac{16 N \zeta}{L} T^{ab}\\
&+\frac{3 \sqrt{2} \zeta}{L} V^{b} \mathscr D^{a}(L)\Big]\\
&+\sqrt{2} \zeta\Big[V^{a} \Box_{\mathrm B}^{c}(L^{i}{}_{k})\\
&-V_{b} \mathscr D^{a}\mathscr D^{b}(L^{i}{}_{k})\Big]\Big]\\
&+\zeta \mathscr D^{a}(L)\Big[-2 \Box_{\mathrm B}^{c}(L^{ij})\\
&+\frac{1}{L} \mathscr D^{b}(L^{ij}) \mathscr D_{b}(L)\Big]\Big]\Big]\\
&+T_{ab}\Big[T_{cd}\Big[-\frac{16 \alpha}{3} C^{abcd}\\
&-\frac{64 (44 \alpha - 3 \zeta)}{27} T^{ab} T^{cd}\\
&+1024 \alpha T^{ac} T^{bd}\\
&+\frac{128 \alpha}{3} \mathscr D^{e}(T_{ef}) \varepsilon^{abcdf}\Big]\\
&+T^{ab}\Big[-\frac{16 (- 4 D (16 \alpha + 3 \zeta) + 3 L + 3 N \zeta (g + \frac{27 N}{L^{2}}))}{9}\\
&+\frac{16 \zeta}{3 L} \Box_{\mathrm B}^{c}(L)\Big]\\
&+\frac{16 \sqrt{2} \zeta}{L} V^{b}\Big[\frac{N}{L} \mathscr D^{a}(L)\\
&-\mathscr D^{a}(N)\Big]\\
&+\frac{32 N \zeta}{L^{2}} \mathscr D^{a}(E^{b})\\
&+\frac{128 \alpha}{3} \mathscr D^{a}\mathscr D^{c}(T^{b}{}_{c})\\
&-8 (\frac{\alpha g}{3} - \frac{2 N \zeta}{L^{2}}) L^{ij} R^{ab}{}_{ij}(V)\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V_{a}\Big[\frac{1}{L} \mathscr D_{b}(L)\Big[\mathscr D^{a}(E^{b})\\
&-2 \mathscr D^{b}(E^{a})\\
&-L^{ij} R^{ba}{}_{ij}(V)\Big]\\
&+\Box_{\mathrm B}^{c}(E^{a})\\
&-16 N \mathscr D^{b}(T_{b}{}^{a})\\
&+N \mathscr D^{b}(G_{b}{}^{a})\\
&-\mathscr D^{b}\mathscr D^{a}(E_{b})\\
&-L^{ij} \mathscr D^{b}(R^{a}{}_{bij}(V))\\
&+\frac{1}{L} \mathscr D^{a}(L) \mathscr D^{b}(E_{b})\\
&-\mathscr D^{b}(L^{ij}) R^{a}{}_{bij}(V)\Big]\\
&+\frac{\beta}{72} \mathscr D_{a}(H_{bcd})\Big[\varepsilon^{bcd}{}_{ef}\Big[-11 \mathscr D^{a}(G^{ef})\\
&+14 \mathscr D^{e}(G^{af})\Big]\\
&+4\Big[\mathscr D^{a}(H^{bcd})\\
&-9 \mathscr D^{b}(H^{acd})\\
&+3 \mathscr D^{e}(G_{ef}) \varepsilon^{fabcd}\Big]\Big]\\
&+\frac{3 \beta}{4} \mathscr D_{a}\mathscr D_{b}(\sigma)\Big[-2 \mathscr D^{a}\mathscr D^{b}(\sigma)\\
&+2 \mathscr D^{c}(H_{c}{}^{ab})\\
&-\mathscr D^{c}(G_{de}) \varepsilon_{c}{}^{deab}\Big]\\
&+2 E_{ab}\Big[-g G^{ab}\\
&-\frac{2}{L} \mathscr D^{a}(E^{b})\\
&-\frac{1}{L} L^{ij} R^{ab}{}_{ij}(V)\Big]\\
&+\beta \Box_{\mathrm B}^{c}(\sigma)\Big[\frac{g (13 L^{2} g + 16 N)}{6}\\
&+\frac{5}{6} \Box_{\mathrm B}^{c}(\sigma)\Big]\\
&+\frac{64 \alpha}{3} \mathscr D_{a}(T_{bc})\Big[-\mathscr D^{a}(T^{bc})\\
&+\mathscr D^{b}(T^{ac})\Big]\\
&+\frac{\beta}{6} \mathscr D_{a}(G_{bc})\Big[-2 \mathscr D^{a}(G^{bc})\\
&+5 \mathscr D^{b}(G^{ac})\Big]\\
&+\mathscr D_{a}(L)\Big[-\big(\frac{\beta g^{2}}{2} - \frac{4 N^{2} \zeta}{L^{4}}\big) \mathscr D^{a}(L)\\
&-\frac{4 N \zeta}{L^{3}} \mathscr D^{a}(N)\Big]\\
&+\big(\frac{16 D^{2} (4 \alpha + 3 \zeta)}{3} - 8 D (L + N \zeta (g + \frac{3 N}{L^{2}})) + 2 L^{2} g^{2} - 4 N g + \frac{\beta g^{2} (5 L^{4} g^{2} + 16 L^{2} N g - 4 N^{2})}{24} - \frac{2 N^{2}}{L} + \frac{N^{3} \zeta (2 g + \frac{N}{L^{2}})}{L^{2}}\big)\\
&-\big(- \frac{8 D \zeta}{L} + \frac{L \beta g^{2}}{2} + 2 + \frac{2 N \zeta (g + \frac{2 N}{L^{2}})}{L}\big) \Box_{\mathrm B}^{c}(L)\\
&-\big(\beta g - \frac{2 N \zeta}{L^{2}}\big) \Box_{\mathrm B}^{c}(N)\\
&+\frac{4 N^{2} \zeta}{L^{2}} f_{a}{}^{a}\\
&+\frac{\zeta}{L^{2}} \Box_{\mathrm B}^{c}(L^{ij}) \Box_{\mathrm B}^{c}(L_{ij})\\
&+\frac{\beta}{6} \mathscr D^{a}(H_{abc}) \mathscr D^{d}(H^{bc}{}_{d})\\
&+\frac{\alpha}{8} C^{abcd} C_{abcd}\\
&-\frac{2 \alpha - \beta}{6} R^{abij}(V) R_{abij}(V)
\end{aligned}
```

This density contains all bosonic terms of the $`\ell_{2\partial}+\alpha\ell_{\mathrm{Weyl}^2} +\beta\ell_{\mathrm{LOG}}+\zeta\ell_{R^2}`$ combination; bosonic auxiliary fields remain in the action.
