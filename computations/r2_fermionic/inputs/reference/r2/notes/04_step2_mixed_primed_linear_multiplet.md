# Step 2 — Mixed primed linear multiplet

## 1. Problem and Target

Construct $`(L'_{ij},\varphi'_i,E'^a,N')`$ by applying the specified coefficients to **Özkan 2016, Eq. (3.20), with the project-derived scalar-gradient phase repair** `R2-VL-GRADIENT-PHASE-v1`. Both vector arguments remain in vector-component notation. The [confirmed framework](00_action_construction_framework.md) fixes this as Step 2; [Step 1](03_step1_full_primed_BF_density.md) fixes the primed BF density into which these components will later be inserted.

**Primary source inspected:** Özkan, _Off-Shell N=2 Linear Multiplets in Five Dimensions_ ([arXiv:1608.00349v2](../../../../../../references/bibliography.md#Ozkan2016)), Eq. (3.20), printed pp. 9–10 / PDF pp. 10–11. The definitions in (3.9)–(3.10), (3.12)–(3.13) were checked on PDF p. 9, and the scalar d'Alembertian (3.21) on PDF p. 11. The constrained-component convention (3.2)–(3.3) is on PDF p. 8.

**Assumptions and scope**

- **A1.** Use the tensor structures of Eq. (3.20), replacing only the scalar-gradient coefficient $`+1/2`$ by $`+i/2`$ in the working map, off shell and without gauge fixing, field equations, integration by parts, or fermion truncation. The restricted rigid test below proves this necessary phase; it does not reconstruct the entire local map by repeated supersymmetry transformations.
- **A2.** Label 1 is primed and label 2 is unprimed, in either slot $`B`$ or $`C`$. Fix the output $`A=1`$. Only $`C_{112}=C_{121}=1/2`$ contribute; $`C_{111}=C_{122}=0`$. No sum over $`A`$ or extra entries $`C_{2BC}`$ are introduced.
- **A3.** Keep the two vector roles and all their derivatives distinct. Gold (4) and the earlier linear-to-vector map are not substituted in this step. Their eventual input is the same original unprimed linear multiplet, which is distinct from this new primed output.
- **A4.** Every background $`T_{ab},\chi^i,D`$ denotes the common **gauged Coomans–Özkan** composite fixed in the framework: respectively (5.6), (5.3), (5.4), together with the gauged three-form (5.7). These background slots remain unexpanded here, including inside supercovariant derivatives. No unknown source-omitted higher-fermion term is set to zero.
- **A5.** Equalities below are local component equalities. All fermion ordering changes are displayed. Formal identical-vector and zero-vector tests in Section 5 are algebra checks, not identifications imposed on the physical construction.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Use [the branch conventions](../../../../derivations/component_conventions.md) and the inherited [convention handoff, Sections 2–3](../../../../../../common/README.md). They agree with Step 1. The following definitions are result-sensitive here.

| Item | Convention |
|---|---|
| Dimension and signature | Five dimensions, $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$; $`\hbar=c=1`$ |
| Indices | $`a,b,c,d,e`$ and $`\mu,\nu,\ldots`$ run from 0 to 4; $`i,j=1,2`$ are $`SU(2)`$ indices; $`B,C=1,2`$ label vectors |
| Raising and lowering | Tangent indices use $`\eta`$; world indices use $`g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}`$; $`SU(2)`$ uses the NW–SE epsilon convention below |
| Symmetrization | Unit weight; parentheses carry $`1/2`$ for a pair. Antisymmetrized gamma matrices include $`1/p!`$ |
| Orientation and gamma matrices | $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$ in the frame; $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$ and $`\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1`$ |
| Spinors | Grassmann-odd symplectic Majorana; operational bar $`\bar\lambda^i=(\lambda^i)^T C`$; no Dirac-bar conversion or chirality projection |
| Charge conjugation | $`C^T=-C`$, $`\gamma_a^T=C\gamma_aC^{-1}`$, $`(C\gamma_a)^T=-C\gamma_a`$, $`(C\gamma_{ab})^T=+C\gamma_{ab}`$; their role in flips is derived below |
| Conjugation scope | No Hermitian conjugation is performed. The explicit matrix check may choose unitary $`C`$; a $`C^\dagger`$ phase is not used to change any source term |
| Derivatives | $`\mathcal D`$ is the source supercovariant derivative, an even derivation; $`\Box_c`$ is source (3.21). Do not identify it with an ordinary Laplacian |
| Connections and torsion | Source dependent second-order $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$ are retained; $`\omega`$ includes fermionic contorsion |
| Curvature | Inherited $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\alpha\vert}\Gamma^\alpha_{\nu]\sigma}`$, $`R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}`$; no curvature commutator is used |
| Gauge representation | Abelian vector slots, as in (3.9); physical gauging enters through the fixed gauged background and later maps. No Yang–Mills structure constants are added |
| Normalization | The only new weights are the specified $`C_{1BC}`$. No BF normalization or higher-derivative coupling is inserted |
| Fermionic variations | The rigid component SUSY test below uses a Grassmann-odd parameter and even $`\delta_\epsilon`$; no action or left/right functional derivative is invoked |

The scalar auxiliary $`D`$ and the derivative $`\mathcal D`$ are different symbols. The charge-conjugation matrix $`C`$, the coefficient tensor $`C_{1BC}`$, and the slot index $`C`$ have different roles; no new field is denoted by them. The gravitino is $`\psi_\mu^i`$ and remains unprimed. The S connection is $`\phi_\mu^i`$, distinct from the output fermion $`\varphi'_i`$.

The derivative definitions used by the calculation are stated explicitly below. Metric, units, spinor ordering and coupling conventions are those in the table above. Fourier transforms, state normalization and renormalization do not enter this classical local calculation.

## 3. Definitions and Required Identities

### 3.1 Arguments and coefficient selection

```math
\begin{aligned}
(\rho^1,\lambda_i^1,Y_{ij}^1,A_\mu^1,\widehat F_{ab}^1)
&=(\rho',\lambda'_i,Y'_{ij},A'_\mu,\widehat F'_{ab}),\\
(\rho^2,\lambda_i^2,Y_{ij}^2,A_\mu^2,\widehat F_{ab}^2)
&=(\rho,\lambda_i,Y_{ij},A_\mu,\widehat F_{ab}),\\
(L_{ij,1},\varphi_{i,1},E_1^a,N_1)&=(L'_{ij},\varphi'_i,E'^a,N'),\\
C_{111}=C_{122}&=0,\qquad C_{112}=C_{121}=\frac12.
\end{aligned}
\tag{1}
```

Thus $`(B,C)=(1,2)`$ means primed/unprimed, while $`(2,1)`$ means unprimed/primed. Differentiation preserves the label: for example $`\mathcal D_a\rho^1=\mathcal D_a\rho'`$ and $`\mathcal D_a\rho^2=\mathcal D_a\rho`$.

### 3.2 Printed source map and explicitly repaired working map

```math
L_{ij,A}=\sum_{B,C}C_{ABC}
\left(2\rho^B Y_{ij}^C-\frac i2\bar\lambda^B_{(i}\lambda^C_{j)}\right).
\tag{2}
```

