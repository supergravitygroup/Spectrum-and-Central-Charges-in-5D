# Independent fields and variation order

[Action definition](../README.md).

<a id="3-independent-fields-and-order-of-variation"></a>

## Independent fields and order of variation

```math
\boxed{
\begin{aligned}
\mathcal F_B&=\{e_\mu{}^a,C_\mu,B_{\mu\nu},L,N,E_{\mu\nu\rho},V_\mu,V'_\mu{}^{ij}\},\\
\mathcal F_F&=\{\psi_\mu{}^i,\varphi^i\}.
\end{aligned}}
```
$`V'`$ is the symmetric traceless internal connection and has two internal components.

```math
E^a=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}
-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}.
```
Thus $`E_a`$ and $`E_3`$ are not two independent fields. $`\delta E_a`$ is the total variation of the vielbein, epsilon, three-form, and fermion dependence on the right-hand side.

The dependency order is
```math
\mathcal F_B,\mathcal F_F
\longrightarrow(E,\widehat G,\widehat H,\omega)
\longrightarrow T\longrightarrow\phi\longrightarrow\chi
\longrightarrow f\longrightarrow D
```
In particular,
```math
\begin{aligned}
\mathcal D_\mu\psi^i|_{\mathrm P}
&=\left(\frac14\gamma\cdot\widehat G-\gamma\cdot T\right)\psi_\mu{}^i
-\frac g2L^{ij}\psi_{\mu j}-\phi_\mu{}^i,\\
\chi^i&=\frac i8\gamma^\mu\mathcal D_\mu\psi^i|_{\mathrm P}
+\frac g8\varphi^i+O(\Psi^3),\\
f_\mu{}^a&=-\frac16\mathcal R_\mu{}^a+\frac1{48}e_\mu{}^a\mathcal R,
\qquad f_a{}^a=-\frac1{16}\mathcal R,\\
D&=\frac12f_a{}^a-\frac1{16}\widehat G^2-\frac{26}{3}T^2
+2\widehat G\cdot T+\frac g4N+\frac{g^2L^2}{16}\\
&\quad-\frac i8\bar\psi_a\mathcal D^a\psi|_{\mathrm P}
-\frac12\bar\psi_a\gamma^a\chi+O(\Psi^4).
\end{aligned}
```
$`\psi^i=0`$ does not imply $`\mathcal D\psi^i=0`$. In the presence of fermions, $`\mathcal R`$ is not identical to the ordinary Ricci scalar.

For a composite $`Z[\Phi]`$, after inserting field dependencies, the variation proceeds as
```math
\delta S[\Phi,Z[\Phi]]
=\left.\delta S\right|_Z+
\int\frac{\delta S}{\delta Z}\,\delta Z[\Phi]
```
All contributions are collected in front of the same independent $`\delta\Phi`$, retaining integration by parts and Grassmann ordering. This chain rule is not a complete list of Euler equations; it is the variational principle used in the background and linearized calculations below.

