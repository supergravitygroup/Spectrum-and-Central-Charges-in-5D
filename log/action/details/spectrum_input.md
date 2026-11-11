# LOG action and conventions used for the AdS5 spectrum

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="1-fixed-total-action-and-common-conventions"></a>

## Fixed total action and common conventions

```math
\boxed{S=S_{2\text{-der}}+\alpha S_{\mathrm{Log}},\qquad
\alpha\ne0,\quad g\ne0,}
\qquad
S_I=\frac1{2\kappa_5^2}\int_M d^5x\,e\,\ell_I .
\tag{A1}
```

The action retains all bosonic dependence and the free parameters $`\alpha,g,\kappa_5`$, through physical fermion degrees zero and two. There is no expansion in $`\alpha`$. The common gravitational prefactor is $`(2\kappa_5^2)^{-1}`$. The two-derivative source's internal factor $`-2`$ is retained; no additional factor multiplies the LOG density.

Here $`S`$ denotes the specified action through two fermions. The unspecified completion satisfies $`S_{\mathrm{full}}=S+O(\text{four physical fermions})`$. Off shell means that no independent-field equation of the target gauged Dilaton–Weyl theory is used to define this action. Relations used to construct that target multiplet are not eliminations of its auxiliary fields.

## Sources, common fields, and fermion order

The two-derivative input is [the component density](05_gauged_two_derivative_full_fermionic_action_from_1608_map.md), equations (4.33)–(4.37), (4.47)–(4.49), (5.1), and (5.10). The LOG input is the [compact component construction](construction.md), with the substituted multiplet, current and BF density. The authoritative convention file is the project-root `CONVENTIONS.md`. Source instructions and certification labels are not treated as new requests or independent mathematical proofs.

The compensator subscript in the LOG source is removed by the following renaming only:

```math
(L_c^{ij},\varphi_c^i,N_c,E_c^a,E_{c\mu\nu\rho})
=(L^{ij},\varphi^i,N,E^a,E_{\mu\nu\rho}).
\tag{A2}
```

The composite LOG multiplet $`(L_{\log}^{ij},\varphi_{\log}^i,N_{\log},E_{\log}^a)`$ is distinct from the independent linear multiplet. Both inputs already use the following common gauge:

```math
\sigma=1,\quad\psi^i=0,\quad b_\mu=0,\quad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\quad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\quad\delta_{ij}V_\mu^{\prime\,ij}=0.
\tag{A3}
```

Since $`L^{ij}L_{ij}=L^2`$ and the source map contains $`L^{-1}`$, its domain is $`L\ne0`$; $`L`$ is not fixed. The independent fields are

```math
e_\mu{}^a,\ \psi_\mu^i,\ C_\mu,\ B_{\mu\nu},\ L,\ \varphi^i,
\ N,\ E_{\mu\nu\rho},\ V_\mu,\ V_\mu^{\prime\,ij}
\tag{A4}
```

as displayed. $`E_a`$ represents the same degrees of freedom as the three-form defined below. The dilatino $`\psi^i`$ is distinct from the gravitino $`\psi_\mu^i`$. Covariant derivatives of the gauge-fixed dilatino remain connection composites, not independent fields.

The projection $`[\ ]_{\le2}`$ counts implicit as well as explicit fermions. For bosonic covariants $`B=B^{(0)}+B^{(2)}+\cdots`$ and fermionic covariants $`u=u^{(1)}+u^{(3)}+\cdots`$,

```math
\begin{aligned}
\left[\prod_rB_r\right]_{\le2}
&=\prod_rB_r^{(0)}+\sum_sB_s^{(2)}\prod_{r\ne s}B_r^{(0)},\\
[B\bar u\Gamma v]_{\le2}
&=B^{(0)}\overline{u^{(1)}}\Gamma v^{(1)}.
\end{aligned}\tag{A5}
```

Hatted fields and full derivatives therefore remain in the formulas, while their products are projected to the stated fermion order.

## Spinors, metric, and curvature

```math
\begin{gathered}
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\quad a,\mu=0,\ldots,4,
\quad i,j=1,2,\quad e=\det(e_\mu{}^a)=\sqrt{-g},\\
\{\gamma^a,\gamma^b\}=2\eta^{ab},\quad
\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]},\quad
X_{[ab]}=\tfrac12(X_{ab}-X_{ba}),\\
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\quad
\gamma\!\cdot\!X=\gamma^{a_1\cdots a_p}X_{a_1\cdots a_p},\quad
\not{\mathcal D}=\gamma^a\mathcal D_a,\\
\epsilon_{12}=\epsilon^{12}=1,\quad X^i=\epsilon^{ij}X_j,
\quad X_i=X^j\epsilon_{ji},\quad
\bar X\Gamma Y=\bar X^i\Gamma Y_i .
\end{gathered}\tag{A6}
```

The dot contraction contains no $`1/p!`$. Spacetime $`\varepsilon`$ and doublet $`\epsilon`$ are distinct. The orientation-covariant identity $`\gamma^{abcde}=i\varepsilon^{abcde}`$ replaces a numerical orientation choice; epsilon and the Clifford volume element cannot be changed independently.

Both sources use a linear Majorana bar. Their common additional definition fixes this operation where the root conventions do not explicitly do so:

```math
\bar u=u^T\mathsf C,\quad \overline{cu}=c\bar u,\quad
\overline{\gamma_a u}=\bar u\gamma_a,\quad
\overline{\gamma_{ab}u}=-\bar u\gamma_{ab}.
\tag{A7}
```

