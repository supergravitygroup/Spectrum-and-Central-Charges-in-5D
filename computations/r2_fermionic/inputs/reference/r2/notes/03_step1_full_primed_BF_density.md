# Step 1 — Complete fermionic BF density in primed components

## 1. Problem and Target

Write the complete vector–linear (BF) density with the **primed vector paired with the new primed linear multiplet**, as required by [the confirmed construction framework](00_action_construction_framework.md). This step fixes the density into which the mixed linear multiplet will subsequently be inserted.

The starting formula is **Özkan–Pang, _Supersymmetric Completion of Gauss-Bonnet Combination in Five Dimensions_, arXiv:1301.6622v4, Sec. 3, Eq. (3.1), printed/PDF p. 10**. Its seven terms are transcribed and individually relabelled below. The formula was checked on page 10 of the [publication](../../../../../../references/bibliography.md#OzkanPangGB2013). The constrained-form definition was checked on page 9, Eqs. (2.20)–(2.22). The inherited [source ledger, Sec. 3.4](../../../../../../common/README.md) provides a matching transcription of (3.1).

The work here is an exact specialization of that source density. It is not a derivation of the universal density from supersymmetry transformations, nor yet a calculation of the mixed linear components or the final $`R^2`$ action.

**Assumptions and permitted operations**

- **A1.** Work in five-dimensional off-shell superconformal tensor calculus, with the complete source BF density and no fermion truncation.
- **A2.** The vector argument is $`(Y'_{ij},\rho',A'_\mu,\lambda'^i)`$ and the linear argument is $`(L'_{ij},\varphi'_i,E'^a,N')`$. At this stage they retain their component notation. The original unprimed linear multiplet $`(L_{ij},\varphi_i,E^a,N)`$ is the common input for the two later vector maps; it is not the linear argument of this BF pairing.
- **A3.** Only source transcription, priming of matter slots, expansion of brackets, and explicitly indicated dummy-index relabelling are used. No vector-to-linear map or linear-to-vector map is applied here.
- **A4.** No gauge condition, field equation, background specialization, auxiliary elimination, dualization, or integration by parts is applied. The source potential–three-form representative is retained pointwise. No boundary term is discarded.
- **A5.** All background composite slots remain bound to the gauged Coomans–Özkan prescription fixed in the framework. $`T_{ab},\chi^i,D`$ do not occur explicitly in the universal density (3.1); their later occurrences through the component maps must use that gauged prescription. No expansion in $`g`$ or in the higher-derivative coupling is made.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The [branch convention ledger](../../../../derivations/component_conventions.md) and the inherited [supporting-source ledger, Sec. 2](../../../../../../common/README.md) control the notation. No source field rescaling is made.

| Item | Convention used in this step |
|---|---|
| Dimension, signature, units | $`D=5`$, $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$, $`\hbar=c=1`$ |
| Indices | $`a,b=0,\ldots,4`$ tangent; $`\mu,\nu,\rho,\sigma,\tau=0,\ldots,4`$ world; $`i,j=1,2`$ for $`SU(2)`$ |
| Metric and frame | $`g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}`$, $`e=\det(e_\mu{}^a)`$, $`\psi_a^i=e_a{}^\mu\psi_\mu^i`$ |
| Symmetrization | Unit weight: $`X_{(ij)}=(X_{ij}+X_{ji})/2`$ and $`\gamma^{ab}=(\gamma^a\gamma^b-\gamma^b\gamma^a)/2`$ |
| Orientation | $`\varepsilon^{01234}=+1`$ in an oriented orthonormal frame and $`\varepsilon_{01234}=-1`$. In world indices $`\varepsilon^{\mu\nu\rho\sigma\tau}=e^{-1}\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}`$, with the constant oriented symbol $`\widetilde\varepsilon^{01234}=+1`$ |
| Clifford algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; $`\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1`$ |
| $`SU(2)`$ indices | NW–SE convention: $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$ |
| Fermions and bar | Grassmann-odd symplectic Majorana spinors, with the inherited operational Majorana bar. No conversion to a differently phased Dirac bar is made |
| Spinor ordering | Preserve the source's left-to-right bilinear ordering. Fixed-index flip signs are $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; an NW–SE-contracted flip has the additional minus sign. No flip is used below |
| Geometry | Inherited $`R^\rho{}_{\sigma\mu\nu}=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}+2\Gamma^\rho_{[\mu\vert\alpha\vert}\Gamma^\alpha_{\nu]\sigma}`$, $`R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}`$; no curvature operation occurs in Step 1 |
| Derivatives and torsion | $`\partial_\mu`$ in the BF term is an ordinary derivative. $`\mathcal D`$ in the separately quoted constrained-component relation is the source supercovariant derivative. These are not identified; no torsion or dependent connection is suppressed |
| Gauging | Common Coomans–Özkan gauged background; no explicit $`g`$ appears before component substitution |
| Normalization | Exactly the overall coefficient of source (3.1). No two-derivative overall sign, extra $`1/2`$, or $`C_{1BC}`$ is applied to BF |
| Later coupling | $`\lambda_{R^2}`$ has mass dimension $`-2`$ in the eventual Gold bosonic convention. The BF-to-Gold action normalization is a later check, not fixed by this transcription |
| Functional derivatives | No variation with respect to a fermion is performed, so no left/right functional-derivative convention is required |

The metric, units and higher-derivative coupling conventions are those in the table above. The coupling is not inserted into the source density. Fourier transforms, state normalization and renormalization do not enter this classical local operation.

## 3. Definitions and Required Identities

### 3.1 Matter components, background, and primes

The arguments selected for BF are

```math
\begin{aligned}
\text{primed vector:}&\qquad (Y'_{ij},\rho',A'_\mu,\lambda'^i),\\
\text{new primed linear:}&\qquad (L'_{ij},\varphi'_i,E'^a,N'),\\
Y'_{ij}&=Y'_{ji},\qquad L'_{ij}=L'_{ji}.
\end{aligned}
\tag{1}
```

The common Weyl background is unprimed. In particular, $`\psi_\mu^i`$ and $`\psi_a^i`$ are the gravitino, not either vector fermion. A prime on $`\lambda'^i`$ is part of the selected vector role; a prime on $`\varphi'_i`$ is part of the new linear role. The notation $`\bar\lambda'`$ means $`\overline{\lambda'}`$, and $`\bar\lambda'\varphi'=\bar\lambda'{}^i\varphi'_i`$ in the inherited contraction convention. Likewise $`\bar\psi_a\gamma^a\varphi'=\bar\psi_a{}^i\gamma^a\varphi'_i`$. Suppressed spinor matrix indices are contracted in exactly this order.

The Weyl weights used below are

```math
\begin{aligned}
w(\rho')&=1,& w(\lambda')&=\frac32,& w(Y')&=2,& w(A'_\mu)&=0,\\
w(L')&=3,& w(\varphi')&=\frac72,& w(E'^a)&=4,& w(N')&=4,\\
w(e_\mu{}^a)&=-1,&w(e)&=-5,&w(\psi_\mu)&=-\frac12,&w(\psi_a)&=\frac12.
\end{aligned}
\tag{2}
```

The vector and linear weights agree with the dilatation terms in source (2.14), (2.15), and (2.19); the frame conversion adds one to a world gravitino's weight. The conformal weights are the appropriate pre-gauge-fixing dimension check, not an assertion of canonically normalized Poincaré-field dimensions.

### 3.2 Which three-form appears in BF?

$`E'_{\mu\nu\rho}`$ is the three-form potential representing the constrained component of the **new primed linear multiplet**. It is not the original unprimed compensator three-form, and it is not an additional multiplet. Source (2.20)–(2.22), with the linear slots primed, state

```math
\mathcal D^a E'_a=0,\qquad
E'^\mu=e_a{}^\mu E'^a
=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}
\mathcal D_\nu E'_{\rho\sigma\tau},\qquad
\delta E'_{\mu\nu\rho}=3\partial_{[\mu}\Lambda'_{\nu\rho]}.
\tag{3}
```

Here $`\Lambda'_{\nu\rho}`$ is the corresponding two-form gauge parameter. Equation (3) is a source definition of the constrained-form representation, not a component map evaluated in this step. Its $`\mathcal D`$ is kept supercovariant. In particular, it does **not** license replacing the ordinary-derivative BF term by $`A'_aE'^a`$ without the fermionic completion of that conversion. We retain the explicit ordinary-derivative three-form term of source (3.1).

In the world-index convention above, $`w(E'_{\mu\nu\rho})=0`$ and $`w(\varepsilon^{\mu\nu\rho\sigma\tau})=5`$. Indeed $`w(E'^\mu)=w(e_a{}^\mu)+w(E'^a)=1+4=5`$, consistent with (3).

### 3.3 The complete source density before selecting arguments

The symbols in the following equation are the **generic arguments of the published density**, before the primed arguments (1) are selected. These generic unprimed symbols are not an instruction to use vector label 2 in BF:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}
={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\frac12\bar\psi_a{}^i\gamma^a\lambda^jL_{ij}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}
A_\mu\partial_\nu E_{\rho\sigma\tau}\\
&+\rho\left(N+\frac12\bar\psi_a\gamma^a\varphi
+\frac i4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}\right).
\end{aligned}
\tag{4}
```

This is source (3.1), with only its last dummy world index relabelled $`\lambda\to\tau`$ to distinguish it visually from the vector spinor $`\lambda`$. Both occurrences of that dummy index, in $`\varepsilon`$ and $`E`$, are relabelled together; no indices are permuted and no sign changes.

## 4. Detailed Derivation

### 4.1 Apply the priming rule only to matter slots

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The replacement of the generic arguments in (4) is

```math
\begin{aligned}
Y^{ij}&\longmapsto Y'^{ij},&\rho&\longmapsto\rho',&A_\mu&\longmapsto A'_\mu,&\lambda^i&\longmapsto\lambda'^i,\\
L_{ij}&\longmapsto L'_{ij},&N&\longmapsto N',&E_{\rho\sigma\tau}&\longmapsto E'_{\rho\sigma\tau},&\varphi_i&\longmapsto\varphi'_i,\\
e&\longmapsto e,&\psi_a^i&\longmapsto\psi_a^i,&\gamma^a&\longmapsto\gamma^a,&\varepsilon^{\mu\nu\rho\sigma\tau}&\longmapsto\varepsilon^{\mu\nu\rho\sigma\tau}.
\end{aligned}
\tag{5}
```

This is a selection of arguments, not an equality between the primed and unprimed physical vector multiplets. A prime commutes with taking the inherited bar and with the ordinary derivative: $`\bar\lambda\mapsto\overline{\lambda'}`$ and $`\partial_\nu E_{\rho\sigma\tau}\mapsto\partial_\nu E'_{\rho\sigma\tau}`$. It is a component label, not a differential operator or complex conjugation.

### 4.2 Triplet term

Substitute the vector triplet and linear triplet together:

```math
Y^{ij}L_{ij}\ \longmapsto\ Y'^{ij}L'_{ij}=L'_{ij}Y'^{ij}.
\tag{6}
```

The last equality interchanges two Grassmann-even fields, with sign $`(-1)^{0\cdot0}=+1`$. Both $`SU(2)`$ indices remain contracted. Its weight is $`2+3=5`$. No extra factor of two is attached to the contraction of symmetric triplets; the source already uses the full $`i,j`$ sum.

### 4.3 Vector-fermion/linear-fermion term

Replace the two matter spinors without reversing their order:

```math
i\bar\lambda\varphi
\ \longmapsto\ i\overline{\lambda'}\varphi'
=i\bar\lambda'{}^i\varphi'_i.
\tag{7}
```

The coefficient $`i`$ is retained, the barred spinor remains on the left, and no Grassmann swap occurs. The term is even, with parity $`1+1=0\pmod2`$, and has weight $`3/2+7/2=5`$.

### 4.4 Gravitino/vector-fermion/triplet term

Only the vector spinor and linear triplet receive primes:

```math
-\frac12\bar\psi_a{}^i\gamma^a\lambda^jL_{ij}
\ \longmapsto\
-\frac12\bar\psi_a{}^i\gamma^a\lambda'^jL'_{ij}.
\tag{8}
```

The gravitino remains $`\psi_a^i`$. The factor $`-1/2`$ is unchanged, $`a`$ is contracted between the frame gravitino and gamma matrix, and $`i,j`$ contract with $`L'_{ij}`$. Neither spinor nor either $`SU(2)`$ index is interchanged. Its weight is $`1/2+3/2+3=5`$.

### 4.5 Potential–three-form term

Apply (5) to both potentials in the source term:

```math
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A_\mu\partial_\nu E_{\rho\sigma\tau}
\ \longmapsto\
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}.
\tag{9}
```

The $`-1/12`$ is the coefficient of the source potential representative. There is no replacement by a hatted field strength and no boundary conversion. All five world indices are contracted once in $`\varepsilon`$ and once in the other factors. Its weight is $`5+0+0=5`$ in world indices.

Multiplying by the measure exposes the ordinary coordinate density:

```math
e\left(-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}\right)
=-\frac1{12}\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}.
\tag{10}
```

This uses $`e\varepsilon=\widetilde\varepsilon`$ only. It changes neither the boundary representative nor the coefficient.

### 4.6 Scalar bracket: prime every matter occurrence first

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++), procedure_lock=R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1 -->

The remaining source bracket becomes

```math
\begin{aligned}
&\rho\left(N+\frac12\bar\psi_a\gamma^a\varphi
+\frac i4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}\right)\\
&\hspace{8mm}\longmapsto
\rho'\left(N'+\frac12\bar\psi_a\gamma^a\varphi'
+\frac i4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right).
\end{aligned}
\tag{11}
```

The scalar $`\rho'`$ multiplies **all three** bracket entries. Both gravitini in the last entry stay unprimed.

### 4.7 Expand the scalar bracket, one contribution at a time

First, multiplication of its scalar entry gives

```math
\rho'\bigl(N'\bigr)=\rho'N',\qquad w=1+4=5.
\tag{12}
```

Second, multiplication of its one-gravitino entry gives

```math
\rho'\left(\frac12\bar\psi_a\gamma^a\varphi'\right)
=\frac12\rho'\bar\psi_a{}^i\gamma^a\varphi'_i,
\qquad w=1+\frac12+\frac72=5.
\tag{13}
```

The scalar is even, so moving the numerical $`1/2`$ ahead of it introduces no sign. The spinor order is unchanged.

Third, multiplication of its two-gravitino entry gives

```math
\rho'\left(\frac i4\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}\right)
=\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij},
\qquad w=1+\frac12+\frac12+3=5.
\tag{14}
```

There is no additional factor from $`\gamma^{ab}`$ or from $`L'_{ij}`$: their normalized antisymmetrization and the source triplet contraction are already part of (4). For example, making only the gamma definition explicit gives

```math
\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}
=\frac i8\rho'\bar\psi_a{}^i\gamma^a\gamma^b\psi_b{}^jL'_{ij}
-\frac i8\rho'\bar\psi_a{}^i\gamma^b\gamma^a\psi_b{}^jL'_{ij}.
\tag{15}
```

Equation (15) is a normalization check; the result retains the source $`\gamma^{ab}`$ notation. No fermions have been moved through each other.

### 4.8 Assemble the seven entries

Add (6), (7), (8), (9), (12), (13), and (14), preserving their source coefficients:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}
={}&Y'^{ij}L'_{ij}
+i\bar\lambda'\varphi'
-\frac12\bar\psi_a{}^i\gamma^a\lambda'^jL'_{ij}\\
&-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}
A'_\mu\partial_\nu E'_{\rho\sigma\tau}
+\rho'N'\\
&+\frac12\rho'\bar\psi_a\gamma^a\varphi'
+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}
\tag{16}
```

Every equality leading to (16) is pointwise and off shell. In particular, no term has been absorbed into an undisplayed total derivative.

The following is the source-term ledger for subsequent insertion. “Explicit fermions” counts the component spinors as presently displayed, not the underlying fermion order after the two composite maps.

| Entry | Source location | Coefficient | Vector slot | Linear slot | Explicit fermions | Boundary representative |
|---|---|---|---|---|---|---|
| BF-01 | (3.1), triplets | $`1`$ | $`Y'^{ij}`$ | $`L'_{ij}`$ | 0 | Local product |
| BF-02 | (3.1), spinor product | $`i`$ | $`\lambda'`$ | $`\varphi'`$ | 2 | Local product; order fixed |
| BF-03 | (3.1), first gravitino term | $`-1/2`$ | $`\lambda'^j`$ | $`L'_{ij}`$ | 2 | Local product; order fixed |
| BF-04 | (3.1), form term | $`-1/12`$ | $`A'_\mu`$ | $`E'_{\rho\sigma\tau}`$ | 0 | Ordinary $`A'\partial E'_3`$ |
| BF-05 | (3.1), first scalar-bracket entry | $`1`$ | $`\rho'`$ | $`N'`$ | 0 | Local product |
| BF-06 | (3.1), second scalar-bracket entry | $`1/2`$ | $`\rho'`$ | $`\varphi'`$ | 2 | Local product; order fixed |
| BF-07 | (3.1), third scalar-bracket entry | $`i/4`$ | $`\rho'`$ | $`L'_{ij}`$ | 2 | Local product; order fixed |

Each entry contains one vector slot and one linear slot. No coefficient $`C_{1BC}`$ belongs to this ledger yet: those coefficients enter when the new linear components are constructed in Step 2, then reach BF through Step 3.

## 5. Consistency Checks

### 5.1 Indices, parity, weights, and fermion order

The free-index count of each of the seven density terms is zero. The nontrivial contraction lists are: BF-01 $`(i,j)`$; BF-02 the NW–SE spinor doublet contraction; BF-03 $`(a,i,j)`$; BF-04 $`(\mu,\nu,\rho,\sigma,\tau)`$; BF-06 $`(a,i)`$ after resolving the suppressed doublet index; and BF-07 $`(a,b,i,j)`$. BF-05 is a scalar product. All Lorentz and $`SU(2)`$ indices are paired, and the epsilon term is a world scalar before multiplication by $`e`$.

The explicit fermion counts are $`0,2,2,0,0,2,2`$. Thus all seven terms are Grassmann even. Their weight sums, in the same order, are

```math
2+3=5,\quad
\frac32+\frac72=5,\quad
\frac12+\frac32+3=5,\quad
5+0+0=5,\quad
1+4=5,\quad
1+\frac12+\frac72=5,\quad
1+\frac12+\frac12+3=5.
\tag{17}
```

Therefore $`w(e^{-1}\mathcal L_{VL})=5`$ and $`w(\mathcal L_{VL})=-5+5=0`$. In local scale-dimension bookkeeping the density weight five matches the five-dimensional measure. This check does not import canonical Poincaré normalizations before compensator gauge fixing.

The component density contains no omitted higher-order component terms. Nevertheless, products such as $`\rho'N'`$ and $`Y'^{ij}L'_{ij}`$ will contain higher fermion orders once their composite definitions are substituted. Equation (16) must not be interpreted as a quadratic truncation in the underlying unprimed fermions.

### 5.2 Bosonic component limit

Set $`\lambda'=\varphi'=\psi_\mu=0`$ only for this check. BF-02 has a vanishing $`\lambda'`$ and $`\varphi'`$ factor; BF-03 has a vanishing $`\psi_a`$ and $`\lambda'`$ factor; BF-06 has a vanishing $`\psi_a`$ and $`\varphi'`$ factor; BF-07 has two vanishing gravitino factors. The three remaining terms are

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\lambda'=\varphi'=\psi_\mu=0}
=Y'^{ij}L'_{ij}+\rho'N'
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}.
\tag{18}
```