```math
\begin{aligned}
\left.\varphi_{i,A}\right|_{\rm printed}=\sum_{B,C}C_{ABC}\bigg(&i\rho^B\not{\mathcal D}\lambda_i^C
+2\rho^B\gamma\!\cdot\!T\lambda_i^C-8\rho^B\rho^C\chi_i\\
&-\frac14\gamma\!\cdot\!\widehat F^B\lambda_i^C
+\frac12(\not{\mathcal D}\rho^B)\lambda_i^C-Y_{ij}^B\lambda^{jC}\bigg).
\end{aligned}
\tag{3}
```

The printed coefficient is $`+1/2`$. It is preserved in Eq. (3) as source evidence, but the coefficient used in every calculation below is $`+i/2`$:

```math
\begin{aligned}
\varphi_{i,A}=\sum_{B,C}C_{ABC}\bigg(&i\rho^B\not{\mathcal D}\lambda_i^C
+2\rho^B\gamma\!\cdot\!T\lambda_i^C-8\rho^B\rho^C\chi_i\\
&-\frac14\gamma\!\cdot\!\widehat F^B\lambda_i^C
+\frac i2(\not{\mathcal D}\rho^B)\lambda_i^C-Y_{ij}^B\lambda^{jC}\bigg).
\end{aligned}
\tag{3a}
```

To establish the phase, isolate the term with $`\partial_a\rho'`$ and an unprimed gaugino in a flat rigid **test** of the universal map, at fixed Standard-Weyl background. Take $`Y=Y'=\widehat F=\widehat F'=T=\chi=0`$, $`\lambda'=0`$, $`\lambda`$ constant and $`\rho`$ constant, with nonzero $`\partial_a\rho'`$. This is a test of an independent tensor coefficient, not a restriction imposed on the gauged construction. Coomans–Özkan (2.15), (2.20), on PDF p. 7  and PDF p. 8, fix $`\delta\lambda'_i=-i(\not\partial\rho')\epsilon_i/2`$ and $`\delta L'_{ij}=i\bar\epsilon_{(i}\varphi'_{j)}`$. The operational bar takes a transpose without complex conjugating $`i`$:

```math
\begin{aligned}
\delta\bar\lambda'_i
&=(\delta\lambda'_i)^TC
=-\frac i2\epsilon_i^T(\not\partial\rho')^TC
=-\frac i2\bar\epsilon_i(\not\partial\rho'),\\
\delta L'_{ij}\big|_{\partial\rho'\lambda}
&=-\frac i2(\delta\bar\lambda'_{(i})\lambda_{j)}
=\left(-\frac i2\right)\left(-\frac i2\right)
\bar\epsilon_{(i}(\not\partial\rho')\lambda_{j)}\\
&=-\frac14\bar\epsilon_{(i}(\not\partial\rho')\lambda_{j)}.
\end{aligned}
\tag{3b}
```

Here $`(\gamma^a)^TC=C\gamma^a`$ was inserted in the first line. No spinor interchange or complex conjugation is used. The varied scalar–triplet products vanish in this selected tensor sector: their triplets and the derivatives of their gauginos vanish. The variation of the second spinor in $`\bar\lambda'\lambda`$ is multiplied by $`\lambda'=0`$. If $`c`$ denotes a numerical coefficient, not a field, its required value is therefore

```math
\begin{aligned}
\varphi'_i\big|_{\partial\rho'\lambda}
&=c(\not\partial\rho')\lambda_i,\\
i c&=-\frac14,
\qquad c=\frac{-1/4}{i}=\frac i4,\\
\left.ic\right|_{c=1/4}&=\frac i4\ne-\frac14,
\qquad\left.ic\right|_{c=i/4}=-\frac14.
\end{aligned}
\tag{3c}
```

Exchanging the vector roles and using the symmetric scalar-triplet bilinear identity (14) gives the same coefficient for $`(\not\partial\rho)\lambda'_i`$. The general coefficient in Eq. (3a) is $`i/2`$ because the selected ordered weight is $`1/2`$. The change from the printed specialization is explicitly

```math
\begin{aligned}
\frac12\frac i2&=\frac i4,\\
\varphi'_i-\left.\varphi'_i\right|_{\rm printed}
&=\frac{i-1}{4}\left[(\not{\mathcal D}\rho')\lambda_i
+(\not{\mathcal D}\rho)\lambda'_i\right].
\end{aligned}
\tag{3d}
```

This fixes the necessary coefficient under the declared transformations. The promotion from the isolated derivative to its source-supercovariant tensor structure keeps the rest of the map fixed; the full local transformation at every fermion order is outside this calculation. In particular this argument neither changes the $`E`$ derivative-bilinear coefficient nor removes the $`Y^B Y^C`$ term in $`N`$.

```math
\begin{aligned}
E_A^a=\sum_{B,C}C_{ABC}\bigg[\mathcal D_b\bigg(&-\rho^B\widehat F^{abC}
+8\rho^B\rho^C T^{ab}-\frac i4\bar\lambda^B\gamma^{ab}\lambda^C\bigg)\\
&-\frac18\varepsilon^{abcde}\widehat F_{bc}^B\widehat F_{de}^C\bigg].
\end{aligned}
\tag{4}
```

```math
\begin{aligned}
N_A=\sum_{B,C}C_{ABC}\bigg[&\rho^B\Box_c\rho^C
+\frac12\mathcal D_a\rho^B\mathcal D^a\rho^C
-\frac14\widehat F_{ab}^B\widehat F^{abC}+Y_{ij}^B Y^{ijC}\\
&+8\rho^B\widehat F_{ab}^C T^{ab}
-4\rho^B\rho^C\left(D+\frac{26}{3}T^2\right)\\
&-\frac12\bar\lambda^B\not{\mathcal D}\lambda^C
+i\bar\lambda^B\gamma\!\cdot\!T\lambda^C
+16i\rho^B\bar\chi\lambda^C\bigg].
\end{aligned}
\tag{5}
```

Replacing the dummy world derivative index of the source's contracted scalar-gradient term by a tangent index does not alter it: $`\mathcal D_\mu\rho^B\mathcal D^\mu\rho^C=\mathcal D_a\rho^B\mathcal D^a\rho^C`$ by insertion of the inverse frames and $`g^{\mu\nu}=e_a{}^\mu e_b{}^\nu\eta^{ab}`$.

### 3.3 Gamma contractions and source supercovariant quantities

```math
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},\qquad
\gamma\!\cdot\!\widehat F=\gamma^{ab}\widehat F_{ab},\qquad
T^2=T_{ab}T^{ab},\qquad
\not{\mathcal D}=\gamma^a\mathcal D_a.
\tag{6}
```

There is no extra $`1/2`$ in a gamma dot. For example $`\gamma\!\cdot\!\widehat F'\lambda_i=\gamma^{ab}\widehat F'_{ab}\lambda_i`$. Source (3.9)–(3.10) define the unprimed entries by

```math
\begin{aligned}
\widehat F_{\mu\nu}&=2\partial_{[\mu}A_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda
+\frac i2\rho\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\rho&=(\partial_\mu-b_\mu)\rho-\frac i2\bar\psi_\mu\lambda,\\
\mathcal D_\mu\lambda^i&=(\partial_\mu-\tfrac32b_\mu)\lambda^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\lambda^i-V_\mu{}^{ij}\lambda_j
+\frac14\gamma\!\cdot\!\widehat F\psi_\mu^i\\
&\quad+\frac i2(\not{\mathcal D}\rho)\psi_\mu^i+Y^{ij}\psi_{\mu j}
-\rho\gamma\!\cdot\!T\psi_\mu^i-\rho\phi_\mu^i.
\end{aligned}
\tag{7}
```

