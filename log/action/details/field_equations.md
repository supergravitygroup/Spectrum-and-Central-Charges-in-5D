# Field equations

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="4-field-equations-derivation-and-verification-scope"></a>

## Field equations: derivation and verification scope

This chapter derives the complete bosonic-body equations and the diagonal linear-multiplet fermion block. The selected spectrum uses the explicit AdS5 bilinear maps in [the quadratic action](../../ads5/quadratic_action.md), (Q31)–(Q40), (Q57), with the check scope stated there. The general block arrangement and the background-specific quadratic reduction have distinct roles.

Inputs are the fixed action, independent-field inventory, and root conventions reproduced above.

## Variation order and scope

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,[\ell_0(\Phi_{\rm B})+\ell_2(\Phi_{\rm B},\Phi_{\rm F})],
\qquad \ell_r=\ell_{2\partial,r}+\alpha\ell_{\log,r},
\quad \alpha\ne0,\quad g\ne0,\quad L\ne0.
\tag{E1}
```

Let $`\ell_r`$ have physical fermion degree $`r`$. Bosonic variation preserves that degree; fermionic variation lowers it by one. Imposing the background only after variation gives

```math
\begin{aligned}
(\delta_B S)_{\Phi_F=0}
&=\frac1{2\kappa_5^2}\int\delta_B(e\ell_0),\\
(\delta_F S)_{\text{one fermion}}
&=\frac1{2\kappa_5^2}\int e\,\delta_F\ell_2,\\
(\delta_B\delta_F S)_{\Phi_F=0}&=0,\\
(\delta_B\delta_B S)_{\Phi_F=0}
&=\delta_B\delta_B S_0,
\qquad
(\delta_F\delta_F S)_{\Phi_F=0}
=\delta_F\delta_F S_2.
\end{aligned}\tag{E2}
```

These equalities justify varying the bosonic body without deleting the fermionic Hessian. Four-fermion terms contribute to neither classical linear sector. The bosonic equations are evaluated on the zero-fermion body, while the fermionic Hessian determines the linear fermion sector.

Local Euler coefficients are defined using compactly supported test variations, without imposing physical boundary conditions. Exact divergences between density representatives are retained explicitly. No auxiliary is eliminated, no free parameter is assigned a numerical value, and no expansion in $`\alpha`$ is made.

## Reconstruction of the bosonic density

Here $`\nabla`$ is Levi–Civita, supplemented by the stated internal connection where necessary; it is not the full supercovariant $`\mathcal D`$. Define the following intermediate quantities:

```math
\begin{gathered}
U_{\mu\nu}:=-\frac1{12}\varepsilon_{\mu\nu\rho\sigma\lambda}H^{\rho\sigma\lambda},\qquad
I:=G_{\mu\nu}G^{\mu\nu},\quad J:=G_{\mu\nu}U^{\mu\nu},\quad K:=U_{\mu\nu}U^{\mu\nu},\\
j^\mu:=\nabla_\nu G^{\mu\nu},\qquad k_{\mu\nu\rho}:=3\nabla_{[\mu}U_{\nu\rho]},\\
A^\mu:=\varepsilon^{\mu\nu\rho\sigma\lambda}G_{\nu\rho}G_{\sigma\lambda},\quad
B^\mu:=\varepsilon^{\mu\nu\rho\sigma\lambda}U_{\nu\rho}U_{\sigma\lambda},\quad
D_\times^\mu:=\varepsilon^{\mu\nu\rho\sigma\lambda}U_{\nu\rho}G_{\sigma\lambda},\\
\mathcal F_{\mu\nu}^{ij}:=2\partial_{[\mu}V_{\nu]}^{ij}
-2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)},\qquad
L_{ij}=\frac L{\sqrt2}\delta_{ij}.
\end{gathered}\tag{E3}
```

The object $`B^\mu`$ is an epsilon contraction, not the two-form potential. $`D_\times^\mu`$ is not the scalar composite $`D`$. The two-form $`U`$ is not independent and is replaced by its E3 three-form expression in the final equations. Matrix products use $`G^\mu{}_\nu,U^\mu{}_\nu`$.

The epsilon contraction and form definition imply

```math
\begin{aligned}
U_{ab}U^{ab}
&=\frac1{144}(-2!3!)\delta_{[c}^{f}\delta_d^g\delta_{e]}^h
H^{cde}H_{fgh}=-\frac1{12}H_{abc}H^{abc},\\
\varepsilon^{abcde}U_{ab}&=H^{cde},\\
G&=dC,\qquad H=dB+\tfrac12C\wedge G+\tfrac g2E_3,\\
P^\mu&=-\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda},\qquad \nabla_\mu P^\mu=0,\\
\nabla_bU^{ab}&=-\tfrac1{16}\varepsilon^{abcde}G_{bc}G_{de}+\tfrac g2P^a
\end{aligned}\tag{E4}
```

The last line is the Bianchi identity $`dH=G\wedge G/2+g\,dE_3/2`$, not an $`E_3`$ equation.

### Two-derivative contribution

Using A20–A28, the bosonic composites become

```math
\begin{aligned}
f_a{}^a&=-R/16,\qquad T_{ab}=(G_{ab}-2U_{ab})/8,\\
D&=-R/32+5I/96+J/24-13K/24+gN/4+g^2L^2/16,\\
(\nabla L^{ij})(\nabla L_{ij})&=(\partial L)^2+2L^2V_\mu^{\prime ij}V^{\prime\mu}_{ij}.
\end{aligned}\tag{E5}
```

For the last line, write $`L^{ij}=Ln^{ij}`$ with $`n^{ij}=\delta^{ij}/\sqrt2`$. Since $`n_{ij}\nabla_\mu n^{ij}=0`$ and $`(\nabla_\mu n^{ij})(\nabla_\nu n_{ij})=2V_\mu^{\prime ij}V'_{\nu ij}`$,

```math
\begin{aligned}
\nabla_\mu L^{ij}\nabla^\mu L_{ij}
&=(\partial_\mu L)(\partial^\mu L)n^{ij}n_{ij}
+2L\partial_\mu L\,n_{ij}\nabla^\mu n^{ij}
+L^2\nabla_\mu n^{ij}\nabla^\mu n_{ij}\\
&=(\partial L)^2+2L^2V'^2.
\end{aligned}\tag{E6}
```

Combining the scalar, triplet, and field-strength slots gives

```math
\boxed{\begin{aligned}
\ell_{2\partial,0}\simeq_\partial{}&
L\left(R-\tfrac12I+4K+2V'^2\right)
+L^{-1}(\partial L)^2-2L^{-1}(P^2+N^2)\\
&-2\sqrt2P^\mu V_\mu-4gP^\mu C_\mu
-2gLN-4gN-\tfrac12g^2L^3+2g^2L^2
\end{aligned}}\tag{E7}
```

For example, the curvature and flux coefficients collect as

```math
\begin{aligned}
-2L^{-1}L^{ij}\Box^cL_{ij}
&\simeq_\partial 12L\,R/16-2L^{-1}L^{ij}\nabla^2L_{ij},\\
-\tfrac{16}{3}LT^2-8LD
&=\tfrac14LR-\tfrac12LI+4LK-2gLN-\tfrac12g^2L^3,\\
\tfrac34LR+\tfrac14LR&=LR,\\
(+2L^{-1}N^2)-4L^{-1}N^2&=-2L^{-1}N^2,\\
(+2L^{-1}P^2)-4L^{-1}P^2&=-2L^{-1}P^2
\end{aligned}\tag{E8}
```

The first line uses $`\Box^cL_{ij}=\nabla^2L_{ij}+6f_a{}^aL_{ij}`$. The notation $`\simeq_\partial`$ denotes only the displayed ordinary integrations by parts.

The exact change from the field-strength representative to the potential representative is