In particular, $`i`$ is not complex-conjugated by this bar. Fermions are Grassmann odd. The signs are checked by

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y^j&=t_n\bar Y^j\gamma_{(n)}X^i,
& (t_0,t_1,t_2,t_3,t_4,t_5)&=(+,+,-,-,+,+),\\
\bar X^i\gamma_{(n)}Y_i
&=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j,\\
L^{ij}&=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},
&L_i{}^j&=\epsilon^{jk}L_{ik},\\
\epsilon^{ik}\epsilon^{j\ell}\frac{L}{\sqrt2}\delta_{k\ell}
&=\frac{L}{\sqrt2}\delta^{ij},
&L^{ij}L_{ij}&=\frac{L^2}{2}\delta^{ij}\delta_{ij}=L^2.
\end{aligned}\tag{A8}
```

The common connections and curvatures are given below. $`\mathcal R_{\mu\nu}`$ is the Ricci contraction of the primed supercovariant curvature and differs from $`R_{\mu\nu}(\omega)`$ in the presence of fermions.

```math
\begin{aligned}
\omega_\mu{}^{ab}={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+2e_\mu{}^{[a}b^{b]}
+\tfrac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\tfrac14\bar\psi^a\gamma_\mu\psi^b,\\
R_{\mu\nu}{}^{ab}(\omega)={}&2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
\widehat R'_{\mu\nu}{}^i(Q)={}&2\partial_{[\mu}\psi_{\nu]}^i
+\tfrac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i
+b_{[\mu}\psi_{\nu]}^i-2V_{[\mu}^{ij}\psi_{\nu]j}
+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i={}&\tfrac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\tfrac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)={}&\widehat R'_{\mu\nu}{}^i(Q)
-2i\gamma_{[\mu}\phi_{\nu]}^i,\\
\widehat R'_{\mu\nu}{}^{ab}(M)={}&R_{\mu\nu}{}^{ab}(\omega)
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\tfrac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\mathcal R_{\mu\nu}={}&\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad\mathcal R=\mathcal R_\mu{}^\mu,\\
f_\mu{}^a={}&-\tfrac16\mathcal R_\mu{}^a+\tfrac1{48}e_\mu{}^a\mathcal R,
\qquad f_a{}^a=-\tfrac1{16}\mathcal R,\\
\widehat R_{\mu\nu}{}^{ab}(M)={}&\widehat R'_{\mu\nu}{}^{ab}(M)
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\qquad
\widehat C_{abcd}=\widehat R(M)_{abcd},\\
\widehat R_{\mu\nu}^{ij}(V)={}&2\partial_{[\mu}V_{\nu]}^{ij}
-2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{A9}
```

The explicit $`\chi`$ term has coefficient $`+8`$ and the same index order in both sources; no extra shift of $`f`$ is made. The trace check is

```math
\begin{aligned}
f_a{}^a&=(-\tfrac16+\tfrac5{48})\mathcal R=-\tfrac1{16}\mathcal R,\\
\widehat R(M)_{ab}{}^{cb}
&=\mathcal R_a{}^c+6f_a{}^c+2\delta_a{}^cf_b{}^b\\
&=\mathcal R_a{}^c-\mathcal R_a{}^c
+(\tfrac18-\tfrac18)\delta_a{}^c\mathcal R=0.
\end{aligned}\tag{A10}
```

The conditions $`R(P)=0`$ and $`\gamma^a\widehat R(Q)_{ab}=0`$ define dependent connections. Neither $`\mathcal R_{ab}`$ nor $`f_{ab}`$ is assumed symmetric with fermions present. The supercovariant $`\widehat C`$ is not replaced by the ordinary Weyl tensor.

For a separate gamma-trace check, define $`A_b^i=\gamma^a\widehat R'_{ab}{}^i(Q)`$ and $`B^i=\gamma^{ab}\widehat R'_{ab}{}^i(Q)`$. Substituting $`\gamma^bA_b^i=-B^i`$ and $`\gamma^a\gamma_b\phi_a=2\phi_b-\gamma_b\gamma^a\phi_a`$ gives

```math
\begin{aligned}
\phi_b^i&=-\frac i3A_b^i-\frac i{24}\gamma_bB^i,
\qquad \gamma^b\phi_b^i=\frac i3B^i-\frac{5i}{24}B^i
=\frac i8B^i,\\
\gamma^a\widehat R_{ab}{}^i(Q)
&=A_b^i-3i\phi_b^i-i\gamma_b\gamma^a\phi_a^i\\
&=A_b^i-A_b^i-\frac18\gamma_bB^i+\frac18\gamma_bB^i=0.
\end{aligned}\tag{A10b}
```

## Differential forms and explicit convention conversions

```math
\begin{gathered}
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
\varepsilon^{abcdf},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}=e\varepsilon^{\mu\nu\rho\sigma\lambda},\\
\varepsilon_{a_1\cdots a_n b_1\cdots b_p}
\varepsilon^{a_1\cdots a_n c_1\cdots c_p}
=-n!p!\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p},\qquad n+p=5,\\
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},\quad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}
+\tfrac32 C_{[\mu}G_{\nu\rho]}+\tfrac g2E_{\mu\nu\rho},\\
\widehat G_{\mu\nu}=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\tfrac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}=H_{\mu\nu\rho}
-\tfrac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\tfrac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi.
\end{gathered}\tag{A11}
```

The component conventions are $`C=C_\mu dx^\mu`$, $`B=B_{\mu\nu}dx^\mu\wedge dx^\nu/2`$, and $`E_3=E_{\mu\nu\rho}dx^\mu\wedge dx^\nu\wedge dx^\rho/3!`$. Hence

```math
G=dC,\quad H=dB+\tfrac12C\wedge G+\tfrac g2E_3,
\quad dH=\tfrac12G\wedge G+\tfrac g2dE_3,
\tag{A12}
```

Under $`\delta E_3=d\Lambda_2`$, $`\delta B=d\Lambda_1-\Lambda G/2-g\Lambda_2/2`$, and $`\delta C=d\Lambda`$, direct substitution gives $`\delta H=d\Lambda\wedge G/2-d\Lambda\wedge G/2-g\,d\Lambda_2/2+g\,d\Lambda_2/2=0`$.

Temporarily label the source's two-index shorthand $`\widehat H^{\mathrm{src}(2)}_{ab}`$. Its conversion is

```math
\begin{aligned}
\widehat H^{\mathrm{src}(2)}_{ab}
&=-\tfrac1{12}\varepsilon_{abcde}\widehat H^{cde},\\
\varepsilon^{abcde}\widehat H^{\mathrm{src}(2)}_{ab}
&=-\tfrac1{12}(-2!3!)\delta_{[f}^c\delta_g^d\delta_{h]}^e
\widehat H^{fgh}=\widehat H^{cde},\\
\widehat H^{\mathrm{src}(2)}_{ab}\widehat H_{\mathrm{src}(2)}^{ab}
&=\tfrac1{144}(-2!3!)\widehat H_{cde}\widehat H^{cde}
=-\tfrac1{12}\widehat H_{cde}\widehat H^{cde},\\
\widehat G_{ab}\widehat H_{\mathrm{src}(2)}^{ab}
&=-\tfrac1{12}\widehat G^{ab}\varepsilon_{abcde}\widehat H^{cde},\\
\tfrac18(\widehat G_{ab}-2\widehat H^{\mathrm{src}(2)}_{ab})
&=\tfrac18\left(\widehat G_{ab}+\tfrac16\varepsilon_{abcde}\widehat H^{cde}\right).
\end{aligned}\tag{A13}
```

This invertible substitution is applied to every LOG term. Since $`\mathcal D\varepsilon=0`$, ordered derivatives transform in the same way:

```math
\mathcal D_{a_1}\cdots\mathcal D_{a_n}\widehat H^{\mathrm{src}(2)}_{bc}
=-\tfrac1{12}\varepsilon_{bcdef}
\mathcal D_{a_1}\cdots\mathcal D_{a_n}\widehat H^{def}.
\tag{A14}
```

This expands a shorthand for the same three-form; it is not a dynamical dualization. Every $`\widehat H`$ in the final component register has three indices.

The independent linear multiplet's form and current definitions are

```math
\begin{aligned}
E^{\mu\nu}&=-\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda},\qquad
E_{\mu\nu\rho}=\varepsilon_{\mu\nu\rho\sigma\lambda}E^{\sigma\lambda},\\
P^a&=E^a+\tfrac i2\bar\psi_b\gamma^{ba}\varphi
+\tfrac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},\\
P^\mu&=-\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}
=e^{-1}\partial_\nu(eE^{\mu\nu}),\\
E^\mu&=P^\mu-\tfrac i2\bar\psi_\nu\gamma^{\nu\mu}\varphi
-\tfrac14\bar\psi_\nu^i\gamma^{\mu\nu\rho}\psi_\rho^jL_{ij}
=-\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}.
\end{aligned}\tag{A15}
```

Composing the first two relations yields $`(-1/12)(-3!2!)\delta_{[\mu}^{\alpha}\delta_{\nu]}^{\beta}E^{\mu\nu}=E^{\alpha\beta}`$. This fixes the sign and normalization. A15 corrects the earlier mixing of epsilon tensors and density symbols in source equations (3.5), (3.6), and (3.10). The source was corrected on 2026-09-27: tensor epsilon carries no additional determinant, whereas $`e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}=\varepsilon^{\mu\nu\rho\sigma\lambda}`$. Equation (3.8) now uses $`e^{-1}\partial_\nu(eE^{\mu\nu})`$ for the divergence of the tensor $`E^{\mu\nu}`$; equation (3.10a) supplies the direct check.

For the ordinary field strength $`F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}`$, the product rule gives

```math
\begin{aligned}
eA_\mu P^\mu
&=-\tfrac1{12}e\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu\partial_\nu E_{\rho\sigma\lambda}\\
&=-\tfrac1{12}\partial_\nu
(e\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda})
+\tfrac1{12}e\varepsilon^{\mu\nu\rho\sigma\lambda}
(\partial_\nu A_\mu)E_{\rho\sigma\lambda}\\
&=-\tfrac1{12}\partial_\nu
(e\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda})
-\tfrac1{24}e\varepsilon^{\mu\nu\rho\sigma\lambda}
F_{\mu\nu}E_{\rho\sigma\lambda}\\
&=\tfrac12eF_{\mu\nu}E^{\mu\nu}
-\tfrac1{12}\partial_\nu
(e\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda}).
\end{aligned}\tag{A16}
```

The defining representative for $`S_{2\text{-der}}`$ is the source's field-strength representative (5.1)/(5.10); for $`S_{\mathrm{Log}}`$ it is the ordinary-current representative SC7-51. This fixes the local density without silently discarding a boundary term. The explicit difference from the two-derivative potential representative is

```math
S_{2\text{-der}}^{\mathrm{pot}}-S_{2\text{-der}}
=\frac1{2\kappa_5^2}\frac16\int_{\partial M}d\Sigma_\nu\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
A_{\mathrm{eff}\mu}E_{\rho\sigma\lambda},
\quad dA_{\mathrm{eff}}=F_{\mathrm{eff}}.
\tag{A17}
```

Here $`A_{\mathrm{eff}}`$ is only a local potential used to compare representatives, not an additional independent field. The boundary integral is not assumed to vanish.

## Full supercovariant derivatives and gauged composites

The source notations $`\square^C,\square^c,\Box^c`$ are identified with the single symbol $`\Box^c`$:

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-\delta_D(b_\mu)\Phi
-\delta_M(\omega_\mu)\Phi-\delta_U(V_\mu)\Phi
-\delta_Q(\psi_\mu)\Phi-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,
\quad\mathcal D_a=e_a{}^\mu\mathcal D_\mu,
\quad\Box^c\Phi=\mathcal D^a\mathcal D_a\Phi.
\tag{A18}
```

Each outer derivative acts on the actual descendant's Lorentz indices and Q/S/K transformations. Full supercovariance is retained. The gauge-evaluation bar is suppressed according to

```math
\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi
\equiv\left.(\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi)\right|_{\mathrm P}.
\tag{A19}
```

Composites are differentiated before the gauge A3 is imposed. In particular, $`\mathcal D_a\mathcal D_b\sigma`$ is not replaced by $`\partial_a\partial_b1`$, nor $`\mathcal D_a\psi^i`$ by $`\partial_a0`$. At the required fermion order the ungauged composites are

```math
\begin{aligned}
Y^{ij}&=\frac i{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac g{2\sigma}L^{ij},\\
T_{ab}&=\frac1{8\sigma}\widehat G_{ab}
+\frac1{48\sigma^2}\varepsilon_{abcde}\widehat H^{cde}
+\frac i{32\sigma^2}\bar\psi\gamma_{ab}\psi,\\
\chi^i&=\frac i{8\sigma}\not{\mathcal D}\psi^i
+\frac i{16\sigma^2}\not{\mathcal D}\sigma\,\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\,\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\,\psi^i
-\frac g{16\sigma^3}L^{ij}\psi_j+\frac g{8\sigma^2}\varphi^i
+O(\text{three fermions}),\\
D&=\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D\sigma)^2
-\frac1{16\sigma^2}\widehat G^2
-\frac1{8\sigma^2}\bar\psi\not{\mathcal D}\psi
+\frac1{4\sigma^2}Y^{ij}Y_{ij}
+\frac i{4\sigma^2}T_{ab}\bar\psi\gamma^{ab}\psi
-\frac{4i}{\sigma}\bar\psi\chi\\
&\quad-\frac{26}{3}T_{ab}T^{ab}
+\frac2\sigma\widehat G_{ab}T^{ab}+\frac g{4\sigma^2}N.
\end{aligned}\tag{A20}
```

