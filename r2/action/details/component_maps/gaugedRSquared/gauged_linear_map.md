# Gauged Linear Map

```math
\begin{aligned}
L_{ij 1}
={}&
\sigma Y_{ij}
-\frac12 g\rho\sigma^{-1}L_{ij}
+\frac14 i\rho\sigma^{-1}\bar{\psi}_{(i}\psi_{j)}
-\frac12 i\bar{\lambda}_{(i}\psi_{j)},
\\[2mm]
\varphi_{i 1}
={}&
\frac12 i\sigma\not D\lambda_i
+\frac12 i\rho\not D\psi_i
+\rho\,\gamma\!\cdot\!T_g\,\psi_i
+\sigma\,\gamma\!\cdot\!T_g\,\lambda_i
-8\sigma\rho\chi_{g\,i}
-\frac18\gamma\!\cdot\!\widehat G\,\lambda_i
\\
&-\frac18\gamma\!\cdot\!\widehat F\,\psi_i
+\frac14\not D\sigma\,\lambda_i
+\frac14\not D\rho\,\psi_i
-\frac12Y_{ij}\psi^j
-\frac18 i\sigma^{-1}\lambda^j\bar{\psi}_i\psi_j
+\frac14 g\sigma^{-1}L_{ij}\lambda^j,
\\[2mm]
E^a_1
={}&
D_b\!\left(
-\frac12\sigma\widehat F^{ab}
-\frac12\rho\widehat G^{ab}
+8\sigma\rho T_g^{ab}
-\frac18 i\bar{\lambda}\gamma^{ab}\psi
\right)
-\frac18\varepsilon^{abcde}G_{bc}F_{de},
\\[2mm]
N_1
={}&
\frac12\rho\,\square^C\sigma
+\frac12\sigma\,\square^C\rho
+\frac12D_a\rho D^a\sigma
-\frac14\widehat G_{ab}\widehat F^{ab}
-4\rho\sigma\!\left(D_g+\frac{26}{3}T_g^2\right)
\\
&+4\sigma\widehat F^{ab}T_{g\,ab}
+4\rho\widehat G^{ab}T_{g\,ab}
+8i\sigma\bar{\chi}_g\lambda
+8i\rho\bar{\chi}_g\psi
-\frac14\bar{\lambda}\not D\psi
-\frac14\bar{\psi}\not D\lambda
+i\bar{\psi}\gamma\!\cdot\!T_g\,\lambda ,
\end{aligned}
\qquad
T_g^2\equiv T_{g\,ab}T_g^{ab}.
```

## $`E^{ab}`$ Map

```math
\mathcal K_g^{ab}\equiv
-\frac12\sigma\widehat F^{ab}
-\frac12\rho\widehat G^{ab}
+8\sigma\rho T_g^{ab}
-\frac18i\bar\lambda\gamma^{ab}\psi .
```

Using $`E^a=D_bE^{ab}`$, $`G_{bc}=2D_{[b}C_{c]}`$, and
$`D_{[b}F_{de]}=0`$,

```math
\begin{aligned}
D_b\!\left(\varepsilon^{abcde}C_cF_{de}\right)
&=
\varepsilon^{abcde}(D_bC_c)F_{de}
+\varepsilon^{abcde}C_cD_bF_{de}
\\
&=\frac12\varepsilon^{abcde}G_{bc}F_{de}.
\end{aligned}
```

Therefore,

```math
\boxed{
\begin{aligned}
E^{ab}_{1}
={}&
-\frac12\sigma\widehat F^{ab}
-\frac12\rho\widehat G^{ab}
+8\sigma\rho T_g^{ab}
-\frac18i\bar\lambda\gamma^{ab}\psi
-\frac14\varepsilon^{abcde}C_cF_{de}.
\end{aligned}}
```

Indeed,

```math
D_bE^{ab}
=
D_b\mathcal K_g^{ab}
-\frac18\varepsilon^{abcde}G_{bc}F_{de}
=E^a.
```

The map is defined modulo the two-form gauge freedom

```math
E^{\mu\nu}
\sim
E^{\mu\nu}
-\partial_\rho\widetilde\Lambda^{\mu\nu\rho}.
```
