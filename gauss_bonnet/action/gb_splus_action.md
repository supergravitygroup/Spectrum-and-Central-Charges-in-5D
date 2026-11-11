---
title: Gauged Gauss–Bonnet action through two physical fermions
date: 2026-09-28
status: assembled and checked from the adopted input actions; inherited Weyl-map qualification retained
convention_lock: GB-FERMION-SPECTRUM-CONVENTIONS-v1
action_lock: GB-FERMION-ACTION-0+2-v1
assumptions: [A1, A2, A3, A4, A5, A6]
---

# Gauged Gauss–Bonnet action through two physical fermions

<a id="1-problem-and-target"></a>

## Problem and Target

We construct the total gauged action, including the two-derivative part, with all bosonic terms and all terms containing two physical fermions. The final density is collected in **one continuous expression in §6**, with several factors and terms on each row. The intermediate derivation explains the normalization, gauge evaluation, density insertions, and coefficient arithmetic. It uses the previously derived LOG, Weyl, and two-derivative actions as inputs.

The target normalization and the normalization of the existing Weyl file are different. In the common component frame the combination is

```math
\ell_{\rm tot}^{(0+2)}=\left[\ell_{2\partial}^{\rm inherited}+\lambda_{\rm GB}\left(-2\ell_{\rm W,OP}^{\rm inherited}-4\ell_{\log}^{\rm inherited}\right)\right]_{\le2},\qquad S^{(0+2)}=\frac1{2\kappa_5^2}\int d^5x\,e\,\ell_{\rm tot}^{(0+2)}.
\tag{GB01}
```

The factor $`-2`$ on the OP-normalized Weyl input is derived below from its **complete primary**, including the fermions. The already converted LOG input has unit normalization before the GB multiplier $`-4`$. No additional linear-multiplet bridge is applied to it.

The precise assumptions are:

1. **A1 — Off-shell fields.** We retain the independent vielbein, gravitino, graviphoton, two-form, linear compensator, R-symmetry connection, and constrained three-form. No auxiliary-field equation, background, or fermion fluctuation gauge is used.
2. **A2 — Source gauge.** On the nonzero compensator patch we use $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$, $`L^{ij}=\delta^{ij}L/\sqrt2`$. The spinor without a world index is the dilatino; $`\psi_\mu^i`$ and $`\varphi^i`$ remain independent physical fermions. No condition $`L=1`$ is imposed.
3. **A3 — Fermion order.** “Complete” means through two physical fermions. The symbol $`[\ ]_{\le2}`$ includes fermions inside all supercovariants, dependent connections, and ordered derivatives. The omitted interactions start at $`O(\Psi^4)`$, where $`\Psi=(\psi_\mu,\varphi)`$.
4. **A4 — Adopted Weyl map.** The input is FM01–FM04 and its gauged GA24 density, including the project-derived $`8/3`$ coefficient in FM02. Its independent nonlinear multiplet tests retain the qualifications stated in the source derivation. The present assembly does not promote those tests to a completed supersymmetry certificate.
5. **A5 — Other inherited actions.** The LOG input is the current corrected ordinary-current action. The two-derivative input is the explicit 2016-map calculation, its equation (5.10). Its recorded comparison/reality qualifications remain inherited.
6. **A6 — Equality and boundaries.** Algebraic equalities below are exact through the stated fermion order. The symbol $`\doteq`$ allows the explicitly described current integration by parts in the inherited two-derivative representative. Local bulk variations can have compact support; no boundary condition or boundary norm is assigned here.

The eleven exact action inputs are frozen and hashed in [the action input manifest](../ads5/code/inputs/action_sources.json). The [convention reference](../ads5/code/references/COMPONENT_CONVENTIONS.md) supplies all fields, variations, curvatures, and derivative towers, with source equations and an [index](../ads5/code/references/COMPONENT_INDEX.md).

<a id="2-convention-ledger"></a>

## Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fourier_convention=not_used, renormalization_scheme=not_applicable_classical -->

We use $`a,b=0,\ldots,4`$, $`\mu,\nu=0,\ldots,4`$, $`i,j=1,2`$, $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$, and $`e=\det e_\mu{}^a>0`$. Antisymmetrization has unit weight. The orientation, Clifford algebra and full-contraction convention are

```math
\varepsilon^{01234}=1,\quad \varepsilon_{01234}=-1,\quad \varepsilon^{\mu\nu\rho\sigma\tau}=e^{-1}[\mu\nu\rho\sigma\tau],\qquad \{\gamma^a,\gamma^b\}=2\eta^{ab},\quad \gamma^{01234}=i,\quad \gamma\!\cdot\!T=\gamma^{ab}T_{ab}.
\tag{GB02}
```

The world epsilon in this document is a tensor; it has no additional factor of $`e^{-1}`$ when converted from tangent indices. Dots contain no factorial. The Majorana bar and SU(2) rules are

```math
\bar\zeta^{\,i}=(\zeta^i)^T\mathsf C,\quad \overline{i\zeta}=i\bar\zeta,\quad X^i=\varepsilon^{ij}X_j,\quad X_i=X^j\varepsilon_{ji},\quad \varepsilon_{12}=\varepsilon^{12}=1,\quad \bar u\Gamma v=\bar u^i\Gamma v_i.
\tag{GB03}
```

The bar is linear, not a Hermitian conjugation. For odd spinors, $`\bar u^i\gamma_{(n)}v^j=t_n\bar v^j\gamma_{(n)}u^i`$, with $`(t_0,t_1,t_2,t_3)=(1,1,-1,-1)`$; contracting the doublet indices introduces the additional minus in $`\bar u\gamma_{(n)}v=-t_n\bar v\gamma_{(n)}u`$. The construction below preserves the inherited spinor order, so none of its coefficient multiplications requires a new flip or Fierz transformation.

All spinors and supersymmetry parameters are Grassmann odd. Functional variations are left variations, with $`\delta\Psi`$ moved to the left and the two contributions of a diagonal Majorana bilinear both retained. No functional variation is performed in this assembly. The curvature sign is fixed by

```math
R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\qquad R_{\mu\nu}=R_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a},\qquad R_{\mu\nu\rho\sigma}=k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})\ \Rightarrow\ R=20k.
\tag{GB04}
```

The hatted Lorentz/Weyl curvature in the action is the full conformal curvature. Only its purely bosonic restriction may be treated with the usual pair interchange and algebraic Bianchi symmetries. In particular, the ordered primed Ricci tensor and $`f_{ab}`$ are not assumed symmetric at two fermions.

In the displayed result only, the independent-compensator labels $`L_c^{ij},\varphi_c,N_c,E_c`$ are written $`L^{ij},\varphi,N,E`$. This is a notational identification, without rescaling. $`\phi_\mu`$ is the dependent S connection and differs from the independent $`\varphi`$. $`\psi^i`$ denotes the gauge-fixed dilatino even when it appears inside a nonzero full derivative.

After the compensator scale is fixed, the engineering dimensions are

```math
[\mathcal D]=[g]=[T]=[\widehat G]=[\widehat H_2]=[N]=[E_a]=1,\quad [\psi_a]=[\varphi]=\tfrac12,\quad [\chi]=[\widehat R(Q)]=\tfrac32,\quad [D]=[\widehat C]=[\widehat R(V)]=2,\quad [L]=[C_a]=0.
\tag{GB05}
```

These dimensions are distinct from conformal weights before gauge fixing. We use $`[\lambda_{\rm GB}]=-2`$, $`[\kappa_5^2]=-3`$. No Fourier transform, analytic continuation, or renormalization prescription is used.

<a id="3-definitions-and-required-identities"></a>

## Definitions and Required Identities

<a id="31-full-derivatives-and-the-gauge-evaluation"></a>

### Full derivatives and the gauge evaluation