Priming just the vector slots gives the separately defined primed entries:

```math
\begin{aligned}
\widehat F'_{\mu\nu}&=2\partial_{[\mu}A'_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda'
+\frac i2\rho'\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\rho'&=(\partial_\mu-b_\mu)\rho'-\frac i2\bar\psi_\mu\lambda',\\
\mathcal D_\mu\lambda'^i&=(\partial_\mu-\tfrac32b_\mu)\lambda'^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\lambda'^i-V_\mu{}^{ij}\lambda'_j
+\frac14\gamma\!\cdot\!\widehat F'\psi_\mu^i\\
&\quad+\frac i2(\not{\mathcal D}\rho')\psi_\mu^i+Y'^{ij}\psi_{\mu j}
-\rho'\gamma\!\cdot\!T\psi_\mu^i-\rho'\phi_\mu^i.
\end{aligned}
\tag{8}
```

For both labels, lower the derivative spinor with $`\mathcal D_\mu\lambda_i=(\mathcal D_\mu\lambda^j)\varepsilon_{ji}`$ and $`\mathcal D_\mu\lambda'_i=(\mathcal D_\mu\lambda'^j)\varepsilon_{ji}`$. No single-index lowering is performed with a Kronecker delta. The tangent strengths are obtained by two inverse frames, not by changing their supercovariant completions.

The two scalar d'Alembertians, retaining every term of source (3.21), are

```math
\begin{aligned}
\Box_c\rho={}&(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\rho
-\frac i2\bar\psi_a\mathcal D^a\lambda-2\rho\bar\psi_a\gamma^a\chi\\
&+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda
+\frac12\bar\phi_a\gamma^a\lambda+2f_a{}^a\rho,\\
\Box_c\rho'={}&(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\rho'
-\frac i2\bar\psi_a\mathcal D^a\lambda'-2\rho'\bar\psi_a\gamma^a\chi\\
&+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda'
+\frac12\bar\phi_a\gamma^a\lambda'+2f_a{}^a\rho'.
\end{aligned}
\tag{9}
```

These definitions make the retained supercovariant notation explicit. They do not expand either vector into its eventual underlying linear or Dilaton-Weyl fields. In particular neither $`\widehat F'`$ nor $`\mathcal D\lambda'`$ is replaced by an unprimed entry.

### 3.4 Derive precisely the spinor flips that will be used

Write spinor matrix indices as $`\alpha,\beta`$ in this paragraph only. For odd spinors $`u,v`$ and an ordinary matrix $`M`$, the interchange is

```math
u_\alpha M_{\alpha\beta}v_\beta
=-v_\beta M_{\alpha\beta}u_\alpha
=-v_\alpha(M^T)_{\alpha\beta}u_\beta.
\tag{10}
```

The first minus sign is Grassmann parity; the second equality just relabels the dummy matrix indices. For $`M=C`$ and $`M=C\gamma^{ab}`$, their transpose symmetries therefore give

```math
\bar u_i v_j=+\bar v_j u_i,\qquad
\bar u^i\gamma^{ab}v^j=-\bar v^j\gamma^{ab}u^i.
\tag{11}
```

For completeness the rank-two transpose follows directly from the ledger:

```math
\begin{aligned}
(\gamma^{ab})^T
&=\frac12\big((\gamma^b)^T(\gamma^a)^T-(\gamma^a)^T(\gamma^b)^T\big)
=-C\gamma^{ab}C^{-1},\\
(C\gamma^{ab})^T&=(\gamma^{ab})^TC^T
=(-C\gamma^{ab}C^{-1})(-C)=C\gamma^{ab}.
\end{aligned}
\tag{12}
```

An NW–SE contraction contains another antisymmetric epsilon. Using $`v_i=v^j\varepsilon_{ji}`$ gives

```math
\begin{aligned}
\bar u\gamma^{ab}v
&=\bar u^i\gamma^{ab}v^j\varepsilon_{ji}
=-\bar v^j\gamma^{ab}u^i\varepsilon_{ji}\\
&=-\bar v^i\gamma^{ab}u^j\varepsilon_{ij}
=+\bar v^i\gamma^{ab}u^j\varepsilon_{ji}
=\bar v\gamma^{ab}u.
\end{aligned}
\tag{13}
```

Here the third expression relabels $`i\leftrightarrow j`$, and the next uses $`\varepsilon_{ij}=-\varepsilon_{ji}`$. Thus the contracted rank-two mixed bilinear is **symmetric** under exchanging the two spinors. Multiplying this identity by the even $`T_{ab}`$ also proves $`\bar u\gamma\!\cdot\!T v=\bar v\gamma\!\cdot\!T u`$.

The scalar-triplet bilinear instead uses fixed lower indices and explicit symmetrization:

```math
\begin{aligned}
\bar\lambda_{(i}\lambda'_{j)}
&=\frac12\big(\bar\lambda_i\lambda'_j+\bar\lambda_j\lambda'_i\big)\\
&=\frac12\big(\bar\lambda'_j\lambda_i+\bar\lambda'_i\lambda_j\big)
=\bar\lambda'_{(i}\lambda_{j)}.
\end{aligned}
\tag{14}
```

No Fierz identity is needed. No rank-one derivative bilinear is exchanged to move a derivative onto the other spinor.

## 4. Detailed Derivation

### 4.1 Enumerate all coefficient slots before collecting anything

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

Each working-map line contains the four ordered pairs $`(1,1),(1,2),(2,1),(2,2)`$. Multiplication by $`C_{111}=0`$ eliminates every $`(1,1)`$ term; multiplication by $`C_{122}=0`$ eliminates every $`(2,2)`$ term. For any displayed product in that line, the surviving operation is exactly

```math
\sum_{B,C=1}^{2} C_{1BC}\,[\text{working product with }B,C]
=\frac12[\text{working product with }B=1,C=2]
+\frac12[\text{working product with }B=2,C=1].
\tag{15}
```

This notation describes a sum, not a new field. The two brackets are written out for each component below. A source coefficient such as $`2`$ is multiplied once by each $`1/2`$; it is not first doubled by an additional symmetry prescription.

### 4.2 Derive $`L'_{ij}`$

Insert both assignments into the full source triplet:

```math
\begin{aligned}
L'_{ij}={}&\underbrace{\frac12\left(2\rho'Y_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)}_{(B,C)=(1,2)}\\
&+\underbrace{\frac12\left(2\rho Y'_{ij}-\frac i2\bar\lambda_{(i}\lambda'_{j)}\right)}_{(B,C)=(2,1)}.
\end{aligned}
\tag{16}
```

Distribute the two weights, including the source factor 2:

```math
\begin{aligned}
\frac12(2\rho'Y_{ij})+\frac12(2\rho Y'_{ij})&=\rho'Y_{ij}+\rho Y'_{ij},\\
\frac12\left(-\frac i2\bar\lambda'_{(i}\lambda_{j)}\right)
+\frac12\left(-\frac i2\bar\lambda_{(i}\lambda'_{j)}\right)
&=-\frac i4\bar\lambda'_{(i}\lambda_{j)}-\frac i4\bar\lambda_{(i}\lambda'_{j)}\\
&=-\frac i2\bar\lambda'_{(i}\lambda_{j)}.
\end{aligned}
\tag{17}
```

