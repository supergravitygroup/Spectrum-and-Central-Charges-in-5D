```math
\boxed{\begin{gathered}
S_{\le2}=S_{2\text{-der}}+\alpha S_{\mathrm{Weyl}^2}
+\beta S_{\mathrm{Log}}+\zeta S_{R^2}
=\frac{1}{2\kappa_5^2}\int_M d^5x\,e\,\big[\mathscr L^{[0]}_{\mathrm a}+\mathscr L^{[2]}_{\mathrm a}\big]_{\le2},\\
S_{\mathrm{full}}=S_{\le2}+S_{\mathrm{fermi}\ge4},\qquad
 e=\det e_\mu{}^a=\sqrt{-g}.
\end{gathered}}
```

$`\alpha,\beta,\zeta,g,\kappa_5`$ is symbolic; no coupling expansion is performed. The source normalizations are retained: $`-2`$ for the two-derivative density, $`\widehat C^2/8`$ for Weyl squared and $`R^2/4`$ for the $`R^2`$ density. The earlier LOG action coefficient is $`\beta`$ here, and the earlier $`\lambda_{R^2}`$ is $`\zeta`$ here; these coefficients multiply the densities only once.

The sources' shared gauge and local domain of definition:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad L>0,\qquad g\ne0,
\qquad V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad \delta_{ij}V_\mu^{\prime\,ij}=0.
```

$`L`$, $`N`$, $`E_3`$, $`V`$, $`V'`$ and the gravitino are retained. In the density below, $`[\ ]_{\le2}`$ also counts every implicit fermion; each supercovariant composite and ordered derivative is defined first, and the gauge is imposed afterward.

```math
\begin{gathered}
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad a,b,\mu=0,\ldots,4,
\qquad i,j,k,l,o,z=1,2,\\
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ij)}=\frac12(X_{ij}+X_{ji}),\\
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\cdots a_r}=\gamma^{[a_1}\cdots\gamma^{a_r]},\qquad
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\\
\gamma^{abc}=-\frac i2\varepsilon^{abcde}\gamma_{de},\qquad
\gamma^{abcd}=i\varepsilon^{abcde}\gamma_e,\\
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i,\\
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},\qquad
L_i{}^j=\epsilon^{jk}L_{ik},\qquad
L^i{}_j=\epsilon^{ik}L_{kj},\qquad L^{ij}L_{ij}=L^2,\\
\overline{cX}=c\bar X,\qquad
\overline{\gamma_{(r)}X}=t_r\bar X\gamma_{(r)},\qquad
(t_0,t_1,t_2,t_3,t_4,t_5)=(+,+,-,-,+,+),\\
\bar X^i\gamma_{(r)}Y_i=-t_r\bar Y^i\gamma_{(r)}X_i,\qquad
\gamma\!\cdot\!T=\gamma^{ab}T_{ab}.
\end{gathered}
```

No numerical epsilon-orientation component has been chosen. Contractions are full index sums; gamma blocks contain no hidden $`1/r!`$.

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

$`\varphi^i`$ is the independent linear-multiplet fermion, and $`\phi_\mu^i`$ is the dependent $`S`$ connection. $`\psi^i`$ is the defining dilatino, $`\psi_\mu^i`$ the gravitino; $`\mathcal D\psi`$, $`\Box^c\psi`$ and higher dilatino derivatives retain the supercovariant definitions below.

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

$`T,\chi,D`$ are the shared gauged composites. The working definition of their ordered derivatives agrees with [CONVENTIONS.md](source_conventions.md) and [relations GC17–GC24 of the Weyl input](../../weyl2/action/details/construction.md); derivative order is unchanged.

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

Dependent connection and curvatures:

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

```math
\begin{gathered}
\gamma^a\widehat R_{ab}^i(Q)=0,\qquad
\overline{\widehat R_{ab}^i(Q)}\gamma^a=0,\qquad
\eta^{ac}\widehat C_{abcd}=0,\\
L^{ij}\mathcal D_aL_{ij}=L\mathcal D_aL,\\
L^{ij}\mathcal D_a\mathcal D_bL_{ij}
=L\mathcal D_a\mathcal D_bL
+(\mathcal D_aL)(\mathcal D_bL)
-(\mathcal D_aL^{ij})(\mathcal D_bL_{ij}).
\end{gathered}
```

$`\mathrm a`$ labels explicit fermion order:

```math
\begin{gathered}
\nu_{\mathrm a}(\psi_\mu,\varphi,\chi,\phi_\mu,
\widehat R(Q),\mathcal D\psi)=1,\qquad
\nu_{\mathrm a}(\mathcal D^kX)=\nu_{\mathrm a}(X),\\
\nu_{\mathrm a}(e,C,G,H,E_3,E,N,L,L^{ij},\sigma,V,T,D,
\widehat G,\widehat H,\widehat C,\widehat R(V))=0,\\
\boxed{\mathscr L_{\le2}
=\big[\mathscr L^{[0]}_{\mathrm a}+\mathscr L^{[2]}_{\mathrm a}\big]_{\le2}}.
\end{gathered}
```

Each shared bracket has one explicit fermion order. Fermions implicit in hatted objects and supercovariant derivatives are counted in the $`[\ ]_{\le2}`$ projection of the sum. Gamma-trace constraints are algebraic consequences of the dependent-connection definitions. For $`\widehat C`$, within-pair antisymmetry and the trace constraint are used; ordinary Riemann pair-exchange or Bianchi identities are not added. Ordered covariant derivatives retain their written order. Couplings are exact; no field equation has been used.

```math
\begin{aligned}
\mathscr L^{[0]}_{\mathrm{a}}={}&C_{a}\Big[\beta \widehat H_{bcd}\Big[\frac{1}{248832} \widehat H_{efg}\Big[\varepsilon^{defg}{}_{h}\Big[27648 \mathcal D^{h}(\widehat H^{abc})\\
&+7632 \widehat C^{abch}\\
&+504 \widehat C^{ahbc}\\
&-6480 \widehat C^{bhac}\\
&-6408 \widehat G^{ab} \widehat G^{ch}\\
&+19823 \widehat G^{ah} \widehat G^{bc}\Big]\\
&+5 \varepsilon^{efg}{}_{hm}\Big[2725 \widehat H^{abc} \widehat H^{dhm}\\
&-2032 \widehat H^{abh} \widehat H^{cdm}\\
&-1247 \widehat H^{ahm} \widehat H^{bcd}\Big]\\
&+1152 \varepsilon^{bcdef}\Big[7 \mathcal D^{a}\mathcal D^{g}(\sigma)\\
&-37 \mathcal D^{g}\mathcal D^{a}(\sigma)\Big]\\
&-4752 \varepsilon^{ahefg} \widehat C^{b}{}_{h}{}^{cd}\\
&+23027 \varepsilon^{cdefg} \widehat G^{a}{}_{h} \widehat G^{hb}\Big]\\
&+\frac{1}{497664} \widehat G_{ef}\Big[\widehat H^{a}{}_{gh}\Big[-8770 \varepsilon^{efbcd} \widehat G^{gh}\\
&-92108 \varepsilon^{fhbcd} \widehat G^{eg}\\
&+23027 \varepsilon^{ghbcd} \widehat G^{ef}\Big]\\
&+4385 \widehat G_{gh}\Big[3 \varepsilon^{efghd} \widehat H^{abc}\\
&+4 \varepsilon^{fhbcd} \widehat H^{aeg}\Big]\\
&+2\Big[13824 \varepsilon^{bcdf}{}_{g}\Big[-\mathcal D^{a}(\widehat G^{eg})\\
&-4 \mathcal D^{e}(\widehat G^{ag})\Big]\\
&+6912 \varepsilon^{abcd}{}_{g}\Big[4 \mathcal D^{e}(\widehat G^{fg})\\
&-\mathcal D^{g}(\widehat G^{ef})\Big]\\
&-41472 \mathcal D^{g}(\widehat G^{a}{}_{g}) \varepsilon^{efbcd}\\
&-13824 \mathcal D^{g}(\widehat G^{e}{}_{g}) \varepsilon^{afbcd}\\
&+26677 \widehat H^{aef} \widehat H^{bcd}\Big]\Big]\\
&+\frac{1}{576} \widehat G^{a}{}_{e}\Big[32 \varepsilon^{bcd}{}_{fg}\Big[-5 \mathcal D^{e}(\widehat G^{fg})\\
&+3 \mathcal D^{f}(\widehat G^{eg})\Big]\\
&-192 \mathcal D^{b}(\widehat H^{ecd})\\
&+64 \mathcal D^{e}(\widehat H^{bcd})\\
&+53 \widehat C^{bced}\\
&-5 \widehat C^{ebcd}\\
&+160 \mathcal D^{f}(\widehat G_{fg}) \varepsilon^{egbcd}\Big]\\
&+\frac{1}{82944} \widehat H^{a}{}_{ef}\Big[192 \varepsilon^{bcd}{}_{gh}\Big[-18 \widehat C^{egfh}\\
&-11 \widehat C^{ghef}\Big]\\
&+11520 \Box^c(\sigma) \varepsilon^{efbcd}\\
&-26677 \widehat G^{bc} \widehat H^{efd}\\
&-53354 \widehat G^{eb} \widehat H^{fcd}\Big]\\
&+\frac{1}{18} \mathcal D_{e}(\widehat H_{fgh})\Big[-2 \varepsilon^{adfgh} \widehat H^{bce}\\
&+\varepsilon^{aefgh} \widehat H^{bcd}\\
&-2 \varepsilon^{defgh} \widehat H^{abc}\Big]\\
&+\frac{1}{576} \widehat G^{d}{}_{e}\Big[-165 \widehat C^{abec}\\
&+133 \widehat C^{aebc}\\
&-21 \widehat C^{bcae}\\
&-485 \widehat C^{ebac}\Big]\\
&+\frac{1}{20736} \widehat G^{b}{}_{e}\Big[27648 \mathcal D^{c}(\widehat H^{aed})\\
&-6912 \mathcal D^{e}(\widehat H^{acd})\\
&+26677 \widehat H^{ac}{}_{f} \widehat H^{efd}\Big]\\
&+\frac{1}{1152} \widehat C_{efgh}\Big[5 \varepsilon^{aefgh} \widehat H^{bcd}\\
&+6 \varepsilon^{efghd} \widehat H^{abc}\Big]\\
&+\frac{1}{576} \widehat H^{cd}{}_{e}\Big[-192 \mathcal D^{e}(\widehat G^{ab})\\
&+5 \varepsilon^{afghe} \widehat C^{b}{}_{fgh}\Big]\\
&+\frac{1}{6} \widehat H^{ad}{}_{e}\Big[-10 \mathcal D^{b}(\widehat G^{ec})\\
&+\mathcal D^{e}(\widehat G^{bc})\Big]\\
&+\frac{1}{6} \widehat G^{bc}\Big[\mathcal D^{a}\mathcal D^{d}(\sigma)\\
&+3 \mathcal D^{d}\mathcal D^{a}(\sigma)\Big]\\
&+\frac{1}{9} \widehat G^{ab}\Big[5 \mathcal D^{c}\mathcal D^{d}(\sigma)\\
&-3 \mathcal D^{e}(\widehat H^{cd}{}_{e})\Big]\\
&+\varepsilon^{abcd}{}_{e}\Big[\frac{2}{9} \Box^c\mathcal D^{e}(\sigma)\\
&+\frac{L g^{2}}{18} \mathcal D^{e}(L)\\
&+\frac{g}{9} \mathcal D^{e}(N)\\
&-\frac{1}{9} \mathcal D^{e}\Box^c(\sigma)\\
&-\frac{55}{864} \mathcal D^{f}\mathcal D^{g}(\widehat H_{fg}{}^{e})\Big]\\
&+\frac{1}{864}\Big[\varepsilon^{bcd}{}_{ef}\Big[25 \mathcal D^{e}\mathcal D^{g}(\widehat H^{a}{}_{g}{}^{f})\\
&+72 \mathcal D^{g}(\widehat C^{ae}{}_{g}{}^{f})\\
&+36 \mathcal D^{g}(\widehat C^{a}{}_{g}{}^{ef})\\
&-55 \mathcal D^{g}\mathcal D^{e}(\widehat H^{a}{}_{g}{}^{f})\Big]\\
&+\varepsilon^{cd}{}_{efg}\Big[8 \mathcal D^{a}\mathcal D^{b}(\widehat H^{efg})\\
&+25 \mathcal D^{b}\mathcal D^{a}(\widehat H^{efg})\Big]\\
&+3\Big[3 \varepsilon^{ad}{}_{efg}\Big[8 \mathcal D^{b}\mathcal D^{c}(\widehat H^{efg})\\
&-11 \mathcal D^{e}\mathcal D^{f}(\widehat H^{bcg})\Big]\\
&+16\Big[-4 \mathcal D^{a}\mathcal D^{b}(\widehat G^{cd})\\
&+10 \mathcal D^{b}\mathcal D^{a}(\widehat G^{cd})\\
&-2 \mathcal D^{b}\mathcal D^{c}(\widehat G^{ad})\\
&+\mathcal D^{e}(\widehat G^{a}{}_{e}) \widehat H^{bcd}\\
&+6 \mathcal D^{e}(\widehat G_{e}{}^{b}) \widehat H^{acd}\Big]\Big]\Big]\Big]\\
&+\frac{\beta}{82944} \widehat G_{bc}\Big[\widehat G_{de}\Big[\widehat G_{fg}\Big[-4408 \varepsilon^{acefg} \widehat G^{bd}\\
&+1102 \varepsilon^{adefg} \widehat G^{bc}\\
&-86015 \varepsilon^{cdefg} \widehat G^{ab}\Big]\\
&+72\Big[112 \varepsilon^{bcde}{}_{f}\Big[\mathcal D^{a}\mathcal D^{f}(\sigma)\\
&-4 \mathcal D^{f}\mathcal D^{a}(\sigma)\Big]\\
&+\varepsilon^{ade}{}_{fg}\Big[-\widehat C^{bcfg}\\
&-31 \widehat C^{bfcg}\Big]\\
&+2\Big[\varepsilon^{ace}{}_{fg}\Big[5 \widehat C^{bdfg}\\
&-41 \widehat C^{bfdg}\Big]\\
&+168 \Box^c(\sigma) \varepsilon^{abcde}\Big]\Big]\Big]\\
&+36\Big[\widehat G^{a}{}_{d}\Big[2 \varepsilon^{cd}{}_{efg}\Big[-320 \mathcal D^{b}(\widehat H^{efg})\\
&+9 \widehat C^{befg}\Big]\\
&+3\Big[\varepsilon^{bc}{}_{efg}\Big[-128 \mathcal D^{d}(\widehat H^{efg})\\
&+25 \widehat C^{defg}\Big]\\
&+896\Big[2 \mathcal D^{b}(\widehat G^{dc})\\
&-\mathcal D^{d}(\widehat G^{bc})\Big]\Big]\Big]\\
&+2 \widehat H^{a}{}_{de}\Big[384 \mathcal D^{b}(\widehat H^{cde})\\
&-19 \widehat C^{bcde}\\
&-16 \widehat C^{bdce}\\
&+59 \widehat C^{debc}\Big]\\
&+128 \mathcal D_{d}(\widehat H_{efg})\Big[-\varepsilon^{acefg} \widehat G^{bd}\\
&+\varepsilon^{adefg} \widehat G^{bc}\\
&+\varepsilon^{cdefg} \widehat G^{ab}\Big]\\
&+256 \widehat H^{ab}{}_{d}\Big[4 \mathcal D^{c}\mathcal D^{d}(\sigma)\\
&-7 \mathcal D^{d}\mathcal D^{c}(\sigma)\\
&+12 \mathcal D^{e}(\widehat H^{cd}{}_{e})\Big]\\
&+\widehat C_{defg}\Big[35 \varepsilon^{adefg} \widehat G^{bc}\\
&+12 \varepsilon^{defgc} \widehat G^{ab}\Big]\\
&+4\Big[2 \varepsilon^{bc}{}_{def}\Big[-5 \mathcal D^{a}\mathcal D^{d}(\widehat G^{ef})\\
&+23 \mathcal D^{d}\mathcal D^{a}(\widehat G^{ef})\\
&+24 \mathcal D^{d}\mathcal D^{e}(\widehat G^{af})\Big]\\
&+8 \varepsilon^{ac}{}_{def}\Big[-2 \mathcal D^{b}\mathcal D^{d}(\widehat G^{ef})\\
&+5 \mathcal D^{d}\mathcal D^{b}(\widehat G^{ef})\\
&-9 \mathcal D^{d}\mathcal D^{e}(\widehat G^{bf})\Big]\\
&+4 \varepsilon^{abc}{}_{de}\Big[-21 \Box^c(\widehat G^{de})\\
&-5 \mathcal D^{d}\mathcal D^{f}(\widehat G_{f}{}^{e})\\
&-25 \mathcal D^{f}\mathcal D^{d}(\widehat G_{f}{}^{e})\Big]\\
&-32 \mathcal D^{a}\mathcal D^{d}(\widehat H^{bc}{}_{d})\\
&+160 \mathcal D^{b}\mathcal D^{d}(\widehat H^{ac}{}_{d})\\
&-144 \mathcal D^{d}(\widehat C^{ab}{}_{d}{}^{c})\\
&-72 \mathcal D^{d}(\widehat C^{a}{}_{d}{}^{bc})\\
&+32 \mathcal D^{d}\mathcal D^{a}(\widehat H^{bc}{}_{d})\\
&-352 \mathcal D^{d}\mathcal D^{b}(\widehat H^{ac}{}_{d})\\
&-384 \Box^c(\sigma) \widehat H^{abc}\\
&+384 \mathcal D^{d}(\widehat G^{ac}) \widehat G^{b}{}_{d}\\
&-96 \mathcal D^{d}(\widehat G^{a}{}_{d}) \widehat G^{bc}\\
&-384 \mathcal D^{d}(\widehat G^{c}{}_{d}) \widehat G^{ab}\\
&-43 \varepsilon^{adefg} \widehat C^{b}{}_{def} \widehat G^{c}{}_{g}\Big]\Big]\Big]\\
&+\beta \mathcal D_{b}(\widehat H_{cde})\Big[\frac{1}{4608} \varepsilon^{cde}{}_{fg}\Big[191 \mathcal D^{a}(\widehat H^{bfg})\\
&-191 \mathcal D^{b}(\widehat H^{afg})\\
&-561 \mathcal D^{f}(\widehat H^{abg})\Big]\\
&+\frac{1}{1536} \varepsilon^{bcde}{}_{f}\Big[-64 \mathcal D^{a}\mathcal D^{f}(\sigma)\\
&+320 \mathcal D^{f}\mathcal D^{a}(\sigma)\\
&+241 \mathcal D^{g}(\widehat H^{a}{}_{g}{}^{f})\Big]\\
&+\frac{1}{4608} \varepsilon^{acde}{}_{f}\Big[1920 \mathcal D^{b}\mathcal D^{f}(\sigma)\\
&-384 \mathcal D^{f}\mathcal D^{b}(\sigma)\\
&-431 \mathcal D^{g}(\widehat H_{g}{}^{bf})\Big]\\
&+\varepsilon^{abcde}\Big[-\frac{g (L^{2} g + 4 N)}{36}\\
&-\frac{5}{18} \Box^c(\sigma)\Big]\\
&+\frac{431}{1536} \mathcal D^{f}(\widehat H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}\Big]\\
&+\frac{\beta}{1536} \mathcal D_{b}(\widehat G_{cd})\Big[\varepsilon^{bcd}{}_{ef}\Big[-415 \mathcal D^{a}(\widehat G^{ef})\\
&+113 \mathcal D^{e}(\widehat G^{af})\Big]\\
&+\varepsilon^{abd}{}_{ef}\Big[1105 \mathcal D^{c}(\widehat G^{ef})\\
&-2078 \mathcal D^{e}(\widehat G^{cf})\Big]\\
&+1728 \mathcal D^{a}(\widehat H^{bcd})\\
&-704 \mathcal D^{b}(\widehat H^{acd})\\
&+2432 \mathcal D^{c}(\widehat H^{abd})\\
&-353 \mathcal D^{b}(\widehat G_{ef}) \varepsilon^{aefcd}\\
&+525 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{afbcd}\Big]\\
&+\frac{4 \alpha}{9} T_{bc}\Big[64 T^{a}{}_{d}\Big[-6 \mathcal D^{b}(T^{dc})\\
&-\mathcal D^{d}(T^{bc})\Big]\\
&+24 \varepsilon^{ac}{}_{def}\Big[-2 \mathcal D^{d}\mathcal D^{b}(T^{ef})\\
&+3 \mathcal D^{d}\mathcal D^{e}(T^{bf})\Big]\\
&+9 \mathcal D^{d}(\widehat C^{a}{}_{d}{}^{bc})\\
&+384 T^{ab} \mathcal D^{d}(T^{c}{}_{d})\\
&-32 T^{bc} \mathcal D^{d}(T^{a}{}_{d})\\
&-384 T^{b}{}_{d} \mathcal D^{d}(T^{ac})\Big]\\
&+\frac{\beta}{864} \widehat H^{a}{}_{bc}\Big[2 \varepsilon^{c}{}_{defg}\Big[67 \mathcal D^{b}\mathcal D^{d}(\widehat H^{efg})\\
&+44 \mathcal D^{d}\mathcal D^{b}(\widehat H^{efg})\Big]\\
&+3\Big[96 \Box^c(\widehat G^{bc})\\
&-32 \mathcal D^{b}\mathcal D^{d}(\widehat G_{d}{}^{c})\\
&-160 \mathcal D^{d}\mathcal D^{b}(\widehat G_{d}{}^{c})\\
&-11 \Box^c(\widehat H_{efg}) \varepsilon^{bcefg}\Big]\Big]\\
&+\frac{\beta}{12} \mathcal D_{b}\mathcal D_{c}(\sigma)\Big[6 \mathcal D^{a}(\widehat G^{bc})\\
&+6 \mathcal D^{b}(\widehat G^{ac})\\
&+6 \mathcal D^{c}(\widehat G^{ab})\\
&+\mathcal D^{a}(\widehat H_{def}) \varepsilon^{defbc}\Big]\\
&+\beta \widehat G^{a}{}_{b}\Big[\frac{2}{3} \Box^c\mathcal D^{b}(\sigma)\\
&-\frac{4 L g^{2}}{3} \mathcal D^{b}(L)\\
&-\frac{5 g}{3} \mathcal D^{b}(N)\\
&-\frac{1}{3} \mathcal D^{b}\Box^c(\sigma)\\
&-\frac{1}{18} \mathcal D^{c}\mathcal D^{d}(\widehat H^{b}{}_{cd})\\
&+\frac{7}{144} \mathcal D^{c}\mathcal D^{d}(\widehat G_{ef}) \varepsilon^{b}{}_{cd}{}^{ef}\Big]\\
&+\frac{4 \alpha}{3} \mathcal D_{b}(T_{cd})\Big[8 \varepsilon^{abd}{}_{ef}\Big[2 \mathcal D^{c}(T^{ef})\\
&-3 \mathcal D^{e}(T^{cf})\Big]\\
&+3 \widehat C^{abcd}\Big]\\
&+\frac{\beta}{12} \mathcal D_{b}(\widehat G^{b}{}_{c})\Big[3 \mathcal D^{a}\mathcal D^{c}(\sigma)\\
&-15 \mathcal D^{c}\mathcal D^{a}(\sigma)\\
&+4 \mathcal D^{d}(\widehat H^{ac}{}_{d})\Big]\\
&+\frac{\beta}{12} \mathcal D_{b}(\widehat H_{cd}{}^{b})\Big[7 \mathcal D^{a}(\widehat G^{cd})\\
&-18 \mathcal D^{c}(\widehat G^{ad})\Big]\\
&+\beta \mathcal D_{b}(\widehat G^{ab})\Big[-\frac{g (2 L^{2} g + 5 N)}{3}\\
&-\frac{2}{3} \Box^c(\sigma)\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[\frac{\beta}{6} \Box^c\mathcal D^{b}(\widehat H^{cde})\\
&+\frac{\alpha}{16} \widehat C^{bc}{}_{fg} \widehat C^{defg}\\
&-\frac{\alpha + \beta}{12} \widehat R^{bc}{}_{ij}(V) \widehat R^{deij}(V)\Big]\\
&-\frac{64 D \alpha}{3} \mathcal D^{b}(T^{a}{}_{b})\\
&+\beta g L^{ij} \mathcal D^{b}(\widehat R^{a}{}_{bij}(V))\\
&-\frac{64 \alpha}{3} T^{a}{}_{b} \mathcal D^{b}(D)\\
&+\beta g \mathcal D^{b}(L^{ij}) \widehat R^{a}{}_{bij}(V)\Big]\\
&+\widehat G_{ab}\Big[\beta \widehat H_{cde}\Big[\frac{1}{12} \widehat G_{fg}\Big[-2 \varepsilon^{bgcde} \widehat G^{af}\\
&+\varepsilon^{fgcde} \widehat G^{ab}\Big]\\
&+\frac{1}{3456} \varepsilon^{cde}{}_{fg}\Big[225 \mathcal D^{f}(\widehat H^{abg})\\
&-136 \widehat C^{afbg}\\
&-92 \widehat C^{fgab}\Big]\\
&+\frac{7}{27} \varepsilon^{acde}{}_{f}\Big[-\mathcal D^{b}\mathcal D^{f}(\sigma)\\
&+\mathcal D^{f}\mathcal D^{b}(\sigma)\Big]\\
&+\varepsilon^{abcde}\Big[\frac{g (L^{2} g + 4 N)}{36}\\
&+\frac{1}{9} \Box^c(\sigma)\Big]\\
&+\frac{1}{6912}\Big[-278 \mathcal D^{f}(\widehat H^{a}{}_{fg}) \varepsilon^{bcdeg}\\
&-267 \mathcal D^{f}(\widehat H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}\\
&-192 \widehat G^{ab} \widehat H^{cde}\\
&+1152 \widehat G^{ac} \widehat H^{bde}\\
&-2304 \widehat G^{cd} \widehat H^{abe}\Big]\Big]\\
&+L^{ij}\Big[\frac{\zeta}{L^{3}} \mathcal D_{c}(L_{j}{}^{k}) \mathcal D_{d}(L_{ik}) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{2 L} E^{e}\\
&-\frac{\sqrt{2}}{4} V^{e}\Big]\\
&+\frac{\zeta}{L} \widehat R_{cdij}(V) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{2 L} E^{e}\\
&-\frac{\sqrt{2}}{4} V^{e}\Big]\\
&-\big(\frac{\beta g}{3} + \frac{N \zeta}{L^{2}}\big) \widehat R^{ab}{}_{ij}(V)\\
&+\frac{N \zeta}{L^{4}} \mathcal D^{a}(L_{ki}) \mathcal D^{b}(L^{k}{}_{j})\Big]\\
&+\frac{\beta}{144} \widehat G_{cd}\Big[-96 \mathcal D^{a}(\widehat H^{bcd})\\
&+17 \widehat C^{abcd}\\
&+22 \widehat C^{acbd}\\
&+12 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{abcdf}\\
&+9 \widehat G^{ab} \widehat G^{cd}\\
&-54 \widehat G^{ac} \widehat G^{bd}\Big]\\
&+\frac{\beta}{6912} \mathcal D_{c}(\widehat H_{def})\Big[456 \varepsilon^{bgdef} \widehat H^{ac}{}_{g}\\
&-1129 \varepsilon^{gcdef} \widehat H^{ab}{}_{g}\Big]\\
&+\frac{\zeta}{L} \mathcal D_{c}(E_{d}) \varepsilon^{abcd}{}_{e}\Big[-\frac{1}{L} E^{e}\\
&-\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\frac{\beta}{3} \widehat H^{b}{}_{cd}\Big[-2 \mathcal D^{a}(\widehat G^{cd})\\
&+\mathcal D^{c}(\widehat G^{ad})\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V^{b}\Big[-\frac{N}{L} \mathcal D^{a}(L)\\
&+\mathcal D^{a}(N)\Big]\\
&+\frac{\beta}{432} \varepsilon^{b}{}_{cdef}\Big[-27 \mathcal D^{a}(\widehat C^{cdef})\\
&+112 \mathcal D^{a}\mathcal D^{c}(\widehat H^{def})\\
&-27 \mathcal D^{c}(\widehat C^{adef})\\
&+8 \mathcal D^{c}\mathcal D^{a}(\widehat H^{def})\Big]\\
&+\varepsilon^{ab}{}_{cde}\Big[-\frac{3 \beta}{32} \mathcal D^{f}(\widehat C_{f}{}^{cde})\\
&-\frac{\sqrt{2} \zeta}{2 L^{2}} E^{c} V^{e} \mathcal D^{d}(L)\Big]\\
&+\frac{16 N^{2} \zeta}{L^{2}} T^{ab}\\
&+\frac{\beta}{3} \Box^c(\widehat G^{ab})\\
&-\frac{2 N \zeta}{L^{2}} \mathcal D^{a}(E^{b})\\
&+\frac{2 \beta}{9} \mathcal D^{a}\mathcal D^{c}(\widehat G^{b}{}_{c})\\
&+\frac{\beta}{9} \mathcal D^{c}\mathcal D^{a}(\widehat G^{b}{}_{c})\\
&+\frac{\beta g (3 L^{2} g + 4 N)}{8} \widehat G^{ab}\\
&-\frac{2 \zeta}{L^{2}} E^{a} \mathcal D^{b}(N)\\
&-\frac{\beta}{3} \mathcal D^{c}(\widehat G_{cd}) \widehat H^{abd}\\
&-\frac{4 \beta}{3} \mathcal D^{c}\mathcal D^{b}(\sigma) \widehat G^{a}{}_{c}\\
&+\frac{563 \beta}{6912} \mathcal D^{b}(\widehat H_{cde}) \varepsilon^{fgcde} \widehat H^{a}{}_{fg}\Big]\\
&+\frac{1}{L} E_{a}\Big[\frac{2}{L} \mathcal D_{b}(L)\Big[\frac{\zeta}{L} \mathcal D^{b}(L)\Big[\frac{2}{L} E^{a}\\
&+\sqrt{2} V^{a}\Big]\\
&+\frac{\zeta}{L} \mathcal D^{a}(L)\Big[-\frac{2}{L} E^{b}\\
&-\sqrt{2} V^{b}\Big]\\
&+\frac{\zeta}{L} L^{ij}\Big[\widehat R^{ab}{}_{ij}(V)\\
&-\frac{5}{L^{2}} \mathcal D^{a}(L_{ki}) \mathcal D^{b}(L^{k}{}_{j})\Big]\\
&-2 E^{ab}\\
&+\frac{\zeta}{L} \mathcal D^{a}(E^{b})\\
&-\frac{2 \zeta}{L} \mathcal D^{b}(E^{a})\Big]\\
&+E^{a}\Big[2 (- \frac{4 D \zeta}{L} + 1 + \frac{N \zeta (g + \frac{N}{L^{2}})}{L})\\
&-\frac{4 \zeta}{L^{2}} \Box^c(L)\\
&+\frac{\zeta}{L^{3}} E^{b} E_{b}\\
&-\frac{16 \zeta}{3 L} T^{bc} T_{bc}\\
&+\frac{\zeta}{L^{3}} \mathcal D^{b}(L^{ij}) \mathcal D_{b}(L_{ij})\Big]\\
&+\frac{\zeta}{L}\Big[2 L^{ij}\Big[\frac{1}{L^{2}} \mathcal D^{a}(L_{ik})\Big[3 \Box^c(L^{k}{}_{j})\\
&-\frac{1}{L^{2}} E_{b} L^{kl} \mathcal D^{b}(L_{jl})\Big]\\
&-\mathcal D^{b}(\widehat R^{a}{}_{bij}(V))\\
&-\frac{1}{L^{2}} \mathcal D^{b}\mathcal D^{a}(L^{k}{}_{j}) \mathcal D_{b}(L_{ki})\Big]\\
&+\mathcal D^{a}\mathcal D_{b}(L)\Big[\frac{2}{L} E^{b}\\
&+\sqrt{2} V^{b}\Big]\\
&+\mathcal D_{b}(L^{ij})\Big[-2 \widehat R^{ab}{}_{ij}(V)\\
&+\frac{1}{L^{2}} E^{b} \mathcal D^{a}(L_{ij})\Big]\\
&+2 \Box^c(E^{a})\\
&+32 N \mathcal D^{b}(T^{a}{}_{b})\\
&-2 N \mathcal D^{b}(\widehat G^{a}{}_{b})\\
&-2 \mathcal D^{b}\mathcal D^{a}(E_{b})\\
&+32 T^{a}{}_{b} \mathcal D^{b}(N)\\
&-\sqrt{2} V^{a} \Box^c(L)\\
&+\frac{2}{L} \mathcal D^{a}(L) \mathcal D^{b}(E_{b})\Big]\Big]\\
&+\beta \widehat H_{abc}\Big[\widehat H^{abc}\Big[\frac{g (L^{2} g - 2 N)}{12}\\
&+\frac{1}{9} \Box^c(\sigma)\\
&-\frac{1}{72} \widehat H^{def} \widehat H_{def}\Big]\\
&+\frac{1}{72} \widehat H^{c}{}_{de}\Big[11 \widehat C^{abde}\\
&+10 \widehat C^{adbe}\Big]\\
&+\varepsilon^{abc}{}_{de}\Big[-\frac{1}{9} \Box^c(\widehat G^{de})\\
&+\frac{2}{27} \mathcal D^{d}\mathcal D^{f}(\widehat G_{f}{}^{e})\\
&+\frac{1}{27} \mathcal D^{f}\mathcal D^{d}(\widehat G_{f}{}^{e})\\
&-\frac{g}{18} L^{ij} \widehat R^{de}{}_{ij}(V)\Big]\\
&+\frac{1}{36}\Big[4 \Box^c(\widehat H^{abc})\\
&+4 \mathcal D^{a}\mathcal D^{d}(\widehat H^{bc}{}_{d})\\
&+9 \mathcal D^{d}(\widehat C^{ab}{}_{d}{}^{c})\\
&-16 \mathcal D^{d}\mathcal D^{a}(\widehat H^{bc}{}_{d})\\
&+24 \mathcal D^{d}(\widehat H^{ebc}) \widehat H^{a}{}_{de}\\
&-12 \mathcal D^{d}\mathcal D^{c}(\sigma) \widehat H^{ab}{}_{d}\\
&-\mathcal D^{d}(\widehat G_{d}{}^{a}) \varepsilon^{bcefg} \widehat H_{efg}\Big]\Big]\\
&+\mathcal D_{a}(L_{ij})\Big[\mathcal D^{a}(L^{ij})\Big[-\big(\frac{4 D \zeta}{L^{2}} + \frac{\beta g^{2}}{4} - \frac{1 + \frac{N \zeta (g + \frac{N}{L^{2}})}{L}}{L}\big)\\
&+\frac{\zeta}{L^{3}} \Box^c(L)\\
&-\frac{8 \zeta}{3 L^{2}} T^{bc} T_{bc}\\
&-\frac{3 \zeta}{4 L^{4}} \mathcal D^{b}(L^{kl}) \mathcal D_{b}(L_{kl})\Big]\\
&+\frac{1}{L^{3}}\Big[L^{jk}\Big[\mathcal D_{b}(L^{i}{}_{k})\Big[2 E^{ab}\\
&-\frac{16 N \zeta}{L} T^{ab}\\
&+\frac{3 \sqrt{2} \zeta}{L} V^{b} \mathcal D^{a}(L)\Big]\\
&+\sqrt{2} \zeta\Big[V^{a} \Box^c(L^{i}{}_{k})\\
&-V_{b} \mathcal D^{a}\mathcal D^{b}(L^{i}{}_{k})\Big]\Big]\\
&+\zeta \mathcal D^{a}(L)\Big[-2 \Box^c(L^{ij})\\
&+\frac{1}{L} \mathcal D^{b}(L^{ij}) \mathcal D_{b}(L)\Big]\Big]\Big]\\
&+T_{ab}\Big[T_{cd}\Big[-\frac{16 \alpha}{3} \widehat C^{abcd}\\
&-\frac{64 (44 \alpha - 3 \zeta)}{27} T^{ab} T^{cd}\\
&+1024 \alpha T^{ac} T^{bd}\\
&+\frac{128 \alpha}{3} \mathcal D^{e}(T_{ef}) \varepsilon^{abcdf}\Big]\\
&+T^{ab}\Big[-\frac{16 (- 4 D (16 \alpha + 3 \zeta) + 3 L + 3 N \zeta (g + \frac{27 N}{L^{2}}))}{9}\\
&+\frac{16 \zeta}{3 L} \Box^c(L)\Big]\\
&+\frac{16 \sqrt{2} \zeta}{L} V^{b}\Big[\frac{N}{L} \mathcal D^{a}(L)\\
&-\mathcal D^{a}(N)\Big]\\
&+\frac{32 N \zeta}{L^{2}} \mathcal D^{a}(E^{b})\\
&+\frac{128 \alpha}{3} \mathcal D^{a}\mathcal D^{c}(T^{b}{}_{c})\\
&-8 (\frac{\alpha g}{3} - \frac{2 N \zeta}{L^{2}}) L^{ij} \widehat R^{ab}{}_{ij}(V)\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V_{a}\Big[\frac{1}{L} \mathcal D_{b}(L)\Big[\mathcal D^{a}(E^{b})\\
&-2 \mathcal D^{b}(E^{a})\\
&-L^{ij} \widehat R^{ba}{}_{ij}(V)\Big]\\
&+\Box^c(E^{a})\\
&-16 N \mathcal D^{b}(T_{b}{}^{a})\\
&+N \mathcal D^{b}(\widehat G_{b}{}^{a})\\
&-\mathcal D^{b}\mathcal D^{a}(E_{b})\\
&-L^{ij} \mathcal D^{b}(\widehat R^{a}{}_{bij}(V))\\
&+\frac{1}{L} \mathcal D^{a}(L) \mathcal D^{b}(E_{b})\\
&-\mathcal D^{b}(L^{ij}) \widehat R^{a}{}_{bij}(V)\Big]\\
&+\frac{\beta}{72} \mathcal D_{a}(\widehat H_{bcd})\Big[\varepsilon^{bcd}{}_{ef}\Big[-11 \mathcal D^{a}(\widehat G^{ef})\\
&+14 \mathcal D^{e}(\widehat G^{af})\Big]\\
&+4\Big[\mathcal D^{a}(\widehat H^{bcd})\\
&-9 \mathcal D^{b}(\widehat H^{acd})\\
&+3 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{fabcd}\Big]\Big]\\
&+\frac{3 \beta}{4} \mathcal D_{a}\mathcal D_{b}(\sigma)\Big[-2 \mathcal D^{a}\mathcal D^{b}(\sigma)\\
&+2 \mathcal D^{c}(\widehat H_{c}{}^{ab})\\
&-\mathcal D^{c}(\widehat G_{de}) \varepsilon_{c}{}^{deab}\Big]\\
&+2 E_{ab}\Big[-g G^{ab}\\
&-\frac{2}{L} \mathcal D^{a}(E^{b})\\
&-\frac{1}{L} L^{ij} \widehat R^{ab}{}_{ij}(V)\Big]\\
&+\beta \Box^c(\sigma)\Big[\frac{g (13 L^{2} g + 16 N)}{6}\\
&+\frac{5}{6} \Box^c(\sigma)\Big]\\
&+\frac{64 \alpha}{3} \mathcal D_{a}(T_{bc})\Big[-\mathcal D^{a}(T^{bc})\\
&+\mathcal D^{b}(T^{ac})\Big]\\
&+\frac{\beta}{6} \mathcal D_{a}(\widehat G_{bc})\Big[-2 \mathcal D^{a}(\widehat G^{bc})\\
&+5 \mathcal D^{b}(\widehat G^{ac})\Big]\\
&+\mathcal D_{a}(L)\Big[-\big(\frac{\beta g^{2}}{2} - \frac{4 N^{2} \zeta}{L^{4}}\big) \mathcal D^{a}(L)\\
&-\frac{4 N \zeta}{L^{3}} \mathcal D^{a}(N)\Big]\\
&+\big(\frac{16 D^{2} (4 \alpha + 3 \zeta)}{3} - 8 D (L + N \zeta (g + \frac{3 N}{L^{2}})) + 2 L^{2} g^{2} - 4 N g + \frac{\beta g^{2} (5 L^{4} g^{2} + 16 L^{2} N g - 4 N^{2})}{24} - \frac{2 N^{2}}{L} + \frac{N^{3} \zeta (2 g + \frac{N}{L^{2}})}{L^{2}}\big)\\
&-\big(- \frac{8 D \zeta}{L} + \frac{L \beta g^{2}}{2} + 2 + \frac{2 N \zeta (g + \frac{2 N}{L^{2}})}{L}\big) \Box^c(L)\\
&-\big(\beta g - \frac{2 N \zeta}{L^{2}}\big) \Box^c(N)\\
&+\frac{4 N^{2} \zeta}{L^{2}} f_{a}{}^{a}\\
&+\frac{\zeta}{L^{2}} \Box^c(L^{ij}) \Box^c(L_{ij})\\
&+\frac{\beta}{6} \mathcal D^{a}(\widehat H_{abc}) \mathcal D^{d}(\widehat H^{bc}{}_{d})\\
&+\frac{\alpha}{8} \widehat C^{abcd} \widehat C_{abcd}\\
&-\frac{2 \alpha - \beta}{6} \widehat R^{abij}(V) \widehat R_{abij}(V)
\end{aligned}
```