This is exactly the bosonic restriction of source (3.1) with the same priming. It is not yet the Gold $`R^2`$ action.

### 5.3 Zero-gravitino and bilinearity checks

Setting only $`\psi_\mu=0`$ removes BF-03, BF-06, and BF-07, while preserving the matter-fermion coupling:

```math
\left.e^{-1}\mathcal L_{VL}\right|_{\psi_\mu=0}
=Y'^{ij}L'_{ij}+i\bar\lambda'\varphi'+\rho'N'
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu\partial_\nu E'_{\rho\sigma\tau}.
\tag{19}
```

For an identically vanishing vector argument, BF-01 vanishes with $`Y'`$, BF-02 and BF-03 with $`\lambda'`$, BF-04 with $`A'`$, and BF-05–07 with $`\rho'`$. For an identically vanishing linear argument in its zero-potential representative, BF-01, BF-03 and BF-07 vanish with $`L'`$, BF-02 and BF-06 with $`\varphi'`$, BF-04 with $`E'_3`$, and BF-05 with $`N'`$. Thus both bilinearity limits give zero without using a field equation.

### 5.4 Abelian gauge check of the ordinary BF term

This is a check of the retained representative, not a replacement of it. For the primed vector transformation $`\delta A'_\mu=\partial_\mu\alpha'`$ and the constant symbol of (10), the form part of the coordinate density varies as