The source definitions are LOG G01, W04, L02, GG03–GG05 and the ordered derivative dictionary SC7D in [the component reference](../ads5/code/references/COMPONENT_CONVENTIONS.md#ordered-gauge-fixed-derivatives-hessians-and-conformal-boxes). In particular,

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad \mathcal D_a=e_a{}^\mu\mathcal D_\mu,\quad \square^C=\Box^c=\mathcal D^a\mathcal D_a.
\tag{GB06}
```

The notation $`|_{\mathrm P}`$ means evaluation in A2 **after** full differentiation. Both notations for the box in the input files denote this ordered conformal box. They never mean the Levi–Civita scalar Laplacian unless such a restriction is separately derived.

For example, substitute $`T_{ab}=(\widehat G_{ab}-2\widehat H_{ab})/8`$ into LOG-G02a:

```math
\mathcal D_a\psi^i\big|_{\mathrm P}=\left(\frac14\gamma^{bc}\widehat G_{bc}-\gamma^{bc}T_{bc}\right)\psi_a^i-\frac g2L^{ij}\psi_{aj}-\phi_a^i=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L^{ij}\psi_{aj}-\phi_a^i.
\tag{GB07}
```

Thus $`\psi^i|_{\mathrm P}=0`$ does not make $`\mathcal D_a\psi^i|_{\mathrm P}`$ vanish. Likewise the scalar Hessian and its trace, using the fixed ordering of SC7D, are

```math
\mathcal D_a\mathcal D_b\sigma\big|_{\mathrm P}=2f_{ab}-\frac i2\bar\psi_a\mathcal D_b\psi\big|_{\mathrm P}-2\bar\psi_a\gamma_b\chi,\qquad \Box^c\sigma\big|_{\mathrm P}=2f_a{}^a-\frac i2\bar\psi_a\mathcal D^a\psi\big|_{\mathrm P}-2\bar\psi_a\gamma^a\chi.
\tag{GB08}
```

An explicit constant-compensator derivative also keeps the connection:

```math
\mathcal D_aL^{ij}\big|_{\mathrm P}=\frac{\delta^{ij}}{\sqrt2}\partial_aL+\frac L{\sqrt2}\left(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\right)-i\bar\psi_a^{(i}\varphi^{j)},\qquad V_a^{ij}=V'_a{}^{ij}+\frac12\delta^{ij}V_a.
\tag{GB09}
```

All linear-multiplet spinor derivatives and contracted Hessians in §6 have the full L02/SC7D meaning. Equations (4.21), (4.24), (4.30), and (4.32) of [the two-derivative input](../../common/two_derivative_action/details/construction.md) give the related gauge-evaluated objects. Its lower-index (4.27) retains an earlier connection sign; it is not literally identical to (GC24) or (GB09). The existing index-lowering derivation and the scope of this source difference are given in the [input correspondence](../../references/fermionic_input_correspondence.md#lower-triplet-derivative).

<a id="32-gauged-covariants-and-form-current"></a>

### Gauged covariants and form current

The complete ungauged formulas and their gauged replacements have already been extracted in GG01–GG05 and GC01–GC24. In particular, before the gauge is applied the full spinor composite is

```math
\chi^i=\frac{i}{8\sigma}\not{\mathcal D}\psi^i+\frac{i}{16\sigma^2}\not{\mathcal D}\sigma\,\psi^i-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\,\psi^i+\frac1{4\sigma}\gamma\!\cdot\!T\,\psi^i+\frac{i}{32\sigma^3}\psi_j\bar\psi^i\psi^j-\frac{g}{16\sigma^3}L^{ij}\psi_j+\frac{g}{8\sigma^2}\varphi^i.
\tag{GB10}
```

Its gauge value and the scalar composite are

```math
T_{ab}=\frac18(\widehat G_{ab}-2\widehat H_{ab}),\quad \widehat H^{ab}=-\frac1{12}\varepsilon^{abcde}\widehat H_{cde},\quad \chi^i\big|_{\mathrm P}=\frac i8\not{\mathcal D}\psi^i\big|_{\mathrm P}+\frac g8\varphi^i,\quad D\big|_{\mathrm P}=\frac14\Box^c\sigma\big|_{\mathrm P}+\frac5{96}\widehat G^2+\frac1{24}\widehat G\!\cdot\!\widehat H-\frac{13}{24}\widehat H^2+\frac g4N+\frac{g^2}{16}L^{ij}L_{ij}.
\tag{GB11}
```

The shorthand squares and dots contract all indicated tangent indices. These definitions, including the dependence of $`D`$ on the ordered K connection, remain part of the action.

For clarity, the source gauge gives the explicit supercovariant strengths

```math
\widehat G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\qquad
\widehat H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}+\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
\tag{GB12}
```

Here $`G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}`$ is the ordinary strength in the Chern–Simons term. The source formula contains the full additional dilatino pieces before gauge fixing; those must be retained whenever that expression is differentiated. The conventional constraints $`R(P)=0`$, $`\gamma^\mu\widehat R_{\mu\nu}(Q)=0`$, and $`e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0`$ determine $`\omega,\phi,f`$. Their explicit expressions, the ordered primed Lorentz curvature, $`\widehat R(Q)`$, $`\widehat R(V)`$ and their variations are R01–R07 in [the local reference](../ads5/code/references/COMPONENT_CONVENTIONS.md#connections-curvatures-and-their-variations); they are definitions, not equations of motion of the GB action.

The ordinary current of a generic linear multiplet $`X`$ is

```math
P_X^a=E_X^a+\frac i2\bar\psi_b\gamma^{ba}\varphi_X+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{X\,ij}.
\tag{GB13}
```

For the independent compensator we use the corrected tensor/density convention

```math
E^{\mu\nu}=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}E_{\rho\sigma\tau},\qquad P^\mu=e^{-1}\partial_\nu(eE^{\mu\nu}).
\tag{GB14}
```

It is this $`E^{\mu\nu}`$ that occurs in the two-derivative density. $`E_a`$ denotes the supercovariant constrained vector in GB13, not the potential. GB14 incorporates the current repair already anchored in the LOG branch and does not repeat the older extra-determinant typo.

<a id="33-the-vectorlinear-density"></a>

### The vector–linear density

The repaired ordinary-current version of OP (3.1), LOG-S1-16, is

```math
\ell_{\rm VL}(V,X)=Y^{ij}L_{X\,ij}+i\bar\lambda\varphi_X-\frac12\bar\psi_a^i\gamma^a\lambda^jL_{X\,ij}+A_aP_X^a+\rho\left(N_X+\frac12\bar\psi_a\gamma^a\varphi_X+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{X\,ij}\right).
\tag{GB15}
```

For the defining vector, $`(\rho,A,\lambda,Y)=(\sigma,C,\psi,Y)`$ with $`Y^{ij}=i\bar\psi^{(i}\psi^{j)}/(4\sigma)-gL^{ij}/(2\sigma)`$. Therefore its source-gauge values are $`(1,C,0,-gL^{ij}/2)`$. This substitution will account for every explicit BF term in the higher-derivative action.

<a id="4-detailed-derivation"></a>

## Detailed Derivation

### Step 1. Normalize the complete Weyl primary

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, metric_signature=(-,+,+,+,+), bar=linear_Majorana -->

C24 equation (4.3a), PDF p.31 / printed p.30, gives $`h_W^{ij}=-iW^{\alpha\beta\gamma(i}W_{\alpha\beta\gamma}{}^{j)}/2-w^{ab}\Phi_{ab}^{ij}+256i\chi^{\alpha(i}\chi_\alpha{}^{j)}/3`$. Its footnote 4 (PDF p.9), the component torsion projection (2.17), Appendix A (A.4a), and Appendix C Table 4 (PDF p.91) give

```math
W_{\alpha\beta\gamma}^i=\frac12(\Sigma^{ab})_{\alpha\beta}W_{ab\gamma}^i,\quad \frac12(\Sigma_{ab})^{\alpha\beta}(\Sigma^{ab})_{\rho\sigma}=\delta_{(\rho}^{\alpha}\delta_{\sigma)}^\beta,\quad W_{ab}^i=i\widehat R_{ab}^i(Q),\quad w_{ab}=\frac{16}{3}T_{ab},\quad \Phi_{ab}^{ij}=-\widehat R_{ab}^{ij}(V).
\tag{GB16}
```

Insert the inverse conversion twice. The two factors $`1/2`$ give $`1/4`$ and contraction of the pair kernel gives $`2`$, leaving $`1/2`$. The remaining spinor contraction is the Majorana bilinear:

```math
W^{\alpha\beta\gamma(i}W_{\alpha\beta\gamma}{}^{j)}=\frac12\overline{W_{ab}^{(i}}W^{j)ab}=\frac12i^2\overline{\widehat R_{ab}^{(i}(Q)}\widehat R^{j)ab}(Q)=-\frac12\overline{\widehat R_{ab}^{(i}(Q)}\widehat R^{j)ab}(Q).
\tag{GB17}
```

The minus is $`i^2`$, with no fermion interchange. Hence each of the three terms in the primary becomes

```math
-\frac i2\left(-\frac12\bar R(Q)^{(i}R(Q)^{j)}\right)=\frac i4\bar R(Q)^{(i}R(Q)^{j)},\quad -\left(\frac{16}{3}T^{ab}\right)\left(-\widehat R_{ab}^{ij}(V)\right)=\frac{16}{3}\widehat R_{ab}^{ij}(V)T^{ab},\quad \frac{256i}{3}\chi^{\alpha(i}\chi_\alpha{}^{j)}=\frac{256i}{3}\bar\chi^{(i}\chi^{j)}.
\tag{GB18}
```

The suppressed curvature indices in the first equality are exactly those in GB17. These are all the terms of FM01. Thus $`h_W|_{G\to B}=L_{\rm W,OP}`$ including both fermion bilinears. Now apply the **generic** linear-slot bridge $`h_G=-L/2`$: $`L_{\rm W,target}=-2L_{\rm W,OP}`$. The linear transformation law and its independent scalar/vector projections propagate this constant:

```math
\delta(-2L_{\rm W,OP}^{ij})=i\bar\epsilon^{(i}(-2\varphi_{\rm W,OP}^{j)}),\qquad (\varphi_{\rm W,target},N_{\rm W,target},E_{\rm W,target})=-2(\varphi_{\rm W,OP},N_{\rm W,OP},E_{\rm W,OP}),\qquad P_{\rm W,target}=-2P_{\rm W,OP}.
\tag{GB19}
```

For the last equality insert the three scaled slots into GB13 and factor out $`-2`$. Substitution into every slot of GB15 then proves $`\ell_{\rm W,target}=-2\ell_{\rm W,OP}`$. It does not change the defining vector or the common covariant derivative. This argument uses the inherited descendant map with the input conventions stated in §7.

Each primary term has conformal weight three and every BF term has weight five. The multiplier is dimensionless. The [normalization explanation](../ads5/code/derivations/support/gb-action-normalization-EXPLAIN.md) also displays the complete bosonic scalar/current comparison and the explicit Clifford-pair checks.

### Step 2. Gauge the BF density and distribute both GB factors

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, derivatives=full_before_gauge -->

Insert $`(1,C,0,-gL^{ij}/2)`$ into GB15 and expand $`C_aP_X^a`$ using GB13. The two terms containing an undifferentiated defining gaugino vanish, leaving exactly seven insertions:

```math
\ell_X\big|_{\mathrm P}=N_X-\frac g2L^{ij}L_{X\,ij}+C_aE_X^a+\frac12\bar\psi_a\gamma^a\varphi_X+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_X+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{X\,ij}+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{X\,ij}.
\tag{GB20}
```

Multiplication of these seven coefficients by $`-2`$ or $`-4`$ gives the following complete density arithmetic. The linear-multiplet label is W,OP or LOG in the corresponding column.

| Field structure | Weyl input coefficient | Weyl contribution to GB | LOG input coefficient | LOG contribution to GB |
|---|---:|---:|---:|---:|
| $`N_X`$ | $`1`$ | $`-2`$ | $`1`$ | $`-4`$ |
| $`gL^{ij}L_{X\,ij}`$ | $`-1/2`$ | $`1`$ | $`-1/2`$ | $`2`$ |
| $`C_aE_X^a`$ | $`1`$ | $`-2`$ | $`1`$ | $`-4`$ |
| $`\bar\psi_a\gamma^a\varphi_X`$ | $`1/2`$ | $`-1`$ | $`1/2`$ | $`-2`$ |
| $`C_a\bar\psi_b\gamma^{ba}\varphi_X`$ | $`i/2`$ | $`-i`$ | $`i/2`$ | $`-2i`$ |
| $`\bar\psi_a^i\gamma^{ab}\psi_b^jL_{X\,ij}`$ | $`i/4`$ | $`-i/2`$ | $`i/4`$ | $`-i`$ |
| $`C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{X\,ij}`$ | $`1/4`$ | $`-1/2`$ | $`1/4`$ | $`-1`$ |

Thus there is no unspecified “current completion” in the endpoint. Its two current-completion terms are the fifth and seventh rows.

### Step 3. Carry the gauging through derivatives before truncating

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, derivatives=ordered_full_D_Q_S_K -->

The explicit $`gL L_X`$ term is only part of the gauging: GB10, GB11 and GB12 also enter all descendants. To see why differentiating a gauge value would lose terms, differentiate the last two terms of GB10 before imposing A2:

```math
\begin{aligned}
\mathcal D_a\left(-\frac{g}{16\sigma^3}L^{ij}\psi_j+\frac{g}{8\sigma^2}\varphi^i\right)={}&\frac{3g}{16\sigma^4}(\mathcal D_a\sigma)L^{ij}\psi_j-\frac{g}{16\sigma^3}(\mathcal D_aL^{ij})\psi_j-\frac{g}{16\sigma^3}L^{ij}\mathcal D_a\psi_j\\
&-\frac{g}{4\sigma^3}(\mathcal D_a\sigma)\varphi^i+\frac{g}{8\sigma^2}\mathcal D_a\varphi^i
\ \xrightarrow{\mathrm P}\ -\frac g{16}L^{ij}\mathcal D_a\psi_j\big|_{\mathrm P}+\frac g8\mathcal D_a\varphi^i\big|_{\mathrm P}.
\end{aligned}\tag{GB21}
```

The first, second and fourth terms vanish after this first derivative because $`\psi|_{\mathrm P}=\mathcal D_a\sigma|_{\mathrm P}=0`$. The third term remains by GB07. A second derivative acts on this full expression and its connection representations; GB08 is retained. The final action keeps the inherited ordered covariants and therefore keeps precisely this information. No replacement $`\mathcal D\to\nabla`$ is made.

### Step 4. Insert the Weyl slots and retain all physical degrees zero and two

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fermion_degree=physical_after_covariant_expansion -->

The input GA24 is already the nine-slot BF expansion of FM01–FM04. Its exact source ledger has 73 outer terms. Gauge fixing removes the 11 defining-dilatino terms, the 3 gravitino–dilatino terms, and the 3 dilatino-bilinear terms from $`Y L_W`$: $`11+3+3=17`$. In each of the last two BF slots, the $`\bar R(Q)R(Q)`$ and $`\bar\chi\chi`$ parts of $`L_W`$ multiply two explicit gravitinos; those four terms start at physical degree four. They contribute neither to the bosonic density nor to the quadratic fermion density. Therefore $`73-17-4=52`$ Weyl terms remain. The companion ledger's “Every discarded Weyl term” table displays all 21 actual expressions and their vanishing projections.

For example, the triplet insertion is computed without omitting either bilinear:

```math
(-2)\left(-\frac g2 L_{ij}\right)\left[\frac i4\overline{\widehat R_{ab}^{(i}(Q)}\widehat R^{j)ab}(Q)+\frac{256i}{3}\bar\chi^{(i}\chi^{j)}+\frac{16}{3}\widehat R_{ab}^{ij}(V)T^{ab}\right]=\frac{ig}{4}L_{ij}\overline{\widehat R_{ab}^{i}(Q)}\widehat R^{jab}(Q)+\frac{256ig}{3}L_{ij}\bar\chi^i\chi^j+\frac{16g}{3}L_{ij}\widehat R_{ab}^{ij}(V)T^{ab}.
\tag{GB22}
```

The two explicit-gravitino insertions need only the bosonic-degree part of that primary. Their coefficients follow directly:

```math
\left(-\frac i2\right)\frac{16}{3}=-\frac{8i}{3},\qquad \left(-\frac12\right)\frac{16}{3}=-\frac83.
\tag{GB23}
```

They multiply, respectively, $`\bar\psi_a^i\gamma^{ab}\psi_b^j\widehat R_{cd\,ij}(V)T^{cd}`$ and $`C_a\bar\psi_b^i\gamma^{abc}\psi_c^j\widehat R_{de\,ij}(V)T^{de}`$. These products remain inside the overall physical-degree projection, which removes any extra fermions supplied by their covariants.

Every other Weyl coefficient receives the same $`-2`$ and no index permutation. For example, $`(-2)(1/8)=-1/4`$ for $`\widehat C^2`$, $`(-2)(64/3)=-128/3`$ for $`D^2`$, and $`(-2)(-1/3)=2/3`$ for $`\widehat R(V)^2`$. The complete 52 multiplications, with their field expressions, are displayed in [the coefficient ledger](../ads5/code/outputs/action_coefficient_ledger.md).

### Step 5. Insert the fully expanded LOG action

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, LOG_bridge=already_applied_once -->

The current LOG action was obtained by substituting all 13 triplet, 94 spinor, 141 scalar, and 373 vector terms of STEP_07 into the seven BF insertions. The assembled input in [LOG action §4–§5](../ads5/code/inputs/action_sources/04_02_fermionic_log_action.md) contains 297 terms with no explicit physical spinor and 835 explicit bilinears. Its two stored sums are named covariant seed and explicit sum. “No explicit spinor” does not mean “bosonic”: the seed retains all hats and full derivatives.

Write these two **input sums for this step only** as $`B_{\rm cov}=\sum_{r=1}^{297}b_r\mathcal O_r`$ and $`F_{\rm explicit}=\sum_{s=1}^{835}f_s\mathcal Q_s`$. Then ordinary distributivity gives

```math
-4\ell_{\log}^{(0+2)}=\left[-4(B_{\rm cov}+F_{\rm explicit})\right]_{\le2}=\left[\sum_{r=1}^{297}(-4b_r)\mathcal O_r+\sum_{s=1}^{835}(-4f_s)\mathcal Q_s\right]_{\le2}.
\tag{GB24}
```

This equality neither reorders the covariant derivatives nor changes the bilinear order. The source coefficient and each displayed multiplication are provided for all 1,132 terms in the ledger. For its first seed term and first explicit bilinear the arithmetic is, for instance,

```math
(-4)\frac16=-\frac23,\qquad (-4)\frac{685i}{6144}=-\frac{685i}{1536}.
\tag{GB25}
```

The first multiplies $`\widehat R(V)_{ab}^{ij}\widehat R(V)^{ab}_{ij}`$. The second multiplies the unchanged source contraction $`\widehat G^{ef}\varepsilon_{abdef}\overline{\widehat R^{abi}(Q)}\gamma^{cd}\mathcal D_c\psi_i`$. The full collection is printed in §6; the sums in GB24 are not the final action.

For the **isolated fermionic** part one would take $`F_{\rm explicit}+B_{\rm cov}-B_{\rm cov}|_{\Psi=0}`$ through degree two. We are constructing the **total** action, so it is $`F_{\rm explicit}+B_{\rm cov}`$ that enters. Subtracting the bosonic seed here would incorrectly remove the bosonic GB completion.

### Step 6. Retain and expand the two-derivative input

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, bar=linear_Majorana, current=ordinary_P -->

The inherited 2016-map construction uses $`\ell_{2\partial}=-2\ell_{\rm VL}(V_{\rm linear}[L]+2gV_{\rm defining},L)`$. Linearity in the vector argument gives $`-2\ell_{\rm VL}(V_{\rm linear}[L],L)-4g\ell_{\rm VL}(V_{\rm defining},L)`$. For the second term substitute GB15 and A2, and put its ordinary-current coupling into the form representative used by the input:

```math
-4g\left[\frac12G_{\mu\nu}E^{\mu\nu}+N-\frac g2L^2+\frac12\bar\psi_a^i\gamma^a\varphi_i+\frac{iL}{4\sqrt2}\delta_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j\right]=-2gG_{\mu\nu}E^{\mu\nu}-4gN+2g^2L^2-2g\bar\psi_a^i\gamma^a\varphi_i-\frac{igL}{\sqrt2}\delta_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j.
\tag{GB26}
```

The integration by parts behind the factor $`1/2`$ can be checked directly:

```math
A_\mu\partial_\nu(eE^{\mu\nu})=\partial_\nu(eA_\mu E^{\mu\nu})-e(\partial_\nu A_\mu)E^{\mu\nu}=\partial_\nu(eA_\mu E^{\mu\nu})+\frac e2F_{\mu\nu}(A)E^{\mu\nu}.
\tag{GB27}
```

In the second equality antisymmetry of $`E^{\mu\nu}`$ gives $`-(\partial_\nu A_\mu)E^{\mu\nu}=(\partial_\mu A_\nu-\partial_\nu A_\mu)E^{\mu\nu}/2`$. The displayed divergence specifies the discarded boundary term. This is the source representative already used in the two-derivative input; no additional integration by parts is used to combine the higher-derivative densities.

For the first term, equation (5.10) of that input already inserts all vector-linear slots. Its only remaining named composite spinor occurs inside a Majorana bar. We replace that one symbol by the **entire right side of its equation (5.5)**, retaining the bar around the full sum. The final expression below therefore contains no $`\lambda_{\rm linear}`$ placeholder. The bar does not conjugate $`i`$; the full barred sum retains the source ordering of the gamma matrices and Grassmann fields.

Products containing four explicit physical fermions in this inherited presentation are harmless only because the overall $`[\ ]_{\le2}`$ is explicit. The truncation is made after the same replacement and full covariant definitions; no term can return to degree two because no further spinor differentiation is performed during this final assembly.

### Step 7. Collect the total action without changing its derivative order

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2 -->

Add the unchanged two-derivative input to the 52 Weyl and 1,132 LOG terms, multiply the latter collection by $`\lambda_{\rm GB}`$, and apply $`[\ ]_{\le2}`$ to the complete density. There are $`52+297+835=1,184`$ four-derivative outer terms before any further collecting of identical tensor structures. This count measures source entries; it is not a count of independent invariants.

The exact rational [assembly script](../ads5/code/calculations/assemble_action.py) performs only the multiplications just derived, the listed 21 Weyl removals, the explicit barred-spinor substitution, and formatting. The corresponding [JSON ledger](../ads5/code/outputs/action_coefficients.json) records input coefficient, multiplier, output coefficient, phase of $`i`$, and original tensor body for every retained higher-derivative term. The hand derivation determines the operations; the script checks and prints their complete arithmetic.

<a id="5-consistency-checks"></a>

## Consistency Checks

<a id="51-curvature-normalization"></a>

### Curvature normalization

For this normalization probe only, set $`T=G=H=g=0`$ and use the bosonic composite $`D=-R/32`$. The Weyl input gives

```math
\ell_{\rm W,OP}\big|_{\rm curv}=\frac18C_{abcd}C^{abcd}+\frac{64}{3}\frac{R^2}{1024}=\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2,\qquad \ell_{\log}\big|_{\rm curv}=-\frac16R_{ab}R^{ab}+\frac1{24}R^2.
\tag{GB28}
```

Here $`C^2=R_{\rm iem}^2-\frac43R_{\rm ic}^2+\frac16R^2`$ in five dimensions. Consequently,

```math
-2\left(\frac18,-\frac16,\frac1{24}\right)-4\left(0,-\frac16,\frac1{24}\right)=\left(-\frac14,1,-\frac14\right),\qquad \ell_{\rm GB}\big|_{\rm curv}=-\frac14\left(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2\right).
\tag{GB29}
```

This agrees with [GB-WEYLOG-DEF-v1](../ads5/code/inputs/action_sources/09_gauss_bonnet_from_weyl_log_action_lock.md), Gold et al. (2025), equations (22)–(23). This checks the normalization of the curvature sector. The complete off-shell action retains the other fields and couplings; no vacuum ansatz is imposed.

<a id="52-current-connection-and-derivative-checks"></a>

### Current, connection and derivative checks

The source Chern–Simons coefficients provide independent arithmetic:

```math
C\varepsilon RR:\quad (-2)\frac1{16}=-\frac18,\qquad C\varepsilon R(V)R(V):\quad (-2)\left(-\frac1{12}\right)+(-4)\left(-\frac1{12}\right)=\frac12,\qquad \widehat R(V)^2:\quad (-2)\left(-\frac13\right)+(-4)\frac16=0.
\tag{GB30}
```

The last cancellation removes the two displayed identical seed monomials; it does not establish absence of all connection dependence inside the other covariants.

There is a useful derivative-order check in the bosonic Weyl scalar comparison. The converted Gold expression has $`(160/3)C_{abcd}T^{ab}T^{cd}+(256/3)T_{ab}\mathcal D_c\mathcal D^aT^{cb}`$. On this bosonic check alone,

```math
T_{ab}[\mathcal D_c,\mathcal D^a]T^{cb}=-C_{acbd}T^{ab}T^{cd}=-\frac12C_{abcd}T^{ab}T^{cd},
\qquad \frac{160}{3}-\frac{256}{3}\frac12=\frac{32}{3}.
\tag{GB31}
```

For the first equality the traced curvature term vanishes by the conformal trace constraint. For the second, contract $`C_{abcd}+C_{acdb}+C_{adbc}=0`$ with $`T^{ab}T^{cd}`$: the last two terms both become $`-C_{acbd}T^{ab}T^{cd}`$, using antisymmetry and exchanging the dummy $`c,d`$. The result is the $`32/3`$ coefficient of $`-2`$ times FM04 in its original order. At two fermions the full commutator also has Q/S terms; we have not used GB31 to reorder the final action.

The quartic-$`T`$ scalar check likewise gives $`-(81/32)(16/3)^4=-2048=(-2)(1024)`$ and $`(33/128)(16/3)^4=5632/27=(-2)(-2816/27)`$. The complete bosonic current comparison, with every divergence term, is GN16 of [the normalization explanation](../ads5/code/derivations/support/gb-action-normalization-EXPLAIN.md).

<a id="53-dimensions-limits-and-verification-scope"></a>

### Dimensions, limits and verification scope

For example, $`[\bar\chi\not{\mathcal D}\chi]=3/2+1+3/2=4`$, $`[\bar R(Q)\not{\mathcal D}R(Q)]=4`$, $`[gL\bar\chi\chi]=1+0+3=4`$, and $`[C\varepsilon RR]=0+2+2=4`$. The two-derivative terms have dimension two; $`\lambda_{\rm GB}`$ converts dimension four to two. Finally $`[1/\kappa_5^2]+[d^5x]+[\ell_{\rm tot}]=3-5+2=0`$.

| Limit or check | Result and precise scope |
|---|---|
| $`\lambda_{\rm GB}=0`$ | The complete inherited two-derivative action, with the one barred composite replaced by its full definition. |
| $`g=0`$ | The explicit triplet/deformation terms vanish and the gauged covariants reduce to their ungauged definitions. The full derivatives of the gauge-fixed dilatino still survive. |
| $`\Psi=0`$ | Explicit bilinears vanish; the full covariant seed remains and gives the adopted bosonic Weyl–LOG action. |
| Curvature-only sector | GB29 agrees exactly with the anchored bosonic GB normalization. |
| Relative normalization | Complete primary matching, all density/current slots, and independent bosonic scalar/current comparisons. |
| Coefficient audit | Exact rational multiplication for all 1,184 retained higher-derivative entries; original derivative and spinor order preserved. |
| Source integrity | Eleven frozen inputs and their live originals checked against SHA-256 hashes. |

The [coefficient assembly](../ads5/code/calculations/assemble_action.py) and [independent readback report](../ads5/code/outputs/action_readback.json) give the retained reproducible coefficient checks. The 256-entry Clifford-pair identity, three nonzero spinor contractions and nonzero Weyl-commutator test are described in the [normalization derivation](../ads5/code/derivations/support/gb-action-normalization-EXPLAIN.md); that derivation states their scope. The inherited LOG dimensional/free-index audit applies unchanged to its term bodies because multiplying by $`-4`$ changes neither indices nor dimensions. The same statement applies to the retained Weyl bodies. This is not an independent new Fierz, action-reality, or full supersymmetry proof.

<a id="6-final-result"></a>

## Final Result

Under A1–A6, the action through two physical fermions is

```math
\boxed{S^{(0+2)}=\frac1{2\kappa_5^2}\int d^5x\,e\,\ell_{\rm tot}^{(0+2)},\qquad S=S^{(0+2)}+O(\Psi^4),\qquad [\lambda_{\rm GB}]=-2.}
\tag{GB-FINAL-ACTION}
```

The following is the **complete collected density**. It includes the two-derivative action and every retained Weyl/LOG term; it has no invariant-slot placeholders. Full supercovariant tensors, $`T,\chi,D`$, and ordered derivatives retain the definitions in §3 and the anchored component reference. The trailing projection is part of the formula. A source-gauge vertical bar and the overall projection are never instructions to set a differentiated dilatino to zero.

```math
\fbox{$\displaystyle{\begin{aligned}
\ell_{\mathrm{tot}}^{(0+2)}\doteq\Bigg[&-2\Bigg\{\frac{L}{\sqrt2}\delta^{ij}\Bigg[L^{-1}\square^C\left(\frac{L}{\sqrt2}\delta_{ij}\right)-\frac1{\sqrt2}L^{-2}\delta^{km}\mathcal D_aL_{k(i}\big|_{\mathrm P}\mathcal D^aL_{j)m}\big|_{\mathrm P}-\frac1{\sqrt2}L^{-2}\delta_{ij}N^2-\frac1{\sqrt2}L^{-2}\delta_{ij}E_aE^a\\
&+\sqrt2L^{-2}E_a\delta_{k(i}\mathcal D^aL_{j)}{}^k\big|_{\mathrm P}+\frac1{24\sqrt2}\delta_{ij}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\left(\widehat G^{ab}+\frac16\varepsilon^{abfgh}\widehat H_{fgh}\right)+2\sqrt2\delta_{ij}D\big|_{\mathrm P}\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl}\bar\varphi_k\varphi_l+\frac32L^{-3}\delta_{ij}\delta^{kl}\bar\varphi_k\not E\varphi_l-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}-16iL^{-1}\bar\chi_{(i}\big|_{\mathrm P}\varphi_{j)}\\
&+8iL^{-1}\delta_{ij}\delta_{kl}\bar\chi^k\big|_{\mathrm P}\varphi^l+\sqrt2L^{-2}\delta_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}\big|_{\mathrm P}-\frac32L^{-3}\delta_{k(i}\delta^{lm}\bar\varphi^k\not{\mathcal D}L_{j)l}\big|_{\mathrm P}\varphi_m+\frac12L^{-3}\bar\varphi^l\not{\mathcal D}L_{l(i}\big|_{\mathrm P}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m\not{\mathcal D}L_{ij}\big|_{\mathrm P}\varphi_m+\frac{i}{4\sqrt2}L^{-2}\delta_{ij}\bar\varphi\gamma^{ab}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\varphi\Bigg]+i\left[\overline{\left(\varepsilon^{ir}\Bigg\{-2iL^{-1}\gamma^\mu\mathcal D_\mu\varphi_r\big|_{\mathrm P}+i\sqrt2\delta_{rs}\gamma^\mu\Bigg[\Bigg(\frac14\gamma^{ab}\widehat G_{ab}-\frac18\gamma^{ab}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\Bigg)\psi_\mu{}^s-\phi_\mu{}^s-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}\Bigg]+\frac1{2L}\gamma^{ab}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\varphi_r-\sqrt2NL^{-2}\delta_{rs}\varphi^s+2iL^{-3}\left[\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)\frac{L}{\sqrt2}\delta^{st}\varphi_t-\frac{L}{\sqrt2}\delta_{rs}\not E\varphi^s\right]+\sqrt2g\delta_{rs}\varphi^s\Bigg\}\right)}\varphi_i\right]\\
&-\frac{L}{2\sqrt2}\delta_{ij}\bar\psi_a{}^i\gamma^a\varepsilon^{jr}\Bigg[-2iL^{-1}\gamma^\mu\mathcal D_\mu\varphi_r\big|_{\mathrm P}+i\sqrt2\delta_{rs}\gamma^\mu\Bigg\{\Bigg[\frac14\gamma^{bc}\widehat G_{bc}-\frac18\gamma^{bc}\left(\widehat G_{bc}+\frac16\varepsilon_{bcdef}\widehat H^{def}\right)\Bigg]\psi_\mu{}^s\\
&-\phi_\mu{}^s-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}\Bigg\}+\frac1{2L}\gamma^{bc}\left(\widehat G_{bc}+\frac16\varepsilon_{bcdef}\widehat H^{def}\right)\varphi_r-\sqrt2NL^{-2}\delta_{rs}\varphi^s+2iL^{-3}\Bigg[\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)\frac{L}{\sqrt2}\delta^{st}\varphi_t\\
&-\frac{L}{\sqrt2}\delta_{rs}\not E\varphi^s\Bigg]+\sqrt2g\delta_{rs}\varphi^s\Bigg]+\frac12E^{\mu\nu}\Bigg[4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)+\sqrt2\delta_{ij}\widehat R_{\mu\nu}{}^{ij}(V)+\sqrt2L^{-2}\delta_{km}\varepsilon^{m\ell}\mathcal D_{[\mu}L^{kp}\big|_{\mathrm P}\mathcal D_{\nu]}L_{\ell p}\big|_{\mathrm P}\\
&-\sqrt2\mathcal D_{[\mu}\left(L^{-2}\delta_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j\right)-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)+\bar\psi_{[\mu}{}^i\gamma_{\nu]}\Bigg\{-2iL^{-1}\gamma^\rho\mathcal D_\rho\varphi_i\big|_{\mathrm P}+i\sqrt2\delta_{ij}\gamma^\rho\Bigg[\Bigg(\frac14\gamma^{ab}\widehat G_{ab}\\
&-\frac18\gamma^{ab}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\Bigg)\psi_\rho{}^j-\phi_\rho{}^j-\frac{gL}{2\sqrt2}\delta^{jk}\psi_{\rho k}\Bigg]+\frac1{2L}\gamma^{ab}\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)\varphi_i\\
&-\sqrt2NL^{-2}\delta_{ij}\varphi^j+2iL^{-3}\Bigg[\left(\not{\mathcal D}L_{ij}\big|_{\mathrm P}\right)\frac{L}{\sqrt2}\delta^{jk}\varphi_k-\frac{L}{\sqrt2}\delta_{ij}\not E\varphi^j\Bigg]+\sqrt2g\delta_{ij}\varphi^j\Bigg\}-iL^{-1}N\bar\psi_{[\mu}{}^i\psi_{\nu]i}\Bigg]\\
&+\left(2L^{-1}N+\frac{i}{\sqrt2}L^{-2}\delta_{ij}\bar\varphi^i\varphi^j\right)\times\left(N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i+\frac{iL}{4\sqrt2}\delta_{ij}\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\right)\Bigg\}-4g\Bigg\{\frac12G_{\mu\nu}E^{\mu\nu}+N-\frac g2L^2\\
&+\frac12\bar\psi_a{}^i\gamma^a\varphi_i+\frac{iL}{4\sqrt2}\delta_{ij}\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\Bigg\}\\[3pt]
&+\lambda_{\mathrm{GB}}\Bigg(-\frac{1}{4}\widehat C_{abcd}\widehat C^{abcd} -\frac{128}{3}D^2\\
&-\frac{2048}{9}DT_{ab}T^{ab} +\frac{32}{3}\widehat C_{abcd}T^{ab}T^{cd}\\
&+\frac{2}{3}\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V) +\frac{128}{3}(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\\
&-\frac{128}{3}(\mathcal D_bT_{ac})(\mathcal D^aT^{bc}) +\frac{256}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&+\frac{256}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef} -2048T_{ab}T^{bc}T_{cd}T^{da}\\
&+\frac{5632}{27}(T_{ab}T^{ab})^2 -\frac{3}{2}\overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
&+4iT^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q) +\frac{320i}{3}T^{ab}\overline{\widehat R_{ab}(Q)}\chi\\
&+\frac{512}{3}\bar\chi\gamma^a\mathcal D_a\chi -\frac{1}{8}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}\\
&+\frac{1}{6}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij} -2C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]\\
&+64C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big] +2C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d\\
&-6C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d -32C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi\\
&-\frac{32}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi -iC_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}\\
&-3iC_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da} +\frac{1}{8}\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}\\
&+4i\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc} -\frac{128}{3}\bar\psi_m\gamma^m\chi D\\
&-8i\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab} -8i\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}\\
&+\frac{64i}{3}\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc} -\frac{1024}{9}\bar\psi_m\gamma^m\chi T^2\\
&-\frac{128i}{3}\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab} -\frac{8}{3}\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}\\
&-\frac{1}{2}\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q) +\frac{8}{3}\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j\\
&+\frac{i}{8}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd} -4C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
&-\frac{128i}{3}C_m\bar\psi_n\gamma^{nm}\chi D +8C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
&+8C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab} -\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
&-\frac{1024i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2 +\frac{128}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}\\
&-\frac{8i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd} -\frac{i}{2}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
&+\frac{8i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j +\frac{i}{4}gL^{ij}\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\\
&+\frac{256i}{3}gL^{ij}\bar\chi_{(i}\chi_{j)} +\frac{16}{3}gL^{ij}\widehat R_{ab\,ij}(V)T^{ab}\\
&-\frac{8i}{3}(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big) -\frac{8}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
&-\frac{2}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j} -\frac{17}{36}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&-\frac{23}{18}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}_{b}{}^{c}{}^{d}\widehat G{}_{c}{}_{d} +\frac{22}{9}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{b}{}_{c}{}_{d}\\
&-\frac{11}{18}\widehat C{}^{a}{}^{b}{}^{c}{}^{d}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d} -\frac{17}{9}\widehat H{}^{a}{}^{b}\widehat C{}_{a}{}^{c}{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+\frac{20}{9}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{a}{}_{c}{}_{b}{}_{d} -\frac{1}{4}(\widehat G^2)^{2}\\
&+4\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\widehat G^2 -4\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat G^2\\
&-\frac{16}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d} +8\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\widehat H{}^{c}{}^{d}\widehat H{}_{c}{}_{d}\\
&-\frac{1}{3}\widehat G{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} -\frac{4}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{863}{288}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} +\frac{1129}{144}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} -\frac{16}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{16}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\big(\Box^c\sigma\big) -\frac{3}{2}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\widehat G^2\\
&+\frac{4}{3}g^{2}\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}L{}_{i}{}_{j}\widehat G{}_{a}{}_{b} +4g^{2}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L{}^{i}{}^{j}L{}_{i}{}_{j}\\
&-2Ng\widehat G^2 +\frac{16}{3}Ng\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\\
&-8Ng\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b} +\frac{3}{8}\big(\mathcal D^{a}\widehat C{}_{a}{}^{b}{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{3}{2}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{c}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{1}{4}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{4}\big(\mathcal D^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{16}{3}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{8}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big) +\frac{112}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&-\frac{112}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}_{a}{}_{c} -\frac{112}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{32}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat G{}_{b}{}_{c}\big) +\frac{32}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{128}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D^{c}\widehat H{}_{b}{}_{c}\big) -\frac{4}{3}\widehat G{}^{a}{}^{b}\big(\Box^c\widehat G{}_{a}{}_{b}\big)\\
&-\frac{16}{3}\widehat H{}^{a}{}^{b}\big(\Box^c\widehat G{}_{a}{}_{b}\big) -\frac{4}{9}\widehat G{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{9}\big(\mathcal D^{a}\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\widehat G{}_{b}{}_{c} -\frac{16}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&+\frac{32}{9}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\mathcal D_{a}\widehat H{}_{b}{}_{c}\big) -\frac{10}{3}\big(\Box^c\sigma\big)\big(\Box^c\sigma\big)\\
&-\frac{26}{3}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\big(\Box^c\sigma\big) -\frac{32}{3}Ng\big(\Box^c\sigma\big)\\
&-\frac{7}{12}g^{4}L{}^{i}{}^{j}L{}_{i}{}_{j}L{}^{k}{}^{l}L{}_{k}{}_{l} -\frac{8}{3}Ng^{3}L{}^{i}{}^{j}L{}_{i}{}_{j}\\
&+\frac{2}{3}NNg^{2} -\frac{10}{3}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\\
&+\frac{28}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big) -\frac{16}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\widehat H{}_{a}{}_{c}\big)\\
&+\frac{4}{3}\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big) -\frac{22}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\\
&-\frac{8}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{a}\widehat H{}_{b}{}_{c}\big) +8\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\\
&-16\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\big(\mathcal D^{c}\widehat H{}_{b}{}_{c}\big) +\frac{4}{3}gL{}^{i}{}^{j}\widehat R(V){}^{a}{}^{b}{}_{i}{}_{j}\widehat G{}_{a}{}_{b}\\
&+\frac{1163}{288}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{563}{144}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{269}{144}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{139}{72}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{3}{4}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} -\frac{19}{6}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{353}{144}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{89}{72}\widehat H{}^{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{16}\widehat H{}^{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{25}{8}\widehat H{}^{a}{}^{b}\big(\mathcal D_{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+2g^{2}L{}^{i}{}^{j}\big(\Box^cL{}_{i}{}_{j}\big) +3\big(\mathcal D^{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-6\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e} +6\big(\mathcal D^{a}\mathcal D^{b}\sigma\big)\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\\
&+3g^{2}\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\big(\mathcal D_{a}L{}_{i}{}_{j}\big) +4g\big(\Box^cN\big)\\
&+\frac{3}{2}\widehat G{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d} -8\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d}\\
&+16\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d} -\frac{1}{2}g^{4}L{}^{i}{}^{j}L{}_{i}{}^{k}L{}_{j}{}^{l}L{}_{k}{}_{l}\\
&-\frac{8}{3}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j} +\frac{1}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat R(V){}^{d}{}^{e}{}_{i}{}_{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{1}{32}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{a}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{3}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{a}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{21}{16}C{}^{a}\widehat H{}_{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{5}{4}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{25}{192}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{a}{}_{b}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{11}{24}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{a}{}_{d}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{31}{96}C{}^{a}\widehat H{}_{a}{}^{b}\widehat C{}_{b}{}^{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{37}{24}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat C{}_{b}{}^{e}{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1}{48}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{a}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g} +\frac{5}{48}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{7}{48}C{}^{a}\widehat H{}_{a}{}^{b}\widehat C{}^{c}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{6}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{41}{144}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{29}{72}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{f}{}_{g}\\
&-\frac{53}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{d}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{31}{288}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{59}{72}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{g} +\frac{161}{144}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{19}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}^{f}{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{1}{288}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{23}{288}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{d}{}_{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{23}{288}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}_{c}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{25}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{c}{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{43}{144}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{29}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{149}{72}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{5}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat C{}_{c}{}^{e}{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{35}{576}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&-\frac{59}{288}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{11}{72}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat C{}^{d}{}^{e}{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{5}{144}C{}^{a}\widehat C{}^{b}{}^{c}{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{29}{72}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{b}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{19}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat C{}_{b}{}_{d}{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{86015}{20736}C{}^{a}\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{98689}{10368}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} +\frac{23027}{5184}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{a}{}^{f}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\\
&-\frac{2243}{10368}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{b}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{6947}{1296}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{34427}{10368}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{4385}{5184}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1801}{1296}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{44159}{2592}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{13625}{648}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{551}{2592}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{889}{648}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\widehat G{}_{d}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g} -\frac{26779}{5184}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&+\frac{23027}{10368}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2 +\frac{19823}{2592}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{d}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{21275}{1296}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{d}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{125}{5184}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1181}{2592}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{4385}{10368}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{12205}{1296}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{488}{81}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{1270}{81}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\widehat H{}_{c}{}^{e}\widehat H{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{551}{10368}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\\
&+\frac{889}{1296}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2 +\frac{1237}{1296}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{1513}{324}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{3209}{648}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\widehat G{}_{b}{}_{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{244}{81}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g} -\frac{635}{162}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\widehat H{}^{d}{}^{e}\widehat H{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{2}{3}C{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\widehat G^2 +\frac{8}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)\widehat G^2\\
&-8C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}_{a}{}_{d}\big) +\frac{8}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat G{}_{a}{}_{d}\big)\\
&+\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\big(\mathcal D^{d}\widehat H{}_{a}{}_{d}\big) -\frac{8}{3}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}_{a}{}_{d}\big)\\
&-\frac{8}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\widehat G{}_{b}{}^{d}\widehat G{}_{c}{}_{d} +\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{d}\widehat G{}_{a}{}_{c}\big)\\
&+\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{a}{}_{b}\big)\widehat G{}_{c}{}_{d} -\frac{64}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}_{a}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&-\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat G{}_{a}{}_{d}\big) -\frac{128}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\big(\mathcal D_{c}\widehat H{}_{a}{}_{d}\big)\\
&+\frac{8}{3}C{}^{a}\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big) +\frac{8}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\widehat G{}_{a}{}^{d}\widehat G{}_{c}{}_{d}\\
&-\frac{40}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{b}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big) -\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{d}\big)\widehat G{}_{a}{}_{c}\\
&+\frac{8}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big) +\frac{64}{3}C{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}_{b}{}_{d}\\
&+\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big) +\frac{128}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{c}{}_{d}\big)\\
&-\frac{28}{3}C{}^{a}\widehat G{}_{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big) +\frac{40}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\\
&-8C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big) +\frac{32}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\widehat H{}_{c}{}^{d}\big)\widehat G{}_{a}{}_{d}\\
&+\frac{16}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big) -\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&+\frac{80}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat G{}_{b}{}_{d}\big) -\frac{128}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{c}\widehat H{}_{b}{}_{d}\big)\\
&+\frac{14}{3}C{}^{a}\widehat G{}_{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big) -8C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\\
&-\frac{40}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\big(\mathcal D_{d}\widehat G{}_{b}{}_{c}\big) +\frac{16}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat H{}_{b}{}_{c}\big)\widehat G{}_{a}{}_{d}\\
&+\frac{4}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big) -\frac{8}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\\
&+\frac{64}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\big(\mathcal D_{b}\widehat H{}_{c}{}_{d}\big) +C{}^{a}\big(\mathcal D^{b}\widehat C{}_{a}{}^{c}{}_{b}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&-4C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}_{a}{}_{b}{}_{c}{}_{d}\big) +\frac{1}{2}C{}^{a}\big(\mathcal D^{b}\widehat C{}_{a}{}_{b}{}^{c}{}^{d}\big)\widehat G{}_{c}{}_{d}\\
&+2C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\widehat C{}_{a}{}_{d}{}_{b}{}_{c}\big) +\frac{14}{9}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{7}{18}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{7}{36}C{}^{a}\widehat G{}_{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{52}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{25}{18}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{257}{36}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{91}{36}C{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{74}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{14}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\mathcal D_{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{55}{18}C{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D^{c}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{7}{6}C{}^{a}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&+\frac{1}{9}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{11}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{d}\mathcal D^{f}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{5}{9}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{149}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{b}\mathcal D^{f}\sigma\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{37}{36}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{20}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\big(\Box^c\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{25}{18}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1}{2}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{43}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{5}{3}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{d}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{5}{2}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{11}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{b}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{1}{3}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +2C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{a}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{10}{3}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +4C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{25}{36}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{25}{18}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{b}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{22}{9}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{d}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} -\frac{44}{9}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{d}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&+\frac{5}{72}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{13}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D_{a}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{19}{36}C{}^{a}\big(\mathcal D_{a}\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{8}{9}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{4}{9}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{5}{36}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&+\frac{371}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\sigma\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{55}{18}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}_{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{65}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} +\frac{7}{18}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{67}{9}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\widehat H{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f} -\frac{23}{72}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{43}{12}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{a}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{11}{36}C{}^{a}\big(\mathcal D^{b}\mathcal D_{a}\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{13}{36}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{25}{18}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{a}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{5}{18}C{}^{a}\widehat G{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{2}{9}C{}^{a}\big(\mathcal D^{b}\mathcal D^{c}\widehat H{}^{d}{}^{e}\big)\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{43}{36}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{55}{18}C{}^{a}\widehat H{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{7}{12}C{}^{a}\widehat G{}^{b}{}^{c}\big(\Box^c\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} +\frac{23}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\big(\Box^c\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\\
&-\frac{5}{6}C{}^{a}\big(\Box^c\widehat H{}^{c}{}^{d}\big)\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{17}{12}C{}^{a}\widehat H{}^{b}{}^{c}\big(\Box^c\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\\
&-\frac{11}{6}C{}^{a}\widehat H{}^{b}{}^{c}\big(\Box^c\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f} +\frac{4}{3}C{}^{a}\widehat G{}_{a}{}^{b}\big(\mathcal D_{b}\Box^c\sigma\big)\\
&+\frac{16}{3}C{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D_{b}\Box^c\sigma\big) +\frac{16}{3}g^{2}C{}^{a}L{}^{i}{}^{j}\big(\mathcal D^{b}L{}_{i}{}_{j}\big)\widehat G{}_{a}{}_{b}\\
&-\frac{8}{3}g^{2}C{}^{a}\widehat H{}_{a}{}^{b}L{}^{i}{}^{j}\big(\mathcal D_{b}L{}_{i}{}_{j}\big) +\frac{20}{3}gC{}^{a}\big(\mathcal D^{b}N\big)\widehat G{}_{a}{}_{b}\\
&-\frac{16}{3}gC{}^{a}\widehat H{}_{a}{}^{b}\big(\mathcal D_{b}N\big) +\frac{8}{3}C{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\big(\Box^c\sigma\big)\\
&-\frac{40}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)\big(\Box^c\sigma\big) +\frac{8}{3}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\\
&-\frac{4}{3}g^{2}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)L{}^{i}{}^{j}L{}_{i}{}_{j} +\frac{20}{3}NgC{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\\
&-\frac{16}{3}NgC{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big) -\frac{113}{384}C{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{881}{192}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{a}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1199}{192}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{431}{96}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{1105}{384}C{}^{a}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&+\frac{401}{192}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{b}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{1265}{192}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{187}{32}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{c}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{1039}{192}C{}^{a}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{245}{16}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{c}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f} +\frac{431}{48}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat H{}_{c}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\\
&-\frac{175}{128}C{}^{a}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{17}{64}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\\
&-\frac{49}{64}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{241}{32}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{415}{384}C{}^{a}\big(\mathcal D_{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{415}{192}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{a}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{191}{192}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f} +\frac{191}{96}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D^{d}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\\
&+\frac{353}{384}C{}^{a}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -\frac{59}{32}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\\
&-\frac{191}{96}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\big(\mathcal D_{b}\widehat H{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f} -4gC{}^{a}L{}^{i}{}^{j}\big(\mathcal D^{b}\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j}\big)\\
&-4gC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\widehat R(V){}_{a}{}_{b}{}_{i}{}_{j} +\frac{31}{48}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\\
&+\frac{1}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +\frac{11}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{a}{}^{d}{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&+\frac{25}{16}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{a}{}^{d}{}^{e}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g} -\frac{1}{16}C{}^{a}\widehat H{}^{b}{}^{c}\widehat C{}_{a}{}_{b}{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{63}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\widehat G{}_{b}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g} +37C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\widehat H{}^{e}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\\
&-\frac{8}{3}C{}^{a}\widehat G{}_{a}{}^{b}\big(\Box^c\mathcal D_{b}\sigma\big) -2C{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&-\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\big(\Box^c\mathcal D_{b}\sigma\big) -20C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+8C{}^{a}\big(\Box^c\mathcal D^{c}\widehat H{}_{a}{}_{c}\big) -2C{}^{a}\big(\mathcal D^{b}\widehat G{}_{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\\
&+4C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{b}\sigma\big) +5C{}^{a}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{a}\sigma\big)\\
&-10C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D_{c}\mathcal D_{a}\sigma\big) -C{}^{a}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\big(\mathcal D_{a}\mathcal D_{c}\sigma\big)\\
&+2C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\big(\mathcal D_{a}\mathcal D_{c}\sigma\big) -2C{}^{a}\big(\mathcal D_{a}\widehat G{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\\
&+4C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\big(\mathcal D_{b}\mathcal D_{c}\sigma\big) +\frac{89}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\widehat G{}_{b}{}^{f}\widehat G{}_{d}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\\
&-\frac{8}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{d}\big(\mathcal D_{a}\widehat G{}_{c}{}_{d}\big) -\frac{685i}{1536}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2125i}{4608}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big) -\frac{379i}{768}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{1211i}{2304}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{2651}{4608}g\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi{}_{i}\\
&+\frac{541}{2304}g\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\varphi{}_{i} +\frac{607i}{4608}\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{289}{144}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{65i}{2304}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{11}{36}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{859i}{2304}g\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\varphi{}_{i}\\
&-\frac{6173i}{1152}g\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\varphi{}_{i} +\frac{209}{2304}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{8167}{1152}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{1}{2}\widehat G{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+i\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{i}{3}\widehat G{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+6i\widehat G{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{1}{3}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{2i}{3}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{10i}{3}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{8i}{3}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big) +ig\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+2g\widehat G{}_{a}{}^{b}\overline{\varphi{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{19i}{6}g\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{2}{3}g\widehat H{}^{a}{}^{b}\overline{\varphi{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{3i}{2}g^{2}\widehat G{}_{a}{}_{b}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\varphi{}_{i}\\
&-3ig^{2}\widehat H{}^{a}{}^{b}\overline{\varphi{}^{i}}\gamma{}_{a}{}_{b}\varphi{}_{i} +\frac{81i}{64}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{111}{128}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{153i}{256}g\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&+\frac{i}{3}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big) -\frac{10}{3}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{a}\big(\Box^c\psi{}_{i}\big)\\
&+\frac{2}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big) +\frac{16}{3}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big)\\
&-3igL{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\psi{}_{i}\big)}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big) -12igL{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\psi{}_{i}\big)}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-\frac{10i}{3}g\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{26i}{3}g\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{10i}{3}g\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big) +\frac{10i}{3}g\overline{\varphi{}^{i}}\big(\Box^c\psi{}_{i}\big)\\
&-\frac{35}{3}g^{2}L{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{j}\big) -\frac{2}{3}g^{2}\overline{\varphi{}^{i}}\gamma{}_{a}\big(\mathcal D^{a}\varphi{}_{i}\big)\\
&+\frac{19i}{16}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\widehat R(Q){}_{a}{}^{c}{}_{i} +\frac{19i}{4}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&-\frac{15}{128}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{i} -\frac{15}{32}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{3}{64}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{a}{}^{c}{}_{i} -\frac{3}{16}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{f}\widehat R(Q){}_{c}{}^{e}{}_{i}\\
&+\frac{9i}{256}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\widehat R(Q){}_{a}{}_{b}{}_{i} +\frac{9i}{64}\widehat H{}^{a}{}^{b}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&-\frac{355i}{576}gL{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big) -\frac{131i}{288}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{95i}{144}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{4999i}{9216}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{3271i}{4608}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{117i}{512}\widehat G{}_{c}{}^{e}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{69i}{256}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{i}{16}g\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{c}\varphi{}_{i}\big)\\
&+\frac{i}{256}gL{}^{i}{}^{j}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\widehat R(Q){}_{a}{}_{b}{}_{j} -\frac{1}{512}gL{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{e}\widehat R(Q){}^{c}{}^{d}{}_{j}\\
&+\frac{17i}{3}g^{3}L{}^{i}{}^{j}\overline{\varphi{}_{i}}\varphi{}_{j} +\frac{803}{4608}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{539}{2304}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{f}\psi{}_{i}\big) -\frac{919i}{4608}gC{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\varphi{}_{i}\\
&+\frac{655i}{2304}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\varphi{}_{i} +\frac{2269i}{2304}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{2047i}{384}C{}^{a}\widehat G{}_{b}{}^{c}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{181}{768}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{473i}{192}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{3731i}{1152}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{115}{384}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{719i}{4608}gC{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\varphi{}_{i}\\
&-\frac{889i}{2304}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i} -\frac{4685i}{2304}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{425i}{576}C{}^{a}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{401}{576}C{}^{a}\widehat G{}_{b}{}^{e}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{3691i}{1152}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{305i}{288}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{1469}{288}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{2071i}{4608}gC{}^{a}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&-\frac{5191i}{2304}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i} -\frac{2129i}{576}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{151i}{288}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{2341}{576}gC{}^{a}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}\varphi{}_{i}\\
&+\frac{241}{288}gC{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}_{c}\varphi{}_{i} -\frac{719i}{768}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{929i}{384}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{1099}{2304}gC{}^{a}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}\varphi{}_{i}\\
&-\frac{6509}{1152}gC{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}_{a}\varphi{}_{i} +\frac{505i}{288}C{}^{a}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{313}{384}C{}^{a}\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{839i}{144}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{319}{192}C{}^{a}\widehat H{}_{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{2645i}{9216}gC{}^{a}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&-\frac{5083i}{4608}gC{}^{a}\widehat H{}_{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\varphi{}_{i} +\frac{197i}{192}C{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{49i}{48}C{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big) -\frac{67}{64}gC{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\varphi{}_{i}\\
&-\frac{209i}{192}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{167}{96}C{}^{a}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{221i}{32}gC{}^{a}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\varphi{}_{i} +\frac{217i}{192}C{}^{a}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{283}{192}C{}^{a}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{173}{64}C{}^{a}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{257i}{384}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) +2C{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&+6iC{}^{a}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{a}\psi{}_{i}\big) -2iC{}^{a}\overline{\big(\mathcal D^{c}\psi{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2i}{3}C{}^{a}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}{}^{b}\big(\Box^c\psi{}_{i}\big) +10iC{}^{a}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big)\\
&-2iC{}^{a}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big) -\frac{14i}{3}C{}^{a}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\big(\Box^c\psi{}_{i}\big)\\
&+\frac{14i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{25i}{12}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{22}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{2}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{23i}{8}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big) -\frac{23i}{8}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{16}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{i}{3}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}_{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{4}{3}gC{}^{a}L{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\psi{}_{i}\big)}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{4}{3}gC{}^{a}L{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\psi{}_{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{i}{3}gC{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{2}{3}gC{}^{a}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}_{b}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{14}{3}gC{}^{a}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big) -igC{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&+2gC{}^{a}\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{i}\big) -\frac{2}{3}gC{}^{a}\overline{\varphi{}^{i}}\gamma{}_{a}\big(\Box^c\psi{}_{i}\big)\\
&+\frac{23}{3}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{10i}{3}gC{}^{a}\widehat H{}_{a}{}^{b}\overline{\varphi{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{10i}{3}gC{}^{a}\widehat H{}^{b}{}^{c}\overline{\varphi{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) -2igC{}^{a}\widehat H{}_{a}{}^{b}\overline{\varphi{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{11i}{3}g^{2}C{}^{a}L{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{10i}{3}g^{2}C{}^{a}\overline{\varphi{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D^{b}\varphi{}_{i}\big)\\
&-\frac{5i}{12}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{7i}{12}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{29i}{12}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D_{d}\psi{}^{i}\big)}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{5i}{24}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{a}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{65}{64}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}\widehat R(Q){}_{b}{}^{d}{}_{i} +\frac{65}{16}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}\widehat R(Q){}_{c}{}_{d}{}_{i}\\
&+\frac{11i}{128}C{}^{a}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{11i}{32}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{13i}{64}C{}^{a}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}^{d}{}^{e}{}_{i} -\frac{13i}{16}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{35i}{512}C{}^{a}\widehat G{}_{b}{}_{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{35i}{128}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{7i}{128}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\widehat R(Q){}^{c}{}^{d}{}_{i} -\frac{7i}{32}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\widehat R(Q){}^{e}{}^{f}{}_{i}\\
&+\frac{23i}{128}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\widehat R(Q){}_{b}{}^{d}{}_{i} +\frac{23i}{32}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\widehat R(Q){}_{d}{}^{f}{}_{i}\\
&+\frac{5i}{24}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{f}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\psi{}_{i}\big) -\frac{19i}{256}C{}^{a}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&-\frac{19i}{64}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} +\frac{3i}{32}C{}^{a}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{i}\\
&+\frac{3i}{8}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i} +\frac{7i}{256}C{}^{a}\widehat G{}_{a}{}_{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{7i}{64}C{}^{a}\widehat H{}_{a}{}^{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i} -\frac{i}{64}C{}^{a}\widehat G{}_{b}{}_{d}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{16}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{c}{}^{e}{}_{i} -\frac{i}{32}C{}^{a}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&-\frac{i}{8}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}^{e}{}_{i} +\frac{3}{8}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{d}\widehat R(Q){}_{b}{}^{c}{}_{i}\\
&-\frac{3}{2}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{c}\widehat R(Q){}_{b}{}_{d}{}_{i} -\frac{5i}{256}C{}^{a}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\widehat R(Q){}_{b}{}_{c}{}_{i}\\
&-\frac{5i}{64}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}_{d}{}_{e}{}_{i} +\frac{i}{128}C{}^{a}\widehat G{}_{b}{}_{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{i}{32}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i} -\frac{i}{256}C{}^{a}\widehat G{}_{a}{}_{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{64}C{}^{a}\widehat H{}_{a}{}^{b}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i} +\frac{7i}{256}C{}^{a}\widehat G{}_{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{f}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&+\frac{7i}{64}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}{}_{b}\widehat R(Q){}^{f}{}^{g}{}_{i} -\frac{i}{512}C{}^{a}\widehat G{}_{f}{}_{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{f}{}^{g}\widehat R(Q){}^{d}{}^{e}{}_{i}\\
&-\frac{i}{128}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}_{c}\widehat R(Q){}^{f}{}^{g}{}_{i} +\frac{3i}{128}C{}^{a}\widehat G{}_{e}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{i}\\
&+\frac{3i}{32}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{g}\widehat R(Q){}^{e}{}^{f}{}_{i} -3C{}^{a}\widehat G{}_{a}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{22i}{3}gC{}^{a}\widehat G{}_{a}{}^{b}\overline{\varphi{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{433}{1152}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{83}{96}C{}^{a}\widehat G{}_{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{503}{576}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5}{48}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{461i}{512}gC{}^{a}\widehat G{}_{d}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\varphi{}_{i}\\
&+\frac{77i}{256}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}^{f}\varphi{}_{i} -\frac{1}{6}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{107}{2304}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{49}{48}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{469}{1152}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{5i}{64}gC{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\varphi{}_{i}\\
&+\frac{27i}{32}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}{}^{f}\varphi{}_{i} -\frac{16i}{3}C{}^{a}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{16i}{3}C{}^{a}\overline{\big(\mathcal D^{b}\psi{}^{i}\big)}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big) +4gC{}^{a}\overline{\big(\mathcal D_{a}\varphi{}^{i}\big)}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-iC{}^{a}\widehat G{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\psi{}^{i}\big)}\big(\mathcal D^{e}\psi{}_{i}\big) -gC{}^{a}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{211i}{36}gC{}^{a}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{a}{}^{b}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{103}{72}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{499i}{576}g^{2}C{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}{}^{e}\varphi{}_{j} -\frac{259}{1152}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{533}{576}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{437i}{384}C{}^{a}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{39i}{256}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{95i}{192}C{}^{a}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{13i}{32}C{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\Box^c\psi{}_{i}\big) -\frac{35i}{384}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{a}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{4}C{}^{a}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{b}\psi{}_{i}\big) +\frac{i}{8}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{4}{3}gC{}^{a}\overline{\varphi{}^{i}}\gamma{}^{b}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{i}\big) +\frac{i}{8}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{16}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{a}\psi{}_{i}\big) +\frac{i}{16}C{}^{a}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{a}\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{4}C{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big) -\frac{3}{8}gC{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{e}\big(\mathcal D^{d}\varphi{}_{i}\big)\\
&-\frac{13i}{4}gC{}^{a}\overline{\widehat R(Q){}_{a}{}^{b}{}^{i}}\big(\mathcal D_{b}\varphi{}_{i}\big) -\frac{23i}{768}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}_{b}{}^{d}{}_{j}\\
&+\frac{17}{256}gC{}^{a}L{}^{i}{}^{j}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}_{a}\widehat R(Q){}_{b}{}_{c}{}_{j} +\frac{5i}{1536}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\widehat R(Q){}^{d}{}^{e}{}_{j}\\
&+\frac{i}{48}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{b}{}_{i}}\gamma{}^{e}{}^{f}\widehat R(Q){}^{c}{}^{d}{}_{j} +C{}^{a}\widehat G{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\psi{}^{i}\big)}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{4i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big) +\frac{2i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&-\frac{2}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big) +\frac{2i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{2i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}_{a}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big) +\frac{i}{3}g\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}_{i}}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{j}\\
&-\frac{4}{3}g\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}_{a}\psi{}_{b}{}_{j} +\frac{i}{144}\widehat G{}_{a}{}_{b}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{i}\\
&-\frac{1}{36}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\psi{}^{d}{}_{i} +\frac{i}{36}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\varepsilon{}_{a}{}_{b}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{1}{9}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{a}\psi{}_{b}{}_{i} -\frac{7i}{72}\widehat H{}^{a}{}^{b}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{i}\\
&+\frac{7}{18}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{c}\psi{}^{d}{}_{i} -\frac{7i}{18}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i}\\
&+\frac{14}{9}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}_{c}\psi{}_{d}{}_{i} +\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\overline{\psi{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{1}{2}g\widehat G^2\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}_{a}{}_{i}\\
&-\frac{4}{3}g\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{b}\overline{\varphi{}^{i}}\gamma{}^{c}\psi{}_{c}{}_{i} +5g\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}\overline{\varphi{}^{i}}\gamma{}^{c}\psi{}_{c}{}_{i}\\
&-\frac{5i}{8}\widehat G{}_{b}{}_{c}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}^{d}\psi{}_{d}{}_{i} -\frac{7i}{8}\widehat G{}_{b}{}_{c}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\psi{}_{a}{}_{i}\\
&-\frac{5i}{2}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\gamma{}_{c}{}^{d}\psi{}_{d}{}_{i} -\frac{7i}{2}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\psi{}_{c}{}_{i}\\
&+2\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}\psi{}_{d}{}_{i} -\frac{i}{24}\widehat G{}_{a}{}^{f}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{i}\\
&+\frac{1}{6}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{a}{}^{b}{}^{i}}\gamma{}^{c}\psi{}^{d}{}_{i} +\frac{i}{12}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}^{f}{}_{i}\\
&-\frac{1}{6}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}\psi{}_{b}{}_{i} +\frac{1}{6}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}_{b}\psi{}^{d}{}_{i}\\
&+\frac{i}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}_{c}{}^{i}}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i} -\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{a}{}_{c}{}^{i}}\gamma{}_{b}\psi{}_{d}{}_{i}\\
&+\frac{3i}{2}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) -3i\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{3}{8}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{3}{8}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{1}{8}\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}\big(\mathcal D^{f}\psi{}_{i}\big) -2i\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\psi{}_{a}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{8i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big) -4i\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big) +\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{16i}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{32i}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{e}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-\frac{4}{3}\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{f}{}^{i}}\gamma{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big) +\frac{3i}{8}g\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\psi{}_{a}{}_{i}\\
&-\frac{3i}{8}g\widehat G{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\psi{}^{a}{}_{i} -ig\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{c}{}^{d}\psi{}_{c}{}_{i}\\
&+ig\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\psi{}^{c}{}_{i} -\frac{i}{2}g\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i}\\
&+\frac{i}{2}g\widehat H{}^{a}{}^{b}\widehat H{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\psi{}^{e}{}_{i} -\frac{1}{16}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{d}{}_{i}\\
&-\frac{1}{4}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)}\gamma{}^{f}\psi{}_{f}{}_{i} +\frac{i}{8}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\psi{}_{b}{}_{i}\\
&-\frac{3i}{4}\widehat G{}_{b}{}_{c}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\psi{}^{c}{}_{i} +\frac{1}{8}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}\psi{}^{d}{}_{i}\\
&+3i\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{c}{}^{i}\big)}\psi{}_{b}{}_{i} +\frac{i}{2}\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)}\gamma{}_{a}{}_{b}\psi{}_{d}{}_{i}\\
&+\frac{1}{2}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\psi{}^{f}{}_{i} -\frac{i}{4}\widehat G{}_{a}{}_{c}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\psi{}_{b}{}_{i}\\
&+\frac{1}{8}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}^{e}{}_{i} +i\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\psi{}_{c}{}_{i}\\
&+\frac{1}{2}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{a}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}\psi{}^{f}{}_{i} +\frac{i}{4}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}^{d}\psi{}_{b}{}_{i}\\
&+\frac{1}{4}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}^{e}{}_{i} +i\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)}\gamma{}_{b}{}_{c}\psi{}_{d}{}_{i}\\
&+\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)}\gamma{}^{e}\psi{}^{f}{}_{i} +\frac{i}{4}\widehat G{}_{b}{}_{d}\overline{\big(\mathcal D^{a}\widehat R(Q){}_{a}{}^{b}{}^{i}\big)}\gamma{}^{c}{}^{d}\psi{}_{c}{}_{i}\\
&+i\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{a}{}_{c}{}^{i}\big)}\gamma{}_{b}{}^{d}\psi{}_{d}{}_{i} +\frac{4i}{3}\widehat H{}^{a}{}^{b}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{8}{3}\widehat H{}^{a}{}^{b}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}\big(\mathcal D_{c}\mathcal D_{b}\psi{}_{i}\big) -\frac{8}{3}\widehat H{}^{a}{}^{b}\overline{\psi{}_{a}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{4i}{3}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) +\frac{4i}{3}\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{c}{}^{i}}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{16i}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{16i}{3}\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}^{c}\overline{\psi{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+8ig\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big) -4ig\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&+4g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big) +4ig\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\varphi{}^{i}\big)}\gamma{}_{a}{}_{c}\psi{}_{b}{}_{i}\\
&-2ig\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D^{c}\varphi{}^{i}\big)}\gamma{}_{a}{}_{b}\psi{}_{c}{}_{i} -2g\widehat H{}^{a}{}^{b}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{c}\varphi{}^{i}\big)}\gamma{}^{d}\psi{}^{e}{}_{i}\\
&+\frac{1}{6}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D_{e}\psi{}_{i}\big) +\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{b}{}^{c}\overline{\psi{}_{a}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{i}{3}gL{}^{i}{}^{j}\widehat G{}_{b}{}^{c}\overline{\psi{}_{a}{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&+\frac{i}{3}gL{}^{i}{}^{j}\widehat G{}_{a}{}^{b}\overline{\psi{}^{a}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{16i}{3}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{16i}{3}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}_{a}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big) +\frac{4i}{3}g\widehat G{}_{a}{}_{c}\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\gamma{}^{b}{}^{c}\psi{}_{b}{}_{i}\\
&-\frac{4i}{3}g\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{a}\varphi{}^{i}\big)}\psi{}^{b}{}_{i} +\frac{8i}{3}g\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\varphi{}^{i}\big)}\gamma{}_{b}{}^{c}\psi{}_{c}{}_{i}\\
&+\frac{8i}{3}g\widehat H{}^{a}{}^{b}\overline{\big(\mathcal D_{a}\varphi{}^{i}\big)}\psi{}_{b}{}_{i} -\frac{5i}{3}\big(\Box^c\sigma\big)\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5i}{3}\big(\Box^c\sigma\big)\overline{\psi{}^{a}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{5}{3}g\big(\Box^c\sigma\big)\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}_{a}{}_{i}\\
&-\frac{11i}{12}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\psi{}_{a}{}^{k}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{k}\big) -\frac{11i}{12}g^{2}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\psi{}^{a}{}^{k}}\big(\mathcal D_{a}\psi{}_{k}\big)\\
&-\frac{7}{12}g^{3}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\varphi{}^{k}}\gamma{}^{a}\psi{}_{a}{}_{k} -\frac{11i}{3}Ng\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{11i}{3}Ng\overline{\psi{}^{a}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{1}{3}Ng^{2}\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}_{a}{}_{i}\\
&+\frac{13i}{12}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{13}{3}\big(\mathcal D^{c}\widehat G{}_{a}{}_{b}\big)\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{5i}{3}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{e}\psi{}_{i}\big) +\frac{10}{3}\big(\mathcal D_{a}\widehat G{}_{b}{}^{c}\big)\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{10}{3}\big(\mathcal D_{b}\widehat G{}_{a}{}^{c}\big)\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{7i}{6}\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{7i}{6}\big(\mathcal D^{b}\widehat G{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{a}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big) +\frac{i}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{4}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{4i}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{8}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{8}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{a}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{i}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{i}{3}\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{13i}{6}g\big(\mathcal D_{c}\widehat G{}_{a}{}_{b}\big)\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\psi{}^{c}{}_{i} +\frac{13i}{3}g\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\psi{}^{c}{}_{i}\\
&+\frac{13}{6}g\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}^{b}{}_{i} -\frac{7i}{3}g\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{b}{}_{c}\psi{}_{a}{}_{i}\\
&-\frac{14i}{3}g\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{a}{}_{b}\psi{}_{c}{}_{i} -\frac{7}{3}g\big(\mathcal D^{a}\widehat H{}^{b}{}^{c}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{d}\psi{}^{e}{}_{i}\\
&+\frac{i}{3}\big(\mathcal D^{d}\widehat G{}_{d}{}^{e}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{2}{3}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{2}{3}\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{1}{3}\big(\mathcal D^{b}\widehat G{}_{b}{}^{c}\big)\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{8i}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{16}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{16}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{10}{3}\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{5i}{3}g\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\psi{}_{a}{}_{i} +\frac{5i}{3}g\big(\mathcal D^{b}\widehat G{}_{a}{}_{b}\big)\overline{\varphi{}^{i}}\psi{}^{a}{}_{i}\\
&+\frac{22i}{3}g\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\overline{\varphi{}^{i}}\gamma{}_{b}{}^{c}\psi{}_{c}{}_{i} +\frac{22i}{3}g\big(\mathcal D^{a}\widehat H{}_{a}{}^{b}\big)\overline{\varphi{}^{i}}\psi{}_{b}{}_{i}\\
&+2igL{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{c}{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{j}\big) +4gL{}^{i}{}^{j}\overline{\psi{}^{b}{}_{i}}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{j}\big)\\
&-4gL{}^{i}{}^{j}\overline{\psi{}^{b}{}_{i}}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{j}\big) -2gL{}^{i}{}^{j}\overline{\psi{}_{a}{}_{i}}\gamma{}^{a}\big(\Box^c\psi{}_{j}\big)\\
&-\frac{5i}{2}g^{2}L{}^{i}{}^{j}L{}_{i}{}^{k}\overline{\psi{}_{a}{}_{j}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{k}\big) -\frac{5i}{2}g^{2}L{}^{i}{}^{j}L{}_{i}{}^{k}\overline{\psi{}^{a}{}_{j}}\big(\mathcal D_{a}\psi{}_{k}\big)\\
&+4ig^{2}L{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\varphi{}_{i}\big)}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{j} +4ig^{2}L{}^{i}{}^{j}\overline{\big(\mathcal D^{a}\varphi{}_{i}\big)}\psi{}_{a}{}_{j}\\
&-\frac{i}{2}\widehat H{}^{a}{}^{b}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i} +\frac{i}{2}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}_{a}{}^{c}{}^{i}}\psi{}^{d}{}_{i}\\
&+\frac{i}{2}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i} -\frac{i}{2}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\psi{}^{e}{}_{i}\\
&-\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{b}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i} +\frac{i}{4}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\psi{}^{e}{}_{i}\\
&+5i\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\psi{}_{i}\big) +5i\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\overline{\psi{}^{a}{}^{i}}\big(\mathcal D^{b}\psi{}_{i}\big)\\
&+g\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{j}\big) -2g\overline{\big(\Box^c\varphi{}^{i}\big)}\gamma{}^{b}\psi{}_{b}{}_{i}\\
&+\frac{i}{3}\widehat G{}^{c}{}^{d}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) +\frac{i}{3}\widehat G{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{a}{}^{i}}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{i}\big)\\
&-\frac{i}{3}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big) +\frac{2}{3}\widehat G{}_{a}{}^{c}\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{2}{3}\widehat G{}_{b}{}^{c}\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big) -ig\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+2g\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\overline{\psi{}^{b}{}_{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{j}\big) -2g\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\overline{\psi{}_{a}{}_{i}}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+2ig^{2}\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\overline{\varphi{}_{i}}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{j} +2ig^{2}\big(\mathcal D^{a}L{}^{i}{}^{j}\big)\overline{\varphi{}_{i}}\psi{}_{a}{}_{j}\\
&-i\widehat G{}_{b}{}^{c}\widehat G{}_{c}{}^{d}\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) -i\widehat G{}_{a}{}^{b}\widehat G{}_{b}{}^{c}\overline{\psi{}^{a}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-2i\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{d}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big) -2i\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}_{c}\overline{\psi{}^{c}{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{23i}{288}gL{}^{i}{}^{j}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\psi{}_{c}{}_{j} +\frac{23i}{288}gL{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\psi{}^{c}{}_{j}\\
&+\frac{11i}{144}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\widehat R(Q){}^{c}{}^{d}{}_{i}}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{j} -\frac{11i}{144}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}_{i}}\psi{}^{e}{}_{j}\\
&-\frac{1}{144}gL{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\widehat R(Q){}^{a}{}^{b}{}_{i}}\gamma{}^{c}\psi{}_{c}{}_{j} -\frac{59}{72}g\widehat H{}^{a}{}^{b}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{a}{}_{b}{}_{i}}\gamma{}^{c}\psi{}_{c}{}_{j}\\
&-2i\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) +2i\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-2i\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big) +2\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{b}{}^{i}}\gamma{}^{a}\big(\mathcal D^{c}\psi{}_{i}\big)\\
&-2i\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\overline{\psi{}_{a}{}^{i}}\gamma{}^{a}{}^{b}\big(\mathcal D^{c}\psi{}_{i}\big) -2i\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\overline{\psi{}^{a}{}^{i}}\big(\mathcal D^{b}\psi{}_{i}\big)\\
&+ig\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{a}{}^{b}\psi{}^{c}{}_{i} +2g\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}^{b}{}_{i}\\
&-2g\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\overline{\varphi{}^{i}}\gamma{}^{a}\psi{}^{b}{}_{i} +\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{1}{2}\widehat H{}^{a}{}^{b}\widehat G{}_{c}{}^{e}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{2}\widehat H{}^{a}{}^{b}\widehat G{}_{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big) -igL{}^{i}{}^{j}\widehat G{}_{a}{}_{c}\overline{\psi{}^{c}{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{i}{2}gL{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\psi{}^{c}{}_{i}}\gamma{}^{a}{}^{b}\big(\mathcal D_{c}\psi{}_{j}\big) -\frac{1}{2}gL{}^{i}{}^{j}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{b}{}_{i}}\gamma{}^{a}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{i}{4}g^{2}L{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}_{i}}\gamma{}^{a}{}^{b}\psi{}^{c}{}_{j} -g^{2}L{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\varphi{}_{i}}\gamma{}^{a}\psi{}^{b}{}_{j}\\
&-\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{1}{3}\widehat H{}^{a}{}^{b}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{a}{}^{i}}\gamma{}^{c}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{4}{3}C{}^{a}\widehat R(V){}_{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big) +\frac{4}{3}C{}^{a}\widehat R(V){}_{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&+\frac{4}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}_{b}\big(\mathcal D_{a}\psi{}_{j}\big) +\frac{2i}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}_{d}{}_{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{j}\big)\\
&+\frac{2i}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}_{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{f}\psi{}_{j}\big) +\frac{2i}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&+\frac{i}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}_{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\psi{}_{j}\big) +\frac{2}{3}C{}^{a}\widehat R(V){}_{a}{}^{b}{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-\frac{2}{3}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{j}\big) -\frac{2}{3}gC{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}_{i}}\gamma{}^{d}\psi{}^{e}{}_{j}\\
&-\frac{4i}{3}gC{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}_{a}{}_{b}\psi{}_{c}{}_{j} +\frac{4i}{3}gC{}^{a}\widehat R(V){}_{a}{}^{b}{}^{i}{}^{j}\overline{\varphi{}_{i}}\gamma{}_{b}{}^{c}\psi{}_{c}{}_{j}\\
&+\frac{4i}{3}gC{}^{a}\widehat R(V){}_{a}{}^{b}{}^{i}{}^{j}\overline{\varphi{}_{i}}\psi{}_{b}{}_{j} -\frac{1}{72}C{}^{a}\widehat G{}_{b}{}_{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\psi{}^{e}{}_{i}\\
&-\frac{i}{36}C{}^{a}\widehat G{}_{b}{}_{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\psi{}^{e}{}_{i} -\frac{i}{36}C{}^{a}\widehat G{}_{a}{}_{e}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i}\\
&+\frac{i}{36}C{}^{a}\widehat G{}_{a}{}_{d}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\psi{}^{d}{}_{i} -\frac{1}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{i}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}{}_{b}\psi{}_{c}{}_{i} +\frac{i}{9}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{e}\psi{}_{e}{}_{i}\\
&-\frac{7i}{18}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\psi{}_{b}{}_{i} +\frac{7}{36}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{d}\psi{}^{e}{}_{i}\\
&+\frac{7i}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}_{a}{}^{d}\psi{}^{e}{}_{i} +\frac{7i}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{e}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i}\\
&-\frac{25i}{18}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\psi{}^{d}{}_{i} +\frac{7}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}^{f}\psi{}^{g}{}_{i}\\
&+\frac{14i}{9}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}_{a}{}_{d}\psi{}_{e}{}_{i} -\frac{14i}{9}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{c}{}_{d}{}^{i}}\gamma{}_{b}{}^{e}\psi{}_{e}{}_{i}\\
&-\frac{14i}{9}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{c}{}_{d}{}^{i}}\psi{}_{b}{}_{i} -\frac{2i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{f}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{g}\psi{}_{i}\big)\\
&-\frac{4}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{4}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{i}{2}gC{}^{a}\widehat G^2\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{i} -\frac{4i}{3}gC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{c}\overline{\varphi{}^{i}}\gamma{}_{a}{}^{d}\psi{}_{d}{}_{i}\\
&+5igC{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}\overline{\varphi{}^{i}}\gamma{}_{a}{}^{d}\psi{}_{d}{}_{i} +\frac{5i}{16}C{}^{a}\widehat G{}_{c}{}_{d}\varepsilon{}_{a}{}_{b}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{5}{8}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{a}\psi{}_{b}{}_{i} +\frac{5}{8}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\big(\mathcal D_{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{d}{}_{i}\\
&+\frac{5i}{4}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}_{c}{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i} -\frac{5}{2}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}_{c}{}^{i}\big)}\gamma{}_{a}\psi{}_{d}{}_{i}\\
&+\frac{5}{2}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{a}\widehat R(Q){}_{b}{}_{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{d}{}_{i} +2iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\psi{}_{e}{}_{i}\\
&+\frac{1}{12}C{}^{a}\widehat G{}_{b}{}^{f}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}\psi{}^{e}{}_{i} +\frac{i}{6}C{}^{a}\widehat G{}_{b}{}_{d}\widehat G{}_{c}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}_{a}{}^{d}\psi{}^{e}{}_{i}\\
&-\frac{i}{6}C{}^{a}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{e}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i} +\frac{i}{6}C{}^{a}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}^{b}{}^{c}{}^{i}}\psi{}^{d}{}_{i}\\
&+\frac{1}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\psi{}^{f}{}_{i} -\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}{}^{e}\psi{}_{c}{}_{i}\\
&+\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}{}_{c}\psi{}^{e}{}_{i} -\frac{i}{6}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{e}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i}\\
&-\frac{4i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\psi{}^{d}{}_{i} -\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{e}\psi{}_{e}{}_{i}\\
&+\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\psi{}_{c}{}_{i} -\frac{2}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}_{d}{}^{i}}\gamma{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\overline{\widehat R(Q){}_{b}{}_{d}{}^{i}}\gamma{}_{a}{}_{c}\psi{}_{e}{}_{i} -\frac{4i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\gamma{}_{d}{}^{e}\psi{}_{e}{}_{i}\\
&-\frac{4i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\widehat R(Q){}_{b}{}_{c}{}^{i}}\psi{}_{d}{}_{i} -3C{}^{a}\widehat G{}_{a}{}_{c}\widehat G{}_{b}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+3C{}^{a}\widehat G{}_{a}{}^{d}\widehat G{}_{b}{}_{c}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) +3C{}^{a}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{3i}{8}C{}^{a}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{3i}{8}C{}^{a}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{3i}{8}C{}^{a}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{3i}{8}C{}^{a}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{3i}{8}C{}^{a}\widehat G{}^{d}{}^{e}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{3i}{8}C{}^{a}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{8}C{}^{a}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D^{g}\psi{}_{i}\big) +\frac{8}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-4C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{8}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-4C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\psi{}_{b}{}^{i}}\gamma{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{8}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+4C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{i}\big) +iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&-iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big) +iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\psi{}_{d}{}^{i}}\gamma{}_{c}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{32}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}_{f}{}^{i}}\gamma{}^{f}{}^{g}\big(\mathcal D_{g}\psi{}_{i}\big) -\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\psi{}^{g}{}^{i}}\gamma{}_{a}{}^{f}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&-\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\psi{}_{f}{}^{i}}\gamma{}^{f}{}^{g}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{g}{}^{i}}\gamma{}_{a}{}^{f}\big(\mathcal D_{g}\psi{}_{i}\big) +\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{f}{}^{i}}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+\frac{3i}{2}gC{}^{a}\widehat G{}_{a}{}_{d}\widehat G{}_{b}{}_{c}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}^{d}{}_{i} +3igC{}^{a}\widehat G{}_{a}{}_{b}\widehat G{}_{c}{}_{d}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}^{d}{}_{i}\\
&-\frac{3}{8}gC{}^{a}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}_{a}\psi{}^{b}{}_{i} +\frac{3}{8}gC{}^{a}\widehat G{}^{c}{}^{d}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}_{b}{}_{i}\\
&-2igC{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\varphi{}^{i}}\gamma{}^{c}{}^{d}\psi{}_{b}{}_{i} -4igC{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{c}{}_{d}\overline{\varphi{}^{i}}\gamma{}_{b}{}^{c}\psi{}^{d}{}_{i}\\
&+4igC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\varphi{}^{i}}\gamma{}_{b}{}^{d}\psi{}_{c}{}_{i} -2igC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{d}\overline{\varphi{}^{i}}\gamma{}_{b}{}_{c}\psi{}^{d}{}_{i}\\
&+gC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}_{a}\psi{}^{d}{}_{i} -gC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{d}\psi{}_{d}{}_{i}\\
&-2igC{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\varphi{}^{i}}\gamma{}_{c}{}_{d}\psi{}_{b}{}_{i} -4igC{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}^{c}{}^{d}\overline{\varphi{}^{i}}\gamma{}_{b}{}_{c}\psi{}_{d}{}_{i}\\
&+\frac{1}{2}gC{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}_{a}\psi{}^{f}{}_{i} -\frac{1}{2}gC{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{f}\psi{}_{f}{}_{i}\\
&-\frac{i}{16}C{}^{a}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{a}{}^{e}\psi{}_{e}{}_{i} -\frac{i}{4}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\widehat R(Q){}^{e}{}^{f}{}^{i}\big)}\gamma{}_{a}{}^{g}\psi{}_{g}{}_{i}\\
&+\frac{1}{4}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\gamma{}^{c}\psi{}^{d}{}_{i} -\frac{1}{4}C{}^{a}\widehat G{}_{a}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{c}{}_{i}\\
&+\frac{i}{8}C{}^{a}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{a}{}^{d}\psi{}^{e}{}_{i} -\frac{i}{8}C{}^{a}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\psi{}_{d}{}_{i}\\
&+\frac{i}{8}C{}^{a}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\psi{}^{d}{}_{i} -C{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{c}{}^{d}{}^{i}\big)}\gamma{}_{b}\psi{}_{d}{}_{i}\\
&+C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{a}{}_{d}{}^{i}\big)}\gamma{}_{b}\psi{}_{c}{}_{i} +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{d}{}^{e}{}^{i}\big)}\gamma{}_{a}{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{d}{}^{e}{}^{i}\big)}\gamma{}^{f}{}^{g}\psi{}_{f}{}_{i} +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{d}{}^{e}{}^{i}\big)}\psi{}^{f}{}_{i}\\
&+\frac{1}{4}C{}^{a}\widehat G{}_{b}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{c}{}_{i} +\frac{i}{8}C{}^{a}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{a}{}^{e}\psi{}^{f}{}_{i}\\
&+\frac{i}{8}C{}^{a}\widehat G{}_{b}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i} -\frac{i}{8}C{}^{a}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\psi{}^{e}{}_{i}\\
&+C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\widehat R(Q){}_{a}{}^{d}{}^{i}\big)}\gamma{}_{c}\psi{}_{d}{}_{i} +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D_{b}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)}\gamma{}_{a}{}^{f}\psi{}^{g}{}_{i}\\
&-\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\big(\mathcal D_{b}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)}\gamma{}^{f}{}^{g}\psi{}_{f}{}_{i} +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\widehat R(Q){}^{d}{}^{e}{}^{i}\big)}\psi{}^{f}{}_{i}\\
&-\frac{1}{4}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D_{a}\widehat R(Q){}^{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{b}{}_{i} +\frac{1}{4}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{b}{}_{i}\\
&-\frac{1}{4}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{a}{}^{c}{}^{i}\big)}\gamma{}_{b}\psi{}^{d}{}_{i} -\frac{1}{4}C{}^{a}\widehat G{}_{a}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{b}\psi{}_{c}{}_{i}\\
&+\frac{i}{4}C{}^{a}\widehat G{}_{c}{}^{g}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}_{a}{}^{e}\psi{}^{f}{}_{i} +\frac{i}{4}C{}^{a}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{b}{}_{d}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i}\\
&-\frac{i}{4}C{}^{a}\widehat G{}_{c}{}^{f}\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\widehat R(Q){}^{c}{}^{d}{}^{i}\big)}\psi{}^{e}{}_{i} +C{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{b}{}^{d}{}^{i}\big)}\gamma{}_{c}\psi{}_{d}{}_{i}\\
&-C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\gamma{}_{d}\psi{}_{c}{}_{i} +C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{a}\widehat R(Q){}_{b}{}^{d}{}^{i}\big)}\gamma{}_{c}\psi{}_{d}{}_{i}\\
&+C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{a}{}_{b}{}^{i}\big)}\gamma{}_{c}\psi{}_{d}{}_{i} +iC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}^{e}{}^{i}\big)}\gamma{}_{a}{}^{f}\psi{}^{g}{}_{i}\\
&-iC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}^{e}{}^{i}\big)}\gamma{}^{f}{}^{g}\psi{}_{f}{}_{i} +iC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}^{e}{}^{i}\big)}\psi{}^{f}{}_{i}\\
&-\frac{i}{8}C{}^{a}\widehat G{}_{c}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}{}^{e}\psi{}^{f}{}_{i} -\frac{1}{4}C{}^{a}\widehat G{}_{c}{}_{d}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}_{a}\psi{}^{d}{}_{i}\\
&-\frac{1}{4}C{}^{a}\widehat G{}_{a}{}_{c}\overline{\big(\mathcal D^{b}\widehat R(Q){}_{b}{}^{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{d}{}_{i} -\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}_{d}{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}^{g}{}_{i}\\
&+C{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D^{d}\widehat R(Q){}_{b}{}_{d}{}^{i}\big)}\gamma{}_{a}\psi{}_{c}{}_{i} +C{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D^{c}\widehat R(Q){}_{b}{}_{c}{}^{i}\big)}\gamma{}^{d}\psi{}_{d}{}_{i}\\
&-\frac{8}{3}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\mathcal D_{b}\psi{}_{i}\big) -\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{d}\mathcal D_{c}\psi{}_{i}\big) -\frac{8i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\psi{}^{c}{}^{i}}\big(\mathcal D_{c}\mathcal D_{b}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{d}\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}_{b}{}^{i}}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\psi{}_{b}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{c}\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{d}\mathcal D_{c}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{a}\mathcal D_{d}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{d}\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\mathcal D_{d}\psi{}_{i}\big) -\frac{4i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{4}{3}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) +\frac{4}{3}C{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{8i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{g}{}^{i}}\gamma{}^{e}{}^{f}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{16}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat H{}_{b}{}^{c}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{16}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}_{a}\big(\mathcal D_{d}\psi{}_{i}\big) +8gC{}^{a}\widehat H{}_{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&-8gC{}^{a}\widehat H{}_{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{b}\big(\mathcal D_{c}\psi{}_{j}\big) -8gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}_{b}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-4igC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}_{d}{}_{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{f}\psi{}_{j}\big) -4igC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}_{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{f}\psi{}_{j}\big)\\
&-4igC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\big(\mathcal D^{e}\psi{}_{j}\big) -4gC{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D^{c}\varphi{}^{i}\big)}\gamma{}_{c}\psi{}_{b}{}_{i}\\
&+4gC{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D^{c}\varphi{}^{i}\big)}\gamma{}_{b}\psi{}_{c}{}_{i} +4gC{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{a}\varphi{}^{i}\big)}\gamma{}_{b}\psi{}_{c}{}_{i}\\
&-2igC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{d}\varphi{}^{i}\big)}\gamma{}_{a}{}^{e}\psi{}^{f}{}_{i} +2igC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\big(\mathcal D^{d}\varphi{}^{i}\big)}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i}\\
&-2igC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{d}\varphi{}^{i}\big)}\psi{}^{e}{}_{i} -\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&-\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{f}\psi{}_{i}\big) -\frac{i}{6}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{2i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{g}\psi{}_{i}\big) +\frac{4}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{b}{}^{d}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{4}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{i}{6}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{d}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{e}\psi{}_{j}\big)\\
&-\frac{1}{3}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}^{c}\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{j}\big) +\frac{1}{3}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{b}{}^{c}\overline{\psi{}^{b}{}_{i}}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&-\frac{8i}{3}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}_{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\psi{}_{j}\big) -\frac{16}{3}gC{}^{a}\widehat H{}_{a}{}^{b}L{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}^{c}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+\frac{16}{3}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{j}\big) -\frac{2i}{3}gC{}^{a}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{i}\\
&-\frac{4}{3}gC{}^{a}\widehat G{}_{b}{}_{c}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}_{a}\psi{}^{c}{}_{i} -\frac{4}{3}gC{}^{a}\widehat G{}_{a}{}_{b}\overline{\big(\mathcal D^{b}\varphi{}^{i}\big)}\gamma{}^{c}\psi{}_{c}{}_{i}\\
&-\frac{4i}{3}gC{}^{a}\widehat H{}^{b}{}^{c}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\big(\mathcal D_{b}\varphi{}^{i}\big)}\gamma{}^{d}{}^{e}\psi{}^{f}{}_{i} +\frac{8}{3}gC{}^{a}\widehat H{}^{b}{}^{c}\overline{\big(\mathcal D_{b}\varphi{}^{i}\big)}\gamma{}_{a}\psi{}_{c}{}_{i}\\
&+\frac{8}{3}gC{}^{a}\widehat H{}_{a}{}^{b}\overline{\big(\mathcal D_{b}\varphi{}^{i}\big)}\gamma{}^{c}\psi{}_{c}{}_{i} +\frac{5i}{6}C{}^{a}\big(\Box^c\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{5}{3}C{}^{a}\big(\Box^c\sigma\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{5}{3}C{}^{a}\big(\Box^c\sigma\big)\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{5i}{3}gC{}^{a}\big(\Box^c\sigma\big)\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{i} +\frac{11i}{24}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}^{k}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{k}\big)\\
&+\frac{11}{12}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\psi{}_{b}{}^{k}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{k}\big) -\frac{11}{12}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\psi{}^{b}{}^{k}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{k}\big)\\
&-\frac{7i}{12}g^{3}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}\overline{\varphi{}^{k}}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{k} +\frac{11i}{6}NgC{}^{a}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big)\\
&+\frac{11}{3}NgC{}^{a}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{11}{3}NgC{}^{a}\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{i}{3}Ng^{2}C{}^{a}\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}_{b}{}_{i} +\frac{13}{6}C{}^{a}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{13i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{a}{}_{c}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{13i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{b}{}_{c}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{13i}{3}C{}^{a}\big(\mathcal D^{c}\widehat G{}_{a}{}_{b}\big)\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{10}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{e}\psi{}_{i}\big)\\
&+\frac{10i}{3}C{}^{a}\big(\mathcal D_{c}\widehat G{}_{a}{}^{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{10i}{3}C{}^{a}\big(\mathcal D_{b}\widehat G{}_{c}{}^{d}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{10i}{3}C{}^{a}\big(\mathcal D_{a}\widehat G{}_{c}{}^{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{10i}{3}C{}^{a}\big(\mathcal D_{a}\widehat G{}_{b}{}^{c}\big)\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{10i}{3}C{}^{a}\big(\mathcal D_{c}\widehat G{}_{b}{}^{d}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{10i}{3}C{}^{a}\big(\mathcal D_{b}\widehat G{}_{a}{}^{c}\big)\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{7i}{3}C{}^{a}\big(\mathcal D_{a}\widehat G{}_{b}{}_{d}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{7i}{6}C{}^{a}\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{7i}{3}C{}^{a}\big(\mathcal D_{d}\widehat G{}_{a}{}_{b}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{7i}{6}C{}^{a}\big(\mathcal D_{d}\widehat G{}_{b}{}_{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{7i}{3}C{}^{a}\big(\mathcal D_{b}\widehat G{}_{a}{}_{d}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{7i}{3}C{}^{a}\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{7i}{3}C{}^{a}\big(\mathcal D_{b}\widehat G{}_{c}{}_{d}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{7}{6}C{}^{a}\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{7}{6}C{}^{a}\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D^{f}\psi{}_{i}\big) +\frac{2}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{e}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{4i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{4i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{a}{}_{c}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{4i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big) +\frac{8}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{f}{}^{i}}\gamma{}^{e}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{8i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{8i}{3}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{8i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{8i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{b}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) +\frac{i}{3}C{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}_{c}{}_{d}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{2i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{2i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}_{c}\big(\mathcal D_{a}\psi{}_{i}\big) -\frac{1}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}_{e}{}^{i}}\gamma{}^{e}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{1}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{13}{3}gC{}^{a}\big(\mathcal D_{a}\widehat G{}_{b}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}^{c}{}_{i}\\
&-\frac{13}{3}gC{}^{a}\big(\mathcal D_{c}\widehat G{}_{a}{}_{b}\big)\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}^{c}{}_{i} +\frac{13}{3}gC{}^{a}\big(\mathcal D_{b}\widehat G{}_{a}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}^{c}{}_{i}\\
&+\frac{13i}{6}gC{}^{a}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}^{c}{}_{i} +\frac{13i}{6}gC{}^{a}\big(\mathcal D^{d}\widehat G{}^{e}{}^{f}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}_{b}{}_{i}\\
&-\frac{13i}{6}gC{}^{a}\big(\mathcal D^{c}\widehat G{}^{d}{}^{e}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\psi{}^{b}{}_{i} +\frac{14}{3}gC{}^{a}\big(\mathcal D_{a}\widehat H{}^{b}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{b}\psi{}_{c}{}_{i}\\
&+\frac{14}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{c}\psi{}_{b}{}_{i} -\frac{14}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{b}\psi{}_{c}{}_{i}\\
&-\frac{7i}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}_{a}{}^{e}\psi{}^{f}{}_{i} +\frac{7i}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{e}{}^{f}\psi{}_{e}{}_{i}\\
&-\frac{7i}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}^{c}{}^{d}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\psi{}^{e}{}_{i} +\frac{2}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{d}{}^{e}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{b}{}_{d}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+\frac{2i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{a}{}_{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\big(\mathcal D^{d}\widehat G{}_{c}{}_{d}\big)\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{2i}{3}C{}^{a}\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{i}{3}C{}^{a}\big(\mathcal D^{c}\widehat G{}_{c}{}^{d}\big)\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{16}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}^{i}}\gamma{}^{d}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{c}{}^{d}\big(\mathcal D_{a}\psi{}_{i}\big) +\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}{}_{c}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)\overline{\psi{}^{c}{}^{i}}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{d}\psi{}_{i}\big) -\frac{16i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\psi{}_{c}{}^{i}}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{10i}{3}C{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\psi{}_{d}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{5i}{6}gC{}^{a}\big(\mathcal D^{e}\widehat G{}_{e}{}^{f}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}^{d}{}_{i}\\
&+\frac{5}{3}gC{}^{a}\big(\mathcal D^{c}\widehat G{}_{b}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}_{a}\psi{}^{b}{}_{i} -\frac{5}{3}gC{}^{a}\big(\mathcal D^{c}\widehat G{}_{a}{}_{c}\big)\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}_{b}{}_{i}\\
&-\frac{11i}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\varphi{}^{i}}\gamma{}^{d}{}^{e}\psi{}^{f}{}_{i} +\frac{22}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}_{b}{}^{c}\big)\overline{\varphi{}^{i}}\gamma{}_{a}\psi{}_{c}{}_{i}\\
&+\frac{22}{3}gC{}^{a}\big(\mathcal D^{b}\widehat H{}_{a}{}_{b}\big)\overline{\varphi{}^{i}}\gamma{}^{c}\psi{}_{c}{}_{i} +4gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{c}{}_{i}}\gamma{}^{b}\big(\mathcal D^{d}\mathcal D^{e}\psi{}_{j}\big)\\
&+4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{a}\psi{}_{j}\big) -4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{j}\big)\\
&-4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{j}\big) -4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}^{b}{}_{i}}\big(\mathcal D_{a}\mathcal D_{b}\psi{}_{j}\big)\\
&+4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{c}\mathcal D_{b}\psi{}_{j}\big) +4igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}^{b}{}_{i}}\big(\mathcal D_{b}\mathcal D_{a}\psi{}_{j}\big)\\
&+2igC{}^{a}L{}^{i}{}^{j}\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}{}^{b}\big(\Box^c\psi{}_{j}\big) +\frac{5i}{4}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}^{k}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{j}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{k}\big)\\
&+\frac{5}{2}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}^{k}\overline{\psi{}_{b}{}_{j}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{k}\big) -\frac{5}{2}g^{2}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}^{k}\overline{\psi{}^{b}{}_{j}}\gamma{}_{a}\big(\mathcal D_{b}\psi{}_{k}\big)\\
&-2ig^{2}C{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\big(\mathcal D^{b}\varphi{}_{i}\big)}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{j} +4g^{2}C{}^{a}L{}^{i}{}^{j}\overline{\big(\mathcal D^{b}\varphi{}_{i}\big)}\gamma{}_{a}\psi{}_{b}{}_{j}\\
&-4g^{2}C{}^{a}L{}^{i}{}^{j}\overline{\big(\mathcal D_{a}\varphi{}_{i}\big)}\gamma{}^{b}\psi{}_{b}{}_{j} +\frac{i}{2}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{b}{}^{c}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{c}{}_{i}\\
&-\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}^{d}{}^{e}\psi{}_{c}{}_{i} -iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\gamma{}_{c}{}^{d}\psi{}^{e}{}_{i}\\
&+iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{e}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{c}{}^{e}\psi{}_{d}{}_{i} +\frac{1}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}_{a}\psi{}^{e}{}_{i}\\
&-\frac{1}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\gamma{}^{e}\psi{}_{e}{}_{i} -iC{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{b}{}_{d}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\psi{}_{c}{}_{i}\\
&+iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\psi{}_{b}{}_{i} +iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{c}{}_{e}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{e}\psi{}_{d}{}_{i}\\
&-iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}_{b}{}^{i}}\psi{}^{d}{}_{i} +iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}_{b}{}^{d}{}^{i}}\psi{}_{d}{}_{i}\\
&-\frac{1}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}\psi{}^{f}{}_{i} -\frac{1}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{g}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\psi{}_{f}{}_{i}\\
&+\frac{i}{2}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}^{c}{}^{d}{}^{i}}\gamma{}_{b}{}^{e}\psi{}_{c}{}_{i} +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{b}{}^{e}\psi{}_{c}{}_{i}\\
&-\frac{i}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}_{e}\overline{\widehat R(Q){}_{a}{}^{d}{}^{i}}\gamma{}_{b}{}_{c}\psi{}^{e}{}_{i} -\frac{i}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{b}{}_{c}\psi{}_{d}{}_{i}\\
&+\frac{1}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}^{g}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}_{a}\psi{}^{f}{}_{i} +\frac{1}{4}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}^{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{g}\overline{\widehat R(Q){}^{d}{}^{e}{}^{i}}\gamma{}^{f}\psi{}_{f}{}_{i}\\
&-\frac{5i}{2}C{}^{a}\big(\mathcal D_{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big) -5C{}^{a}\big(\mathcal D_{c}\mathcal D_{a}\sigma\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\psi{}_{i}\big)\\
&+5C{}^{a}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D^{c}\psi{}_{i}\big) -igC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\psi{}_{c}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&-2igC{}^{a}\overline{\big(\Box^c\varphi{}^{i}\big)}\gamma{}_{a}{}^{c}\psi{}_{c}{}_{i} +\frac{2i}{3}C{}^{a}\widehat G{}_{a}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\widehat G{}_{a}{}_{b}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\mathcal D_{c}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\widehat G{}_{a}{}_{b}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\widehat G{}_{b}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\widehat G{}_{b}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{a}\psi{}_{i}\big)\\
&+\frac{i}{3}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D_{d}\psi{}_{i}\big) -\frac{i}{3}C{}^{a}\widehat G{}_{b}{}_{c}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{d}\mathcal D_{a}\psi{}_{i}\big)\\
&-\frac{1}{3}C{}^{a}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big) +\frac{1}{3}C{}^{a}\widehat G{}^{c}{}^{d}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D^{e}\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{2}{3}C{}^{a}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D^{f}\mathcal D_{d}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\widehat G{}_{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{a}\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\widehat G{}_{b}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{c}\mathcal D_{d}\psi{}_{i}\big) -\frac{2i}{3}C{}^{a}\widehat G{}_{a}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\mathcal D_{d}\psi{}_{i}\big)\\
&-\frac{2i}{3}C{}^{a}\widehat G{}_{a}{}^{c}\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{b}\mathcal D_{c}\psi{}_{i}\big) +\frac{2i}{3}C{}^{a}\widehat G{}_{c}{}^{d}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D_{b}\mathcal D_{d}\psi{}_{i}\big)\\
&+\frac{2i}{3}C{}^{a}\widehat G{}_{b}{}^{c}\overline{\psi{}^{b}{}^{i}}\big(\mathcal D_{a}\mathcal D_{c}\psi{}_{i}\big) +2gC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{c}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-2igC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\psi{}_{c}{}_{i}}\gamma{}_{b}{}^{c}\big(\mathcal D_{a}\psi{}_{j}\big) -2igC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}_{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&-2igC{}^{a}\big(\mathcal D_{a}L{}^{i}{}^{j}\big)\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big) -2igC{}^{a}\big(\mathcal D_{a}L{}^{i}{}^{j}\big)\overline{\psi{}^{b}{}_{i}}\big(\mathcal D_{b}\psi{}_{j}\big)\\
&+2igC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\psi{}_{b}{}_{i}}\gamma{}_{a}{}^{c}\big(\mathcal D_{c}\psi{}_{j}\big) +2igC{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\psi{}_{b}{}_{i}}\big(\mathcal D_{a}\psi{}_{j}\big)\\
&-ig^{2}C{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}_{i}}\gamma{}^{c}{}^{d}\psi{}^{e}{}_{j} +2g^{2}C{}^{a}\big(\mathcal D^{b}L{}^{i}{}^{j}\big)\overline{\varphi{}_{i}}\gamma{}_{a}\psi{}_{b}{}_{j}\\
&-2g^{2}C{}^{a}\big(\mathcal D_{a}L{}^{i}{}^{j}\big)\overline{\varphi{}_{i}}\gamma{}^{b}\psi{}_{b}{}_{j} -\frac{i}{2}C{}^{a}\widehat G{}^{e}{}^{f}\widehat G{}_{e}{}^{g}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{g}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D_{f}\psi{}_{i}\big)\\
&+C{}^{a}\widehat G{}_{a}{}^{c}\widehat G{}_{c}{}^{d}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D_{d}\psi{}_{i}\big) -C{}^{a}\widehat G{}_{b}{}^{c}\widehat G{}_{c}{}^{d}\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D_{d}\psi{}_{i}\big)\\
&+iC{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{g}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{f}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{c}\psi{}_{i}\big) -2C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}_{b}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&-2C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}_{d}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}\big(\mathcal D_{c}\psi{}_{i}\big) -\frac{23i}{144}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{c}{}_{d}\overline{\widehat R(Q){}_{a}{}^{b}{}_{i}}\gamma{}^{c}{}^{d}\psi{}_{b}{}_{j}\\
&+\frac{23i}{72}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}_{a}{}^{b}{}_{i}}\psi{}^{c}{}_{j} +\frac{23i}{72}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\psi{}_{b}{}_{j}\\
&+\frac{23}{288}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}_{a}\psi{}^{d}{}_{j} -\frac{23}{288}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}^{d}\psi{}_{d}{}_{j}\\
&+\frac{11i}{36}gC{}^{a}\widehat H{}_{a}{}^{b}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{b}{}^{c}{}_{i}}\psi{}_{c}{}_{j} -\frac{11i}{36}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{a}{}_{b}{}_{i}}\psi{}_{c}{}_{j}\\
&+\frac{11i}{72}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{a}{}^{d}{}_{i}}\gamma{}_{b}{}_{c}\psi{}_{d}{}_{j} -\frac{11}{144}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\widehat R(Q){}^{d}{}^{e}{}_{i}}\gamma{}_{a}\psi{}^{f}{}_{j}\\
&+\frac{11}{144}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\widehat R(Q){}^{d}{}^{e}{}_{i}}\gamma{}^{f}\psi{}_{f}{}_{j} -\frac{i}{144}gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{b}{}_{c}\overline{\widehat R(Q){}^{b}{}^{c}{}_{i}}\gamma{}_{a}{}^{d}\psi{}_{d}{}_{j}\\
&-\frac{59i}{72}gC{}^{a}\widehat H{}^{b}{}^{c}L{}^{i}{}^{j}\overline{\widehat R(Q){}_{b}{}_{c}{}_{i}}\gamma{}_{a}{}^{d}\psi{}_{d}{}_{j} +2C{}^{a}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big)\\
&-2C{}^{a}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{i}\big) -2C{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big)\\
&+2C{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{i}\big) +2C{}^{a}\big(\mathcal D_{a}\mathcal D_{c}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&-2C{}^{a}\big(\mathcal D_{c}\mathcal D_{a}\sigma\big)\overline{\psi{}^{c}{}^{i}}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{i}\big) -2iC{}^{a}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{d}\psi{}_{i}\big)\\
&-2iC{}^{a}\big(\mathcal D^{e}\mathcal D^{f}\sigma\big)\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\gamma{}_{a}{}^{b}\big(\mathcal D^{d}\psi{}_{i}\big) -2iC{}^{a}\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{b}{}^{i}}\big(\mathcal D^{c}\psi{}_{i}\big)\\
&+iC{}^{a}\big(\mathcal D^{f}\mathcal D_{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{f}\overline{\psi{}^{d}{}^{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{e}\psi{}_{i}\big) +2C{}^{a}\big(\mathcal D_{a}\mathcal D_{c}\sigma\big)\overline{\psi{}_{b}{}^{i}}\gamma{}^{b}\big(\mathcal D^{c}\psi{}_{i}\big)\\
&-2C{}^{a}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\overline{\psi{}^{b}{}^{i}}\gamma{}_{a}\big(\mathcal D^{c}\psi{}_{i}\big) -2gC{}^{a}\big(\mathcal D^{d}\mathcal D^{e}\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}^{i}}\gamma{}^{b}\psi{}^{c}{}_{i}\\
&+2igC{}^{a}\big(\mathcal D_{c}\mathcal D_{b}\sigma\big)\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}^{c}{}_{i} -2igC{}^{a}\big(\mathcal D_{b}\mathcal D_{c}\sigma\big)\overline{\varphi{}^{i}}\gamma{}_{a}{}^{b}\psi{}^{c}{}_{i}\\
&-2igC{}^{a}\big(\mathcal D_{a}\mathcal D_{c}\sigma\big)\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}_{b}{}_{i} +2igC{}^{a}\big(\mathcal D_{a}\mathcal D_{b}\sigma\big)\overline{\varphi{}^{i}}\psi{}^{b}{}_{i}\\
&+2igC{}^{a}\big(\mathcal D_{c}\mathcal D_{a}\sigma\big)\overline{\varphi{}^{i}}\gamma{}^{b}{}^{c}\psi{}_{b}{}_{i} -2igC{}^{a}\big(\mathcal D_{b}\mathcal D_{a}\sigma\big)\overline{\varphi{}^{i}}\psi{}^{b}{}_{i}\\
&+\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{f}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{g}\psi{}_{i}\big) -\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{f}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big)\\
&+\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{b}{}^{e}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D^{f}\psi{}_{i}\big) -\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{f}{}^{g}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D_{b}\psi{}_{i}\big) -\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D_{b}\psi{}_{i}\big)\\
&+\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{e}{}^{f}\varepsilon{}_{a}{}_{b}{}_{c}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{g}\psi{}_{i}\big) -\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}^{f}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big)\\
&-\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{f}\varepsilon{}_{b}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}^{d}{}^{e}\big(\mathcal D^{g}\psi{}_{i}\big) -\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{a}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{e}{}^{f}\varepsilon{}_{b}{}_{c}{}_{d}{}_{f}{}_{g}\overline{\psi{}^{e}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big) +\frac{i}{2}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}_{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{e}{}_{f}\overline{\psi{}^{d}{}^{i}}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}_{c}\overline{\psi{}^{c}{}_{i}}\gamma{}^{b}\big(\mathcal D_{b}\psi{}_{j}\big) +gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\psi{}^{c}{}_{i}}\gamma{}^{b}\big(\mathcal D_{c}\psi{}_{j}\big)\\
&+gC{}^{a}L{}^{i}{}^{j}\widehat G{}_{b}{}_{c}\overline{\psi{}^{c}{}_{i}}\gamma{}^{b}\big(\mathcal D_{a}\psi{}_{j}\big) +\frac{i}{2}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}{}^{c}\big(\mathcal D^{f}\psi{}_{j}\big)\\
&+\frac{i}{2}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{c}{}_{i}}\gamma{}_{a}{}^{b}\big(\mathcal D^{f}\psi{}_{j}\big) +\frac{i}{2}gC{}^{a}L{}^{i}{}^{j}\widehat G{}^{c}{}^{d}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{b}{}_{i}}\big(\mathcal D^{e}\psi{}_{j}\big)\\
&-\frac{1}{2}g^{2}C{}^{a}L{}^{i}{}^{j}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\varphi{}_{i}}\gamma{}^{b}\psi{}^{c}{}_{j} -ig^{2}C{}^{a}L{}^{i}{}^{j}\widehat G{}_{b}{}_{c}\overline{\varphi{}_{i}}\gamma{}_{a}{}^{b}\psi{}^{c}{}_{j}\\
&-ig^{2}C{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}_{c}\overline{\varphi{}_{i}}\gamma{}^{b}{}^{c}\psi{}_{b}{}_{j} +ig^{2}C{}^{a}L{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\varphi{}_{i}}\psi{}^{b}{}_{j}\\
&-\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{a}{}_{c}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{d}{}^{i}}\gamma{}_{b}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big) +\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{d}{}^{i}}\gamma{}_{a}{}_{b}\big(\mathcal D^{g}\psi{}_{i}\big)\\
&+\frac{i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}^{e}{}^{f}\varepsilon{}_{b}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{c}{}^{i}}\gamma{}^{c}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big) +\frac{i}{3}C{}^{a}\widehat H{}_{a}{}^{b}\widehat G{}^{d}{}^{e}\varepsilon{}_{b}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{c}{}^{i}}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&-\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{e}{}^{f}\varepsilon{}_{c}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}_{b}{}^{i}}\gamma{}_{a}{}^{d}\big(\mathcal D^{g}\psi{}_{i}\big) +\frac{i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat G{}^{d}{}^{e}\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}_{b}{}^{i}}\big(\mathcal D^{f}\psi{}_{i}\big)\\
&+\frac{i}{3}\widehat R(V){}^{a}{}^{b}{}^{i}{}^{j}\widehat G{}_{a}{}_{b}\overline{\psi{}_{c}{}_{i}}\gamma{}^{c}{}^{d}\psi{}_{d}{}_{j} +\frac{4i}{3}\widehat H{}^{a}{}^{b}\widehat R(V){}_{a}{}_{b}{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}^{c}{}^{d}\psi{}_{d}{}_{j}\\
&+igL{}^{i}{}^{j}\big(\Box^c\sigma\big)\overline{\psi{}_{a}{}_{i}}\gamma{}^{a}{}^{b}\psi{}_{b}{}_{j} +\frac{i}{2}gL{}^{i}{}^{j}\widehat G^2\overline{\psi{}_{a}{}_{i}}\gamma{}^{a}{}^{b}\psi{}_{b}{}_{j}\\
&+ig^{3}L{}^{i}{}^{j}L{}_{i}{}_{j}L{}^{k}{}^{l}\overline{\psi{}_{a}{}_{k}}\gamma{}^{a}{}^{b}\psi{}_{b}{}_{l} -6ig\widehat H{}^{a}{}^{b}\widehat H{}_{a}{}_{b}L{}^{i}{}^{j}\overline{\psi{}_{c}{}_{i}}\gamma{}^{c}{}^{d}\psi{}_{d}{}_{j}\\
&+3iNg^{2}L{}^{i}{}^{j}\overline{\psi{}_{a}{}_{i}}\gamma{}^{a}{}^{b}\psi{}_{b}{}_{j} +ig\big(\Box^cL{}^{i}{}^{j}\big)\overline{\psi{}_{b}{}_{i}}\gamma{}^{b}{}^{c}\psi{}_{c}{}_{j}\\
&-\frac{i}{6}C{}^{a}\widehat R(V){}^{b}{}^{c}{}^{i}{}^{j}\widehat G{}_{b}{}_{c}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{f}{}_{i}}\gamma{}^{d}{}^{e}\psi{}^{g}{}_{j} -\frac{2i}{3}C{}^{a}\widehat H{}^{b}{}^{c}\widehat R(V){}_{b}{}_{c}{}^{i}{}^{j}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{f}{}_{i}}\gamma{}^{d}{}^{e}\psi{}^{g}{}_{j}\\
&-\frac{i}{2}gC{}^{a}L{}^{i}{}^{j}\big(\Box^c\sigma\big)\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{b}{}^{c}\psi{}^{e}{}_{j} -\frac{i}{4}gC{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\widehat G^2\overline{\psi{}^{d}{}_{i}}\gamma{}^{b}{}^{c}\psi{}^{e}{}_{j}\\
&-\frac{i}{2}g^{3}C{}^{a}L{}^{i}{}^{j}L{}_{i}{}_{j}L{}^{k}{}^{l}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{k}}\gamma{}^{b}{}^{c}\psi{}^{e}{}_{l} +3igC{}^{a}\widehat H{}^{b}{}^{c}\widehat H{}_{b}{}_{c}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{d}{}_{e}{}_{f}{}_{g}\overline{\psi{}^{f}{}_{i}}\gamma{}^{d}{}^{e}\psi{}^{g}{}_{j}\\
&-\frac{3i}{2}Ng^{2}C{}^{a}L{}^{i}{}^{j}\varepsilon{}_{a}{}_{b}{}_{c}{}_{d}{}_{e}\overline{\psi{}^{d}{}_{i}}\gamma{}^{b}{}^{c}\psi{}^{e}{}_{j} -\frac{i}{2}gC{}^{a}\big(\Box^cL{}^{i}{}^{j}\big)\varepsilon{}_{a}{}_{c}{}_{d}{}_{e}{}_{f}\overline{\psi{}^{e}{}_{i}}\gamma{}^{c}{}^{d}\psi{}^{f}{}_{j}
\Bigg)\Bigg]_{\le2}.
\end{aligned}}$}\tag{GB-FINAL-DENSITY}
```

For the fermionic Hessian one takes the degree-two part of this complete density, including the degree-two expansion of the first, covariant-seed terms. This expression is off shell, before background evaluation or auxiliary reduction.

<a id="7-convention-dependence-and-remaining-uncertainties"></a>

## Convention Dependence and Scope

The action assembled here is complete at the specified fermion order **relative to the adopted inputs**. The normalization ambiguity between the OP Weyl action and the target Gold action is resolved by GB16–GB20, including fermions and current terms. It is not being fixed by the curvature check alone.

The assembly uses the adopted FM02 $`8/3`$ coefficient and the specified two-derivative component slots and reality conventions. Its checks establish coefficient assembly and normalization for these inputs through two physical fermions.

No GB background, tadpole cancellation, fermion kernel, eigenmode, norm, stability bound, or degree-of-freedom count has been inferred from this assembly. Those require the separate spectrum workflow applied to this action, with all potentially dynamical auxiliary fields retained.

The source trail is:

- C24: Components of curvature-squared invariants, (4.3), footnote 4, (2.17), (A.4a), and Tables 4–6: complete Weyl primary, bosonic descendants, and component conversion. The inspected local file is arXiv:2311.00679v1 (1 November 2023); “C24” follows the inherited filename.
- Özkan–Pang GB source, (3.1), (5.18), (5.19): density and Weyl construction, read with the explicit project repairs in FM01–FM07.
- [The inherited Weyl map](../../computations/weyl_fermionic/inputs/reference/notes/04_full_fermionic_weyl_linear_map.md), FM01–FM07, and [gauged action](../../weyl2/action/details/construction.md), GA24: actual adopted component input and its qualification.
- The current LOG construction, SC7L/SC7P/SC7N/SC7E, and [assembled LOG density](../ads5/code/inputs/action_sources/04_02_fermionic_log_action.md): actual normalized input with the corrected ordinary current.
- [The two-derivative construction](../../common/two_derivative_action/details/construction.md), (5.5), (5.10): the 2016 linear-map representative retained here. Its local primary source is O16, arXiv:1608.00349v2 (26 November 2016), (3.11)–(3.15), PDF pp.9–10.
- [Bosonic GB source lock](../ads5/code/inputs/action_sources/09_gauss_bonnet_from_weyl_log_action_lock.md), Gold (2025) (22)–(23): target normalization and common bosonic comparison.

The [bibliography](../../references/bibliography.md) identifies the cited sources; the derivation distinguishes their equations from project-derived coefficient repairs.