```math
\tfrac12eF_{\mu\nu}E^{\mu\nu}
=eA_\mu P^\mu+	frac1{12}\partial_\nu
(e\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda})
\tag{E9}
```

Thus $`P`$ in the term $`-4gC\cdot P`$ cannot be replaced by supercovariant $`E`$.

### LOG contribution

Expand the fixed LOG slots at fermion degree zero, evaluating full derivatives before gauge fixing. A representative with the same local Euler equations is

```math
\begin{aligned}
\ell_{\log,0}\simeq_\partial{}&
-\tfrac1{12}\varepsilon^{abcde}C_a\mathcal F_{bc}^{ij}\mathcal F_{deij}
+\tfrac16\mathcal F_{ab}^{ij}\mathcal F^{ab}_{ij}
+\tfrac g6L_{ij}\mathcal F_{ab}^{ij}G^{ab}
+\tfrac{2g}3L_{ij}\mathcal F_{ab}^{ij}U^{ab}\\
&-\tfrac16R_{ab}R^{ab}+\tfrac1{24}R^2
+\tfrac16R_{ab}G^{ac}G^b{}_c-\tfrac43R_{ab}G^{ac}U^b{}_c\\
&+R\left(\tfrac g6N-\tfrac{g^2}{12}L^2+\tfrac13J-\tfrac13K\right)
-\tfrac{g^2}6N^2+\tfrac{2g^3}3NL^2+\tfrac{5g^4}{24}L^4\\
&+gN(-I/3-2J/3+2K)+g^2L^2(I/24-J/6-K)\\
&-I^2/48-IJ/3+2IK/3+4J^2/3-4JK/3-2K^2\\
&-\mathop{\mathrm{tr}}\nolimits(G^4)/24+\mathop{\mathrm{tr}}\nolimits(G^3U)
-\tfrac43\mathop{\mathrm{tr}}\nolimits(G^2U^2)-\tfrac83\mathop{\mathrm{tr}}\nolimits(GUGU)
+\tfrac{16}3\mathop{\mathrm{tr}}\nolimits(GU^3)\\
&-j_aj^a/6+2k_{abc}k^{abc}/9
-\tfrac{g^2}4\big[(\partial L)^2+2L^2V'^2\big]\\
&+j_a(A^a/48+B^a/3-D_\times^a/6)+A^aB_a/12\\
&+gP^aj_a/3-gP^aA_a/24-2gP^aB_a/3+g^2P^2/3.
\end{aligned}\tag{E10}
```

The source covariant polynomial was reconstructed symbolically and compared, with exact rational coefficients, to this density and its explicit divergence. The independent identities used include

```math
X_{[a}\varepsilon_{bcdef]}=0,\quad
R_{a[bcd]}=0,\quad \nabla_{[a}G_{bc]}=0,\quad
\nabla_{[a}R_{bc]de}=0,\quad
\nabla^aR_{ab}=\tfrac12\nabla_bR,
\tag{E11}
```

together with E4, the covariant-derivative commutator, and the triplet identity

```math
L^{ij}L_i{}^kL_j{}^lL_{kl}=\tfrac12(L^{ij}L_{ij})^2
\tag{E12}
```

E12 was checked by coefficient comparison for a general symbolic symmetric two-by-two triplet. Earlier tests using numerical bosonic jets or free-field samples were not used.

In the divergence representative, $`E_{\log}^a=\nabla_bQ_{\log}^{ab}-\varepsilon^{abcde}\mathcal F_{bc}^{ij}\mathcal F_{deij}/12`$, with $`Q_{\log}^{ab}=-Q_{\log}^{ba}`$. Keep the exact boundary difference

```math
\begin{aligned}
C_a\nabla_bQ_{\log}^{ab}
&=\nabla_b(C_aQ_{\log}^{ab})+\tfrac12G_{ab}Q_{\log}^{ab},\\
\ell_{\log,0}^{\rm action}
&=\ell_{\log,0}^{(E10)}+\nabla_b(C_aQ_{\log}^{ab}+J_{\log}^b)
\end{aligned}\tag{E13}
```

The explicit source currents are BC-04, BC-08, and BC-10 of [EXACT_BOSONIC_COMPARISON.md](component_construction/results/gauged_full_fermionic_log/sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md) in the supplied LOG package. After subtracting these currents, the body-minus-E10 residual reduced to zero without further integration-by-parts equivalences. No physical boundary prescription was imposed in this check.

## Scalar equations

### Variation of $`N`$

All bosonic terms depending on $`N`$ are

```math
\begin{aligned}
\ell_0\big|_N={}&-2N^2/L-2gLN-4gN\\
&+\alpha\left[gNR/6-g^2N^2/6+2g^3NL^2/3
+gN(-I/3-2J/3+2K)\right]
\end{aligned}\tag{E14}
```

Their variation is

```math
\delta_N(e\ell_0)
=e\left[-\frac{4N}{L}-2gL-4g
+\alpha\left(\frac g6R-\frac{g^2}3N+\frac{2g^3}3L^2
-\frac g3I-\frac{2g}3J+2gK\right)\right]\delta N.
\tag{E15}
```

Restoring the three-form gives

```math
\boxed{0=\mathcal E_N=
-\frac{4N}{L}-2gL-4g+
\alpha\left[
\frac g6R-\frac{g^2}3N+\frac{2g^3}3L^2
-\frac g3G_{ab}G^{ab}
+\frac g{18}G^{ab}\varepsilon_{abcde}H^{cde}
-\frac g6H_{abc}H^{abc}
\right].}\tag{E16}
```

This equation has not been used to eliminate $`N`$. No division by $`4/L+\alpha g^2/3`$ is made, so its zero locus is retained. Because the equation mixes $`N`$ with curvature, its algebraic form alone does not decide the dynamics of the coupled system.

### Variation of $`L`$

The derivative terms vary as

```math
\begin{aligned}
\delta\big[L^{-1}(\partial L)^2\big]
&=-L^{-2}(\partial L)^2\delta L+2L^{-1}\partial^\mu L\partial_\mu\delta L,\\
2L^{-1}\partial^\mu L\partial_\mu\delta L
&=2\nabla_\mu(L^{-1}\partial^\mu L\,\delta L)
-2\big[L^{-1}\Box L-L^{-2}(\partial L)^2\big]\delta L,\\
\delta\big[-\alpha g^2(\partial L)^2/4\big]
&=-\alpha g^2\nabla_\mu(\partial^\mu L\,\delta L)/2
+\alpha g^2\Box L\,\delta L/2
\end{aligned}\tag{E17}
```

Differentiating the remaining coefficients yields

```math
\boxed{\begin{aligned}
0=\mathcal E_L=\Big\{&
R-\tfrac12I+4K+2V'^2+\frac{(\partial L)^2}{L^2}
-\frac2L\Box L+\frac{2(P^2+N^2)}{L^2}
-2gN-\tfrac32g^2L^2+4g^2L\\
&+\alpha\Big[
\tfrac{g^2}2\Box L-g^2LV'^2
+\tfrac{g}{6\sqrt2}\delta_{ij}\mathcal F_{ab}^{ij}G^{ab}
+\tfrac{2g}{3\sqrt2}\delta_{ij}\mathcal F_{ab}^{ij}U^{ab}\\
&\hspace{3em}-\tfrac{g^2}6LR+\tfrac{4g^3}3LN+\tfrac{5g^4}6L^3
+g^2L(I/12-J/3-2K)\Big]\Big\}_{U_{ab}=-\varepsilon_{abcde}H^{cde}/12}.
\end{aligned}}\tag{E18}
```

## Explicit flux responses

First vary E7+E10 with respect to $`G,U,j,k,P,\mathcal F`$, then restore E3–E4. This exposes the chain rule. The responses below are evaluated algebraic expressions, not unevaluated functional derivatives.