The derivative $`\mathcal D`$ is even, so its Leibniz rule does not lower fermion degree. The three-fermion remainder in A20 starts at degree four in the action. Explicit derivative definitions include

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\tfrac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i
&=(\partial_\mu-\tfrac32b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\psi^i
-V_\mu^{ij}\psi_j+\tfrac14\gamma\!\cdot\!\widehat G\,\psi_\mu^i
+\tfrac i2\not{\mathcal D}\sigma\,\psi_\mu^i
+Y^{ij}\psi_{\mu j}-\sigma\gamma\!\cdot\!T\,\psi_\mu^i-\sigma\phi_\mu^i,\\
\mathcal D_\mu L^{ij}
&=(\partial_\mu-3b_\mu)L^{ij}+2V_\mu^{(i}{}_kL^{j)k}
-i\bar\psi_\mu^{(i}\varphi^{j)},\\
\mathcal D_\mu\varphi^i
&=(\partial_\mu-\tfrac72b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\varphi^i
-V_\mu^{ij}\varphi_j+\tfrac i2\not{\mathcal D}L^{ij}\psi_{\mu j}
+\tfrac i2\not E\psi_\mu^i-\tfrac12N\psi_\mu^i
+\gamma\!\cdot\!T L^{ij}\psi_{\mu j}-3L^{ij}\phi_{\mu j},\\
\mathcal D_\mu E_a
&=(\partial_\mu-4b_\mu)E_a-\omega_\mu{}^b{}_aE_b
+\tfrac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
+2\bar\psi_\mu\gamma^b\varphi T_{ba}+2\bar\phi_\mu\gamma_a\varphi,\\
\mathcal D_\mu N
&=(\partial_\mu-4b_\mu)N-\tfrac12\bar\psi_\mu\not{\mathcal D}\varphi
-\tfrac{3i}{2}\bar\psi_\mu\gamma\!\cdot\!T\varphi
-4i\bar\psi_\mu^i\chi^jL_{ij}-\tfrac{3i}{2}\bar\phi_\mu\varphi,\\
\mathcal D_\mu T_{ab}
&=(\partial_\mu-b_\mu)T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}
-\tfrac i2\bar\psi_\mu\gamma_{ab}\chi+\tfrac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
\end{aligned}\tag{A21}
```

The Q/S contributions in $`\mathcal D\varphi,\mathcal DE,\mathcal DN`$ follow from section 8 of the root conventions with $`\epsilon\mapsto\psi_\mu`$ and $`\eta\mapsto\phi_\mu`$, carrying an overall minus sign. The Lorentz-tensor sign follows from $`-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}=+2\omega_\mu{}^c{}_{[a}T_{b]c}`$.

The upper- and lower-doublet derivative conventions agree because

```math
\begin{aligned}
\epsilon_{ki}\epsilon_{\ell j}\,2V_\mu^{(k}{}_mL^{\ell)m}
&=-2V_{\mu(i}{}^kL_{j)k},\\
\mathcal D_\mu L_{ij}|_{\mathrm P}
&=\tfrac1{\sqrt2}\delta_{ij}\partial_\mu L
-\sqrt2L V'_{\mu(i}{}^k\delta_{j)k}
-i\bar\psi_{\mu(i}\varphi_{j)}.
\end{aligned}\tag{A22}
```

Thus the corrected lower-index two-derivative derivative and the upper-index LOG derivative are the same operator. Their gauge values and scalar box are

```math
\begin{aligned}
Y^{ij}|_{\mathrm P}&=-\tfrac g2L^{ij},\qquad
T_{ab}|_{\mathrm P}=\tfrac18\left(\widehat G_{ab}
+\tfrac16\varepsilon_{abcde}\widehat H^{cde}\right),\\
\mathcal D_a\psi^i|_{\mathrm P}
&=\tfrac18\gamma^{bc}\left(\widehat G_{bc}
-\tfrac16\varepsilon_{bcdef}\widehat H^{def}\right)\psi_a^i
-\tfrac g2L^{ij}\psi_{aj}-\phi_a^i,\\
\chi^i|_{\mathrm P}&=\tfrac i8\gamma^a\mathcal D_a\psi^i|_{\mathrm P}
+\tfrac g8\varphi^i,\\
\mathcal D_a\mathcal D_b\sigma|_{\mathrm P}
&=2f_{ab}-\tfrac i2\bar\psi_a\mathcal D_b\psi|_{\mathrm P}
-2\bar\psi_a\gamma_b\chi,\\
\Box^c\sigma|_{\mathrm P}
&=2f_a{}^a-\tfrac i2\bar\psi_a\mathcal D^a\psi|_{\mathrm P}
-2\bar\psi_a\gamma^a\chi,\\
D|_{\mathrm P}
&=\tfrac14\Box^c\sigma+\tfrac5{96}\widehat G_{ab}\widehat G^{ab}
-\tfrac1{288}\widehat G^{ab}\varepsilon_{abcde}\widehat H^{cde}
+\tfrac{13}{288}\widehat H_{abc}\widehat H^{abc}
+\tfrac g4N+\tfrac{g^2}{16}L^2 .
\end{aligned}\tag{A23}
```

To check the last line of A23 directly, use $`U_{ab}=\widehat H^{\mathrm{src}(2)}_{ab}`$ only within this check:

```math
\begin{aligned}
-\tfrac1{16}\widehat G^2-\tfrac{26}{3}
\frac{(\widehat G-2U)^2}{64}+\tfrac14\widehat G\!\cdot\!(\widehat G-2U)
&=(-\tfrac1{16}-\tfrac{13}{96}+\tfrac14)\widehat G^2
+(\tfrac{13}{24}-\tfrac12)\widehat G\!\cdot\!U-\tfrac{13}{24}U^2\\
&=\tfrac5{96}\widehat G^2-\tfrac1{288}\widehat G^{ab}\varepsilon_{abcde}\widehat H^{cde}
+\tfrac{13}{288}\widehat H_{abc}\widehat H^{abc}.
\end{aligned}\tag{A24}
```

The remaining gauging terms are $`Y^{ij}Y_{ij}/4=g^2L^2/16`$ and $`gN/4`$. A second derivative shows why gauge values must not be substituted before differentiating:

```math
\begin{aligned}
\left.\mathcal D_a\mathcal D_bY^{ij}\right|_{\mathrm P}
={}&-\tfrac g2\mathcal D_a\mathcal D_bL^{ij}
+\tfrac g2L^{ij}\mathcal D_a\mathcal D_b\sigma\\
&+\tfrac i4\left[
\overline{\mathcal D_b\psi^{(i}}\mathcal D_a\psi^{j)}
+\overline{\mathcal D_a\psi^{(i}}\mathcal D_b\psi^{j)}\right].
\end{aligned}\tag{A25}
```

This follows by applying Leibniz twice to $`Y^{ij}=i\sigma^{-1}\bar\psi^{(i}\psi^{j)}/4-g\sigma^{-1}L^{ij}/2`$, then imposing $`\psi=\mathcal D\sigma=0`$ without setting $`\mathcal D_a\mathcal D_b\sigma`$ or $`\mathcal D_a\psi`$ to zero. Higher ordered derivatives follow A18–A20 in the same order. The identity $`[\Box^c,\mathcal D_a]\Phi=\mathcal D^b[\mathcal D_b,\mathcal D_a]\Phi+[\mathcal D^b,\mathcal D_a]\mathcal D_b\Phi`$ forbids silently interchanging a box and a derivative.

## Two-derivative density and complete component map

The linear-to-vector map is reproduced below. Each slot is composed with A20 and evaluated as in A19. The displayed orders are two fermions for $`\rho_{\mathrm{linear}}`$ and $`Y_{\mathrm{linear}\,ij}`$ and one for $`\lambda_{\mathrm{linear}\,i}`$. A5 projects the implicit fermion content of the full derivatives.

```math
\boxed{
\rho_{\mathrm{linear}}
=2L^{-1}N
+iL^{-3}L_{ij}\bar\varphi^i\varphi^j.
}
\tag{A2-4.33}
```

```math
\boxed{
\begin{aligned}
\lambda_{\mathrm{linear}\,i}
={}&-2iL^{-1}\not{\mathcal D}\varphi_i
+L^{-1}\left(
16L_{ij}\chi^j
+4\gamma\!\cdot\!T\,\varphi_i
\right)\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}\left(
\not{\mathcal D}L_{ij}L^{jk}\varphi_k
-\not E\,L_{ij}\varphi^j
\right)\\
\end{aligned}
}\tag{A2-4.34}
```

```math
\boxed{
\begin{aligned}
Y_{\mathrm{linear}\,ij}
={}&L^{-1}\Box^cL_{ij}
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
\bar\varphi\gamma\!\cdot\!T\varphi\\
\end{aligned}
}\tag{A2-4.36}
```

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
\tag{A2-4.37}
```

The contractions are $`\not E=\gamma^aE_a`$, $`T^2=T_{ab}T^{ab}`$, and $`\widehat G^2=\widehat G_{ab}\widehat G^{ab}`$. The fields $`T,\chi,D`$ here are the A20 composites. The scalar-box definition is

```math
\begin{aligned}
L_{ij}\Box^cL^{ij}|_{\mathrm P}
={}&\tfrac L{\sqrt2}\delta_{ij}
(\partial^a+\omega_b{}^{ba})\mathcal D_aL^{ij}
+\sqrt2L\delta_{ij}V_a{}^i{}_k\mathcal D^aL^{jk}
+6L^2f_a{}^a\\
&-\tfrac{iL}{\sqrt2}\delta_{ij}\bar\psi^{ai}\mathcal D_a\varphi^j
-6L^2\bar\psi_a\gamma^a\chi
-\tfrac L{\sqrt2}\delta_{ij}\bar\varphi^i\gamma\!\cdot\!T\gamma^a\psi_a^j
+\tfrac L{\sqrt2}\delta_{ij}\bar\varphi^i\gamma^a\phi_a^j .
\end{aligned}\tag{A26}
```

The effective vector slots entering the density are

```math
\begin{aligned}
\rho_{\mathrm{eff}}&=\rho_{\mathrm{linear}}+2g,\qquad
\lambda_{\mathrm{eff}\,i}=\lambda_{\mathrm{linear}\,i},\\
Y_{\mathrm{eff}\,ij}&=Y_{\mathrm{linear}\,ij}-g^2L_{ij},\\
\widehat F_{\mathrm{eff}\,\mu\nu}
&=\widehat F_{\mathrm{linear}\,\mu\nu}+2g\widehat G_{\mu\nu},\\
F_{\mathrm{eff}\,\mu\nu}
&=\left[\widehat F_{\mathrm{eff}\,\mu\nu}
+\bar\psi_{[\mu}\gamma_{\nu]}\lambda_{\mathrm{eff}}
-\tfrac i2\rho_{\mathrm{eff}}\bar\psi_{[\mu}\psi_{\nu]}\right]_{\le2}\\
&=\left[\widehat F_{\mathrm{linear}\,\mu\nu}
+\bar\psi_{[\mu}\gamma_{\nu]}\lambda_{\mathrm{linear}}
-iL^{-1}N\bar\psi_{[\mu}\psi_{\nu]}+2gG_{\mu\nu}\right]_{\le2} .
\end{aligned}\tag{A27}
```

This uses $`2gY_{ij}=-g^2L_{ij}`$ and $`2g(i/2)\bar\psi_{[\mu}\psi_{\nu]}-(i/2)(2g)\bar\psi_{[\mu}\psi_{\nu]}=0`$. Ordinary $`F`$ and supercovariant $`\widehat F`$ have not been identified.

```math
\boxed{\begin{aligned}
\ell_{2\text{-der}}=-2\Big[&
L^{ij}Y_{\mathrm{eff}\,ij}
+i\bar\lambda_{\mathrm{eff}}{}^i\varphi_i
-\tfrac12\bar\psi_a^i\gamma^a\lambda_{\mathrm{eff}}{}^jL_{ij}
+\tfrac12F_{\mathrm{eff}\,\mu\nu}E^{\mu\nu}\\
&+\rho_{\mathrm{eff}}\left(
N+\tfrac12\bar\psi_a\gamma^a\varphi
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right)
\Big]_{\le2}\Big|_{\mathrm P}.
\end{aligned}}\tag{A28}
```

The barred spinor is $`\bar\lambda_{\mathrm{eff}}{}^i=\overline{\epsilon^{ir}\lambda_{\mathrm{eff}\,r}}`$, with the full scope of the bar fixed by A7. Substitution of A27 and A2-4.33–A2-4.37 into A28 reconstructs (5.1)/(5.10), preserving all internal coefficients.

Expanding the $`2gV_{\mathrm{defining}}`$ contribution separately checks the coefficients and form representative:

```math
\begin{aligned}
-4g\ell_{\mathrm{VL}}[V_{\mathrm{defining}};\mathbb L]_{F}
={}&-4g\left[-\tfrac g2L^2+\tfrac12G_{\mu\nu}E^{\mu\nu}
+N+\tfrac12\bar\psi_a\gamma^a\varphi
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right]\\
={}&2g^2L^2-2gG_{\mu\nu}E^{\mu\nu}-4gN
-2g\bar\psi_a\gamma^a\varphi
-ig\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}.
\end{aligned}\tag{A29}
```

In the potential representative the form term is $`-4gC_aP^a`$. The former source expression $`-4gC_aE^a`$ in (5.11) was not equivalent to (5.1)/(5.10) with fermions present. The source was corrected on 2026-09-27. The missing difference follows directly from A15:

```math
-4gC_a(P^a-E^a)
=-2igC_a\bar\psi_b\gamma^{ba}\varphi
-gC_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{A30}
```

A28 never uses that erroneous shorthand and retains the source (5.10) field-strength coefficients. Source equation (5.11a) displays A16 with $`A=C`$ and overall coefficient $`-4g`$, including the boundary term.

## LOG density and complete component register

The defining vector is $`(\rho,A_\mu,\lambda^i,Y^{ij})=(1,C_\mu,0,-gL^{ij}/2)`$. Substitution into the full vector–linear density gives

```math
\begin{aligned}
\ell_{\mathrm{VL}}[V;\mathbb L_{\log}]
={}&Y^{ij}L_{\log ij}+i\bar\lambda\varphi_{\log}
-\tfrac12\bar\psi_a^i\gamma^a\lambda^jL_{\log ij}+A_aP_{\log}^a\\
&+\rho\left(N_{\log}+\tfrac12\bar\psi_a\gamma^a\varphi_{\log}
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}\right),\\
P_{\log}^a={}&\left[E_{\log}^a+\tfrac i2\bar\psi_b\gamma^{ba}\varphi_{\log}
+\tfrac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2} .
\end{aligned}\tag{A31}
```

The fixed LOG density therefore has the SC7-52 coefficients:

```math
\boxed{\begin{aligned}
\ell_{\mathrm{Log}}=\Big[&N_{\log}
-\frac{gL}{2\sqrt2}\delta^{ij}L_{\log ij}+C_aE_{\log}^a
+\frac12\bar\psi_a\gamma^a\varphi_{\log}
+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}\\
&+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}
+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}
\Big]_{\le2} .
\end{aligned}}\tag{A32}
```

In the first three terms use degrees $`0+2`$ of the even slots; in the next two use degree one of the spinor; in the last two use degree zero of the triplet. A31's ordinary-current completions enter A32 exactly once. The source's Gold-to-component slot factors $`(-2,-2i,-1,+1)`$ were already applied and are not applied again.

All LOG slots in A32 follow. Labels $`[0],[1],[2]`$ denote explicit fermion degree; A5 still controls implicit degree:

```math
L_{\log}^{ij}=[L_{\log}^{ij}[0]+L_{\log}^{ij}[2]]_{\le2},\quad
\varphi_{\log}^i=[\varphi_{\log}^i[1]]_{1},\quad
N_{\log}=[N_{\log}[0]+N_{\log}[2]]_{\le2},\quad
E_{\log}^a=[E_{\log}^a[0]+E_{\log}^a[2]]_{\le2}.
\tag{A33}
```

Successive equalities under each component/degree heading continue the same sum. A gamma with multiple Lorentz indices is an antisymmetric blade, not a product of separate gammas. The indices $`r_k,s_k,t_k`$ are fresh tangent dummy indices introduced by A13. No two-index $`H`$ shorthand remains.

### Triplet: explicit degree zero

```math
\begin{aligned}
L_{\log}^{ij}[0]={}&-\frac{1}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat R(V){}_{a}{}_{b}{}^{i}{}^{j}\\
&-gL{}^{i}{}^{j}\big(\Box^c \sigma\big)\\
&-\frac{1}{2}gL{}^{i}{}^{j}\widehat G^2\\
&-g^{3}L{}^{i}{}^{j}L{}^{k}{}^{l}L{}_{k}{}_{l}\\
&+6g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)L{}^{i}{}^{j}\\
&-3Ng^{2}L{}^{i}{}^{j}\\
&-g\big(\Box^c L{}^{i}{}^{j}\big)
\end{aligned}
\tag{AL-LF0}
```

### Triplet: explicit degree two

```math
\begin{aligned}
L_{\log}^{ij}[2]={}&-\frac{5i}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{j}\big)\\
&+\frac{2i}{3}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&-\frac{11}{6}g\overline{\varphi{}^{j}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{11}{6}g\overline{\varphi{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{j}\big)\\
&+\frac{17i}{6}g^{2}\overline{\varphi{}^{i}}\varphi{}^{j}
\end{aligned}
\tag{AL-LF2}
```

### Spinor: explicit degree one

```math
\begin{aligned}
\varphi_{\log}^{i}[1]={}&\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}g\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\gamma{}_{a}{}_{b}\varphi{}_{j}\\
&+\frac{1}{144}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i}\\
&+\frac{1}{36}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat G{}_{c}{}_{d}\gamma{}_{a}{}_{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\\
&-\frac{7}{72}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\widehat G{}_{c}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\\
&-\frac{7}{18}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\gamma{}_{c}{}_{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\\
&-\frac{2i}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\widehat G{}_{a}{}_{b}\gamma{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{1}{4}g\widehat G^2\varphi{}^{i}\\
&-\frac{2}{3}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat G{}_{a}{}_{b}\varphi{}^{i}\\
&+\frac{5}{2}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\varphi{}^{i}\\
&-\frac{5i}{16}\widehat G{}_{b}{}_{c}\gamma{}_{a}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{5i}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\gamma{}_{c}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)\\
&+\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\widehat G{}_{b}{}_{c}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{1}{24}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\gamma{}^{c}{}^{d}\widehat R(Q){}^{a}{}^{b}{}^{i}\\
&-\frac{1}{12}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\widehat G{}_{c}{}_{d}\gamma{}_{b}{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&+\frac{1}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\gamma{}_{b}{}_{d}\widehat R(Q){}_{a}{}_{c}{}^{i}\\
&-\frac{3}{16}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{16}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{2}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}^{i}\big)\\
&-\frac{3i}{16}g\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\varphi{}^{i}\\
&+\frac{i}{2}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\varphi{}^{i}\\
&+\frac{i}{4}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\varphi{}^{i}\\
&-\frac{1}{32}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{8}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\big(\mathcal D^{c}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)\\
&-\frac{1}{8}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{32}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{8}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)\\
&-\frac{1}{16}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)\\
&-\frac{1}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}{}^{f}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)\\
&-\frac{i}{8}\widehat G{}_{b}{}_{c}\gamma{}^{c}\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)\\
&+\frac{i}{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\gamma{}_{b}\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{c}{}^{i}\big)\\
&+\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{2i}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)
\end{aligned}
\tag{AL-phiF1-1}
```

```math
\begin{aligned}
&-\frac{8i}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\gamma{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{2}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi{}^{i}\big)\\
&+\frac{1}{24}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}^{i}\big)\\
&+\frac{2i}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat G{}_{b}{}^{c}\gamma{}_{a}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{i}{6}gL{}^{i}{}^{j}\widehat G{}_{a}{}^{b}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{8i}{3}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)L{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{2i}{3}g\widehat G{}_{a}{}_{b}\gamma{}^{b}\big(\mathcal D^{a}\varphi{}^{i}\big)\\
&+\frac{4i}{3}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\gamma{}_{b}\big(\mathcal D_{a}\varphi{}^{i}\big)\\
&+\frac{5i}{6}\big(\Box^c \sigma\big)\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{5}{6}g\big(\Box^c \sigma\big)\varphi{}^{i}\\
&+\frac{11i}{24}g^{2}L{}^{j}{}^{k}L{}_{j}{}_{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{7}{24}g^{3}L{}^{j}{}^{k}L{}_{j}{}_{k}\varphi{}^{i}\\
&+\frac{11i}{6}Ng\gamma{}^{a}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{1}{6}Ng^{2}\varphi{}^{i}\\
&+\frac{13}{12}\big(\mathcal D^{c}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{5}{3}\big(\mathcal D_{a}\widehat G{}_{b}{}^{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{7i}{12}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\big)\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&-\frac{4}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\big)\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+\frac{i}{6}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}\big(\mathcal D^{e}\psi{}^{i}\big)\\
&-\frac{13}{24}g\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\varphi{}^{i}\\
&+\frac{7}{12}g\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{d}{}^{e}\varphi{}^{i}\\
&-\frac{1}{3}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{1}{6}\big(\mathcal D^{a}\widehat G{}_{a}{}^{b}\big)\big(\mathcal D_{b}\psi{}^{i}\big)\\
&-\frac{8}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big)\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&-\frac{5}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\big)\big(\mathcal D_{b}\psi{}^{i}\big)\\
&+\frac{5i}{6}g\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\gamma{}^{a}\varphi{}^{i}\\
&+\frac{11i}{3}g\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\big)\gamma{}_{b}\varphi{}^{i}\\
&-2gL{}^{i}{}^{j}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{j}\big)\\
&-gL{}^{i}{}^{j}\big(\Box^c \psi{}_{j}\big)\\
&-\frac{5i}{4}g^{2}L{}^{i}{}^{j}L{}_{j}{}^{k}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{k}\big)\\
&+2ig^{2}L{}^{i}{}^{j}\gamma{}_{a}\big(\mathcal D^{a}\varphi{}_{j}\big)\\
&+\frac{i}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}^{i}\\
&-\frac{i}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i}\\
&+\frac{i}{8}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}^{i}
\end{aligned}
\tag{AL-phiF1-2}
```

```math
\begin{aligned}
&-\frac{5i}{2}\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big)\\
&+\frac{1}{2}g\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-g\big(\Box^c \varphi{}^{i}\big)\\
&-\frac{i}{6}\widehat G{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}\big(\mathcal D^{d}\mathcal D^{e}\psi{}^{i}\big)\\
&+\frac{1}{3}\widehat G{}_{a}{}^{c}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}^{i}\big)\\
&-g\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+ig^{2}\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\gamma{}_{a}\varphi{}_{j}\\
&+\frac{i}{2}\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\gamma{}^{a}\big(\mathcal D_{c}\psi{}^{i}\big)\\
&+i\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat G{}_{a}{}_{c}\gamma{}^{c}\big(\mathcal D_{b}\psi{}^{i}\big)\\
&+\frac{23i}{576}gL{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{c}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{11i}{288}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&-\frac{1}{288}gL{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\widehat R(Q){}^{a}{}^{b}{}_{j}\\
&-\frac{59}{144}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)L{}^{i}{}^{j}\widehat R(Q){}_{a}{}_{b}{}_{j}\\
&+\frac{1}{2}\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\psi{}^{i}\big)\\
&+i\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}\big(\mathcal D^{b}\psi{}^{i}\big)\\
&+g\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\gamma{}^{a}{}^{b}\varphi{}^{i}\\
&+\frac{1}{12}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big)\\
&-\frac{1}{12}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}^{i}\big)\\
&+\frac{1}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat G{}_{c}{}^{e}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}^{i}\big)\\
&+\frac{1}{8}gL{}^{i}{}^{j}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{1}{4}g^{2}L{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\gamma{}^{a}{}^{b}\varphi{}_{j}\\
&-\frac{1}{6}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\gamma{}_{a}{}^{c}\big(\mathcal D^{f}\psi{}^{i}\big)
\end{aligned}
\tag{AL-phiF1-3}
```

### Scalar: explicit degree zero