```math
\begin{aligned}
\delta\mathcal L_{VL}\big|_{\text{form}}
&=-\frac1{12}\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}
(\partial_\mu\alpha')\partial_\nu E'_{\rho\sigma\tau}\\
&=-\frac1{12}\partial_\mu\left(
\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}\alpha'\partial_\nu E'_{\rho\sigma\tau}\right)
+\frac1{12}\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}\alpha'
\partial_\mu\partial_\nu E'_{\rho\sigma\tau}\\
&=-\frac1{12}\partial_\mu\left(
\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}\alpha'\partial_\nu E'_{\rho\sigma\tau}\right).
\end{aligned}
\tag{20}
```

The second line is the ordinary product rule. The last term is zero because its contraction equals one half of the commutator of ordinary partial derivatives:

```math
\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\mu\partial_\nu E'_{\rho\sigma\tau}
=\frac12\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}
(\partial_\mu\partial_\nu-\partial_\nu\partial_\mu)E'_{\rho\sigma\tau}=0.
\tag{21}
```

The boundary variation in (20) is displayed and retained. An invariant integrated action requires, for example, compactly supported gauge parameters or suitable boundary data; no such condition was needed for the pointwise priming calculation.

For the three-form gauge transformation in (3), unit-weight antisymmetrization gives

