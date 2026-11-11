# Ungauged Composite Map for a Single Multiplet

Here

```math
L=\sqrt{L_{ij}L^{ij}},\qquad L\neq0.
```

Since the map contains $`L^{-1}`$, $`L^{-3}`$, $`L^{-5}`$ and $`L^{-7}`$, it is defined only in this domain. On the real positive-square-root branch of $`L`$, this condition is $`L>0`$; no extension to $`L=0`$ is assumed.

$`\mathcal D`$, $`\Box^c`$ and the hatted curvatures use the definitions in [superconformal_definitions.md](superconformal_definitions.md). In particular, $`\mathcal D\varphi`$ contains the $`+\frac i2(\mathord{\not{\mathcal D}}L^{ij})\psi_{\mu j}`$ contribution of Section 3.2; $`\Box^cL`$ uses the same corrected derivative.

## $`\rho_1`$

```math
\boxed{
\rho_1=
\frac{2N}{L}
+\frac{i}{L^3}L^{ij}\bar\varphi_i\varphi_j
}
```

## $`\lambda_{1i}`$

```math
\boxed{
\begin{aligned}
\lambda_{1i}={}&
-\frac{2i}{L}\mathord{\not{\mathcal D}}\varphi_i
-\frac{2N}{L^3}L_{ij}\varphi^j
-\frac{2i}{L^3}L_{ij}\mathord{\not{E}}\,\varphi^j\\
&+\frac{2i}{L^3}L^{jk}
 \bigl(\mathord{\not{\mathcal D}}L_{ij}\bigr)\varphi_k
+\frac{16}{L}L_{ij}\chi^j
+\frac4L(\gamma\!\cdot\!T)\varphi_i\\
&-\frac{6i}{L^5}L_{ij}L^{kl}
 \varphi^j\bar\varphi_k\varphi_l
+\frac{2i}{L^3}\varphi^k\bar\varphi_k\varphi_i .
\end{aligned}}
```

Here $`\varphi^k\bar\varphi_k`$ is an outer product in spinor space, not a scalar NW–SE bilinear.

## $`Y_{1ij}`$

```math
\boxed{
\begin{aligned}
Y_{1ij}={}&
\frac1L\Box^cL_{ij}
-\frac{L_{ij}}{L^3}\left(N^2+E_aE^a\right)
-\frac{L^{km}}{L^3}
 \mathcal D_aL_{ki}\mathcal D^aL_{jm}\\
&-\frac2{L^3}L_{(i}{}^k
 E_a\mathcal D^aL_{j)k}
+\frac{4L_{ij}}L\left(D+\frac23T^2\right)\\
&+\frac{iN}{L^3}\left[
 \bar\varphi_i\varphi_j
-\frac{3L_{ij}}{L^2}
 L^{kl}\bar\varphi_k\varphi_l
\right]\\
&-\frac1{L^3}\left[
 \bar\varphi_i\mathord{\not{E}}\,\varphi_j
-\frac{3L_{ij}}{L^2}
 L^{kl}\bar\varphi_k\mathord{\not{E}}\,\varphi_l
\right]\\
&-\frac{16i}{L}\left[
 \bar\chi_{(i}\varphi_{j)}
-\frac{L_{ij}}{L^2}
 L_{kl}\bar\chi^k\varphi^l
\right]\\
&+\frac2{L^3}L_{k(i}
 \bar\varphi^k\mathord{\not{\mathcal D}}\varphi_{j)}\\
&-\frac3{L^5}L_{k(i}L^{lm}
 \bar\varphi^k
 \bigl(\mathord{\not{\mathcal D}}L_{j)l}\bigr)\varphi_m\\
&+\frac1{2L^3}
 \bar\varphi^k
 \bigl(\mathord{\not{\mathcal D}}L_{k(i}\bigr)\varphi_{j)}\\
&+\frac{2i}{L^3}L_{ij}
 \bar\varphi^k\gamma^{ab}T_{ab}\varphi_k\\
&+\frac{15}{2L^7}L_{ij}
 \left(L^{kl}\bar\varphi_k\varphi_l\right)^2\\
&-\frac3{L^5}
 \left(L^{kl}\bar\varphi_k\varphi_l\right)
 \bar\varphi_i\varphi_j\\
&-\frac{3}{2L^5}L_{ij}
 \left(\bar\varphi_k\varphi_l\right)
 \left(\bar\varphi^k\varphi^l\right).
\end{aligned}}
```

## $`\widehat F_{1\mu\nu}`$

```math
\boxed{
\begin{aligned}
\widehat F_{1\mu\nu}={}&
\frac4L\,\mathcal D_{[\mu}E_{\nu]}
-\frac4{L^3}L^{ij}
 (\mathcal D_{[\mu}L_{ij})E_{\nu]}\\
&+\frac2L\,\widehat R_{\mu\nu}{}^{ij}(V)L_{ij}\\
&-\frac2{L^3}L_k{}^l
 (\mathcal D_\mu L^{kp})(\mathcal D_\nu L_{lp})\\
&-\frac2{L^3}(\mathcal D_{[\mu}L_{ij})
 \bar\varphi^i\gamma_{\nu]}\varphi^j\\
&+\frac6{L^5}L_{ij}L^{kl}
 (\mathcal D_{[\mu}L_{kl})
 \bar\varphi^i\gamma_{\nu]}\varphi^j\\
&+\frac4{L^3}L_{ij}\bar\varphi^i\gamma_{[\mu}
 \mathcal D_{\nu]}\varphi^j
-\frac{i}{L}\bar\varphi^i\widehat R_{\mu\nu i}(Q).
\end{aligned}}
```

## Notation

$`1`$ labels the composite vector multiplet and is placed at the start of the subscript group: $`\rho_1`$, $`\lambda_{1i}`$, $`Y_{1ij}`$ and $`\widehat F_{1\mu\nu}`$. The $`1`$ label for the same field denotes the same vector multiplet in the BF and composite-linear-multiplet files; a superscript or subscript label does not define a separate multiplet. Unlabeled $`L_{ij}`$ and $`L_{1ij}`$ are distinct objects.

```math
\mathord{\not{E}}=\gamma^aE_a,
\qquad
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},
\qquad
T^2=T_{ab}T^{ab},
```

```math
\mathord{\not{\mathcal D}}\varphi_i
=\gamma^a\mathcal D_a\varphi_i,
\qquad
\mathord{\not{\mathcal D}}L_{ij}
=\gamma^a\mathcal D_aL_{ij}.
```

Parenthesized and bracketed indices are symmetrized and antisymmetrized, respectively, with unit weight. No gauge choice or fermion truncation has been applied.
