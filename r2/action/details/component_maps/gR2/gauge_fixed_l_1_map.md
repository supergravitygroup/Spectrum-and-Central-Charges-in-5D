# Gauge-fixed composite linear-multiplet map

This record applies the gauge

```math
\sigma=1,\qquad b_\mu=0,\qquad \psi^i=0
```

to the earlier map on the gauged Dilaton–Weyl background. The dilatino
$`\psi^i`$ vanishes; the gravitino $`\psi_\mu^i`$ is retained. $`L_{ij}`$ and $`L_{1ij}`$
are distinct fields. Unlabeled $`L_{ij},\varphi_i,E^a,N`$ belongs to the linear multiplet
of the gauged background. Multiplet labels are subscripts.

By explicit spinor count, bosonic components retain $`0`$ and $`2`$,
while the fermionic $`\varphi_{1i}`$ component retains $`1`$-fermion terms.
Hatted fields and the supercovariant derivatives explicitly defined below
contain their own fermionic completions. Remainders $`\mathcal O_f(4)`$ and $`\mathcal O_f(3)`$
are displayed consistently with the previously selected action order.

## Derivatives compatible with the gauge

Spin connection including the gravitino and ordinary Lorentz–$`SU(2)`$ derivative:

```math
\begin{aligned}
\omega_\mu{}^{ab}
&=\omega_\mu{}^{ab}(e)
+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,
\\
\nabla_\mu\lambda_{1i}
&=\partial_\mu\lambda_{1i}
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\lambda_{1i}
+V_{\mu ij}\lambda_1^j.
\end{aligned}
```

$`\omega_\mu{}^{ab}(e)`$ is the torsion-free spin connection. $`\nabla`$ acts with the same
connections on other Lorentz and $`SU(2)`$ indices; $`\nabla_a=e_a{}^\mu\nabla_\mu`$.

```math
\boxed{
\mathscr D_a\rho_1
\equiv\left.\mathcal D_a\rho_1\right|
=\partial_a\rho_1-\frac i2\bar\psi_a\lambda_1.
}
```

The gauge does not set $`\mathcal D_a\psi_i`$ to zero:

```math
\left.\mathcal D_a\psi_i\right|
=\frac18\widehat G_{bc}\gamma^{bc}\psi_{ai}
+\frac14\widehat H_{bc}\gamma^{bc}\psi_{ai}
+\frac g2L_{ij}\psi_a^j
-\phi_{ai}.
```

The gauge-compatible fermion derivative used in the map is:

```math
\boxed{
\begin{aligned}
\mathscr D_a\lambda_{1i}
&\equiv
\left.\mathcal D_a\lambda_{1i}\right|
-\rho_1\left.\mathcal D_a\psi_i\right|
\\
&=\nabla_a\lambda_{1i}
+\frac14\widehat F_{1bc}\gamma^{bc}\psi_{ai}
-\frac14\rho_1\widehat G_{bc}\gamma^{bc}\psi_{ai}
+\frac i2\mathscr D_b\rho_1\,\gamma^b\psi_{ai}
\\
&\quad-Y_{1ij}\psi_a^j
-\frac g2\rho_1L_{ij}\psi_a^j.
\end{aligned}
}
```

The dependent $`S`$ connection $`\phi_{ai}`$ cancels in this combination.
$`D,T_{ab},\phi_\mu^i,f_\mu{}^a`$ does not appear explicitly in the final map; composite
definitions have been substituted without using field equations.

## Linear-multiplet components

```math
\boxed{
L_{1ij}=Y_{1ij}-\frac g2\rho_1L_{ij}.
}
```

```math
\boxed{
\begin{aligned}
\varphi_{1i}
={}&\frac i2\gamma^a\mathscr D_a\lambda_{1i}
-\frac14\widehat H_{ab}\gamma^{ab}\lambda_{1i}
+\frac g4L_{ij}\lambda_1^j
-g\rho_1\varphi_i
+\mathcal O_f(3).
\end{aligned}
}
```

```math
\boxed{
\begin{aligned}
E_1^a
={}&\frac12\rho_1\nabla_b\widehat G^{ab}
-\frac12\nabla_b\widehat F_1^{ab}
+\frac12\mathscr D_b\rho_1\,\widehat G^{ab}
-2\mathscr D_b\rho_1\,\widehat H^{ab}
\\
&+\frac18\rho_1\varepsilon^{abcde}
\widehat G_{bc}\widehat G_{de}
-\frac18\varepsilon^{abcde}
\widehat F_{1bc}\widehat G_{de}
-g\rho_1E^a
\\[2pt]
&-\frac14\bar\psi_b\gamma^a\mathscr D^b\lambda_1
+\frac14\bar\psi_b\gamma^b\mathscr D^a\lambda_1
+\frac i8\varepsilon^{abcde}
\nabla_b\bar\psi_c\,\gamma_{de}\lambda_1
\\
&+\frac i4\widehat G^{ab}\bar\psi_b\lambda_1
-\frac{3i}{4}\widehat H^{ab}\bar\psi_b\lambda_1
+\frac i4\widehat H^a{}_c\bar\psi_b\gamma^{bc}\lambda_1
-\frac i4\widehat H^b{}_c\bar\psi_b\gamma^{ac}\lambda_1
\\
&-\frac18\varepsilon^{abcde}
\widehat G_{bc}\bar\psi_d\gamma_e\lambda_1
+\frac18\varepsilon^{abcde}
\widehat H_{bc}\bar\psi_d\gamma_e\lambda_1
+\frac{ig}{8}L_{ij}\bar\psi_b^i\gamma^{ab}\lambda_1^j
+\mathcal O_f(4).
\end{aligned}
}
```