```math
3\partial_{[\rho}\Lambda'_{\sigma\tau]}
=\partial_\rho\Lambda'_{\sigma\tau}
+\partial_\sigma\Lambda'_{\tau\rho}
+\partial_\tau\Lambda'_{\rho\sigma}.
\tag{22}
```

Its insertion into the same density produces

```math
\delta\mathcal L_{VL}\big|_{\text{form}}
=-\frac1{12}\widetilde\varepsilon^{\mu\nu\rho\sigma\tau}A'_\mu
\left(\partial_\nu\partial_\rho\Lambda'_{\sigma\tau}
+\partial_\nu\partial_\sigma\Lambda'_{\tau\rho}
+\partial_\nu\partial_\tau\Lambda'_{\rho\sigma}\right)=0.
\tag{23}
```

For the first term the symmetric derivative pair is $`(\nu,\rho)`$; for the second it is $`(\nu,\sigma)`$; for the third it is $`(\nu,\tau)`$. Each contracts an antisymmetric pair of the epsilon symbol and vanishes by the commutator argument (21). This is the Abelian form-gauge check; it is not a full local supersymmetry variation.

### 5.5 Signs, numerical factors, and reproducible algebra check

The ordered coefficients after expanding (4) are

```math
\left(1,\ i,\ -\frac12,\ -\frac1{12},\ 1,\ \frac12,\ \frac i4\right).
\tag{24}
```