```math
\begin{aligned}
\mathscr L^{[2]}_{\mathrm{a}}={}&-32 i (\frac{4 \alpha g}{3} - \zeta (g + \frac{16 N}{L^{2}})) L_{ij}\bar\chi^{i}\chi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+16 \zeta\bar\chi^{i}\gamma^{ab}\chi_{i}\Bigg[8 i T_{ab}\\
&-i \widehat G_{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{128 i \alpha}{3} C_{a}\bar\chi^{i}\gamma^{ab}\mathcal D_{b}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L} L_{ij}\bar\chi^{i}\gamma^{ab}\phi_{b}{}^{j}\Bigg[-\frac{2 i}{L} E_{a}\\
&-\sqrt{2} i V_{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{128 \zeta}{L^{2}} L_{j}{}^{k} \mathcal D_{a}(L_{ik})\bar\chi^{i}\gamma^{a}\chi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-64 (\frac{4 \alpha}{3} + \zeta)\bar\chi^{i}\gamma^{a}\mathcal D_{a}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{24 N \zeta}{L^{2}} L_{ij}\bar\chi^{i}\gamma^{a}\phi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 \alpha}{3}\bar\chi^{i}\gamma^{a}\widehat R_{bci}(Q)\Bigg[3 C^{b} T_{a}{}^{c}\\
&-C_{a} T^{bc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-8 i \alpha C^{b}\bar\chi^{i}\mathcal D^{a}(\widehat R_{bai}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{160 i \alpha}{3} T^{ab}\bar\chi^{i}\widehat R_{abi}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\chi^{j}\Bigg[\frac{4 \zeta}{L} L_{ij}\Big[6 T^{a}{}_{b}\Big[-\frac{2 i}{L} E^{b}\\
&-\sqrt{2} i V^{b}\Big]\\
&+\widehat G^{a}{}_{b}\Big[\frac{2 i}{L} E^{b}\\
&+\sqrt{2} i V^{b}\Big]\\
&-\frac{2 i N}{L^{2}} \mathcal D^{a}(L)\Big]\\
&+\frac{8 i N \zeta}{L^{2}} \mathcal D^{a}(L_{ij})\\
&-\frac{8 i \alpha}{3} C_{b} \widehat R^{ba}{}_{ij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{32 \alpha}{3}\bar\psi_{a}{}^{i}\chi_{i}\Bigg[-i \mathcal D^{b}(T_{b}{}^{a})\\
&+i C_{b} \mathcal D^{c}(T_{de}) \varepsilon^{b}{}_{c}{}^{dea}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ab}\chi^{j}\Bigg[\frac{8 i N \zeta}{L^{2}} \mathcal D_{b}(L_{ij})\\
&-\frac{8 i \alpha}{3} C_{c} \widehat R^{c}{}_{bij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}} \mathcal D_{b}(L_{ik}) L_{j}{}^{k}\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D^{c}(\varphi^{j})\Bigg[\frac{i}{L} E_{c}\\
&+\frac{\sqrt{2} i}{2} V_{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D^{c}\mathcal D_{b}(\varphi_{i})\Bigg[\frac{i}{L} E_{c}\\
&+\frac{\sqrt{2} i}{2} V_{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i N \zeta}{L^{2}} L_{ij}\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D_{b}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D_{b}(\varphi^{j})\Bigg[L_{ij}\Big[\frac{\zeta}{L^{3}} E_{c}\Big[-\frac{2 i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Big]\\
&-i (- \frac{4 D \zeta}{L^{2}} + \beta g^{2} + \frac{2 (1 + \frac{N^{2} \zeta}{L^{3}})}{L})\\
&+\frac{8 i \zeta}{3 L^{2}} T^{cd} T_{cd}\\
&+\frac{i \zeta}{2 L^{4}} \mathcal D^{c}(L^{kl}) \mathcal D_{c}(L_{kl})\Big]\\
&+\frac{\zeta}{L^{2}}\Big[\frac{1}{L} \mathcal D_{c}(L_{ik}) L_{j}{}^{k}\Big[-\frac{2 i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Big]\\
&+i \Box^c(L_{ij})\\
&-\frac{i}{L} \mathcal D^{c}(L_{ij}) \mathcal D_{c}(L)\\
&-\frac{i}{L^{2}} E_{c} L_{i}{}^{k} \mathcal D^{c}(L_{jk})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{2}} \mathcal D_{c}(L)\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D_{b}(\varphi_{i})\Bigg[-\frac{i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D_{b}(\widehat R_{cdi}(Q))\Bigg[4 i \alpha T^{cd}\\
&-\frac{5 i \beta}{32} \widehat G^{cd}\\
&-\frac{i \beta}{16} C_{e} \widehat H^{ecd}\\
&+\frac{5 i \beta}{96} \varepsilon^{efgcd} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{ab}\mathcal D_{b}\mathcal D^{c}(\varphi_{i})\Bigg[-\frac{i}{L} E_{c}\\
&-\frac{\sqrt{2} i}{2} V_{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i N^{2} \zeta}{L^{2}}\bar\psi_{a}{}^{i}\gamma^{ab}\phi_{bi}
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ab}\psi_{b}{}^{j}\Bigg[L_{ij}\Big[-i (- \frac{2 D N \zeta}{L^{2}} + \frac{\beta g^{2} (L^{2} g + 3 N)}{4} + g + \frac{N}{L} + \frac{N^{3} \zeta}{2 L^{4}})\\
&-\frac{i \beta g}{4} \Box^c(\sigma)\\
&-\frac{i N \zeta}{2 L^{4}} E^{c} E_{c}\\
&+\frac{4 i N \zeta}{3 L^{2}} T^{cd} T_{cd}\\
&+\frac{i N \zeta}{4 L^{4}} \mathcal D^{c}(L^{kl}) \mathcal D_{c}(L_{kl})\\
&-\frac{i \beta g}{8} \widehat G^{cd} \widehat G_{cd}\\
&-\frac{i \beta g}{8} \widehat H^{cde} \widehat H_{cde}\Big]\\
&+\widehat R_{cdij}(V)\Big[\frac{4 i \alpha}{3} T^{cd}\\
&-\frac{i \beta}{12} \widehat G^{cd}\\
&+\frac{i \beta}{36} \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&-\frac{i (\beta g - \frac{2 N \zeta}{L^{2}})}{4} \Box^c(L_{ij})\\
&-\frac{i N \zeta}{2 L^{3}} \mathcal D^{c}(L_{ij}) \mathcal D_{c}(L)\\
&-\frac{i N \zeta}{L^{4}} E_{c} L_{j}{}^{k} \mathcal D^{c}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ab}\varphi^{j}\Bigg[\frac{1}{L^{3}} L_{j}{}^{k}\Big[\mathcal D_{b}(L_{kl})\Big[L_{i}{}^{l}\Big[-i (\frac{4 D \zeta}{L} - 2 - \frac{N^{2} \zeta}{L^{3}})\\
&+\frac{i \zeta}{L^{3}} E^{c} E_{c}\\
&-\frac{8 i \zeta}{3 L} T^{cd} T_{cd}\\
&-\frac{i \zeta}{2 L^{3}} \mathcal D^{c}(L^{oz}) \mathcal D_{c}(L_{oz})\Big]\\
&+\frac{\zeta}{L}\Big[-i \Box^c(L_{i}{}^{l})\\
&+\frac{i}{L^{2}} E_{c} L^{ol} \mathcal D^{c}(L_{io})\Big]\Big]\\
&+\zeta\Big[\frac{1}{L} E_{c}\Big[i \mathcal D^{c}\mathcal D_{b}(L_{ik})\\
&-i \mathcal D_{b}\mathcal D^{c}(L_{ik})\\
&-\frac{3 i}{L} \mathcal D^{c}(L) \mathcal D_{b}(L_{ik})\\
&-\frac{i}{L^{2}} L_{i}{}^{l} \mathcal D^{c}(L_{ol}) \mathcal D_{b}(L^{o}{}_{k})\Big]\\
&+\sqrt{2} V_{c}\Big[\frac{i}{2} \mathcal D^{c}\mathcal D_{b}(L_{ik})\\
&-\frac{i}{2} \mathcal D_{b}\mathcal D^{c}(L_{ik})\\
&-\frac{3 i}{2 L} \mathcal D^{c}(L) \mathcal D_{b}(L_{ik})\Big]\\
&-\frac{i}{L^{2}} \mathcal D^{c}(L_{il}) \mathcal D_{b}(L^{l}{}_{k}) \mathcal D_{c}(L)\Big]\Big]\\
&+\mathcal D_{b}(L_{ij})\Big[\frac{\zeta}{L^{3}} E_{c}\Big[-\frac{i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Big]\\
&-i (\frac{\beta g^{2}}{2} + \frac{N^{2} \zeta}{L^{4}})\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D_{c}(L_{jk}) \mathcal D_{b}(L_{i}{}^{k})\Big[-\frac{i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D_{c}(L_{ik}) \mathcal D_{b}(L_{j}{}^{k})\Big[-\frac{i}{L} E^{c}\\
&-\frac{\sqrt{2} i}{2} V^{c}\Big]\\
&-\frac{i \beta g}{3} C_{c} \widehat R^{c}{}_{bij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\big(\frac{\beta g}{2} - \frac{N \zeta}{L^{2}}\big)\bar\psi_{a}{}^{i}\gamma^{a}\Box^c(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{a}\chi^{j}\Bigg[\frac{1}{L} \mathcal D_{b}(L)\Big[L_{ij}\Big[\frac{2}{L} E^{b}\\
&+\sqrt{2} V^{b}\Big]\\
&+\frac{2}{L} L_{j}{}^{k} \mathcal D^{b}(L_{ik})\Big]\\
&+\mathcal D_{b}(L_{ij})\Big[-\frac{3}{L} E^{b}\\
&-\sqrt{2} V^{b}\Big]\\
&+\frac{2}{L} L_{j}{}^{k}\Big[-\Box^c(L_{ik})\\
&+\frac{1}{L^{2}} E_{b} L_{i}{}^{l} \mathcal D^{b}(L_{lk})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\chi_{i}\Bigg[8 (\frac{2 D (4 \alpha + 3 \zeta)}{3} - L - \frac{3 N^{2} \zeta}{L^{2}})\\
&-\frac{32 \alpha}{3} C_{b} \mathcal D^{c}(T^{b}{}_{c})\\
&-\frac{4 \zeta}{L^{2}} E^{b} E_{b}\\
&+\frac{32 (16 \alpha + 3 \zeta)}{9} T^{bc} T_{bc}\\
&+\frac{2 \zeta}{L^{2}} \mathcal D^{b}(L^{jk}) \mathcal D_{b}(L_{jk})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L} L_{ij}\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\chi^{j})\Bigg[-\frac{2}{L} E_{b}\\
&-\sqrt{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{64 \alpha}{3} C_{c} T^{c}{}_{b}\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+L_{ij}\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\varphi^{j})\Bigg[\beta g^{2} C_{b}\\
&+\frac{2 N \zeta}{L^{4}} E_{b}\\
&+\frac{\sqrt{2} N \zeta}{2 L^{3}} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\varphi_{i})\Bigg[\frac{\beta g}{18} C_{c}\Big[-6 \widehat G^{c}{}_{b}\\
&+\varepsilon^{cdef}{}_{b} \widehat H_{def}\Big]\\
&+\frac{\zeta}{L}\Big[3 T_{bc}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&-\frac{N}{L^{2}} \mathcal D_{b}(L)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+C_{d}\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\widehat R_{cbi}(Q))\Bigg[-4 \alpha T^{dc}\\
&+\frac{\beta}{16} \widehat G^{dc}\\
&+\frac{\beta}{48} \varepsilon^{defgc} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D^{b}(\widehat R_{cdi}(Q))\Bigg[C_{b}\Big[-4 \alpha T^{cd}\\
&+\frac{5 \beta}{32} \widehat G^{cd}\\
&-\frac{5 \beta}{96} \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\frac{\beta}{64}\Big[-4 \widehat H_{b}{}^{cd}\\
&-\varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L^{4}} L_{j}{}^{k} \mathcal D^{b}(L_{ik})\bar\psi_{a}{}^{i}\gamma^{a}\mathcal D_{b}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{a}\phi_{bi}\Bigg[\frac{1}{L} E^{b}\\
&+\frac{\sqrt{2}}{2} V^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\varphi^{j}\Bigg[\frac{\zeta}{L^{3}} L_{ij}\Big[\sqrt{2} V_{b}\Big[-\frac{3 N}{2 L} \mathcal D^{b}(L)\\
&+\frac{1}{2} \mathcal D^{b}(N)\\
&-E_{c} T^{cb}\Big]\\
&+\frac{1}{L}\Big[E_{b}\Big[-\frac{6 N}{L} \mathcal D^{b}(L)\\
&+\mathcal D^{b}(N)\Big]\\
&+N \mathcal D^{b}(E_{b})\Big]\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D_{b}(L_{ik})\Big[L_{j}{}^{k}\Big[T^{b}{}_{c}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&-\frac{4 N}{L^{2}} \mathcal D^{b}(L)\Big]\\
&+\frac{N}{L} \mathcal D^{b}(L_{j}{}^{k})\Big]\\
&+\mathcal D_{b}(L_{ij})\Big[\frac{\beta g^{2}}{2} C^{b}\\
&+\frac{5 N \zeta}{2 L^{4}} E^{b}\\
&+\frac{\sqrt{2} N \zeta}{2 L^{3}} V^{b}\Big]\\
&+\frac{N \zeta}{L^{4}} L_{j}{}^{k}\Big[2 \Box^c(L_{ik})\\
&-\frac{1}{L^{2}} E_{b} L_{i}{}^{l} \mathcal D^{b}(L_{lk})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\varphi_{i}\Bigg[\frac{\beta g}{288} C_{b}\Big[3 \widehat H^{b}{}_{cd}\Big[-24 \widehat G^{cd}\\
&+\varepsilon^{cdefg} \widehat H_{efg}\Big]\\
&+\varepsilon^{b}{}_{cdef}\Big[-44 \mathcal D^{c}(\widehat H^{def})\\
&+27 \widehat G^{cd} \widehat G^{ef}\Big]\\
&-120 \mathcal D^{c}(\widehat G^{b}{}_{c})\Big]\\
&+\frac{\zeta}{L^{2}} T_{bc}\Big[-\frac{64 N}{3} T^{bc}\\
&+4 N \widehat G^{bc}\\
&-\frac{4}{L} E^{b} \mathcal D^{c}(L)\\
&+2 \sqrt{2} V^{c} \mathcal D^{b}(L)\Big]\\
&+\frac{\beta g}{144} \widehat H_{bcd}\Big[-15 \widehat H^{bcd}\\
&+4 \varepsilon^{efbcd} \widehat G_{ef}\Big]\\
&+\frac{\zeta}{L^{2}} E_{b}\Big[\frac{N}{2 L^{2}} E^{b}\\
&+4 \mathcal D^{c}(T^{b}{}_{c})\Big]\\
&-\big(\frac{2 D N \zeta}{L^{2}} + \frac{\beta g^{2} (7 L^{2} g + 4 N)}{48} + 2 g + \frac{N}{L} - \frac{N^{3} \zeta}{2 L^{4}}\big)\\
&+\frac{5 \beta g}{12} \Box^c(\sigma)\\
&-\frac{2 \sqrt{2} \zeta}{L} V^{c} \mathcal D^{b}(T_{bc})\\
&-\frac{N \zeta}{4 L^{4}} \mathcal D^{b}(L^{jk}) \mathcal D_{b}(L_{jk})\\
&-\frac{\beta g}{8} \widehat G^{bc} \widehat G_{bc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\widehat R_{bci}(Q)\Bigg[C_{d}\Big[-2 \alpha \mathcal D^{b}(T^{dc})\\
&-\frac{\beta}{16} \widehat G^{d}{}_{e} \widehat H^{ebc}\\
&+\frac{\beta}{16} \widehat G_{e}{}^{b} \widehat H^{dec}\Big]\\
&+\frac{\beta}{48}\Big[-3 C^{b} \widehat G_{de} \widehat H^{dec}\\
&+2 \varepsilon^{defgc} \widehat G_{d}{}^{b} \widehat H_{efg}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{a}\widehat R_{bc}{}^{j}(Q)\Bigg[\frac{\beta g}{3456} L_{ij}\Big[3 C_{d}\Big[-22 \widehat H^{dbc}\\
&+23 \varepsilon^{defbc} \widehat G_{ef}\Big]\\
&+6 \widehat G^{bc}\\
&-59 \varepsilon^{defbc} \widehat H_{def}\Big]\\
&+\frac{\alpha}{4} \widehat R^{bc}{}_{ij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\Box^c(\varphi_{i})\Bigg[\frac{i \beta g}{2} C_{b}\\
&-\frac{i \zeta}{L^{2}} E_{b}\\
&-\frac{\sqrt{2} i \zeta}{2 L} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 \zeta}{L} L_{ij}\bar\psi_{a}{}^{i}\gamma^{ba}\chi^{j}\Bigg[T_{bc}\Big[\frac{2 i}{L} E^{c}\\
&+\sqrt{2} i V^{c}\Big]\\
&+\frac{i N}{L^{2}} \mathcal D_{b}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\chi_{i}\Bigg[\alpha C_{b}\Big[-\frac{64 i D}{3}\\
&-\frac{512 i}{9} T^{cd} T_{cd}\Big]\\
&+\frac{16 i N \zeta}{L^{2}} E_{b}\\
&+\frac{8 \sqrt{2} i N \zeta}{L} V_{b}\\
&+\frac{32 i \alpha}{3} \mathcal D^{c}(T_{cb})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{64 i \alpha}{3} T_{bc}\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D^{c}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}} L_{ij}\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D^{c}(\varphi^{j})\Bigg[E_{c}\Big[-\frac{2 i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&-\frac{\sqrt{2} i}{2} E_{b} V_{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D^{c}(\varphi_{i})\Bigg[\frac{\zeta}{L^{2}} \mathcal D_{c}(L)\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\frac{\zeta}{L^{2}} \mathcal D_{b}(L)\Big[-\frac{i}{L} E_{c}\\
&-\frac{\sqrt{2} i}{2} V_{c}\Big]\\
&+\frac{14 i N \zeta}{L^{2}} T_{bc}\\
&-i (\frac{\beta g}{3} + \frac{2 N \zeta}{L^{2}}) \widehat G_{bc}\\
&-\frac{i \beta g}{2} C_{d} \widehat H^{d}{}_{bc}\\
&-\frac{i \beta g}{18} \varepsilon^{def}{}_{bc} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D^{c}(\widehat R_{dci}(Q))\Bigg[\frac{\beta}{32} C_{e}\Big[4 i \widehat H^{e}{}_{b}{}^{d}\\
&-i \varepsilon^{efg}{}_{b}{}^{d} \widehat G_{fg}\Big]\\
&-4 i \alpha T_{b}{}^{d}\\
&+\frac{i \beta}{16} \widehat G_{b}{}^{d}\\
&-\frac{i \beta}{48} \varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{64}\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D^{c}(\widehat R_{dei}(Q))\Bigg[2 C_{f}\Big[2 i \varepsilon^{fg}{}_{bc}{}^{e} \widehat G_{g}{}^{d}\\
&+i \varepsilon^{fg}{}_{b}{}^{de} \widehat G_{gc}\Big]\\
&+C_{b}\Big[4 i \widehat H_{c}{}^{de}\\
&+i \varepsilon^{fg}{}_{c}{}^{de} \widehat G_{fg}\Big]\\
&+4\Big[-2 i C^{d} \widehat H_{bc}{}^{e}\\
&-i C_{c} \widehat H_{b}{}^{de}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}} \mathcal D^{c}(L_{ik}) L_{j}{}^{k}\bar\psi_{a}{}^{i}\gamma^{ba}\mathcal D_{c}(\varphi^{j})\Bigg[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\varphi^{j}\Bigg[L_{ij}\Big[\frac{\zeta}{L^{4}} E_{c}\Big[\mathcal D^{c}(L)\Big[\frac{6 i}{L} E_{b}\\
&+\frac{3 \sqrt{2} i}{2} V_{b}\Big]\\
&+\mathcal D_{b}(L)\Big[-\frac{3 i}{L} E^{c}\\
&-\frac{3 \sqrt{2} i}{2} V^{c}\Big]\\
&-8 i N T^{c}{}_{b}\\
&-i \mathcal D^{c}(E_{b})\\
&+i \mathcal D_{b}(E^{c})\\
&+2 i N \widehat G^{c}{}_{b}\Big]\\
&+\frac{\sqrt{2} \zeta}{L^{3}} V_{c}\Big[i N T^{c}{}_{b}\\
&-\frac{i}{2} \mathcal D^{c}(E_{b})\\
&+\frac{i}{2} \mathcal D_{b}(E^{c})\\
&+\frac{3 i}{2 L} E_{b} \mathcal D^{c}(L)\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D_{c}(E^{c})\Big[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&-\frac{3 i N^{2} \zeta}{L^{5}} \mathcal D_{b}(L)\\
&+\frac{i N \zeta}{L^{4}} \mathcal D_{b}(N)\\
&+\frac{i \beta g^{2}}{4} C_{c} \widehat G^{c}{}_{b}\Big]\\
&+\frac{\zeta}{L^{3}}\Big[\mathcal D_{c}(L_{ik})\Big[\frac{1}{L} L_{j}{}^{k}\Big[\mathcal D^{c}(L)\Big[\frac{4 i}{L} E_{b}\\
&+\frac{3 \sqrt{2} i}{2} V_{b}\Big]\\
&+\mathcal D_{b}(L)\Big[-\frac{3 i}{L} E^{c}\\
&-\frac{3 \sqrt{2} i}{2} V^{c}\Big]\\
&+2 N\Big[5 i T_{b}{}^{c}\\
&-i \widehat G_{b}{}^{c}\Big]\Big]\\
&+\mathcal D^{c}(L_{j}{}^{k})\Big[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\Big]\\
&+\mathcal D_{c}(L_{ij})\Big[E^{c}\Big[-\frac{5 i}{2 L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&-\frac{\sqrt{2} i}{2} E_{b} V^{c}\Big]\\
&+L_{j}{}^{k}\Big[\Box^c(L_{ik})\Big[-\frac{2 i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\frac{i}{L^{3}} E_{b} E_{c} L_{i}{}^{l} \mathcal D^{c}(L_{lk})\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\varphi_{i}\Bigg[\beta g C_{b}\Big[\frac{1}{144} \widehat H_{cde}\Big[15 i \widehat H^{cde}\\
&-4 i \varepsilon^{fgcde} \widehat G_{fg}\Big]\\
&+\frac{i g (7 L^{2} g + 4 N)}{48}\\
&-\frac{5 i}{12} \Box^c(\sigma)\\
&+\frac{i}{8} \widehat G^{cd} \widehat G_{cd}\Big]\\
&+\frac{\zeta}{L} T_{cd}\Big[T^{cd}\Big[\frac{40 i}{3 L} E_{b}\\
&+6 \sqrt{2} i V_{b}\Big]\\
&+\widehat G^{cd}\Big[-\frac{2 i}{L} E_{b}\\
&-\sqrt{2} i V_{b}\Big]\\
&+2\Big[\sqrt{2} V^{d}\Big[-4 i T^{c}{}_{b}\\
&+i \widehat G^{c}{}_{b}\Big]\\
&+\frac{2}{L} E^{c}\Big[4 i T^{d}{}_{b}\\
&-i \widehat G^{d}{}_{b}\Big]\Big]\Big]\\
&+\frac{\beta g}{24} C_{c}\Big[-12 i \mathcal D^{c}\mathcal D_{b}(\sigma)\\
&+14 i \mathcal D^{d}(\widehat H^{c}{}_{db})\\
&+12 i \mathcal D_{b}\mathcal D^{c}(\sigma)\\
&-13 i \mathcal D^{d}(\widehat G_{ef}) \varepsilon^{c}{}_{d}{}^{ef}{}_{b}\Big]\\
&+\frac{1}{L} E_{b}\Big[i (\frac{2 D \zeta}{L} - 1 - \frac{N^{2} \zeta}{2 L^{3}})\\
&-\frac{i \zeta}{2 L^{3}} E^{c} E_{c}\\
&+\frac{i \zeta}{4 L^{3}} \mathcal D^{c}(L^{jk}) \mathcal D_{c}(L_{jk})\Big]\\
&+\frac{\beta g}{96} \widehat H_{bcd}\Big[-24 i \widehat G^{cd}\\
&+i \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\frac{\beta g}{288} \varepsilon_{bcdef}\Big[-44 i \mathcal D^{c}(\widehat H^{def})\\
&+27 i \widehat G^{cd} \widehat G^{ef}\Big]\\
&-\frac{4 i N \zeta}{L^{2}} \mathcal D^{c}(T_{cb})\\
&+\frac{5 i \beta g}{12} \mathcal D^{c}(\widehat G_{cb})\\
&+\frac{4 i N \zeta}{L^{3}} T_{cb} \mathcal D^{c}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\widehat R_{cdi}(Q)\Bigg[C_{e}\Big[\frac{\beta}{864} \widehat H_{fgh}\Big[-3 i \varepsilon^{efghd} \widehat G_{b}{}^{c}\\
&-2 i \varepsilon^{efgh}{}_{b} \widehat G^{cd}\\
&-7 i \varepsilon^{fghcd} \widehat G^{e}{}_{b}\\
&-3 i \varepsilon^{fgh}{}_{b}{}^{d} \widehat G^{ec}\Big]\\
&+\frac{i \alpha}{8} \widehat C^{cde}{}_{b}\\
&-\frac{8 i \alpha}{3} T^{cd} T^{e}{}_{b}\\
&-\frac{i \beta}{144} \widehat G^{cd} \widehat G^{e}{}_{b}\\
&+\frac{i \beta}{24} \widehat G^{ec} \widehat G_{b}{}^{d}\\
&+\frac{7 i \beta}{72} \widehat H^{e}{}_{fb} \widehat H^{fcd}\\
&-\frac{i \beta}{12} \widehat H^{e}{}_{f}{}^{c} \widehat H^{f}{}_{b}{}^{d}\Big]\\
&+\frac{\beta}{48} \widehat G^{c}{}_{e}\Big[3 i \widehat H^{e}{}_{b}{}^{d}\\
&+2 i C_{b} \varepsilon^{efghd} \widehat H_{fgh}\Big]\\
&-2 i \alpha \mathcal D^{c}(T_{b}{}^{d})\\
&+\frac{i \beta}{16} \widehat G_{eb} \widehat H^{ecd}\\
&+\frac{i \beta}{18} C^{c} \widehat H^{efd} \widehat H_{efb}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{ba}\widehat R_{cd}{}^{j}(Q)\Bigg[C_{b}\Big[\frac{\beta g}{3456} L_{ij}\Big[-6 i \widehat G^{cd}\\
&+59 i \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&-\frac{i \alpha}{4} \widehat R^{cd}{}_{ij}(V)\Big]\\
&+\frac{\beta g}{1152} L_{ij}\Big[-22 i \widehat H_{b}{}^{cd}\\
&+23 i \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\chi^{j}\Bigg[\frac{2 \zeta}{L} L_{ij}\Big[\frac{1}{L} \mathcal D_{d}(L) \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[\frac{2 i}{L} E^{e}\\
&+\sqrt{2} i V^{e}\Big]\\
&+2\Big[\frac{N}{L} \varepsilon^{a}{}_{bcde}\Big[-5 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&+2\Big[-\frac{2 i}{L} E_{b} T^{a}{}_{c}\\
&+\sqrt{2} i T^{a}{}_{b} V_{c}\Big]\Big]\Big]\\
&+\frac{2 \zeta}{L} \mathcal D_{d}(L_{ij}) \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[-\frac{2 i}{L} E^{e}\\
&-\sqrt{2} i V^{e}\Big]\\
&+\frac{2 \alpha}{3}\Big[4 i C_{b} \widehat R^{a}{}_{cij}(V)\\
&+i \varepsilon^{a}{}_{bcde} \widehat R^{de}{}_{ij}(V)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 \alpha}{3}\bar\psi_{a}{}^{i}\gamma^{bc}\chi_{i}\Bigg[C_{d}\Big[\varepsilon_{bc}{}^{d}{}_{ef}\Big[i \mathcal D^{a}(T^{ef})\\
&+2 i \mathcal D^{e}(T^{fa})\Big]\\
&+\varepsilon^{a}{}_{bcef}\Big[-i \mathcal D^{d}(T^{ef})\\
&+2 i \mathcal D^{e}(T^{df})\Big]\\
&-i \mathcal D^{e}(T_{ef}) \varepsilon^{dfa}{}_{bc}\Big]\\
&+2\Big[-i \mathcal D^{a}(T_{bc})\\
&+2 i \mathcal D_{b}(T^{a}{}_{c})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{a}(\varphi^{j})\Bigg[\mathcal D_{c}(L_{ik}) L_{j}{}^{k}\Big[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\frac{\sqrt{2} i}{2} E_{b} L_{ij} V_{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{a}(\varphi_{i})\Bigg[\frac{\zeta}{L} T_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[\frac{i}{2 L} E^{f}\\
&+\frac{\sqrt{2} i}{4} V^{f}\Big]\\
&+\frac{\zeta}{L} \widehat G_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[-\frac{i}{4 L} E^{f}\\
&-\frac{\sqrt{2} i}{8} V^{f}\Big]\\
&-\frac{3 i N \zeta}{L^{2}} T_{bc}\\
&+\frac{i N \zeta}{L^{2}} \widehat G_{bc}\\
&-\frac{i \beta g}{6} C_{d} \widehat H^{d}{}_{bc}\\
&-\frac{i \zeta}{L^{3}} E_{b} \mathcal D_{c}(L)\\
&+\frac{\sqrt{2} i \zeta}{2 L^{2}} V_{c} \mathcal D_{b}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{16} C_{b} \widehat H_{c}{}^{de}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{a}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{a}\mathcal D_{c}(\varphi_{i})\Bigg[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L} L_{ij} \varepsilon^{a}{}_{bcde}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\chi^{j})\Bigg[-\frac{2 i}{L} E^{e}\\
&-\sqrt{2} i V^{e}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{32 i \alpha}{3} C_{e} T_{fd} \varepsilon^{efa}{}_{bc}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\varphi^{j})\Bigg[L_{ij} \varepsilon^{a}{}_{bcde}\Big[\frac{i \beta g^{2}}{2} C^{e}\\
&+\frac{\sqrt{2} i N \zeta}{4 L^{3}} V^{e}\Big]\\
&-\frac{i N \zeta}{2 L^{4}} L_{j}{}^{k} \mathcal D^{e}(L_{ik}) \varepsilon^{a}{}_{bcde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\varphi_{i})\Bigg[\frac{\zeta}{L} T_{ef}\Big[\varepsilon^{a}{}_{bc}{}^{ef}\Big[-\frac{i}{2 L} E_{d}\\
&-\frac{\sqrt{2} i}{4} V_{d}\Big]\\
&+\varepsilon^{a}{}_{bcd}{}^{f}\Big[-\frac{i}{L} E^{e}\\
&-\frac{\sqrt{2} i}{2} V^{e}\Big]\Big]\\
&+\widehat G_{de} \varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[\frac{i \beta g}{6} C^{f}\\
&+\frac{i \zeta}{2 L^{2}} E^{f}\\
&+\frac{\sqrt{2} i \zeta}{4 L} V^{f}\Big]\\
&+\frac{\zeta}{L} T_{de} \varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[-\frac{5 i}{L} E^{f}\\
&-\frac{5 \sqrt{2} i}{2} V^{f}\Big]\\
&+\frac{\zeta}{L} T^{a}{}_{e} \varepsilon_{bcd}{}^{e}{}_{f}\Big[\frac{i}{L} E^{f}\\
&+\frac{\sqrt{2} i}{2} V^{f}\Big]\\
&+\frac{\zeta}{L} \widehat G_{ef} \varepsilon^{a}{}_{bc}{}^{ef}\Big[\frac{i}{4 L} E_{d}\\
&+\frac{\sqrt{2} i}{8} V_{d}\Big]\\
&-\frac{i \beta g}{2} C_{b} \widehat H^{a}{}_{cd}\\
&+\frac{i \beta g}{6} C_{d} \widehat H^{a}{}_{bc}\\
&-\frac{i N \zeta}{2 L^{3}} \mathcal D^{e}(L) \varepsilon_{e}{}^{a}{}_{bcd}\\
&-\frac{i \beta g}{8} \varepsilon^{efa}{}_{bc} \widehat H_{efd}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{32}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\widehat R^{a}{}_{di}(Q))\Bigg[i \widehat G_{bc}\\
&+8 i C_{e} \widehat H^{e}{}_{bc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\widehat R_{edi}(Q))\Bigg[C_{f} \varepsilon^{a}{}_{bc}{}^{f}{}_{g}\Big[2 i \alpha T^{ge}\\
&-\frac{i \beta}{32} \widehat G^{ge}\Big]\\
&+\frac{\beta}{32}\Big[C_{b}\Big[4 i \widehat H^{a}{}_{c}{}^{e}\\
&-i \varepsilon^{fga}{}_{c}{}^{e} \widehat G_{fg}\Big]\\
&-8 i C^{e} \widehat H^{a}{}_{bc}\\
&-i \varepsilon^{fga}{}_{bc} \widehat H_{fg}{}^{e}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\widehat R_{efi}(Q))\Bigg[C_{g} \varepsilon^{a}{}_{bcd}{}^{g}\Big[-2 i \alpha T^{ef}\\
&+\frac{5 i \beta}{64} \widehat G^{ef}\Big]\\
&+\frac{\beta}{32} C_{b}\Big[-2 i \varepsilon^{ga}{}_{cd}{}^{f} \widehat G_{g}{}^{e}\\
&-i \varepsilon^{ga}{}_{c}{}^{ef} \widehat G_{gd}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{16}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}(\widehat R_{e}{}^{a}{}_{i}(Q))\Bigg[5 i C^{e} \widehat H_{bcd}\\
&+2 i C_{b} \widehat H_{cd}{}^{e}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i N \zeta}{2 L^{2}} \varepsilon^{a}{}_{bcde}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D^{d}\mathcal D^{e}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D_{c}(\varphi^{j})\Bigg[\mathcal D^{a}(L_{ik}) L_{j}{}^{k}\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+L_{ij} E^{a}\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D_{c}(\varphi_{i})\Bigg[\frac{\zeta}{L^{2}} \mathcal D^{a}(L)\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\frac{2 i}{L} E^{a}{}_{b}\\
&+\frac{6 i N \zeta}{L^{2}} T^{a}{}_{b}\\
&-\frac{i N \zeta}{L^{2}} \widehat G^{a}{}_{b}\\
&-\frac{i \beta g}{3} C_{d} \widehat H^{da}{}_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{16} C_{b} \widehat H^{ade}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D_{c}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{48}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D_{c}(\widehat R_{d}{}^{a}{}_{i}(Q))\Bigg[3 i \widehat G_{b}{}^{d}\\
&-i \varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{bc}\mathcal D_{c}\mathcal D^{a}(\varphi_{i})\Bigg[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L} \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\bar\psi_{a}{}^{i}\gamma^{bc}\phi_{di}\Bigg[\frac{i}{2 L} E^{e}\\
&+\frac{\sqrt{2} i}{4} V^{e}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{bc}\psi^{a}{}_{i}\Bigg[T_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[\frac{i}{2 L} E^{f}\\
&+\frac{\sqrt{2} i}{4} V^{f}\Big]\\
&+\widehat G_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[-\frac{i}{8 L} E^{f}\\
&-\frac{\sqrt{2} i}{16} V^{f}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{bc}\psi_{di}\Bigg[T_{ef} \varepsilon_{bc}{}^{def}\Big[-\frac{i}{2 L} E^{a}\\
&-\frac{\sqrt{2} i}{4} V^{a}\Big]\\
&+\widehat G_{ef} \varepsilon_{bc}{}^{def}\Big[\frac{i}{8 L} E^{a}\\
&+\frac{\sqrt{2} i}{16} V^{a}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\psi_{d}{}^{j}\Bigg[C_{e}\Big[\beta g L_{ij} \varepsilon^{a}{}_{bc}{}^{de}\Big[\frac{i g (L^{2} g + 3 N)}{8}\\
&+\frac{i}{8} \Box^c(\sigma)\\
&+\frac{i}{16} \widehat G^{fg} \widehat G_{fg}\\
&+\frac{i}{16} \widehat H^{fgh} \widehat H_{fgh}\Big]\\
&+\widehat R_{fgij}(V) \varepsilon^{a}{}_{bc}{}^{de}\Big[-\frac{2 i \alpha}{3} T^{fg}\\
&+\frac{i \beta}{24} \widehat G^{fg}\Big]\\
&+\beta\Big[\frac{i g}{8} \Box^c(L_{ij}) \varepsilon^{ea}{}_{bc}{}^{d}\\
&-\frac{i}{3} \widehat H^{a}{}_{bc} \widehat R^{ed}{}_{ij}(V)\\
&+\frac{i}{3} \widehat H^{a}{}_{b}{}^{d} \widehat R^{e}{}_{cij}(V)\\
&+\frac{i}{6} \widehat H^{ead} \widehat R_{bcij}(V)\\
&+\frac{2 i}{3} \widehat H^{ea}{}_{b} \widehat R_{c}{}^{d}{}_{ij}(V)\\
&+\frac{i}{6} \widehat H^{e}{}_{bc} \widehat R^{ad}{}_{ij}(V)\Big]\Big]\\
&+\frac{\zeta}{L}\Big[\frac{1}{L} E_{e}\Big[L_{ij}\Big[\frac{1}{L} E^{e} \varepsilon^{a}{}_{bc}{}^{d}{}_{f}\Big[\frac{i}{4 L} E^{f}\\
&+\frac{\sqrt{2} i}{8} V^{f}\Big]\\
&+\varepsilon^{a}{}_{bc}{}^{de}\Big[-i (D - \frac{N^{2}}{4 L^{2}})\\
&-\frac{2 i}{3} T^{fg} T_{fg}\\
&-\frac{i}{8 L^{2}} \mathcal D^{f}(L^{kl}) \mathcal D_{f}(L_{kl})\Big]\Big]\\
&+\frac{1}{L} L_{j}{}^{k}\Big[\frac{i}{2 L} E_{f} \mathcal D^{f}(L_{ik}) \varepsilon^{ea}{}_{bc}{}^{d}\\
&+\frac{\sqrt{2} i}{4} V_{f} \mathcal D^{e}(L_{ik}) \varepsilon^{fa}{}_{bc}{}^{d}\Big]\\
&+\varepsilon^{a}{}_{bc}{}^{de}\Big[-\frac{i}{4} \Box^c(L_{ij})\\
&+\frac{i}{4 L} \mathcal D^{f}(L_{ij}) \mathcal D_{f}(L)\Big]\Big]\\
&+\sqrt{2} V_{e}\Big[L_{ij} \varepsilon^{a}{}_{bc}{}^{de}\Big[-\frac{i (4 D - \frac{N^{2}}{L^{2}})}{8}\\
&-\frac{i}{3} T^{fg} T_{fg}\\
&-\frac{i}{16 L^{2}} \mathcal D^{f}(L^{kl}) \mathcal D_{f}(L_{kl})\Big]\\
&+\varepsilon^{a}{}_{bc}{}^{de}\Big[-\frac{i}{8} \Box^c(L_{ij})\\
&+\frac{i}{8 L} \mathcal D^{f}(L_{ij}) \mathcal D_{f}(L)\Big]\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\varphi^{j}\Bigg[L_{ij}\Big[\frac{\zeta}{L^{3}} E_{d}\Big[T_{ef}\Big[\varepsilon^{a}{}_{bc}{}^{ef}\Big[-\frac{5 i}{2 L} E^{d}\\
&-\frac{3 \sqrt{2} i}{4} V^{d}\Big]\\
&+\frac{3 i}{2 L} E^{a} \varepsilon^{def}{}_{bc}\\
&+\frac{\sqrt{2} i}{2} V^{e} \varepsilon^{dfa}{}_{bc}\Big]\\
&+\widehat G_{ef}\Big[\varepsilon^{a}{}_{bc}{}^{ef}\Big[\frac{i}{4 L} E^{d}\\
&+\frac{\sqrt{2} i}{8} V^{d}\Big]\\
&-\frac{i}{4 L} E^{a} \varepsilon^{def}{}_{bc}\Big]\\
&+\frac{\sqrt{2}}{4} V_{e}\Big[\varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[6 i T^{df}\\
&-i \widehat G^{df}\Big]\\
&+2 i T_{f}{}^{a} \varepsilon^{dfe}{}_{bc}\Big]\\
&+\frac{1}{2 L}\Big[E_{e} \varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[8 i T^{df}\\
&-i \widehat G^{df}\Big]\\
&-i \mathcal D^{e}(N) \varepsilon^{d}{}_{e}{}^{a}{}_{bc}\Big]\Big]\\
&+\frac{\zeta}{L^{3}} E^{a}\Big[\frac{\sqrt{2}}{8} V_{d} \varepsilon_{bc}{}^{d}{}_{ef}\Big[6 i T^{ef}\\
&-i \widehat G^{ef}\Big]\\
&+\frac{1}{L}\Big[-5 i N T_{bc}\\
&+i N \widehat G_{bc}\\
&-\frac{3 i}{L} E_{b} \mathcal D_{c}(L)\\
&+\frac{3 \sqrt{2} i}{2} V_{c} \mathcal D_{b}(L)\Big]\Big]\\
&+\frac{\sqrt{2} \zeta}{L^{3}} V_{c}\Big[-i N T^{a}{}_{b}\\
&+\frac{i}{2} \mathcal D^{a}(E_{b})\\
&-\frac{i}{2} \mathcal D_{b}(E^{a})\\
&-\frac{3 i}{2 L} E_{b} \mathcal D^{a}(L)\Big]\\
&+\frac{1}{L} T_{de}\Big[\varepsilon^{a}{}_{bc}{}^{de}\Big[i (\frac{4 D \zeta}{L} - 2 + \frac{3 N^{2} \zeta}{2 L^{3}})\\
&+\frac{i \zeta}{2 L^{3}} \mathcal D^{f}(L^{kl}) \mathcal D_{f}(L_{kl})\Big]\\
&+\frac{8 i \zeta}{3 L} T^{de} T_{fg} \varepsilon^{fga}{}_{bc}\Big]\\
&+\frac{\zeta}{L^{4}} E_{b}\Big[-i \mathcal D^{a}(E_{c})\\
&+i \mathcal D_{c}(E^{a})\\
&+i N \widehat G^{a}{}_{c}\Big]\\
&+\frac{\sqrt{2} \zeta}{L^{3}} V_{d} \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[\frac{3 i N}{4 L} \mathcal D^{e}(L)\\
&-\frac{i}{4} \mathcal D^{e}(N)\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[-\frac{i N \zeta}{2 L^{4}} \mathcal D^{d}(E^{e})\\
&+\frac{i (\beta g^{2} - \frac{8 N^{2} \zeta}{L^{4}})}{16} \widehat G^{de}\Big]\\
&+\frac{i \beta g^{2}}{4} C_{b} \widehat G^{a}{}_{c}\\
&+\frac{2 i}{L^{3}} E^{a}{}_{b} E_{c}\Big]\\
&+\frac{1}{L^{3}} L_{j}{}^{k}\Big[\zeta \mathcal D_{d}(L_{ik})\Big[T_{ef}\Big[\varepsilon^{a}{}_{bc}{}^{ef}\Big[-\frac{5 i}{2 L} E^{d}\\
&-\frac{3 \sqrt{2} i}{4} V^{d}\Big]\\
&+\varepsilon^{a}{}_{bc}{}^{df}\Big[\frac{i}{L} E^{e}\\
&+\frac{\sqrt{2} i}{2} V^{e}\Big]\Big]\\
&+\frac{\sqrt{2}}{4} V_{e}\Big[\varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[-6 i T^{fd}\\
&+i \widehat G^{fd}\Big]\\
&+2 i T_{f}{}^{a} \varepsilon^{fe}{}_{bc}{}^{d}\Big]\\
&+\frac{1}{2 L} E_{e}\Big[\varepsilon^{a}{}_{bc}{}^{e}{}_{f}\Big[-6 i T^{fd}\\
&+i \widehat G^{fd}\Big]\\
&-2 i T_{f}{}^{a} \varepsilon^{ef}{}_{bc}{}^{d}\Big]\\
&+\widehat G_{ef} \varepsilon^{a}{}_{bc}{}^{ef}\Big[\frac{i}{4 L} E^{d}\\
&+\frac{\sqrt{2} i}{8} V^{d}\Big]\\
&-\frac{3 i N}{2 L^{2}} \mathcal D^{e}(L) \varepsilon_{e}{}^{a}{}_{bc}{}^{d}\Big]\\
&+\zeta \mathcal D^{a}(L_{ik})\Big[T_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[\frac{3 i}{2 L} E^{f}\\
&+\frac{3 \sqrt{2} i}{4} V^{f}\Big]\\
&+\widehat G_{de} \varepsilon_{bc}{}^{de}{}_{f}\Big[-\frac{i}{4 L} E^{f}\\
&-\frac{\sqrt{2} i}{8} V^{f}\Big]\\
&+\frac{1}{L}\Big[-5 i N T_{bc}\\
&+i N \widehat G_{bc}\\
&-\frac{3 i}{L} E_{b} \mathcal D_{c}(L)\\
&+\frac{3 \sqrt{2} i}{2} V_{c} \mathcal D_{b}(L)\Big]\Big]\\
&+\mathcal D_{c}(L_{ik})\Big[\frac{\zeta}{L} \mathcal D^{a}(L)\Big[\frac{3 i}{L} E_{b}\\
&+\frac{3 \sqrt{2} i}{2} V_{b}\Big]\\
&+2 i E^{a}{}_{b}\\
&+\frac{2 i N \zeta}{L} T^{a}{}_{b}\\
&-\frac{i N \zeta}{L} \widehat G^{a}{}_{b}\Big]\\
&+\zeta\Big[\mathcal D_{c}\mathcal D^{a}(L_{ik})\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\mathcal D^{a}\mathcal D_{c}(L_{ik})\Big[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&-\frac{i N}{2 L} \mathcal D^{d}\mathcal D^{e}(L_{ik}) \varepsilon^{a}{}_{bcde}\Big]\Big]\\
&+\mathcal D_{d}(L_{ij})\Big[\varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[\frac{i \beta g^{2}}{4} C^{e}\\
&+\frac{\sqrt{2} i N \zeta}{4 L^{3}} V^{e}\Big]\\
&-\frac{i \zeta}{L^{3}} T_{ef} \mathcal D^{d}(L) \varepsilon^{efa}{}_{bc}\Big]\\
&+\frac{\zeta}{L^{3}} E_{b}\Big[\frac{i}{L} E^{a} \mathcal D_{c}(L_{ij})\\
&+\frac{\sqrt{2} i}{2} V_{c} \mathcal D^{a}(L_{ij})\\
&+\frac{i}{L} \mathcal D^{a}(L_{ik}) \mathcal D_{c}(L_{j}{}^{k})\\
&+\frac{i}{L} \mathcal D^{a}(L_{jk}) \mathcal D_{c}(L_{i}{}^{k})\Big]\\
&+\frac{\sqrt{2} \zeta}{2 L^{3}} V_{b}\Big[i E^{a} \mathcal D_{c}(L_{ij})\\
&+i \mathcal D^{a}(L_{ik}) \mathcal D_{c}(L_{j}{}^{k})\\
&+i \mathcal D^{a}(L_{jk}) \mathcal D_{c}(L_{i}{}^{k})\Big]\\
&+\frac{\zeta}{L^{2}} T_{de} \varepsilon^{a}{}_{bc}{}^{de}\Big[i \Box^c(L_{ij})\\
&-\frac{i}{L^{2}} E_{f} L_{i}{}^{k} \mathcal D^{f}(L_{jk})\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[\frac{i \beta g}{12} \widehat R^{de}{}_{ij}(V)\\
&+\frac{i N \zeta}{2 L^{4}} \mathcal D^{d}(L_{ik}) \mathcal D^{e}(L_{j}{}^{k})\Big]\\
&+\frac{i \beta g}{3} C_{b} \widehat R^{a}{}_{cij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\varphi_{i}\Bigg[\frac{\beta g}{24} C_{d}\Big[\varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[-5 i \mathcal D^{f}(\widehat G_{f}{}^{e})\\
&+3 i \widehat G_{fg} \widehat H^{fge}\Big]\\
&-11 i \mathcal D^{a}(\widehat H^{d}{}_{bc})\\
&+11 i \mathcal D^{d}(\widehat H^{a}{}_{bc})\\
&+22 i \mathcal D_{b}(\widehat H^{da}{}_{c})\\
&+18 i \widehat G^{a}{}_{c} \widehat G^{d}{}_{b}\\
&-9 i \widehat G^{da} \widehat G_{bc}\\
&-6 i \widehat H^{d}{}_{eb} \widehat H^{ea}{}_{c}\\
&+3 i \widehat H^{d}{}_{e}{}^{a} \widehat H^{e}{}_{bc}\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V_{d}\Big[\frac{1}{L} \mathcal D_{e}(L)\Big[i T^{d}{}_{f} \varepsilon^{efa}{}_{bc}\\
&+i T^{e}{}_{f} \varepsilon^{fda}{}_{bc}\\
&+i T_{f}{}^{a} \varepsilon^{efd}{}_{bc}\Big]\\
&+\frac{1}{2 L} T_{ef}\Big[i \mathcal D^{a}(L) \varepsilon^{efd}{}_{bc}\\
&-i \mathcal D^{d}(L) \varepsilon^{efa}{}_{bc}\Big]\\
&+T_{bc}\Big[12 i T^{da}\\
&-i \widehat G^{da}\Big]\\
&+\frac{1}{2} \varepsilon_{bc}{}^{d}{}_{ef}\Big[-i \mathcal D^{a}(T^{ef})\\
&-2 i \mathcal D^{e}(T^{fa})\Big]\\
&+\frac{1}{2} \varepsilon^{a}{}_{bcef}\Big[i \mathcal D^{d}(T^{ef})\\
&-2 i \mathcal D^{e}(T^{df})\Big]\\
&-8 i T^{a}{}_{c} T^{d}{}_{b}\\
&-i T^{da} \widehat G_{bc}\\
&-i \mathcal D^{e}(T_{ef}) \varepsilon^{fda}{}_{bc}\Big]\\
&+\frac{\zeta}{L^{2}} E_{d}\Big[\frac{2}{L} \mathcal D_{e}(L)\Big[i T^{d}{}_{f} \varepsilon^{efa}{}_{bc}\\
&-i T^{e}{}_{f} \varepsilon^{dfa}{}_{bc}\\
&+i T_{f}{}^{a} \varepsilon^{def}{}_{bc}\Big]\\
&+\frac{1}{L} T_{ef}\Big[i \mathcal D^{a}(L) \varepsilon^{def}{}_{bc}\\
&-i \mathcal D^{d}(L) \varepsilon^{efa}{}_{bc}\Big]\\
&+2 T_{bc}\Big[12 i T^{da}\\
&-i \widehat G^{da}\Big]\\
&+\varepsilon_{bc}{}^{d}{}_{ef}\Big[-i \mathcal D^{a}(T^{ef})\\
&-2 i \mathcal D^{e}(T^{fa})\Big]\\
&+\varepsilon^{a}{}_{bcef}\Big[i \mathcal D^{d}(T^{ef})\\
&-2 i \mathcal D^{e}(T^{df})\Big]\\
&+2\Big[-8 i T^{a}{}_{c} T^{d}{}_{b}\\
&-i T^{da} \widehat G_{bc}\\
&+i \mathcal D^{e}(T_{ef}) \varepsilon^{dfa}{}_{bc}\Big]\Big]\\
&+\frac{\beta g}{24} C_{b}\Big[-12 i \mathcal D^{a}\mathcal D_{c}(\sigma)\\
&-14 i \mathcal D^{d}(\widehat H_{d}{}^{a}{}_{c})\\
&+12 i \mathcal D_{c}\mathcal D^{a}(\sigma)\\
&+13 i \mathcal D^{d}(\widehat G_{ef}) \varepsilon_{d}{}^{efa}{}_{c}\Big]\\
&+\frac{2 \zeta}{L} T^{a}{}_{d}\Big[\sqrt{2} V_{c}\Big[-4 i T^{d}{}_{b}\\
&+i \widehat G^{d}{}_{b}\Big]\\
&+\frac{1}{L}\Big[2 E_{b}\Big[4 i T^{d}{}_{c}\\
&-i \widehat G^{d}{}_{c}\Big]\\
&+N \varepsilon_{bc}{}^{d}{}_{ef}\Big[-4 i T^{ef}\\
&+i \widehat G^{ef}\Big]\Big]\Big]\\
&+\frac{1}{L} T_{de}\Big[\varepsilon_{bc}{}^{de}{}_{f}\Big[-2 i E^{fa}\\
&+\frac{i N \zeta}{L} \widehat G^{fa}\Big]\\
&-\frac{4 i N \zeta}{L} \varepsilon^{fea}{}_{bc} \widehat G^{d}{}_{f}\Big]\\
&+\frac{\beta g}{48} \varepsilon^{a}{}_{bcde}\Big[-12 i \mathcal D^{d}\mathcal D^{e}(\sigma)\\
&-7 i \mathcal D^{f}(\widehat H_{f}{}^{de})\Big]\\
&+\frac{2 i N \zeta}{L^{2}} \mathcal D^{a}(T_{bc})\\
&-\frac{13 i \beta g}{24} \mathcal D^{a}(\widehat G_{bc})\\
&-\frac{4 i N \zeta}{L^{2}} \mathcal D_{b}(T^{a}{}_{c})\\
&+\frac{13 i \beta g}{12} \mathcal D_{b}(\widehat G^{a}{}_{c})\\
&+\frac{4 i N \zeta}{L^{3}} T^{a}{}_{c} \mathcal D_{b}(L)\\
&-\frac{2 i N \zeta}{L^{3}} T_{bc} \mathcal D^{a}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{bc}\widehat R_{dei}(Q)\Bigg[C_{b}\Big[\frac{\beta}{864} \widehat H_{fgh}\Big[3 i \varepsilon^{fghae} \widehat G_{c}{}^{d}\\
&+2 i \varepsilon^{fgha}{}_{c} \widehat G^{de}\\
&-7 i \varepsilon^{fghde} \widehat G^{a}{}_{c}\\
&-3 i \varepsilon^{fgh}{}_{c}{}^{e} \widehat G^{ad}\Big]\\
&+\frac{i \alpha}{8} \widehat C^{dea}{}_{c}\\
&-\frac{8 i \alpha}{3} T^{a}{}_{c} T^{de}\\
&+\frac{i \beta}{24} \widehat G^{ad} \widehat G_{c}{}^{e}\\
&-\frac{i \beta}{144} \widehat G^{a}{}_{c} \widehat G^{de}\\
&-\frac{7 i \beta}{72} \widehat H^{fde} \widehat H_{f}{}^{a}{}_{c}\\
&+\frac{i \beta}{12} \widehat H^{f}{}_{c}{}^{e} \widehat H_{f}{}^{ad}\Big]\\
&+C_{f}\Big[\frac{\beta}{32} \widehat G_{gh}\Big[i \varepsilon^{fa}{}_{bc}{}^{e} \widehat H^{ghd}\\
&-i \varepsilon^{fha}{}_{bc} \widehat H^{gde}\Big]\\
&+\varepsilon^{a}{}_{bc}{}^{f}{}_{g}\Big[i \alpha \mathcal D^{d}(T^{ge})\\
&+\frac{i \beta}{32} \widehat G_{h}{}^{d} \widehat H^{hge}\Big]\Big]\\
&+\frac{\beta}{216} \widehat H^{a}{}_{bc}\Big[6 i \widehat G^{de}\\
&-i \varepsilon^{fghde} \widehat H_{fgh}\Big]\\
&+\varepsilon^{a}{}_{bcfg}\Big[\frac{i \alpha}{32} \widehat C^{defg}\\
&-\frac{2 i \alpha}{3} T^{de} T^{fg}\\
&-\frac{i \beta}{576} \widehat G^{de} \widehat G^{fg}\\
&+\frac{i \beta}{96} \widehat G^{fd} \widehat G^{ge}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{11 i \beta g}{1152} C_{f} L_{ij} \varepsilon^{fga}{}_{bc} \widehat H_{g}{}^{de}\bar\psi_{a}{}^{i}\gamma^{bc}\widehat R_{de}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{23 i \beta g}{576} C^{d} L_{ij} \widehat G_{bc}\bar\psi_{a}{}^{i}\gamma^{bc}\widehat R_{d}{}^{aj}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\bar\psi_{a}{}^{i}\gamma^{bc}\widehat R_{d}{}^{a}{}_{i}(Q)\Bigg[\widehat H_{bce}\Big[17 i \widehat G^{ed}\\
&+i \varepsilon^{fghed} \widehat H_{fgh}\Big]\\
&-16 i C_{b} \widehat H^{efd} \widehat H_{efc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\chi^{j}\Bigg[\frac{2}{L} L_{ij}\Big[\frac{2 \zeta}{L} \mathcal D^{a}(L)\Big[-\frac{2}{L} E_{b}\\
&-\sqrt{2} V_{b}\Big]\\
&+6 \zeta T_{cd} \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[\frac{2}{L} E^{e}\\
&+\sqrt{2} V^{e}\Big]\\
&+\zeta \widehat G_{cd} \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[-\frac{2}{L} E^{e}\\
&-\sqrt{2} V^{e}\Big]\\
&+4\Big[-2 E^{a}{}_{b}\\
&-\frac{2 N \zeta}{L} T^{a}{}_{b}\\
&+\frac{N \zeta}{L} \widehat G^{a}{}_{b}\Big]\Big]\\
&+\frac{4 \zeta}{L} \mathcal D^{a}(L_{ij})\Big[\frac{2}{L} E_{b}\\
&+\sqrt{2} V_{b}\Big]\\
&+\frac{4 \alpha}{3}\Big[-2 \widehat R^{a}{}_{bij}(V)\\
&-C_{c} \varepsilon^{ca}{}_{bde} \widehat R^{de}{}_{ij}(V)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{32 \alpha}{3}\bar\psi_{a}{}^{i}\gamma^{b}\chi_{i}\Bigg[2 C_{c}\Big[-\mathcal D^{a}(T^{c}{}_{b})\\
&+\mathcal D^{c}(T^{a}{}_{b})\\
&+\mathcal D_{b}(T^{ca})\Big]\\
&-C_{b} \mathcal D^{c}(T_{c}{}^{a})\\
&-\mathcal D^{c}(T_{de}) \varepsilon_{c}{}^{dea}{}_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L} L_{ij}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{a}(\chi^{j})\Bigg[\frac{2}{L} E_{b}\\
&+\sqrt{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{a}(\varphi^{j})\Bigg[L_{ij}\Big[-\beta g^{2} C_{b}\\
&-\frac{\sqrt{2} N \zeta}{2 L^{3}} V_{b}\Big]\\
&+\frac{N \zeta}{L^{4}} L_{j}{}^{k} \mathcal D_{b}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{a}(\varphi_{i})\Bigg[T_{bc}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&+\frac{N}{L^{2}} \mathcal D_{b}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{a}(\widehat R_{cdi}(Q))\Bigg[C_{b}\Big[4 \alpha T^{cd}\\
&-\frac{5 \beta}{32} \widehat G^{cd}\\
&+\frac{5 \beta}{96} \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\frac{\beta}{48}\Big[C^{c}\Big[-3 \widehat G_{b}{}^{d}\\
&+\varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Big]\\
&+3 \widehat H_{b}{}^{cd}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L^{2}}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{a}\mathcal D_{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{64 \alpha}{3} C_{b} T^{a}{}_{c}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\varphi^{j})\Bigg[\mathcal D_{d}(L_{ik}) L_{j}{}^{k} \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[\frac{1}{L} E^{e}\\
&+\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\frac{\sqrt{2}}{2} E_{d} L_{ij} V_{e} \varepsilon^{dea}{}_{bc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\varphi_{i})\Bigg[\frac{\beta g}{18} C_{b}\Big[6 \widehat G^{a}{}_{c}\\
&+\varepsilon^{defa}{}_{c} \widehat H_{def}\Big]\\
&+\frac{\zeta}{L^{2}} \mathcal D_{d}(L) \varepsilon^{a}{}_{bc}{}^{d}{}_{e}\Big[\frac{1}{L} E^{e}\\
&+\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\frac{3 \zeta}{L} T^{a}{}_{c}\Big[-\frac{2}{L} E_{b}\\
&-\sqrt{2} V_{b}\Big]\\
&+\frac{\zeta}{L} T^{a}{}_{b}\Big[-\frac{2}{L} E_{c}\\
&-\sqrt{2} V_{c}\Big]\\
&+\frac{N \zeta}{L^{2}} \varepsilon^{a}{}_{bcde}\Big[-3 T^{de}\\
&+\widehat G^{de}\Big]\\
&+\frac{\beta g}{4}\Big[2 \widehat H^{a}{}_{bc}\\
&+C_{d} \varepsilon^{defa}{}_{b} \widehat H_{efc}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{16} C_{d} \widehat G^{d}{}_{b}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\widehat R^{a}{}_{ci}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\widehat R_{dci}(Q))\Bigg[C_{b}\Big[4 \alpha T^{ad}\\
&-\frac{\beta}{16} \widehat G^{ad}\\
&+\frac{\beta}{48} \varepsilon^{efgad} \widehat H_{efg}\Big]\\
&+\frac{\beta}{32}\Big[-4 \widehat H^{a}{}_{b}{}^{d}\\
&-2 C^{d} \widehat G^{a}{}_{b}\\
&+\varepsilon^{efa}{}_{b}{}^{d} \widehat G_{ef}\\
&+2 C_{e} \varepsilon^{efga}{}_{b} \widehat H_{fg}{}^{d}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{32}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\widehat R_{dei}(Q))\Bigg[2 \varepsilon^{fa}{}_{bc}{}^{e} \widehat G_{f}{}^{d}\\
&+\varepsilon^{fa}{}_{b}{}^{de} \widehat G_{fc}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{48}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}(\widehat R_{d}{}^{a}{}_{i}(Q))\Bigg[C^{d}\Big[-3 \widehat G_{bc}\\
&+\varepsilon^{efg}{}_{bc} \widehat H_{efg}\Big]\\
&+C_{c}\Big[-3 \widehat G_{b}{}^{d}\\
&+\varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Big]\\
&-6 \widehat H_{bc}{}^{d}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L} \varepsilon^{a}{}_{bcde}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D^{c}\mathcal D^{d}(\varphi_{i})\Bigg[\frac{1}{L} E^{e}\\
&+\frac{\sqrt{2}}{2} V^{e}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L^{4}}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D_{b}(\varphi^{j})\Bigg[-E^{a} L_{ij}\\
&-L_{j}{}^{k} \mathcal D^{a}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D_{b}(\varphi_{i})\Bigg[T^{a}{}_{c}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&+\widehat G^{a}{}_{c}\Big[\frac{1}{L} E^{c}\\
&+\frac{\sqrt{2}}{2} V^{c}\Big]\\
&-\frac{N}{L^{2}} \mathcal D^{a}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{48}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D_{b}(\widehat R_{cdi}(Q))\Bigg[C^{c}\Big[3 \widehat G^{ad}\\
&-\varepsilon^{efgad} \widehat H_{efg}\Big]\\
&-3 \widehat H^{acd}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{48} C_{d}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D_{b}(\widehat R_{c}{}^{a}{}_{i}(Q))\Bigg[3 \widehat G^{dc}\\
&+\varepsilon^{defgc} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{N \zeta}{L^{2}}\bar\psi_{a}{}^{i}\gamma^{b}\mathcal D_{b}\mathcal D^{a}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{b}\phi^{a}{}_{i}\Bigg[-\frac{1}{L} E_{b}\\
&-\frac{\sqrt{2}}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N g \zeta}{L} L_{ij}\bar\psi_{a}{}^{i}\gamma^{b}\psi^{aj}\Bigg[\frac{1}{2 L} E_{b}\\
&+\frac{\sqrt{2}}{4} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{b}\psi_{bi}\Bigg[2 T^{a}{}_{c}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&+\widehat G^{a}{}_{c}\Big[\frac{1}{L} E^{c}\\
&+\frac{\sqrt{2}}{2} V^{c}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N g \zeta}{L} L_{ij}\bar\psi_{a}{}^{i}\gamma^{b}\psi_{b}{}^{j}\Bigg[-\frac{1}{2 L} E^{a}\\
&-\frac{\sqrt{2}}{4} V^{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L}\bar\psi_{a}{}^{i}\gamma^{b}\psi_{ci}\Bigg[T^{ac}\Big[\frac{2}{L} E_{b}\\
&+\sqrt{2} V_{b}\Big]\\
&+\widehat G^{ac}\Big[-\frac{1}{2 L} E_{b}\\
&-\frac{\sqrt{2}}{4} V_{b}\Big]\\
&+\frac{\sqrt{2}}{4} V^{c}\Big[4 T^{a}{}_{b}\\
&-\widehat G^{a}{}_{b}\Big]\\
&+\frac{1}{L}\Big[\frac{1}{2} E^{a}\Big[4 T_{b}{}^{c}\\
&-\widehat G_{b}{}^{c}\Big]\\
&+\frac{N}{4} \varepsilon^{a}{}_{b}{}^{c}{}_{de}\Big[-4 T^{de}\\
&+\widehat G^{de}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\varphi^{j}\Bigg[L_{ij}\Big[\frac{\zeta}{L^{3}} E_{c}\Big[T^{ac}\Big[-\frac{8}{L} E_{b}\\
&-\sqrt{2} V_{b}\Big]\\
&+T^{a}{}_{b}\Big[\frac{6}{L} E^{c}\\
&+\sqrt{2} V^{c}\Big]\\
&+\frac{1}{L}\Big[\varepsilon^{a}{}_{b}{}^{c}{}_{de}\Big[-8 N T^{de}\\
&+\mathcal D^{d}(E^{e})\\
&+\frac{3 N}{2} \widehat G^{de}\\
&+\frac{3 \sqrt{2}}{2} V^{e} \mathcal D^{d}(L)\Big]\\
&-2 E^{a} T^{c}{}_{b}\\
&-E_{b} \widehat G^{ca}\Big]\Big]\\
&+\frac{\sqrt{2} \zeta}{L^{3}} V_{c}\Big[\frac{1}{2} E_{b}\Big[6 T^{ca}\\
&-\widehat G^{ca}\Big]\\
&+\varepsilon^{a}{}_{b}{}^{c}{}_{de}\Big[-\frac{3 N}{2} T^{de}\\
&+\frac{1}{2} \mathcal D^{d}(E^{e})\\
&+\frac{N}{4} \widehat G^{de}\Big]\\
&-E^{a} T^{c}{}_{b}\Big]\\
&+\frac{1}{L} T^{a}{}_{b}\Big[-2 (\frac{8 D \zeta}{L} - 4 - \frac{3 N^{2} \zeta}{L^{3}})\\
&-\frac{32 \zeta}{3 L} T^{cd} T_{cd}\\
&-\frac{2 \zeta}{L^{3}} \mathcal D^{c}(L^{kl}) \mathcal D_{c}(L_{kl})\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D^{a}(N)\Big[-\frac{1}{L} E_{b}\\
&-\frac{\sqrt{2}}{2} V_{b}\Big]\\
&+\frac{2 N}{L^{3}} E^{a}{}_{b}\\
&+\frac{N \zeta}{L^{4}} \mathcal D^{a}(E_{b})\\
&-\frac{N \zeta}{L^{4}} \mathcal D_{b}(E^{a})\\
&-\big(\frac{\beta g^{2}}{4} + \frac{N^{2} \zeta}{L^{4}}\big) \widehat G^{a}{}_{b}\\
&+\frac{3 N \zeta}{L^{5}} E^{a} \mathcal D_{b}(L)\\
&+\frac{3 \sqrt{2} N \zeta}{2 L^{4}} V_{b} \mathcal D^{a}(L)\\
&-\frac{\beta g^{2}}{8} C_{c} \varepsilon^{cdea}{}_{b} \widehat G_{de}\Big]\\
&+\frac{\zeta}{L^{3}} L_{j}{}^{k}\Big[\mathcal D_{c}(L_{ik})\Big[\frac{1}{L} \mathcal D_{d}(L) \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[\frac{3}{L} E^{e}\\
&+\frac{3 \sqrt{2}}{2} V^{e}\Big]\\
&+T^{ac}\Big[-\frac{2}{L} E_{b}\\
&-\sqrt{2} V_{b}\Big]\\
&+T^{a}{}_{b}\Big[\frac{6}{L} E^{c}\\
&+\sqrt{2} V^{c}\Big]\\
&+\frac{N}{L} \varepsilon^{a}{}_{b}{}^{c}{}_{de}\Big[-5 T^{de}\\
&+\widehat G^{de}\Big]\Big]\\
&+\mathcal D_{b}(L_{ik})\Big[3 T^{a}{}_{c}\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&+\widehat G^{a}{}_{c}\Big[\frac{1}{L} E^{c}\\
&+\frac{\sqrt{2}}{2} V^{c}\Big]\\
&-\frac{3 N}{L^{2}} \mathcal D^{a}(L)\Big]\\
&+\mathcal D^{a}(L_{ik})\Big[T_{bc}\Big[\frac{2}{L} E^{c}\\
&+\sqrt{2} V^{c}\Big]\\
&+\frac{3 N}{L^{2}} \mathcal D_{b}(L)\Big]\\
&+\mathcal D_{c}\mathcal D_{d}(L_{ik}) \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[\frac{1}{L} E^{e}\\
&+\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\frac{N}{L}\Big[\mathcal D^{a}\mathcal D_{b}(L_{ik})\\
&-\mathcal D_{b}\mathcal D^{a}(L_{ik})\Big]\Big]\\
&+\frac{4 \zeta}{L^{2}} T^{a}{}_{b}\Big[-\Box^c(L_{ij})\\
&+\frac{1}{L} \mathcal D^{c}(L_{ij}) \mathcal D_{c}(L)\\
&+\frac{1}{L^{2}} E_{c} L_{i}{}^{k} \mathcal D^{c}(L_{jk})\Big]\\
&+\frac{\zeta}{L^{3}} \mathcal D_{c}(L_{j}{}^{k}) \mathcal D_{d}(L_{ik}) \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[\frac{1}{L} E^{e}\\
&+\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+\mathcal D^{a}(L_{ij})\Big[-\frac{\beta g^{2}}{2} C_{b}\\
&-\frac{\sqrt{2} N \zeta}{2 L^{3}} V_{b}\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[-\frac{\beta g}{6} C^{c} \widehat R^{de}{}_{ij}(V)\\
&+\frac{\sqrt{2} \zeta}{2 L^{3}} E^{c} V^{d} \mathcal D^{e}(L_{ij})\Big]\\
&-\frac{\beta g}{3} \widehat R^{a}{}_{bij}(V)\\
&-\frac{N \zeta}{L^{4}} E^{a} \mathcal D_{b}(L_{ij})\\
&-\frac{N \zeta}{L^{4}} \mathcal D^{a}(L_{ik}) \mathcal D_{b}(L_{j}{}^{k})\\
&-\frac{N \zeta}{L^{4}} \mathcal D^{a}(L_{jk}) \mathcal D_{b}(L_{i}{}^{k})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\varphi_{i}\Bigg[\frac{\zeta}{L} T^{a}{}_{c}\Big[\frac{2}{L} \mathcal D^{c}(L)\Big[\frac{2}{L} E_{b}\\
&+\sqrt{2} V_{b}\Big]\\
&+\frac{2}{L} \mathcal D_{b}(L)\Big[-\frac{2}{L} E^{c}\\
&-\sqrt{2} V^{c}\Big]\\
&+8 T_{de} \varepsilon_{b}{}^{cde}{}_{f}\Big[-\frac{2}{L} E^{f}\\
&-\sqrt{2} V^{f}\Big]\\
&+\widehat G_{de} \varepsilon_{b}{}^{cde}{}_{f}\Big[\frac{2}{L} E^{f}\\
&+\sqrt{2} V^{f}\Big]\\
&+\frac{8 N}{L}\Big[-6 T^{c}{}_{b}\\
&+\widehat G^{c}{}_{b}\Big]\Big]\\
&+\frac{\beta g}{24} C_{c}\Big[\varepsilon^{a}{}_{b}{}^{c}{}_{de}\Big[12 \mathcal D^{d}\mathcal D^{e}(\sigma)\\
&+7 \mathcal D^{f}(\widehat H_{f}{}^{de})\Big]\\
&+26\Big[-\mathcal D^{a}(\widehat G^{c}{}_{b})\\
&+\mathcal D^{c}(\widehat G^{a}{}_{b})\\
&+\mathcal D_{b}(\widehat G^{ca})\Big]\Big]\\
&+\frac{\beta g}{288} C_{b}\Big[3 \widehat H^{a}{}_{cd}\Big[24 \widehat G^{cd}\\
&-\varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\varepsilon^{a}{}_{cdef}\Big[44 \mathcal D^{c}(\widehat H^{def})\\
&-27 \widehat G^{cd} \widehat G^{ef}\Big]\\
&-120 \mathcal D^{c}(\widehat G_{c}{}^{a})\Big]\\
&+\frac{\sqrt{2} \zeta}{L} V_{c}\Big[2 T_{de}\Big[4 T^{c}{}_{f} \varepsilon^{fdea}{}_{b}\\
&+\varepsilon^{feca}{}_{b} \widehat G^{d}{}_{f}\Big]\\
&+2 \mathcal D^{a}(T^{c}{}_{b})\\
&-2 \mathcal D^{c}(T^{a}{}_{b})\\
&-2 \mathcal D_{b}(T^{ca})\\
&+\frac{2}{L} T^{a}{}_{b} \mathcal D^{c}(L)\\
&-\frac{2}{L} T^{c}{}_{b} \mathcal D^{a}(L)\\
&-T^{c}{}_{d} \varepsilon^{efda}{}_{b} \widehat G_{ef}\Big]\\
&+\frac{2 \zeta}{L^{2}} E_{c}\Big[2 T_{de}\Big[4 T^{c}{}_{f} \varepsilon^{fdea}{}_{b}\\
&+\varepsilon^{cfea}{}_{b} \widehat G^{d}{}_{f}\Big]\\
&+2 \mathcal D^{a}(T^{c}{}_{b})\\
&-2 \mathcal D^{c}(T^{a}{}_{b})\\
&-2 \mathcal D_{b}(T^{ca})\\
&+\frac{2}{L} T^{a}{}_{b} \mathcal D^{c}(L)\\
&-\frac{2}{L} T^{c}{}_{b} \mathcal D^{a}(L)\\
&-T^{c}{}_{d} \varepsilon^{efda}{}_{b} \widehat G_{ef}\Big]\\
&+\frac{2 \zeta}{L} \mathcal D_{c}(T^{ac})\Big[-\frac{2}{L} E_{b}\\
&-\sqrt{2} V_{b}\Big]\\
&+\frac{4}{L} T_{bc}\Big[-2 E^{ca}\\
&+\frac{N \zeta}{L} \widehat G^{ca}\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[\frac{2 N \zeta}{L^{2}} \mathcal D^{c}(T^{de})\\
&-\frac{13 \beta g}{24} \mathcal D^{c}(\widehat G^{de})\\
&-\frac{2 N \zeta}{L^{3}} T^{de} \mathcal D^{c}(L)\Big]\\
&+\frac{\beta g}{12}\Big[6 \mathcal D^{a}\mathcal D_{b}(\sigma)\\
&+7 \mathcal D^{c}(\widehat H_{c}{}^{a}{}_{b})\\
&-6 \mathcal D_{b}\mathcal D^{a}(\sigma)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\gamma^{b}\widehat R_{cdi}(Q)\Bigg[C_{e}\Big[\frac{\beta}{108} \widehat H^{a}{}_{b}{}^{e}\Big[-6 \widehat G^{cd}\\
&+\varepsilon^{fghcd} \widehat H_{fgh}\Big]\\
&+\varepsilon^{a}{}_{b}{}^{e}{}_{fg}\Big[-\frac{\alpha}{16} \widehat C^{cdfg}\\
&+\frac{4 \alpha}{3} T^{cd} T^{fg}\\
&+\frac{\beta}{288} \widehat G^{cd} \widehat G^{fg}\\
&-\frac{\beta}{48} \widehat G^{fc} \widehat G^{gd}\Big]\Big]\\
&+\frac{\beta}{864} \widehat H_{efg}\Big[-3 \varepsilon^{efgad} \widehat G_{b}{}^{c}\\
&-2 \varepsilon^{efga}{}_{b} \widehat G^{cd}\\
&+7 \varepsilon^{efgcd} \widehat G^{a}{}_{b}\\
&+3 \varepsilon^{efg}{}_{b}{}^{d} \widehat G^{ac}\\
&+6 C^{c} \varepsilon^{efghd} \widehat H_{h}{}^{a}{}_{b}\Big]\\
&+C_{b}\Big[2 \alpha \mathcal D^{c}(T^{ad})\\
&-\frac{\beta}{16} \widehat G_{e}{}^{a} \widehat H^{ecd}\\
&+\frac{\beta}{16} \widehat G_{e}{}^{c} \widehat H^{ead}\Big]\\
&+\frac{\beta}{144} \widehat H^{a}{}_{be}\Big[14 \widehat H^{ecd}\\
&+17 C^{c} \widehat G^{ed}\Big]\\
&-\frac{\alpha}{8} \widehat C^{cda}{}_{b}\\
&+\frac{8 \alpha}{3} T^{a}{}_{b} T^{cd}\\
&-\frac{\beta}{24} \widehat G^{ac} \widehat G_{b}{}^{d}\\
&+\frac{\beta}{144} \widehat G^{a}{}_{b} \widehat G^{cd}\\
&-\frac{\beta}{12} \widehat H^{e}{}_{b}{}^{d} \widehat H_{e}{}^{ac}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{1152} C_{b} L_{ij}\bar\psi_{a}{}^{i}\gamma^{b}\widehat R_{cd}{}^{j}(Q)\Bigg[22 \widehat H^{acd}\\
&-23 \varepsilon^{efacd} \widehat G_{ef}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{144}\bar\psi_{a}{}^{i}\gamma^{b}\widehat R_{c}{}^{a}{}_{i}(Q)\Bigg[\widehat H_{bde}\Big[C^{d}\Big[-17 \widehat G^{ec}\\
&+\varepsilon^{efghc} \widehat H_{fgh}\Big]\\
&+8 \widehat H^{dec}\\
&-7 C^{c} \widehat G^{de}\Big]\\
&-9 C_{b} \widehat G_{de} \widehat H^{dec}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i N \zeta}{L^{2}} L_{ij}\bar\psi_{a}{}^{i}\mathcal D^{a}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\mathcal D^{a}(\varphi^{j})\Bigg[L_{ij}\Big[\frac{\zeta}{L^{3}} E_{b}\Big[-\frac{2 i}{L} E^{b}\\
&-\frac{\sqrt{2} i}{2} V^{b}\Big]\\
&-i (- \frac{4 D \zeta}{L^{2}} + \beta g^{2} + \frac{2 (1 + \frac{N^{2} \zeta}{L^{3}})}{L})\\
&+\frac{8 i \zeta}{3 L^{2}} T^{bc} T_{bc}\\
&+\frac{i \zeta}{2 L^{4}} \mathcal D^{b}(L^{kl}) \mathcal D_{b}(L_{kl})\Big]\\
&+\frac{\zeta}{L^{2}}\Big[\frac{1}{L} \mathcal D_{b}(L_{ik}) L_{j}{}^{k}\Big[-\frac{2 i}{L} E^{b}\\
&-\frac{\sqrt{2} i}{2} V^{b}\Big]\\
&+i \Box^c(L_{ij})\\
&-\frac{i}{L} \mathcal D^{b}(L_{ij}) \mathcal D_{b}(L)\\
&-\frac{i}{L^{2}} E_{b} L_{i}{}^{k} \mathcal D^{b}(L_{jk})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{2}} \mathcal D_{b}(L)\bar\psi_{a}{}^{i}\mathcal D^{a}(\varphi_{i})\Bigg[-\frac{i}{L} E^{b}\\
&-\frac{\sqrt{2} i}{2} V^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\mathcal D^{a}(\widehat R_{bci}(Q))\Bigg[4 i \alpha T^{bc}\\
&-\frac{7 i \beta}{32} \widehat G^{bc}\\
&-\frac{i \beta}{16} C_{d} \widehat H^{dbc}\\
&+\frac{7 i \beta}{96} \varepsilon^{defbc} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\mathcal D^{a}\mathcal D^{b}(\varphi_{i})\Bigg[-\frac{i}{L} E_{b}\\
&-\frac{\sqrt{2} i}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{64 i \alpha}{3} T^{a}{}_{b}\bar\psi_{a}{}^{i}\mathcal D^{b}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\psi_{a}{}^{i}\mathcal D^{b}(\varphi^{j})\Bigg[\mathcal D^{a}(L_{ik}) L_{j}{}^{k}\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+L_{ij} E^{a}\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\mathcal D^{b}(\varphi_{i})\Bigg[\frac{\zeta}{L^{2}} \mathcal D^{a}(L)\Big[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Big]\\
&+\frac{\zeta}{L} T_{cd} \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[-\frac{i}{L} E^{e}\\
&-\frac{\sqrt{2} i}{2} V^{e}\Big]\\
&+\frac{\zeta}{L} \widehat G_{cd} \varepsilon^{a}{}_{b}{}^{cd}{}_{e}\Big[\frac{i}{2 L} E^{e}\\
&+\frac{\sqrt{2} i}{4} V^{e}\Big]\\
&+\frac{2 i}{L} E^{a}{}_{b}\\
&-\frac{2 i N \zeta}{L^{2}} T^{a}{}_{b}\\
&+i (\frac{\beta g}{3} - \frac{N \zeta}{L^{2}}) \widehat G^{a}{}_{b}\\
&+\frac{i \beta g}{2} C_{c} \widehat H^{ca}{}_{b}\\
&+\frac{i \beta g}{18} \varepsilon^{cdea}{}_{b} \widehat H_{cde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\mathcal D^{b}(\widehat R_{cbi}(Q))\Bigg[\frac{\beta}{32} C_{d}\Big[-20 i \widehat H^{dac}\\
&+i \varepsilon^{defac} \widehat G_{ef}\Big]\\
&+4 i \alpha T^{ac}\\
&-\frac{3 i \beta}{16} \widehat G^{ac}\\
&+\frac{i \beta}{24} \varepsilon^{defac} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{32}\bar\psi_{a}{}^{i}\mathcal D^{b}(\widehat R_{cdi}(Q))\Bigg[C_{e}\Big[-i \varepsilon^{efacd} \widehat G_{fb}\\
&-2 i \varepsilon^{efa}{}_{b}{}^{d} \widehat G_{f}{}^{c}\Big]\\
&+2\Big[10 i C^{c} \widehat H^{a}{}_{b}{}^{d}\\
&+i C_{b} \widehat H^{acd}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{48}\bar\psi_{a}{}^{i}\mathcal D^{b}(\widehat R_{c}{}^{a}{}_{i}(Q))\Bigg[3 i \widehat G_{b}{}^{c}\\
&+30 i C_{d} \widehat H^{d}{}_{b}{}^{c}\\
&-i \varepsilon^{def}{}_{b}{}^{c} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\psi_{a}{}^{i}\mathcal D^{b}\mathcal D^{a}(\varphi_{i})\Bigg[\frac{i}{L} E_{b}\\
&+\frac{\sqrt{2} i}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N}{L}\bar\psi_{a}{}^{i}\psi_{bi}\Bigg[\zeta T_{cd} \varepsilon^{abcd}{}_{e}\Big[-\frac{i}{L} E^{e}\\
&-\frac{\sqrt{2} i}{2} V^{e}\Big]\\
&+\zeta \widehat G_{cd} \varepsilon^{abcd}{}_{e}\Big[\frac{i}{4 L} E^{e}\\
&+\frac{\sqrt{2} i}{8} V^{e}\Big]\\
&+i E^{ab}\\
&+\frac{2 i N \zeta}{L} T^{ab}\\
&-\frac{i N \zeta}{2 L} \widehat G^{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\varphi^{j}\Bigg[\frac{1}{L^{3}} L_{j}{}^{k}\Big[\mathcal D_{b}(L_{ik})\Big[\frac{\zeta}{L} \mathcal D^{a}(L)\Big[\frac{3 i}{L} E^{b}\\
&+\frac{3 \sqrt{2} i}{2} V^{b}\Big]\\
&+\zeta T_{cd} \varepsilon^{abcd}{}_{e}\Big[-\frac{3 i}{L} E^{e}\\
&-\frac{3 \sqrt{2} i}{2} V^{e}\Big]\\
&+\zeta \widehat G_{cd} \varepsilon^{abcd}{}_{e}\Big[\frac{i}{2 L} E^{e}\\
&+\frac{\sqrt{2} i}{4} V^{e}\Big]\\
&+2 i E^{ab}\\
&+\frac{2 i N \zeta}{L} T^{ab}\\
&-\frac{i N \zeta}{L} \widehat G^{ab}\\
&-\frac{i \zeta}{L^{2}} E^{a} \mathcal D^{b}(L)\Big]\\
&+\mathcal D^{a}(L_{kl})\Big[L_{i}{}^{l}\Big[-i (\frac{4 D \zeta}{L} - 2 - \frac{N^{2} \zeta}{L^{3}})\\
&+\frac{i \zeta}{L^{3}} E^{b} E_{b}\\
&-\frac{8 i \zeta}{3 L} T^{bc} T_{bc}\\
&-\frac{i \zeta}{2 L^{3}} \mathcal D^{b}(L^{oz}) \mathcal D_{b}(L_{oz})\Big]\\
&+\frac{\zeta}{L}\Big[-i \Box^c(L_{i}{}^{l})\\
&+\frac{i}{L^{2}} E_{b} L^{ol} \mathcal D^{b}(L_{io})\Big]\Big]\\
&+\zeta\Big[\frac{1}{L} E_{b}\Big[\frac{1}{L^{2}} L_{i}{}^{l}\Big[-i E^{a} \mathcal D^{b}(L_{lk})\\
&-i \mathcal D^{a}(L^{o}{}_{k}) \mathcal D^{b}(L_{ol})\Big]\\
&-i \mathcal D^{a}\mathcal D^{b}(L_{ik})\\
&+i \mathcal D^{b}\mathcal D^{a}(L_{ik})\\
&-\frac{3 i}{L} \mathcal D^{a}(L_{ik}) \mathcal D^{b}(L)\Big]\\
&+\sqrt{2} V_{b}\Big[-\frac{i}{2} \mathcal D^{a}\mathcal D^{b}(L_{ik})\\
&+\frac{i}{2} \mathcal D^{b}\mathcal D^{a}(L_{ik})\\
&-\frac{3 i}{2 L} \mathcal D^{a}(L_{ik}) \mathcal D^{b}(L)\Big]\\
&+\frac{1}{L}\Big[i E^{a} \Box^c(L_{ik})\\
&-\frac{i}{L} \mathcal D^{a}(L^{l}{}_{k}) \mathcal D^{b}(L_{il}) \mathcal D_{b}(L)\Big]\Big]\Big]\\
&+L_{ij}\Big[\frac{1}{L^{3}} E_{b}\Big[\frac{\zeta}{L} \mathcal D^{a}(L)\Big[\frac{3 i}{L} E^{b}\\
&+\frac{3 \sqrt{2} i}{2} V^{b}\Big]\\
&+\frac{\sqrt{2} \zeta}{4} V_{c} \varepsilon^{abc}{}_{de}\Big[-6 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&-2 i E^{ba}\\
&-\frac{8 i N \zeta}{L} T^{ba}\\
&-\frac{i \zeta}{L} \mathcal D^{a}(E^{b})\\
&+\frac{i \zeta}{L} \mathcal D^{b}(E^{a})\\
&+\frac{2 i N \zeta}{L} \widehat G^{ba}\\
&-\frac{3 i \zeta}{L^{2}} E^{a} \mathcal D^{b}(L)\Big]\\
&+\frac{\sqrt{2} \zeta}{L^{3}} V_{b}\Big[-3 i N T^{ba}\\
&-\frac{i}{2} \mathcal D^{a}(E^{b})\\
&+\frac{i}{2} \mathcal D^{b}(E^{a})\\
&+\frac{i N}{2} \widehat G^{ba}\\
&-\frac{3 i}{2 L} E^{a} \mathcal D^{b}(L)\Big]\\
&+\frac{3 i N^{2} \zeta}{L^{5}} \mathcal D^{a}(L)\\
&-\frac{i N \zeta}{L^{4}} \mathcal D^{a}(N)\\
&-\frac{i \beta g^{2}}{4} C_{b} \widehat G^{ba}\Big]\\
&+\frac{\zeta}{L^{3}} E_{b}\Big[\mathcal D^{a}(L_{ij})\Big[-\frac{i}{L} E^{b}\\
&-\frac{\sqrt{2} i}{2} V^{b}\Big]\\
&+\frac{1}{2 L}\Big[3 i E^{a} \mathcal D^{b}(L_{ij})\\
&-2 i \mathcal D^{a}(L_{i}{}^{k}) \mathcal D^{b}(L_{jk})\\
&-2 i \mathcal D^{a}(L_{j}{}^{k}) \mathcal D^{b}(L_{ik})\Big]\Big]\\
&+\frac{\sqrt{2} \zeta}{2 L^{3}} V_{b}\Big[i E^{a} \mathcal D^{b}(L_{ij})\\
&-i \mathcal D^{a}(L_{i}{}^{k}) \mathcal D^{b}(L_{jk})\\
&-i \mathcal D^{a}(L_{j}{}^{k}) \mathcal D^{b}(L_{ik})\Big]\\
&-i (\frac{\beta g^{2}}{2} + \frac{N^{2} \zeta}{L^{4}}) \mathcal D^{a}(L_{ij})\\
&-\frac{i \beta g}{3} C_{b} \widehat R^{ba}{}_{ij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\varphi_{i}\Bigg[\frac{\zeta}{L^{2}} \mathcal D_{b}(L)\Big[T_{cd} \varepsilon^{abcd}{}_{e}\Big[-\frac{2 i}{L} E^{e}\\
&-\sqrt{2} i V^{e}\Big]\\
&+\frac{1}{L}\Big[L^{jk}\Big[-i \widehat R^{ba}{}_{jk}(V)\\
&+\frac{3 i}{L^{2}} \mathcal D^{a}(L^{l}{}_{k}) \mathcal D^{b}(L_{lj})\Big]\\
&+12 i N T^{ba}\\
&+i \mathcal D^{a}(E^{b})\\
&-2 i \mathcal D^{b}(E^{a})\\
&-i N \widehat G^{ba}\\
&+\frac{2 i}{L} E^{a} \mathcal D^{b}(L)\\
&-\frac{2 i}{L} E^{b} \mathcal D^{a}(L)\\
&-\frac{i}{2} E_{c} \varepsilon^{cdeba} \widehat G_{de}\Big]\Big]\\
&+\frac{\beta g}{24} C_{b}\Big[-12 i \mathcal D^{a}\mathcal D^{b}(\sigma)\\
&+12 i \mathcal D^{b}\mathcal D^{a}(\sigma)\\
&-14 i \mathcal D^{c}(\widehat H^{b}{}_{c}{}^{a})\\
&+13 i \mathcal D^{c}(\widehat G_{de}) \varepsilon^{b}{}_{c}{}^{dea}\Big]\\
&+\widehat G_{bc}\Big[\frac{\zeta}{L^{2}} L^{jk} \varepsilon^{abc}{}_{de}\Big[-\frac{i}{4} \widehat R^{de}{}_{jk}(V)\\
&+\frac{i}{4 L^{2}} \mathcal D^{d}(L_{lj}) \mathcal D^{e}(L^{l}{}_{k})\Big]\\
&+\varepsilon^{abc}{}_{de}\Big[-\frac{2 i N \zeta}{L^{2}} T^{de}\\
&-\frac{i \zeta}{2 L^{2}} \mathcal D^{d}(E^{e})\\
&-\frac{3 i \beta g}{32} \widehat G^{de}\Big]\\
&+\frac{i \beta g}{4} \widehat H^{bca}\Big]\\
&+\frac{1}{L} E^{a}\Big[-i (\frac{2 D \zeta}{L} - 1 - \frac{N^{2} \zeta}{2 L^{3}})\\
&-\frac{i \zeta}{L^{2}} \Box^c(L)\\
&+\frac{i \zeta}{2 L^{3}} E^{b} E_{b}\\
&-\frac{4 i \zeta}{3 L} T^{bc} T_{bc}\\
&-\frac{i \zeta}{4 L^{3}} \mathcal D^{b}(L^{jk}) \mathcal D_{b}(L_{jk})\Big]\\
&+\frac{\zeta}{L^{2}} L^{jk}\Big[-i \mathcal D^{b}(\widehat R^{a}{}_{bjk}(V))\\
&+\frac{i}{L^{2}} \Box^c(L^{l}{}_{k}) \mathcal D^{a}(L_{lj})\\
&-\frac{i}{L^{2}} \mathcal D^{b}\mathcal D^{a}(L^{l}{}_{k}) \mathcal D_{b}(L_{lj})\Big]\\
&+\frac{\zeta}{L} \mathcal D_{b}(T_{cd}) \varepsilon^{abcd}{}_{e}\Big[\frac{2 i}{L} E^{e}\\
&+\sqrt{2} i V^{e}\Big]\\
&+\frac{\zeta}{L^{2}} \mathcal D_{b}(N)\Big[-16 i T^{ba}\\
&+i \widehat G^{ba}\Big]\\
&+\varepsilon^{a}{}_{bcde}\Big[\frac{11 i \beta g}{72} \mathcal D^{b}(\widehat H^{cde})\\
&+\frac{10 i N \zeta}{L^{2}} T^{bc} T^{de}\Big]\\
&+\frac{i \zeta}{L^{2}} \Box^c(E^{a})\\
&-\frac{12 i N \zeta}{L^{2}} \mathcal D^{b}(T_{b}{}^{a})\\
&-i (\frac{5 \beta g}{12} - \frac{N \zeta}{L^{2}}) \mathcal D^{b}(\widehat G_{b}{}^{a})\\
&-\frac{i \zeta}{L^{2}} \mathcal D^{b}\mathcal D^{a}(E_{b})\\
&+\frac{i \zeta}{L^{3}} E_{b} \mathcal D^{b}\mathcal D^{a}(L)\\
&+\frac{i \zeta}{L^{3}} \mathcal D^{a}(L) \mathcal D^{b}(E_{b})\\
&-\frac{i \zeta}{L^{2}} \mathcal D^{b}(L^{jk}) \widehat R^{a}{}_{bjk}(V)\\
&-\frac{i \beta g}{96} \varepsilon^{bcdef} \widehat H_{bcd} \widehat H_{ef}{}^{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\psi_{a}{}^{i}\widehat R_{bci}(Q)\Bigg[C_{d}\Big[\frac{\beta}{864} \widehat H_{efg}\Big[2 i \varepsilon^{defga} \widehat G^{bc}\\
&+3 i \varepsilon^{defgc} \widehat G^{ab}\\
&+3 i \varepsilon^{efgac} \widehat G^{db}\\
&+7 i \varepsilon^{efgbc} \widehat G^{da}\Big]\\
&-\frac{i \alpha}{8} \widehat C^{bcda}\\
&+\frac{8 i \alpha}{3} T^{bc} T^{da}\\
&-\frac{i \beta}{24} \widehat G^{ac} \widehat G^{db}\\
&+\frac{i \beta}{144} \widehat G^{bc} \widehat G^{da}\\
&-\frac{7 i \beta}{72} \widehat H^{d}{}_{e}{}^{a} \widehat H^{ebc}\\
&+\frac{i \beta}{12} \widehat H^{d}{}_{e}{}^{b} \widehat H^{eac}\Big]\\
&+2 i \alpha \mathcal D^{b}(T^{ac})\\
&-\frac{i \beta}{16} \widehat G_{d}{}^{a} \widehat H^{dbc}\\
&-\frac{i \beta}{18} \widehat G_{d}{}^{b} \widehat H^{dac}\\
&+\frac{i \beta}{144} \varepsilon^{defgc} \widehat H_{def} \widehat H_{g}{}^{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{1152} L_{ij}\bar\psi_{a}{}^{i}\widehat R_{bc}{}^{j}(Q)\Bigg[22 i \widehat H^{abc}\\
&+92 i C^{b} \widehat G^{ac}\\
&-23 i \varepsilon^{deabc} \widehat G_{de}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{23 i \beta g}{288} C_{c} L_{ij} \widehat G^{cb}\bar\psi_{a}{}^{i}\widehat R_{b}{}^{aj}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{432}\bar\psi_{a}{}^{i}\widehat R_{b}{}^{a}{}_{i}(Q)\Bigg[-21 i \widehat G_{cd} \widehat H^{cdb}\\
&-8 i C^{b} \widehat H^{cde} \widehat H_{cde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 i N \zeta}{L^{4}} L_{ij}\bar\varphi^{i}\Box^c(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8}{L}\bar\varphi^{i}\chi^{j}\Bigg[L_{ij}\Big[\frac{4 \zeta}{L} T_{ab}\Big[8 i T^{ab}\\
&-i \widehat G^{ab}\Big]\\
&-i (-4 + \frac{N \zeta (g + \frac{8 N}{L^{2}})}{L})\\
&+\frac{4 i \zeta}{L^{2}} \Box^c(L)\\
&-\frac{4 i \zeta}{L^{3}} \mathcal D^{a}(L^{kl}) \mathcal D_{a}(L_{kl})\Big]\\
&+\frac{2 \zeta}{L}\Big[\frac{1}{L^{2}} L_{j}{}^{k}\Big[L_{i}{}^{l}\Big[i \Box^c(L_{lk})\\
&-\frac{2 i}{L} \mathcal D^{a}(L_{lk}) \mathcal D_{a}(L)\Big]\\
&+3 i E_{a} \mathcal D^{a}(L_{ik})\\
&-i \mathcal D^{a}(L^{l}{}_{k}) \mathcal D_{a}(L_{li})\Big]\\
&+\frac{1}{L^{2}} \mathcal D_{a}(L_{jk})\Big[3 i E^{a} L^{k}{}_{i}\\
&+i L^{l}{}_{i} \mathcal D^{a}(L^{k}{}_{l})\Big]\\
&+2\Big[-i \Box^c(L_{ij})\\
&+\frac{i}{L} \mathcal D^{a}(L_{ij}) \mathcal D_{a}(L)\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 \zeta}{L^{2}}\bar\varphi^{i}\chi_{i}\Bigg[-i \mathcal D^{a}(E_{a})\\
&+\frac{2 i}{L} E_{a} \mathcal D^{a}(L)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{4 i \zeta}{L^{2}} T_{ab}\bar\varphi^{i}\gamma^{ab}\Box^c(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L^{2}}\bar\varphi^{i}\gamma^{ab}\chi^{j}\Bigg[\frac{1}{L^{2}} L_{j}{}^{k}\Big[L_{i}{}^{l}\Big[\mathcal D_{c}(L_{kl}) \varepsilon_{ab}{}^{c}{}_{de}\Big[8 i T^{de}\\
&-i \widehat G^{de}\Big]\\
&+4\Big[-i \mathcal D_{a}\mathcal D_{b}(L_{lk})\\
&+\frac{2 i}{L} \mathcal D_{a}(L) \mathcal D_{b}(L_{lk})\Big]\Big]\\
&+4\Big[i E_{a} \mathcal D_{b}(L_{ik})\\
&+i \mathcal D_{a}(L_{il}) \mathcal D_{b}(L^{l}{}_{k})\Big]\Big]\\
&+4\Big[\frac{1}{L^{2}} L_{i}{}^{k}\Big[i E_{a} \mathcal D_{b}(L_{jk})\\
&-i \mathcal D_{a}(L_{jl}) \mathcal D_{b}(L^{l}{}_{k})\Big]\\
&+L_{ij}\Big[4 i T^{c}{}_{b} \widehat G_{ca}\\
&+i \mathcal D^{c}(T_{de}) \varepsilon_{c}{}^{de}{}_{ab}\Big]\\
&-i T_{cd} \mathcal D^{e}(L_{ij}) \varepsilon^{cd}{}_{abe}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+2 \zeta\bar\varphi^{i}\gamma^{ab}\chi_{i}\Bigg[\frac{1}{L^{2}} E_{c} \varepsilon_{ab}{}^{c}{}_{de}\Big[-8 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&+2\Big[4 i (g + \frac{6 N}{L^{2}}) T_{ab}\\
&+\frac{2 i}{L^{2}} \mathcal D_{a}(E_{b})\\
&+\frac{i N}{L^{2}} \widehat G_{ab}\\
&+\frac{4 i}{L^{3}} E_{a} \mathcal D_{b}(L)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{16 i \zeta}{L^{2}} L_{ij} T_{de} \varepsilon^{de}{}_{abc}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{2}}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}(\varphi^{j})\Bigg[L_{ij}\Big[\frac{2}{L^{2}} E_{a}\Big[16 i T_{bc}\\
&-i \widehat G_{bc}\Big]\\
&+\varepsilon_{abcde}\Big[2 i g T^{de}\\
&+\frac{i}{L^{2}} \mathcal D^{d}(E^{e})\\
&+\frac{i N}{2 L^{2}} \widehat G^{de}\\
&+\frac{2 i}{L^{3}} E^{d} \mathcal D^{e}(L)\Big]\\
&-\frac{i}{L^{2}} E_{c} \widehat G_{ab}\Big]\\
&+\frac{1}{L^{2}}\Big[L_{i}{}^{k}\Big[\frac{1}{L^{2}} \mathcal D_{d}(L_{kl}) \varepsilon_{abc}{}^{d}{}_{e}\Big[-2 i E^{e} L_{j}{}^{l}\\
&-i L_{j}{}^{o} \mathcal D^{e}(L^{l}{}_{o})\Big]\\
&+2 \mathcal D_{b}(L_{jk})\Big[-12 i T_{ac}\\
&+i \widehat G_{ac}\Big]\\
&+\varepsilon_{abcde}\Big[i \mathcal D^{d}\mathcal D^{e}(L_{jk})\\
&-\frac{2 i}{L} \mathcal D^{d}(L) \mathcal D^{e}(L_{jk})\Big]\Big]\\
&+\varepsilon_{abcde}\Big[-i E^{d} \mathcal D^{e}(L_{ij})\\
&-i \mathcal D^{d}(L_{ik}) \mathcal D^{e}(L_{j}{}^{k})\Big]\\
&-8 i L_{j}{}^{k} T_{ac} \mathcal D_{b}(L_{ik})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{2}}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}(\varphi_{i})\Bigg[T_{de}\Big[\varepsilon_{ab}{}^{de}{}_{f}\Big[16 i T^{f}{}_{c}\\
&-i \widehat G^{f}{}_{c}\Big]\\
&-2 i \varepsilon^{fe}{}_{abc} \widehat G^{d}{}_{f}\Big]\\
&+4 i \mathcal D_{a}(T_{bc})\\
&+2 i \mathcal D_{c}(T_{ab})\\
&-i T_{fc} \varepsilon^{def}{}_{ab} \widehat G_{de}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{153 i \beta g}{1024} \varepsilon_{abc}{}^{de}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{4}} \varepsilon_{abcde}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}\mathcal D^{d}(\varphi^{j})\Bigg[i E^{e} L_{ij}\\
&+i L_{i}{}^{k} \mathcal D^{e}(L_{jk})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{8 i \zeta}{L^{2}} T_{ac}\bar\varphi^{i}\gamma^{ab}\mathcal D^{c}\mathcal D_{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 i \zeta}{L^{4}} L_{i}{}^{k} L_{j}{}^{l} \mathcal D_{b}(L_{kl})\bar\varphi^{i}\gamma^{ab}\mathcal D_{a}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{4}}\bar\varphi^{i}\gamma^{ab}\mathcal D_{a}(\varphi^{j})\Bigg[i N \mathcal D_{b}(L_{ij})\\
&-i (g + \frac{2 N}{L^{2}}) L_{i}{}^{k} L_{j}{}^{l} \mathcal D_{b}(L_{kl})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 i N \zeta}{L^{4}} L_{ij}\bar\varphi^{i}\gamma^{ab}\mathcal D_{a}\mathcal D_{b}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i \zeta}{L^{2}} E_{a}\bar\varphi^{i}\gamma^{ab}\mathcal D_{b}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{4}}\bar\varphi^{i}\gamma^{ab}\mathcal D_{b}(\varphi^{j})\Bigg[L_{ij}\Big[\frac{2 i N}{L} \mathcal D_{a}(L)\\
&-i \mathcal D_{a}(N)\\
&-i E_{c} \widehat G^{c}{}_{a}\Big]\\
&+\mathcal D_{c}(L_{jk}) L_{i}{}^{k}\Big[-4 i T_{a}{}^{c}\\
&+i \widehat G_{a}{}^{c}\Big]\\
&+4 i L_{j}{}^{k} T_{ac} \mathcal D^{c}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\gamma^{ab}\mathcal D_{b}(\varphi_{i})\Bigg[\frac{5 i \beta g^{2}}{6} C_{a}\\
&-\frac{i g \zeta}{L^{2}} E_{a}\\
&-\frac{8 i \zeta}{L^{2}} \mathcal D^{c}(T_{ca})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i \zeta}{L^{2}} T_{ac}\bar\varphi^{i}\gamma^{ab}\mathcal D_{b}\mathcal D^{c}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{4}}\bar\varphi^{i}\gamma^{ab}\mathcal D_{c}(\varphi^{j})\Bigg[\mathcal D^{c}(L_{jk}) L_{i}{}^{k}\Big[4 i T_{ab}\\
&-i \widehat G_{ab}\Big]\\
&-4 i L_{j}{}^{k} T_{ab} \mathcal D^{c}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 i N \zeta}{L^{4}} L_{i}{}^{k} \mathcal D_{b}(L_{jk})\bar\varphi^{i}\gamma^{ab}\phi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L} T_{ac}\bar\varphi^{i}\gamma^{ab}\phi_{bi}\Bigg[-\frac{2 i}{L} E^{c}\\
&-\sqrt{2} i V^{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{N \zeta}{L^{3}} L_{ij}\bar\varphi^{i}\gamma^{ab}\phi_{b}{}^{j}\Bigg[\frac{4 i}{L} E_{a}\\
&+\frac{\sqrt{2} i}{2} V_{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\varphi^{i}\gamma^{ab}\phi_{ci}\Bigg[-\frac{4 i}{L} E_{a} T_{b}{}^{c}\\
&+2 \sqrt{2} i T_{a}{}^{c} V_{b}\\
&+\frac{3 i N}{L} T_{de} \varepsilon^{de}{}_{ab}{}^{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\gamma^{ab}\phi_{c}{}^{j}\Bigg[\mathcal D_{d}(L_{jk}) L_{i}{}^{k} \varepsilon_{ab}{}^{cd}{}_{e}\Big[\frac{i}{2 L} E^{e}\\
&+\frac{\sqrt{2} i}{4} V^{e}\Big]\\
&+\frac{\sqrt{2} i}{4} E_{d} L_{ij} V_{e} \varepsilon^{de}{}_{ab}{}^{c}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{4}}\bar\varphi^{i}\gamma^{ab}\varphi^{j}\Bigg[L_{j}{}^{k}\Big[2 \mathcal D_{c}(L_{ik})\Big[T_{de}\Big[\varepsilon_{ab}{}^{de}{}_{f}\Big[16 i T^{fc}\\
&-i \widehat G^{fc}\Big]\\
&-2 i \varepsilon^{fe}{}_{ab}{}^{c} \widehat G^{d}{}_{f}\Big]\\
&+2 i \mathcal D^{c}(T_{ab})\\
&+4 i \mathcal D_{a}(T_{b}{}^{c})\\
&+\frac{4 i}{L} T_{ab} \mathcal D^{c}(L)\\
&+\frac{8 i}{L} T_{b}{}^{c} \mathcal D_{a}(L)\\
&-i T_{d}{}^{c} \varepsilon^{efd}{}_{ab} \widehat G_{ef}\Big]\\
&+\frac{1}{L^{2}} \mathcal D_{c}(L_{lo}) L_{i}{}^{o}\Big[\frac{1}{2} \mathcal D^{c}(L_{k}{}^{l})\Big[8 i T_{ab}\\
&-i \widehat G_{ab}\Big]\\
&+2 \mathcal D_{b}(L_{k}{}^{l})\Big[-8 i T_{a}{}^{c}\\
&+i \widehat G_{a}{}^{c}\Big]\\
&+i \mathcal D^{d}\mathcal D^{e}(L^{l}{}_{k}) \varepsilon_{ab}{}^{c}{}_{de}\Big]\\
&+\mathcal D_{b}(L_{ik})\Big[-i g E_{a}\\
&-8 i \mathcal D^{c}(T_{ca})\\
&-\frac{16 i}{L} T_{ca} \mathcal D^{c}(L)\Big]\\
&+\frac{1}{L^{2}} \mathcal D_{c}(L_{k}{}^{l}) \varepsilon_{ab}{}^{c}{}_{de}\Big[-2 i E^{d} \mathcal D^{e}(L_{il})\\
&-i \mathcal D^{d}(L_{io}) \mathcal D^{e}(L^{o}{}_{l})\Big]\\
&+8 T_{ac}\Big[-i \mathcal D^{c}\mathcal D_{b}(L_{ik})\\
&+i \mathcal D_{b}\mathcal D^{c}(L_{ik})\Big]\\
&-4 i T_{ab} \Box^c(L_{ik})\\
&-\frac{4 i N}{L^{2}} \mathcal D_{a}(L_{il}) \mathcal D_{b}(L^{l}{}_{k})\\
&-\frac{i g}{L^{2}} L^{lo} L_{i}{}^{z} \mathcal D_{a}(L_{zl}) \mathcal D_{b}(L_{ko})\Big]\\
&-4 i T_{ab} \mathcal D^{c}(L_{j}{}^{k}) \mathcal D_{c}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\gamma^{ab}\varphi_{i}\Bigg[\frac{\zeta}{L^{2}} T_{cd}\Big[\frac{4}{3} T^{cd}\Big[80 i T_{ab}\\
&-3 i \widehat G_{ab}\Big]\\
&+32 T_{b}{}^{d}\Big[4 i T^{c}{}_{a}\\
&-i \widehat G^{c}{}_{a}\Big]\\
&+8 \varepsilon_{ab}{}^{d}{}_{ef}\Big[i \mathcal D^{c}(T^{ef})\\
&-2 i \mathcal D^{e}(T^{cf})\Big]\\
&+\varepsilon_{ab}{}^{cd}{}_{e}\Big[-i (g - \frac{2 N}{L^{2}}) E^{e}\\
&-8 i \mathcal D^{f}(T_{f}{}^{e})\Big]\\
&-8 i T_{ab} \widehat G^{cd}\Big]\\
&+\frac{\zeta}{L^{4}} E_{c}\Big[\frac{1}{4} E^{c}\Big[-24 i T_{ab}\\
&+i \widehat G_{ab}\Big]\\
&+E_{a}\Big[8 i T^{c}{}_{b}\\
&-i \widehat G^{c}{}_{b}\Big]\\
&+\varepsilon_{ab}{}^{c}{}_{de}\Big[-\frac{i}{2} \mathcal D^{d}(E^{e})\\
&-\frac{i N}{4} \widehat G^{de}\Big]\Big]\\
&+\frac{2}{L} T_{ab}\Big[-i (- \frac{8 D \zeta}{L} - 2 + \frac{N \zeta (3 g + \frac{N}{L^{2}})}{L})\\
&+\frac{2 i \zeta}{L^{2}} \Box^c(L)\\
&-\frac{i \zeta}{L^{3}} \mathcal D^{c}(L^{jk}) \mathcal D_{c}(L_{jk})\Big]\\
&-\frac{i N \zeta}{L^{4}} \mathcal D_{a}(E_{b})\\
&-\frac{i (3 \beta g^{2} + \frac{2 N^{2} \zeta}{L^{4}})}{8} \widehat G_{ab}\\
&-\frac{i \zeta}{L^{4}} E_{a} \mathcal D_{b}(N)\\
&-\frac{i \beta g^{2}}{16} \varepsilon^{cde}{}_{ab} \widehat H_{cde}\\
&-\frac{16 i \zeta}{L^{2}} T^{c}{}_{a} T^{d}{}_{b} \widehat G_{cd}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{36864}\bar\varphi^{i}\gamma^{ab}\widehat R_{cdi}(Q)\Bigg[C_{e}\Big[4142 i \varepsilon^{ef}{}_{ab}{}^{d} \widehat G_{f}{}^{c}\\
&-8298 i \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{fa}\\
&+2645 i \varepsilon^{f}{}_{ab}{}^{cd} \widehat G^{e}{}_{f}\Big]\\
&+2\Big[C^{c}\Big[1886 i \widehat H_{ab}{}^{d}\\
&+719 i \varepsilon^{ef}{}_{ab}{}^{d} \widehat G_{ef}\Big]\\
&+8 C_{a}\Big[-1208 i \widehat H_{b}{}^{cd}\\
&+45 i \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{ef}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{499 i \beta g^{2}}{2304} C_{e} L_{ij} \varepsilon^{e}{}_{ab}{}^{cd}\bar\varphi^{i}\gamma^{ab}\widehat R_{cd}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\gamma^{a}\Box^c(\varphi^{j})\Bigg[L_{ij}\Big[-\frac{4}{L} E_{a}\\
&-\sqrt{2} V_{a}\Big]\\
&-\frac{2}{L} L_{i}{}^{k} \mathcal D_{a}(L_{jk})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 \zeta}{L^{2}}\bar\varphi^{i}\gamma^{a}\chi^{j}\Bigg[L_{ij}\Big[2 T_{bc} \varepsilon_{a}{}^{bc}{}_{de}\Big[8 T^{de}\\
&-\widehat G^{de}\Big]\\
&+\big(g + \frac{8 N}{L^{2}}\big) E_{a}\\
&+8 \mathcal D^{b}(T_{ba})\Big]\\
&+\frac{2}{L^{2}} L_{j}{}^{k}\Big[\mathcal D_{b}(L_{kl}) L_{i}{}^{l}\Big[8 T_{a}{}^{b}\\
&-\widehat G_{a}{}^{b}\Big]\\
&+N \mathcal D_{a}(L_{ik})\Big]\\
&+\big(g + \frac{10 N}{L^{2}}\big) L_{i}{}^{k} \mathcal D_{a}(L_{jk})\\
&+8 T_{ab} \mathcal D^{b}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 \zeta}{L^{2}}\bar\varphi^{i}\gamma^{a}\chi_{i}\Bigg[E_{b}\Big[8 T^{b}{}_{a}\\
&-\widehat G^{b}{}_{a}\Big]\\
&+\frac{2 N}{L} \mathcal D_{a}(L)\\
&-\mathcal D_{a}(N)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{64 \zeta}{L^{2}} L_{ij} T_{ab}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{1}{L^{2}}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}(\varphi^{j})\Bigg[L_{ij}\Big[\frac{2 \zeta}{L^{2}} \mathcal D_{b}(L)\Big[\frac{4}{L} E_{a}\\
&+3 \sqrt{2} V_{a}\Big]\\
&+\frac{\zeta}{L^{2}} \mathcal D_{a}(L)\Big[-\frac{2}{L} E_{b}\\
&-3 \sqrt{2} V_{b}\Big]\\
&+\frac{\zeta}{L} \widehat G_{cd} \varepsilon_{ab}{}^{cd}{}_{e}\Big[-\frac{2}{L} E^{e}\\
&-\frac{\sqrt{2}}{2} V^{e}\Big]\\
&+2\Big[-\frac{2}{L} E_{ab}\\
&-4 \zeta (g - \frac{6 N}{L^{2}}) T_{ab}\\
&-\frac{\zeta}{L^{2}} \mathcal D_{a}(E_{b})\\
&+\frac{\zeta}{L^{2}} \mathcal D_{b}(E_{a})\\
&-\frac{2 N \zeta}{L^{2}} \widehat G_{ab}\\
&+\frac{4 \zeta}{L^{2}} E_{c} T_{de} \varepsilon^{cde}{}_{ab}\Big]\Big]\\
&+\frac{\zeta}{L}\Big[\frac{1}{L} L_{i}{}^{k}\Big[\mathcal D_{c}(L_{jk}) \varepsilon_{ab}{}^{c}{}_{de}\Big[4 T^{de}\\
&-\widehat G^{de}\Big]\\
&-\frac{4}{L} \mathcal D_{a}(L_{jk}) \mathcal D_{b}(L)\Big]\\
&+\sqrt{2} V_{b} \mathcal D_{a}(L_{ij})\\
&+\frac{4}{L} L_{j}{}^{k} T_{cd} \mathcal D^{e}(L_{ik}) \varepsilon^{cd}{}_{abe}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{2}}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}(\varphi_{i})\Bigg[4 T_{bc}\Big[-8 T^{c}{}_{a}\\
&-\widehat G^{c}{}_{a}\Big]\\
&+\frac{1}{L^{2}} E_{a} E_{b}\\
&-4 T^{c}{}_{a} \widehat G_{cb}\\
&+2 \mathcal D^{c}(T_{de}) \varepsilon_{c}{}^{de}{}_{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{67 \beta g}{256} C_{e} \varepsilon^{e}{}_{ab}{}^{cd}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}(\widehat R_{cdi}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L^{2}} T_{de} \varepsilon^{de}{}_{abc}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}\mathcal D^{c}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{2 \zeta}{L^{4}} E_{b} L_{ij}\bar\varphi^{i}\gamma^{a}\mathcal D^{b}\mathcal D_{a}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 N \zeta}{L^{2}}\bar\varphi^{i}\gamma^{a}\mathcal D_{a}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\gamma^{a}\mathcal D_{a}(\varphi^{j})\Bigg[\frac{2}{L} L_{i}{}^{k}\Big[\frac{1}{L^{2}} \mathcal D_{b}(L_{kl})\Big[-2 E^{b} L_{j}{}^{l}\\
&+L_{j}{}^{o} \mathcal D^{b}(L^{l}{}_{o})\Big]\\
&+3 \Box^c(L_{jk})\\
&-\frac{4}{L} \mathcal D^{b}(L_{jk}) \mathcal D_{b}(L)\Big]\\
&+\frac{1}{L} L_{ij}\Big[\mathcal D_{b}(L)\Big[-\frac{10}{L} E^{b}\\
&-3 \sqrt{2} V^{b}\Big]\\
&+2 \mathcal D^{b}(E_{b})\Big]\\
&+\mathcal D_{b}(L_{ij})\Big[\frac{6}{L} E^{b}\\
&+\sqrt{2} V^{b}\Big]\\
&-\frac{2}{L} \mathcal D^{b}(L_{j}{}^{k}) \mathcal D_{b}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\gamma^{a}\mathcal D_{a}(\varphi_{i})\Bigg[\frac{4 \zeta}{3 L^{2}} T_{bc}\Big[16 T^{bc}\\
&-3 \widehat G^{bc}\Big]\\
&+\big(\frac{8 D \zeta}{L^{2}} + \frac{\beta g^{2}}{6} + \frac{2 - \frac{3 N \zeta (g + \frac{N}{L^{2}})}{L}}{L}\big)\\
&-\frac{3 \zeta}{L^{4}} E^{b} E_{b}\\
&+\frac{\zeta}{L^{4}} \mathcal D^{b}(L^{jk}) \mathcal D_{b}(L_{jk})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}} L_{ij}\bar\varphi^{i}\gamma^{a}\mathcal D_{a}\mathcal D^{b}(\varphi^{j})\Bigg[\frac{4}{L} E_{b}\\
&+\sqrt{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{4}} L_{i}{}^{k} \mathcal D^{b}(L_{jk})\bar\varphi^{i}\gamma^{a}\mathcal D_{a}\mathcal D_{b}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{3}}\bar\varphi^{i}\gamma^{a}\mathcal D_{b}(\varphi^{j})\Bigg[\frac{1}{L} L_{i}{}^{k}\Big[\frac{1}{L^{2}} L_{j}{}^{l}\Big[\mathcal D^{b}(L^{o}{}_{k}) \mathcal D_{a}(L_{ol})\\
&-\mathcal D^{b}(L^{o}{}_{l}) \mathcal D_{a}(L_{ok})\Big]\\
&+\mathcal D^{b}\mathcal D_{a}(L_{jk})\\
&-\mathcal D_{a}\mathcal D^{b}(L_{jk})\\
&+\frac{2}{L} \mathcal D^{b}(L_{jk}) \mathcal D_{a}(L)\Big]\\
&+\mathcal D^{b}(L_{ij})\Big[-\frac{1}{L} E_{a}\\
&-\sqrt{2} V_{a}\Big]\\
&+\frac{1}{L}\Big[\mathcal D^{b}(L_{i}{}^{k}) \mathcal D_{a}(L_{jk})\\
&+\mathcal D^{b}(L_{j}{}^{k}) \mathcal D_{a}(L_{ik})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{2 \zeta}{L^{4}} L_{i}{}^{k} \mathcal D^{b}(L_{jk})\bar\varphi^{i}\gamma^{a}\mathcal D_{b}\mathcal D_{a}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\gamma^{a}\phi_{a}{}^{j}\Bigg[L_{ij}\Big[E_{b}\Big[-\frac{1}{L} E^{b}\\
&-\frac{\sqrt{2}}{2} V^{b}\Big]\\
&+\frac{3 N^{2}}{L}\Big]\\
&+\mathcal D_{b}(L_{jk}) L_{i}{}^{k}\Big[-\frac{1}{L} E^{b}\\
&-\frac{\sqrt{2}}{2} V^{b}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\bar\varphi^{i}\gamma^{a}\phi_{bi}\Bigg[T_{cd} \varepsilon_{a}{}^{bcd}{}_{e}\Big[-\frac{2}{L} E^{e}\\
&-\sqrt{2} V^{e}\Big]\\
&-\frac{12 N}{L} T_{a}{}^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\gamma^{a}\phi_{b}{}^{j}\Bigg[\mathcal D^{b}(L_{jk}) L_{i}{}^{k}\Big[\frac{1}{L} E_{a}\\
&+\frac{\sqrt{2}}{2} V_{a}\Big]\\
&+L_{ij} E^{b}\Big[\frac{1}{L} E_{a}\\
&+\frac{\sqrt{2}}{2} V_{a}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{1}{L^{2}}\bar\varphi^{i}\gamma^{a}\varphi^{j}\Bigg[L_{ij}\Big[\frac{1}{L^{2}} \mathcal D_{b}(L)\Big[\frac{2 \zeta}{L} \mathcal D^{b}(L)\Big[-\frac{7}{L} E_{a}\\
&-3 \sqrt{2} V_{a}\Big]\\
&+\frac{2 \zeta}{L} \mathcal D_{a}(L)\Big[\frac{7}{L} E^{b}\\
&+3 \sqrt{2} V^{b}\Big]\\
&+\frac{\zeta}{L} L^{kl}\Big[\widehat R^{b}{}_{akl}(V)\\
&-\frac{9}{L^{2}} \mathcal D^{b}(L_{ok}) \mathcal D_{a}(L^{o}{}_{l})\Big]\\
&+\zeta \widehat G_{cd} \varepsilon_{a}{}^{bcd}{}_{e}\Big[\frac{1}{L} E^{e}\\
&+\frac{3 \sqrt{2}}{4} V^{e}\Big]\\
&-6 E^{b}{}_{a}\\
&+\frac{16 N \zeta}{L} T^{b}{}_{a}\\
&+\frac{2 \zeta}{L} \mathcal D^{b}(E_{a})\\
&-\frac{\zeta}{L} \mathcal D_{a}(E^{b})\\
&-\frac{2 N \zeta}{L} \widehat G^{b}{}_{a}\\
&+\frac{8 \zeta}{L} E_{c} T_{de} \varepsilon^{cbde}{}_{a}\Big]\\
&+\zeta\Big[\frac{1}{L^{2}} E_{b}\Big[\frac{3}{L^{2}} \mathcal D^{b}(L_{kl})\Big[-\mathcal D_{a}(L^{kl})\\
&+\frac{2}{L^{2}} L^{ko} L^{lz} \mathcal D_{a}(L_{oz})\Big]\\
&-\frac{1}{L} \mathcal D^{b}\mathcal D_{a}(L)\\
&-\frac{3}{L} \mathcal D_{a}\mathcal D^{b}(L)\\
&-\frac{4}{L^{2}} E^{b} E_{a}\\
&-8 T^{bc} \widehat G_{ca}\\
&+8 T^{c}{}_{a} \widehat G^{b}{}_{c}\\
&+4 \mathcal D^{c}(T_{de}) \varepsilon^{b}{}_{c}{}^{de}{}_{a}\Big]\\
&+T_{bc}\Big[\frac{4}{3 L^{2}} E_{a}\Big[32 T^{bc}\\
&-3 \widehat G^{bc}\Big]\\
&+2 \varepsilon_{a}{}^{bc}{}_{de}\Big[2 (g - \frac{4 N}{L^{2}}) T^{de}\\
&+\frac{2}{L^{2}} \mathcal D^{d}(E^{e})\\
&+\frac{N}{L^{2}} \widehat G^{de}\Big]\Big]\\
&+\frac{1}{L^{2}}\Big[L^{kl}\Big[\frac{1}{4 L^{2}} \mathcal D_{b}(L_{ko})\Big[4 \mathcal D^{b}\mathcal D_{a}(L^{o}{}_{l})\\
&-\mathcal D^{c}(L^{o}{}_{l}) \varepsilon^{de}{}_{a}{}^{b}{}_{c} \widehat G_{de}\Big]\\
&+\mathcal D^{b}(\widehat R_{abkl}(V))\\
&-\frac{7}{L^{2}} \Box^c(L^{o}{}_{l}) \mathcal D_{a}(L_{ok})\\
&+\frac{1}{4} \varepsilon^{bc}{}_{ade} \widehat G_{bc} \widehat R^{de}{}_{kl}(V)\Big]\\
&+E_{a}\Big[-\big(- 16 D + N (5 g + \frac{4 N}{L^{2}})\big)\\
&+\frac{10}{L} \Box^c(L)\\
&-\frac{4}{L^{2}} \mathcal D^{b}(L^{kl}) \mathcal D_{b}(L_{kl})\Big]\\
&+\mathcal D_{b}(N)\Big[24 T^{b}{}_{a}\\
&-\widehat G^{b}{}_{a}\Big]\\
&-\Box^c(E_{a})\\
&+8 N \mathcal D^{b}(T_{ba})\\
&-N \mathcal D^{b}(\widehat G_{ba})\\
&+\mathcal D^{b}\mathcal D_{a}(E_{b})\\
&+\frac{3 \sqrt{2}}{2} V_{a} \Box^c(L)\\
&-\frac{3 \sqrt{2}}{2} V_{b} \mathcal D_{a}\mathcal D^{b}(L)\\
&-\frac{1}{L} \mathcal D^{b}(E_{b}) \mathcal D_{a}(L)\\
&+\mathcal D^{b}(L^{kl}) \widehat R_{abkl}(V)\\
&+\frac{1}{2} \mathcal D^{b}(E_{c}) \varepsilon_{b}{}^{cde}{}_{a} \widehat G_{de}\Big]\Big]\Big]\\
&+\frac{1}{L}\Big[L_{j}{}^{k}\Big[\frac{\zeta}{L} L_{i}{}^{l}\Big[\mathcal D_{b}(L_{kl})\Big[\frac{1}{L^{2}} E_{c} \varepsilon_{a}{}^{bc}{}_{de}\Big[-8 T^{de}\\
&+\widehat G^{de}\Big]\\
&+2\Big[4 (g - \frac{2 N}{L^{2}}) T_{a}{}^{b}\\
&-\frac{1}{L^{2}} \mathcal D^{b}(E_{a})\\
&+\frac{1}{L^{2}} \mathcal D_{a}(E^{b})\\
&+\frac{N}{L^{2}} \widehat G_{a}{}^{b}\Big]\Big]\\
&+\frac{1}{2 L^{2}}\Big[\mathcal D_{b}(L_{lo})\Big[\mathcal D_{c}(L_{k}{}^{o}) \varepsilon_{a}{}^{bc}{}_{de}\Big[-8 T^{de}\\
&+\widehat G^{de}\Big]\\
&+4\Big[-\mathcal D^{b}\mathcal D_{a}(L^{o}{}_{k})\\
&+\mathcal D_{a}\mathcal D^{b}(L^{o}{}_{k})\Big]\Big]\\
&+4\Big[E_{b}\Big[\mathcal D^{b}\mathcal D_{a}(L_{lk})\\
&-\mathcal D_{a}\mathcal D^{b}(L_{lk})\Big]\\
&+E_{a} \Box^c(L_{lk})\\
&-\Box^c(L^{o}{}_{k}) \mathcal D_{a}(L_{ol})\\
&-\mathcal D^{b}(E_{b}) \mathcal D_{a}(L_{lk})\Big]\Big]\Big]\\
&+\frac{4 \zeta}{L} \mathcal D_{b}(L_{ik})\Big[\varepsilon_{a}{}^{b}{}_{cde}\Big[\mathcal D^{c}(T^{de})\\
&+\frac{2}{L} T^{de} \mathcal D^{c}(L)\Big]\\
&+2\Big[\frac{1}{L^{2}} E^{b} E_{a}\\
&+T^{cb} \widehat G_{ca}\\
&-T^{c}{}_{a} \widehat G_{c}{}^{b}\Big]\Big]\\
&+\mathcal D_{a}(L_{ik})\Big[\frac{4 \zeta}{3 L} T_{bc}\Big[28 T^{bc}\\
&-3 \widehat G^{bc}\Big]\\
&-\big(- \frac{8 D \zeta}{L} - 2 + \frac{N \zeta (3 g + \frac{4 N}{L^{2}})}{L}\big)\\
&-\frac{4 \zeta}{L^{3}} E^{b} E_{b}\\
&+\frac{\zeta}{L^{3}} \mathcal D^{b}(L^{lo}) \mathcal D_{b}(L_{lo})\Big]\\
&+\frac{2 \zeta}{L}\Big[\frac{1}{L^{2}} \mathcal D_{b}(L_{k}{}^{l})\Big[\mathcal D^{b}(L^{o}{}_{l}) \mathcal D_{a}(L_{io})\\
&+\mathcal D^{b}(L_{i}{}^{o}) \mathcal D_{a}(L_{ol})\Big]\\
&+\frac{1}{L^{2}} E_{b} \mathcal D^{b}(L_{lk}) \mathcal D_{a}(L_{i}{}^{l})\\
&+2 T_{bc} \mathcal D^{d}\mathcal D^{e}(L_{ik}) \varepsilon^{bc}{}_{ade}\\
&+\frac{1}{L^{2}} \mathcal D^{b}(L^{lo}) \mathcal D_{a}(L_{lk}) \mathcal D_{b}(L_{io})\Big]\Big]\\
&+\mathcal D_{b}(L_{ij})\Big[\frac{\zeta}{L} \mathcal D^{b}(L)\Big[\frac{8}{L} E_{a}\\
&+3 \sqrt{2} V_{a}\Big]\\
&+\frac{\zeta}{L} \mathcal D_{a}(L)\Big[-\frac{3}{L} E^{b}\\
&-\frac{3 \sqrt{2}}{2} V^{b}\Big]\\
&+\zeta \widehat G_{cd} \varepsilon_{a}{}^{bcd}{}_{e}\Big[-\frac{1}{2 L} E^{e}\\
&-\frac{\sqrt{2}}{4} V^{e}\Big]\\
&-2 E_{a}{}^{b}\\
&+\frac{8 N \zeta}{L} T_{a}{}^{b}\\
&-\frac{N \zeta}{L} \widehat G_{a}{}^{b}\\
&+\frac{4 \zeta}{L} E_{c} T_{de} \varepsilon^{cde}{}_{a}{}^{b}\Big]\\
&+\zeta\Big[\frac{2}{L} \mathcal D_{b}(L_{ik})\Big[\frac{1}{L} \mathcal D^{b}(L) \mathcal D_{a}(L_{j}{}^{k})\\
&-\frac{1}{L^{2}} E^{b} L^{kl} \mathcal D_{a}(L_{jl})\\
&-2 T_{cd} \mathcal D^{e}(L_{j}{}^{k}) \varepsilon^{cd}{}_{a}{}^{b}{}_{e}\Big]\\
&+\Box^c(L_{ij})\Big[-\frac{3}{L} E_{a}\\
&-\frac{\sqrt{2}}{2} V_{a}\Big]\\
&+\mathcal D_{a}\mathcal D_{b}(L_{ij})\Big[\frac{1}{L} E^{b}\\
&+\frac{\sqrt{2}}{2} V^{b}\Big]\\
&+\frac{1}{L}\Big[\mathcal D_{a}(L_{ij}) \mathcal D_{b}(L)\Big[-\frac{3}{L} E^{b}\\
&-\frac{3 \sqrt{2}}{2} V^{b}\Big]\\
&+2 \Box^c(L_{j}{}^{k}) \mathcal D_{a}(L_{ik})\Big]\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{55296}\bar\varphi^{i}\gamma^{a}\widehat R_{bci}(Q)\Bigg[4 C^{b}\Big[14046 \widehat G_{a}{}^{c}\\
&+241 \varepsilon^{def}{}_{a}{}^{c} \widehat H_{def}\Big]\\
&+C_{a}\Big[-6594 \widehat G^{bc}\\
&+6509 \varepsilon^{defbc} \widehat H_{def}\Big]\\
&+3\Big[1082 \widehat H_{a}{}^{bc}\\
&+2651 \varepsilon^{de}{}_{a}{}^{bc} \widehat G_{de}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i \zeta}{L^{2}} E_{a}\bar\varphi^{i}\mathcal D^{a}(\chi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\bar\varphi^{i}\mathcal D^{a}(\varphi^{j})\Bigg[L_{ij}\Big[16 T_{ab}\Big[-\frac{3 i}{L} E^{b}\\
&-\sqrt{2} i V^{b}\Big]\\
&+\widehat G_{ab}\Big[\frac{4 i}{L} E^{b}\\
&+\sqrt{2} i V^{b}\Big]\\
&+\frac{2}{L}\Big[-\frac{4 i N}{L} \mathcal D_{a}(L)\\
&-i \mathcal D_{a}(N)\Big]\Big]\\
&+\frac{2}{L}\Big[\mathcal D_{b}(L_{jk}) L_{i}{}^{k}\Big[-12 i T_{a}{}^{b}\\
&+i \widehat G_{a}{}^{b}\Big]\\
&+4 i L_{j}{}^{k} T_{ab} \mathcal D^{b}(L_{ik})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{2}}\bar\varphi^{i}\mathcal D^{a}(\varphi_{i})\Bigg[2 T_{bc} \varepsilon_{a}{}^{bc}{}_{de}\Big[-4 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&-i (g + \frac{2 N}{L^{2}}) E_{a}\\
&-8 i \mathcal D^{b}(T_{ba})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\mathcal D^{a}(\widehat R_{bai}(Q))\Bigg[-\frac{221 i \beta g}{128} C^{b}\\
&+\frac{i \zeta}{L^{2}} E^{b}\\
&+\frac{\sqrt{2} i \zeta}{2 L} V^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{8 i \zeta}{L^{2}} T_{ab}\bar\varphi^{i}\mathcal D^{a}\mathcal D^{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{16 i \zeta}{L^{4}} L_{i}{}^{k} L_{j}{}^{l} \mathcal D^{a}(L_{kl})\bar\varphi^{i}\mathcal D_{a}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{4}}\bar\varphi^{i}\mathcal D_{a}(\varphi^{j})\Bigg[i N \mathcal D^{a}(L_{ij})\\
&+i g L_{i}{}^{k} L_{j}{}^{l} \mathcal D^{a}(L_{kl})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L} T^{a}{}_{b}\bar\varphi^{i}\phi_{ai}\Bigg[-\frac{2 i}{L} E^{b}\\
&-\sqrt{2} i V^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{3 N \zeta}{L^{4}}\bar\varphi^{i}\phi_{a}{}^{j}\Bigg[i E^{a} L_{ij}\\
&+i L_{i}{}^{k} \mathcal D^{a}(L_{jk})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\varphi^{j}\Bigg[L_{ij}\Big[\frac{\zeta}{L^{2}} T_{ab}\Big[\frac{8}{L^{2}} L^{kl}\Big[i \widehat R^{ab}{}_{kl}(V)\\
&-\frac{i}{L^{2}} \mathcal D^{a}(L_{ok}) \mathcal D^{b}(L^{o}{}_{l})\Big]\\
&+\frac{2}{L^{2}} E_{c} \varepsilon^{abc}{}_{de}\Big[-8 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&+\frac{16 i (g - \frac{34 N}{L^{2}})}{3} T^{ab}\\
&+\frac{24 i}{L^{2}} \mathcal D^{a}(E^{b})\\
&+\frac{20 i N}{L^{2}} \widehat G^{ab}\\
&-\frac{16 i}{L^{3}} E^{a} \mathcal D^{b}(L)\\
&+\frac{24 \sqrt{2} i}{L^{2}} V^{b} \mathcal D^{a}(L)\Big]\\
&+\frac{\zeta}{L^{4}} \widehat G_{ab}\Big[L^{kl}\Big[-\frac{i}{2} \widehat R^{ab}{}_{kl}(V)\\
&+\frac{i}{2 L^{2}} \mathcal D^{a}(L_{ok}) \mathcal D^{b}(L^{o}{}_{l})\Big]\\
&-i \mathcal D^{a}(E^{b})\\
&+\frac{2 i}{L} E^{a} \mathcal D^{b}(L)\\
&-\frac{3 \sqrt{2} i}{2} V^{b} \mathcal D^{a}(L)\Big]\\
&+\frac{\zeta}{L^{4}} E_{a}\Big[i (\frac{g}{2} + \frac{4 N}{L^{2}}) E^{a}\\
&+24 i \mathcal D^{b}(T^{a}{}_{b})\\
&-i \mathcal D^{b}(\widehat G^{a}{}_{b})\Big]\\
&+\frac{2 \zeta}{L^{5}} \mathcal D_{a}(L)\Big[\frac{7 i N}{L} \mathcal D^{a}(L)\\
&-i \mathcal D^{a}(N)\Big]\\
&+\frac{\sqrt{2} \zeta}{2 L^{3}} V_{a}\Big[-16 i \mathcal D^{b}(T_{b}{}^{a})\\
&+i \mathcal D^{b}(\widehat G_{b}{}^{a})\Big]\\
&-i (\frac{4 D \zeta (g + \frac{8 N}{L^{2}})}{L^{2}} + \frac{17 \beta g^{3}}{12} + \frac{N (4 - \frac{N \zeta (11 g + \frac{8 N}{L^{2}})}{L})}{2 L^{3}})\\
&-\frac{i \zeta (g + \frac{10 N}{L^{2}})}{L^{3}} \Box^c(L)\\
&+\frac{i \zeta}{L^{4}} \Box^c(N)\\
&+\frac{4 i N \zeta}{L^{4}} f_{a}{}^{a}\\
&+\frac{i \zeta (\frac{g}{2} + \frac{4 N}{L^{2}})}{L^{4}} \mathcal D^{a}(L^{kl}) \mathcal D_{a}(L_{kl})\Big]\\
&+\frac{\zeta}{L^{3}}\Big[\frac{1}{L} L_{j}{}^{k}\Big[\frac{1}{L^{2}} L_{i}{}^{l}\Big[\mathcal D_{a}(L_{lo})\Big[\mathcal D_{b}(L_{k}{}^{o})\Big[8 i T^{ab}\\
&-i \widehat G^{ab}\Big]\\
&-i g L^{oz} \mathcal D^{a}(L_{zk})\Big]\\
&+2\Big[\mathcal D_{a}(L_{kl})\Big[E_{b}\Big[-8 i T^{ba}\\
&+i \widehat G^{ba}\Big]\\
&+i \mathcal D^{a}(N)\Big]\\
&-i N \Box^c(L_{lk})\Big]\Big]\\
&+\mathcal D_{a}(L_{ik})\Big[2 T_{bc} \varepsilon^{abc}{}_{de}\Big[-8 i T^{de}\\
&+i \widehat G^{de}\Big]\\
&-i (g + \frac{8 N}{L^{2}}) E^{a}\\
&-8 i \mathcal D^{b}(T_{b}{}^{a})\\
&-\frac{16 i}{L} T_{b}{}^{a} \mathcal D^{b}(L)\Big]\\
&+8 i T_{ab} \mathcal D^{a}\mathcal D^{b}(L_{ik})\Big]\\
&+\mathcal D_{a}(L_{ij})\Big[8 T^{a}{}_{b}\Big[-\frac{i}{L} E^{b}\\
&-\sqrt{2} i V^{b}\Big]\\
&+\widehat G^{a}{}_{b}\Big[\frac{i}{L} E^{b}\\
&+\frac{\sqrt{2} i}{2} V^{b}\Big]\\
&-\frac{8 i N}{L^{2}} \mathcal D^{a}(L)\Big]\\
&+\frac{1}{L}\Big[3 i N \Box^c(L_{ij})\\
&-8 i T_{ab} \mathcal D^{a}(L_{ki}) \mathcal D^{b}(L^{k}{}_{j})\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\bar\varphi^{i}\widehat R_{abi}(Q)\Bigg[\frac{\beta g}{18432} C_{c}\Big[-10458 i \widehat H^{cab}\\
&-919 i \varepsilon^{cdeab} \widehat G_{de}\Big]\\
&+\frac{\zeta}{L} \widehat G_{cd} \varepsilon^{abcd}{}_{e}\Big[\frac{i}{4 L} E^{e}\\
&+\frac{\sqrt{2} i}{8} V^{e}\Big]\\
&+\frac{i}{L} E^{ab}\\
&-\frac{8 i N \zeta}{L^{2}} T^{ab}\\
&-\frac{i (859 \beta g - \frac{4608 N \zeta}{L^{2}})}{9216} \widehat G^{ab}\\
&-\frac{i \zeta}{L^{3}} E^{a} \mathcal D^{b}(L)\\
&+\frac{\sqrt{2} i \zeta}{2 L^{2}} V^{b} \mathcal D^{a}(L)\\
&+\frac{6173 i \beta g}{55296} \varepsilon^{cdeab} \widehat H_{cde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{2} C_{b} L_{ij}\overline{\Box^c(\psi^{i})}\gamma^{bc}\psi_{c}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{6} \widehat H_{bc}{}^{d}\overline{\Box^c(\psi^{i})}\gamma^{bc}\psi_{di}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{13 i \beta}{128} C_{f} \varepsilon^{f}{}_{bc}{}^{de}\overline{\Box^c(\psi^{i})}\gamma^{bc}\widehat R_{dei}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{2} L_{ij}\overline{\Box^c(\psi^{i})}\gamma^{b}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{3} C_{d} \widehat H^{d}{}_{b}{}^{c}\overline{\Box^c(\psi^{i})}\gamma^{b}\psi_{ci}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta g}{6} C_{b}\overline{\Box^c(\psi^{i})}\gamma^{b}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{5 i \beta g}{6}\overline{\Box^c(\psi^{i})}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{16 i \zeta}{L^{2}} L_{ij}\overline{\Box^c(\varphi^{i})}\chi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-8 i \alpha C^{b}\overline{\mathcal D^{a}(\chi^{i})}\widehat R_{bai}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{7 i \beta}{6} C_{a}\overline{\mathcal D^{a}(\psi^{i})}\Box^c(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta g}{12} C_{e} L_{ij} \varepsilon^{e}{}_{abcd}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\psi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{96}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\psi_{i})\Bigg[C_{a}\Big[44 i \widehat H_{bcd}\\
&+5 i \varepsilon^{ef}{}_{bcd} \widehat G_{ef}\Big]\\
&-10 i C_{e} \varepsilon^{ef}{}_{bcd} \widehat G_{fa}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{12} C_{e} \varepsilon^{e}{}_{abcd}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{437 i \beta}{1536} C_{f} \varepsilon^{f}{}_{bcd}{}^{e}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\widehat R_{eai}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{217 i \beta}{768} C_{f} \varepsilon^{f}{}_{abc}{}^{e}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\widehat R_{edi}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{3072}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}(\widehat R_{efi}(Q))\Bigg[836 i C^{e} \varepsilon_{abcd}{}^{f}\\
&-117 i C_{a} \varepsilon_{bcd}{}^{ef}\\
&-70 i C_{b} \varepsilon_{acd}{}^{ef}\\
&+514 i C_{d} \varepsilon_{abc}{}^{ef}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{12} \varepsilon_{abcde}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D^{d}\mathcal D^{e}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{2} C_{a}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D_{b}\mathcal D_{c}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{144}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\mathcal D_{c}(\psi_{i})\Bigg[3 C_{d}\Big[-4 i \widehat H^{d}{}_{ab}\\
&+7 i \varepsilon^{def}{}_{ab} \widehat G_{ef}\Big]\\
&+2\Big[6 i \widehat G_{ab}\\
&+i \varepsilon^{def}{}_{ab} \widehat H_{def}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{ai}\Bigg[C_{b}\Big[8 \widehat H_{cde}\Big[-9 i \widehat G^{de}\\
&+i \varepsilon^{fghde} \widehat H_{fgh}\Big]\\
&+\varepsilon_{cdefg}\Big[-32 i \mathcal D^{d}(\widehat H^{efg})\\
&+27 i \widehat G^{de} \widehat G^{fg}\Big]\\
&+48 i \mathcal D^{d}(\widehat G_{dc})\Big]\\
&+2\Big[6 C_{d}\Big[7 i \mathcal D^{d}(\widehat G_{bc})\\
&-14 i \mathcal D_{b}(\widehat G^{d}{}_{c})\\
&-3 i \widehat G^{d}{}_{e} \widehat H^{e}{}_{bc}\\
&+6 i \widehat G_{eb} \widehat H^{de}{}_{c}\Big]\\
&+24 i \mathcal D^{d}(\widehat H_{dbc})\\
&+72 i \mathcal D_{b}\mathcal D_{c}(\sigma)\\
&-i \varepsilon^{defg}{}_{c} \widehat G_{db} \widehat H_{efg}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{a}{}^{j}\Bigg[\frac{g}{24} L_{ij}\Big[3 i \widehat G_{bc}\\
&+8 i C_{d} \widehat H^{d}{}_{bc}\Big]\\
&+\frac{i}{6} \widehat R_{bcij}(V)\\
&-\frac{i g}{2} C_{b} \mathcal D_{c}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{b}{}^{j}\Bigg[\frac{i}{6} \widehat R_{acij}(V)\\
&+\frac{i g}{2} C_{a} \mathcal D_{c}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{ci}\Bigg[8 C_{d}\Big[30 i \mathcal D^{d}(\widehat G_{ab})\\
&-39 i \mathcal D_{a}(\widehat G^{d}{}_{b})\\
&+30 i \mathcal D_{b}(\widehat G^{d}{}_{a})\\
&+2 i \mathcal D^{d}(\widehat H_{efg}) \varepsilon^{efg}{}_{ab}\\
&+18 i \mathcal D^{e}\mathcal D^{f}(\sigma) \varepsilon^{d}{}_{efab}\\
&-i \mathcal D_{a}(\widehat H_{efg}) \varepsilon^{defg}{}_{b}\\
&-2 i \mathcal D_{b}(\widehat H_{efg}) \varepsilon^{defg}{}_{a}\\
&-6 i \widehat G_{ea} \widehat H^{de}{}_{b}\Big]\\
&+C_{a}\Big[8 \widehat H_{bde}\Big[-9 i \widehat G^{de}\\
&+i \varepsilon^{fghde} \widehat H_{fgh}\Big]\\
&+\varepsilon_{bdefg}\Big[-32 i \mathcal D^{d}(\widehat H^{efg})\\
&+27 i \widehat G^{de} \widehat G^{fg}\Big]\\
&+48 i \mathcal D^{d}(\widehat G_{db})\Big]\\
&+C_{b}\Big[\varepsilon_{adefg}\Big[20 i \mathcal D^{d}(\widehat H^{efg})\\
&-9 i \widehat G^{de} \widehat G^{fg}\Big]\\
&+24 i \mathcal D^{d}(\widehat G_{da})\Big]\\
&+4\Big[\widehat H_{def}\Big[-3 i \varepsilon^{gdef}{}_{a} \widehat G_{gb}\\
&+2 i \varepsilon^{gdef}{}_{b} \widehat G_{ga}\Big]\\
&+3\Big[2 i \mathcal D^{d}(\widehat H_{dab})\\
&+30 i \mathcal D_{a}\mathcal D_{b}(\sigma)\\
&-12 i \mathcal D_{b}\mathcal D_{a}(\sigma)\\
&-7 i \mathcal D^{d}(\widehat G_{ef}) \varepsilon_{d}{}^{ef}{}_{ab}\\
&+6 i \widehat G^{d}{}_{b} \widehat G_{da}\\
&+4 i \widehat H^{de}{}_{b} \widehat H_{dea}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{c}{}^{j}\Bigg[C_{d}\Big[\frac{g}{8} L_{ij}\Big[-8 i \widehat H^{d}{}_{ab}\\
&+i \varepsilon^{def}{}_{ab} \widehat G_{ef}\Big]\\
&+\frac{i}{6} \varepsilon^{d}{}_{abef} \widehat R^{ef}{}_{ij}(V)\Big]\\
&+\frac{g}{36} L_{ij}\Big[3 i \widehat G_{ab}\\
&-4 i \varepsilon^{def}{}_{ab} \widehat H_{def}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{di}\Bigg[C_{e}\Big[\frac{1}{36} \widehat H_{fgh}\Big[-3 i \varepsilon^{eh}{}_{bc}{}^{d} \widehat H^{fg}{}_{a}\\
&+i \varepsilon^{e}{}_{abc}{}^{d} \widehat H^{fgh}\Big]\\
&+\frac{1}{24} \varepsilon_{bc}{}^{de}{}_{f}\Big[6 i \mathcal D^{f}\mathcal D_{a}(\sigma)\\
&+i \mathcal D^{g}(\widehat H_{g}{}^{f}{}_{a})\\
&-15 i \mathcal D_{a}\mathcal D^{f}(\sigma)\\
&-3 i \widehat G^{g}{}_{a} \widehat G_{g}{}^{f}\Big]\\
&+\varepsilon_{abc}{}^{de}\Big[\frac{i g (13 L^{2} g + 22 N)}{48}\\
&+\frac{5 i}{24} \Box^c(\sigma)\Big]\\
&+\frac{1}{24}\Big[4 i \widehat G^{ed} \widehat H_{abc}\\
&-3 i \widehat G^{e}{}_{a} \widehat H_{bc}{}^{d}\\
&+8 i \widehat G^{e}{}_{b} \widehat H_{ac}{}^{d}\\
&-6 i \widehat G_{ab} \widehat H^{e}{}_{c}{}^{d}\\
&-3 i \widehat G_{a}{}^{d} \widehat H^{e}{}_{bc}\\
&-4 i \widehat G_{bc} \widehat H^{e}{}_{a}{}^{d}\\
&+8 i \widehat G_{b}{}^{d} \widehat H^{e}{}_{ac}\Big]\Big]\\
&+\frac{1}{288}\Big[8 C_{b}\Big[30 i \mathcal D^{d}(\widehat G_{ac})\\
&+39 i \mathcal D_{a}(\widehat G_{c}{}^{d})\\
&-30 i \mathcal D_{c}(\widehat G_{a}{}^{d})\\
&+2 i \mathcal D^{d}(\widehat H_{efg}) \varepsilon^{efg}{}_{ac}\\
&+18 i \mathcal D^{e}\mathcal D^{f}(\sigma) \varepsilon_{efac}{}^{d}\\
&-i \mathcal D_{a}(\widehat H_{efg}) \varepsilon^{efg}{}_{c}{}^{d}\\
&-2 i \mathcal D_{c}(\widehat H_{efg}) \varepsilon^{efg}{}_{a}{}^{d}\\
&-6 i \widehat G_{ea} \widehat H^{e}{}_{c}{}^{d}\Big]\\
&+12 C_{a}\Big[-7 i \mathcal D^{d}(\widehat G_{bc})\\
&-14 i \mathcal D_{b}(\widehat G_{c}{}^{d})\\
&-6 i \widehat G_{eb} \widehat H^{e}{}_{c}{}^{d}\\
&-3 i \widehat G_{e}{}^{d} \widehat H^{e}{}_{bc}\Big]\\
&+\widehat H_{efg}\Big[-4 i \varepsilon^{efg}{}_{ac} \widehat G_{b}{}^{d}\\
&+2 i \varepsilon^{efg}{}_{a}{}^{d} \widehat G_{bc}\\
&+3 i \varepsilon^{fg}{}_{bc}{}^{d} \widehat G^{e}{}_{a}\\
&+30 i \varepsilon^{g}{}_{abc}{}^{d} \widehat G^{ef}\Big]\\
&+6\Big[\varepsilon_{bc}{}^{d}{}_{ef}\Big[-20 i \mathcal D^{e}(\widehat G^{f}{}_{a})\\
&-13 i \mathcal D_{a}(\widehat G^{ef})\\
&-i \widehat G_{g}{}^{e} \widehat H^{gf}{}_{a}\Big]\\
&+2\Big[8 i \mathcal D^{d}(\widehat H_{abc})\\
&-14 i \mathcal D_{a}(\widehat H_{bc}{}^{d})\\
&+16 i \mathcal D_{b}(\widehat H_{ac}{}^{d})\\
&-2 i \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{f}{}_{abc}{}^{d}\\
&+18 i \widehat G_{ab} \widehat G_{c}{}^{d}\\
&+9 i \widehat G_{a}{}^{d} \widehat G_{bc}\\
&+8 i \widehat H^{e}{}_{bc} \widehat H_{ea}{}^{d}\\
&+16 i \widehat H^{e}{}_{c}{}^{d} \widehat H_{eab}\Big]\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\psi_{d}{}^{j}\Bigg[C_{b}\Big[\frac{g}{8} L_{ij}\Big[-8 i \widehat H_{ac}{}^{d}\\
&+i \varepsilon^{ef}{}_{ac}{}^{d} \widehat G_{ef}\Big]\\
&+\frac{i}{6} \varepsilon_{ac}{}^{d}{}_{ef} \widehat R^{ef}{}_{ij}(V)\Big]\\
&+C_{e} \varepsilon_{bc}{}^{de}{}_{f}\Big[-\frac{i}{12} \widehat R^{f}{}_{aij}(V)\\
&+\frac{i g}{24} L_{ij} \widehat G^{f}{}_{a}\Big]\\
&+\frac{g}{12}\Big[L_{ij}\Big[-4 i C_{a} \widehat H_{bc}{}^{d}\\
&+3 i \varepsilon^{ef}{}_{bc}{}^{d} \widehat H_{efa}\Big]\\
&+3 i \mathcal D^{e}(L_{ij}) \varepsilon_{abc}{}^{d}{}_{e}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{72}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\varphi_{i}\Bigg[57 i \widehat H_{abc}\\
&-18 i \varepsilon^{de}{}_{abc} \widehat G_{de}\\
&+5 i C_{b} \varepsilon^{def}{}_{ac} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{55296}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\widehat R_{dai}(Q)\Bigg[C^{d}\Big[-13614 i \widehat G_{bc}\\
&+3731 i \varepsilon^{efg}{}_{bc} \widehat H_{efg}\Big]\\
&+4\Big[5 C_{b}\Big[-510 i \widehat G_{c}{}^{d}\\
&-61 i \varepsilon^{efg}{}_{c}{}^{d} \widehat H_{efg}\Big]\\
&+6\Big[-37 i \widehat H_{bc}{}^{d}\\
&-262 i \varepsilon^{ef}{}_{bc}{}^{d} \widehat G_{ef}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{36864}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\widehat R_{dei}(Q)\Bigg[1214 i \varepsilon^{f}{}_{abc}{}^{e} \widehat G_{f}{}^{d}\\
&-2106 i \varepsilon^{f}{}_{ac}{}^{de} \widehat G_{fb}\\
&-4999 i \varepsilon^{f}{}_{bc}{}^{de} \widehat G_{fa}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{355 i \beta g}{2304} L_{ij} \varepsilon_{abc}{}^{de}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{bc}\widehat R_{de}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{72}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D^{c}(\psi_{i})\Bigg[C_{b}\Big[-18 \widehat G_{ac}\\
&+\varepsilon^{def}{}_{ac} \widehat H_{def}\Big]\\
&-6 \widehat H_{abc}\\
&+9 \varepsilon^{de}{}_{abc} \widehat G_{de}\\
&+8 C_{a} \varepsilon^{def}{}_{bc} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{283 \beta}{768} C_{b}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D^{c}(\widehat R_{aci}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{111 \beta}{512} \varepsilon_{abc}{}^{de}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D^{c}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{2} C_{e} \varepsilon^{e}{}_{abcd}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D^{c}\mathcal D^{d}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{3} C_{a} L_{ij}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D_{b}(\psi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{72} C_{c}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D_{b}(\psi_{i})\Bigg[-54 \widehat G^{c}{}_{a}\\
&-11 \varepsilon^{cdef}{}_{a} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{6} C_{a}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D_{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{167 \beta}{384} C^{c}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\mathcal D_{b}(\widehat R_{cai}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{ai}\Bigg[\frac{1}{144} C_{c}\Big[\widehat H_{def}\Big[-\varepsilon^{cgdef} \widehat G_{gb}\\
&-\varepsilon^{gdef}{}_{b} \widehat G^{c}{}_{g}\Big]\\
&+24\Big[-3 \mathcal D^{c}\mathcal D_{b}(\sigma)\\
&+2 \mathcal D^{d}(\widehat H^{c}{}_{db})\\
&+3 \mathcal D_{b}\mathcal D^{c}(\sigma)\Big]\Big]\\
&+C_{b}\Big[\frac{1}{36} \widehat H_{cde}\Big[-2 \widehat H^{cde}\\
&-\varepsilon^{fgcde} \widehat G_{fg}\Big]\\
&-\frac{g (13 L^{2} g + 22 N)}{24}\\
&-\frac{5}{12} \Box^c(\sigma)\Big]\\
&+\frac{1}{288}\Big[8 \widehat H_{bcd}\Big[-9 \widehat G^{cd}\\
&+\varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\varepsilon_{bcdef}\Big[-32 \mathcal D^{c}(\widehat H^{def})\\
&+27 \widehat G^{cd} \widehat G^{ef}\Big]\\
&+48 \mathcal D^{c}(\widehat G_{cb})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{a}{}^{j}\Bigg[C_{c}\Big[-\frac{1}{3} \widehat R^{c}{}_{bij}(V)\\
&-\frac{g}{4} L_{ij} \widehat G^{c}{}_{b}\Big]\\
&-\frac{g}{2} \mathcal D_{b}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{bi}\Bigg[\frac{1}{72} C_{c}\Big[\widehat H_{def}\Big[-2 \varepsilon^{cgdef} \widehat G_{ga}\\
&-3 \varepsilon^{gdef}{}_{a} \widehat G^{c}{}_{g}\Big]\\
&+3\Big[12 \mathcal D^{c}\mathcal D_{a}(\sigma)\\
&-2 \mathcal D^{d}(\widehat H^{c}{}_{da})\\
&-30 \mathcal D_{a}\mathcal D^{c}(\sigma)\\
&+7 \mathcal D^{d}(\widehat G_{ef}) \varepsilon^{c}{}_{d}{}^{ef}{}_{a}\\
&+6 \widehat G^{c}{}_{d} \widehat G^{d}{}_{a}\\
&-4 \widehat H^{c}{}_{de} \widehat H^{de}{}_{a}\Big]\Big]\\
&+C_{a}\Big[\frac{1}{36} \widehat H_{cde}\Big[2 \widehat H^{cde}\\
&+\varepsilon^{fgcde} \widehat G_{fg}\Big]\\
&+\frac{g (13 L^{2} g + 22 N)}{24}\\
&+\frac{5}{12} \Box^c(\sigma)\Big]\\
&+\frac{1}{288}\Big[\varepsilon_{acdef}\Big[20 \mathcal D^{c}(\widehat H^{def})\\
&-9 \widehat G^{cd} \widehat G^{ef}\Big]\\
&+24 \mathcal D^{c}(\widehat G_{ca})\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta C_{c}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{b}{}^{j}\Bigg[\frac{g}{36} L_{ij}\Big[3 \widehat G^{c}{}_{a}\\
&+4 \varepsilon^{cdef}{}_{a} \widehat H_{def}\Big]\\
&-\frac{1}{6} \widehat R^{c}{}_{aij}(V)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{144}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{ci}\Bigg[C_{d}\Big[\widehat H_{efg}\Big[-2 \varepsilon^{defg}{}_{a} \widehat G_{b}{}^{c}\\
&-3 \varepsilon^{dfg}{}_{b}{}^{c} \widehat G^{e}{}_{a}\\
&-30 \varepsilon^{dg}{}_{ab}{}^{c} \widehat G^{ef}\\
&+2 \varepsilon^{efg}{}_{ab} \widehat G^{dc}\\
&-2 \varepsilon^{efg}{}_{a}{}^{c} \widehat G^{d}{}_{b}\Big]\\
&+6\Big[\varepsilon_{b}{}^{cd}{}_{ef}\Big[20 \mathcal D^{e}(\widehat G^{f}{}_{a})\\
&+13 \mathcal D_{a}(\widehat G^{ef})\\
&+\widehat G_{g}{}^{e} \widehat H^{gf}{}_{a}\Big]\\
&+2\Big[8 \mathcal D^{c}(\widehat H^{d}{}_{ab})\\
&-8 \mathcal D^{d}(\widehat H_{ab}{}^{c})\\
&+14 \mathcal D_{a}(\widehat H^{d}{}_{b}{}^{c})\\
&-8 \mathcal D_{b}(\widehat H^{d}{}_{a}{}^{c})\\
&+2 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{df}{}_{ab}{}^{c}\\
&+9 \widehat G^{dc} \widehat G_{ab}\\
&+9 \widehat G^{d}{}_{a} \widehat G_{b}{}^{c}\\
&-9 \widehat G^{d}{}_{b} \widehat G_{a}{}^{c}\\
&-8 \widehat H^{d}{}_{ea} \widehat H^{e}{}_{b}{}^{c}\\
&+8 \widehat H^{d}{}_{eb} \widehat H^{e}{}_{a}{}^{c}\\
&-8 \widehat H^{d}{}_{e}{}^{c} \widehat H^{e}{}_{ab}\Big]\Big]\Big]\\
&+2 C_{b}\Big[\widehat H_{def}\Big[2 \varepsilon^{gdefc} \widehat G_{ga}\\
&-3 \varepsilon^{gdef}{}_{a} \widehat G_{g}{}^{c}\Big]\\
&+3\Big[-12 \mathcal D^{c}\mathcal D_{a}(\sigma)\\
&+2 \mathcal D^{d}(\widehat H_{da}{}^{c})\\
&+30 \mathcal D_{a}\mathcal D^{c}(\sigma)\\
&-7 \mathcal D^{d}(\widehat G_{ef}) \varepsilon_{d}{}^{ef}{}_{a}{}^{c}\\
&+6 \widehat G^{dc} \widehat G_{da}\\
&+4 \widehat H^{dec} \widehat H_{dea}\Big]\Big]\\
&+C_{a}\Big[\widehat H_{def}\Big[\varepsilon^{gdefc} \widehat G_{gb}\\
&-\varepsilon^{gdef}{}_{b} \widehat G_{g}{}^{c}\Big]\\
&+24\Big[3 \mathcal D^{c}\mathcal D_{b}(\sigma)\\
&-2 \mathcal D^{d}(\widehat H_{db}{}^{c})\\
&-3 \mathcal D_{b}\mathcal D^{c}(\sigma)\Big]\Big]\\
&+4\Big[30 \mathcal D^{c}(\widehat G_{ab})\\
&+39 \mathcal D_{a}(\widehat G_{b}{}^{c})\\
&-30 \mathcal D_{b}(\widehat G_{a}{}^{c})\\
&+2 \mathcal D^{c}(\widehat H_{def}) \varepsilon^{def}{}_{ab}\\
&+18 \mathcal D^{d}\mathcal D^{e}(\sigma) \varepsilon_{deab}{}^{c}\\
&-\mathcal D_{a}(\widehat H_{def}) \varepsilon^{def}{}_{b}{}^{c}\\
&-2 \mathcal D_{b}(\widehat H_{def}) \varepsilon^{def}{}_{a}{}^{c}\\
&-6 \widehat G_{da} \widehat H^{d}{}_{b}{}^{c}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\psi_{c}{}^{j}\Bigg[\frac{g}{72} L_{ij}\Big[2 C_{b}\Big[3 \widehat G_{a}{}^{c}\\
&-4 \varepsilon^{def}{}_{a}{}^{c} \widehat H_{def}\Big]\\
&+9\Big[-8 \widehat H_{ab}{}^{c}\\
&-2 C_{a} \widehat G_{b}{}^{c}\\
&+\varepsilon^{de}{}_{ab}{}^{c} \widehat G_{de}\\
&-4 C_{d} \varepsilon^{def}{}_{b}{}^{c} \widehat H_{efa}\Big]\Big]\\
&+\varepsilon_{ab}{}^{c}{}_{de}\Big[\frac{1}{6} \widehat R^{de}{}_{ij}(V)\\
&-\frac{g}{2} C^{d} \mathcal D^{e}(L_{ij})\Big]\\
&+\frac{1}{6}\Big[-2 C_{a} \widehat R_{b}{}^{c}{}_{ij}(V)\\
&-C_{b} \widehat R_{a}{}^{c}{}_{ij}(V)\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{72}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\varphi_{i}\Bigg[6 C_{c}\Big[-23 \widehat H^{c}{}_{ab}\\
&+3 \varepsilon^{cde}{}_{ab} \widehat G_{de}\Big]\\
&-36 \widehat G_{ab}\\
&-\varepsilon^{cde}{}_{ab} \widehat H_{cde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{13824}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\widehat R_{cai}(Q)\Bigg[3 C_{d}\Big[-2998 \widehat H^{d}{}_{b}{}^{c}\\
&-259 \varepsilon^{def}{}_{b}{}^{c} \widehat G_{ef}\Big]\\
&+8\Big[-867 \widehat G_{b}{}^{c}\\
&-11 \varepsilon^{def}{}_{b}{}^{c} \widehat H_{def}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{9216}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\widehat R_{cdi}(Q)\Bigg[2 C_{e}\Big[-802 \varepsilon^{ef}{}_{ab}{}^{d} \widehat G_{f}{}^{c}\\
&-996 \varepsilon^{ef}{}_{a}{}^{cd} \widehat G_{fb}\\
&+433 \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{fa}\\
&-939 \varepsilon^{f}{}_{ab}{}^{cd} \widehat G^{e}{}_{f}\Big]\\
&+C^{c}\Big[-2738 \widehat H_{ab}{}^{d}\\
&-543 \varepsilon^{ef}{}_{ab}{}^{d} \widehat G_{ef}\Big]\\
&+C_{b}\Big[-2972 \widehat H_{a}{}^{cd}\\
&-107 \varepsilon^{ef}{}_{a}{}^{cd} \widehat G_{ef}\Big]\\
&+4 C_{a}\Big[815 \widehat H_{b}{}^{cd}\\
&-96 \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{103 \beta g}{288} C_{e} L_{ij} \varepsilon^{e}{}_{ab}{}^{cd}\overline{\mathcal D^{a}(\psi^{i})}\gamma^{b}\widehat R_{cd}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{36}\overline{\mathcal D^{a}(\psi^{i})}\mathcal D^{b}(\psi_{i})\Bigg[3 C_{c}\Big[-14 i \widehat H^{c}{}_{ab}\\
&+3 i \varepsilon^{cde}{}_{ab} \widehat G_{de}\Big]\\
&+2\Big[-27 i \widehat G_{ab}\\
&-i \varepsilon^{cde}{}_{ab} \widehat H_{cde}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{81 i \beta}{256}\overline{\mathcal D^{a}(\psi^{i})}\mathcal D^{b}(\widehat R_{abi}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{49 i \beta}{192} C_{e} \varepsilon^{e}{}_{ab}{}^{cd}\overline{\mathcal D^{a}(\psi^{i})}\mathcal D^{b}(\widehat R_{cdi}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\psi_{ai}\Bigg[\frac{1}{288} C_{b}\Big[8 \widehat H^{b}{}_{cd}\Big[9 i \widehat G^{cd}\\
&-i \varepsilon^{cdefg} \widehat H_{efg}\Big]\\
&+\varepsilon^{b}{}_{cdef}\Big[32 i \mathcal D^{c}(\widehat H^{def})\\
&-27 i \widehat G^{cd} \widehat G^{ef}\Big]\\
&+48 i \mathcal D^{c}(\widehat G^{b}{}_{c})\Big]\\
&+\frac{1}{36} \widehat H_{bcd}\Big[-2 i \widehat H^{bcd}\\
&-i \varepsilon^{efbcd} \widehat G_{ef}\Big]\\
&-\frac{i g (13 L^{2} g + 22 N)}{24}\\
&-\frac{5 i}{12} \Box^c(\sigma)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{2} C_{b} \mathcal D^{b}(L_{ij})\overline{\mathcal D^{a}(\psi^{i})}\psi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D^{a}(\psi^{i})}\psi_{bi}\Bigg[8 C_{c}\Big[30 i \mathcal D^{b}(\widehat G^{c}{}_{a})\\
&+30 i \mathcal D^{c}(\widehat G_{a}{}^{b})\\
&-39 i \mathcal D_{a}(\widehat G^{cb})\\
&-2 i \mathcal D^{b}(\widehat H_{def}) \varepsilon^{cdef}{}_{a}\\
&+2 i \mathcal D^{c}(\widehat H_{def}) \varepsilon^{def}{}_{a}{}^{b}\\
&+18 i \mathcal D^{d}\mathcal D^{e}(\sigma) \varepsilon^{c}{}_{dea}{}^{b}\\
&-i \mathcal D_{a}(\widehat H_{def}) \varepsilon^{cdefb}\\
&-6 i \widehat G_{da} \widehat H^{cdb}\Big]\\
&+C_{a}\Big[8 \widehat H^{b}{}_{cd}\Big[-9 i \widehat G^{cd}\\
&+i \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\varepsilon^{b}{}_{cdef}\Big[-32 i \mathcal D^{c}(\widehat H^{def})\\
&+27 i \widehat G^{cd} \widehat G^{ef}\Big]\\
&+48 i \mathcal D^{c}(\widehat G_{c}{}^{b})\Big]\\
&+4\Big[\widehat H_{cde}\Big[2 i \varepsilon^{fcdeb} \widehat G_{fa}\\
&-3 i \varepsilon^{fcde}{}_{a} \widehat G_{f}{}^{b}\Big]\\
&+3\Big[-12 i \mathcal D^{b}\mathcal D_{a}(\sigma)\\
&+2 i \mathcal D^{c}(\widehat H_{ca}{}^{b})\\
&+30 i \mathcal D_{a}\mathcal D^{b}(\sigma)\\
&-7 i \mathcal D^{c}(\widehat G_{de}) \varepsilon_{c}{}^{de}{}_{a}{}^{b}\\
&+6 i \widehat G^{cb} \widehat G_{ca}\\
&+4 i \widehat H^{cdb} \widehat H_{cda}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D^{a}(\psi^{i})}\psi_{b}{}^{j}\Bigg[C_{c}\Big[\frac{g}{8} L_{ij}\Big[-8 i \widehat H^{c}{}_{a}{}^{b}\\
&+i \varepsilon^{cde}{}_{a}{}^{b} \widehat G_{de}\Big]\\
&+\frac{i}{6} \varepsilon^{c}{}_{a}{}^{b}{}_{de} \widehat R^{de}{}_{ij}(V)\Big]\\
&+\frac{g}{36} L_{ij}\Big[3 i \widehat G_{a}{}^{b}\\
&-4 i \varepsilon^{cde}{}_{a}{}^{b} \widehat H_{cde}\Big]\\
&-\frac{i}{6} \widehat R_{a}{}^{b}{}_{ij}(V)\\
&-\frac{i g}{2} C_{a} \mathcal D^{b}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{24} C_{b}\overline{\mathcal D^{a}(\psi^{i})}\varphi_{i}\Bigg[44 i \widehat G^{b}{}_{a}\\
&-i \varepsilon^{bcde}{}_{a} \widehat H_{cde}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{6912} C_{c}\overline{\mathcal D^{a}(\psi^{i})}\widehat R_{bai}(Q)\Bigg[3030 i \widehat G^{cb}\\
&+839 i \varepsilon^{cdefb} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{211 i \beta g}{144} C^{b} L_{ij}\overline{\mathcal D^{a}(\psi^{i})}\widehat R_{ba}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{55296}\overline{\mathcal D^{a}(\psi^{i})}\widehat R_{bci}(Q)\Bigg[6 C^{b}\Big[12282 i \widehat G_{a}{}^{c}\\
&-473 i \varepsilon^{def}{}_{a}{}^{c} \widehat H_{def}\Big]\\
&+C_{a}\Big[-28110 i \widehat G^{bc}\\
&+3691 i \varepsilon^{defbc} \widehat H_{def}\Big]\\
&+3\Big[3534 i \widehat H_{a}{}^{bc}\\
&+2125 i \varepsilon^{de}{}_{a}{}^{bc} \widehat G_{de}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{8 i \zeta}{L^{2}} E_{a}\overline{\mathcal D^{a}(\varphi^{i})}\chi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 \zeta}{L^{2}} L_{ij} \varepsilon_{abcde}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\chi^{j}\Bigg[-4 i T^{de}\\
&+i \widehat G^{de}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{4}} \varepsilon_{abcde}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\mathcal D^{d}(\varphi^{j})\Bigg[-i E^{e} L_{ij}\\
&-i L_{j}{}^{k} \mathcal D^{e}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \zeta}{L^{2}} \varepsilon_{abcde}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\mathcal D^{d}\mathcal D^{e}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{2}}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\mathcal D_{c}(\varphi_{i})\Bigg[-8 i T_{ab}\\
&+i \widehat G_{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L} \varepsilon_{abc}{}^{d}{}_{e}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\phi_{di}\Bigg[\frac{i}{2 L} E^{e}\\
&+\frac{\sqrt{2} i}{4} V^{e}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta g}{64} \varepsilon_{abc}{}^{de}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{bc}\widehat R_{dei}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 \zeta}{L^{2}} L_{ij}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\chi^{j}\Bigg[12 T_{ab}\\
&-\widehat G_{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{2 L^{2}} \varepsilon^{de}{}_{abc} \widehat G_{de}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\mathcal D^{c}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}} L_{ij}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\mathcal D_{b}(\varphi^{j})\Bigg[\frac{2}{L} E_{a}\\
&+\sqrt{2} V_{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\phi_{ai}\Bigg[-\frac{1}{L} E_{b}\\
&-\frac{\sqrt{2}}{2} V_{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\phi_{bi}\Bigg[\frac{1}{L} E_{a}\\
&+\frac{\sqrt{2}}{2} V_{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 \beta g}{32} C_{e} \varepsilon^{e}{}_{ab}{}^{cd}\overline{\mathcal D^{a}(\varphi^{i})}\gamma^{b}\widehat R_{cdi}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{2}}\overline{\mathcal D^{a}(\varphi^{i})}\mathcal D^{b}(\varphi_{i})\Bigg[-16 i T_{ab}\\
&+i \widehat G_{ab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 i N \zeta}{L^{2}}\overline{\mathcal D^{a}(\varphi^{i})}\phi_{ai}
\end{aligned}
```