Antisymmetrization has unit weight. A matrix word means $`(GUG)^{ab}=(G^a{}_cU^c{}_dG^d{}_e)g^{eb}`$. The algebraic LOG response to $`G`$ is

```math
\begin{aligned}
K_G^{ab}={}&\tfrac13R^{[a}{}_cG^{c b]}-\tfrac43R^{[a}{}_cU^{c b]}
+\tfrac R3U^{ab}+gN(-2G^{ab}/3-2U^{ab}/3)
+g^2L^2(G^{ab}/12-U^{ab}/6)+\tfrac g6L_{ij}\mathcal F^{abij}\\
&+2G^{ab}(-I/24-J/3+2K/3)
+U^{ab}(-I/3+8J/3-4K/3)\\
&+(G^3)^{ab}/6-(UG^2+GUG+G^2U)^{ab}
+\tfrac43(GU^2+U^2G)^{ab}
+\tfrac{16}3(UGU)^{ab}-\tfrac{16}3(U^3)^{ab}\\
&+2\varepsilon^{cabde}(j_c/48+B_c/12-gP_c/24)G_{de}
-\tfrac16\varepsilon^{cabde}j_cU_{de}.
\end{aligned}\tag{E19}
```

The algebraic response to $`U`$ is

```math
\begin{aligned}
K_U^{ab}={}&-\tfrac43R^{[a}{}_cG^{c b]}+\tfrac R3(G^{ab}-2U^{ab})
+gN(-2G^{ab}/3+4U^{ab})+g^2L^2(-G^{ab}/6-2U^{ab})
+\tfrac{2g}3L_{ij}\mathcal F^{abij}\\
&+2U^{ab}(2I/3-4J/3-4K)
+G^{ab}(-I/3+8J/3-4K/3)\\
&-(G^3)^{ab}+\tfrac43(UG^2+G^2U)^{ab}
+\tfrac{16}3(GUG)^{ab}
-\tfrac{16}3(U^2G+UGU+GU^2)^{ab}\\
&+2\varepsilon^{cabde}(j_c/3+A_c/12-2gP_c/3)U_{de}
-\tfrac16\varepsilon^{cabde}j_cG_{de}.
\end{aligned}\tag{E20}
```

Direct variation rules include

```math
\begin{aligned}
\delta I&=2G^{ab}\delta G_{ab},&
\delta J&=U^{ab}\delta G_{ab}+G^{ab}\delta U_{ab},&
\delta K&=2U^{ab}\delta U_{ab},\\
\delta\mathop{\mathrm{tr}}\nolimits(G^4)&=4\mathop{\mathrm{tr}}\nolimits(G^3\delta G)
=-4(G^3)^{ab}\delta G_{ab},\\
\delta_G\mathop{\mathrm{tr}}\nolimits(G^3U)
&=\mathop{\mathrm{tr}}\nolimits[(UG^2+GUG+G^2U)\delta G]\\
&=-(UG^2+GUG+G^2U)^{ab}\delta G_{ab},\\
\delta A^a&=2\varepsilon^{abcde}G_{de}\delta G_{bc},\qquad
\delta B^a=2\varepsilon^{abcde}U_{de}\delta U_{bc},\\
\delta D_\times^a&=\varepsilon^{abcde}(G_{de}\delta U_{bc}+U_{bc}\delta G_{de})
\end{aligned}\tag{E21}
```

The trace signs follow from reversing antisymmetric two-form indices. E19–E20 were checked by differentiating the polynomial with respect to each independent symbolic two-form component, leaving the Ricci components symbolic.

The derivative response and complete flux responses are

```math
\begin{gathered}
w_a:=-j_a/3+A_a/48+B_a/3-D_{\times a}/6+gP_a/3,\\
\mathcal K_G^{ab}:=-LG^{ab}+\alpha\big(K_G^{ab}+\nabla^{[a}w^{b]}\big),\\
\mathcal K_U^{ab}:=8LU^{ab}+\alpha\big(K_U^{ab}-\tfrac43\nabla_c k^{cab}\big),\\
\Pi^{ab}:=2\mathcal K_G^{ab},\qquad
Q^{abc}:=-\tfrac12\varepsilon^{deabc}\mathcal K_{Ude},\\
W_a:=-4P_a/L-2\sqrt2V_a-4gC_a
+\alpha(2g^2P_a/3+gj_a/3-gA_a/24-2gB_a/3),\\
J_C^a:=-4gP^a-\tfrac\alpha{12}\varepsilon^{abcde}\mathcal F_{bc}^{ij}\mathcal F_{deij}
\end{gathered}\tag{E22}
```

Integrating derivatives off the variations gives

```math
\begin{aligned}
w_a\delta j^a&=w_a\nabla_b\delta G^{ab}
\simeq_\partial-(\nabla_bw_a)\delta G^{ab}
=\nabla^{[a}w^{b]}\delta G_{ab},\\
\tfrac49k^{abc}\delta k_{abc}
&=\tfrac43k^{abc}\nabla_a\delta U_{bc}
\simeq_\partial-\tfrac43\nabla_ak^{abc}\delta U_{bc},\\
\mathcal K_U^{ab}\delta U_{ab}
&=-\tfrac1{12}\mathcal K_{Uab}\varepsilon^{abcde}\delta H_{cde}
=\tfrac16Q^{cde}\delta H_{cde}
\end{aligned}\tag{E23}
```

The form variation is consequently

```math
\delta\ell_0\simeq_\partial
\tfrac12\Pi^{\mu\nu}\delta G_{\mu\nu}
+\tfrac16Q^{\mu\nu\rho}\delta H_{\mu\nu\rho}
+W_\mu\delta P^\mu+J_C^\mu\delta C_\mu+\cdots
\tag{E24}
```

with all coefficients specified above.

## Vector and form equations

The Chern–Simons mixing is retained in the field-strength variation:

```math
\begin{aligned}
\delta G&=d\delta C,\\
\delta H&=d\delta B+\tfrac12\delta C\wedge G
+\tfrac12C\wedge d\delta C+\tfrac g2\delta E_3\\
&=d(\delta B-\tfrac12C\wedge\delta C)
+\delta C\wedge G+\tfrac g2\delta E_3,\\
\delta P^\mu\big|_{\delta e=0}
&=-\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu\delta E_{\rho\sigma\lambda}.
\end{aligned}\tag{E25}
```

Use the normalization $`\delta S=(2\kappa_5^2)^{-1}\int e(\mathcal E_C\delta C+\mathcal E_B\delta B/2+\mathcal E_E\delta E_3/6+\cdots)`$. Then

```math
\begin{aligned}
\tfrac16Q^{\mu\nu\rho}\,3\nabla_\mu\delta B_{\nu\rho}
&\simeq_\partial-\tfrac12\nabla_\mu Q^{\mu\nu\rho}\delta B_{\nu\rho},\\
\tfrac16Q^{\mu\nu\rho}\,3\delta C_{[\mu}G_{\nu\rho]}
&=\tfrac12Q^{\mu\nu\rho}G_{\nu\rho}\delta C_\mu,\\
-\tfrac1{12}W_\mu\varepsilon^{\mu\nu\rho\sigma\lambda}\nabla_\nu\delta E_{\rho\sigma\lambda}
&\simeq_\partial\tfrac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu W_\mu\,\delta E_{\rho\sigma\lambda}
\end{aligned}\tag{E26}
```

The resulting equations are

```math
\boxed{\begin{aligned}
0=\mathcal E_B^{\nu\rho}&=-\nabla_\mu Q^{\mu\nu\rho},\\
0=\mathcal E_C^\nu&=J_C^\nu-\nabla_\mu\Pi^{\mu\nu}
+\tfrac12Q^{\nu\mu\rho}G_{\mu\rho}
-\tfrac12C_\mu\mathcal E_B^{\mu\nu},\\
0=\mathcal E_E^{\rho\sigma\lambda}
&=\tfrac g2Q^{\rho\sigma\lambda}
+\tfrac12\varepsilon^{\mu\nu\rho\sigma\lambda}\nabla_\nu W_\mu.
\end{aligned}}\quad
\substack{U_{ab}=-\varepsilon_{abcde}H^{cde}/12,\\
H=dB+C\wedge dC/2+gE_3/2,\quad P^\mu=-\varepsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}/12.}
\tag{E27}
```

