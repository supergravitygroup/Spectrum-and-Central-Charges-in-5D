# Gauged composite linear-multiplet map

This map substitutes expressions (5.3)–(5.7) of local
[coomans.pdf](https://arxiv.org/abs/1210.4704), together with the gauged $`Y_g`$ in (5.2),
for the explicit fields $`D`$, $`T_{ab}`$, and $`\chi`$ in `composite_linear_multiplet.md`.
The two input vector multiplets remain $`(\rho_A,\lambda_{Ai},Y_{Aij},A_{A\mu})`$, $`A=1,2`$.

Action contributions with four or more fermions are omitted.
$`\varphi_{1i}`$ is retained through one fermion; $`L_{1ij}`$, $`E_1^a`$, $`N_1`$, and $`E_1^{ab}`$
through two. $`\mathcal O_{\mathrm f}(n)`$ denotes omitted contributions with at least $`n`$
fermions. Counting concerns explicit spinors; supercovariant derivatives
and curvatures are unexpanded. Their dependent fields are evaluated
with the same gauged $`D_g,T_{ab},\chi_g,Y_g`$ expressions. No gauge fixing is applied.

Multiplet labels appear first in the subscript group. Unlabeled $`L_{ij},N,\varphi_i,E^a,E_{\mu\nu\rho}`$
are gauged-background fields, distinct from the composite linear-multiplet
components labeled $`1`$.

## Gauged background

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
\chi_{gi}
&=\frac{i}{8\sigma}\mathord{\not{\mathcal D}}\psi_i
+\frac{i}{16\sigma^2}(\mathcal D_a\sigma)\gamma^a\psi_i
-\frac1{16\sigma^3}\widehat H_{ab}\gamma^{ab}\psi_i\\
&\quad+\frac{g}{16\sigma^3}L_{ij}\psi^j
+\frac{g}{8\sigma^2}\varphi_i
+\mathcal O_{\mathrm f}(3).
\end{aligned}
```

The $`gL\psi`$ sign of lower-index $`\chi_{gi}`$ is determined by

```math
(L^{jk}\psi_k)\epsilon_{ji}=-L_{ij}\psi^j
```

The combination used in $`N_1`$ is:

```math
\begin{aligned}
D_g+\frac{26}{3}T_{ab}T^{ab}
={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}\mathcal D_a\sigma\mathcal D^a\sigma
+\frac3{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{2\sigma^3}\widehat G_{ab}\widehat H^{ab}\\
&+\frac{g^2}{16\sigma^4}L_{ij}L^{ij}
+\frac{g}{4\sigma^2}N
+\frac3{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi\\
&+\frac{3i}{32\sigma^3}\widehat G_{ab}\bar\psi\gamma^{ab}\psi
+\frac{3i}{16\sigma^4}\widehat H_{ab}\bar\psi\gamma^{ab}\psi\\
&-\frac{5ig}{16\sigma^4}L_{ij}\bar\psi^i\psi^j
+\frac{ig}{2\sigma^3}\bar\varphi\psi
+\mathcal O_{\mathrm f}(4).
\end{aligned}
```

## $`L_{1ij}`$

```math
\boxed{
L_{1ij}
=\rho_1Y_{2ij}
+\rho_2Y_{1ij}
-\frac i2\bar\lambda_{1(i}\lambda_{2j)}.
}
```

## $`\varphi_{1i}`$

```math
\boxed{
\begin{aligned}
\varphi_{1i}
={}&\frac i2\rho_1\mathord{\not{\mathcal D}}\lambda_{2i}
+\frac i2\rho_2\mathord{\not{\mathcal D}}\lambda_{1i}
-\frac{i\rho_1\rho_2}{\sigma}\mathord{\not{\mathcal D}}\psi_i\\
&+\frac i4(\mathcal D_a\rho_1)\gamma^a\lambda_{2i}
+\frac i4(\mathcal D_a\rho_2)\gamma^a\lambda_{1i}
-\frac{i\rho_1\rho_2}{2\sigma^2}
(\mathcal D_a\sigma)\gamma^a\psi_i\\
&-\frac12Y_{1ij}\lambda_2^j
-\frac12Y_{2ij}\lambda_1^j
-\frac{g\rho_1\rho_2}{2\sigma^3}L_{ij}\psi^j
-\frac{g\rho_1\rho_2}{\sigma^2}\varphi_i\\
&-\frac18\widehat F_{1ab}\gamma^{ab}\lambda_{2i}
-\frac18\widehat F_{2ab}\gamma^{ab}\lambda_{1i}\\
&+\frac{\rho_1}{8\sigma}\widehat G_{ab}\gamma^{ab}\lambda_{2i}
+\frac{\rho_2}{8\sigma}\widehat G_{ab}\gamma^{ab}\lambda_{1i}\\
&-\frac{\rho_1}{4\sigma^2}\widehat H_{ab}\gamma^{ab}\lambda_{2i}
-\frac{\rho_2}{4\sigma^2}\widehat H_{ab}\gamma^{ab}\lambda_{1i}
+\frac{\rho_1\rho_2}{2\sigma^3}
\widehat H_{ab}\gamma^{ab}\psi_i
+\mathcal O_{\mathrm f}(3).
\end{aligned}
}
```

## $`E_1^a`$

```math
\boxed{
\begin{aligned}
E_1^a
={}&-\frac12\rho_1\mathcal D_b\widehat F_2^{ab}
-\frac12\rho_2\mathcal D_b\widehat F_1^{ab}\\
&-\frac12(\mathcal D_b\rho_1)\widehat F_2^{ab}
-\frac12(\mathcal D_b\rho_2)\widehat F_1^{ab}\\
&+\frac{\rho_1\rho_2}{\sigma}\mathcal D_b\widehat G^{ab}
+\frac{\rho_2}{\sigma}(\mathcal D_b\rho_1)\widehat G^{ab}
+\frac{\rho_1}{\sigma}(\mathcal D_b\rho_2)\widehat G^{ab}\\
&-\frac{\rho_1\rho_2}{\sigma^2}
(\mathcal D_b\sigma)\widehat G^{ab}\\
&-\frac{2\rho_2}{\sigma^2}
(\mathcal D_b\rho_1)\widehat H^{ab}
-\frac{2\rho_1}{\sigma^2}
(\mathcal D_b\rho_2)\widehat H^{ab}
+\frac{4\rho_1\rho_2}{\sigma^3}
(\mathcal D_b\sigma)\widehat H^{ab}\\
&+\frac{\rho_1\rho_2}{8\sigma^2}
\varepsilon^{abcde}\widehat G_{bc}\widehat G_{de}
-\frac{g\rho_1\rho_2}{\sigma^2}E^a
-\frac18\varepsilon^{abcde}
\widehat F_{1bc}\widehat F_{2de}\\[4pt]
&+\frac{i\rho_2}{4\sigma^2}
(\mathcal D_b\rho_1)\bar\psi\gamma^{ab}\psi
+\frac{i\rho_1}{4\sigma^2}
(\mathcal D_b\rho_2)\bar\psi\gamma^{ab}\psi\\
&-\frac{i\rho_1\rho_2}{2\sigma^3}
(\mathcal D_b\sigma)\bar\psi\gamma^{ab}\psi
+\frac{i\rho_1\rho_2}{2\sigma^2}
\bar\psi\gamma^{ab}\mathcal D_b\psi\\
&-\frac i4\overline{\mathcal D_b\lambda_1}
\gamma^{ab}\lambda_2
-\frac i4\bar\lambda_1\gamma^{ab}\mathcal D_b\lambda_2
+\mathcal O_{\mathrm f}(4).
\end{aligned}
}
```

## $`N_1`$

```math
\boxed{
\begin{aligned}
N_1
={}&\frac12\rho_1\Box^c\rho_2
+\frac12\rho_2\Box^c\rho_1
+\frac12\mathcal D_a\rho_1\mathcal D^a\rho_2\\
&-\frac{\rho_1\rho_2}{\sigma}\Box^c\sigma
-\frac{\rho_1\rho_2}{2\sigma^2}
\mathcal D_a\sigma\mathcal D^a\sigma\\
&+Y_{1ij}Y_2^{ij}
-\frac14\widehat F_{1ab}\widehat F_2^{ab}\\
&+\frac{\rho_1}{2\sigma}\widehat F_{2ab}\widehat G^{ab}
+\frac{\rho_2}{2\sigma}\widehat F_{1ab}\widehat G^{ab}\\
&-\frac{\rho_1}{\sigma^2}\widehat F_{2ab}\widehat H^{ab}
-\frac{\rho_2}{\sigma^2}\widehat F_{1ab}\widehat H^{ab}\\
&-\frac{3\rho_1\rho_2}{4\sigma^2}
\widehat G_{ab}\widehat G^{ab}
+\frac{2\rho_1\rho_2}{\sigma^3}
\widehat G_{ab}\widehat H^{ab}\\
&-\frac{g\rho_1\rho_2}{\sigma^2}N
-\frac{g^2\rho_1\rho_2}{4\sigma^4}L_{ij}L^{ij}\\[4pt]
&-\frac14\bar\lambda_1\mathord{\not{\mathcal D}}\lambda_2
+\frac14\overline{\mathcal D_a\lambda_1}\gamma^a\lambda_2\\
&+\frac{\rho_1}{\sigma}\bar\lambda_2\mathord{\not{\mathcal D}}\psi
+\frac{\rho_2}{\sigma}\bar\lambda_1\mathord{\not{\mathcal D}}\psi
-\frac{3\rho_1\rho_2}{2\sigma^2}
\bar\psi\mathord{\not{\mathcal D}}\psi\\
&+\frac{\rho_1}{2\sigma^2}
(\mathcal D_a\sigma)\bar\lambda_2\gamma^a\psi
+\frac{\rho_2}{2\sigma^2}
(\mathcal D_a\sigma)\bar\lambda_1\gamma^a\psi\\
&+\frac{i}{8\sigma}
\widehat G_{ab}\bar\lambda_1\gamma^{ab}\lambda_2
-\frac{i}{4\sigma^2}
\widehat H_{ab}\bar\lambda_1\gamma^{ab}\lambda_2\\
&+\frac{i\rho_1}{2\sigma^3}
\widehat H_{ab}\bar\lambda_2\gamma^{ab}\psi
+\frac{i\rho_2}{2\sigma^3}
\widehat H_{ab}\bar\lambda_1\gamma^{ab}\psi\\
&+\frac{i\rho_1}{8\sigma^2}
\widehat F_{2ab}\bar\psi\gamma^{ab}\psi
+\frac{i\rho_2}{8\sigma^2}
\widehat F_{1ab}\bar\psi\gamma^{ab}\psi\\
&-\frac{3i\rho_1\rho_2}{8\sigma^3}
\widehat G_{ab}\bar\psi\gamma^{ab}\psi
-\frac{3i\rho_1\rho_2}{4\sigma^4}
\widehat H_{ab}\bar\psi\gamma^{ab}\psi\\
&-\frac{ig\rho_1}{2\sigma^3}
L_{ij}\bar\lambda_2^i\psi^j
-\frac{ig\rho_2}{2\sigma^3}
L_{ij}\bar\lambda_1^i\psi^j\\
&+\frac{5ig\rho_1\rho_2}{4\sigma^4}
L_{ij}\bar\psi^i\psi^j\\
&+\frac{ig\rho_1}{\sigma^2}\bar\varphi\lambda_2
+\frac{ig\rho_2}{\sigma^2}\bar\varphi\lambda_1
-\frac{2ig\rho_1\rho_2}{\sigma^3}\bar\varphi\psi
+\mathcal O_{\mathrm f}(4).
\end{aligned}
}
```

## $`E_1^{ab}`$ potential

```math
\boxed{
\begin{aligned}
E_1^{ab}
={}&-\frac12\rho_1\widehat F_2^{ab}
-\frac12\rho_2\widehat F_1^{ab}
+\frac{\rho_1\rho_2}{\sigma}\widehat G^{ab}
-\frac{2\rho_1\rho_2}{\sigma^2}\widehat H^{ab}\\
&-\frac18\varepsilon^{abcde}A_{1c}F_{2de}
-\frac18\varepsilon^{abcde}A_{2c}F_{1de}\\[4pt]
&+\frac{i\rho_1\rho_2}{4\sigma^2}\bar\psi\gamma^{ab}\psi
-\frac i4\bar\lambda_1\gamma^{ab}\lambda_2\\
&+\frac i8\rho_1\varepsilon^{abcde}
\bar\psi_c\gamma_{de}\lambda_2
+\frac i8\rho_2\varepsilon^{abcde}
\bar\psi_c\gamma_{de}\lambda_1\\
&+\frac18\rho_1\rho_2\varepsilon^{abcde}
\bar\psi_c\gamma_d\psi_e
+\mathcal O_{\mathrm f}(4).
\end{aligned}
}
```

## Canonicalization relations used

From (5.5) and project normalization:

```math
\begin{aligned}
E^a&=-\frac1{12}\varepsilon^{abcde}\mathcal D_bE_{cde},\\
\mathcal D_b\widehat H^{ab}
&=-\frac1{12}\varepsilon^{abcde}
\mathcal D_{[b}\widehat H_{cde]}\\
&=-\frac1{16}\varepsilon^{abcde}
\widehat G_{bc}\widehat G_{de}
-\frac g{24}\varepsilon^{abcde}\mathcal D_bE_{cde}\\
&=-\frac1{16}\varepsilon^{abcde}
\widehat G_{bc}\widehat G_{de}
+\frac g2E^a.
\end{aligned}
```

```math
\begin{aligned}
\gamma^{abc}
&=-\frac i2\varepsilon^{abcde}\gamma_{de},\qquad
\gamma^{abcd}=i\varepsilon^{abcde}\gamma_e,\\
\bar\lambda_2\mathord{\not{\mathcal D}}\lambda_1
&=-\overline{\mathcal D_a\lambda_1}\gamma^a\lambda_2,\\
\mathcal D_b(\bar\psi\gamma^{ab}\psi)
&=\overline{\mathcal D_b\psi}\gamma^{ab}\psi
+\bar\psi\gamma^{ab}\mathcal D_b\psi
=2\bar\psi\gamma^{ab}\mathcal D_b\psi.
\end{aligned}
```

## Notation

```math
\begin{gathered}
\bar X\Gamma Y=\bar X^i\Gamma Y_i,\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a,\\
F_{A\mu\nu}=2\partial_{[\mu}A_{A\nu]},\qquad
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
\end{gathered}
```

$`\psi^i`$ is the dilatino, $`\psi_\mu^i`$ the gravitino, and $`\varphi^i`$ the unlabeled
linear-multiplet fermion. Parenthesized and bracketed indices are
symmetrized and antisymmetrized, respectively, with unit weight.
Conventions are in [CONVENTIONS.md](CONVENTIONS.md); source definitions of the
retained supercovariant objects are in
[superconformal_definitions.md](../../../../../common/details/superconformal_definitions.md).
Dependent fields in this map are evaluated on the gauged background.