```math
\begin{aligned}
N_{\log}[0]={}&\frac{1}{6}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j}\\
&+\frac{17}{144}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&+\frac{23}{72}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat C{}_{a}{}_{b}{}^{c}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{11}{18}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\widehat C{}_{a}{}_{b}{}_{c}{}_{d}\\
&+\frac{11}{72}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\\
&+\frac{17}{36}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\widehat C{}_{a}{}^{c}{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{5}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat C{}_{a}{}_{c}{}_{b}{}_{d}\\
&+\frac{1}{16}(\widehat G^2)^{2}\\
&-\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\widehat G{}_{a}{}_{b}\widehat G^2\\
&+\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\widehat G^2\\
&+\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&-2\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\left(-\frac1{12}\varepsilon{}_{c}{}_{d}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\\
&+\frac{1}{12}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{1}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\big)\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{863}{1152}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{1129}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{c}{}^{d}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\big(\mathcal D^{e}\left(-\frac1{12}\varepsilon{}_{e}{}^{f}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\widehat G{}_{a}{}_{b}\big(\Box^c \sigma\big)\\
&+\frac{1}{8}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\widehat G^2\\
&-\frac{1}{3}g^{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)L{}^{i}{}^{j}L{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&+2g^{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)L{}^{i}{}^{j}L{}_{i}{}_{j}\\
&+\frac{1}{2}Ng\widehat G^2\\
&-\frac{4}{3}Ng\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\widehat G{}_{a}{}_{b}\\
&+2Ng\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}_{b}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\\
&-\frac{3}{32}\big(\mathcal D^{a}\widehat C{}_{a}{}^{b}{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{3}{8}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\big(\mathcal D^{c}\widehat C{}_{c}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\big(\mathcal D^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{16}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\big(\mathcal D_{a}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{4}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{2}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{28}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{35}}{}_{s_{35}}{}_{t_{35}}\widehat H^{r_{35}s_{35}t_{35}}\right)\widehat G{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&+\frac{28}{9}\big(\mathcal D^{a}\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{36}}{}_{s_{36}}{}_{t_{36}}\widehat H^{r_{36}s_{36}t_{36}}\right)\big)\widehat G{}_{a}{}_{c}\\
&+\frac{28}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{37}}{}_{s_{37}}{}_{t_{37}}\widehat H^{r_{37}s_{37}t_{37}}\right)\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)
\end{aligned}
\tag{AL-NF0-1}
```

```math
\begin{aligned}
&+\frac{8}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{32}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\big(\mathcal D_{a}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\big)\\
&+\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \widehat G{}_{a}{}_{b}\big)\\
&+\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\big(\Box^c \widehat G{}_{a}{}_{b}\big)\\
&+\frac{1}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{9}\big(\mathcal D^{a}\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{a}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\big)\widehat G{}_{b}{}_{c}\\
&+\frac{4}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{9}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\big(\mathcal D^{c}\mathcal D_{a}\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\big)\\
&+\frac{5}{6}\big(\Box^c \sigma\big)\big(\Box^c \sigma\big)\\
&+\frac{5}{3}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\big(\Box^c \sigma\big)\\
&+\frac{8}{3}Ng\big(\Box^c \sigma\big)\\
&-\frac{17}{48}g^{4}L{}^{i}{}^{j}L{}_{i}{}_{j}L{}^{k}{}^{l}L{}_{k}{}_{l}\\
&-\frac{5}{6}Ng^{3}L{}^{i}{}^{j}L{}_{i}{}_{j}\\
&-\frac{1}{6}NNg^{2}\\
&+\frac{5}{6}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&-\frac{7}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&+\frac{4}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\big)\big(\mathcal D_{b}\left(-\frac1{12}\varepsilon{}_{a}{}_{c}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big)\\
&-\frac{1}{3}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{11}{6}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{2}{3}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\big)\big(\mathcal D_{a}\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\big)\\
&-2\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\big)\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&+4\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}_{a}{}^{b}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\big)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\big)\\
&-\frac{1}{2}gL{}^{i}{}^{j}\widehat R(V){}^{a}{}^{b}{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&-\frac{1163}{1152}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{563}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\big)\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{269}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\widehat G{}_{a}{}^{c}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{139}{288}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\big)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{16}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{19}{24}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\big)\widehat G{}_{d}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{353}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{89}{288}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{a}{}^{d}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{64}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{32}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\big(\mathcal D_{a}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-g^{2}L{}^{i}{}^{j}\big(\Box^c L{}_{i}{}_{j}\big)\\
&-\frac{3}{4}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}
\end{aligned}
\tag{AL-NF0-2}
```

```math
\begin{aligned}
&+\frac{3}{2}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{3}{2}\big(\mathcal D^{a}\mathcal D^{b}\sigma\big)\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\\
&-\frac{3}{4}g^{2}\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\big(\mathcal D_{a}L{}_{i}{}_{j}\big)\\
&-g\big(\Box^c N\big)\\
&-\frac{3}{8}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+2\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-4\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\left(-\frac1{12}\varepsilon{}_{a}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+\frac{1}{8}g^{4}L{}^{i}{}^{j}L{}_{i}{}^{k}L{}_{j}{}^{l}L{}_{k}{}_{l}
\end{aligned}
\tag{AL-NF0-3}
```

### Scalar: explicit degree two

```math
\begin{aligned}
N_{\log}[2]={}&\frac{685i}{6144}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{2125i}{18432}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{379i}{3072}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{1211i}{9216}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{2651}{18432}g\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi{}_{i}\\
&-\frac{541}{9216}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\varphi{}_{i}\\
&-\frac{607i}{18432}\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{289}{576}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{65i}{9216}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{11}{144}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{859i}{9216}g\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\varphi{}_{i}\\
&+\frac{6173i}{4608}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\varphi{}_{i}\\
&-\frac{209}{9216}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{8167}{4608}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{i}{4}\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}\widehat G{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{3i}{2}\widehat G{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{1}{12}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{i}{6}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{5i}{6}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2i}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{4}g\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{2}g\widehat G{}_{a}{}^{b}\overline{\varphi{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{19i}{24}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{1}{6}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\overline{\varphi{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{3i}{8}g^{2}\widehat G{}_{a}{}_{b}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\varphi{}_{i}\\
&+\frac{3i}{4}g^{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\overline{\varphi{}^{i}}\gamma{}_{a}{}_{b}\varphi{}_{i}\\
&-\frac{81i}{256}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{111}{512}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{153i}{1024}g\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&-\frac{i}{12}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{5}{6}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{1}{6}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{4}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{i}{3}gL{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\psi{}_{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)
\end{aligned}
\tag{AL-NF2-1}
```

```math
\begin{aligned}
&+\frac{10i}{3}gL{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&+\frac{5i}{6}g\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{13i}{6}g\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{5i}{6}g\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\overline{\varphi{}^{i}}\big(\Box^c \psi{}_{i}\big)\\
&+\frac{13}{12}g^{2}L{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&+\frac{1}{6}g^{2}\overline{\varphi{}^{i}}\gamma{}_{a}\big(\mathcal D^{a}\varphi{}_{i}\big)\\
&-\frac{19i}{64}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}_{a}{}^{c}{}_{i}\\
&-\frac{19i}{16}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&+\frac{15}{512}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{15}{128}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{3}{256}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}_{i}\\
&+\frac{3}{64}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{f}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&-\frac{9i}{1024}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}_{i}\\
&-\frac{9i}{256}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&+\frac{355i}{2304}gL{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{131i}{1152}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{95i}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{4999i}{36864}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{3271i}{18432}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{117i}{2048}\widehat G{}_{c}{}^{e}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{69i}{1024}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{64}g\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi{}_{i}\big)\\
&-\frac{i}{1024}gL{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\widehat R(Q){}_{a}{}_{b}{}_{j}\\
&+\frac{1}{2048}gL{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}
\end{aligned}
\tag{AL-NF2-2}
```

### Vector: explicit degree zero

```math
\begin{aligned}
E_{\log}^{a}[0]={}&-\frac{1}{12}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat R(V){}^{d}{}^{e}{}_{i}{}_{j}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{1}{128}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{3}{8}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}^{a}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{21}{64}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{16}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{25}{768}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}_{b}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{11}{96}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{d}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{31}{384}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat C{}_{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{96}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\widehat C{}_{b}{}^{e}{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{192}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{5}{192}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}^{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{7}{192}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{24}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{41}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{29}{288}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}^{a}{}_{c}{}_{d}{}_{f}{}_{g}\\
&+\frac{53}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\widehat C{}_{b}{}^{f}{}_{d}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{31}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{59}{288}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{f}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{g}\\
&-\frac{161}{576}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\widehat C{}_{b}{}^{d}{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{19}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\widehat C{}_{b}{}^{f}{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{1152}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{23}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{23}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\widehat C{}_{b}{}_{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{25}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\widehat C{}_{b}{}_{c}{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{43}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{29}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{149}{288}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{5}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{35}{2304}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&+\frac{59}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{288}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{576}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{29}{288}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{19}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\widehat C{}_{b}{}_{d}{}^{f}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{86015}{82944}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{98689}{41472}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\widehat G{}^{a}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}
\end{aligned}
\tag{AL-EF0-1}
```