The term $`-C\mathcal E_B/2`$ in $`\mathcal E_C`$ comes from resolving the combined variation $`\delta B-C\wedge\delta C/2`$ into independent variations. It is not dropped using another equation.

Without using the equations of motion, their differential identities are

```math
\nabla_\nu\mathcal E_C^\nu+\tfrac14G_{\mu\nu}\mathcal E_B^{\mu\nu}=0,
\qquad
\nabla_\rho\mathcal E_E^{\rho\mu\nu}+\tfrac g2\mathcal E_B^{\mu\nu}=0
\tag{E28}
```

The first uses $`dG=0`$, $`\nabla\cdot P=0`$, and $`D\mathcal F=0`$; the second uses antisymmetric epsilon to cancel two derivatives. These are gauge identities, not a field truncation.

## Internal-connection equations

Define $`\delta\ell_0|_{\delta\mathcal F}=M^{\mu\nu}_{ij}\delta\mathcal F_{\mu\nu}^{ij}/2`$. The response is

```math
M^{\mu\nu}_{ij}:=\alpha\left[
\tfrac23\mathcal F^{\mu\nu}_{ij}+\tfrac g3L_{ij}G^{\mu\nu}
+\tfrac{4g}3L_{ij}U^{\mu\nu}
-\tfrac13\varepsilon^{\lambda\mu\nu\rho\sigma}C_\lambda\mathcal F_{\rho\sigma ij}
\right].\tag{E29}
```

Varying the two equal field-strength factors produces the factor two in the Chern–Simons coefficient. Here $`D`$ contains only Levi–Civita and the internal connection. Since $`\delta\mathcal F_{\mu\nu}^{ij}=2D_{[\mu}\delta V_{\nu]}^{ij}`$,

```math
\begin{aligned}
\tfrac12M^{\mu\nu}_{ij}\delta\mathcal F_{\mu\nu}^{ij}
&=M^{\mu\nu}_{ij}D_\mu\delta V_\nu^{ij}
\simeq_\partial-D_\mu M^{\mu\nu}_{ij}\delta V_\nu^{ij},\\
\delta\big[(2L-\alpha g^2L^2/2)V'^2-2\sqrt2P^\mu V_\mu\big]
&=\big[(4L-\alpha g^2L^2)V'{}^\nu_{ij}
-2\sqrt2P^\nu\delta_{ij}\big]\delta V_\nu^{ij}.
\end{aligned}\tag{E30}
```

The independent trace and traceless equations are therefore

```math
\begin{gathered}
\mathcal V^\nu_{ij}:=
-D_\mu M^{\mu\nu}_{ij}+(4L-\alpha g^2L^2)V'{}^\nu_{ij}
-2\sqrt2P^\nu\delta_{ij},\\
\boxed{\mathcal E_V^\nu=\tfrac12\delta^{ij}\mathcal V^\nu_{ij}=0,\qquad
\mathcal E_{V'}^{\nu}{}_{ij}=
(\delta_{(i}^{k}\delta_{j)}^l-\tfrac12\delta_{ij}\delta^{kl})
\mathcal V^\nu_{kl}=0,}\qquad
U_{ab}=-\tfrac1{12}\varepsilon_{abcde}H^{cde}.
\end{gathered}\tag{E31}
```

The derivative of $`\mathcal F`$ inside $`M`$ remains present. The two-derivative connection equations have not been imported as algebraic constraints on the total theory.

## Vielbein equation

On the bosonic body the local Lorentz identity permits use of the symmetric metric equation, followed by the vielbein chain rule. Set $`h^{\mu\nu}=\delta g^{\mu\nu}`$ and $`h=g_{\mu\nu}h^{\mu\nu}`$; these are test variations, not a background choice.

### Variation of dependent geometry

Convert all tangent indices in the preceding responses with the common vielbein. Vary $`g^{\mu\nu}`$, not the fixed tangent metric $`\eta^{ab}`$.

```math
\begin{aligned}
\delta e&=-\tfrac12eh,\qquad \delta g_{\mu\nu}=-h_{\mu\nu},\\
\delta\Gamma^\rho_{\mu\nu}
&=-\tfrac12(\nabla_\mu h_\nu{}^\rho+\nabla_\nu h_\mu{}^\rho-\nabla^\rho h_{\mu\nu}),\\
\delta R_{\mu\nu}
&=\nabla_\rho\delta\Gamma^\rho_{\nu\mu}-\nabla_\nu\delta\Gamma^\rho_{\rho\mu},\\
\delta j^\lambda\big|_{\delta G_{\mu\nu}=0}
&=\nabla_\rho(h^{\lambda\sigma}G_\sigma{}^\rho+h^{\rho\sigma}G^\lambda{}_\sigma)-\tfrac12G^{\lambda\sigma}\nabla_\sigma h,\\
\delta U_{\mu\nu}\big|_{\delta H_{\rho\sigma\lambda}=0}
&=-\tfrac12hU_{\mu\nu}-\tfrac14\varepsilon_{\mu\nu\rho\sigma\lambda}h^{\rho\kappa}H_\kappa{}^{\sigma\lambda},\\
\delta P^\mu\big|_{\delta E_3=0}&=\tfrac12hP^\mu.
\end{aligned}\tag{E32}
```

The last two lines of E32 follow from $`\delta\varepsilon_{\mu\nu\rho\sigma\lambda}=-h\varepsilon_{\mu\nu\rho\sigma\lambda}/2`$, $`\delta\varepsilon^{\mu\nu\rho\sigma\lambda}=h\varepsilon^{\mu\nu\rho\sigma\lambda}/2`$, and the three inverse metrics in $`H^{\rho\sigma\lambda}`$. Both contributions are needed for the three-form and current stress tensors.

The response to the Ricci tensor in E7+E10 is

```math
\begin{aligned}
Z^{\mu\nu}:={}&Lg^{\mu\nu}+\alpha\Big[-\tfrac13R^{\mu\nu}+\tfrac1{12}Rg^{\mu\nu}
+\tfrac16G^{\mu\rho}G^\nu{}_\rho-\tfrac43G^{(\mu|\rho|}U^{\nu)}{}_\rho\\
&\hspace{7em}+g^{\mu\nu}(gN/6-g^2L^2/12+J/3-K/3)\Big]
\end{aligned}\tag{E33}
```

Two integrations by parts in $`Z^{\mu\nu}\delta R_{\mu\nu}`$, without changing derivative order, give

```math
Z^{\mu\nu}\delta R_{\mu\nu}\simeq_\partial
\mathscr P_{\mu\nu}[Z]h^{\mu\nu},\qquad
\mathscr P_{\mu\nu}[Z]
=\tfrac12\Box Z_{\mu\nu}+\tfrac12g_{\mu\nu}\nabla_\rho\nabla_\sigma Z^{\rho\sigma}
-\nabla_\rho\nabla_{(\mu}Z_{\nu)}{}^\rho.
\tag{E34}
```

For $`Z^{\mu\nu}=Lg^{\mu\nu}`$, E34 reduces to $`g_{\mu\nu}\Box L-\nabla_\mu\nabla_\nu L`$, the dependent-connection contribution of the Einstein term.

### Algebraic metric contributions

Write $`\ell=\ell_{2\partial,0}^{(E7)}+\alpha\ell_{\log,0}^{(E10)}`$ and define