The last equality uses the displayed triplet flip, Eq. (14). Thus the assembled triplet is

```math
L'_{ij}=\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}.
\tag{18}
```

The two scalar–triplet products are not equal to each other in the current variables and are both retained.

### 4.3 Derive $`\varphi'_i`$

The complete two ordered contributions of the repaired working map (3a) are

```math
\begin{aligned}
\varphi'_i={}&\frac12\bigg[i\rho'\not{\mathcal D}\lambda_i
+2\rho'\gamma\!\cdot\!T\lambda_i-8\rho'\rho\chi_i
-\frac14\gamma\!\cdot\!\widehat F'\lambda_i
+\frac i2(\not{\mathcal D}\rho')\lambda_i-Y'_{ij}\lambda^j\bigg]_{(1,2)}\\
&+\frac12\bigg[i\rho\not{\mathcal D}\lambda'_i
+2\rho\gamma\!\cdot\!T\lambda'_i-8\rho\rho'\chi_i
-\frac14\gamma\!\cdot\!\widehat F\lambda'_i
+\frac i2(\not{\mathcal D}\rho)\lambda'_i-Y_{ij}\lambda'^j\bigg]_{(2,1)}.
\end{aligned}
\tag{19}
```

Subscripts $`(1,2)`$ and $`(2,1)`$ on brackets in this note are contribution labels only. Weight the derivative-on-spinor entries:

```math
\frac12 i\rho'\not{\mathcal D}\lambda_i
+\frac12 i\rho\not{\mathcal D}\lambda'_i
=\frac i2\left(\rho'\not{\mathcal D}\lambda_i+\rho\not{\mathcal D}\lambda'_i\right).
\tag{20}
```

Weight the $`T`$ entries, without moving a gamma matrix through a spinor:

```math
\frac12(2\rho'\gamma\!\cdot\!T\lambda_i)
+\frac12(2\rho\gamma\!\cdot\!T\lambda'_i)
=\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i.
\tag{21}
```

The two $`\chi_i`$ entries have identical even scalar factors after commuting $`\rho`$ and $`\rho'`$:

```math
\frac12(-8\rho'\rho\chi_i)+\frac12(-8\rho\rho'\chi_i)
=-4\rho'\rho\chi_i-4\rho'\rho\chi_i=-8\rho'\rho\chi_i.
\tag{22}
```

Weight the strength entries:

```math
\frac12\left(-\frac14\gamma\!\cdot\!\widehat F'\lambda_i\right)
+\frac12\left(-\frac14\gamma\!\cdot\!\widehat F\lambda'_i\right)
=-\frac18\left(\gamma\!\cdot\!\widehat F'\lambda_i+\gamma\!\cdot\!\widehat F\lambda'_i\right).
\tag{23}
```

Weight the derivatives of the scalars; the gamma contraction acts on the scalar gradient before multiplying the displayed spinor:

```math
\frac12\left(\frac i2(\not{\mathcal D}\rho')\lambda_i\right)
+\frac12\left(\frac i2(\not{\mathcal D}\rho)\lambda'_i\right)
=\frac i4\left((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\right).
\tag{24}
```

Weight the triplet–spinor entries, preserving their index placement:

```math
\frac12(-Y'_{ij}\lambda^j)+\frac12(-Y_{ij}\lambda'^j)
=-\frac12\left(Y'_{ij}\lambda^j+Y_{ij}\lambda'^j\right).
\tag{25}
```

Adding the six results gives

```math
\begin{aligned}
\varphi'_i={}&\frac i2\left(\rho'\not{\mathcal D}\lambda_i+\rho\not{\mathcal D}\lambda'_i\right)
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\\
&-\frac18\left(\gamma\!\cdot\!\widehat F'\lambda_i+\gamma\!\cdot\!\widehat F\lambda'_i\right)
+\frac i4\left((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\right)\\
&-\frac12\left(Y'_{ij}\lambda^j+Y_{ij}\lambda'^j\right).
\end{aligned}
\tag{26}
```

No spinor interchange was needed in this component. In particular the derivatives acting on $`\lambda_i`$ and $`\lambda'_i`$ have not been identified.

### 4.4 Derive $`E'^a`$

Retain the full derivative brackets and both topological contributions initially:

```math
\begin{aligned}
E'^a={}&\frac12\bigg[\mathcal D_b\left(-\rho'\widehat F^{ab}+8\rho'\rho T^{ab}
-\frac i4\bar\lambda'\gamma^{ab}\lambda\right)
-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}\bigg]_{(1,2)}\\
&+\frac12\bigg[\mathcal D_b\left(-\rho\widehat F'^{ab}+8\rho\rho'T^{ab}
-\frac i4\bar\lambda\gamma^{ab}\lambda'\right)
-\frac18\varepsilon^{abcde}\widehat F_{bc}\widehat F'_{de}\bigg]_{(2,1)}.
\end{aligned}
\tag{27}
```

The constants $`1/2`$ commute with $`\mathcal D_b`$. Its scalar–strength entries become

```math
-\frac12\mathcal D_b(\rho'\widehat F^{ab})
-\frac12\mathcal D_b(\rho\widehat F'^{ab})
=\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})\right].
\tag{28}
```

The $`T`$ entries combine using $`\rho\rho'=\rho'\rho`$:

```math
\frac12\mathcal D_b(8\rho'\rho T^{ab})
+\frac12\mathcal D_b(8\rho\rho'T^{ab})
=\mathcal D_b(8\rho'\rho T^{ab}).
\tag{29}
```

The rank-two spinor entries require Eq. (13):

```math
\begin{aligned}
&\mathcal D_b\left[-\frac i8\bar\lambda'\gamma^{ab}\lambda
-\frac i8\bar\lambda\gamma^{ab}\lambda'\right]\\
&=\mathcal D_b\left[-\frac i8\bar\lambda'\gamma^{ab}\lambda
-\frac i8\bar\lambda'\gamma^{ab}\lambda\right]
=-\frac i4\mathcal D_b(\bar\lambda'\gamma^{ab}\lambda).
\end{aligned}
\tag{30}
```

For the two topological entries, first relabel the two dummy pairs in the second contraction:

```math
\begin{aligned}
\varepsilon^{abcde}\widehat F_{bc}\widehat F'_{de}
&=\varepsilon^{adebc}\widehat F_{de}\widehat F'_{bc}\\
&=(-1)^{2\cdot2}\varepsilon^{abcde}\widehat F_{de}\widehat F'_{bc}
=\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{31}
```

Swapping the pair $`(bc)`$ with $`(de)`$ makes four single-index exchanges and has positive sign. The last step commutes two Grassmann-even strengths. Consequently

```math
-\frac1{16}\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}
-\frac1{16}\varepsilon^{abcde}\widehat F_{bc}\widehat F'_{de}
=-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\tag{32}
```

Combining all four source structures gives

```math
\begin{aligned}
E'^a={}&\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})
+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]
-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{33}
```

To display what the outer derivative does, apply its even product rule without integration by parts:

