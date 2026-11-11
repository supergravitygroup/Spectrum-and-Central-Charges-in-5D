# Step 1: independent check of the generic Gold linear-multiplet bridge

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

Scope: convention comparison of the Gold-to-Bergshoeff/Özkan linear multiplet, with exact Q/S coefficient matching. This does not certify a completed LOG invariant or nonlinear gauge-fixed supersymmetry.

The parent convention source is [CONVENTIONS.md](../CONVENTIONS.md), lock `GAUGED-LOG-CONVENTIONS-v1`. Equations (LB42)–(LB44) follow [the full superform derivation](../../../../../../../references/source_evidence/log/derivations/form-interface.md), which closes the generic form/potential interface for a genuine linear multiplet.

<!-- ASSERT_CONVENTION: regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

## 1. Problem and Target

Determine the conversion of a **generic**, off-shell Gold linear multiplet
$`(G_{ij},\varphi_{Gi},F_G,\mathcal H_{Ga})`$ to the component multiplet
$`(L_{ij},\varphi_i,N,E_a)`$. The LOG multiplet is a later particular composite of these slots. No auxiliary equation, gauge fixing, fermion truncation, background, integration by parts, or action equation is used here.

Sources inspected as page images, not only extracted text:

| Input | Exact source location | Cached page |
|---|---|---|
| Gold covariant linear rules | C24 (2.50)–(2.53b), PDF22 / printed21 | [C24-p022](https://arxiv.org/abs/2311.00679) |
| Gold potential rule | C24 (2.54), PDF23 / printed22 | [C24-p023](https://arxiv.org/abs/2311.00679) |
| Weyl/parameter bridge | C24 Appendix C, Tables4–5, PDF91 / printed90 | [C24-p091](https://arxiv.org/abs/2311.00679) |
| Vector calibration | C24 Table6, PDF92 / printed91; scalar rule (2.38a), PDF18 | [C24-p092](https://arxiv.org/abs/2311.00679), [C24-p018](https://arxiv.org/abs/2311.00679) |
| Component linear rules | OP (2.18)–(2.23), PDF9 / printed9 | [OP-p009](https://arxiv.org/abs/1301.6622) |
| Component potential rules and density | OP (2.24), (3.1)–(3.2), PDF10 / printed10 | [OP-p010](https://arxiv.org/abs/1301.6622) |
| Gold BF displays | S23 (3.2b), PDF14; C24 (3.2b–c), PDF24 | [S23-p014](https://arxiv.org/abs/2302.14295), [C24-p024](https://arxiv.org/abs/2311.00679) |

The cited branch conventions control the explicitly declared five-dimensional calculation.

## 2. Convention Ledger

Use $`D=5`$, $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$, natural units, and weighted (anti)symmetrization. Frame indices are $`a,b=0,\ldots,4`$ and doublet indices $`i,j=1,2`$. All physical spinors and SUSY parameters are Grassmann odd; a parameter-contracted SUSY variation is even. No Fourier transform or state normalization occurs.

The component Clifford and orientation conventions are

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{01234}=i,\qquad
\epsilon_B^{01234}=1,\qquad
\epsilon_{B01234}=-1.
\tag{LB01}
```

The bar is the linear Majorana transpose $`\bar\zeta=\zeta^T\mathsf C`$, including $`\overline{i\zeta}=i\bar\zeta`$. The NW–SE doublet convention is

```math
X_i=X^j\varepsilon_{ji},\qquad X^i=\varepsilon^{ij}X_j,
\qquad \varepsilon_{12}=\varepsilon^{12}=1.
\tag{LB02}
```

In particular, $`\bar\xi\varphi=\bar\xi^i\varphi_i`$ and $`\bar\xi_i\varphi^i=-\bar\xi^i\varphi_i`$. Moving a doublet index is not an innocent notational substitution.

The C24 Tables4–5 bridge needed here is

```math
\begin{aligned}
\Gamma_G^a&=i\gamma^a,&\Sigma_G^{ab}&=\frac12\gamma^{ab},&
w_{Gab}&=\frac{16}{3}T_{ab},&\epsilon_G^{abcde}&=-\epsilon_B^{abcde},\\
\epsilon_B^i&=2\xi^i,&
\eta_B^i&=-2i\eta_G^i+\frac23T_{ab}\gamma^{ab}\xi^i,&
\Lambda_{K,B}^a&=-\Lambda_{K,G}^a+\frac23\xi^i\gamma^a\chi_i.
\end{aligned}
\tag{LB03}
```

The $`S`$ and $`K`$ connections receive the corresponding source shifts. C24 Appendix C, paragraph before Table4, identifies the **whole** covariant vector derivative across conventions; individual named connections are not set equal. The four covariant linear-slot rules (2.52) have no explicit $`K`$ term. Thus the displayed $`K`$ shift does not change these primary covariant slots, but must be retained when acting on their covariant derivatives or dependent connections.

Gold's explicit contracted spinor products are converted in their written order. The contraction sign is calibrated by $`W_G=\sigma`$, $`\lambda_G=-\lambda_B`$ and $`\delta W=i\xi_i\lambda_G^i`$ against $`\delta\sigma=i\bar\epsilon\lambda_B/2`$; their equality uses $`\bar\xi_i\lambda_B^i=-\bar\xi^i\lambda_{Bi}`$. No Hermitian conjugation is used.

## 3. Definitions and Required Identities

Introduce one dimensionless, real, nonzero normalization $`a`$ and three initially undetermined conversion factors:

```math
G_{ij}=aL_{ij},\qquad
\varphi_{Gi}=b\varphi_i,\qquad F_G=cN,\qquad
\mathcal H_{Ga}=dE_a.
\tag{LB04}
```

Here $`a`$ is a normalization of the entire linear multiplet, not a new physical coupling. Homogeneous transformation rules cannot fix it.

Lowering the component spinor transformation requires

```math
(L^{ij}\epsilon_j)_k=-L_{kj}\epsilon^j.
\tag{LB05}
```

For a concrete check, take $`L^{ij}=\begin{pmatrix}2&3\\3&5\end{pmatrix}`$ and $`\xi^i=(7,11)`$. Then $`L_{ij}=\begin{pmatrix}5&-3\\-3&2\end{pmatrix}`$ and both sides of (LB05) give $`(-2,-1)`$.

The bar of the $`S`$ shift is

```math
\bar\eta_B=-2i\bar\eta_G-\frac23\bar\xi\gamma^{ab}T_{ab}.
\tag{LB06}
```

The second minus follows from $`(\gamma^{ab})^T\mathsf C=-\mathsf C\gamma^{ab}`$; the first coefficient is not complex conjugated.

Two identities needed for the vector slot are

```math
T_{bc}\gamma^{bc}\gamma_a
=T_{bc}\gamma_a{}^{bc}-2T_{ab}\gamma^b,
\qquad
\gamma_{abc}=-\frac i2\epsilon_{Babcde}\gamma^{de}.
\tag{LB07}
```

The first follows by substituting
$`\gamma^{bc}\gamma_a=\gamma^{bc}{}_a+\delta_a^c\gamma^b-\delta_a^b\gamma^c`$
and using $`T_{ba}=-T_{ab}`$. The second is the rank-three specialization of the master C04c duality, including reversal of the final gamma indices.

## 4. Detailed Derivation

### 4.1 Triplet and spinor slots

The triplet variations are

```math
\delta G_{ij}=-2\bar\xi_{(i}\varphi_{Gj)}
=-2b\bar\xi_{(i}\varphi_{j)},\qquad
\delta(aL_{ij})=2ia\bar\xi_{(i}\varphi_{j)}.
\tag{LB08}
```

Hence $`b=-ia`$. This comparison keeps both doublet indices lowered throughout.

The lowered OP spinor rule, after (LB05), is

```math
\begin{aligned}
\delta\varphi_i={}&
\frac i2\gamma^a\mathcal D_aL_{ij}\epsilon_B^j
-\frac i2\gamma^a E_a\epsilon_{Bi}
+\frac12N\epsilon_{Bi}
+\gamma^{ab}T_{ab}L_{ij}\epsilon_B^j
-3L_{ij}\eta_B^j.
\end{aligned}
\tag{LB09}
```

Insert (LB03). The last two terms give

```math
2\gamma^{ab}T_{ab}L_{ij}\xi^j
-3L_{ij}\left(-2i\eta_G^j+\frac23\gamma^{ab}T_{ab}\xi^j\right)
=6iL_{ij}\eta_G^j.
\tag{LB10}
```

The apparent $`T`$ discrepancy cancels only when the field-dependent $`S`$ shift is retained. Multiplication by $`b=-ia`$ then gives

```math
\delta(-ia\varphi_i)
=a\gamma^b\mathcal D_bL_{ij}\xi^j
-a\gamma^bE_b\xi_i-iaN\xi_i+6aL_{ij}\eta_G^j.
\tag{LB11}
```

C24 (2.52b), after (LB03)–(LB04), independently becomes

```math
\delta\varphi_{Gi}
=a\gamma^b\mathcal D_bL_{ij}\xi^j
+\frac d2\gamma^bE_b\xi_i-\frac{ic}{2}N\xi_i
+6aL_{ij}\eta_G^j.
\tag{LB12}
```

Matching the $`E`$ and $`N`$ coefficients fixes $`d=-2a`$ and $`c=2a`$.

### 4.2 Scalar slot

The four terms of C24 (2.52c) become, in source order,

```math
\begin{aligned}
2\xi^i\Gamma_G^a\nabla_a\varphi_{Gi}
&=2a\bar\xi\not{\mathcal D}\varphi,\\
-\frac32(\xi^i\Sigma_G^{ab}\varphi_{Gi})w_{Gab}
&=4ia\bar\xi\gamma^{ab}T_{ab}\varphi,\\
16i(\xi^i\chi^j)G_{ij}
&=16ia\bar\xi^i\chi^jL_{ij},\\
6i\eta_G^i\varphi_{Gi}
&=6a\bar\eta_G\varphi.
\end{aligned}
\tag{LB13}
```

The second coefficient is
$`-(3/2)(1/2)(-ia)(16/3)=4ia`$.

On the OP side, insert both $`\epsilon_B=2\xi`$ and (LB06):

```math
\begin{aligned}
\delta(2aN)
={}&2a\left[\bar\xi\not{\mathcal D}\varphi
+3i\bar\xi\gamma^{ab}T_{ab}\varphi
+8i\bar\xi^i\chi^jL_{ij}
+\frac{3i}{2}\left(-2i\bar\eta_G-\frac23\bar\xi\gamma^{ab}T_{ab}\right)\varphi\right]\\
={}&2a\bar\xi\not{\mathcal D}\varphi
+4ia\bar\xi\gamma^{ab}T_{ab}\varphi
+16ia\bar\xi^i\chi^jL_{ij}
+6a\bar\eta_G\varphi.
\end{aligned}
\tag{LB14}
```

This matches every displayed source scalar-slot term.

### 4.3 Constrained vector slot

C24 (2.52d) becomes

```math
\begin{aligned}
\delta\mathcal H_{Ga}={}&
2ia\bar\xi\gamma_{ab}\mathcal D^b\varphi
-\frac{8a}{3}T_{ab}\bar\xi\gamma^b\varphi
+\frac{4ia}{3}\epsilon_{Babcde}T^{bc}\bar\xi\gamma^{de}\varphi
-8ia\bar\eta_G\gamma_a\varphi.
\end{aligned}
\tag{LB15}
```

The epsilon coefficient includes **all** factors:
$`(1/2)(-1)(16/3)(1/2)(-ia)=4ia/3`$.

Independently, the OP rule gives

```math
\begin{aligned}
\delta(-2aE_a)={}&
2ia\bar\xi\gamma_{ab}\mathcal D^b\varphi
-8aT_{ab}\bar\xi\gamma^b\varphi
-8ia\bar\eta_G\gamma_a\varphi
-\frac{8a}{3}\bar\xi\gamma^{bc}T_{bc}\gamma_a\varphi.
\end{aligned}
\tag{LB16}
```

Use (LB07) in the last term:

```math
\begin{aligned}
-8aT_{ab}\bar\xi\gamma^b\varphi
-\frac{8a}{3}\bar\xi\gamma^{bc}T_{bc}\gamma_a\varphi
={}&-\frac{8a}{3}T_{ab}\bar\xi\gamma^b\varphi
-\frac{8a}{3}T_{bc}\bar\xi\gamma_a{}^{bc}\varphi\\
={}&-\frac{8a}{3}T_{ab}\bar\xi\gamma^b\varphi
+\frac{4ia}{3}\epsilon_{Babcde}T^{bc}\bar\xi\gamma^{de}\varphi.
\end{aligned}
\tag{LB17}
```

Thus (LB16) is (LB15). The covariant constraints also match:
$`\nabla^a\mathcal H_{Ga}=-2a\mathcal D^aE_a=0`$.

### 4.4 Potential-interface diagnostic

At bosonic order C24 and OP give

```math
h_G^a=-\frac1{24}\epsilon_G^{abcde}(4\partial_{[b}b_{cde]})
=\frac16\epsilon_B^{abcde}\partial_b b_{cde},
\qquad E^a=-\frac1{12}\epsilon_B^{abcde}\partial_b E_{cde}.
\tag{LB18}
```

Consequently $`b_{G\mu\nu\rho}=aE_{\mu\nu\rho}`$ is the bosonic potential map, locally modulo a closed three-form and gauge freedom. The complete superform pullback now establishes this map for the full potentials, locally modulo form gauge transformations; source C24 (2.54) gives

```math
\delta E_{\mu\nu\rho}
=+\bar\epsilon_B\gamma_{\mu\nu\rho}\varphi
-3i\bar\psi_{[\mu}^i\gamma_{\nu\rho]}\epsilon_B^jL_{ij}
+3\partial_{[\mu}\Lambda_{\nu\rho]}.
\tag{LB19}
```

The first coefficient follows explicitly from
$`2\epsilon_G\xi_i\Sigma_G\varphi_G =ia\epsilon_B\bar\xi_i\gamma_2\varphi^i =-ia\epsilon_B\bar\xi\gamma_2\varphi =2a\bar\xi\gamma_3\varphi`$.
The second is $`(-12i)a(1/2)(1/2)=-3ia`$ before dividing by $`a`$.

Relative to the printed OP (2.24), the resulting difference is

```math
\Delta(\delta E_{\mu\nu\rho})
=2\bar\epsilon_B\gamma_{\mu\nu\rho}\varphi
-4i\bar\psi_{[\mu}^i\gamma_{\nu\rho]}\epsilon_B^jL_{ij}.
\tag{LB20}
```

Even the leading flat-space sign mismatch survives when the gravitino is zero. This confirms the existing master X10 quarantine. Equation (LB19) is now derived as the full potential law by [the full superform derivation](../../../../../../../references/source_evidence/log/derivations/form-interface.md), (FI19)–(FI24), including exact spinor indices and the graded pullback. Literal OP and Gold source formulas remain preserved separately from this derived repair.

## 5. Consistency Checks

- **All four Q/S transformation slots:** explicit algebra (LB08)–(LB17), including the induced $`S`$ shift and its Majorana transpose. No action equation or fermion truncation is used.
- **Covariant constraint:** $`\nabla\cdot\mathcal H_G=-2a\mathcal D\cdot E`$ with nonzero constant $`a`$; hence the same constrained field is carried across the interface.
- **Doublet lowering:** the concrete test following (LB05) gives $`(-2,-1)`$ on both sides.
- **Clifford identities:** run the existing frozen common-convention checker read-only, then separately test (LB07) for each of the ten independent two-form basis elements and five values of $`a`$. Both sets of 50 matrix equalities pass. The test uses the master $`4\times4`$ mostly-plus Clifford representation with $`\gamma^{01234}=i`$.
- **Exact rational factors:** $`(3/2)(1/2)(16/3)=4`$, $`3-(3/2)(2/3)=2`$, $`-8+(8/3)2=-8/3`$, and $`(8/3)(1/2)=4/3`$ were checked using rational arithmetic.
- **Weights:** $`w(G)=w(L)=3`$, $`w(\varphi_G)=w(\varphi)=7/2`$, and $`w(F)=w(N)=w(\mathcal H)=w(E)=4`$. Constants $`a,b,c,d`$ have weight zero. With $`w(\xi)=-1/2`$, $`w(\eta)=1/2`$, $`w(T)=1`$, $`w(\chi)=3/2`$, each term in (LB11), (LB14), and (LB15) has respectively weight $`7/2`$, $`4`$, and $`4`$.
- **Reality:** the source/project spinor phase $`-i`$ is explicit. It must be carried through the source's reality conventions; replacing the linear Majorana bar by an antilinear Dirac bar would spoil (LB14). This check establishes consistent algebraic conjugation, not a new independent derivation of the superspace reality structure.
- **Flat limit:** setting $`T=\chi=0`$ removes the field-dependent $`S`$ correction and its associated terms, leaving identical derivative, scalar, vector and pure-$`S`$ rules.
- **Ungauged/gauged scope:** these are Standard-Weyl generic-slot identities before the gauged map. No gauge-coupling dependence has been invented.
- **Boundary terms:** none are discarded in this derivation. The BF/form-action comparison and its boundary current belong to the parent Step1 result.

Terminal result of the explicit matrix/rational check:

```text
PASS: 50 T.gamma gamma_a identities; 50 epsilon-dual identities;
SU2 lowering test=(-2,-1); scalar/vector rational coefficients exact.
```

## 6. Final Result

The generic linear multiplet bridge is

```math
\boxed{
G_{ij}=aL_{ij},\qquad
\varphi_{Gi}=-ia\varphi_i,\qquad
F_G=2aN,\qquad
\mathcal H_{Ga}=-2aE_a
},\qquad a\in\mathbb R\setminus\{0\}.
\tag{LB21}
```

The parent density matching chooses the convenient representative $`a=-1/2`$:

```math
\boxed{
G_{ij}=-\frac12L_{ij},\qquad
\varphi_{Gi}=\frac i2\varphi_i,\qquad
F_G=-N,\qquad\mathcal H_{Ga}=E_a
}.
\tag{LB22}
```

Changing $`a`$ rescales the **entire** linear multiplet and its BF invariant. It is not permitted to alter only one slot or silently transfer the normalization of another invariant. The relative factors in (LB21) are fixed by the source Q/S rules; the overall action normalization depends on every density term, including the ordinary/current distinction.

## 7. Convention Dependence and Remaining Uncertainties

1. The generic covariant-slot map is checked. The later substituted LOG primary/descendants are not independently derived by this test.
2. The numerical choice $`a=-1/2`$ comes from the parent's BF matching. This note independently verifies its transformation compatibility, not the missing form-current comparison.
3. C24 (3.2b) and S23 (3.2b) print a covariant $`\mathcal H`$ in the BF term, whereas the original superform action uses the ordinary four-form dual. Equations (FI25)–(FI31) of [the full superform derivation](../../../../../../../references/source_evidence/log/derivations/form-interface.md) derive the required $`h_G=P`$ coupling and its complete fermionic current. C24 (3.2c) agrees with that ordinary form representative up to the displayed divergence.
4. The potential residual (LB20) identifies the incompatible literal OP potential law under the fixed map. The full superform derivation supports (LB19); it does not certify the later expanded LOG multiplet merely by naming its four slots.
5. All source spinor index placements must be preserved in the conversion of C24 (2.50). The master cached-page image is evidence; a previously typed contraction is not a substitute for checking which SU(2) index is up or down.
6. No nonlinear SUSY, target gauge closure, auxiliary elimination, full LOG action, vacuum or spectrum claim is made.

## 8. Explicit chi sector of the Lorentz-curvature bridge

**Result:** the C24 bridge agrees with the project's **positive-eight coefficient in the written $`\bar\psi_{[\mu}e_{\nu]}`$ ordering**. An apparent $`-8`$ versus $`+8`$ disagreement vanishes once the antisymmetrized vielbein/gravitino ordering is put in the same form.

The explicit chi-sector comparison uses C24 **(2.18c)**, [PDF13 / printed12](https://arxiv.org/abs/2311.00679), C24 **Table4**, [PDF91 / printed90](https://arxiv.org/abs/2311.00679), and literal OP **(2.7)**, [PDF7 / printed7](https://arxiv.org/abs/1301.6622). The project comparison is master **R03/X01**. The object checked is only the **explicit** $`\bar\psi\gamma\chi`$ term while $`R(Q)`$, $`\phi_B`$, $`f_B`$, and $`\omega_B`$ are held as named slots. No hidden chi dependence of these slots is expanded or counted a second time.

### 8.1 Source terms and double antisymmetrization

C24 (2.18c) contains

```math
R_G(M)_{ab}{}^{cd}\supset
8\delta_{[a}{}^{[c}\mathfrak f_{G,b]}{}^{d]}
+\frac{16i}{3}\delta_{[a}{}^{[c}\psi_{b]i}\Gamma_G^{d]}\chi^i.
\tag{LB23}
```

The Table4 substitutions relevant for this sector are

```math
\mathfrak f_{G,a}{}^c=-f_{B,a}{}^c+\frac13\bar\psi_a^i\gamma^c\chi_i,
\qquad\Gamma_G^a=i\gamma^a,
\qquad R_G(M)_{ab}{}^{cd}=-R_B(M)_{ab}{}^{cd}.
\tag{LB24}
```

The compact contracted Gold product in (LB23) is from top left to bottom right in spinor indices, as C24 PDF13 footnote6 specifies. The lower-first/upper-second doublet contraction is

```math
\psi_{bi}\Gamma_G^d\chi^i
=i\bar\psi_{bi}\gamma^d\chi^i
=-i\bar\psi_b^i\gamma^d\chi_i.
\tag{LB25}
```

There is no interchange of two odd spinors in this operation; its minus is the NW–SE doublet contraction.

For transparency define only the two orderings being compared:

```math
\begin{aligned}
K_{ab}{}^{cd}
&=\delta_{[a}{}^{[c}\bar\psi_{b]}^i\gamma^{d]}\chi_i\\
&=\frac14\left(
\delta_a^c\bar\psi_b\gamma^d\chi
-\delta_b^c\bar\psi_a\gamma^d\chi
-\delta_a^d\bar\psi_b\gamma^c\chi
+\delta_b^d\bar\psi_a\gamma^c\chi\right),\\
J_{ab}{}^{cd}
&=\bar\psi_{[a}^i\delta_{b]}{}^{[c}\gamma^{d]}\chi_i\\
&=\frac14\left(
\delta_b^c\bar\psi_a\gamma^d\chi
-\delta_a^c\bar\psi_b\gamma^d\chi
-\delta_b^d\bar\psi_a\gamma^c\chi
+\delta_a^d\bar\psi_b\gamma^c\chi\right)
=-K_{ab}{}^{cd}.
\end{aligned}
\tag{LB26}
```

Each independent two-index bracket contributes $`1/2`$, hence the $`1/4`$. Commuting the even Kronecker delta through a spinor introduces no Grassmann sign; the minus is entirely the exchange inside the $`[ab]`$ antisymmetrization.

### 8.2 Conversion and comparison

The explicit chi term generated by the special-conformal connection shift is

```math
8\delta_{[a}{}^{[c}\left(\frac13\bar\psi_{b]}^i\gamma^{d]}\chi_i\right)
=\frac83K_{ab}{}^{cd}.
\tag{LB27}
```

The explicitly written Gold chi term gives, by (LB25),

```math
\frac{16i}{3}\delta_{[a}{}^{[c}\left(-i\bar\psi_{b]}^i\gamma^{d]}\chi_i\right)
=\frac{16}{3}K_{ab}{}^{cd}.
\tag{LB28}
```

Consequently the sum in $`R_G`$ is $`8K`$. Apply the curvature sign map before comparing to the project:

```math
\left.R_B(M)_{ab}{}^{cd}\right|_{\text{explicit }\psi\chi}
=-\left(\frac83+\frac{16}{3}\right)K_{ab}{}^{cd}
=-8K_{ab}{}^{cd}
=+8J_{ab}{}^{cd}.
\tag{LB29}
```

After conversion to world indices this is

```math
\boxed{
\left.R_B(M)_{\mu\nu}{}^{cd}\right|_{\text{explicit }\psi\chi}
=+8\bar\psi_{[\mu}^i e_{\nu]}{}^{[c}\gamma^{d]}\chi_i
}.
\tag{LB30}
```

This is precisely master R03/X01. Literal OP (2.7) has $`-8J=+8K`$, so its coefficient remains opposite. The source conversion supports the project's existing repair; it does not require a new curvature convention or an additional correction to the master.

### 8.3 Checks and exact scope

The following executable arithmetic checks all $`5^4=625`$ index components. The entries $`U_a{}^b`$ stand only for the even bilinear $`\bar\psi_a\gamma^b\chi`$ during this tensor-order check; they do not impose spinor equations or replace the displayed derivation.

```python
from fractions import Fraction as F
from itertools import product
U = [[2 + 3*a - 5*b + 7*a*b for b in range(5)] for a in range(5)]
delta = lambda a, b: int(a == b)
def K(a, b, c, d):
    return F(delta(a,c)*U[b][d] - delta(b,c)*U[a][d]
             - delta(a,d)*U[b][c] + delta(b,d)*U[a][c], 4)
def J(a, b, c, d):
    return F(U[a][d]*delta(b,c) - U[b][d]*delta(a,c)
             - U[a][c]*delta(b,d) + U[b][c]*delta(a,d), 4)
for a, b, c, d in product(range(5), repeat=4):
    assert J(a,b,c,d) == -K(a,b,c,d)
    assert -(F(8,3) + F(16,3))*K(a,b,c,d) == 8*J(a,b,c,d)
U = [[0]*5 for _ in range(5)]
U[2][3] = 4
assert K(1,2,1,3) == 1 and J(1,2,1,3) == -1
```

Result: **PASS**, 625 index-order identities and 625 coefficient equalities. The sparse check gives $`K_{12}{}^{13}=1`$: converted Gold and project expressions are both $`-8`$, whereas literal OP is $`+8`$.

Both brackets in (LB26) are antisymmetric as required. The world-index bilinear has Weyl weight $`-1/2-1+3/2=0`$, agreeing with $`R_{\mu\nu}{}^{cd}(M)`$. The tangent version has weight two. All equalities are exact slot-wise equalities; no boundary current, background, field equation or bosonic restriction is used. The result checks the explicit chi interface only. It does not certify all curvature terms or expand the hidden chi dependence of the held covariant slots.

## 9. Potential law and the principal derivative of the SUSY parameter

The calculation in §§9.1–9.2 checks a necessary local covariance condition. The independent full superform proof now establishes the current and potential law, including the undifferentiated-parameter terms; its closed-five-form argument establishes generic BF invariance conditional on the true linear constraint. The local principal test remains a separate cross-check.

### 9.1 Data and retained order

Use the component current bridge in master A02, sourced from OPall (3.2):

```math
\begin{aligned}
P^a&=E^a+Q_1^a+Q_2^a,
&P^a&=-\frac1{12}\epsilon_B^{abcde}\partial_bE_{cde},\\
Q_1^a&=\frac i2\bar\psi_b\gamma^{ba}\varphi,
&Q_2^a&=\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
\tag{LB31}
```

The second equality is written in a local frame at the test point; the ordinary derivative and inverse vielbeins can equivalently be kept in world indices as in A02a. Variations of the explicit frame factors contain $`\epsilon`$, but no derivative of $`\epsilon`$, so they do not change the sector checked here. Neither matter-field equations nor bosonic truncation are imposed.

Parameterize the two source structures in the potential law by

```math
\delta E_{cde}
=\alpha\bar\epsilon\gamma_{cde}\varphi
+\beta i\bar\psi_{[c}^i\gamma_{de]}\epsilon^jL_{ij}
+3\partial_{[c}\Lambda_{de]}.
\tag{LB32}
```

Retain exactly the terms proportional to a single ordinary derivative of the local SUSY parameter, using $`\delta\psi_b|_{\partial\epsilon}=\partial_b\epsilon`$. The independent linear-multiplet fields have algebraic Q/S parameters in OP (2.18), so their variations supply no $`\partial\epsilon`$ term. The relevant Clifford and Grassmann identities are

```math
\epsilon_B^{abcde}\gamma_{cde}=6i\gamma^{ab},\qquad
\epsilon_B^{abcde}\gamma_{de}=2i\gamma^{abc},\qquad
\bar\zeta^i\gamma^{abc}\vartheta^j=-\bar\vartheta^j\gamma^{abc}\zeta^i.
\tag{LB33}
```

The last identity is for two fixed **upper** doublet indices and odd spinors. No contracted-doublet flip is substituted for it.

### 9.2 Potential and current variations

The first potential term contributes

```math
\begin{aligned}
\left.\delta P^a\right|_{\alpha,\partial\epsilon}
&=-\frac{\alpha}{12}\epsilon_B^{abcde}
(\partial_b\bar\epsilon)\gamma_{cde}\varphi\\
&=-\frac{\alpha i}{2}(\partial_b\bar\epsilon)\gamma^{ab}\varphi
=\frac{\alpha i}{2}(\partial_b\bar\epsilon)\gamma^{ba}\varphi.
\end{aligned}
\tag{LB34}
```

The second term gives

```math
\begin{aligned}
\left.\delta P^a\right|_{\beta,\partial\epsilon}
&=-\frac{\beta i}{12}\epsilon_B^{abcde}
\bar\psi_c^i\gamma_{de}(\partial_b\epsilon^j)L_{ij}\\
&=\frac\beta6\bar\psi_c^i\gamma^{abc}(\partial_b\epsilon^j)L_{ij}\\
&=-\frac\beta6(\partial_b\bar\epsilon^j)\gamma^{abc}\psi_c^iL_{ij}
=-\frac\beta6(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
\tag{LB35}
```

The antisymmetrization in (LB32) is absorbed by contraction with epsilon with no extra factor: relabeling each of its unit-weight terms gives the same contraction. The third line uses the fixed-upper rank-three odd-spinor flip; the last equality relabels $`i,j`$ and uses $`L_{ij}=L_{ji}`$.

The current completions vary as

```math
\left.\delta Q_1^a\right|_{\partial\epsilon}
=\frac i2(\partial_b\bar\epsilon)\gamma^{ba}\varphi,
\tag{LB36}
```

and

```math
\begin{aligned}
\left.\delta Q_2^a\right|_{\partial\epsilon}
&=\frac14\left[(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^j
+\bar\psi_b^i\gamma^{abc}(\partial_c\epsilon^j)\right]L_{ij}\\
&=\frac14\left[(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^j
-(\partial_c\bar\epsilon^j)\gamma^{abc}\psi_b^i\right]L_{ij}\\
&=\frac12(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
\tag{LB37}
```

For the last line interchange $`b,c`$ in the second term, so $`\gamma^{acb}=-\gamma^{abc}`$, then interchange the dummy doublet labels. Thus both gravitino variations contribute with the same sign.

Collecting $`E=P-Q_1-Q_2`$ gives

```math
\left.\delta E^a\right|_{\partial\epsilon}
=(\alpha-1)\frac i2(\partial_b\bar\epsilon)\gamma^{ba}\varphi
-\frac{\beta+3}{6}(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\tag{LB38}
```

These are independent field structures. Covariance of $`E^a`$ therefore requires

```math
\boxed{\alpha=1,\qquad\beta=-3.}
\tag{LB39}
```

These coefficients are precisely the conversion (LB19) of C24 (2.54). Literal OP (2.24), $`\alpha=-1`$ and $`\beta=1`$, instead leaves

```math
\left.\delta E^a\right|_{\partial\epsilon,\,\mathrm{literal\ OP}}
=-i(\partial_b\bar\epsilon)\gamma^{ba}\varphi
-\frac23(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\tag{LB40}
```

The principal test supports the C24-derived potential coefficients. The additional full potential and closure argument is given in [the full superform derivation](../../../../../../../references/source_evidence/log/derivations/form-interface.md), (FI19)–(FI27); it is not inferred from this principal test.

### 9.3 The separate current-completion discrepancy

The parent checked PDF glyph positions in C24 (2.50): the first gravitino carries **lower** $`i`$, and the linear spinor carries **upper** $`i`$. The master transcription of those positions is literal. Together with the normalized map (LB22), its first completion is

```math
2(\Sigma_G^{ab})_\alpha{}^\beta
\psi_{bi}^{\alpha}\varphi_{G\beta}{}^i
=\frac i2\bar\psi_{bi}\gamma^{ab}\varphi^i
=-\frac i2\bar\psi_b^i\gamma^{ab}\varphi_i
=Q_1^a.
\tag{LB41}
```

The source's second completion has two upper spinor indices contracted with the two-lowered-index generator. In a spinor basis calibrated by the scalar bilinear, take the upper-index spinor metric to be $`-\mathsf C`$ and its inverse to be $`\mathsf C`$, with $`\mathsf C^2=-1`$. For a generator matrix $`M=\gamma^{bc}/2`$ acting on lower spinor columns, the source rule $`M_{\alpha\beta}=\varepsilon_{\beta\gamma}M_\alpha{}^\gamma`$ gives $`M\mathsf C^T=-M\mathsf C`$. Thus

```math
(-\mathsf C)^T(M\mathsf C^T)(-\mathsf C)=-\mathsf C M.
\tag{LB42}
```

This gives minus the ordinary Majorana bilinear. The sign comes from lowering the second matrix index, not from reordering spinors. Converting both lower doublet indices and the upper symmetric triplet together yields

```math
\begin{aligned}
-\frac i2\epsilon_G^{abcde}(\Sigma_{Gbc})_{\alpha\beta}
\psi_{di}^{\alpha}\psi_{ej}^{\beta}G^{ij}
&=\frac i8\epsilon_B^{abcde}\bar\psi_d^i\gamma_{bc}\psi_e^jL_{ij}\\
&=-\frac14\bar\psi_d^i\gamma^{ade}\psi_e^jL_{ij}=-Q_2^a.
\end{aligned}
\tag{LB43}
```

The first coefficient is $`(-i/2)(-1)(-1/2)(-1/2)=+i/8`$; the second line uses $`\epsilon_B^{abcde}\gamma_{bc}=2i\gamma^{ade}`$, with an even permutation of the four contracted frame indices.

Therefore the literal source current formula converts to

```math
\mathcal H_G^a=h_G^a+Q_1^a-Q_2^a.
\tag{LB44}
```

But the generic covariant-slot matching gives $`\mathcal H_G=E`$, and the ordinary potential identification $`b_G=-E_3/2`$ gives $`h_G=P`$. The OPall current relation (LB31) then instead requires

```math
E^a=h_G^a-Q_1^a-Q_2^a.
\tag{LB45}
```

The difference **literal source minus required covariant current** is $`2Q_1^a`$. The two-gravitino completion agrees once (LB42) uses the correct tensor. Because (LB39) gives $`\delta P|_{\partial\epsilon}=\delta(Q_1+Q_2)|_{\partial\epsilon}`$, (LB45) has no principal parameter derivative, whereas (LB44) leaves exactly $`2\delta Q_1|_{\partial\epsilon}`$. The old claim of a $`2(Q_1+Q_2)`$ difference was caused by the local matrix-lowering error.

The full superfour-form pullback derives (LB45), and the closed superfive-form derives the ordinary-current BF coupling. These are **source-grounded derived repairs** of the incompatible printed formulas, not a claim that a published erratum exists. The unaltered source displays remain available. Generic BF invariance follows conditional on genuine vector and linear multiplets; verification of the particular expanded LOG polynomials remains a separate task.

### 9.4 Independent check and boundary of the result

The two scalar coefficient equations in (LB38) were checked exactly with rational arithmetic. The project Clifford representation already checks (LB33) and the fixed-upper rank-three transpose/odd-spinor flip. The corrected kernel (LB42) is checked for all ten independent two-form generators by [verify_log_form_interface.py](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_form_interface.py), using exact Gaussian-rational matrices and the actual index-lowering rule.

The principal test cancels every displayed $`\partial\epsilon`$ structure for a generic independent linear multiplet. Its scope remains limited. The separate full superform derivation supplies the complete potential law and generic BF invariance through a closed five-form, and therefore closes FORM-01 at that interface. It does not replace the independent curved constraint, reality or gauged-map checks of the calculated LOG multiplet.
