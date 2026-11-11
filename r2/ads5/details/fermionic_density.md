# R² on AdS5: unreduced fermion density and surface currents

[Quadratic action](../quadratic_action.md) · [Operator reduction](fermionic_operator_reduction.md)

This appendix gives the component expression behind the compact fermionic Hessian. The source is `SpectrumAnalysis/R^2/quadratic_action_ads5.bg`, §§1, 3, 5–6; the operator reduction is recorded in its §10. The action input is [the assembled R² theory](../../action/details/source_action.md), Eqs. (A.19), (M.1)–(M.4), and (A.31)–(A.35). All spinor bilinears retain the source's NW–SE contraction and linear Majorana bar.

## Background and notation

Here $`L_0`$ and $`A_0`$ denote the quantities written as $`L`$ and $`A`$ in the spectrum summary. The branch is

```math
\lambda\equiv\lambda_{R^2},\qquad
L_0=\frac{2}{1+\sqrt{1-3\lambda g^2}},\quad
g\ne0,\quad\lambda g^2\le\frac13,
```

```math
N_0=-\frac32gL_0^2,\quad R_0=-10g^2L_0^2,\quad
\bar R_{\mu\nu}=-2g^2L_0^2\bar g_{\mu\nu},\quad
\ell^{-2}=\frac12g^2L_0^2,
```

```math
3\lambda g^2L_0^2-4L_0+4=0,\qquad
A_0=L_0-3\lambda g^2L_0^2=4-3L_0.
```

The unreduced density and its component-to-Hessian identities use the background polynomial, not an assumption that $`A_0>0`$. Generic eigenfield diagonalization additionally requires $`\lambda A_0(2-L_0)\ne0`$. The $`A_0=0`$ and $`L_0=2`$ cases retain the original equations in [critical branches](critical_branches.md).

```math
\rho'_0=-3gL_0,\quad Y'_{0ij}=\nu_{ij}y_0,\quad
\nu_{ij}=\delta_{ij}/\sqrt2,\quad y_0=\frac32g^2L_0^2,\quad
f_{0a}{}^a=\frac58g^2L_0^2,\quad T_0=D_0=0.
```

The background form strengths and fermions vanish. The independent fluctuations are defined in the [quadratic action](../quadratic_action.md): $`(\psi_\mu,\varphi)=(\Psi_\mu,\zeta)`$, $`L_{\rm field}=L_0+s`$, $`N=N_0+n`$, and $`(C,B,E_3,V,V')=(c,b,a,v,w)`$. All derivatives and contractions below use the background metric.

<a id="linear-fermion-composites"></a>

## Forms and linear fermion composites

```math
\begin{gathered}
\mathsf G=dc,\quad\mathsf H=db+\tfrac g2a,\quad
Q_{ab}=\tfrac16\varepsilon_{abcde}\mathsf H^{cde},\quad Q^2=-\tfrac13\mathsf H^2,\\
\mathsf E^{\mu\nu}=-\tfrac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}a_{\rho\sigma\lambda},\quad
\mathsf E^\mu=\nabla_\nu\mathsf E^{\mu\nu},\\
\mathcal A_\mu=2\mathsf E_\mu/L_0+\sqrt2v_\mu,\quad
\mathsf F_{\mu\nu}=2\nabla_{[\mu}\mathcal A_{\nu]},\quad
T_{1ab}=\tfrac18(\mathsf G_{ab}+Q_{ab}),\\
\widehat G_{2\mu\nu}=\tfrac i2\bar\Psi_{[\mu}\Psi_{\nu]},\quad
\widehat H_{2\mu\nu\rho}=\tfrac32c_{[\mu}\mathsf G_{\nu\rho]}
-\tfrac34\bar\Psi_{[\mu}\gamma_\nu\Psi_{\rho]}.
\end{gathered}
```

The following symbols are linear differential expressions in $`(\Psi,\zeta)`$, rather than additional independent fields:

```math
\begin{aligned}
\mathcal Q_{\mu\nu}{}^i&=2\nabla_{[\mu}\Psi_{\nu]}{}^i,\\
\Phi_\mu{}^i&=\tfrac i3\gamma^a\mathcal Q_{\mu a}{}^i
-\tfrac i{24}\gamma_\mu\gamma^{ab}\mathcal Q_{ab}{}^i,
\qquad\gamma^a\Phi_a{}^i=\tfrac i8\gamma^{ab}\mathcal Q_{ab}{}^i,\\
\mathfrak k_{\mu i}&=\tfrac{gL_0}2\nu_{ij}\Psi_\mu{}^j-\Phi_{\mu i},\\
\Xi^i&=\tfrac1{64}\gamma^{ab}\mathcal Q_{ab}{}^i
-\tfrac{igL_0}{16}\nu^{ij}\gamma^a\Psi_{aj}+\tfrac g8\zeta^i,\\
\mathfrak p_{\mu i}&=\nabla_\mu\zeta_i+\tfrac{3gL_0^2}4\Psi_{\mu i}
+3L_0\nu_{ij}\Phi_\mu{}^j,\\
\Lambda_i&=-\tfrac{2i}{L_0}\mathord{\not{\nabla}}\zeta_i
+\nu_{ij}\gamma^{ab}\mathcal Q_{ab}{}^j
-2igL_0\gamma^a\Psi_{ai}+5g\nu_{ij}\zeta^j,\\
\mathfrak W_{\mu i}&=\nabla_\mu\Lambda_i-\tfrac32g^2L_0^2\nu_{ij}\Psi_\mu{}^j
+3gL_0\Phi_{\mu i},\\
\bar\Lambda_i&=-\tfrac{2i}{L_0}(\nabla_a\bar\zeta_i)\gamma^a
-\nu_{ij}\bar{\mathcal Q}_{ab}{}^j\gamma^{ab}
-2igL_0\bar\Psi_{ai}\gamma^a+5g\nu_{ij}\bar\zeta^j.
\end{aligned}
```