```math
\mathsf G^{\mu\nu}:=-LG^{\mu\nu}+\alpha K_G^{\mu\nu},\quad
\mathsf U^{\mu\nu}:=8LU^{\mu\nu}+\alpha K_U^{\mu\nu},\quad
c_L:=L^{-1}-\alpha g^2/4
\tag{E35}
```

These algebraic responses hold $`j,k`$ fixed and differ from the derivative-completed responses $`\mathcal K`$ in E22.

The algebraic metric response is

```math
\begin{aligned}
\mathscr A_{\mu\nu}:={}&
Z_{(\mu}{}^\rho R_{\nu)\rho}
+\mathsf G_{(\mu}{}^\rho G_{\nu)\rho}
+\mathsf U_{(\mu}{}^\rho U_{\nu)\rho}
+\tfrac12M_{(\mu}{}^{\rho}{}_{ij}\mathcal F_{\nu)\rho}^{ij}\\
&+\tfrac{2\alpha}3k_{\mu\rho\sigma}k_\nu{}^{\rho\sigma}
-\tfrac12W_{(\mu}P_{\nu)}-\tfrac\alpha2w_{(\mu}j_{\nu)}
+\tfrac12J_{C(\mu}C_{\nu)}\\
&+\tfrac12(4L-\alpha g^2L^2)V'_\mu{}^{ij}V'_{\nu ij}
-\sqrt2P_{(\mu}V_{\nu)}+c_L\partial_\mu L\partial_\nu L.
\end{aligned}\tag{E36}
```

For a covariant rank-$`r`$ tensor with variation coefficient $`p^{a_1\ldots a_r}`$, each lower index contributes $`p_{(\mu}{}^{\cdots}X_{\nu)\cdots}/2`$; upper indices contribute with the opposite sign. This follows from invariance under a local basis change. Rank two for $`G,U,\mathcal F`$, rank three for $`k`$, and upper rank one for $`P,j`$ reproduce E36. Epsilon's metric dependence is included rather than treating it as a fixed coordinate tensor.

### Metric dependence of currents and duality

Multiply the $`j`$ variation in E32 by $`\alpha w_a`$ and integrate derivatives off $`h`$:

```math
\begin{aligned}
\mathscr J_{\mu\nu}:={}&
(\nabla_{(\mu}w_\rho-\nabla_\rho w_{(\mu})G_{\nu)}{}^\rho
+\tfrac12g_{\mu\nu}\nabla_\rho(w_\lambda G^{\lambda\rho}),\\
\mathscr U_{\mu\nu}:={}&
-\tfrac12g_{\mu\nu}\mathcal K_U^{\rho\sigma}U_{\rho\sigma}
-\tfrac14\mathcal K_U^{\rho\sigma}\varepsilon_{\rho\sigma(\mu|\lambda\kappa|}H_{\nu)}{}^{\lambda\kappa},\\
\mathscr T^P_{\mu\nu}:={}&\tfrac12g_{\mu\nu}W_\rho P^\rho
\end{aligned}\tag{E37}
```

Because $`k=dU`$, its connection variations cancel in the exterior derivative. The remaining $`\delta U`$ in E37 multiplies the full derivative-completed $`\mathcal K_U`$.

The independent vielbein equation is

```math
\boxed{\begin{aligned}
0=\mathcal E_{\mu\nu}
&=\left[\mathscr A_{\mu\nu}-\tfrac12g_{\mu\nu}\ell
+\mathscr P_{\mu\nu}[Z]+\alpha\mathscr J_{\mu\nu}
+\mathscr U_{\mu\nu}+\mathscr T^P_{\mu\nu}\right]_{U_{\rho\sigma}=-\varepsilon_{\rho\sigma\lambda\kappa\tau}H^{\lambda\kappa\tau}/12},\\
0=\mathcal E_e{}^\rho{}_a
&=-2e_{\nu a}\mathcal E^{\rho\nu}.
\end{aligned}}\tag{E38}
```

E38 retains all curvature, derivative-flux, three-form, and internal-connection mixing. There are no spurious independent equations for $`\omega(e)`$ or $`f(e)`$. The second line is the chain rule $`\delta g^{\mu\nu}=-(g^{\mu\rho}e_a{}^\nu+g^{\nu\rho}e_a{}^\mu)\delta e_\rho{}^a`$.

Its two-derivative coefficient expands as

```math
\begin{aligned}
\mathcal E_{\mu\nu}^{2\partial}={}&
L(R_{\mu\nu}-\tfrac12g_{\mu\nu}R)+(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)L\\
&-LG_{\mu\rho}G_\nu{}^\rho+\tfrac L4g_{\mu\nu}G^2
-LH_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}+\tfrac L6g_{\mu\nu}H^2\\
&+L^{-1}\partial_\mu L\partial_\nu L-\tfrac1{2L}g_{\mu\nu}(\partial L)^2
+2LV'_\mu{}^{ij}V'_{\nu ij}-Lg_{\mu\nu}V'^2\\
&+\tfrac2L P_\mu P_\nu-\tfrac1L g_{\mu\nu}P^2
+g_{\mu\nu}(N^2/L+gLN+2gN+g^2L^3/4-g^2L^2)
\end{aligned}\tag{E39}
```

This checks the coefficient independent of $`\alpha`$; it does not set the total theory's coupling to zero. The metric variations of the $`C\cdot P`$ and $`V\cdot P`$ densities cancel because they contain the epsilon density.

## Grassmann signs in fermionic variation

The variation $`\delta`$ is even; the variations of fermions are odd. The Majorana bar is linear:

```math
\delta\bar u=\overline{\delta u},\qquad
\overline{iu}=i\bar u,\qquad
\delta(\bar u\Gamma v)=\overline{\delta u}\Gamma v+\bar u\Gamma\delta v.
\tag{E40}
```

The Leibniz rule itself introduces no minus sign. A sign arises when an odd test variation passes another odd factor. In components,

```math
\begin{aligned}
\delta(c_{AB}u^Av^B)
&=c_{AB}\delta u^Av^B+c_{AB}u^A\delta v^B\\
&=\delta u^A c_{AB}v^B-\delta v^B c_{AB}u^A.
\end{aligned}\tag{E41}
```

For ordered ordinary covariant derivatives,

```math
\int e\,X\nabla_{\mu_1}\cdots\nabla_{\mu_r}\delta u
\simeq_\partial
(-1)^r\int e\,(\nabla_{\mu_r}\cdots\nabla_{\mu_1}X)\delta u.
\tag{E42}
```

The derivative order reverses and is not restored without a commutator. E42 applies to contracted Lorentz/internal ordinary derivatives. No assumption $`\mathcal D^\dagger=-\mathcal D`$ is made for the full supercovariant derivative.

## Fermionic variations of dependent connections and composites

Keep the bosonic fields arbitrary and define test spinors $`\xi_\mu^i=\delta\psi_\mu^i`$, $`\zeta^i=\delta\varphi^i`$. They are not new physical fields.

### One-fermion connection operators

Here $`\nabla`$ contains the bosonic spin connection and full $`V_\mu^{ij}`$. The explicit linear operators are

```math
\begin{aligned}
\mathscr R'_{\mu\nu}{}^i[\xi]
&:=2\nabla_{[\mu}\xi_{\nu]}^i+2i\gamma\!\cdot T_0\gamma_{[\mu}\xi_{\nu]}^i,\qquad
T_{0ab}=\tfrac18(G_{ab}+\tfrac16\varepsilon_{abcde}H^{cde}),\\
\Phi_\mu^i[\xi]
&:=\tfrac i3\gamma^a\mathscr R'_{\mu a}{}^i[\xi]
-\tfrac i{24}\gamma_\mu\gamma^{ab}\mathscr R'_{ab}{}^i[\xi],\\
\mathscr R_{\mu\nu}{}^i[\xi]
&:=\mathscr R'_{\mu\nu}{}^i[\xi]-2i\gamma_{[\mu}\Phi_{\nu]}^i[\xi],\\
s_a^i[\xi]
&:=\tfrac18\gamma^{bc}(G_{bc}-\tfrac16\varepsilon_{bcdef}H^{def})\xi_a^i
-\tfrac g2L^{ij}\xi_{aj}-\Phi_a^i[\xi],\\
\Xi^i[\xi,\zeta]&:=\tfrac i8\gamma^as_a^i[\xi]+\tfrac g8\zeta^i
\end{aligned}\tag{E43}
```

