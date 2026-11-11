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

The eleven exact action inputs are frozen and hashed in the action input manifest. The convention reference supplies all fields, variations, curvatures, and derivative towers, with source equations and an index.

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

The source definitions are LOG G01, W04, L02, GG03–GG05 and the ordered derivative dictionary SC7D in the component reference. In particular,

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

All linear-multiplet spinor derivatives and contracted Hessians in §6 have the full L02/SC7D meaning. Equations (4.21), (4.24), (4.27), (4.30), (4.32) of the two-derivative input display the same gauge-evaluated objects term by term.

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

Here $`G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}`$ is the ordinary strength in the Chern–Simons term. The source formula contains the full additional dilatino pieces before gauge fixing; those must be retained whenever that expression is differentiated. The conventional constraints $`R(P)=0`$, $`\gamma^\mu\widehat R_{\mu\nu}(Q)=0`$, and $`e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0`$ determine $`\omega,\phi,f`$. Their explicit expressions, the ordered primed Lorentz curvature, $`\widehat R(Q)`$, $`\widehat R(V)`$ and their variations are R01–R07 in the local reference; they are definitions, not equations of motion of the GB action.

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

Each primary term has conformal weight three and every BF term has weight five. The multiplier is dimensionless. The normalization explanation also displays the complete bosonic scalar/current comparison and the explicit Clifford-pair checks.

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

Every other Weyl coefficient receives the same $`-2`$ and no index permutation. For example, $`(-2)(1/8)=-1/4`$ for $`\widehat C^2`$, $`(-2)(64/3)=-128/3`$ for $`D^2`$, and $`(-2)(-1/3)=2/3`$ for $`\widehat R(V)^2`$. The complete 52 multiplications, with their field expressions, are displayed in the coefficient ledger.

### Step 5. Insert the fully expanded LOG action

<!-- ASSERT_CONVENTION: source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, LOG_bridge=already_applied_once -->

The current LOG action was obtained by substituting all 13 triplet, 94 spinor, 141 scalar, and 373 vector terms of STEP_07 into the seven BF insertions. The assembled input in LOG action §4–§5 contains 297 terms with no explicit physical spinor and 835 explicit bilinears. Its two stored sums are named covariant seed and explicit sum. “No explicit spinor” does not mean “bosonic”: the seed retains all hats and full derivatives.

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

The exact rational assembly script performs only the multiplications just derived, the listed 21 Weyl removals, the explicit barred-spinor substitution, and formatting. The corresponding JSON ledger records input coefficient, multiplier, output coefficient, phase of $`i`$, and original tensor body for every retained higher-derivative term. The hand derivation determines the operations; the script checks and prints their complete arithmetic.

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

This agrees with GB-WEYLOG-DEF-v1, Gold et al. (2025), equations (22)–(23). This checks the normalization of the curvature sector. The complete off-shell action retains the other fields and couplings; no vacuum ansatz is imposed.

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

The quartic-$`T`$ scalar check likewise gives $`-(81/32)(16/3)^4=-2048=(-2)(1024)`$ and $`(33/128)(16/3)^4=5632/27=(-2)(-2816/27)`$. The complete bosonic current comparison, with every divergence term, is GN16 of the normalization explanation.

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

The assembly report, independent verification report, and math rendering report give reproducible outcomes. The normalization checker independently reproduces the 256-entry Clifford-pair identity, three nonzero spinor contractions and a nonzero Weyl-commutator test; its report states the exact scope. The inherited LOG dimensional/free-index audit applies unchanged to its term bodies because multiplying by $`-4`$ changes neither indices nor dimensions. The same statement applies to the retained Weyl bodies. This is not an independent new Fierz, action-reality, or full supersymmetry proof.

<a id="6-final-result"></a>

## Final Result

Under A1–A6, the action through two physical fermions is

```math
\boxed{S^{(0+2)}=\frac1{2\kappa_5^2}\int d^5x\,e\,\ell_{\rm tot}^{(0+2)},\qquad S=S^{(0+2)}+O(\Psi^4),\qquad [\lambda_{\rm GB}]=-2.}
\tag{GB-FINAL-ACTION}
```

The following is the **complete collected density**. It includes the two-derivative action and every retained Weyl/LOG term; it has no invariant-slot placeholders. Full supercovariant tensors, $`T,\chi,D`$, and ordered derivatives retain the definitions in §3 and the anchored component reference. The trailing projection is part of the formula. A source-gauge vertical bar and the overall projection are never instructions to set a differentiated dilatino to zero.

<!-- COLLECTED_ACTION -->

For the fermionic Hessian one takes the degree-two part of this complete density, including the degree-two expansion of the first, covariant-seed terms. This expression is off shell, before background evaluation or auxiliary reduction.

<a id="7-convention-dependence-and-remaining-uncertainties"></a>

## Convention Dependence and Scope

The action assembled here is complete at the specified fermion order **relative to the adopted inputs**. The normalization ambiguity between the OP Weyl action and the target Gold action is resolved by GB16–GB20, including fermions and current terms. It is not being fixed by the curvature check alone.

The assembly uses the adopted FM02 $`8/3`$ coefficient and the specified two-derivative component slots and reality conventions. Its checks establish coefficient assembly and normalization for these inputs through two physical fermions.

No GB background, tadpole cancellation, fermion kernel, eigenmode, norm, stability bound, or degree-of-freedom count has been inferred from this assembly. Those require the separate spectrum workflow applied to this action, with all potentially dynamical auxiliary fields retained.

The source trail is:

- C24: Components of curvature-squared invariants, (4.3), footnote 4, (2.17), (A.4a), and Tables 4–6: complete Weyl primary, bosonic descendants, and component conversion. The inspected local file is arXiv:2311.00679v1 (1 November 2023); “C24” follows the inherited filename.
- Özkan–Pang GB source, (3.1), (5.18), (5.19): density and Weyl construction, read with the explicit project repairs in FM01–FM07.
- The inherited Weyl map, FM01–FM07, and gauged action, GA24: actual adopted component input and its qualification.
- The current LOG construction, SC7L/SC7P/SC7N/SC7E, and assembled LOG density: actual normalized input with the corrected ordinary current.
- The two-derivative construction, (5.5), (5.10): the 2016 linear-map representative retained here. Its local primary source is O16, arXiv:1608.00349v2 (26 November 2016), (3.11)–(3.15), PDF pp.9–10.
- Bosonic GB source lock, Gold (2025) (22)–(23): target normalization and common bosonic comparison.

The source references in this derivation distinguish cited equations from project-derived coefficient repairs.