```math
\boxed{
\begin{aligned}
N_1
={}&\frac12\nabla^a\mathscr D_a\rho_1
-\frac g2Y_1{}^{ij}L_{ij}
+\frac14\widehat F_{1ab}\widehat G^{ab}
-\frac14\rho_1\widehat G_{ab}\widehat G^{ab}
\\
&+\rho_1\widehat G_{ab}\widehat H^{ab}
-\widehat F_{1ab}\widehat H^{ab}
-g\rho_1N
-\frac{g^2}{4}\rho_1L_{ij}L^{ij}
\\[2pt]
&-\frac i4\bar\psi_a\mathscr D^a\lambda_1
-\frac i4\bar\lambda_1\gamma^{ab}\nabla_a\psi_b
-\frac34\widehat H_{ab}\bar\psi^a\gamma^b\lambda_1
\\
&-\frac i{16}\varepsilon^{abcde}
\widehat G_{bc}\bar\psi_a\gamma_{de}\lambda_1
-\frac i{16}\varepsilon^{abcde}
\widehat H_{bc}\bar\psi_a\gamma_{de}\lambda_1
\\
&+\frac{3g}{8}L_{ij}\bar\psi_a^i\gamma^a\lambda_1^j
+ig\bar\varphi\lambda_1
+\mathcal O_f(4).
\end{aligned}
}
```

## Antisymmetric potential

```math
\boxed{
\begin{aligned}
E_1^{ab}
={}&\frac12\rho_1\widehat G^{ab}
-\frac12\widehat F_1^{ab}
-2\rho_1\widehat H^{ab}
-\frac18\varepsilon^{abcde}A_{1c}G_{de}
-\frac18\varepsilon^{abcde}C_cF_{1de}
\\
&+\frac i8\varepsilon^{abcde}
\bar\psi_c\gamma_{de}\lambda_1
+\frac18\rho_1\varepsilon^{abcde}
\bar\psi_c\gamma_d\psi_e
+\mathcal O_f(4).
\end{aligned}
}
```

## Field strengths in the gauge

```math
\begin{aligned}
\widehat F_{1ab}
&=F_{1ab}
-\bar\psi_{[a}\gamma_{b]}\lambda_1
+\frac i2\rho_1\bar\psi_{[a}\psi_{b]},
\\
\widehat G_{ab}
&=G_{ab}+\frac i2\bar\psi_{[a}\psi_{b]},
\\
\widehat H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}
-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},
\\
\widehat H_{ab}
&=-\frac1{12}\varepsilon_{abcde}\widehat H^{cde},
\\
F_{1\mu\nu}&=2\partial_{[\mu}A_{1\nu]},
\qquad
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}.
\end{aligned}
```

## Source and convention record

Conventions are in [CONVENTIONS.md](CONVENTIONS.md).
Derivatives use multiplets.pdf, (3.7)–(3.10), (3.21),
(A.3)–(A.7), and the corrected definitions in
[superconformal_definitions.md](../../../../../common/details/superconformal_definitions.md).
The printed $`-\frac12\not{\mathcal D}\rho\,\epsilon^i`$ in (3.8) is replaced by $`-\frac i2\not{\mathcal D}\rho\,\epsilon^i`$;
the $`+\frac12\not{\mathcal D}L^{ij}\psi_{\mu j}`$ in (3.7) is replaced by $`+\frac i2\not{\mathcal D}L^{ij}\psi_{\mu j}`$.
The Lorentz-connection term in (A.4) has sign $`+2\omega_\mu{}^c{}_{[a}T_{b]c}`$.

Gauged composite fields use [coomans.pdf](https://arxiv.org/abs/1210.4704), (5.2)–(5.7).
In particular, in this gauge,

```math
Y_{2ij}=-\frac g2L_{ij},\qquad
T_{ab}\big|=\frac18\widehat G_{ab}-\frac14\widehat H_{ab}.
```

The gauging term of $`Y_{2ij}`$ contains no extra $`i`$.
Gamma-basis canonicalization uses

```math
\gamma^{abc}=-\frac i2\varepsilon^{abcde}\gamma_{de},
\qquad
\gamma^{abcd}=i\varepsilon^{abcde}\gamma_e
```

and the project's NW–SE spinor contractions.