```math
\begin{aligned}
\mathcal D_b(\rho'\widehat F^{ab})&=(\mathcal D_b\rho')\widehat F^{ab}+\rho'\mathcal D_b\widehat F^{ab},\\
\mathcal D_b(\rho\widehat F'^{ab})&=(\mathcal D_b\rho)\widehat F'^{ab}+\rho\mathcal D_b\widehat F'^{ab},\\
\mathcal D_b(\rho'\rho T^{ab})&=(\mathcal D_b\rho')\rho T^{ab}
+\rho'(\mathcal D_b\rho)T^{ab}+\rho'\rho\mathcal D_bT^{ab},\\
\mathcal D_b(\bar\lambda'\gamma^{ab}\lambda)&=(\mathcal D_b\bar\lambda')\gamma^{ab}\lambda
+\bar\lambda'\gamma^{ab}\mathcal D_b\lambda.
\end{aligned}
\tag{34}
```

In the last line the derivative preserves the Clifford tensor, $`\mathcal D_b\gamma^{ac}=0`$ in its covariant product action, and the operator is even; no minus sign is generated by differentiation. It does not interchange the two spinors. Inserting these four equalities explicitly yields

```math
\begin{aligned}
E'^a={}&-\frac12(\mathcal D_b\rho')\widehat F^{ab}-\frac12\rho'\mathcal D_b\widehat F^{ab}
-\frac12(\mathcal D_b\rho)\widehat F'^{ab}-\frac12\rho\mathcal D_b\widehat F'^{ab}\\
&+8(\mathcal D_b\rho')\rho T^{ab}+8\rho'(\mathcal D_b\rho)T^{ab}
+8\rho'\rho\mathcal D_bT^{ab}\\
&-\frac i4(\mathcal D_b\bar\lambda')\gamma^{ab}\lambda
-\frac i4\bar\lambda'\gamma^{ab}\mathcal D_b\lambda
-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}
\tag{35}
```

This expands the outer derivative only. Its component derivatives retain their full supercovariant meanings; it is not a replacement by ordinary derivatives or a gauge-fixed expression.

### 4.5 Derive $`N'`$

Write the full $`(1,2)`$ contribution and then the full $`(2,1)`$ contribution:

```math
\begin{aligned}
N'={}&\frac12\bigg[\rho'\Box_c\rho+\frac12\mathcal D_a\rho'\mathcal D^a\rho
-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}+8\rho'\widehat F_{ab}T^{ab}\\
&\hspace{6mm}-4\rho'\rho\left(D+\frac{26}{3}T^2\right)
-\frac12\bar\lambda'\not{\mathcal D}\lambda
+i\bar\lambda'\gamma\!\cdot\!T\lambda+16i\rho'\bar\chi\lambda\bigg]_{(1,2)}\\
&+\frac12\bigg[\rho\Box_c\rho'+\frac12\mathcal D_a\rho\mathcal D^a\rho'
-\frac14\widehat F_{ab}\widehat F'^{ab}+Y_{ij}Y'^{ij}+8\rho\widehat F'_{ab}T^{ab}\\
&\hspace{6mm}-4\rho\rho'\left(D+\frac{26}{3}T^2\right)
-\frac12\bar\lambda\not{\mathcal D}\lambda'
+i\bar\lambda\gamma\!\cdot\!T\lambda'+16i\rho\bar\chi\lambda'\bigg]_{(2,1)}.
\end{aligned}
\tag{36}
```

**Second derivatives.** Distribute the coefficient; do not move $`\Box_c`$ between its arguments:

```math
\frac12\rho'\Box_c\rho+\frac12\rho\Box_c\rho'
=\frac12\left(\rho'\Box_c\rho+\rho\Box_c\rho'\right).
\tag{37}
```

The two $`\Box_c`$ definitions in Eq. (9) are distinct and complete. Equation (37) is not replaced by $`\rho'\Box_c\rho`$ through an undisplayed boundary manipulation.

**Scalar gradients.** The contraction is symmetric because the metric is symmetric and the gradients are even:

```math
\begin{aligned}
\mathcal D_a\rho\mathcal D^a\rho'
&=\eta^{ab}(\mathcal D_a\rho)(\mathcal D_b\rho')
=\eta^{ba}(\mathcal D_b\rho')(\mathcal D_a\rho)\\
&=\mathcal D_a\rho'\mathcal D^a\rho,\\
\frac14\mathcal D_a\rho'\mathcal D^a\rho
+\frac14\mathcal D_a\rho\mathcal D^a\rho'
&=\frac12\mathcal D_a\rho'\mathcal D^a\rho.
\end{aligned}
\tag{38}
```

The third expression in the first chain is reached by the dummy relabelling $`a\leftrightarrow b`$. No commutator is taken.

**Strength contraction.** Both metrics and the even strengths commute, giving

```math
\begin{aligned}
\widehat F_{ab}\widehat F'^{ab}
&=\eta^{ac}\eta^{bd}\widehat F_{ab}\widehat F'_{cd}
=\eta^{ca}\eta^{db}\widehat F'_{cd}\widehat F_{ab}
=\widehat F'_{ab}\widehat F^{ab},\\
-\frac18\widehat F'_{ab}\widehat F^{ab}
-\frac18\widehat F_{ab}\widehat F'^{ab}
&=-\frac14\widehat F'_{ab}\widehat F^{ab}.
\end{aligned}
\tag{39}
```

In the last step of the first line, relabel $`(a,b)\leftrightarrow(c,d)`$. There is no epsilon sign in this metric contraction.

**Triplet contraction.** Raising both indices gives two epsilons, so exchanging the two triplets gives two minus signs:

```math
\begin{aligned}
Y_{ij}Y'^{ij}
&=Y_{ij}\varepsilon^{ik}\varepsilon^{j\ell}Y'_{k\ell}
=Y'_{k\ell}\varepsilon^{ki}\varepsilon^{\ell j}Y_{ij}
=Y'_{ij}Y^{ij},\\
\frac12Y'_{ij}Y^{ij}+\frac12Y_{ij}Y'^{ij}&=Y'_{ij}Y^{ij}.
\end{aligned}
\tag{40}
```

The final dummy relabelling is $`(i,j)\leftrightarrow(k,\ell)`$. No one-index lowering convention is changed.

**Scalar–strength–$`T`$ terms.** These two products have different vector slots and remain separate:

```math
\frac12(8\rho'\widehat F_{ab}T^{ab})
+\frac12(8\rho\widehat F'_{ab}T^{ab})
=4\left(\rho'\widehat F_{ab}+\rho\widehat F'_{ab}\right)T^{ab}.
\tag{41}
```

**$`D`$ and $`T^2`$ terms.** First commute the two scalars, then add the weighted terms:

```math
\begin{aligned}
&-2\rho'\rho\left(D+\frac{26}{3}T^2\right)
-2\rho\rho'\left(D+\frac{26}{3}T^2\right)\\
&=-4\rho'\rho\left(D+\frac{26}{3}T^2\right)
=-4\rho'\rho D-\frac{104}{3}\rho'\rho T^2.
\end{aligned}
\tag{42}
```

The factor $`104/3`$ is $`4\cdot26/3`$; it is not an additional coupling. Both background components retain the gauged meaning in A4.

**Derivative spinor terms.** Weight the two ordered terms separately:

```math
\frac12\left(-\frac12\bar\lambda'\not{\mathcal D}\lambda\right)
+\frac12\left(-\frac12\bar\lambda\not{\mathcal D}\lambda'\right)
=-\frac14\left(\bar\lambda'\not{\mathcal D}\lambda
+\bar\lambda\not{\mathcal D}\lambda'\right).
\tag{43}
```

The rank-one contracted flip would relate $`\bar\lambda\gamma^a\mathcal D_a\lambda'`$ to $`-\overline{\mathcal D_a\lambda'}\gamma^a\lambda`$, not to $`\bar\lambda'\gamma^a\mathcal D_a\lambda`$. Moving that derivative requires another operation. No such operation is made here; Eq. (43) remains the local source sum.

**$`T`$ spinor terms.** Use the contracted rank-two flip in Eq. (13), with the even $`T`$ factor retained:

```math
\frac i2\bar\lambda'\gamma\!\cdot\!T\lambda
+\frac i2\bar\lambda\gamma\!\cdot\!T\lambda'
=\frac i2\bar\lambda'\gamma\!\cdot\!T\lambda
+\frac i2\bar\lambda'\gamma\!\cdot\!T\lambda
=i\bar\lambda'\gamma\!\cdot\!T\lambda.
\tag{44}
```

**$`\chi`$ spinor terms.** Keep $`\bar\chi`$ on the left of the vector spinor, as printed:

```math
\frac12(16i\rho'\bar\chi\lambda)+\frac12(16i\rho\bar\chi\lambda')
=8i\left(\rho'\bar\chi\lambda+\rho\bar\chi\lambda'\right).
\tag{45}
```

The nine source structures (ten if $`D`$ and $`T^2`$ are listed separately) therefore give

```math
\begin{aligned}
N'={}&\frac12(\rho'\Box_c\rho+\rho\Box_c\rho')
+\frac12\mathcal D_a\rho'\mathcal D^a\rho
-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}\\
&+4(\rho'\widehat F_{ab}+\rho\widehat F'_{ab})T^{ab}
-4\rho'\rho\left(D+\frac{26}{3}T^2\right)\\
&-\frac14\left(\bar\lambda'\not{\mathcal D}\lambda
+\bar\lambda\not{\mathcal D}\lambda'\right)
+i\bar\lambda'\gamma\!\cdot\!T\lambda
+8i(\rho'\bar\chi\lambda+\rho\bar\chi\lambda').
\end{aligned}
\tag{46}
```

### 4.6 Relate the constrained component to the Step 1 representation

The output here is $`E'^a`$, while Step 1 retained $`E'_{\mu\nu\rho}`$ in the BF potential term. Combining source (3.12) and (3.13) and priming their linear arguments gives the relation, without introducing a new field name,

```math
E'^a+\frac i2\bar\psi_b\gamma^{ba}\varphi'
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL'_{ij}
=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\tau}
\partial_\nu E'_{\rho\sigma\tau}.
\tag{47}
```

This is the same primed constrained linear multiplet, with the same gravitino, as in Step 1. It records the exact source bridge between its component and potential descriptions. The newly calculated right-hand sides for $`L',\varphi',E',N'`$ have not been inserted into BF; that is Step 3. In particular $`E'^a`$ must not be substituted alone for the ordinary three-form curl without the two fermionic terms in Eq. (47).

## 5. Consistency Checks

### 5.1 Complete working-map term and weight ledger

The input weights are $`w(\rho)=w(\rho')=1`$, $`w(\lambda)=w(\lambda')=3/2`$, $`w(Y)=w(Y')=w(\widehat F)=w(\widehat F')=2`$, $`w(T)=1`$, $`w(\chi)=3/2`$, $`w(D)=2`$; $`\mathcal D_a`$ adds one and $`\Box_c`$ adds two. Priming does not change a weight. Each of the following working-map rows has been evaluated above; the half-weight is applied to each of its two ordered copies.

| Row | Source tensor structure | Working coefficient | Each ordered coefficient | Weight calculation |
|---|---|---|---|---|
| L-01 | $`\rho^B Y^C`$ | $`2`$ | $`1`$ | $`1+2=3`$ |
| L-02 | $`\bar\lambda^B_{(i}\lambda^C_{j)}`$ | $`-i/2`$ | $`-i/4`$ | $`3/2+3/2=3`$ |
| P-01 | $`\rho^B\not{\mathcal D}\lambda_i^C`$ | $`i`$ | $`i/2`$ | $`1+1+3/2=7/2`$ |
| P-02 | $`\rho^B\gamma\!\cdot\!T\lambda_i^C`$ | $`2`$ | $`1`$ | $`1+1+3/2=7/2`$ |
| P-03 | $`\rho^B\rho^C\chi_i`$ | $`-8`$ | $`-4`$ | $`1+1+3/2=7/2`$ |
| P-04 | $`\gamma\!\cdot\!\widehat F^B\lambda_i^C`$ | $`-1/4`$ | $`-1/8`$ | $`2+3/2=7/2`$ |
| P-05 | $`(\not{\mathcal D}\rho^B)\lambda_i^C`$ | $`i/2`$ (printed: $`1/2`$) | $`i/4`$ | $`1+1+3/2=7/2`$ |
| P-06 | $`Y^B_{ij}\lambda^{jC}`$ | $`-1`$ | $`-1/2`$ | $`2+3/2=7/2`$ |
| E-01 | $`\mathcal D_b(\rho^B\widehat F^{abC})`$ | $`-1`$ | $`-1/2`$ | $`1+1+2=4`$ |
| E-02 | $`\mathcal D_b(\rho^B\rho^C T^{ab})`$ | $`8`$ | $`4`$ | $`1+1+1+1=4`$ |
| E-03 | $`\mathcal D_b(\bar\lambda^B\gamma^{ab}\lambda^C)`$ | $`-i/4`$ | $`-i/8`$ | $`1+3/2+3/2=4`$ |
| E-04 | $`\varepsilon^{abcde}\widehat F^B_{bc}\widehat F^C_{de}`$ | $`-1/8`$ | $`-1/16`$ | $`2+2=4`$ |
| N-01 | $`\rho^B\Box_c\rho^C`$ | $`1`$ | $`1/2`$ | $`1+2+1=4`$ |
| N-02 | $`\mathcal D_a\rho^B\mathcal D^a\rho^C`$ | $`1/2`$ | $`1/4`$ | $`(1+1)+(1+1)=4`$ |
| N-03 | $`\widehat F^B_{ab}\widehat F^{abC}`$ | $`-1/4`$ | $`-1/8`$ | $`2+2=4`$ |
| N-04 | $`Y^B_{ij}Y^{ijC}`$ | $`1`$ | $`1/2`$ | $`2+2=4`$ |
| N-05 | $`\rho^B\widehat F^C_{ab}T^{ab}`$ | $`8`$ | $`4`$ | $`1+2+1=4`$ |
| N-06 | $`\rho^B\rho^C D`$ | $`-4`$ | $`-2`$ | $`1+1+2=4`$ |
| N-07 | $`\rho^B\rho^C T^2`$ | $`-104/3`$ | $`-52/3`$ | $`1+1+2=4`$ |
| N-08 | $`\bar\lambda^B\not{\mathcal D}\lambda^C`$ | $`-1/2`$ | $`-1/4`$ | $`3/2+1+3/2=4`$ |
| N-09 | $`\bar\lambda^B\gamma\!\cdot\!T\lambda^C`$ | $`i`$ | $`i/2`$ | $`3/2+1+3/2=4`$ |
| N-10 | $`\rho^B\bar\chi\lambda^C`$ | $`16i`$ | $`8i`$ | $`1+3/2+3/2=4`$ |