```math
\begin{aligned}
&-\frac{23027}{20736}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\widehat G{}^{a}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&+\frac{2243}{41472}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\widehat G{}^{a}{}_{b}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{6947}{5184}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\widehat G{}^{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{34427}{41472}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{20736}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1801}{5184}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{44159}{10368}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{13625}{2592}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{551}{10368}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{889}{2592}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\widehat G{}^{d}{}^{e}\widehat G{}_{d}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\\
&+\frac{26779}{20736}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\widehat G{}_{b}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{23027}{41472}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{19823}{10368}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{21275}{5184}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\widehat G{}_{b}{}_{d}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{125}{20736}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1181}{10368}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{4385}{41472}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{12205}{5184}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{35}}{}_{s_{35}}{}_{t_{35}}\widehat H^{r_{35}s_{35}t_{35}}\right)\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{36}}{}_{s_{36}}{}_{t_{36}}\widehat H^{r_{36}s_{36}t_{36}}\right)\widehat G{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{122}{81}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{37}}{}_{s_{37}}{}_{t_{37}}\widehat H^{r_{37}s_{37}t_{37}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{38}}{}_{s_{38}}{}_{t_{38}}\widehat H^{r_{38}s_{38}t_{38}}\right)\left(-\frac1{12}\varepsilon{}_{c}{}^{e}{}_{r_{39}}{}_{s_{39}}{}_{t_{39}}\widehat H^{r_{39}s_{39}t_{39}}\right)\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{635}{162}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{40}}{}_{s_{40}}{}_{t_{40}}\widehat H^{r_{40}s_{40}t_{40}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{41}}{}_{s_{41}}{}_{t_{41}}\widehat H^{r_{41}s_{41}t_{41}}\right)\left(-\frac1{12}\varepsilon{}_{c}{}^{e}{}_{r_{42}}{}_{s_{42}}{}_{t_{42}}\widehat H^{r_{42}s_{42}t_{42}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{43}}{}_{s_{43}}{}_{t_{43}}\widehat H^{r_{43}s_{43}t_{43}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{551}{41472}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{889}{5184}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{44}}{}_{s_{44}}{}_{t_{44}}\widehat H^{r_{44}s_{44}t_{44}}\right)\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{1237}{5184}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{45}}{}_{s_{45}}{}_{t_{45}}\widehat H^{r_{45}s_{45}t_{45}}\right)\widehat G{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1513}{1296}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{46}}{}_{s_{46}}{}_{t_{46}}\widehat H^{r_{46}s_{46}t_{46}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{47}}{}_{s_{47}}{}_{t_{47}}\widehat H^{r_{47}s_{47}t_{47}}\right)\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{3209}{2592}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{48}}{}_{s_{48}}{}_{t_{48}}\widehat H^{r_{48}s_{48}t_{48}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{49}}{}_{s_{49}}{}_{t_{49}}\widehat H^{r_{49}s_{49}t_{49}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{50}}{}_{s_{50}}{}_{t_{50}}\widehat H^{r_{50}s_{50}t_{50}}\right)\widehat G{}_{b}{}_{c}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{61}{81}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{51}}{}_{s_{51}}{}_{t_{51}}\widehat H^{r_{51}s_{51}t_{51}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{52}}{}_{s_{52}}{}_{t_{52}}\widehat H^{r_{52}s_{52}t_{52}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{53}}{}_{s_{53}}{}_{t_{53}}\widehat H^{r_{53}s_{53}t_{53}}\right)\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{635}{648}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{54}}{}_{s_{54}}{}_{t_{54}}\widehat H^{r_{54}s_{54}t_{54}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{55}}{}_{s_{55}}{}_{t_{55}}\widehat H^{r_{55}s_{55}t_{55}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{56}}{}_{s_{56}}{}_{t_{56}}\widehat H^{r_{56}s_{56}t_{56}}\right)\left(-\frac1{12}\varepsilon{}^{f}{}^{g}{}_{r_{57}}{}_{s_{57}}{}_{t_{57}}\widehat H^{r_{57}s_{57}t_{57}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{6}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\widehat G^2\\
&-\frac{2}{3}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}_{b}{}_{r_{58}}{}_{s_{58}}{}_{t_{58}}\widehat H^{r_{58}s_{58}t_{58}}\right)\big)\widehat G^2\\
&+2\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{59}}{}_{s_{59}}{}_{t_{59}}\widehat H^{r_{59}s_{59}t_{59}}\right)\widehat G{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big)\\
&-\frac{2}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{60}}{}_{s_{60}}{}_{t_{60}}\widehat H^{r_{60}s_{60}t_{60}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{61}}{}_{s_{61}}{}_{t_{61}}\widehat H^{r_{61}s_{61}t_{61}}\right)\big(\mathcal D^{d}\widehat G{}^{a}{}_{d}\big)\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{62}}{}_{s_{62}}{}_{t_{62}}\widehat H^{r_{62}s_{62}t_{62}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{63}}{}_{s_{63}}{}_{t_{63}}\widehat H^{r_{63}s_{63}t_{63}}\right)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{a}{}_{d}{}_{r_{64}}{}_{s_{64}}{}_{t_{64}}\widehat H^{r_{64}s_{64}t_{64}}\right)\big)\\
&+\frac{2}{3}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big)\\
&+\frac{2}{3}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{c}{}_{r_{65}}{}_{s_{65}}{}_{t_{65}}\widehat H^{r_{65}s_{65}t_{65}}\right)\big)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{66}}{}_{s_{66}}{}_{t_{66}}\widehat H^{r_{66}s_{66}t_{66}}\right)\widehat G{}_{b}{}^{d}\big(\mathcal D_{d}\widehat G{}^{a}{}_{c}\big)\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{67}}{}_{s_{67}}{}_{t_{67}}\widehat H^{r_{67}s_{67}t_{67}}\right)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{a}{}_{b}{}_{r_{68}}{}_{s_{68}}{}_{t_{68}}\widehat H^{r_{68}s_{68}t_{68}}\right)\big)\widehat G{}_{c}{}_{d}
\end{aligned}
\tag{AL-EF0-2}
```

```math
\begin{aligned}
&+\frac{16}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\big(\mathcal D_{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{d}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\big)\widehat G{}_{c}{}_{d}\\
&+\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\big(\mathcal D_{c}\widehat G{}^{a}{}_{d}\big)\\
&+\frac{32}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\big(\mathcal D_{c}\left(-\frac1{12}\varepsilon{}^{a}{}_{d}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\big)\\
&-\frac{2}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\big)\widehat G{}^{a}{}^{d}\widehat G{}_{c}{}_{d}\\
&+\frac{10}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\widehat G{}^{a}{}_{b}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}_{b}{}_{d}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big)\widehat G{}^{a}{}_{c}\\
&-\frac{2}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{16}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{c}{}^{d}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\big)\widehat G{}_{b}{}_{d}\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{32}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}_{c}{}_{d}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\big)\\
&+\frac{7}{3}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&-\frac{10}{3}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\big)\widehat G{}^{a}{}_{c}\widehat G{}_{b}{}_{d}\\
&+2\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\widehat G{}^{a}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\big(\mathcal D_{b}\left(-\frac1{12}\varepsilon{}_{c}{}^{d}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\big)\widehat G{}^{a}{}_{d}\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\big(\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\big)\widehat G{}_{c}{}_{d}\\
&-\frac{20}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big)\\
&+\frac{32}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\big(\mathcal D_{c}\left(-\frac1{12}\varepsilon{}_{b}{}_{d}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\big)\\
&-\frac{7}{6}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+2\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\big)\widehat G{}^{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&+\frac{10}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\widehat G{}^{a}{}^{d}\big(\mathcal D_{d}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}_{b}{}_{c}{}_{r_{35}}{}_{s_{35}}{}_{t_{35}}\widehat H^{r_{35}s_{35}t_{35}}\right)\big)\widehat G{}^{a}{}_{d}\\
&-\frac{1}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{36}}{}_{s_{36}}{}_{t_{36}}\widehat H^{r_{36}s_{36}t_{36}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{2}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{37}}{}_{s_{37}}{}_{t_{37}}\widehat H^{r_{37}s_{37}t_{37}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{38}}{}_{s_{38}}{}_{t_{38}}\widehat H^{r_{38}s_{38}t_{38}}\right)\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&-\frac{16}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{39}}{}_{s_{39}}{}_{t_{39}}\widehat H^{r_{39}s_{39}t_{39}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{40}}{}_{s_{40}}{}_{t_{40}}\widehat H^{r_{40}s_{40}t_{40}}\right)\big(\mathcal D_{b}\left(-\frac1{12}\varepsilon{}_{c}{}_{d}{}_{r_{41}}{}_{s_{41}}{}_{t_{41}}\widehat H^{r_{41}s_{41}t_{41}}\right)\big)\\
&-\frac{1}{4}\big(\mathcal D^{b}\widehat C{}^{a}{}^{c}{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&+\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{42}}{}_{s_{42}}{}_{t_{42}}\widehat H^{r_{42}s_{42}t_{42}}\right)\big(\mathcal D^{d}\widehat C{}^{a}{}_{b}{}_{c}{}_{d}\big)\\
&-\frac{1}{8}\big(\mathcal D^{b}\widehat C{}^{a}{}_{b}{}^{c}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&-\frac{1}{2}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{43}}{}_{s_{43}}{}_{t_{43}}\widehat H^{r_{43}s_{43}t_{43}}\right)\big(\mathcal D^{d}\widehat C{}^{a}{}_{d}{}_{b}{}_{c}\big)\\
&-\frac{7}{18}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{72}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{144}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{9}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{44}}{}_{s_{44}}{}_{t_{44}}\widehat H^{r_{44}s_{44}t_{44}}\right)\widehat G{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{45}}{}_{s_{45}}{}_{t_{45}}\widehat H^{r_{45}s_{45}t_{45}}\right)\big)\widehat G{}^{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{257}{144}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{46}}{}_{s_{46}}{}_{t_{46}}\widehat H^{r_{46}s_{46}t_{46}}\right)\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{AL-EF0-3}
```

```math
\begin{aligned}
&+\frac{91}{144}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{37}{18}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{18}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\big(\mathcal D^{c}\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{24}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{1}{36}\widehat G{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{36}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D_{d}\mathcal D^{f}\sigma\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{36}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\big)\widehat G{}_{b}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{149}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D_{b}\mathcal D^{f}\sigma\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{37}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big(\Box^c \sigma\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{25}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\big(\mathcal D_{b}\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{24}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\widehat G{}_{b}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{12}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\big)\widehat G{}_{d}{}^{f}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{8}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{11}{12}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\big(\mathcal D^{d}\mathcal D^{e}\left(-\frac1{12}\varepsilon{}_{b}{}^{f}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{12}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{2}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{a}{}^{d}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{6}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\big(\mathcal D^{d}\mathcal D^{e}\left(-\frac1{12}\varepsilon{}^{a}{}^{f}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{25}{72}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{b}{}^{d}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{18}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{11}{9}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\big(\mathcal D^{d}\mathcal D^{e}\left(-\frac1{12}\varepsilon{}_{d}{}^{f}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{5}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{24}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{19}{144}\big(\mathcal D^{a}\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{2}{9}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\big(\mathcal D^{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{9}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\big(\mathcal D^{a}\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{33}}{}_{s_{33}}{}_{t_{33}}\widehat H^{r_{33}s_{33}t_{33}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{144}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{371}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{34}}{}_{s_{34}}{}_{t_{34}}\widehat H^{r_{34}s_{34}t_{34}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\sigma\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}_{c}{}^{d}{}_{r_{35}}{}_{s_{35}}{}_{t_{35}}\widehat H^{r_{35}s_{35}t_{35}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{65}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{36}}{}_{s_{36}}{}_{t_{36}}\widehat H^{r_{36}s_{36}t_{36}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\sigma\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{7}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{37}}{}_{s_{37}}{}_{t_{37}}\widehat H^{r_{37}s_{37}t_{37}}\right)\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{67}{36}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{38}}{}_{s_{38}}{}_{t_{38}}\widehat H^{r_{38}s_{38}t_{38}}\right)\big(\mathcal D^{d}\mathcal D^{e}\left(-\frac1{12}\varepsilon{}_{e}{}^{f}{}_{r_{39}}{}_{s_{39}}{}_{t_{39}}\widehat H^{r_{39}s_{39}t_{39}}\right)\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}
\end{aligned}
\tag{AL-EF0-4}
```