They respectively give the one-fermion variations of $`R'(Q),\phi,R(Q),\mathcal D_a\psi_{\mathrm{dilatino}},\chi`$. The quantity $`s_a`$ is not an independent dilatino equation.

With $`A_b=\gamma^a\mathscr R'_{ab}`$ and $`B=\gamma^{ab}\mathscr R'_{ab}`$,

```math
\begin{aligned}
\Phi_b&=-iA_b/3-i\gamma_bB/24,\qquad \gamma^b\Phi_b=iB/8,\\
\gamma^a\mathscr R_{ab}
&=A_b-3i\Phi_b-i\gamma_b\gamma^a\Phi_a
=A_b-A_b-\gamma_bB/8+\gamma_bB/8=0.
\end{aligned}\tag{E44}
```

Thus variation of the dependent $`S`$ connection preserves the gamma-trace constraint. Holding that connection artificially fixed would be incorrect.

The one-fermion variation of the full derivative of the linear-multiplet fermion is

```math
\begin{aligned}
v_a^i[\xi,\zeta]:={}&\nabla_a\zeta^i
+\tfrac i2\gamma^b(\nabla_bL^{ij})\xi_{aj}
+\tfrac i2\not P\,\xi_a^i-\tfrac12N\xi_a^i\\
&+\gamma\!\cdot T_0L^{ij}\xi_{aj}-3L^{ij}\Phi_{aj}[\xi]
\end{aligned}\tag{E45}
```

Here $`\nabla_bL^{ij}`$ includes the $`V'`$ term in E6.

### Two-fermion objects

At fixed vielbein, the spin-connection variation is

```math
\delta\omega_\mu{}^{ab}=
\tfrac12\big(\bar\xi^{[a}\gamma^{b]}\psi_\mu+\bar\psi^{[a}\gamma^{b]}\xi_\mu\big)
+\tfrac14\big(\bar\xi^a\gamma_\mu\psi^b+\bar\psi^a\gamma_\mu\xi^b\big)
\tag{E46}
```

and hence

```math
\delta R_{\mu\nu}{}^{ab}(\omega)=2\nabla_{[\mu}\delta\omega_{\nu]}{}^{ab}
\tag{E47}
```

This term contributes to the gravitino equation. E47–E52 are linear in the physical fermions other than the test spinor, as required for the Euler coefficient of a two-fermion action. The derivative on the right uses the bosonic spin connection.

For hatted fluxes and the linear-multiplet current,

```math
\begin{aligned}
\delta\widehat G_{\mu\nu}
&=\tfrac i2(\bar\xi_{[\mu}\psi_{\nu]}+\bar\psi_{[\mu}\xi_{\nu]}),\\
\delta\widehat H_{\mu\nu\rho}
&=-\tfrac34(\bar\xi_{[\mu}\gamma_\nu\psi_{\rho]}+\bar\psi_{[\mu}\gamma_\nu\xi_{\rho]}),\\
\delta E^a
&=-\tfrac i2(\bar\xi_b\gamma^{ba}\varphi+\bar\psi_b\gamma^{ba}\zeta)
-\tfrac14L_{ij}(\bar\xi_b^i\gamma^{abc}\psi_c^j+\bar\psi_b^i\gamma^{abc}\xi_c^j),\\
\delta T_{ab}
&=\tfrac18\left(\delta\widehat G_{ab}+\tfrac16\varepsilon_{abcde}\delta\widehat H^{cde}\right),\\
\delta(\mathcal D_aL^{ij})
&=-i(\bar\xi_a^{(i}\varphi^{j)}+\bar\psi_a^{(i}\zeta^{j)}).
\end{aligned}\tag{E48}
```

Ordinary $`P^\mu`$ is fermion independent: $`\delta_FP^\mu=0`$, whereas $`\delta_FE^a\ne0`$.

Preserving factor order, the primed Lorentz curvature varies as

```math
\begin{aligned}
\delta\widehat R'_{\mu\nu}{}^{ab}(M)={}&2\nabla_{[\mu}\delta\omega_{\nu]}{}^{ab}\\
&+i\overline{\Phi_{[\mu}[\xi]}\gamma^{ab}\psi_{\nu]}
+i\bar\phi_{[\mu}\gamma^{ab}\xi_{\nu]}\\
&+i\bar\xi_{[\mu}\gamma^{[a}\gamma\!\cdot T_0\gamma^{b]}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot T_0\gamma^{b]}\xi_{\nu]}\\
&+\bar\xi_{[\mu}\gamma^{[a}\mathscr R_{\nu]}{}^{b]}[\psi]
+\bar\psi_{[\mu}\gamma^{[a}\mathscr R_{\nu]}{}^{b]}[\xi]\\
&+\tfrac12\bar\xi_{[\mu}\gamma_{\nu]}\mathscr R^{ab}[\psi]
+\tfrac12\bar\psi_{[\mu}\gamma_{\nu]}\mathscr R^{ab}[\xi]\\
&+8\bar\xi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\Xi[\xi,\zeta]
\end{aligned}\tag{E49}
```

where $`\phi=\Phi[\psi]`$ and $`\chi=\Xi[\psi,\varphi]`$ are their one-fermion values. The dependent $`K`$ connection and full Lorentz curvature contribute

```math
\begin{aligned}
\delta\mathcal R_{\mu\nu}
&=\delta\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},\\
\delta f_\mu{}^a&=-\tfrac16\delta\mathcal R_\mu{}^a+\tfrac1{48}e_\mu{}^a\delta\mathcal R,\\
\delta\widehat R_{\mu\nu}{}^{ab}(M)
&=\delta\widehat R'_{\mu\nu}{}^{ab}(M)+8\delta f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
\end{aligned}\tag{E50}
```

Neither $`\delta\mathcal R_{\mu\nu}`$ nor $`\delta f_{\mu\nu}`$ is assumed symmetric in this fermionic calculation.

The internal curvature varies as

```math
\begin{aligned}
\delta\widehat R_{\mu\nu}^{ij}(V)={}&
-3i\left(\overline{\Phi_{[\mu}^{(i}[\xi]}\psi_{\nu]}^{j)}
+\bar\phi_{[\mu}^{(i}\xi_{\nu]}^{j)}\right)\\
&-8\left(\bar\xi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
+\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\Xi^{j)}[\xi,\zeta]\right)\\
&-i\left(\bar\xi_{[\mu}^{(i}\gamma\!\cdot T_0\psi_{\nu]}^{j)}
+\bar\psi_{[\mu}^{(i}\gamma\!\cdot T_0\xi_{\nu]}^{j)}\right)
\end{aligned}\tag{E51}
```

The variation of the scalar composite $`D`$ includes a nonzero $`\delta\Box^c\sigma`$:

```math
\begin{aligned}
\delta\Box^c\sigma={}&2\delta f_a{}^a
-\tfrac i2\left(\bar\xi_as^a[\psi]+\bar\psi_as^a[\xi]\right)
-2\left(\bar\xi_a\gamma^a\chi+\bar\psi_a\gamma^a\Xi[\xi,\zeta]\right),\\
\delta D={}&\tfrac14\delta\Box^c\sigma
+\tfrac5{48}G^{ab}\delta\widehat G_{ab}
-\tfrac1{288}\varepsilon_{abcde}\left(H^{cde}\delta\widehat G^{ab}
+G^{ab}\delta\widehat H^{cde}\right)
+\tfrac{13}{144}H^{abc}\delta\widehat H_{abc}.
\end{aligned}\tag{E52}
```