Only P-05 differs from the printed-source coefficient ledger; its two values and the reason for the repair are displayed in (3)–(3d). This verifies $`w(L')=3`$, $`w(\varphi')=7/2`$, $`w(E')=w(N')=4`$ term by term. These are conformal scaling weights before gauge fixing, not canonical Poincaré field dimensions. The full fermionic target is preserved: hatted strengths, component derivatives and background composites retain their implicit fermions.

### 5.2 Free indices, parity, and covariance

- $`L'_{ij}`$ has exactly the symmetric free pair $`(ij)`$: the two $`Y`$ terms are symmetric, and Eq. (14) explicitly symmetrizes the spinors. Every term has even parity.
- $`\varphi'_i`$ has the same single lower free $`SU(2)`$ index and the same spinor type in every term. The gamma dots contract their two-form indices, the slashes contract the derivative index, and $`Y_{ij}\lambda^j`$ contracts only $`j`$. Each term has one odd component factor, possibly with implicit fermions in its even coefficients.
- $`E'^a`$ has one free tangent index $`a`$. Inside the derivative, every summand is antisymmetric in $`(a,b)`$: $`\widehat F^{ab}=-\widehat F^{ba}`$, $`T^{ab}=-T^{ba}`$, and $`\gamma^{ab}=-\gamma^{ba}`$. Its epsilon term has precisely four contracted indices $`(b,c,d,e)`$ and free $`a`$. All terms are even.
- $`N'`$ is an even Lorentz and $`SU(2)`$ scalar. Metric contractions were verified in Eqs. (38)–(40); contracted spinor strings use the declared NW–SE pairing.

The source's covariant tensor types and weights are preserved by the constant mixed sum. The rigid scalar-gradient transformation is checked explicitly in (3b)–(3c). These type and weight checks do not establish the full local linear-multiplet transformation law of the repaired map; that all-order statement is outside the checked scope.

### 5.3 Bosonic limit of all four results

For this check only, set $`\lambda'=\lambda=\psi_\mu=\chi=\phi_\mu=0`$, retaining bosonic vector and background fields. Hatted strengths reduce to their ordinary Abelian values, $`F'_{\mu\nu}=2\partial_{[\mu}A'_{\nu]}`$ and $`F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}`$. The $`L`$ bilinear vanishes; every $`\varphi`$ term has a vanished spinor; the $`E`$ derivative bilinear vanishes; and the three explicit fermion structures in $`N`$ vanish. The surviving expressions are

```math
\begin{aligned}
L'_{ij}\big|_{\rm bos}&=\rho'Y_{ij}+\rho Y'_{ij},\qquad
\varphi'_i\big|_{\rm bos}=0,\\
E'^a\big|_{\rm bos}&=\mathcal D_b\left[-\frac12(\rho'F^{ab}+\rho F'^{ab})
+8\rho'\rho T^{ab}\right]-\frac18\varepsilon^{abcde}F'_{bc}F_{de},\\
N'\big|_{\rm bos}&=\frac12(\rho'\Box_c\rho+\rho\Box_c\rho')
+\frac12\mathcal D_a\rho'\mathcal D^a\rho-\frac14F'_{ab}F^{ab}+Y'_{ij}Y^{ij}\\
&\quad+4(\rho'F_{ab}+\rho F'_{ab})T^{ab}
-4\rho'\rho\left(D+\frac{26}{3}T^2\right).
\end{aligned}
\tag{48}
```

The $`\mathcal D`$ and $`\Box_c`$ in this check retain the bosonic conformal connections; setting fermions to zero is not permission to drop them.

### 5.4 Independent polarization, exchange, and identical-input tests

Hold the common Weyl background fixed, and temporarily let $`q`$ stand for any one repaired working component evaluated with a **single** vector and coefficient one. This is a verification function, not a new physical field. Every source structure is quadratic in vector entries; $`\mathcal D`$, $`\widehat F`$ and $`\Box_c`$ are linear in the vector arguments at fixed background by Eqs. (7)–(9). For an ordered source product the independent expansion is

```math
\begin{aligned}
(X'+X)(Z'+Z)&=X'Z'+X'Z+XZ'+XZ,\\
\frac12\big[(X'+X)(Z'+Z)-X'Z'-XZ\big]&=\frac12(X'Z+XZ').
\end{aligned}
\tag{49}
```

$`X,Z`$ in this identity are placeholders for the source factors, with their order retained even when both are odd. Thus each component above must equal the polarization

```math
\frac12\left[q(\text{primed vector}+\text{unprimed vector})
-q(\text{primed vector})-q(\text{unprimed vector})\right].
\tag{50}
```

The verification script expands every one of the 22 working-map rows this way, independently of the direct $`C_{1BC}`$ sum. It retains both ordered words before applying the proved flip/contraction identities. This tests the factors of $`1/2`$ without assuming that the two vectors are equal.

The ordered sum is invariant under exchanging its two vector arguments because its two weights are equal. Equations (14), (13), and (31) verify that the collected expressions preserve that exchange. All pairs left explicitly in $`\varphi'`$ and $`N'`$ exchange into each other.

As a **formal check only**, replace every primed vector slot and its derivatives by the corresponding unprimed slot. For example

```math
\begin{aligned}
L'_{ij}\big|_{1=2}&=2\rho Y_{ij}-\frac i2\bar\lambda_{(i}\lambda_{j)},\\
\frac i2(\rho'\not{\mathcal D}\lambda_i+\rho\not{\mathcal D}\lambda'_i)\big|_{1=2}
&=i\rho\not{\mathcal D}\lambda_i,\\
\frac i4\big[(\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\big]\big|_{1=2}
&=\left(\frac i4+\frac i4\right)(\not{\mathcal D}\rho)\lambda_i
=\frac i2(\not{\mathcal D}\rho)\lambda_i,\\
-\frac14(\bar\lambda'\not{\mathcal D}\lambda+\bar\lambda\not{\mathcal D}\lambda')\big|_{1=2}
&=-\frac12\bar\lambda\not{\mathcal D}\lambda,\\
8i(\rho'\bar\chi\lambda+\rho\bar\chi\lambda')\big|_{1=2}&=16i\rho\bar\chi\lambda.
\end{aligned}
\tag{51}
```

For every remaining row the same coefficient test is explicitly $`\tfrac12c+\tfrac12c=c`$, with $`c`$ the working coefficient in the ledger; the script tests it for all rows. The map therefore reduces to the unit-coefficient single-vector working map, including $`+i/2`$ for its scalar-gradient term. The printed $`+1/2`$ is not the target of this repaired coincident-input test. This check does not change the primed/unprimed assignments of the actual construction.

Every term is bilinear in the two vector arguments. If either vector, including its derivatives, vanishes identically, every row of both ordered contributions contains a zero factor. Thus all four outputs vanish. This is also tested row by row.

### 5.5 Check the constrained vector in the flat bosonic limit