Equations (6)–(14) retain them entry by entry. The single interchange in (6) involves bosons; every fermion bilinear retains its original order. The gamma normalization check (15) accounts explicitly for the $`1/2`$ inside $`\gamma^{ab}`$.

The independent symbolic audit in [verify_step1_primed_bf.py](../../../../src/kernels/verify_step1_primed_bf.py) expands the grouped source expression with noncommuting ordered factors, compares the seven ordered words with the final-density transcription, checks all seven exact weight sums, tests the displayed zero-field limits, and checks the epsilon/symmetric-derivative contractions by explicit five-index permutation sums. Its report is generated as `build/step1_primed_bf_verification.json` in the [component-check runner](../../../../checks/run_component_checks.py)'s temporary directory. These checks audit relabelling, distribution, ordering and the displayed tensor identities; they do not evaluate a supersymmetry variation or the later composite maps.

Reality and symplectic Majorana type are preserved by the identity relabelling (5): the same spinor real structure and source factors $`i`$ occur before and after it, with no analytic continuation or conjugation change. A separate Hermitian-conjugation proof of the published density is not performed. There is no five-dimensional Weyl chirality projection. The background-independent coefficients have a regular $`g\to0`$ limit. The composite-action limit after map substitution is given in [Step 6, §5.5](10_step6_gauged_action_through_two_fermions.md#55-limits-and-verification-scope).

## 6. Final Result

With the source potential representative and the primed arguments (1), the complete BF density for Step 1 is

```math
\boxed{\begin{aligned}
e^{-1}\mathcal L_{VL}
={}&L'_{ij}Y'^{ij}+\rho'N'
+i\bar\lambda'\varphi'
-\frac12\bar\psi_a{}^i\gamma^a\lambda'^jL'_{ij}\\
&-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\tau}
A'_\mu\partial_\nu E'_{\rho\sigma\tau}\\
&+\frac12\rho'\bar\psi_a\gamma^a\varphi'
+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL'_{ij}.
\end{aligned}}
\tag{25}
```

The first two entries use the stated primed-first order. Compared with (16), this only moves Grassmann-even summands and commutes the two even triplets. All seven source terms remain present. The corresponding action is $`S_{VL}=\int d^5x\,\mathcal L_{VL}`$, with exactly this source normalization.

**Step 1 is complete.** The result is the full component density ready for Step 2's construction of the new primed linear multiplet. It is exact at this stage, off shell and gauge unfixed, with no approximation error or discarded fermion order.

## 7. Convention Dependence and Remaining Uncertainties

- The result uses the source orientation, Majorana-bar phase, gamma normalization and BF coefficient. A change to any of these conventions requires an explicit conversion. None is made here.
- $`E'_{\mu\nu\rho}`$ represents the new mixed primed linear output. Its construction from the two vectors is given in [Step 2](04_step2_mixed_primed_linear_multiplet.md). The original unprimed linear multiplet remains the shared input to the later, different vector maps.
- The potential $`A'_\mu`$ is retained as a vector slot. The earlier map directly supplies $`\widehat F'_{\mu\nu}`$; the local potential representative is derived in [Step 5](08_step5_primed_composite_vector_insertion.md). Equation (25) neither guesses a potential nor identifies an ordinary strength with a hatted one.
- The BF density feeds the mixed-map construction and two vector substitutions in Steps 2–5. The [gauged $`R^2`$ action through two physical fermions](10_step6_gauged_action_through_two_fermions.md) and [total-action normalization](12_total_action_zeroth_first_second_orders.md) give the retained endpoint. An independent all-order local supersymmetry or reality proof is outside this construction.
- No source-omitted higher-fermion term in a later Coomans composite has been set to zero. Such omissions concern subsequent expansions, not a missing term in the seven-term source density reproduced here.
- Steps 2–6, gauge fixing, auxiliary equations, backgrounds and spectra have not been executed in this note.