E43–E52 determine the dependent-connection and composite contributions. Varying only explicit bilinears would miss them.

## Diagonal linear-multiplet fermion block

This section computes one diagonal coefficient block of the full quadratic form. It does not remove the gravitino or discard mixed terms. Setting this operator alone to zero is not the full fermion equation.

### Collection of two-derivative coefficients

Temporarily define $`\mathcal B_0=L_{ij}\bar\varphi^i\varphi^j`$, $`\mathcal B_P=L_{ij}\bar\varphi^i\not P\varphi^j`$, and $`\mathcal A=L^{lm}\bar\varphi^j\gamma^a(\nabla_aL_{jl})\varphi_m`$. The pure $`\varphi\varphi`$ part of the triplet contraction is

```math
\left.L^{ij}Y_{ij}\right|_{\varphi\varphi}
=-\frac{2iN}{L^3}\mathcal B_0+\frac2{L^3}\mathcal B_P
+\frac1L\bar\varphi\not\nabla\varphi
-\frac1{L^3}\mathcal A+\frac{2i}L\bar\varphi\gamma\!\cdot T_0\varphi.
\tag{E53}
```

The two $`\chi\varphi`$ terms cancel as $`-16iL^{-1}L^{ij}\bar\chi_i\varphi_j+16iL^{-3}L^2L_{ij}\bar\chi^i\varphi^j=0`$. Keeping the $`\lambda,\rho,F`$ contributions separate,

```math
\begin{array}{c|ccccc}
\text{contribution}&\bar\varphi\not\nabla\varphi&\bar\varphi\gamma\!\cdot T_0\varphi&\mathcal B_0&\mathcal B_P&\mathcal A\\ \hline
-2L^{ij}Y_{ij}&-2/L&-4i/L&4iN/L^3&-4/L^3&2/L^3\\
-2i\bar\lambda\varphi\ (\bmod\ \partial)&4/L&8i/L&4ig/L-4iN/L^3&4/L^3&-4/L^3\\
-2\rho_{[2]}N&0&0&-2iN/L^3&0&0\\
-F_{[2]\mu\nu}E^{\mu\nu}\ (\bmod\ \partial)&0&0&0&2/L^3&0
\end{array}\tag{E54}
```

For the last line use

```math
2E^{\mu\nu}\nabla_\mu(L^{-3}L_{ij}\bar\varphi^i\gamma_\nu\varphi^j)
\simeq_\partial 2P^\nu L^{-3}L_{ij}\bar\varphi^i\gamma_\nu\varphi^j
\tag{E55}
```

The sign $`\nabla_\mu E^{\mu\nu}=-P^\nu`$ is essential in E55.

The internal contraction and the symmetric fixed-upper rank-one bilinear imply

```math
\mathcal A=L^2 V'_{aij}\bar\varphi^i\gamma^a\varphi^j,
\qquad
\bar\varphi\not\nabla\varphi
=\bar\varphi\not\nabla^{\circ}\varphi
+V'_{aij}\bar\varphi^i\gamma^a\varphi^j
\tag{E56}
```

where

```math
\nabla_\mu^{\circ}\varphi^i
:=\left(\partial_\mu+\tfrac14\omega_\mu{}^{ab}(e)\gamma_{ab}\right)\varphi^i
-\tfrac12\delta^{ij}V_\mu\varphi_j
\tag{E57}
```

contains only the residual trace connection. This is the algebraic cancellation of $`V'`$ terms in E54, not an additional gauge choice. The sum is

```math
\begin{aligned}
\ell_{2\partial,\varphi\varphi}\simeq_\partial{}&
\frac2L\bar\varphi\not\nabla^{\circ}\varphi
+\frac{i}{2L}(G_{ab}-2U_{ab})\bar\varphi\gamma^{ab}\varphi\\
&+\left(\frac{4ig}{L}-\frac{2iN}{L^3}\right)L_{ij}\bar\varphi^i\varphi^j
+\frac2{L^3}L_{ij}\bar\varphi^i\not P\varphi^j.
\end{aligned}\tag{E58}
```

### LOG coefficients and current contribution

The active LOG polynomial contributes one pure $`\varphi\varphi`$ triplet term, three scalar terms, and one vector term. Every implicit two-fermion connection correction in this block contains at least one gravitino; Q/S derivative corrections multiply $`\psi_\mu`$ or $`\Phi_\mu[\psi]`$. Thus no hidden pure $`\varphi\varphi`$ term is lost. The five contributions sum to

```math
\begin{aligned}
\ell_{\log,\varphi\varphi}={}&
\tfrac{g^2}6\bar\varphi\not\nabla\varphi
-\tfrac{3ig^2}8G_{ab}\bar\varphi\gamma^{ab}\varphi
+\tfrac{3ig^2}4U_{ab}\bar\varphi\gamma^{ab}\varphi\\
&-\tfrac{17ig^3}{12}L_{ij}\bar\varphi^i\varphi^j
+\tfrac{5ig^2}6C_a\bar\varphi\gamma^{ab}\nabla_b\varphi.
\end{aligned}\tag{E59}
```

The last term must remain. The contracted rank-two Majorana flip has sign $`-t_2=+1`$, so

```math
\begin{aligned}
\nabla_b(\bar\varphi\gamma^{ab}\varphi)
&=\overline{\nabla_b\varphi}\gamma^{ab}\varphi
+\bar\varphi\gamma^{ab}\nabla_b\varphi
=2\bar\varphi\gamma^{ab}\nabla_b\varphi,\\
\tfrac{5ig^2}6C_a\bar\varphi\gamma^{ab}\nabla_b\varphi
&=\tfrac{5ig^2}{12}\nabla_b(C_a\bar\varphi\gamma^{ab}\varphi)
-\tfrac{5ig^2}{12}(\nabla_bC_a)\bar\varphi\gamma^{ab}\varphi\\
&\simeq_\partial\tfrac{5ig^2}{24}G_{ab}\bar\varphi\gamma^{ab}\varphi,\\
-\tfrac38+\tfrac5{24}&=-\tfrac16.
\end{aligned}\tag{E60}
```

and therefore

```math
\ell_{\log,\varphi\varphi}\simeq_\partial
\tfrac{g^2}6\bar\varphi\not\nabla\varphi
+ig^2(-G_{ab}/6+3U_{ab}/4)\bar\varphi\gamma^{ab}\varphi
-\tfrac{17ig^3}{12}L_{ij}\bar\varphi^i\varphi^j.
\tag{E61}
```

### Diagonal Euler operator

Combining the Grassmann flip with E42 for variable $`a(x)`$ gives

```math
\begin{aligned}
\delta\int e\,a\bar\varphi\not\nabla\varphi
&=\int e\,\big[a\delta\bar\varphi\not\nabla\varphi
-a\overline{\nabla\delta\varphi}\gamma\varphi\big]\\
&\simeq_\partial\int e\,\delta\bar\varphi
\big(2a\not\nabla\varphi+\not\partial a\,\varphi\big)
\end{aligned}\tag{E62}
```

The two endpoint variations of algebraic rank-two contracted bilinears and symmetric $`L_{ij}`$ rank-zero/one bilinears are equal and double their coefficients. Varying E58 and E61 and restoring the three-form gives