```math
\begin{aligned}
&+\frac{23}{288}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{48}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{11}{144}\big(\mathcal D^{b}\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{13}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\big(\mathcal D^{d}\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{25}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\big(\mathcal D^{d}\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{5}{72}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1}{18}\big(\mathcal D^{b}\mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\big)\widehat G{}_{c}{}^{f}\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{43}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{55}{72}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\big(\mathcal D^{d}\mathcal D_{b}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{48}\widehat G{}^{b}{}^{c}\big(\Box^c \widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{23}{16}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\widehat G{}^{d}{}^{e}\big(\Box^c \sigma\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{5}{24}\big(\Box^c \left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big)\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{17}{48}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\big(\Box^c \widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{11}{24}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big(\Box^c \left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{1}{3}\widehat G{}^{a}{}^{b}\big(\mathcal D_{b}\Box^c \sigma\big)\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\big(\mathcal D_{b}\Box^c \sigma\big)\\
&-\frac{4}{3}g^{2}L{}^{i}{}^{j}\big(\mathcal D^{b}L{}_{i}{}_{j}\big)\widehat G{}^{a}{}_{b}\\
&+\frac{2}{3}g^{2}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)L{}^{i}{}^{j}\big(\mathcal D_{b}L{}_{i}{}_{j}\big)\\
&-\frac{5}{3}g\big(\mathcal D^{b}N\big)\widehat G{}^{a}{}_{b}\\
&+\frac{4}{3}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\big(\mathcal D_{b}N\big)\\
&-\frac{2}{3}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\big(\Box^c \sigma\big)\\
&+\frac{10}{3}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}_{b}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\big)\big(\Box^c \sigma\big)\\
&-\frac{2}{3}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\\
&+\frac{1}{3}g^{2}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}_{b}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\big)L{}^{i}{}^{j}L{}_{i}{}_{j}\\
&-\frac{5}{3}Ng\big(\mathcal D^{b}\widehat G{}^{a}{}_{b}\big)\\
&+\frac{4}{3}Ng\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}_{b}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\big)\\
&+\frac{113}{1536}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{881}{768}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\big)\big(\mathcal D^{e}\widehat G{}^{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1199}{768}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{c}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{431}{384}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{c}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\big)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{1105}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{401}{768}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\big)\big(\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1265}{768}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{187}{128}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\big)\big(\mathcal D_{c}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{1039}{768}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{245}{64}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}
\end{aligned}
\tag{AL-EF0-5}
```

```math
\begin{aligned}
&-\frac{431}{192}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\big)\big(\mathcal D^{e}\left(-\frac1{12}\varepsilon{}_{c}{}^{f}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\big)\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{175}{512}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{17}{256}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\big)\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{49}{256}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{241}{128}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\big)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{415}{1536}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{415}{768}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\big)\big(\mathcal D^{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{191}{768}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{191}{384}\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\big)\big(\mathcal D^{d}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{353}{1536}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{59}{128}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{191}{384}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\big)\big(\mathcal D_{b}\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\big)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+gL{}^{i}{}^{j}\big(\mathcal D^{b}\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\big)\\
&+g\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\widehat R(V){}^{a}{}_{b}{}_{i}{}_{j}\\
&-\frac{31}{192}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\\
&-\frac{1}{8}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{11}{24}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\widehat C{}^{a}{}^{d}{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{25}{64}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\widehat C{}^{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{1}{64}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{18}}{}_{s_{18}}{}_{t_{18}}\widehat H^{r_{18}s_{18}t_{18}}\right)\widehat C{}^{a}{}_{b}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{63}{16}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{19}}{}_{s_{19}}{}_{t_{19}}\widehat H^{r_{19}s_{19}t_{19}}\right)\widehat G{}^{a}{}^{d}\widehat G{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{37}{4}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{20}}{}_{s_{20}}{}_{t_{20}}\widehat H^{r_{20}s_{20}t_{20}}\right)\left(-\frac1{12}\varepsilon{}^{c}{}^{d}{}_{r_{21}}{}_{s_{21}}{}_{t_{21}}\widehat H^{r_{21}s_{21}t_{21}}\right)\left(-\frac1{12}\varepsilon{}^{e}{}^{f}{}_{r_{22}}{}_{s_{22}}{}_{t_{22}}\widehat H^{r_{22}s_{22}t_{22}}\right)\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{2}{3}\widehat G{}^{a}{}^{b}\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+\frac{8}{3}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{23}}{}_{s_{23}}{}_{t_{23}}\widehat H^{r_{23}s_{23}t_{23}}\right)\big(\Box^c \mathcal D_{b}\sigma\big)\\
&+5\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{c}{}_{r_{24}}{}_{s_{24}}{}_{t_{24}}\widehat H^{r_{24}s_{24}t_{24}}\right)\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-2\big(\Box^c \mathcal D^{c}\left(-\frac1{12}\varepsilon{}^{a}{}_{c}{}_{r_{25}}{}_{s_{25}}{}_{t_{25}}\widehat H^{r_{25}s_{25}t_{25}}\right)\big)\\
&+\frac{1}{2}\big(\mathcal D^{b}\widehat G{}^{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}^{a}{}^{c}{}_{r_{26}}{}_{s_{26}}{}_{t_{26}}\widehat H^{r_{26}s_{26}t_{26}}\right)\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\frac{5}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big)\\
&+\frac{5}{2}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{27}}{}_{s_{27}}{}_{t_{27}}\widehat H^{r_{27}s_{27}t_{27}}\right)\big)\big(\mathcal D_{c}\mathcal D^{a}\sigma\big)\\
&+\frac{1}{4}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big)\\
&-\frac{1}{2}\big(\mathcal D^{b}\left(-\frac1{12}\varepsilon{}_{b}{}^{c}{}_{r_{28}}{}_{s_{28}}{}_{t_{28}}\widehat H^{r_{28}s_{28}t_{28}}\right)\big)\big(\mathcal D^{a}\mathcal D_{c}\sigma\big)\\
&+\frac{1}{2}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\big(\mathcal D^{a}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{29}}{}_{s_{29}}{}_{t_{29}}\widehat H^{r_{29}s_{29}t_{29}}\right)\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{89}{144}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{30}}{}_{s_{30}}{}_{t_{30}}\widehat H^{r_{30}s_{30}t_{30}}\right)\left(-\frac1{12}\varepsilon{}^{d}{}^{e}{}_{r_{31}}{}_{s_{31}}{}_{t_{31}}\widehat H^{r_{31}s_{31}t_{31}}\right)\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{2}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{32}}{}_{s_{32}}{}_{t_{32}}\widehat H^{r_{32}s_{32}t_{32}}\right)\widehat G{}_{b}{}^{d}\big(\mathcal D^{a}\widehat G{}_{c}{}_{d}\big)
\end{aligned}
\tag{AL-EF0-6}
```

### Vector: explicit degree two

```math
\begin{aligned}
E_{\log}^{a}[2]={}&-\frac{803}{18432}\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{539}{9216}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{919i}{18432}g\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\varphi{}_{i}\\
&-\frac{655i}{9216}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\varphi{}_{i}\\
&-\frac{2269i}{9216}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{2047i}{1536}\widehat G{}_{b}{}^{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{181}{3072}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{473i}{768}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{3731i}{4608}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{115}{1536}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{719i}{18432}g\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\varphi{}_{i}\\
&+\frac{889i}{9216}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i}\\
&+\frac{4685i}{9216}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{425i}{2304}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{401}{2304}\widehat G{}_{b}{}^{e}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{3691i}{4608}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&-\frac{305i}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{1469}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2071i}{18432}g\widehat G{}_{b}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&+\frac{5191i}{9216}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i}\\
&+\frac{2129i}{2304}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{151i}{1152}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{2341}{2304}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi{}_{i}\\
&-\frac{241}{1152}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}_{c}\varphi{}_{i}\\
&+\frac{719i}{3072}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{929i}{1536}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{1099}{9216}g\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\varphi{}_{i}\\
&+\frac{6509}{4608}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{a}\varphi{}_{i}\\
&-\frac{505i}{1152}\widehat G{}^{a}{}_{b}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{313}{1536}\widehat G{}^{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{839i}{576}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{319}{768}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{2645i}{36864}g\widehat G{}^{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&+\frac{5083i}{18432}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{17}}{}_{s_{17}}{}_{t_{17}}\widehat H^{r_{17}s_{17}t_{17}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i}\\
&-\frac{197i}{768}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{49i}{192}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)
\end{aligned}
\tag{AL-EF2-1}
```

```math
\begin{aligned}
&+\frac{67}{256}g\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\varphi{}_{i}\\
&+\frac{209i}{768}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{167}{384}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{221i}{128}g\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\varphi{}_{i}\\
&-\frac{217i}{768}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{283}{768}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{173}{256}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{257i}{1536}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{2}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{3i}{2}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{6}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{5i}{2}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{i}{2}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{7i}{6}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{7i}{6}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{25i}{48}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{11}{6}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{1}{6}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{23i}{32}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{23i}{32}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{4}{3}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{12}gL{}^{i}{}^{j}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}_{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{1}{3}gL{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\psi{}_{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{1}{3}gL{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{i}{12}g\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{6}g\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{7}{6}g\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{4}g\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{1}{2}g\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{1}{6}g\overline{\varphi{}^{i}}\gamma{}^{a}\big(\Box^c \psi{}_{i}\big)\\
&-\frac{23}{12}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{5i}{6}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\overline{\varphi{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{5i}{6}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\overline{\varphi{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{i}{2}g\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\overline{\varphi{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{11i}{12}g^{2}L{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)
\end{aligned}
\tag{AL-EF2-2}
```

```math
\begin{aligned}
&+\frac{5i}{6}g^{2}\overline{\varphi{}^{i}}\gamma{}^{a}{}_{b}\big(\mathcal D^{b}\varphi{}_{i}\big)\\
&+\frac{5i}{48}\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{7i}{48}\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{29i}{48}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{96}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{65}{256}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{65}{64}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&-\frac{11i}{512}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{11i}{128}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{a}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{13i}{256}\widehat G{}_{b}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{13i}{64}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{35i}{2048}\widehat G{}_{b}{}_{c}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{35i}{512}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{7i}{512}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{7i}{128}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&-\frac{23i}{512}\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{23i}{128}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\widehat R(Q){}_{d}{}^{f}{}_{i}\\
&-\frac{5i}{96}\widehat G{}^{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{19i}{1024}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{19i}{256}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}_{b}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{3i}{128}\widehat G{}_{c}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&-\frac{3i}{32}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{7i}{1024}\widehat G{}^{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{7i}{256}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{256}\widehat G{}_{b}{}_{d}\varepsilon{}^{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{64}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{11}}{}_{s_{11}}{}_{t_{11}}\widehat H^{r_{11}s_{11}t_{11}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&+\frac{i}{128}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&+\frac{i}{32}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{12}}{}_{s_{12}}{}_{t_{12}}\widehat H^{r_{12}s_{12}t_{12}}\right)\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i}\\
&-\frac{3}{32}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&+\frac{3}{8}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{13}}{}_{s_{13}}{}_{t_{13}}\widehat H^{r_{13}s_{13}t_{13}}\right)\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{c}\widehat R(Q){}_{b}{}_{d}{}_{i}\\
&+\frac{5i}{1024}\widehat G{}^{f}{}^{g}\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&+\frac{5i}{256}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{14}}{}_{s_{14}}{}_{t_{14}}\widehat H^{r_{14}s_{14}t_{14}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}_{e}{}_{i}\\
&-\frac{i}{512}\widehat G{}_{b}{}_{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{128}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{15}}{}_{s_{15}}{}_{t_{15}}\widehat H^{r_{15}s_{15}t_{15}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{i}{1024}\widehat G{}^{a}{}_{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{256}\left(-\frac1{12}\varepsilon{}^{a}{}^{b}{}_{r_{16}}{}_{s_{16}}{}_{t_{16}}\widehat H^{r_{16}s_{16}t_{16}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}
\end{aligned}
\tag{AL-EF2-3}
```