```math
\begin{aligned}
{}&+\overline{\mathcal D^{a}(\varphi^{i})}\widehat R_{bai}(Q)\Bigg[-\frac{13 i \beta g}{16} C^{b}\\
&+\frac{i \zeta}{L^{2}} E^{b}\\
&+\frac{\sqrt{2} i \zeta}{2 L} V^{b}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{36}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\psi_{ai}\Bigg[2 C_{c}\Big[-3 i \widehat G_{bd}\\
&+i \varepsilon^{efg}{}_{bd} \widehat H_{efg}\Big]\\
&+3 i C_{b} \widehat G_{cd}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{12}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\psi_{bi}\Bigg[2 i \widehat H_{acd}\\
&-i C_{a} \widehat G_{cd}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{36}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\psi_{di}\Bigg[2 C_{a}\Big[-3 i \widehat G_{bc}\\
&+i \varepsilon^{efg}{}_{bc} \widehat H_{efg}\Big]\\
&+3\Big[4 i \widehat H_{abc}\\
&+i \varepsilon^{ef}{}_{abc} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{12}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\psi_{ei}\Bigg[-i \varepsilon^{f}{}_{acd}{}^{e} \widehat G_{fb}\\
&-2 i C_{f} \varepsilon^{fg}{}_{cd}{}^{e} \widehat H_{gab}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{2} L_{ij} \varepsilon_{abcd}{}^{e}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\psi_{e}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{4} C_{e} \varepsilon^{e}{}_{abcd}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{16} C_{f} \varepsilon^{f}{}_{acd}{}^{e}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\widehat R_{ebi}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{64}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{cd}\widehat R_{efi}(Q)\Bigg[-2 i C^{e} \varepsilon_{abcd}{}^{f}\\
&-i C_{a} \varepsilon_{bcd}{}^{ef}\\
&-i C_{b} \varepsilon_{acd}{}^{ef}\\
&-2 i C_{c} \varepsilon_{abd}{}^{ef}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{18}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{c}\psi_{ai}\Bigg[-3 \widehat G_{bc}\\
&+\varepsilon^{def}{}_{bc} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{3} C_{d} \widehat H^{d}{}_{ac}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{c}\psi_{bi}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{12} C_{d}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{c}\psi_{ci}\Bigg[-4 \widehat H^{d}{}_{ab}\\
&-\varepsilon^{def}{}_{ab} \widehat G_{ef}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{12}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{c}\psi_{di}\Bigg[C_{c}\Big[4 \widehat H_{ab}{}^{d}\\
&+\varepsilon^{ef}{}_{ab}{}^{d} \widehat G_{ef}\Big]\\
&+2\Big[-2 C_{b} \widehat H_{ac}{}^{d}\\
&+C_{e} \varepsilon^{ef}{}_{ac}{}^{d} \widehat G_{fb}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\beta g C_{e} L_{ij} \varepsilon^{e}{}_{abc}{}^{d}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\gamma^{c}\psi_{d}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{18} C_{c}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\psi_{ai}\Bigg[-3 i \widehat G^{c}{}_{b}\\
&-i \varepsilon^{cdef}{}_{b} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-i \beta g C_{b} L_{ij}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\psi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+i \beta g C_{a} L_{ij}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{36}\overline{\mathcal D^{a}\mathcal D^{b}(\psi^{i})}\psi_{ci}\Bigg[2 C_{a}\Big[-3 i \widehat G_{b}{}^{c}\\
&+i \varepsilon^{def}{}_{b}{}^{c} \widehat H_{def}\Big]\\
&+3\Big[4 i \widehat H_{ab}{}^{c}\\
&+i \varepsilon^{de}{}_{ab}{}^{c} \widehat G_{de}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+i \beta g C_{a} L_{ij}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{bc}\psi_{c}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta g L_{ij}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{b}\psi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta}{3} C_{d} \widehat H^{d}{}_{a}{}^{c}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{b}\psi_{ci}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta g}{3} C_{a}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{b}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{6} C_{d} \widehat G^{d}{}_{c}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{cb}\psi_{ai}
\end{aligned}
```