Take the further **test** specialization to flat space, vanishing conformal connections and $`T=0`$, with the two ordinary closed strengths. The double divergence of the derivative part is zero because its bracket is antisymmetric:

```math
\begin{aligned}
&\partial_a\partial_b\left[-\frac12(\rho'F^{ab}+\rho F'^{ab})\right]\\
&=\frac12(\partial_a\partial_b-\partial_b\partial_a)
\left[-\frac12(\rho'F^{ab}+\rho F'^{ab})\right]=0.
\end{aligned}
\tag{52}
```

For the remaining term the product rule gives

```math
\partial_a\big(\varepsilon^{abcde}F'_{bc}F_{de}\big)
=\varepsilon^{abcde}(\partial_aF'_{bc})F_{de}
+\varepsilon^{abcde}F'_{bc}(\partial_aF_{de}).
\tag{53}
```

The first contraction can be replaced by one third of the three cyclic derivatives, since a three-cycle has positive permutation sign:

```math
\varepsilon^{abcde}(\partial_aF'_{bc})F_{de}
=\frac13\varepsilon^{abcde}
(\partial_aF'_{bc}+\partial_bF'_{ca}+\partial_cF'_{ab})F_{de}=0.
\tag{54}
```

The second has the corresponding cycle on $`(a,d,e)`$:

```math
\varepsilon^{abcde}F'_{bc}(\partial_aF_{de})
=\frac13\varepsilon^{abcde}F'_{bc}
(\partial_aF_{de}+\partial_dF_{ea}+\partial_eF_{ad})=0.
\tag{55}
```

Each final zero is the ordinary Abelian Bianchi identity $`\partial_{[a}F_{bc]}=\partial_{[a}F'_{bc]}=0`$. It follows that $`\partial_aE'^a=0`$ in this test limit. For general supergravity, $`\mathcal D^aE'_a=0`$ is the source linear-multiplet constraint; the preceding flat proof does not replace its full supercovariant Bianchi and supersymmetry analysis.

### 5.6 Reproducible checks and their limits

[verify_step2_mixed_linear.py](../../../../src/kernels/verify_step2_mixed_linear.py) distinguishes the 22 printed coefficients from the 22 working coefficients, checks that only P-05 changes, and audits all weights, direct ordered substitution versus independent polarization, exchange and zero/coincident limits, and collected coefficient multiplicities. It also tests the two spinor flip identities using explicit Clifford matrices and an exterior algebra for odd spinor components, and checks the epsilon pair exchange by full component sums. Its report, generated as `build/step2_mixed_linear_verification.json` in the [component-check runner](../../../../checks/run_component_checks.py)'s temporary directory, records the document hash and exact scope.

The check uses Grassmann components, not commuting numerical spinors. Exact rational arithmetic is used for coefficients. No full SUSY variation, Fierz rearrangement, Hermitian-conjugation proof, or gauged-background expansion is claimed. The necessary scalar-gradient phase follows from (3b)–(3c) and the [mixed-map component check](../../../../src/kernels/verify_step2_mixed_linear.py); full-density reality and all-order symplectic Majorana consistency are outside its scope. The verifier separates the printed Eq. (3), repaired Eq. (3a), ordered Eq. (19), weighting Eq. (24), assembled Eq. (26), equal-input Eq. (51), and delivered Eq. (57). No approximation has been made, so there is no truncation error estimate to attach to this result.

## 6. Final Result

In the common gauged Coomans background, with both vector arguments retained, the new primed linear multiplet is

```math
\boxed{L'_{ij}=\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}.}
\tag{56}
```

```math
\boxed{\begin{aligned}
\varphi'_i={}&\frac i2(\rho'\not{\mathcal D}\lambda_i+\rho\not{\mathcal D}\lambda'_i)
+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i\\
&-\frac18(\gamma\!\cdot\!\widehat F'\lambda_i+\gamma\!\cdot\!\widehat F\lambda'_i)
+\frac i4\big((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\big)\\
&-\frac12(Y'_{ij}\lambda^j+Y_{ij}\lambda'^j).
\end{aligned}}
\tag{57}
```

```math
\boxed{\begin{aligned}
E'^a={}&\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})
+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]\\
&-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.
\end{aligned}}
\tag{58}
```

```math
\boxed{\begin{aligned}
N'={}&\frac12(\rho'\Box_c\rho+\rho\Box_c\rho')
+\frac12\mathcal D_a\rho'\mathcal D^a\rho
-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}\\
&+4(\rho'\widehat F_{ab}+\rho\widehat F'_{ab})T^{ab}
-4\rho'\rho\left(D+\frac{26}{3}T^2\right)\\
&-\frac14(\bar\lambda'\not{\mathcal D}\lambda+\bar\lambda\not{\mathcal D}\lambda')
+i\bar\lambda'\gamma\!\cdot\!T\lambda
+8i(\rho'\bar\chi\lambda+\rho\bar\chi\lambda').
\end{aligned}}
\tag{59}
```

These are the four complete working component expressions after the specified $`C_{1BC}`$ sum, with source-supercovariant notation retained. They have weights $`(3,7/2,4,4)`$ and preserve every tensor structure of source (3.20), with the sole project-derived coefficient repair $`+1/2\to+i/2`$ before weighting. The unchanged $`-i/4`$ derivative bilinear in $`E'`$ and $`+Y'_{ij}Y^{ij}`$ in $`N'`$ are independently supported by the audit's component tests. The constrained-form relation (47) accompanies $`E'^a`$ for the subsequent BF insertion.

## 7. Convention Dependence and Remaining Uncertainties

- **Step 2 is complete as the repaired specialization**, lock `R2-MIXED-PRIMED-LINEAR-v2`. The printed phase remains explicitly quoted in Eq. (3), while all active descendants use (3a), lock `R2-VL-GRADIENT-PHASE-v1`. The necessary rigid transformation test fixes the repair under the locked Coomans rules; it is not a published erratum, a proof that no further local correction exists, or a full reality/SUSY certification.
- The two vector maps remain unexpanded. In particular $`\rho'\ne\rho`$, $`\lambda'\ne\lambda`$, $`Y'\ne Y`$ are not imposed as equations either way: their roles remain distinct until the different maps are applied. The formal equal-input test in Section 5 is not a field identification.
- All $`T,\chi,D`$ slots remain bound to the gauged Coomans–Özkan source ([publication](../../../../../../references/bibliography.md#CoomansOzkan2013)), through [the framework's exact anchors](00_action_construction_framework.md). The [Step 6 action](10_step6_gauged_action_through_two_fermions.md) inserts the explicit background through two physical fermions; source-omitted higher orders are outside that result's scope.
- The full local constraint and full supersymmetry transformation of the repaired multiplet remain unproved by the scoped symbolic verifier. The flat bosonic constraint check is explicitly narrower.
- [Step 3](05_step3_mixed_linear_inserted_in_BF.md) inserts these components into the primed BF density. The potential/component bridge (47) must accompany its form term; neither an isolated $`A'_aE'^a`$ replacement nor a guessed local potential is allowed.
- No BF insertion, Gold substitution, earlier primed-vector substitution, integration by parts, gauge fixing, auxiliary elimination, vacuum or spectrum calculation was performed here. The source-normalized invariant and its coupling are used in the [total action](12_total_action_zeroth_first_second_orders.md); no independent conversion of every fermionic term to a different boundary representative is claimed here.