```math
\boxed{\begin{aligned}
(\mathcal K_{\varphi\varphi}\varphi)_i={}&
\frac4L\not\nabla^{\circ}\varphi_i
-\frac2{L^2}\not\partial L\,\varphi_i
+\frac iL\gamma^{ab}\left(G_{ab}+\tfrac16\varepsilon_{abcde}H^{cde}\right)\varphi_i\\
&+\left(\frac{8ig}{L}-\frac{4iN}{L^3}\right)L_{ij}\varphi^j
+\frac4{L^3}L_{ij}\not P\varphi^j\\
&+\alpha\left[
\frac{g^2}3\not\nabla\varphi_i
-\frac{ig^2}3G_{ab}\gamma^{ab}\varphi_i
-\frac{ig^2}8\varepsilon_{abcde}H^{cde}\gamma^{ab}\varphi_i
-\frac{17ig^3}6L_{ij}\varphi^j\right].
\end{aligned}}\tag{E63}
```

In E63, $`\nabla`$ contains full $`V^{ij}`$, whereas $`\nabla^\circ`$ contains only its trace. The two-derivative cancellation of $`V'`$ does not extend to the LOG kinetic term. E63 is the diagonal contribution; the full coupled equation has the block structure E69, including $`\mathcal K_{\varphi\psi}\psi`$.

## Background restriction and linearization

Only now, after variation, impose the zero-fermion background:

```math
\bar\psi_\mu^i=0,\qquad\bar\varphi^i=0.
\tag{E64}
```

The bosonic background remains arbitrary: no constant scalars, Einstein metric, or zero flux is assumed yet. Its required equations are

```math
\boxed{
\mathcal E_e[\bar\Phi_B]=\mathcal E_C[\bar\Phi_B]
=\mathcal E_B[\bar\Phi_B]=\mathcal E_E[\bar\Phi_B]
=\mathcal E_L[\bar\Phi_B]=\mathcal E_N[\bar\Phi_B]
=\mathcal E_V[\bar\Phi_B]=\mathcal E_{V'}[\bar\Phi_B]=0,
}\tag{E65}
```

Each Euler coefficient is the explicit E16, E18, E27, E31, or E38 expression. Even fermion parity makes the background fermion equations vanish, without making their linearized equations vanish.

Define perturbations $`a_\mu=\delta C_\mu`$, $`b_{\mu\nu}=\delta B_{\mu\nu}`$, $`u_{\mu\nu\rho}=\delta E_{\mu\nu\rho}`$, $`l=\delta L`$, $`n=\delta N`$, $`v_\mu^{ij}=\delta V_\mu^{ij}`$, and $`h^{\mu\nu}=\delta g^{\mu\nu}`$. Alongside E25 and E32, the identities

```math
\begin{aligned}
\delta\mathcal F_{\mu\nu}^{ij}&=2\bar D_{[\mu}v_{\nu]}^{ij},\\
\delta P^\mu&=-\tfrac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\bar\nabla_\nu u_{\rho\sigma\lambda}+\tfrac12h\bar P^\mu,\\
\delta U_{\mu\nu}&=-\tfrac1{12}\bar\varepsilon_{\mu\nu\rho\sigma\lambda}
\bar g^{\rho\alpha}\bar g^{\sigma\beta}\bar g^{\lambda\gamma}\delta H_{\alpha\beta\gamma}
-\tfrac12h\bar U_{\mu\nu}-\tfrac14\bar\varepsilon_{\mu\nu\rho\sigma\lambda}h^{\rho\kappa}\bar H_\kappa{}^{\sigma\lambda},\\
\delta\Box L&=\bar\Box l+h^{\mu\nu}\bar\nabla_\mu\bar\nabla_\nu\bar L
-\bar g^{\mu\nu}\delta\Gamma^\rho_{\mu\nu}\partial_\rho\bar L
\end{aligned}\tag{E66}
```

fix the basic dependencies needed for bosonic linearization. Here $`h^{\mu\nu}`$ is an inverse-metric perturbation; the covariant-metric perturbation is $`-h_{\mu\nu}`$.

For example, the $`N`$ equation linearizes to

```math
\begin{aligned}
0=\delta\mathcal E_N={}&
-\left(\frac4{\bar L}+\frac{\alpha g^2}3\right)n
+\left(\frac{4\bar N}{\bar L^2}-2g+\frac{4\alpha g^3}3\bar L\right)l\\
&+\frac{\alpha g}6\delta R
-\frac{\alpha g}3\delta(G_{ab}G^{ab})
+\frac{\alpha g}{18}\delta(G^{ab}\varepsilon_{abcde}H^{cde})
-\frac{\alpha g}6\delta(H_{abc}H^{abc})
\end{aligned}\tag{E67}
```

The last three variations follow the algebraic product rules E21/E66, including epsilon and inverse-metric variations. All $`N`$–metric–scalar–flux mixing remains.

After varying, use the background equations to write the linear form equations as

```math
\begin{aligned}
0=\delta\mathcal E_B^{\nu\rho}
&=-\bar\nabla_\mu\delta Q^{\mu\nu\rho}
+\tfrac12\bar Q^{\mu\nu\rho}\partial_\mu h,\\
0=\delta\mathcal E_C^\nu
&=\delta J_C^\nu-\bar\nabla_\mu\delta\Pi^{\mu\nu}
+\tfrac12\bar\Pi^{\mu\nu}\partial_\mu h
+\tfrac12\delta Q^{\nu\mu\rho}\bar G_{\mu\rho}
+\tfrac12\bar Q^{\nu\mu\rho}\delta G_{\mu\rho}
-\tfrac12\bar C_\mu\delta\mathcal E_B^{\mu\nu},\\
0=\delta\mathcal E_E^{\rho\sigma\lambda}
&=\tfrac g2\delta Q^{\rho\sigma\lambda}
+\tfrac12\bar\varepsilon^{\mu\nu\rho\sigma\lambda}\bar\nabla_\nu\delta W_\mu
+\tfrac14h\bar\varepsilon^{\mu\nu\rho\sigma\lambda}\bar\nabla_\nu\bar W_\mu.
\end{aligned}\tag{E68}
```

The responses $`\delta Q,\delta\Pi,\delta W`$ come from E19–E23 and are not additional fields. The remaining bosonic linear equations are the variations of E18, E31, and E38 using E32/E66; this general-background chapter does not expand every perturbation monomial separately.

The required structure of the fermionic linear system is

```math
\begin{pmatrix}
\mathcal K_{\psi\psi}&\mathcal K_{\psi\varphi}\\
\mathcal K_{\varphi\psi}&\mathcal K_{\varphi\varphi}
\end{pmatrix}_{\bar\Phi_B}
\begin{pmatrix}\psi\\\varphi\end{pmatrix}=0
\tag{E69}
```

E69 defines the general-background block arrangement; E63 evaluates only the lower-right block. The AdS5 bilinear maps are given in [the quadratic action](../../ads5/quadratic_action.md), (Q31)–(Q40), (Q57). Two-fermion action order suffices for the classical linear spectrum on a bosonic background.

## Verification record

| Object | Scope of this chapter |
|---|---|
| Bosonic-body equations for the eight independent bosonic field groups | E16, E18, E27, E31, E38, including composite, form, and metric dependence |
| General zero-fermion background conditions | E65; general zero-fermion background |
| Flux, scalar, and internal-connection mixing | Retained in explicit responses and Euler equations |
| Bosonic linearization | Basic variations, $`N`$ and form equations explicit; other equations are specified as variations rather than expanded into every perturbation monomial |
| Dependent $`\omega,\phi,f`$ and hatted-object fermionic variations | E43–E52 |
| Total $`\varphi\varphi`$ operator | E63, including both source coefficients and the current contribution |

The recorded checks used exact rational arithmetic, coefficient comparison, antisymmetry, internal contractions, Clifford traces, Bianchi identities, and integration by parts, with no sampling of free parameters or field components. The bosonic LOG-density equivalence had zero symbolic residual. The check scope is restricted to the general-background expressions displayed here; the selected AdS5 calculation is given in [the quadratic action](../../ads5/quadratic_action.md) and [physical operators](../../ads5/details/physical_operators.md).