```math
\begin{aligned}
{}&+i \beta g C_{c} L_{ij}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{cb}\psi_{a}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{6}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{cb}\psi_{di}\Bigg[-2 i \widehat H_{ac}{}^{d}\\
&+i C_{a} \widehat G_{c}{}^{d}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{16} C_{f} \varepsilon^{f}{}_{ac}{}^{de}\overline{\mathcal D^{a}\mathcal D_{b}(\psi^{i})}\gamma^{cb}\widehat R_{dei}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 i \beta}{3} C_{c}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\mathcal D^{c}\mathcal D_{b}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{3 i \beta g}{4} L_{ij}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\mathcal D_{b}(\psi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{5 i \beta g}{6}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\mathcal D_{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 i \beta}{2} C_{c}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\mathcal D_{b}\mathcal D^{c}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\psi_{bi}\Bigg[\frac{1}{288} C_{c}\Big[8 \widehat H^{c}{}_{de}\Big[9 i \widehat G^{de}\\
&-i \varepsilon^{defgh} \widehat H_{fgh}\Big]\\
&+\varepsilon^{c}{}_{defg}\Big[32 i \mathcal D^{d}(\widehat H^{efg})\\
&-27 i \widehat G^{de} \widehat G^{fg}\Big]\\
&+48 i \mathcal D^{d}(\widehat G^{c}{}_{d})\Big]\\
&+\frac{1}{36} \widehat H_{cde}\Big[-2 i \widehat H^{cde}\\
&-i \varepsilon^{fgcde} \widehat G_{fg}\Big]\\
&-\frac{i g (13 L^{2} g + 22 N)}{24}\\
&-\frac{5 i}{12} \Box^c(\sigma)\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta g}{2} C_{c} \mathcal D^{c}(L_{ij})\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{3} \widehat R_{b}{}^{c}{}_{ij}(V)\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ab}\psi_{c}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{5 \beta}{6}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\Box^c(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta g C_{b}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\mathcal D^{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{173 \beta}{256} C^{c}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\mathcal D^{b}(\widehat R_{cbi}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\psi_{bi}\Bigg[2 C_{c}\Big[\widehat H_{def}\Big[\varepsilon^{cgdef} \widehat G_{g}{}^{b}\\
&+\varepsilon^{gdefb} \widehat G^{c}{}_{g}\Big]\\
&+24\Big[-3 \mathcal D^{b}\mathcal D^{c}(\sigma)\\
&+3 \mathcal D^{c}\mathcal D^{b}(\sigma)\\
&-2 \mathcal D^{d}(\widehat H^{c}{}_{d}{}^{b})\Big]\Big]\\
&+8 \widehat H^{b}{}_{cd}\Big[9 \widehat G^{cd}\\
&-\varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&+\varepsilon^{b}{}_{cdef}\Big[32 \mathcal D^{c}(\widehat H^{def})\\
&-27 \widehat G^{cd} \widehat G^{ef}\Big]\\
&-48 \mathcal D^{c}(\widehat G_{c}{}^{b})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\beta\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\psi_{b}{}^{j}\Bigg[C_{c}\Big[\frac{1}{3} \widehat R^{cb}{}_{ij}(V)\\
&+\frac{g}{4} L_{ij} \widehat G^{cb}\Big]\\
&+\frac{g}{2} \mathcal D^{b}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{35 \beta g^{2}}{12} L_{ij}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\varphi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{55296}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{a}\widehat R_{bci}(Q)\Bigg[3 C_{d}\Big[1174 \widehat H^{dbc}\\
&+803 \varepsilon^{defbc} \widehat G_{ef}\Big]\\
&+1254 \widehat G^{bc}\\
&-8167 \varepsilon^{defbc} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{6} C_{b}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\Box^c(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{197 i \beta}{768} C_{f} \varepsilon^{f}{}_{bc}{}^{de}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\mathcal D^{c}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\psi_{ci}\Bigg[24 C_{d}\Big[-7 i \mathcal D^{c}(\widehat G^{d}{}_{b})\\
&-7 i \mathcal D^{d}(\widehat G_{b}{}^{c})\\
&+7 i \mathcal D_{b}(\widehat G^{dc})\\
&+3 i \widehat G^{d}{}_{e} \widehat H^{e}{}_{b}{}^{c}\\
&-3 i \widehat G_{eb} \widehat H^{dec}\\
&+3 i \widehat G_{e}{}^{c} \widehat H^{de}{}_{b}\Big]\\
&+C_{b}\Big[8 \widehat H^{c}{}_{de}\Big[9 i \widehat G^{de}\\
&-i \varepsilon^{fghde} \widehat H_{fgh}\Big]\\
&+\varepsilon^{c}{}_{defg}\Big[32 i \mathcal D^{d}(\widehat H^{efg})\\
&-27 i \widehat G^{de} \widehat G^{fg}\Big]\\
&-48 i \mathcal D^{d}(\widehat G_{d}{}^{c})\Big]\\
&+2\Big[\widehat H_{def}\Big[i \varepsilon^{gdefc} \widehat G_{gb}\\
&-i \varepsilon^{gdef}{}_{b} \widehat G_{g}{}^{c}\Big]\\
&+24\Big[3 i \mathcal D^{c}\mathcal D_{b}(\sigma)\\
&-2 i \mathcal D^{d}(\widehat H_{db}{}^{c})\\
&-3 i \mathcal D_{b}\mathcal D^{c}(\sigma)\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{12}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\psi_{c}{}^{j}\Bigg[L_{ij}\Big[-3 i \widehat G_{b}{}^{c}\\
&-8 i C_{d} \widehat H^{d}{}_{b}{}^{c}\Big]\\
&+6 i C_{b} \mathcal D^{c}(L_{ij})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{11 i \beta g^{2}}{12} C_{b} L_{ij}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\varphi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{5 i \beta g}{72} C_{c} \varepsilon^{cdef}{}_{b} \widehat H_{def}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{55296}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{ba}\widehat R_{cdi}(Q)\Bigg[4 C^{c}\Big[-12774 i \widehat G_{b}{}^{d}\\
&+151 i \varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Big]\\
&+3\Big[C_{b}\Big[4314 i \widehat G^{cd}\\
&-929 i \varepsilon^{efgcd} \widehat H_{efg}\Big]\\
&-6166 i \widehat H_{b}{}^{cd}\\
&-2055 i \varepsilon^{ef}{}_{b}{}^{cd} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{288}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{bc}\mathcal D^{a}(\psi_{i})\Bigg[3 C_{d}\Big[-44 i \widehat H^{d}{}_{bc}\\
&-5 i \varepsilon^{def}{}_{bc} \widehat G_{ef}\Big]\\
&+4\Big[-18 i \widehat G_{bc}\\
&+5 i \varepsilon^{def}{}_{bc} \widehat H_{def}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{95 i \beta}{768} C_{f} \varepsilon^{f}{}_{bc}{}^{de}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{bc}\mathcal D^{a}(\widehat R_{dei}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \beta}{2} C_{b}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{bc}\mathcal D_{c}\mathcal D^{a}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta g}{4} C_{b} \mathcal D^{a}(L_{ij})\overline{\mathcal D_{a}(\psi^{i})}\gamma^{bc}\psi_{c}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta g}{3} C_{b} L_{ij}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{b}\mathcal D^{a}(\psi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{7 \beta g}{6} C_{b}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{b}\mathcal D^{a}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{4 \beta}{3}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{b}\mathcal D^{a}\mathcal D_{b}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta}{6}\overline{\mathcal D_{a}(\psi^{i})}\gamma^{b}\mathcal D_{b}\mathcal D^{a}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{\beta g}{4} \mathcal D^{a}(L_{ij})\overline{\mathcal D_{a}(\psi^{i})}\gamma^{b}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+3 i \beta g L_{ij}\overline{\mathcal D_{a}(\psi^{i})}\mathcal D^{a}(\psi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{13 i \beta g}{6}\overline{\mathcal D_{a}(\psi^{i})}\mathcal D^{a}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{5 i \beta}{2} C_{b}\overline{\mathcal D_{a}(\psi^{i})}\mathcal D^{a}\mathcal D^{b}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{4 i \beta}{3} C_{b}\overline{\mathcal D_{a}(\psi^{i})}\mathcal D^{b}\mathcal D^{a}(\psi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\chi^{j}\Bigg[i \mathcal D^{a}(L_{ij})\\
&+\frac{i}{L^{2}} L_{i}{}^{k} L_{j}{}^{l} \mathcal D^{a}(L_{kl})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{ab}\chi^{j}\Bigg[i \mathcal D_{b}(L_{ij})\\
&-\frac{i}{L^{2}} L_{i}{}^{k} L_{j}{}^{l} \mathcal D_{b}(L_{kl})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 i \zeta}{L^{2}} L_{ij}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{ab}\mathcal D_{b}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \zeta (g + \frac{2 N}{L^{2}})}{L^{2}} L_{ij}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{ab}\mathcal D_{b}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 i N \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{ab}\phi_{bi}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{a}\Box^c(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-8 \zeta (g + \frac{9 N}{L^{2}})\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{a}\chi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{4}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{a}\mathcal D_{b}(\varphi^{j})\Bigg[-L_{i}{}^{k} \mathcal D^{b}(L_{jk})\\
&+L_{j}{}^{k} \mathcal D^{b}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{8 i \zeta}{L^{2}} E_{b}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{ba}\chi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \zeta}{2 L^{2}} \widehat G_{bc}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{bc}\mathcal D^{a}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\zeta}{L^{3}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{b}\mathcal D^{a}(\varphi^{j})\Bigg[-\sqrt{2} L_{ij} V_{b}\\
&+\frac{2}{L} L_{j}{}^{k} \mathcal D_{b}(L_{ik})\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{2 \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{b}\mathcal D^{a}\mathcal D_{b}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{2 \zeta}{L^{2}}\overline{\mathcal D_{a}(\varphi^{i})}\gamma^{b}\mathcal D_{b}\mathcal D^{a}(\varphi_{i})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 i \zeta}{L^{2}} L_{ij}\overline{\mathcal D_{a}(\varphi^{i})}\mathcal D^{a}(\chi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i g \zeta}{L^{2}} L_{ij}\overline{\mathcal D_{a}(\varphi^{i})}\mathcal D^{a}(\varphi^{j})
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{18} C_{d}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{ac}\psi_{ci}\Bigg[-3 i \widehat G^{d}{}_{b}\\
&-i \varepsilon^{defg}{}_{b} \widehat H_{efg}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-i \beta g C_{b} L_{ij}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{ac}\psi_{c}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&-\beta g L_{ij}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{a}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{18}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{a}\psi_{ci}\Bigg[3 \widehat G_{b}{}^{c}\\
&-\varepsilon^{def}{}_{b}{}^{c} \widehat H_{def}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{2} C_{b}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{a}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{6} C_{d} \widehat G^{d}{}_{c}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{ca}\psi_{bi}
\end{aligned}
```

