# Common quadratic compensator-fermion diagonal block

[Product-background guide](../README.md). This diagonal-block derivation supplies the compensator entry of the current coupled fermionic action.

## Problem and Target

Evaluate the complete contribution of the **higher-derivative invariant** to the $`\zeta`$-$`\zeta`$ diagonal block, before selecting a branch. The calculation extracts terms from [GB-FINAL-DENSITY](../../../action/gb_splus_action.md#6-final-result) with the gravitino fluctuation set to zero solely to read this diagonal entry. It does not impose $`\xi_\mu=0`$ on the eventual coupled physical problem.

Sections 1–6 first collect the higher-derivative diagonal entry. Sections 7–9 add the two-derivative contribution, including the charged compensator derivative. Both gravitino-containing blocks remain necessary for the complete fermionic action and its norms. A diagonal raw kinetic coefficient does not establish a ghost or positivity.

## Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, action_lock=GB-FERMION-ACTION-0+2-v1, fermion_bar=linear_Majorana, fermion_variation=left, SU2_lowering=NWSE, antisymmetrization=unit_weight -->

Let $`\varphi^i=t\zeta^i`$, with odd $`\zeta`$ and even $`t`$. The bar is linear: $`\overline{g\zeta/8}=g\bar\zeta/8`$. Bosonic coefficients are held at the free product background. No fermion equation, fluctuation gauge or branch relation is used.

## Definitions and Required Identities

With $`\xi_\mu=0`$, component GB07, GB10 and R01 give

```math
\phi_a^{(1)}=0,\quad\mathcal D_a\psi^i\big|_1=0,\quad
R'_{ab}(Q)\big|_1=\widehat R_{ab}(Q)\big|_1=0,\quad
\chi^{(1)i}=\frac g8\zeta^i.
\tag{FQ.1}
```

The full higher descendants of the gauge-fixed dilatino also vanish **in this restricted diagonal entry**: their ordinary derivative term differentiates zero; every Q/S connection term is multiplied by $`\xi_\mu`$ or $`\phi_\mu^{(1)}`$; the K term acts on the zero dilatino. This argument is not used in the gravitino-containing blocks, where those descendants are nonzero.

The surviving derivative of the compensator is

```math
D_a^{R}\zeta^i=
\left(\partial_a+\frac14\bar\omega_a{}^{bc}\gamma_{bc}\right)\zeta^i+
\bar\Gamma_a{}^i{}_j\zeta^j,\qquad
\bar\Gamma_a{}^i{}_j=\bar V_a^{ik}\varepsilon_{kj}.
\tag{FQ.2}
```

The plus follows explicitly from $`-V^{ij}\zeta_j=-V^{ij}\zeta^k\varepsilon_{kj}=+V^{ij}\varepsilon_{jk}\zeta^k`$. No $`gC_a`$ is silently added to this independent off-shell connection.

## Detailed Derivation

### 1. Source coverage of this diagonal block

All terms with an explicit or implicit gravitino, $`R(Q)`$, or a differentiated dilatino vanish under (FQ.1). Bosonic-looking $`G,H,D,R(M),R(V)`$ have no $`\zeta^2`$ completion without a gravitino: the relevant bilinears are $`\xi\xi`$ or $`\xi\zeta`$. The full compensator derivatives' Q/S connection corrections are also multiplied by $`\xi,\phi^{(1)}`$. Thus the surviving higher-derivative source entries are exactly:

| Source | Contribution before collection |
|---|---|
| Weyl_sigma_N:15 | $`+\frac{512}{3}\bar\chi\gamma^a\mathcal D_a\chi`$ |
| Weyl_Y:5 | $`+\frac{256i}{3}gL^{ij}\bar\chi_{(i}\chi_{j)}`$ |
| Weyl_C_E:3, its $`\chi^2`$ part | $`+\frac{128i}{3}C_a\nabla_b(\bar\chi\gamma^{ab}\chi)`$ |
| LOG_explicit:27 | $`+\frac{3i}{2}g^2G_{ab}\bar\zeta^i\gamma^{ab}\zeta_i`$ |
| LOG_explicit:28 | $`-3ig^2H^{ab}\bar\zeta^i\gamma_{ab}\zeta_i`$ |
| LOG_explicit:43 | $`-\frac23g^2\bar\zeta^i\gamma_aD^{Ra}\zeta_i`$ |
| LOG_explicit:62 | $`+\frac{17i}{3}g^3L^{ij}\bar\zeta_i\zeta_j`$ |
| LOG_explicit:135 | $`-\frac{10i}{3}g^2C^a\bar\zeta^i\gamma_{ab}D^{Rb}\zeta_i`$ |

The coefficients include the source ledger's recorded phase $`i`$. The complete 835-entry explicit LOG list is filtered by the actual two factors: exactly entries 27,28,43,62,135 contain two compensator spinors and no $`R(Q)`$ or differentiated dilatino. This establishes the coverage of the diagonal entry, not the full fermionic block.

### 2. Substitute $`\chi=g\zeta/8`$

The two numerical products are

```math
\frac{512}{3}\frac g8\frac g8=\frac83g^2,\qquad
\frac{256i}{3}g\frac g8\frac g8=\frac{4i}{3}g^3.
\tag{FQ.3}
```

Therefore the first two rows give

```math
\frac83g^2\bar\zeta\not D^R\zeta+
\frac{4i}{3}g^3L^{ij}\bar\zeta_i\zeta_j.
\tag{FQ.4}
```

Symmetrizing $`i,j`$ in the Weyl row produces no extra factor because $`L^{ij}`$ is already symmetric. The $`\chi`$-current becomes

```math
\frac{128i}{3}C_a\nabla_b(\bar\chi\gamma^{ab}\chi)
=\frac{2i}{3}g^2C_a\nabla_b(\bar\zeta\gamma^{ab}\zeta).
\tag{FQ.5}
```

### 3. Actual bilinear flip for LOG_explicit:135

The contracted rank-two Majorana flip is $`+1`$, since its fixed-index sign is $`t_2=-1`$ and the SU(2) contraction adds a minus. Applied to the actual odd spinors $`D_b^R\zeta`$ and $`\zeta`$,

```math
\overline{D_b^R\zeta}\gamma^{ab}\zeta
=\bar\zeta\gamma^{ab}D_b^R\zeta.
\tag{FQ.6}
```

The derivative of the singlet bilinear therefore has two equal slots:

```math
\nabla_b(\bar\zeta\gamma^{ab}\zeta)
=\overline{D_b^R\zeta}\gamma^{ab}\zeta+\bar\zeta\gamma^{ab}D_b^R\zeta
=2\bar\zeta\gamma^{ab}D_b^R\zeta.
\tag{FQ.7}
```

The connection is compatible with the doublet symplectic form and the Clifford tensor, so it drops out of this fully contracted singlet derivative. Equation (FQ.7) changes the LOG current into

```math
-\frac{10i}{3}g^2C_a\bar\zeta\gamma^{ab}D_b^R\zeta
=-\frac{5i}{3}g^2C_a\nabla_b(\bar\zeta\gamma^{ab}\zeta).
\tag{FQ.8}
```

Add the Weyl coefficient (FQ.5): $`2i/3-5i/3=-i`$. The complete current is $`-ig^2C_a\nabla_b(\bar\zeta\gamma^{ab}\zeta)`$.

### 4. Derivative transfer of the complete current

For $`J^{ab}=\bar\zeta\gamma^{ab}\zeta=-J^{ba}`$, apply the explicit product rule:

```math
-ig^2C_a\nabla_bJ^{ab}
=-ig^2\nabla_b(C_aJ^{ab})+ig^2(\nabla_bC_a)J^{ab}
=-ig^2\nabla_b(C_aJ^{ab})-\frac{i}{2}g^2G_{ab}J^{ab}.
\tag{FQ.9}
```

The last equality is $`(\nabla_bC_a)J^{ab}=(\nabla_bC_a-\nabla_aC_b)J^{ab}/2=-G_{ab}J^{ab}/2`$. The boundary current is displayed, rather than discarded implicitly.

Collect the coefficients of the kinetic, flux and gauging pairings:

```math
\begin{aligned}
\bar\zeta\not D^R\zeta:&\quad \frac83g^2-\frac23g^2=2g^2,\\
G_{ab}\bar\zeta\gamma^{ab}\zeta:&\quad \frac{3i}{2}g^2-\frac i2g^2=ig^2,\\
H_{ab}\bar\zeta\gamma^{ab}\zeta:&\quad -3ig^2,\\
L^{ij}\bar\zeta_i\zeta_j:&\quad \frac{4i}{3}g^3+\frac{17i}{3}g^3=7ig^3.
\end{aligned}
\tag{FQ.10}
```

### 5. Put the free product background into the collected entry

The doublet contraction is $`\bar\zeta\Gamma\zeta=\bar\zeta^i\Gamma\zeta_i`$. Lowering both indices separately in the last pairing gives $`\delta^{ij}\bar\zeta_i\zeta_j=\delta_{ij}\bar\zeta^i\zeta^j`$, because the two lowering matrices multiply to the identity in this symmetric contraction. Hence

```math
\ell^{(2)}_{{\rm GB},\zeta\zeta}
\doteq 2g^2\bar\zeta\not D^R\zeta+
ig^2(G_{ab}-3H_{ab})\bar\zeta\gamma^{ab}\zeta+
\frac{7ig^3L}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j
=2g^2\bar\zeta\not D^R\zeta+
2ig^2(p-3h)\bar\zeta\gamma^{34}\zeta+
\frac{7ig^3L}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j.
\tag{FQ.11}
```

The factor two in the flux term is $`G_{34}\gamma^{34}+G_{43}\gamma^{43}=p\gamma^{34}+(-p)(-\gamma^{34})=2p\gamma^{34}`$; the same arithmetic holds for $`H`$. The full action contains $`\lambda`$ times (FQ.11).

### 6. Both Majorana variation slots

For the derivative pairing, variation followed by one integration by parts gives

```math
\delta(\bar\zeta\not D^R\zeta)=
\delta\bar\zeta\not D^R\zeta+\bar\zeta\gamma^aD_a^R\delta\zeta
=\delta\bar\zeta\not D^R\zeta
+\nabla_a(\bar\zeta\gamma^a\delta\zeta)
-\overline{D_a^R\zeta}\gamma^a\delta\zeta.
\tag{FQ.12}
```

The contracted rank-one flip is $`-1`$, so the last term is $`+\delta\bar\zeta\gamma^aD_a^R\zeta`$. The bulk variation is $`2\delta\bar\zeta\not D^R\zeta`$. The algebraic rank-two pairing has the $`+1`$ flip (FQ.6), so its two slots also add. The fixed-upper scalar pairing uses $`t_0=+1`$ and symmetric $`\delta_{ij}`$, again giving two equal slots.

The restricted higher-derivative diagonal equation, written with $`\delta\bar\zeta^i`$ on the left, is

```math
\left.\mathcal E_{{\rm GB},\zeta i}\right|_{\xi=0}
=4g^2\not D^R\zeta_i+
4ig^2(p-3h)\gamma^{34}\zeta_i+
\frac{14ig^3L}{\sqrt2}\delta_{ij}\zeta^j.
\tag{FQ.13}
```

It is not the full gravitino-coupled $`\zeta`$ equation.

### 7. Two-derivative source insertions on the same free background

Use a local Stückelberg gauge with the background three-form potential $`E_3=0`$. This is possible because $`d\bar E_3=0`$; its flux contribution is transferred to the two-form potential, preserving $`\bar H_3`$. It is a gauge representative for extracting this fermion block, not a restriction on the independent fluctuation $`e_3`$. The physical background current $`E_a`$ is zero. Its quadratic fermion completion contains $`\xi\zeta`$ and $`\xi\xi`$, so it vanishes in this diagonal extraction.

To avoid mixing two SU(2) matrix conventions, define the **lowering matrix** here explicitly:

```math
J_\ell=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\zeta_i=(J_\ell)_{ij}\zeta^j,\quad J_\ell^T=-J_\ell,\quad J_\ell^2=-1.
\tag{FQ.14}
```

The $`J`$ used in Step 5.5 acts as $`\varepsilon^{ij}`$ and is $`-J_\ell`$; these are the two different index maps, not a change in convention. Decompose the accepted connection matrix into its antisymmetric and symmetric parts:

```math
\Gamma_a=\Gamma_{\parallel a}+\Gamma_{\perp a},\quad
\Gamma_{\parallel a}^T=-\Gamma_{\parallel a},\quad
\Gamma_{\perp a}^T=\Gamma_{\perp a},\quad
\Gamma_{\perp a}J_\ell=-J_\ell\Gamma_{\perp a}.
\tag{FQ.15}
```

Both parts are traceless SU(2) matrices. For $`L^{ij}=L\delta^{ij}/\sqrt2`$, with $`L`$ constant, the source triplet derivative is

```math
\mathcal L_{a,ij}:=(\mathcal D_aL_{ij})_0
=-\frac L{\sqrt2}(\Gamma_a+\Gamma_a^T)_{ij}
=-\sqrt2 L\,\Gamma_{\perp a,ij},\qquad
\delta^{ij}\mathcal L_{a,ij}=0.
\tag{FQ.16}
```

For clarity, the upper triplet derivative is $`+L(\Gamma_a+\Gamma_a^T)/\sqrt2`$, from L02. Lowering its two indices separately gives $`J_\ell^T(\mathcal D_aL^{\cdot\cdot})J_\ell=-L(\Gamma_a+\Gamma_a^T)/\sqrt2`$, which proves (FQ.16)'s sign. This is nonzero on the charged connection class.

The source two-form is $`\mathcal F_{ab}=\bar G_{ab}-2\bar H_{ab}`$: the accepted definition $`H^{ab}=-\varepsilon^{abcde}H_{cde}/12`$ gives $`\varepsilon_{abcde}H^{cde}/6=-2H_{ab}`$. Contract the first scalar brace of GB-FINAL-DENSITY with $`L\delta^{ij}/\sqrt2`$, retaining only two $`\zeta`$'s. Its entries, **before** the outer factor $`-2`$, are

```math
\mathcal A_{\zeta\zeta}
=\frac1L\bar\zeta\not D^R\zeta
-\frac{\sqrt2 iN}{L^2}\delta_{ij}\bar\zeta^i\zeta^j
+\frac{i}{4L}\mathcal F_{ab}\bar\zeta\gamma^{ab}\zeta
-\frac1{\sqrt2L^2}\bar\zeta^i\gamma^a\mathcal L_{a,ij}(J_\ell\zeta)^j.
\tag{FQ.17}
```

The $`N`$ coefficient is $`iN/(\sqrt2L^2)-3iN/(\sqrt2L^2)=-\sqrt2 iN/L^2`$. The flux coefficient is $`(L/\sqrt2)\,(i/(4\sqrt2))L^{-2}\,\delta^{ij}\delta_{ij}=i/(4L)`$. The two explicit $`\chi\zeta`$ coefficients are $`-16i/\sqrt2+16i/\sqrt2=0`$. The three triplet-derivative insertions have coefficients

```math
-\frac3{2\sqrt2L^2}\bar\zeta^i\gamma^a\mathcal L_{a,ij}(J_\ell\zeta)^j
+\frac1{2\sqrt2L^2}\bar\zeta^i\gamma^a\mathcal L_{a,ij}(J_\ell\zeta)^j+0,
\tag{FQ.18}
```

where the zero is the trace in (FQ.16); their sum is the last term of (FQ.17). The conformal boxes and $`D`$ have no $`\zeta^2`$ term when $`\xi=\phi^{(1)}=0`$. Thus no implicit two-derivative term has been omitted.

The upper-index composite spinor actually printed in the action evaluates to

```math
\Lambda^{(1)}
=-\frac{2i}{L}\not D^R\zeta
+\frac1{2L}\gamma^{ab}\mathcal F_{ab}\zeta
+\sqrt2\left(\frac N{L^2}-g\right)J_\ell\zeta
-\frac{\sqrt2 i}{L^2}J_\ell\gamma^a\mathcal L_aJ_\ell\zeta.
\tag{FQ.19}
```

For its last term, raise the source expression explicitly: $`\varepsilon^{ir}=-J_{\ell,ir}`$, $`\delta^{st}\zeta_t=(J_\ell\zeta)^s`$, and $`2iL^{-3}(L/\sqrt2)=\sqrt2i/L^2`$. Their product is the last term of (FQ.19).

### 8. Bar, transfer, and collection of the two-derivative entry

For the derivative term in $`i\bar\Lambda\zeta`$, integrate by parts once:

```math
\frac2L\overline{D_a^R\zeta}\gamma^a\zeta
=-\frac2L\bar\zeta\not D^R\zeta
+\frac2L\nabla_a(\bar\zeta\gamma^a\zeta).
\tag{FQ.20}
```

The rank-two bar identity $`\overline{\gamma^{ab}\zeta}=-\bar\zeta\gamma^{ab}`$ gives the flux coefficient $`-i/(2L)`$. For the scalar map $`J_\ell`$, $`J_\ell^TJ_\ell=1`$. For the triplet derivative, $`\mathcal L_a^T=\mathcal L_a`$ and $`\mathcal L_aJ_\ell=-J_\ell\mathcal L_a`$ give

```math
(J_\ell\mathcal L_aJ_\ell)^TJ_\ell=-J_\ell\mathcal L_a
=\mathcal L_aJ_\ell.
\tag{FQ.21}
```

Consequently

```math
i\bar\Lambda\zeta\doteq
-\frac2L\bar\zeta\not D^R\zeta
-\frac{i}{2L}\mathcal F_{ab}\bar\zeta\gamma^{ab}\zeta
+i\sqrt2\left(\frac N{L^2}-g\right)\delta_{ij}\bar\zeta^i\zeta^j
+\frac{\sqrt2}{L^2}\bar\zeta^i\gamma^a\mathcal L_{a,ij}(J_\ell\zeta)^j.
\tag{FQ.22}
```

The last source product in the two-derivative brace, $`\rho N`$, contributes $`iN\delta_{ij}\bar\zeta^i\zeta^j/(\sqrt2L^2)`$. The explicit $`-4g`$ brace has no two-$`\zeta`$ term. Add (FQ.17), (FQ.22) and this product, then multiply by $`-2`$:

```math
\begin{aligned}
\ell^{(2)}_{2\partial,\zeta\zeta}\doteq{}&
\frac2L\bar\zeta\not D^R\zeta
+\frac{i}{2L}(G_{ab}-2H_{ab})\bar\zeta\gamma^{ab}\zeta
+\sqrt2i\left(2g-\frac N{L^2}\right)\delta_{ij}\bar\zeta^i\zeta^j\\
&-\frac{\sqrt2}{L^2}\bar\zeta^i\gamma^a\mathcal L_{a,ij}(J_\ell\zeta)^j.
\end{aligned}
\tag{FQ.23}
```

There is no branch equation in this result. Substitute (FQ.16) into its last term. Its connection matrix is $`+(2/L)\Gamma_{\perp a}J_\ell=-(2/L)J_\ell\Gamma_{\perp a}`$, while the connection part of the first term is $`+(2/L)J_\ell(\Gamma_{\parallel a}+\Gamma_{\perp a})`$. The charged connection cancels in this **two-derivative diagonal entry**:

```math
\ell^{(2)}_{2\partial,\zeta\zeta}\doteq
\frac2L\bar\zeta\not D^\parallel\zeta
+\frac{i}{2L}(G_{ab}-2H_{ab})\bar\zeta\gamma^{ab}\zeta
+\sqrt2i\left(2g-\frac N{L^2}\right)\delta_{ij}\bar\zeta^i\zeta^j,\qquad
D^\parallel_a=\nabla_a|_{\rm spin}+\Gamma_{\parallel a}.
\tag{FQ.24}
```

The higher-derivative term (FQ.11) retains $`D^R`$. Cancellation in (FQ.24) is not permission to delete the charged connection from other fermionic blocks.

### 9. Complete diagonal entry and its evaluated equation

Define $`K=L^{-1}+\lambda g^2`$, and

```math
M_F=\sqrt2\left(2g-\frac N{L^2}\right)+\frac{7\lambda g^3L}{\sqrt2},\qquad
P_F=\frac{p-2h}{L}+2\lambda g^2(p-3h).
\tag{FQ.25}
```

The sum of (FQ.11) and (FQ.24) is

```math
\boxed{\ell^{(2)}_{\zeta\zeta}\doteq
2K\bar\zeta\not D^\parallel\zeta
+2\lambda g^2\bar\zeta\gamma^a\Gamma_{\perp a}\zeta
+iP_F\bar\zeta\gamma^{34}\zeta
+iM_F\delta_{ij}\bar\zeta^i\zeta^j.}
\tag{FQ.26}
```

Every algebraic pairing has two equal varied slots, as does the derivative after the transfer (FQ.12). The evaluated diagonal Euler entry is therefore

```math
\boxed{\left.\mathcal E_{\zeta i}\right|_{\xi=0}
=4K\not D^\parallel\zeta_i
+4\lambda g^2\gamma^a(\Gamma_{\perp a}\zeta)_i
+2iP_F\gamma^{34}\zeta_i+2iM_F\delta_{ij}\zeta^j.}
\tag{FQ.27}
```

At $`d=1+\lambda g^2L=0`$ its diagonal derivative term vanishes. The charged connection term may remain. This is an entry-wise statement; the gravitino mixing also enters the rank of the full constrained kinetic system.

## Consistency Checks

All three source-invariant densities in (FQ.11) have dimension four: $`2+1/2+1+1/2=4`$, $`2+1+1=4`$, and $`3+0+1=4`$. Multiplication by $`\lambda`$ gives dimension two. The transferred boundary current in (FQ.9) has dimension three before its divergence, giving four afterward.

The current coefficient is checked both before and after transfer: $`2/3-5/3=-1`$, then $`-1`$ times the antisymmetric derivative-transfer factor $`1/2`$ gives the $`-i/2`$ correction in (FQ.10). No Dirac-bar conjugation of $`i`$ is used. The independent odd variation retains both slots in (FQ.12).

The fluxless specialization of this **entry** gives $`2g^2\bar\zeta\not D^R\zeta+7ig^3L\delta_{ij}\bar\zeta^i\zeta^j/\sqrt2`$, matching the corresponding entries of the AdS5 GB fermion action (FC11). This comparison substitutes $`p=h=0`$ only into the displayed pairing, without importing the AdS$`_5`$ operator or adding an excluded zero-coupling branch.

## Final Result

Equation (FQ.26) is the complete two-derivative plus higher-derivative $`\zeta`$-$`\zeta`$ raw diagonal entry on both connection classes. Equation (FQ.27) evaluates its graded Euler entry. The higher-derivative part's eight surviving source insertions and current boundary are collected in (FQ.11).


## Relation to the coupled action

The gravitino mixing and gravitino diagonal entries are supplied in the [coupled fermionic action](../fermionic_quadratic_action.md). The diagonal coefficient (FQ.26) alone does not determine physical fermion norms.