In particular, $`(\mathcal D_\mu\psi_i)^{(1)}=\mathfrak k_{\mu i}`$ is nonzero even though the defining dilatino vanishes on the gauge slice.

<a id="raw-density"></a>

## Unreduced fermionic density

```math
\begin{aligned}
\mathcal L_F^{(2)}={}&iA_0\bar\Phi_a{}^i\gamma^{ab}\Psi_{bi}
+iA_0\bar\Psi_a{}^i\mathfrak k^a{}_i
+\frac{2iA_0}{L_0}\nu_{ij}\bar\Psi^{ai}\mathfrak p_a{}^j\\
&-\frac{2A_0}{L_0}\nu_{ij}\bar\zeta^i\gamma^a\Phi_a{}^j
-\frac{2A_0}{L_0^2}\bar\zeta^i\gamma^a\mathfrak p_{ai}
-\frac{3igA_0}{L_0}\nu_{ij}\bar\zeta^i\zeta^j-2i\bar\Lambda^i\zeta_i\\
&+\frac{5-3L_0}2\nu_{ij}\bar\Psi_a{}^i\gamma^a\Lambda^j
+g(3L_0-2)\bar\Psi_a{}^i\gamma^a\zeta_i
+\frac{igL_0}2\nu_{ij}\bar\Psi_a{}^i\gamma^{ab}\Psi_b{}^j\\
&+\lambda\left[-\tfrac12\bar\Lambda^i\gamma^a\mathfrak W_{ai}
+48igL_0\bar\Lambda^i\Xi_i
+\tfrac{igL_0}4\nu_{ij}\bar\Lambda^i\Lambda^j
+\tfrac{9gL_0}4\bar\Lambda^i\gamma^a\mathfrak k_{ai}\right.\\
&\qquad-\tfrac{3gL_0}4\bar\Phi_a{}^i\gamma^a\Lambda_i
-36g^2L_0^2\bar\Psi_a{}^i\gamma^a\Xi_i
+\tfrac{9ig^2L_0^2}2\bar\Psi_a{}^i\mathfrak k^a{}_i\\
&\qquad\left.-\tfrac{3igL_0}4\bar\Psi_a{}^i\gamma^{ab}\mathfrak W_{bi}
-\tfrac{9ig^2L_0^2}4\bar\Psi_a{}^i\gamma^{ab}\Phi_{bi}\right].
\end{aligned}
```

This expression retains every independent fermionic fluctuation. It does not divide by $`\lambda`$, $`A_0`$, or $`19L_0-22`$. In the source, the delimiter after $`\bar\Lambda^i\gamma^a\mathfrak k_{ai}`$ contains the stray fragment `ight.`; the displayed equation restores `\right.` without changing the term or its coefficient.

<a id="surface-currents"></a>

## Surface currents

The bosonic density is given in the [quadratic action](../quadratic_action.md). The complete boundary representative uses

```math
\boxed{S^{(2)}=\int d^5x\,\bar e\,
\big[\mathcal L_B^{(2)}+\mathcal L_F^{(2)}
+\nabla_\mu(J_{\rm sc}^\mu+J_{\rm form}^\mu+J_F^\mu)\big].}
```

The required scalar coefficients, from source §4, are $`\rho_1=2n/L_0+3gs`$ and $`\rho_{2B}=-2ns/L_0^2-3gs^2/L_0`$. The contorsion is the $`K_\mu{}^{ab}`$ displayed in the quadratic action. With

```math
P^{\mu\nu}=d_1\bar g^{\mu\nu}-h^{\mu\nu},
```

```math
\begin{aligned}
J_{\rm sc}^\mu={}&-\frac{2A_0}{L_0}P^{\mu\nu}\partial_\nu s
+4\lambda g^2s\partial^\mu s+\frac{6\lambda g}{L_0}n\partial^\mu s
+\frac\lambda2\rho_1\partial^\mu\rho_1\\
&-\frac{3\lambda gL_0}2(\partial^\mu\rho_{2B}
+P^{\mu\nu}\partial_\nu\rho_1),\\
J_{\rm form}^\mu={}&-2(\mathcal A_\nu+2gc_\nu)\mathsf E^{\mu\nu}
+\frac\lambda2\mathcal A_\nu
[\mathsf F^{\mu\nu}+3gL_0(\mathsf G^{\mu\nu}+2Q^{\mu\nu})],\\
J_F^\mu={}&2A_0\bar e_a{}^\mu K_b{}^{ab}
+\frac{2iA_0}{L_0}\nu_{ij}\bar\Psi^{\mu i}\zeta^j
-\frac{3i\lambda g}{2L_0}\nu_{ij}\nabla^\mu(\bar\zeta^i\zeta^j)
+\frac{3i\lambda gL_0}4\bar\Psi^{\mu i}\Lambda_i.
\end{aligned}
```

the first variation on this background is

```math
\frac{\mathcal L^{(1)}}{\bar e}
=A_0(\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h)
-\frac{2A_0}{L_0}\Box s+\frac{\lambda\rho'_0}2\Box\rho_1.
```

This is a total derivative. It vanishes for compactly supported variations or boundary data that annul the stated surface variation; it need not vanish for arbitrary variations at a finite boundary. The bulk relation $`\simeq`$ in the operator reduction does not remove these currents from the action.