```math
\begin{aligned}
{}&-i \beta g C_{c} L_{ij}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{ca}\psi_{b}{}^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{18}\overline{\mathcal D_{a}\mathcal D^{b}(\psi^{i})}\gamma^{ca}\psi_{di}\Bigg[C_{c}\Big[3 i \widehat G_{b}{}^{d}\\
&-i \varepsilon^{efg}{}_{b}{}^{d} \widehat H_{efg}\Big]\\
&-3 i C_{b} \widehat G_{c}{}^{d}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta}{6} C_{d} \widehat G^{dc}\overline{\mathcal D_{a}\mathcal D_{b}(\psi^{i})}\gamma^{ab}\psi_{ci}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{5 i \beta g}{6}\overline{\mathcal D_{a}\mathcal D_{b}(\psi^{i})}\gamma^{ab}\varphi_{i}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{16 i \zeta}{L^{2}} L_{ij}\overline{\mathcal D_{a}\mathcal D_{b}(\varphi^{i})}\gamma^{ab}\chi^{j}
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{1024}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{cd}\widehat R^{ab}{}_{i}(Q)\Bigg[5 C_{e}\Big[-18 i \widehat H^{e}{}_{cd}\\
&+i \varepsilon^{efg}{}_{cd} \widehat G_{fg}\Big]\\
&+3\Big[-3 i \widehat G_{cd}\\
&+i \varepsilon^{efg}{}_{cd} \widehat H_{efg}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{2048}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{cd}\widehat R_{efi}(Q)\Bigg[C_{g}\Big[2 i \varepsilon^{ab}{}_{d}{}^{ef} \widehat G^{g}{}_{c}\\
&-14 i \varepsilon^{b}{}_{cd}{}^{ef} \widehat G^{ga}\\
&+i \varepsilon^{gabef} \widehat G_{cd}\\
&+8 i \varepsilon^{gb}{}_{cd}{}^{f} \widehat G^{ae}\\
&-4 i \varepsilon^{gb}{}_{d}{}^{ef} \widehat G^{a}{}_{c}\\
&-35 i \varepsilon^{g}{}_{cd}{}^{ef} \widehat G^{ab}\Big]\\
&+2\Big[C_{c}\Big[7 i \varepsilon^{gabef} \widehat G_{gd}\\
&+22 i \varepsilon^{gb}{}_{d}{}^{ef} \widehat G_{g}{}^{a}\Big]\\
&+C^{a}\Big[6 i \varepsilon^{gb}{}_{d}{}^{ef} \widehat G_{gc}\\
&-19 i \varepsilon^{g}{}_{cd}{}^{ef} \widehat G_{g}{}^{b}\Big]\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i \beta g}{192} C^{a} L_{ij} \varepsilon^{b}{}_{cd}{}^{ef}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{cd}\widehat R_{ef}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{23 i \beta g}{3072} C_{f} L_{ij} \varepsilon^{fa}{}_{cd}{}^{e}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{cd}\widehat R_{e}{}^{bj}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{128}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{cd}\widehat R_{e}{}^{b}{}_{i}(Q)\Bigg[C^{a}\Big[27 i \widehat H_{cd}{}^{e}\\
&-i \varepsilon^{fg}{}_{cd}{}^{e} \widehat G_{fg}\Big]\\
&-3 i C_{f} \varepsilon^{fg}{}_{cd}{}^{e} \widehat G_{g}{}^{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{3 \alpha}{4}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{c}\mathcal D_{c}(\widehat R^{ab}{}_{i}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{17 \beta g}{1024} C_{c} L_{ij}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{c}\widehat R^{abj}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{15 \beta}{512} \varepsilon^{fb}{}_{c}{}^{de} \widehat G_{f}{}^{a}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{c}\widehat R_{dei}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta g}{2048} L_{ij} \varepsilon^{ab}{}_{c}{}^{de}\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{c}\widehat R_{de}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\overline{\widehat R_{ab}{}^{i}(Q)}\gamma^{c}\widehat R_{d}{}^{b}{}_{i}(Q)\Bigg[C_{c}\Big[-\alpha T^{ad}\\
&-\frac{65 \beta}{256} \widehat G^{ad}\\
&+\frac{65 \beta}{768} \varepsilon^{efgad} \widehat H_{efg}\Big]\\
&+C^{a}\Big[3 \alpha T_{c}{}^{d}\\
&-\frac{3 \beta}{32} \widehat G_{c}{}^{d}\\
&+\frac{\beta}{32} \varepsilon^{efg}{}_{c}{}^{d} \widehat H_{efg}\Big]\\
&+\frac{3 \beta}{256}\Big[-14 \widehat H^{a}{}_{c}{}^{d}\\
&-\varepsilon^{efa}{}_{c}{}^{d} \widehat G_{ef}\Big]\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{3 i \alpha}{2} C^{c}\overline{\widehat R_{ab}{}^{i}(Q)}\mathcal D^{a}(\widehat R_{c}{}^{b}{}_{i}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{i \alpha}{2} C_{c}\overline{\widehat R_{ab}{}^{i}(Q)}\mathcal D^{c}(\widehat R^{ab}{}_{i}(Q))
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{i g (128 \alpha + \beta)}{1024} L_{ij}\overline{\widehat R_{ab}{}^{i}(Q)}\widehat R^{abj}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\frac{\beta}{512}\overline{\widehat R_{ab}{}^{i}(Q)}\widehat R_{cdi}(Q)\Bigg[C^{a}\Big[184 i \widehat H^{bcd}\\
&+7 i \varepsilon^{efbcd} \widehat G_{ef}\Big]\\
&-26 i C_{e} \varepsilon^{efbcd} \widehat G_{f}{}^{a}\Bigg]
\end{aligned}
```

```math
\begin{aligned}
{}&-\frac{5 i \beta g}{6144} C_{e} L_{ij} \varepsilon^{eabcd}\overline{\widehat R_{ab}{}^{i}(Q)}\widehat R_{cd}{}^{j}(Q)
\end{aligned}
```

```math
\begin{aligned}
{}&+\overline{\widehat R_{ab}{}^{i}(Q)}\widehat R_{c}{}^{b}{}_{i}(Q)\Bigg[\frac{\beta}{512} C_{d}\Big[176 i \widehat H^{dac}\\
&-23 i \varepsilon^{defac} \widehat G_{ef}\Big]\\
&-2 i \alpha T^{ac}\\
&-\frac{19 i \beta}{64} \widehat G^{ac}\\
&+\frac{19 i \beta}{192} \varepsilon^{defac} \widehat H_{def}\Bigg]
\end{aligned}
```
