# Weyl-squared map

Conventions: [CONVENTIONS.md](component_maps/Weyl2Action/CONVENTIONS.md). Hatted curvatures and full supercovariant derivatives are used without expanding composite fields. $`T^2:=T_{ab}T^{ab}`$ and $`T^4:=T_{ab}T^{bc}T_{cd}T^{da}`$.

The $`N`$ and $`E_a`$ below record results obtained from the $`\delta\varphi^i`$ calculation in the component derivation. The calculation used the stated Lorentz sign compatible with the Clifford algebra:

```math
\mathcal D_\mu T_{ab}
=\partial_\mu T_{ab}-b_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}
-\frac{i}{2}\bar\psi_\mu\gamma_{ab}\chi
+\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
```

This line records the correction derived in the component derivation to the Lorentz sign of the printed $`T`$ derivative in `CONVENTIONS.md`.

## $`L_{ij}`$

Özkan–Pang, [welySquared.pdf](https://arxiv.org/abs/1301.6622), (5.8):

```math
L_{ij}
=\frac{i}{4}\overline{\widehat R}_{ab\,(i}(Q)
                  \widehat R^{ab}{}_{j)}(Q)
+\frac{256i}{3}\bar\chi_{(i}\chi_{j)}
+\frac{16}{3}\widehat R_{ab\,ij}(V)T^{ab}.
```

## $`\varphi^i`$

Expression obtained in the calculation from $`\delta_Q L_{ij}=i\bar\epsilon_{(i}\varphi_{j)}`$ and $`\varphi^i=\epsilon^{ij}\varphi_j`$:

```math
\begin{aligned}
\varphi^i={}&
-\frac18\gamma_{cd}\widehat R_{ab}{}^i(Q)\,\widehat C^{abcd}
-4i\gamma_c\widehat R_{ab}{}^i(Q)\,\mathcal D^aT^{bc}
+\frac{128}{3}\chi^iD\\
&+8i\gamma_c\mathcal D^c\widehat R_{ab}{}^i(Q)\,T^{ab}
+8i\gamma_a\mathcal D^c\widehat R_{bc}{}^i(Q)\,T^{ab}\\
&-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\,\chi^i
+\frac{1024}{9}T^2\chi^i
+\frac{128i}{3}\gamma_a\mathcal D_b\chi^i\,T^{ab}\\
&+\frac83\gamma_{ab}\widehat R_{cd}{}^i(Q)\,T^{ab}T^{cd}\\
&+\frac12\widehat R^{ab\,i}{}_{j}(V)\,\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j.
\end{aligned}
```

In this record, the coefficient of the $`\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}`$ term is $`8/3`$, as obtained in the component derivation; the same coefficient in the paper's printed $`\varphi^i`$ expression in (5.8) is $`16/3`$.

## $`N`$

```math
\begin{aligned}
N={}&
\frac18\widehat C_{abcd}\widehat C^{abcd}
+\frac{64}{3}D^2
+\frac{1024}{9}T^2D
-\frac{16}{3}\widehat C_{abcd}T^{ab}T^{cd}\\
&-\frac13\widehat R_{ab}{}^{ij}(V)
             \widehat R^{ab}{}_{ij}(V)\\
&-\frac{64}{3}\mathcal D_aT_{bc}\mathcal D^aT^{bc}
+\frac{64}{3}\mathcal D_bT_{ac}\mathcal D^aT^{bc}
-\frac{128}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{128}{3}\varepsilon_{abcde}
       T^{ab}T^{cd}\mathcal D_fT^{ef}
+1024T^4-\frac{2816}{27}(T^2)^2\\
&+\frac34\overline{\widehat R}_{ab}(Q)
                  \mathord{\not{\mathcal D}}\widehat R^{ab}(Q)
-\frac{256}{3}\bar\chi\mathord{\not{\mathcal D}}\chi\\
&-\frac i2\overline{\widehat R}_{ab}(Q)
                 \gamma\!\cdot\!T\,\widehat R^{ab}(Q)
-\frac{160i}{3}T^{ab}\overline{\widehat R}_{ab}(Q)\chi.
\end{aligned}
```

## $`E_a`$

```math
\begin{aligned}
E_a={}&
\frac1{16}\varepsilon_{abcde}
       \widehat C^{bcfg}\widehat C^{de}{}_{fg}
-\frac1{12}\varepsilon_{abcde}
       \widehat R^{bc\,ij}(V)\widehat R^{de}{}_{ij}(V)\\
&+\mathcal D^b\left(
4\widehat C_{abcd}T^{cd}
-\frac{64}{3}DT_{ab}
-\frac{128}{9}T_{ab}T^2
-\frac{512}{3}T_{ac}T^{cd}T_{bd}
\right)\\
&-32\varepsilon_{abcde}\mathcal D^b\left(
\frac23T^{cf}\mathcal D_fT^{de}
+T^c{}_f\mathcal D^dT^{ef}
\right)\\
&+\frac i2\overline{\widehat R}_{bc}(Q)
                  \mathcal D_a\widehat R^{bc}(Q)
+\frac{3i}{2}\overline{\widehat R}^{bc}(Q)
                  \mathcal D_b\widehat R_{ca}(Q)\\
&-\frac{128i}{3}\bar\chi\gamma_{ab}\mathcal D^b\chi
+8i\overline{\widehat R}_{ab}(Q)\mathcal D^b\chi
-8i\bar\chi\mathcal D^b\widehat R_{ab}(Q)\\
&+\frac{16}{3}T^{bc}\overline{\widehat R}_{bc}(Q)\gamma_a\chi
+16T^{bc}\overline{\widehat R}_{ab}(Q)\gamma_c\chi\\
&+\frac12T^{bc}\overline{\widehat R}_{bd}(Q)
                    \gamma_a\widehat R_c{}^d(Q)
-\frac38\overline{\widehat R}_{bc}(Q)
                    \gamma_a\gamma\!\cdot\!T\,\widehat R^{bc}(Q).
\end{aligned}
```
