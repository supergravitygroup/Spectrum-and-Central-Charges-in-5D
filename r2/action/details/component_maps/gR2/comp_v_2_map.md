# Gauged composite vector-multiplet map

This map substitutes expressions (5.3)–(5.7) of local
[coomans.pdf](https://arxiv.org/abs/1210.4704), together with the gauged $`Y_g`$ in (5.2),
for the explicit fields $`D`$, $`T_{ab}`$, and $`\chi`$ in `composite_vector_multiplet.md`.

Action contributions with four or more fermions are omitted.
For this purpose, $`\rho_1`$, $`Y_{1ij}`$, and $`\widehat F_{1ab}`$ are retained through
two fermions, and $`\lambda_{1i}`$ through one. $`\mathcal O_{\mathrm f}(n)`$ denotes omitted contributions
with at least $`n`$ fermions. Counting concerns explicit spinors;
supercovariant derivatives and curvatures are unexpanded. Their dependent
fields are evaluated with the same gauged $`D_g,T_{ab},\chi_g,Y_g`$ expressions.

The multiplet label $`1`$ appears first in the subscript group.
Unlabeled $`L_{ij}`$ and $`L_{1ij}`$ are distinct objects. No gauge fixing is applied.

## Definitions and gauged background

```math
L=\sqrt{L_{ij}L^{ij}},\qquad
L\neq0,\qquad
L_{ij}L^{jk}=\frac12L^2\delta_i{}^k.
```

```math
\begin{aligned}
Y_{gij}
&=\frac{i}{4\sigma}\bar\psi_{(i}\psi_{j)}
-\frac{g}{2\sigma}L_{ij},\\
\widehat H_{ab}
&=-\frac1{12}\varepsilon_{abcde}\widehat H^{cde},\\
\widehat H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
T_{ab}
&=\frac1{8\sigma}\widehat G_{ab}
-\frac1{4\sigma^2}\widehat H_{ab}
+\frac{i}{32\sigma^2}\bar\psi\gamma_{ab}\psi,\\
\chi_g^i
&=\frac{i}{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac{i}{16\sigma^2}(\mathcal D_a\sigma)\gamma^a\psi^i
-\frac1{16\sigma^3}\widehat H_{ab}\gamma^{ab}\psi^i\\
&\quad-\frac{g}{16\sigma^3}L^{ij}\psi_j
+\frac{g}{8\sigma^2}\varphi^i
+\mathcal O_{\mathrm f}(3).
\end{aligned}
```

```math
\begin{aligned}
D_g+\frac23T_{ab}T^{ab}
={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}\mathcal D_a\sigma\mathcal D^a\sigma
+\frac1{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{2\sigma^4}\widehat H_{ab}\widehat H^{ab}\\
&+\frac{g^2L^2}{16\sigma^4}
+\frac{gN}{4\sigma^2}
+\frac3{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi\\
&+\frac{i}{32\sigma^3}\widehat G_{ab}\bar\psi\gamma^{ab}\psi
+\frac{5i}{16\sigma^4}\widehat H_{ab}\bar\psi\gamma^{ab}\psi\\
&-\frac{5ig}{16\sigma^4}L^{kl}\bar\psi_k\psi_l
+\frac{ig}{2\sigma^3}\bar\varphi\psi
+\mathcal O_{\mathrm f}(4).
\end{aligned}
```

## $`\rho_1`$

```math
\boxed{
\rho_1
=\frac{2N}{L}
+\frac{i}{L^3}L^{ij}\bar\varphi_i\varphi_j
}
```

## $`\lambda_{1i}`$

```math
\boxed{
\begin{aligned}
\lambda_{1i}
={}&-\frac{2i}{L}\mathord{\not{\mathcal D}}\varphi_i
-\frac{2N}{L^3}L_{ij}\varphi^j
-\frac{2i}{L^3}L_{ij}E_a\gamma^a\varphi^j\\
&+\frac{2i}{L^3}L^{jk}
(\mathcal D_aL_{ij})\gamma^a\varphi_k
+\frac{2i}{L\sigma}L_{ij}\mathord{\not{\mathcal D}}\psi^j\\
&+\frac{i}{L\sigma^2}L_{ij}
(\mathcal D_a\sigma)\gamma^a\psi^j
-\frac1{L\sigma^3}L_{ij}\widehat H_{ab}\gamma^{ab}\psi^j\\
&-\frac{gL}{2\sigma^3}\psi_i
+\frac{2g}{L\sigma^2}L_{ij}\varphi^j\\
&+\frac1{2L\sigma}\widehat G_{ab}\gamma^{ab}\varphi_i
-\frac1{L\sigma^2}\widehat H_{ab}\gamma^{ab}\varphi_i
+\mathcal O_{\mathrm f}(3).
\end{aligned}
}
```

## $`Y_{1ij}`$

```math
\boxed{
\begin{aligned}
Y_{1ij}
={}&\frac1L\Box^cL_{ij}
-\frac{N^2}{L^3}L_{ij}
-\frac1{L^3}L_{ij}E_aE^a\\
&-\frac1{L^3}L^{km}
\mathcal D_aL_{ki}\mathcal D^aL_{jm}
-\frac2{L^3}L_{(i}{}^kE_a\mathcal D^aL_{j)k}\\
&+\frac{L_{ij}}{L\sigma}\Box^c\sigma
+\frac{L_{ij}}{2L\sigma^2}
\mathcal D_a\sigma\mathcal D^a\sigma\\
&+\frac{L_{ij}}{4L\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac{2L_{ij}}{L\sigma^4}\widehat H_{ab}\widehat H^{ab}\\
&+\frac{gN}{L\sigma^2}L_{ij}
+\frac{g^2L}{4\sigma^4}L_{ij}\\[4pt]
&+\frac{iN}{L^3}\bar\varphi_i\varphi_j
-\frac{3iN}{L^5}L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&-\frac1{L^3}E_a\bar\varphi_i\gamma^a\varphi_j
+\frac3{L^5}L_{ij}L^{kl}
E_a\bar\varphi_k\gamma^a\varphi_l\\
&-\frac{2ig}{L\sigma^2}\bar\varphi_i\varphi_j
+\frac{2ig}{L^3\sigma^2}
L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&+\frac2{L^3}L_{k(i}
\bar\varphi^k\mathord{\not{\mathcal D}}\varphi_{j)}\\
&-\frac3{L^5}L_{k(i}L^{lm}
(\mathcal D_aL_{j)l})\bar\varphi^k\gamma^a\varphi_m\\
&+\frac1{2L^3}
(\mathcal D_aL_{k(i})\bar\varphi^k\gamma^a\varphi_{j)}\\
&+\frac{iL_{ij}}{4L^3\sigma}
\widehat G_{ab}\bar\varphi\gamma^{ab}\varphi
-\frac{iL_{ij}}{2L^3\sigma^2}
\widehat H_{ab}\bar\varphi\gamma^{ab}\varphi\\
&+\frac{3L_{ij}}{2L\sigma^2}
\bar\psi\mathord{\not{\mathcal D}}\psi\\
&+\frac{iL_{ij}}{8L\sigma^3}
\widehat G_{ab}\bar\psi\gamma^{ab}\psi
+\frac{5iL_{ij}}{4L\sigma^4}
\widehat H_{ab}\bar\psi\gamma^{ab}\psi\\
&-\frac{5ig}{4L\sigma^4}
L_{ij}L^{kl}\bar\psi_k\psi_l\\
&+\frac2{L\sigma}
\bar\varphi_{(i}\mathord{\not{\mathcal D}}\psi_{j)}
-\frac2{L^3\sigma}L_{ij}L^{kl}
\bar\varphi_k\mathord{\not{\mathcal D}}\psi_l\\
&+\frac1{L\sigma^2}
(\mathcal D_a\sigma)\bar\varphi_{(i}\gamma^a\psi_{j)}\\
&-\frac1{L^3\sigma^2}L_{ij}L^{kl}
(\mathcal D_a\sigma)\bar\varphi_k\gamma^a\psi_l\\
&+\frac{i}{L\sigma^3}
\widehat H_{ab}\bar\varphi_{(i}\gamma^{ab}\psi_{j)}\\
&-\frac{i}{L^3\sigma^3}L_{ij}L^{kl}
\widehat H_{ab}\bar\varphi_k\gamma^{ab}\psi_l\\
&-\frac{ig}{L\sigma^3}
L_{k(i}\bar\varphi^k\psi_{j)}
+\frac{5ig}{2L\sigma^3}L_{ij}\bar\varphi\psi
+\mathcal O_{\mathrm f}(4).
\end{aligned}
}
```

## $`\widehat F_{1ab}`$

```math
\boxed{
\begin{aligned}
\widehat F_{1ab}
={}&\frac4L\mathcal D_{[a}E_{b]}
-\frac4{L^3}L^{ij}(\mathcal D_{[a}L_{ij})E_{b]}\\
&+\frac2L L_{ij}\widehat R_{ab}{}^{ij}(V)
-\frac2{L^3}L_k{}^l
(\mathcal D_aL^{kp})(\mathcal D_bL_{lp})\\[4pt]
&-\frac2{L^3}(\mathcal D_{[a}L_{ij})
\bar\varphi^i\gamma_{b]}\varphi^j\\
&+\frac6{L^5}L_{ij}L^{kl}
(\mathcal D_{[a}L_{kl})
\bar\varphi^i\gamma_{b]}\varphi^j\\
&+\frac4{L^3}L_{ij}
\bar\varphi^i\gamma_{[a}\mathcal D_{b]}\varphi^j
-\frac{i}{L}\bar\varphi^i\widehat R_{abi}(Q)
+\mathcal O_{\mathrm f}(4).
\end{aligned}
}
```

## Notation

```math
\bar X\Gamma Y=\bar X^i\Gamma Y_i,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a,\qquad
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
```

$`\psi^i`$ is the dilatino, $`\psi_\mu^i`$ the gravitino, and $`\varphi^i`$ the unlabeled
linear-multiplet fermion. Parenthesized and bracketed indices are
symmetrized and antisymmetrized with unit weight. Tangent components
are defined by $`\widehat F_{1ab}=e_a{}^\mu e_b{}^\nu\widehat F_{1\mu\nu}`$. Conventions are in [CONVENTIONS.md](CONVENTIONS.md);
source definitions of retained supercovariant objects are in
[superconformal_definitions.md](../../../../../common/details/superconformal_definitions.md).
Dependent fields in this map are evaluated on the gauged background.