```math
\begin{aligned}
&-\frac{7i}{1024}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{7i}{256}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{1}}{}_{s_{1}}{}_{t_{1}}\widehat H^{r_{1}s_{1}t_{1}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}_{b}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&+\frac{i}{2048}\widehat G{}_{f}{}_{g}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{512}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{2}}{}_{s_{2}}{}_{t_{2}}\widehat H^{r_{2}s_{2}t_{2}}\right)\varepsilon{}^{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}_{c}\widehat R(Q){}^{f}{}^{g}{}_{i}\\
&-\frac{3i}{512}\widehat G{}_{e}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{3i}{128}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{3}}{}_{s_{3}}{}_{t_{3}}\widehat H^{r_{3}s_{3}t_{3}}\right)\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{3}{4}\widehat G{}^{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{11i}{6}g\widehat G{}^{a}{}^{b}\overline{\varphi{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{433}{4608}\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{83}{384}\widehat G{}_{d}{}^{e}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{503}{2304}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{4}}{}_{s_{4}}{}_{t_{4}}\widehat H^{r_{4}s_{4}t_{4}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{5}{192}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{5}}{}_{s_{5}}{}_{t_{5}}\widehat H^{r_{5}s_{5}t_{5}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{461i}{2048}g\widehat G{}_{d}{}^{f}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&-\frac{77i}{1024}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{6}}{}_{s_{6}}{}_{t_{6}}\widehat H^{r_{6}s_{6}t_{6}}\right)\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}^{f}\varphi{}_{i}\\
&+\frac{1}{24}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{107}{9216}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{49}{192}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{7}}{}_{s_{7}}{}_{t_{7}}\widehat H^{r_{7}s_{7}t_{7}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{469}{4608}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{8}}{}_{s_{8}}{}_{t_{8}}\widehat H^{r_{8}s_{8}t_{8}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{5i}{256}g\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\varphi{}_{i}\\
&-\frac{27i}{128}g\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{9}}{}_{s_{9}}{}_{t_{9}}\widehat H^{r_{9}s_{9}t_{9}}\right)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{a}{}^{f}\varphi{}_{i}\\
&+\frac{4i}{3}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{a}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{4i}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-g\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{4}\widehat G{}^{b}{}^{c}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{1}{4}g\widehat G{}^{c}{}^{d}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{211i}{144}gL{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{103}{288}gL{}^{i}{}^{j}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{499i}{2304}g^{2}L{}^{i}{}^{j}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}{}^{e}\varphi{}_{j}\\
&+\frac{259}{4608}\widehat G{}^{e}{}^{f}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{533}{2304}\left(-\frac1{12}\varepsilon{}^{b}{}^{c}{}_{r_{10}}{}_{s_{10}}{}_{t_{10}}\widehat H^{r_{10}s_{10}t_{10}}\right)\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{437i}{1536}\varepsilon{}^{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{39i}{1024}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D^{a}\psi{}_{i}\big)\\
&+\frac{95i}{768}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{13i}{128}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\Box^c \psi{}_{i}\big)\\
&+\frac{35i}{1536}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{16}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\psi{}_{i}\big)
\end{aligned}
\tag{AL-EF2-4}
```

```math
\begin{aligned}
&-\frac{i}{32}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{1}{3}g\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D^{a}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{32}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{64}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D^{a}\psi{}_{i}\big)\\
&-\frac{i}{64}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{a}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{16}\varepsilon{}^{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{3}{32}g\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\big(\mathcal D^{d}\varphi{}_{i}\big)\\
&+\frac{13i}{16}g\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\varphi{}_{i}\big)\\
&+\frac{23i}{3072}gL{}^{i}{}^{j}\varepsilon{}^{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{j}\\
&-\frac{17}{1024}gL{}^{i}{}^{j}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{a}\widehat R(Q){}_{b}{}_{c}{}_{j}\\
&-\frac{5i}{6144}gL{}^{i}{}^{j}\varepsilon{}^{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\widehat R(Q){}^{d}{}^{e}{}_{j}\\
&-\frac{i}{192}gL{}^{i}{}^{j}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&-\frac{1}{4}\widehat G{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)
\end{aligned}
\tag{AL-EF2-5}
```

## Fixed sum and extent of verification

```math
\boxed{
S=\frac1{2\kappa_5^2}\int_M d^5x\,e\,
\left\{\ell_{2\text{-der}}+\alpha\ell_{\mathrm{Log}}\right\},
\qquad\alpha\ne0,
}\tag{A34}
```

The two-derivative density is A28 with slots A2-4.33–A2-4.37 and A27. The LOG density is A32 with A33 and the 21 AL-labelled component sums. A2–A27 fix the fields, bar, forms, connections, derivatives, fermion order, and boundary representatives. No restriction on the magnitude or sign of $`\alpha`$ is imposed here; its engineering dimension is $`[\alpha]=-2`$. No target-theory equation for $`N,E_3,V,V'`$ is used.

The symbolic convention checks appear in A8, A10, A13–A17, A22–A25, A27, and A29–A32. The 13 triplet, 94 spinor, 141 scalar, and 373 vector terms were converted to three-form notation and mapped back, preserving every coefficient and ordered factor. This is a transfer/equivalence check of 621 terms, not an independent superspace derivation of their coefficients.

The action uses the cited component constructions through two physical fermions, with the convention conversions stated above. The independent checks here concern the background and quadratic equations; they do not establish full nonlinear invariance of all Pauli couplings.

Numerical samples of free couplings and compensators in the source verification scripts do not establish a symbolic identity. The symbolic derivations below retain the dependence on fields, couplings and derivatives.

## Corrected gauge-preserving compensator

The missing factor $`i`$ in source equation (4.14) was corrected on 2026-09-27 in the common A18/A21 convention. The parameter and its defining traceless bilinear are

```math
\begin{aligned}
S^{ij}
&:=\bar\epsilon^{(i}\varphi^{j)}
 -\tfrac12\delta^{ij}\delta_{kl}\bar\epsilon^k\varphi^l,
\qquad \delta_{ij}S^{ij}=0,\\
\lambda^{ij}
&=-\frac{i}{\sqrt2L}S^{k(i}\delta^{j)\ell}\epsilon_{k\ell},
\qquad L\ne0
\end{aligned}
\tag{A35}
```

Here $`S^{ij}`$ is a bilinear, distinct from the action $`S`$; $`\lambda^{ij}`$ is an internal gauge parameter, distinct from the vector-slot spinor $`\lambda^i`$.

Combining $`-\delta_U(V_\mu)`$ in A18 with $`+2V_\mu^{(i}{}_kL^{j)k}`$ in A21 yields

```math
\delta_U L^{ij}=-2\lambda^{(i}{}_kL^{j)k},\qquad
(\delta_Q L^{ij})_{\mathrm{traceless}}=iS^{ij}
\tag{A36}
```

For an explicit sign check, put $`\mathsf J=(\epsilon_{ij})`$ and $`\mathsf S=(S^{ij})`$. Since $`\mathsf S^T=\mathsf S`$ and $`\mathop{\mathrm{tr}}\nolimits\mathsf S=0`$,

```math
\begin{aligned}
\mathsf J&=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad \mathsf J^2=-\mathbf1,\qquad
(\mathsf S\mathsf J)^T=\mathsf S\mathsf J,\\
\lambda&=-\frac{i}{\sqrt2L}\mathsf S\mathsf J,
\qquad
\lambda\mathsf J=\frac{i}{\sqrt2L}\mathsf S,\\
(\delta_U L^{ij})_{\mathrm{traceless}}
&=\left[-\frac{L}{\sqrt2}
 \big(\lambda\mathsf J+(\lambda\mathsf J)^T\big)\right]^{ij}
=-iS^{ij},\\
(\delta_Q+\delta_U)L^{ij}\big|_{\mathrm{traceless}}
&=iS^{ij}-iS^{ij}=0.
\end{aligned}
\tag{A37}
```

The old coefficient $`-1/(\sqrt2L)`$ left the residual $`(i-1)S^{ij}`$. A trace-proportional gauge parameter remains the alignment-preserving $`U(1)`$ freedom; A35 fixes only the mandatory traceless compensation. Source equations (4.14a)–(4.14b) show the same correction. Neither A28 nor A32 changes.

## Sufficiency of fermion order for the classical linear spectrum

For any zero-fermion background, write $`\Phi_{\mathrm F}=(\psi_\mu^i,\varphi^i)`$. Then

```math
S_{\mathrm{full}}=S^{[0]}+S^{[2]}+O(\Phi_{\mathrm F}^4),
\qquad
\left.
\frac{\delta^2 O(\Phi_{\mathrm F}^4)}{\delta\Phi^I\delta\Phi^J}
\right|_{\Phi_{\mathrm F}=0}=0.
\tag{A38}
```

The index $`I`$ runs over all independent bosonic and fermionic fields, and $`[n]`$ counts physical fermions. Two variations lower fermion degree by at most two. Thus the supplied action order suffices for both bosonic and fermionic classical linear spectra. This statement chooses no background and makes no expansion in $`\alpha`$; all implicit two-fermion terms remain included.

A35–A37 verify the compensator. The [quadratic-action analysis](../../ads5/quadratic_action.md) gives the AdS₅ bulk quadratic action Q40 and the factorized fermionic Euler operator Q57. Its checks include the source-coefficient comparisons Q58–Q59, the diagonal spinor operator Q60–Q62, and the local fermionic Noether identity Q67–Q76.

## Input fingerprints recorded with the action

The recorded SHA-256 fingerprints are: corrected two-derivative source, `73fbaa6bbe65af2bde118d1e1861a6e99dddd4e27c0b5d87dca697cb05a3e4c4`; its pre-correction version, `3170f23c5a72a5020c2d0c8b6f5eceadaa842b5cdd4fa795ff25b8093d0244da`; active LOG component source, `0e4c8b9cde0e2f2721da38b9e0313cf6151dbcf7286255bf9a1d774abe2c735c`; root conventions, `dddcde58009227f6ef0ca131f3d10c80fb98372775b4988bd6798be1791d10f3`. The (5.1)/(5.10) density and four map components used by A28 were unchanged by the correction.

