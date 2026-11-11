<a id="step-6--quadratic-action-on-gb-s"></a>

[Notation dictionary](../notation.md).

# Quadratic action for Gauss–Bonnet on AdS₅

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

<a id="61-input-scope-and-fields"></a>

## Input, scope and fields

The sole action is [GB-FINAL-DENSITY](../action/gb_splus_action.md#6-final-result), with definitions GB06–GB14. The [Part I catalogue](background.md) supplies the tadpole-free branch. We import its vanishing tadpoles; we do not derive unrestricted nonlinear equations or reverify the input action.

For real $`g\ne0`$, define the following background constants:

```math
a=\lambda_{\rm GB}g^2,\qquad x=\frac{2}{1+\sqrt{1+2a}},\qquad c=2-x,\qquad ax^2+2x-2=0.
\tag{6.1}
```

The full real domain of the selected AdS₅ branch is $`a\ge-1/2`$, equivalently $`0<x\le2`$. At finite coupling the endpoint $`x=2`$ is included. The generic calculations that divide by $`c`$ have domain $`0<x<2`$. On this branch,

```math
\bar L=x,\qquad \bar N=-\frac32gx^2,\qquad \bar R_{\mu\nu}=4k\bar g_{\mu\nu},\qquad k=-\frac12g^2x^2,\qquad \bar R=20k.
\tag{6.2}
```

All background field strengths, currents and fermions vanish. Their independent fluctuations remain. Set

```math
g_{\mu\nu}=\bar g_{\mu\nu}+t h_{\mu\nu},\quad L=x+t\ell,\quad N=-\frac32gx^2+tn,\quad (C_\mu,B_{\mu\nu},E_{\mu\nu\rho},V_\mu,V'_\mu{}^{ij},\psi_\mu^i,\varphi^i)=t(A_\mu,b_{\mu\nu},e_{\mu\nu\rho},v_\mu,v'_\mu{}^{ij},\Psi_\mu^i,\zeta^i).
\tag{6.3}
```

Here $`t`$ is even; $`b_{\mu\nu}`$ is the two-form fluctuation, not the already fixed dilatation connection $`b_\mu=0`$. The independent three-form is $`e_{\mu\nu\rho}`$, not its constrained dual current. Metric notation quotients the vielbein's local Lorentz redundancy; it does not impose a diffeomorphism gauge. Both spinors obey the accepted symplectic-Majorana reality convention.

Assumptions: A1 is the accepted action through two physical fermions. A2 is its fixed source gauge. A3 is the branch (6.1)–(6.2). A4 is a local bulk problem, with compactly supported variations when deriving Euler equations; no global AdS boundary condition is imposed. A5 is exact finite $`\lambda_{\rm GB}`$, not a small-coupling EFT truncation. Only terms beyond quadratic fluctuation order are dropped. The omitted four-fermion action starts at $`t^4`$ and cannot change the fermionic Hessian on this bosonic background.

The measure and inverse metric needed before collecting the action are

```math
e=\bar e\left[1+\frac t2h+t^2\left(\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}\right)\right]+O(t^3),\quad g^{\mu\nu}=\bar g^{\mu\nu}-t h^{\mu\nu}+t^2h^{\mu}{}_{\rho}h^{\rho\nu}+O(t^3),\quad h=\bar g^{\mu\nu}h_{\mu\nu}.
\tag{6.4}
```

All fluctuation indices below are raised with $`\bar g`$. Write $`\nabla=\bar\nabla`$ and $`\Box=\bar g^{\mu\nu}\nabla_\mu\nabla_\nu`$ only after a full conformal derivative has actually been expanded.

<a id="62-background-composites-and-first-descendants"></a>

## Background composites and first descendants

GB08 and GB11 give

```math
\bar f_{ab}=-\frac k4\eta_{ab},\quad \overline{\mathcal D_a\mathcal D_b\sigma}=-\frac k2\eta_{ab},\quad \overline{\Box^c\sigma}=-\frac52k,\quad \bar D=-\frac58k+\frac g4\bar N+\frac{g^2x^2}{16}=\frac{5-6+1}{16}g^2x^2=0.
\tag{6.5}
```

Also $`\bar T=\bar\chi=\overline{\widehat C}=\overline{\widehat R(V)}=0`$. Thus $`D^2`$ contributes $`(D^{(1)})^2`$; its implicit second-order terms multiplied by $`\bar D`$ vanish. This observation applies to that monomial, not to other covariants having nonzero backgrounds.

At first fermionic order, GB07 and R01 of the [component reference](code/references/COMPONENT_CONVENTIONS.md) give the explicit dependent connections

```math
\mathcal D_a\psi^i\big|_1=-\frac{gx}{2\sqrt2}\delta^{ij}\Psi_{aj}-\phi_a^{(1)i},\quad R'_{ab}(Q)^i\big|_1=2\nabla_{[a}\Psi_{b]}^i,\quad \phi_a^{(1)i}=\frac i3\gamma^bR'_{ab}(Q)^i\big|_1-\frac i{24}\gamma_a\gamma^{bc}R'_{bc}(Q)^i\big|_1.
\tag{6.6}
```

In particular the gauge-fixed dilatino is zero but its derivative is not. The first-order composite spinor is $`\chi^{(1)i}=i\gamma^a\mathcal D_a\psi^i|_1/8+g\zeta^i/8`$. Full ordered $`f_{ab}`$ must still be used at fermion order two; (6.5) asserts symmetry only of its bosonic background.

<a id="63-source-collection-for-the-scalarmetric-subblock"></a>

## Source collection for the scalar–metric subblock

This section extracts the terms with two scalar/metric fluctuations from the full action, without replacing that action by an independently sourced bosonic density. At this order no parity-even scalar–form bilinear can be built from the fluxless background. Potential parity-odd curvature–form terms require their Bianchi contractions; these are part of the form-block calculation, not assumed cancellations of arbitrary terms.

The two-derivative terms in GB-FINAL-DENSITY contribute, after their displayed SU(2) contractions,

```math
-2\Box^c L-8LD+L^{-1}(\partial L)^2-2L^{-1}N^2-4gN+2g^2L^2.
\tag{6.7}
```

For the bosonic scalar–metric restriction of these particular terms, $`\Box^c L=\Box L-3RL/8`$ and $`D=-R/32+gN/4+g^2L^2/16`$. Inserting these gives

```math
-2\Box L+\left(\frac34+\frac14\right)LR+L^{-1}(\partial L)^2-2L^{-1}N^2-2gLN-4gN+2g^2L^2-\frac12g^2L^3.
\tag{6.8}
```

The first term integrates to $`-2\partial_\mu(e\nabla^\mu L)`$; its boundary current is retained when comparing representatives. This computation also explains the coefficient of the compensator kinetic term; it is not inferred from the vacuum potential.

For the higher-derivative scalar–metric restriction, the source labels refer to the existing [literal coefficient ledger](code/outputs/action_coefficients.json). The only nonzero entries in this restriction are Weyl_sigma_N:1–2 and LOG_seed:46–51,71,74–76,80. Their expansions are

```math
\begin{aligned}
-\frac{128}{3}D^2&=-\frac{R^2}{24}+\frac23gRN+\frac16g^2RL^2-\frac83g^2N^2-\frac43g^3NL^2-\frac16g^4L^4,\\
-\frac{10}{3}(\Box^c\sigma)^2-\frac{26}{3}g^2L^2\Box^c\sigma-\frac{32}{3}gN\Box^c\sigma&=-\frac5{96}R^2+\frac{13}{12}g^2RL^2+\frac43gRN,\\
2g^2L\Box^cL+3g^2(\partial L)^2+4g\Box^c N&=2g^2L\Box L+3g^2(\partial L)^2-\frac34g^2RL^2+4g\Box N-2gRN.
\end{aligned}
\tag{6.9}
```

For the Hessian term, use the bosonic restriction $`f_{ab}=-R_{ab}/6+\eta_{ab}R/48`$. Its square and the remaining scalar polynomial are

```math
24f_{ab}f^{ab}=\frac23R_{ab}R^{ab}-\frac{11}{96}R^2,\qquad -\frac7{12}g^4L^4-\frac83g^3NL^2+\frac23g^2N^2-\frac14g^4L^4.
\tag{6.10}
```

The last $`-g^4L^4/4`$ follows from $`L^{ij}L_i{}^kL_j{}^lL_{kl}=L^4/2`$. The coefficient arithmetic is

```math
\begin{aligned}
R^2:&\ -\frac1{24}-\frac5{96}-\frac{11}{96}=-\frac5{24},\qquad gRN:\ \frac23+\frac43-2=0,\qquad g^2RL^2:\ \frac16+\frac{13}{12}-\frac34=\frac12,\\
g^2N^2:&\ -\frac83+\frac23=-2,\qquad g^3NL^2:\ -\frac43-\frac83=-4,\qquad g^4L^4:\ -\frac16-\frac7{12}-\frac14=-1.
\end{aligned}
\tag{6.11}
```

Finally $`-C^2/4=-R_{abcd}R^{abcd}/4+R_{ab}R^{ab}/3-R^2/24`$, and $`2L\Box L=2\nabla_\mu(L\nabla^\mu L)-2(\partial L)^2`$. Thus the piece needed to construct this subblock is

```math
F(L)R-\frac\lambda4\mathcal B+K(L)(\partial L)^2+V(L,N),\quad F=L+\frac\lambda2g^2L^2,\quad K=L^{-1}+\lambda g^2,\quad \mathcal B=R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2,
\tag{6.12}
```

```math
V=-\frac{2N^2}{L}-2gLN-4gN+2g^2L^2-\frac12g^2L^3+\lambda(-2g^2N^2-4g^3NL^2-g^4L^4),\qquad \lambda=\lambda_{\rm GB}.
\tag{6.13}
```

The total divergence removed in (6.12) is $`\nabla_\mu[-2\nabla^\mu L+\lambda(2g^2L\nabla^\mu L+4g\nabla^\mu N)]`$. Equations (6.12)–(6.13) are an intermediate extraction for a quadratic block, not a separate full bosonic action. They have density dimension two; every $`\lambda`$ term before its multiplication has dimension four.

<a id="64-metric-hessian-and-taylor-factors"></a>

## Metric Hessian and Taylor factors

Define the explicitly linear curvature and cosmological Einstein operator

```math
\begin{aligned}
r_{\mu\nu}&=\frac12\left(\nabla_\rho\nabla_\mu h^\rho{}_{\nu}+\nabla_\rho\nabla_\nu h^\rho{}_{\mu}-\Box h_{\mu\nu}-\nabla_\mu\nabla_\nu h\right),\\
r&=\nabla_\mu\nabla_\nu h^{\mu\nu}-\Box h-4kh,\qquad \mathcal G^L_{\mu\nu}(h)=r_{\mu\nu}-\frac12\bar g_{\mu\nu}r-4kh_{\mu\nu}.
\end{aligned}
\tag{6.14}
```

The order of the derivatives in $`r_{\mu\nu}`$ is part of the formula. In particular $`r=\bar g^{\mu\nu}r_{\mu\nu}-4kh`$. The linearized Bianchi identity gives $`\nabla^\mu\mathcal G^L_{\mu\nu}=0`$.

Here is the Lovelock coefficient directly in the second variation. In a mixed-index contraction, the curvature-dependent Gauss–Bonnet variation uses $`-\delta^{\mu\alpha\beta\gamma\delta}_{\nu\rho\sigma\tau\upsilon}R^{\rho\sigma}{}_{\alpha\beta}R^{\tau\upsilon}{}_{\gamma\delta}/8`$. Expanding one curvature about $`k\delta^{\rho\sigma}_{\alpha\beta}`$ supplies two equal slots and

```math
\delta^{\mu\alpha\beta\gamma\delta}_{\nu\rho\sigma\tau\upsilon}\delta^{\tau\upsilon}_{\gamma\delta}=2(5-3)(5-4)\delta^{\mu\alpha\beta}_{\nu\rho\sigma}=4\delta^{\mu\alpha\beta}_{\nu\rho\sigma}.
\tag{6.15}
```

Therefore the coefficient of $`\delta R^{\rho\sigma}{}_{\alpha\beta}`$ is $`-k\delta^{\mu\alpha\beta}_{\nu\rho\sigma}`$. The Einstein contraction is $`-\delta^{\mu\alpha\beta}_{\nu\rho\sigma}/4`$. Their ratio is $`4k`$. The zeroth-curvature and measure pieces combine with the constant potential into the same cosmological Einstein operator because the imported metric tadpole vanishes. For $`\alpha=-\lambda/4`$, the quadratic coefficient is consequently $`F_0+4\alpha k=F_0-\lambda k`$, with no four-derivative metric operator. The factor $`1/2`$ in the Taylor coefficient gives $`-(F_0-\lambda k)h^{\mu\nu}\mathcal G^L_{\mu\nu}/2`$.

On (6.1),

```math
F_0=x+\frac12ax^2=1,\qquad F'_0=1+ax=\frac c x,\qquad K_0=\frac c{x^2},\qquad F_0-\lambda k=1+\frac12ax^2=c.
\tag{6.16}
```

A separate check is a constant conformal perturbation $`h_{\mu\nu}=s\bar g_{\mu\nu}`$. Then $`e\mapsto(1+ts)^{5/2}\bar e`$, $`R\mapsto(1+ts)^{-1}\bar R`$, and $`\mathcal B\mapsto(1+ts)^{-2}\overline{\mathcal B}`$. The $`t^2s^2`$ coefficient is $`3F_0\bar R/8-\alpha\overline{\mathcal B}/8+15V_0/8=-15kc`$, agreeing with $`\mathcal G^L(s\bar g)=6ks\bar g`$ in the metric Hessian. This is a check of the trace coefficient in addition to (6.15).

For the scalar terms, expand $`F R+V`$ at fixed background curvature. The mixed $`h\ell`$ term is $`F'_0\ell r`$; the measure term proportional to $`h\ell(F'_0\bar R+V_L)/2`$ vanishes by the imported $`L`$ tadpole. Similarly $`hnV_N/2=0`$. The remaining Taylor coefficients are

```math
\frac12(F''_0\bar R+V_{LL})=-4cg^2,\qquad V_{LN}=-\frac{8cg}{x},\qquad \frac12V_{NN}=-\frac{2c}{x^2}.
\tag{6.17}
```

For example the first is $`g^2[-5ax^2-(9/2)x+2-(3/2)x+6ax^2-6ax^2]=g^2(2-6x-5ax^2)=-4cg^2`$. The cross coefficient is $`4\bar N/x^2-2g-8agx=-8g(1+ax)=-8gc/x`$. The $`n^2`$ coefficient is $`-2(1/x+a)=-2c/x^2`$.

<a id="65-evaluated-raw-scalarmetric-block"></a>

## Evaluated raw scalar–metric block

Combining (6.14)–(6.17), with all $`h,\ell,n`$ still independent and no fluctuation gauge,

```math
\boxed{S^{(2)}_{h,\ell,n}=\frac1{2\kappa_5^2}\int d^5x\,\bar e\left[-\frac c2h^{\mu\nu}\mathcal G^L_{\mu\nu}(h)+\frac c x\ell r+\frac c{x^2}(\nabla\ell)^2-4cg^2\ell^2-\frac{8cg}{x}\ell n-\frac{2c}{x^2}n^2\right].}
\tag{6.18}
```

No equation has been used to eliminate $`n`$. This expression is the $`t^2`$ coefficient, including its Taylor factor, not the second derivative $`d^2S/dt^2`$.

The remaining raw blocks are evaluated below; their complete source routes are in [the ledger](code/derivations/spectrum/SOURCE_TERM_LEDGER.md).

<a id="66-bosonic-form-and-connection-ingredients"></a>

## Bosonic form and connection ingredients

Use the names of (6.3), and define only linear strengths in this subsection:

```math
G_{\mu\nu}=2\nabla_{[\mu}A_{\nu]},\quad H_{\mu\nu\rho}=3\nabla_{[\mu}b_{\nu\rho]}+\frac g2e_{\mu\nu\rho},\quad H^{\mu\nu}=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\tau}H_{\rho\sigma\tau},\quad e^{\mu\nu}=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\tau}e_{\rho\sigma\tau},\quad p^\mu=\nabla_\nu e^{\mu\nu}.
\tag{6.19}
```

Thus $`\nabla_\mu p^\mu=0`$ identically and $`j_{H\mu}:=\nabla^\nu H_{\nu\mu}=-gp_\mu/2`$. The second identity follows by substituting $`H_2=-*db/2+ge_2/2`$: the divergence of the $`db`$ term is zero by $`d^2b=0`$, and $`\nabla_\nu e^{\nu\mu}=-p^\mu`$. No equation of motion has been used. $`F(v)=dv`$ and $`F(p)=dp`$ denote ordinary exterior derivatives.

The Hodge relation gives $`H_{ab}H^{ab}=-H_{abc}H^{abc}/12`$: the epsilon contraction is $`\varepsilon^{ab cde}\varepsilon_{ab fgh}=-2!3!\delta^{[c}_f\delta^d_g\delta^{e]}_h`$, and the two factors $`1/12`$ leave $`-12/144=-1/12`$. The full Hodge tensor has metric variations, but a metric fluctuation multiplying two linear form strengths has degree three, so the background star is sufficient in this quadratic block.

The two-derivative coefficient collection from GB-FINAL-DENSITY is

```math
\begin{aligned}
G^2:&\ -\frac{x}{12}-\frac{5x}{12}=-\frac x2,\qquad GH:\ \frac x3-\frac x3=0,\qquad H^2:\ -\frac x3+\frac{13x}{3}=4x,\\
p^2:&\ \frac2x-\frac4x=-\frac2x,\qquad pv:\ -\sqrt2e^{\mu\nu}F_{\mu\nu}(v)\doteq-2\sqrt2p\cdot v,\qquad pA:\ -2gG_{\mu\nu}e^{\mu\nu}\doteq-4gp\cdot A.
\end{aligned}
\tag{6.20}
```

For the $`p^2`$ transfer, $`-4e^{\mu\nu}\nabla_\mu p_\nu/x\doteq4(\nabla_\mu e^{\mu\nu})p_\nu/x=-4p^2/x`$. For the last two entries, $`\nabla_\mu e^{\mu\nu}=-p^\nu`$ gives $`e^{\mu\nu}F_{\mu\nu}(v)\doteq2p\cdot v`$ and $`e^{\mu\nu}G_{\mu\nu}\doteq2p\cdot A`$. Each $`\doteq`$ discards the displayed product-rule divergence, respectively $`-4\nabla_\mu(e^{\mu\nu}p_\nu)/x`$, $`-2\sqrt2\nabla_\mu(e^{\mu\nu}v_\nu)`$ and $`-4g\nabla_\mu(e^{\mu\nu}A_\nu)`$.

The connection mass comes from differentiating the constant compensator. In doublet matrix notation let $`\epsilon=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$ and $`v'=\left(\begin{smallmatrix}u&w\\w&-u\end{smallmatrix}\right)`$. Since $`v'\epsilon=-\epsilon v'`$, (GB09) gives $`\mathcal D_aL^{ij}=\delta^{ij}\partial_a\ell/\sqrt2+\sqrt2x(v'_a\epsilon)^{ij}`$ at bosonic first order. Consequently

```math
\mathcal D_aL^{ij}\mathcal D^aL_{ij}=(\partial\ell)^2+2x^2v'_a{}^{ij}v'^a{}_{ij},\qquad (\Box^c L)_{v'^2}=-2xv'^2.
\tag{6.21}
```

The two-derivative terms give $`+4xv'^2-2xv'^2=2xv'^2`$. The LOG terms $`2g^2L_{ij}\Box^cL^{ij}+3g^2\mathcal D L_{ij}\mathcal D L^{ij}`$ give $`-4g^2x^2v'^2+6g^2x^2v'^2=2g^2x^2v'^2`$. The trace connection commutes with the compensator direction and does not acquire this mass.

<a id="67-ordered-conformal-derivatives-in-the-form-block"></a>

## Ordered conformal derivatives in the form block

The full calculation of the derivative monomials is supplied in [the explicit form-derivative check](code/derivations/support/part2_form_derivative_check.md), equations FD1–FD10 and its term table. Here the actual substitutions and sums needed for the raw block are retained. For a K-primary two-form $`X`$ of weight $`w`$, G01 and R04a give

```math
\mathcal D_a\mathcal D_bX_{cd}=\nabla_a\nabla_bX_{cd}+2wf_{ab}X_{cd}-2f_a{}^e(M_{be}X)_{cd},\quad(M_{be}X)_{cd}=\eta_{bc}X_{ed}-\eta_{ec}X_{bd}+\eta_{bd}X_{ce}-\eta_{ed}X_{cb}.
\tag{6.22}
```

The minus in front of the Lorentz term follows because $`\delta_K\omega_{bc}{}^e=2\eta_{bc}\Lambda^e-2\Lambda_c\delta_b^e`$ and the outer derivative subtracts the K transformation. This supplies an independent sign test: the antisymmetric part of the K correction is $`-kM_{ab}X`$, canceling $`[\nabla_a,\nabla_b]X=kM_{ab}X`$ on the conformally flat background. We use weights $`w(T)=1,w(G)=2,w(H)=3`$ before gauge evaluation.

Introduce temporary contraction labels $`A_{XY}=\nabla_aX_{bc}\nabla^aY^{bc}`$ and $`J_{XY}=j_X\cdot j_Y`$. The concrete ordered-derivative and Bianchi reductions are

```math
Y^{ab}\mathcal D_a\mathcal D^cX_{bc}\doteq J_{XY}+\frac{w-3}{2}kXY,\quad Y^{ab}\mathcal D^c\mathcal D_aX_{bc}\doteq J_{XY}+\frac{w-3}{2}kXY,\quad A_{GY}\doteq2J_{GY}-6kGY.
\tag{6.23}
```

The last equation uses $`dG=0`$, not $`dH=0`$. Applying FD1–FD6 term by term to Weyl_sigma_N:6–8 and LOG_seed:33,35,37,39–45,52–59 gives

```math
\frac{10}{3}A_{GG}-\frac{14}{3}A_{GH}-\frac{20}{3}J_{GG}+\frac{52}{3}J_{GH}-8J_{HH}+\frac{62}{3}kG^2-12kGH+\frac{88}{3}kH^2\doteq8J_{GH}-8J_{HH}+\frac23kG^2+16kGH+\frac{88}{3}kH^2.
\tag{6.24}
```

For example, the $`J_{GG}`$ coefficient is $`-20/3+20/3=0`$ and the $`J_{GH}`$ coefficient is $`52/3-28/3=8`$. LOG_seed:19–25,32,34,36,38 add $`-17kG^2/3+0GH-112kH^2/3`$. Hence the derivative-plus-algebraic subtotal is $`8J_{GH}-8J_{HH}-5kG^2+16kGH-8kH^2`$.

Term LOG_seed:287 is an ordered third derivative. The current $`j_H`$ is K-primary of weight four because $`\delta_K j_{H a}=2(3-w(H))\Lambda^bH_{ba}=0`$. Therefore $`\Box^c j_H=(\Box-10k)j_H`$, and

```math
8A^a\Box^c\mathcal D^cH_{ac}=-8A^a(\Box-10k)j_{H a}\doteq-8J_{GH}+48kA\cdot j_H.
\tag{6.25}
```

Here $`\Box A_a=j_{Ga}+\nabla_a\nabla\cdot A+4kA_a`$ and $`\nabla\cdot j_H=0`$ fix the curvature term and remove the longitudinal transfer. LOG_seed:284,288,290,292 add $`(-1-1-5/2+1/2)kA\cdot j_G=-4kA\cdot j_G`$. Terms 286,289,291,293 add $`(-10+2+5-1)kA\cdot j_H=-4kA\cdot j_H`$. Since $`A\cdot j_X\doteq-GX/2`$, the subtotal including these currents is $`-8J_{HH}-3kG^2-6kGH-8kH^2`$.

The remaining quadratic scalar-coefficient currents are LOG_seed:246–251. Their sums are

```math
\begin{aligned}
A^a\nabla^bG_{ab}:&\quad\frac83\left(-\frac52k\right)+\frac83(-2k)+\frac{20}{3}(3k)=8k,\\
A^a\nabla^bH_{ab}:&\quad-\frac{40}{3}\left(-\frac52k\right)-\frac43(-2k)-\frac{16}{3}(3k)=20k.
\end{aligned}
\tag{6.26}
```

Since $`A^a\nabla^bX_{ab}\doteq GX/2`$, these add $`4kG^2+10kGH`$. The total higher-derivative form subtotal is consequently

```math
-8j_H^2+kG^2+4kGH-8kH^2=-2g^2p^2+kG^2+4kGH-8kH^2.
\tag{6.27}
```

Terms LOG_seed:26–31 vanish because their epsilon contracts the three-index or four-index algebraic Bianchi identity of the bosonic Weyl tensor: $`C_{a[bcd]}=0`$ or $`C_{[abcd]}=0`$, including its differentiated form. Terms 72–73 and 294–295 contract a symmetric background Hessian with an antisymmetric pair. Terms 283/285 have a background third scalar derivative, which is zero. These facts also exclude scalar–form mixing in (6.18). The other bosonic form monomials carry at least three zero-background factors and start at $`t^3`$.

<a id="68-r-connection-mixing-and-complete-bosonic-block"></a>

## R-connection mixing and complete bosonic block

Weyl_Y:6 and LOG_seed:60,81 give

```math
\frac{16}{3}gL^{ij}R(V)_{abij}\frac{G^{ab}-2H^{ab}}8+\frac43gL^{ij}R(V)_{abij}G^{ab}-\frac83gL^{ij}R(V)_{abij}H^{ab}=2gL^{ij}R(V)_{abij}G^{ab}-4gL^{ij}R(V)_{abij}H^{ab}.
\tag{6.28}
```

LOG_seed:274 gives $`-4gA^aL^{ij}\nabla^bR(V)_{abij}\doteq-2gL^{ij}G^{ab}R(V)_{abij}`$; it cancels the first term. The background contraction is $`L^{ij}R(V)_{abij}=xF_{ab}(v)/\sqrt2`$, so the remainder is $`-2\sqrt2gxH^{ab}F_{ab}(v)\doteq-2\sqrt2g^2xp\cdot v`$. The equality uses $`HF(v)\doteq-2v\cdot j_H=gv\cdot p`$. The explicit curvature squares cancel as $`2R(V)^2/3-2R(V)^2/3=0`$.

Combine (6.20)–(6.28), using $`ax^2=2-2x`$, $`\lambda k=-ax^2/2`$ and $`GH\doteq-2A\cdot j_H=gp\cdot A`$:

```math
\begin{aligned}
G^2:&\ -\frac x2+\lambda k=-\frac{x+ax^2}{2}=-\frac c2,\qquad H^2:\ 4x-8\lambda k=4(x+ax^2)=4c,\\
p^2:&\ -\frac2x-2\lambda g^2=-\frac{2c}{x^2},\qquad pv:\ -2\sqrt2(1+ax)=-\frac{2\sqrt2c}{x},\\
pA:&\ -4g+4\lambda kg=-4gc,\qquad v'^2:\ 2x+2ax^2=2c.
\end{aligned}
\tag{6.29}
```

The complete raw bosonic quadratic block, still with all independent bosonic fluctuations, is

```math
\boxed{S^{(2)}_B=\frac1{2\kappa_5^2}\int\bar e\,c\left[-\frac12h^{\mu\nu}\mathcal G^L_{\mu\nu}(h)+\frac{\ell r}{x}+\frac{(\nabla\ell)^2}{x^2}-4g^2\ell^2-\frac{8g}{x}\ell n-\frac{2n^2}{x^2}-\frac12G^2+4H^2-\frac{2p^2}{x^2}-\frac{2\sqrt2}{x}p\cdot v-4gp\cdot A+2v'^2\right].}
\tag{6.30}
```

In (6.30), $`G,H,p`$ are the explicit derivatives of $`A,b,e_3`$ in (6.19), not new independent fields. All equalities retain the source current normalization. The cancellation is established for the full bosonic Hessian on this branch. The separately derived fermionic block follows in §6.9.

<a id="69-complete-raw-fermionic-block"></a>

## Complete raw fermionic block

The full source calculation is [Fermionic calculations](details/fermionic_reduction.md), FC1–FC15. It expands the dependent $`\phi_a`$, $`\chi`$, $`\mathcal D\psi`$, $`\mathcal D\varphi`$, both ordered second derivatives, and the implicit bilinears in $`f_a{}^a`$, $`\Box^c\sigma`$, $`\Box^cL^{ij}`$ and $`\Box^cN`$. The [component sums](code/derivations/spectrum/FERMION_COMPONENT_SUMS.md) display all nonzero coefficient patterns, including the cancellation of the cubic and quadratic derivatives. These appendices are the detailed coefficient calculation for this step.

Define $`m=gx/(2\sqrt2)`$ and $`J(\zeta^1,\zeta^2)=(-\zeta^2,\zeta^1)`$, so $`J^2=-1`$, $`k=-4m^2`$. Pairings without explicit $`\delta_{ij}`$ use NW–SE contraction; $`\delta_{ij}\bar A^iB^j=-\bar A J B`$. Adding the two-derivative coefficients to the higher-derivative coefficients in FC15 gives the raw action in original independent fields:

```math
\boxed{\ell_F^{(2)}=c\left[-\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c+\frac2{x^2}\bar\zeta\not\nabla\zeta-\frac{2\sqrt2i}{x}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\nabla_b\zeta^j-\frac{3igx}{2\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j-4g\bar\Psi_a\gamma^a\zeta+\frac{7ig}{\sqrt2x}\delta_{ij}\bar\zeta^i\zeta^j\right].}
\tag{6.31}
```

There is no gauge condition on $`\Psi_a`$, $`\zeta`$, their traces or divergences. In particular $`\zeta`$ is independent; it is not removed as a compensator remnant. All integrations by parts use the compact-support convention in §6.1. The density representative (6.31) differs from the directly expanded source only by the boundary currents tracked in FC5–FC11 and the descendant appendix.

Since the background is bosonic and the accepted action has even fermion number, there is no boson–fermion bilinear. Thus the complete result of Step 6 is

```math
S^{(2)}=\frac1{2\kappa_5^2}\int d^5x\,\bar e\,[\ell_B^{(2)}+\ell_F^{(2)}],\qquad \ell_B^{(2)}\text{ given by (6.30)},\quad \ell_F^{(2)}\text{ given by (6.31)}.
\tag{6.32}
```

Both expressions retain every independent fluctuation. The use of the branch relation $`ax^2+2x-2=0`$ did not divide by $`c`$, so (6.32) also holds at the endpoint.
