# R²: quadratic action on AdS5

[Notation dictionary](../notation.md).

[Reading guide](README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

This page determines the unreduced second-order action on the selected
[AdS5 background](background.md). It is the common input to the bosonic and
fermionic equations, before separating physical fields. The metric–scalar,
vector–form and gravitino–spinor couplings are retained because their
constraints and kinetic mixing must be solved together; the two-derivative
auxiliary-field classification cannot be imposed on this higher-derivative
action. The output is the pair of quadratic densities below, with the stated
surface terms. Continue to [gauge constraints](details/gauge_constraints.md),
then [eigenfields](details/masses_and_eigenfields.md) and
[norms](details/kinetic_norms.md). The
[paper-check package](../../computations/r2_ads5_paper_checks/README.md)
replays the regular and critical reduction identities; it does not replace
the source-to-density derivation.

<a id="7-quadratic-expansion-of-all-fields"></a>

## Quadratic expansion of all fields

```math
e_\mu{}^a=\bar e_\mu{}^a+u_\mu{}^a,\quad L_{\mathrm{field}}=L+s,
\quad N=N_0+n,\quad(C,B,E_3,V,V')=(c,b,a,v,w),
```
```math
(\psi_\mu,\varphi)=(\Psi_\mu,\zeta).
```
No independent-field fluctuation is set to zero merely because its background value vanishes. $`S^{(2)}`$ is the second-order coefficient itself; no second factor $`1/2`$ is inserted.

```math
h_{\mu\nu}=2u_{(\mu\nu)},\quad k_{\mu\nu}=u_\mu{}^\rho u_\nu{}^\sigma\bar g_{\rho\sigma},
\quad d_1=\mathop{\mathrm{tr}}\nolimits u,\quad
d_2=\frac{(\mathop{\mathrm{tr}}\nolimits u)^2-\mathop{\mathrm{tr}}\nolimits(u^2)}2,
```
```math
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu}+k_{\mu\nu},\quad
g^{\mu\nu}=\bar g^{\mu\nu}-h^{\mu\nu}+h^\mu{}_\rho h^{\rho\nu}-k^{\mu\nu},
\quad e/\bar e=1+d_1+d_2+O(3).
```
```math
\Gamma_1{}^\rho{}_{\mu\nu}=\tfrac12\bar g^{\rho\sigma}
(\nabla_\mu h_{\nu\sigma}+\nabla_\nu h_{\mu\sigma}-\nabla_\sigma h_{\mu\nu}),
```
```math
\Gamma_2{}^\rho{}_{\mu\nu}=\tfrac12\bar g^{\rho\sigma}
(\nabla_\mu k_{\nu\sigma}+\nabla_\nu k_{\mu\sigma}-\nabla_\sigma k_{\mu\nu})
-h^\rho{}_\sigma\Gamma_1{}^\sigma{}_{\mu\nu}.
```
$`R_1,R_2`$ are the curvature coefficients of these connections:
```math
\begin{aligned}
R_{1\mu\nu}&=\nabla_\rho\Gamma_1{}^\rho{}_{\mu\nu}-\nabla_\nu\Gamma_1{}^\rho{}_{\mu\rho},\\
R_{2\mu\nu}&=\nabla_\rho\Gamma_2{}^\rho{}_{\mu\nu}-\nabla_\nu\Gamma_2{}^\rho{}_{\mu\rho}
+\Gamma_1{}^\rho{}_{\rho\sigma}\Gamma_1{}^\sigma{}_{\mu\nu}
-\Gamma_1{}^\rho{}_{\nu\sigma}\Gamma_1{}^\sigma{}_{\mu\rho},\\
r_1&=\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h+2g^2L^2h,\\
r_2&=\bar g^{\mu\nu}R_{2\mu\nu}-h^{\mu\nu}R_{1\mu\nu}
+(h^\mu{}_\rho h^{\rho\nu}-k^{\mu\nu})\bar R_{\mu\nu}.
\end{aligned}
```
The gravitino contorsion
```math
K_\mu{}^{ab}=\frac12\bar\Psi^{[a}\gamma^{b]}\Psi_\mu
+\frac14\bar\Psi^a\gamma_\mu\Psi^b
```
is retained at second order.

The geometric expansion fixes which second-order metric and contorsion terms
enter. Next expand the form and composite fields before solving any form
constraint: a vanishing background field still has an independent fluctuation.
The linearized forms and composites are defined by
```math
\mathsf G=dc,\quad\mathsf H=db+\frac g2a,\quad Q=*\mathsf H,
\quad Q^2=-\frac13\mathsf H^2,
```
```math
\mathsf E^\mu=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu a_{\rho\sigma\lambda},\quad
\nabla_\nu Q^{\nu\mu}=g\mathsf E^\mu,\quad\nabla\cdot\mathsf E=0,
```
```math
\mathcal A_\mu=2\mathsf E_\mu/L+\sqrt2v_\mu,\quad\mathsf F=d\mathcal A,
\quad T_1=\tfrac18(\mathsf G+Q)
```
In particular,
```math
\rho'_1=2n/L+3gs,\quad
D_1=-r_1/32+gn/4+g^2Ls/8
```
is nonzero. With $`\nu_{ij}=\delta_{ij}/\sqrt2`$ and
$`U_{\mu ij}=2w_{\mu(i}{}^k\nu_{j)k}`$,
```math
Y'_{1ij}=\nu_{ij}\left(-\frac12r_1+4gn+5g^2Ls+\frac{\Box s}{L}\right)
-\nabla^\mu U_{\mu ij}
```
also retains the traceless triplet fluctuation.

Substitution into the action gives the bosonic density below. Its mixed
terms and derivatives of n are retained in the coupled Euler equations;
eliminating n using its two-derivative equation would change this kernel.
The subsequent [constraint reduction](details/gauge_constraints.md) states
where each elimination or division is valid. Critical values are treated in
the [undivided actions](details/critical_branches.md).

The bosonic quadratic density is
```math
\begin{aligned}
\mathcal L_B^{(2)}={}&A(r_2+d_1r_1-4g^2L^2d_2)
+(1-5\lambda g^2L)sr_1-3\lambda gnr_1
+\frac\lambda4(r_1-2\Box s/L)^2\\
&+\frac{g^2}2(4-12L+53\lambda g^2L^2)s^2
+g(-8+48\lambda g^2L)sn+(-2/L+19\lambda g^2)n^2\\
&+(1/L-23\lambda g^2/2)(\nabla s)^2
-\frac{12\lambda g}{L}\nabla s\cdot\nabla n-\frac{2\lambda}{L^2}(\nabla n)^2\\
&+2Aw_\mu{}^{ij}w^\mu{}_{ij}+2\lambda(\nabla\cdot w^{ij})^2
-\frac A2\mathsf G^2-\frac A3\mathsf H^2\\
&-(2/L+6\lambda g^2)\mathsf E^2-2\sqrt2v\cdot\mathsf E-4gc\cdot\mathsf E\\
&+\lambda\left[-\frac14\mathsf F^2-\frac{3gL}{2}\mathsf F\cdot(\mathsf G+2Q)
-\frac{9g^2L^2}{4}\mathsf G^2-\frac{9g^2L^2}{2}\mathsf G\cdot Q\right].
\end{aligned}
```

For the fermionic block, the
[component-to-Hessian reduction](details/fermionic_operator_reduction.md#from-the-component-density-to-the-hessian)
explains the cancellations leading to these operators. Vary the coupled
expression with respect to the independent gravitino and spinor; the
composite Lambda is not a new independent field.

For fermions, with
```math
\mathscr R^\mu\Psi=\gamma^{\mu\nu\rho}\nabla_\nu\Psi_\rho
+3m\gamma^{\mu\nu}\mathbb J\Psi_\nu,\quad
\mathcal H=\mathord{\not{\nabla}}-m\mathbb J,\quad
\mathcal K_F=\mathord{\not{\nabla}}+5m\mathbb J,
```
```math
\Lambda=\frac23\mathbb I\gamma_\mu\mathscr R^\mu\Psi
-\frac{2i}{L}\mathcal K_F\zeta
```
the bulk-equivalent expression that eliminates no field is
```math
\begin{aligned}
S_F^{(2)}\simeq{}&-A\langle\Psi_\mu,\mathscr R^\mu\Psi\rangle
+\frac{2A}{L^2}\langle\zeta,\mathord{\not{\nabla}}\zeta\rangle
+\frac{7igA}{L}\langle\zeta,\mathbb I\zeta\rangle\\
&+\frac{4iA}{3L}\langle\zeta,\mathbb I\gamma_\mu\mathscr R^\mu\Psi\rangle
-\frac\lambda2\langle\Lambda,\mathcal H\Lambda\rangle
\end{aligned}
```
Here $`\langle\ ,\ \rangle`$ is the symplectic–Majorana bilinear integrated with the background volume. $`\Lambda`$ is not an independent fermion.

In the full selected boundary representative,
```math
S^{(2)}=\int\bar e\,[\mathcal L_B^{(2)}+\mathcal L_F^{(2)}
+\nabla_\mu(J_{\mathrm{sc}}^\mu+J_{\mathrm{form}}^\mu+J_F^\mu)]
```
The [unreduced fermionic density and explicit surface currents](details/fermionic_density.md) give the source expressions from `quadratic_action_ads5.bg` §§5–6; the [operator reduction](details/fermionic_operator_reduction.md) supplies Eqs. (F.1)–(F.6). In the reduced fermionic expressions here, $`\simeq`$ is not used as equality of full actions concealing this boundary calculation.

