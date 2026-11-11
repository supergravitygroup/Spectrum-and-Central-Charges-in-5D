# Working conventions, transformations and curvature reference

**Lock:** `UNG-WEYL2-OP58-CONVENTIONS-v5` · **2026-09-18**  
**Purpose:** conventions and Q/S transformation rules for the component
calculation of Özkan–Pang (5.8). The canonical singlet coefficients fix the
candidate N and E slots through M13–M14. Independent descendant laws and full
multiplet matching are outside this reference's calculation scope. The four explicit components are consolidated in
[the full fermionic map](../../../../computations/weyl_fermionic/inputs/reference/notes/04_full_fermionic_weyl_linear_map.md),
reference `UNG-WEYL2-FERMIONIC-MAP-v1`; master M01/M08/M13/M14 remain
the derivation anchors.

This is an extracted reference with explicitly identified source-derived
repairs. It is not a proof of the nonlinear composite map or invariant.
The reference covers the Weyl, defining-vector and linear-multiplet ingredients
for the selected procedure. The two-derivative action, gauge-fixed compensating transformations and
spectrum are specified in their respective action and spectrum chapters.

## 0. Provenance and navigation

**OP** = Özkan–Pang, *Supersymmetric Completion of Gauss–Bonnet Combination in
Five Dimensions*, corrected arXiv:1301.6622v4 ([source](../../../../references/bibliography.md)). Printed page = PDF page.

**W** = Bergshoeff et al., *Weyl multiplets of N=2 conformal supergravity in
five dimensions*, arXiv:hep-th/0104113v4 ([source](../../../../references/bibliography.md)). Printed page + 1 = PDF
page.

**OPall** = Özkan–Pang, *All Off-Shell R² Invariants in Five Dimensional
N=2 Supergravity*, arXiv:1306.1540v3 ([source](../../../../references/bibliography.md)). Only (3.1)–(3.2),
PDF/printed p.8, is added here to specify the vector–linear density directly
in terms of E_a; the selected Weyl map remains OP(5.8).

The table below gives the literature equation and page for each relation.
Stable relation IDs connect the component derivations to these definitions.

| IDs | Content | Source anchor |
|---|---|---|
| C01–C07 | Indices, reality, signs, Clifford/Fierz, weights | OP App. A–B, pp.28–29; W App.A, printed31–33/PDF32–34; W Table3 |
| G01–G04 | Covariantization, geometry, constraints, frame variations | OP(2.5)–(2.7),(2.10),(5.2)–(5.4); W(3.6),(3.9)–(3.12),(3.17) |
| W01–W04 | Weyl transformations and derivatives | OP(2.1),(2.2),(2.11),(2.12); W(3.16),(3.17) |
| R01–R07 | Curvatures, connections and curvature variations | OP(2.5)–(2.7); W(3.19)–(3.23), printed20–21/PDF21–22 |
| H01–H03 | Form strengths, transformations, Bianchi identities | OP(2.3),(2.4),(2.8); W(3.26)–(3.28) |
| D01–D02 | Full ungauged Dilaton-Weyl composites | OP(2.9),(2.10), p.7 |
| L01–L04 | Linear multiplet, derivatives, constrained form | OP(2.18)–(2.24), pp.9–10 |
| V01–V03 | Abelian vector and defining-vector map | OP(2.13)–(2.16), p.8; (5.16),(5.17), p.20 |
| A01–A02 | Vector–linear density and direct E_a bridge | OP(3.1), p.10; OPall(3.1)–(3.2), p.8 |
| M01–M09 | Printed map, scalar S/Q results, adopted spinor and its full termwise Q-variation | OP(5.8),(5.9), pp.18–19; notebook S01–S46/Q01–Q64/P01–P80 |
| M10–M14 | Full singlet extraction, Clifford collection, bivector cancellation and canonical scalar/vector coefficients | Notebook Parts IV–VIII; derived from v5/M08 |
| X01–X12 | Literal-source discrepancies and operational choices | Explicit audit at end of this file |

## 1. Indices, spinors and normalizations

### C01 — Geometry and orientation

```math
D=5,\qquad \eta_{ab}=\mathrm{diag}(-,+,+,+,+),\qquad
\mu,\nu,a,b=0,\ldots,4,\quad i,j=1,2.
```

$`g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}`$, $`e=\det(e_\mu{}^a)>0`$
in the chosen oriented chart. $`e_a{}^\mu`$ is the inverse vielbein.
Brackets have unit strength: $`X_{[ab]}=(X_{ab}-X_{ba})/2`$, and similarly
symmetrization; bars inside brackets exclude those indices.

Choose the orientation $`\epsilon^{01234}=+1`$, hence
$`\epsilon_{01234}=-1`$. Here $`\epsilon`$ denotes the **tensor**, with
$`\epsilon^{\mu\nu\rho\sigma\lambda}=e^{-1}[\mu\nu\rho\sigma\lambda]`$
and $`[01234]=+1`$; the square-bracket symbol is a density. Frame conversion
is by one vielbein for each index, with no additional determinant.
This removes the tensor/density ambiguity in the typography of W(A.12).

```math
\epsilon_{a_1\ldots a_n b_1\ldots b_p}
\epsilon^{a_1\ldots a_n c_1\ldots c_p}
=-n!p!\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p},\quad n+p=5.
\tag{C01}
```

### C02 — SU(2) and names

```math
X^i=\varepsilon^{ij}X_j,\quad X_i=X^j\varepsilon_{ji},\quad
\varepsilon_{12}=\varepsilon^{12}=1,\quad
\varepsilon^{ik}\varepsilon_{jk}=\delta^i_j.
\tag{C02}
```

For a matrix, $`V^i{}_j=V^{ik}\varepsilon_{kj}`$; a spinor lowered as
$`\zeta_j=\zeta^k\varepsilon_{kj}`$ consequently obeys
$`-V^{ij}\zeta_j=+V^i{}_k\zeta^k`$. This explains the apparent sign difference
between the doublet derivative and the triplet derivative in L02.
Two lowered indices are lowered separately by this rule, never by a guessed
matrix multiplication. $`V^{ij}=V^{ji}`$, and its mixed matrix is anti-Hermitian.

$`\psi_\mu^i`$ is the gravitino; $`\psi^i`$ is the DW dilatino; $`\phi_\mu^i`$
is the dependent S connection; $`\varphi^i`$ is a linear-multiplet spinor.
Use $`(L_W^{ij},\varphi_W^i,E_{Wa},N_W)`$ for the **Weyl composite** after
substitution, and $`(L_c^{ij},\varphi_c^i,E_{ca},N_c)`$ for the independent
linear compensator. Source formulas use untagged $`L,\varphi,E,N`$.
$`C_\mu`$ is the graviphoton and $`C_{abcd}`$ the Weyl tensor; $`D`$ is a scalar
field, $`D_\mu^{(0)}`$ a bosonic covariant derivative, and $`\mathcal D_\mu`$
a full superconformal derivative.

### C03 — Majorana bar and Grassmann rules

```math
\bar\zeta^{\,i}=(\zeta^i)^T\mathsf C,\qquad
\mathsf C^T=-\mathsf C,\quad
(\mathsf C\gamma_a)^T=-\mathsf C\gamma_a,\quad
\mathsf C^\dagger\mathsf C=1.
\tag{C03a}
```

$`\gamma_0`$ is anti-Hermitian and the spatial gamma matrices are Hermitian.
Use W(A.5) symplectic Majorana reality, with the permitted choice
$`\alpha=1`$ and complex conjugation **not reversing the order of odd factors**:

```math
(\zeta^i)^C=B^{-1}\varepsilon^{ij}(\zeta^j)^*,\quad
B=\mathsf C\gamma_0,\quad (\zeta^i)^C=\zeta^i.
\tag{C03b}
```

The bar is linear in scalar coefficients: $`\overline{i\zeta}=i\bar\zeta`$.
It is not a Hermitian/Dirac conjugate. Physical spinors and $`\epsilon,\eta`$
are odd; the transformations $`\delta_Q(\epsilon),\delta_S(\eta)`$ are even,
so their Leibniz rule introduces no additional graded minus sign.
An explicitly odd operator $`Q`$ would have a graded Leibniz rule.

Suppressed SU(2) indices mean $`\bar\psi\Gamma\chi=\bar\psi^i\Gamma\chi_i`$.
For the OP(A.4) index pattern,

```math
\bar\psi^i\gamma_{(n)}\chi^j=t_n\bar\chi^j\gamma_{(n)}\psi^i,
\qquad (t_0,t_1,t_2,t_3)=(1,1,-1,-1).
\tag{C03c}
```

After **contracting** the doublet indices, the flip has an extra minus:
$`\bar\psi\gamma_{(n)}\chi=-t_n\bar\chi\gamma_{(n)}\psi`$.
Never apply the fixed-index flip unchanged to a contracted bilinear.

### C04 — Clifford algebra and full contractions

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\quad
\gamma^{a_1\ldots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]},\quad
\gamma^{abcde}=i\epsilon^{abcde},\quad \gamma^\mu=e_a{}^\mu\gamma^a.
\tag{C04a}
```

```math
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},\quad
T\!\cdot\!\widehat R(Q)=T^{ab}\widehat R_{ab}(Q),\quad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a.
\tag{C04b}
```

Dots are **full ordered-index contractions, without $`1/n!`$**.
W(A.14) prints $`(A^{a_1\ldots a_n}B_{a_1\ldots a_n})/n!=(A\cdot B)/n!`$;
its first factorial must not be misread as a definition of the dot itself.
$`\gamma^{ab}\gamma^c`$ is a product, not $`\gamma^{abc}`$.
$`\gamma_{ab}{}^{cd}`$ in R05 is a single fully antisymmetric rank-four gamma.

```math
\gamma^a\gamma^{b_1\ldots b_n}
=\gamma^{ab_1\ldots b_n}
+n\eta^{a[b_1}\gamma^{b_2\ldots b_n]},\qquad
\gamma_{a_1\ldots a_n}=
\frac{i}{(5-n)!}\epsilon_{a_1\ldots a_n b_1\ldots b_{5-n}}
\gamma^{b_{5-n}\ldots b_1}.
\tag{C04c}
```

Useful full-index contractions from W Table7:

| rank n | $`\gamma^a\gamma_{(n)}\gamma_a`$ | $`\gamma^{ab}\gamma_{(n)}\gamma_{ab}`$ |
|---:|---|---|
| 0 | $`5\gamma_{(0)}`$ | $`-20\gamma_{(0)}`$ |
| 1 | $`-3\gamma_{(1)}`$ | $`-4\gamma_{(1)}`$ |
| 2 | $`\gamma_{(2)}`$ | $`4\gamma_{(2)}`$ |
| 3 | $`\gamma_{(3)}`$ | $`4\gamma_{(3)}`$ |

### C05 — Fierz and doublet identities

OP(A.5), W(A.10)–(A.11), for odd spinors:

```math
\psi_j\bar\lambda^i=-\frac14(\bar\lambda^i\psi_j)\mathbf1
-\frac14(\bar\lambda^i\gamma^a\psi_j)\gamma_a
+\frac18(\bar\lambda^i\gamma^{ab}\psi_j)\gamma_{ab},\qquad
\bar\psi^{[i}\lambda^{j]}=-\frac12\bar\psi\lambda\,\varepsilon^{ij}.
\tag{C05a}
```

```math
\xi_j\bar\xi^j\xi^i
=\gamma^a\xi_j\bar\xi^j\gamma_a\xi^i
=\frac18\gamma^{ab}\xi^i\bar\xi\gamma_{ab}\xi.
\tag{C05b}
```

The other independent triple-spinor structures can be represented by
$`\xi^{(k}\bar\xi^i\xi^{j)}`$ and $`\xi_j\bar\xi^j\gamma_a\xi^i`$.
Use C05 with explicit spinor order before collecting Q/S parameter structures.

### C06 — Weights, degree and units

| Field / tensor | Weyl weight |
|---|---:|
| $`e_\mu{}^a, e_a{}^\mu`$ | $`-1,+1`$ |
| $`\epsilon,\eta`$ | $`-1/2,+1/2`$ |
| $`\psi_\mu,\phi_\mu,f_\mu{}^a`$ | $`-1/2,+1/2,1`$ |
| $`b_\mu,\omega_\mu{}^{ab},V_\mu{}^{ij},C_\mu,B_{\mu\nu},A_\mu`$ | 0 |
| $`\sigma,\rho,T_{ab}`$ | 1 |
| $`\psi,\lambda,\chi,\widehat R_{ab}(Q)`$ | $`3/2`$ |
| $`D,Y^{ij},\widehat G_{ab},\widehat R_{ab}(V),\widehat C_{abcd}`$ | 2 |
| $`\widehat R_{ab}(S)`$ | $`5/2`$ |
| $`\widehat H_{abc},L^{ij}`$ | 3 |
| $`\varphi`$ | $`7/2`$ |
| $`E_a,N`$ | 4 |

$`\mathcal D_a`$ raises weight by one; $`\mathcal D_\mu`$ preserves weight.
Weights are not canonically normalized Poincare mass dimensions.
Use $`\hbar=c=1`$. Fermion degree counts physical independent fermions inside
connections, hats and composites as well as explicitly written factors.

### C07 — Scope and action convention

Physical gauging is $`g=0`$ exactly. The conformal SU(2) connection and its
quadratic $`VV`$ terms remain. No Poincare gauge or auxiliary equation is used
in the map derivation. Later the selected action is
$`S=S_{\rm 2der}+\lambda_{\rm Weyl}S_{\rm Weyl^2}`$ with
$`[\lambda_{\rm Weyl}]=-2`$ after the Poincare scale is fixed.
The parent bosonic normalization is specified in [the current action](../../../../weyl2/action/README.md); conversion
of the whole OP density, including boundary representatives, is outside this map calculation.
The curvature-only diagnostic gives the candidate factor $`-2`$ between the OP
$`C^2/8+R^2/48`$ density and the target $`-C^2/4-R^2/24`$. Do not promote this
single-sector diagnostic to a full action conversion.

## 2. Geometry and the meaning of a derivative

### G01 — Full covariantization

W(3.17) fixes the algorithm, including derivatives of composites:

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad
\mathcal D_a=e_a{}^\mu\mathcal D_\mu.
\tag{G01}
```

The bosonic derivative on a doublet of weight $`w`$ is
$`D_\mu^{(0)}\zeta^i=(\partial_\mu-wb_\mu+\omega_\mu{}^{ab}\gamma_{ab}/4) \zeta^i-V_\mu{}^{ij}\zeta_j`$. On a covector it has
$`+\omega_{\mu a}{}^b X_b`$, and on $`T_{ab}`$ it has
$`+2\omega_\mu{}^c{}_{[a}T_{b]c}`$ (source index/sign repair X09). Covariantization is a derivation on tensor
products. It acts on gamma matrices compatibly with their Lorentz indices.

The elementary matter fields are K invariant. Their **covariant derivatives
need not be K invariant**. Apply G01 to the actual transformation of the
first derivative to form a second derivative; its S/K terms cannot be
omitted. This is why $`\Box^c\sigma`$ contains $`f_a{}^a`$ in D02.
Likewise $`\mathcal D\psi`$ need not vanish in the later gauge $`\psi=0`$.

For variations of a derivative, use the exact chain rule
$`\delta(\mathcal D_a\Phi)=(\delta e_a{}^\mu)\mathcal D_\mu\Phi+ e_a{}^\mu\delta(\mathcal D_\mu\Phi)`$, varying every connection, coefficient
and matter field in G01 or its displayed expansion. Do not set
$`\delta(\mathcal D\Phi)=\mathcal D\delta\Phi`$.

### G02 — Lorentz and metric curvature

Define the ordinary connection curvature by

```math
R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,
\quad R_{\mu\nu\rho\sigma}=R_{\mu\nu}{}^{ab}(\omega)e_{\rho a}e_{\sigma b}.
\tag{G02a}
```

When $`b=\psi_\mu=0`$, $`\omega`$ is Levi-Civita and
$`[\nabla_\mu,\nabla_\nu]X^\rho=R^\rho{}_{\sigma\mu\nu}X^\sigma`$,
$`[\nabla_\mu,\nabla_\nu]\zeta=R_{\mu\nu}{}^{ab}\gamma_{ab}\zeta/4`$,
with $`R^\rho{}_{\sigma\mu\nu}=e_a{}^\rho R_{\mu\nu}{}^{ab}e_{\sigma b}`$.

The OP Ricci contraction is
$`R_{\mu\nu}=R_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a}`$.
For a torsion-free curvature this also equals $`g^{\rho\sigma}R_{\rho\mu\sigma\nu}`$.
A constant-curvature tensor $`R_{\mu\nu\rho\sigma} =k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})`$
has $`R_{\mu\nu}=4kg_{\mu\nu}`$ and $`R=20k`$.
For the bosonic curvature,

```math
\begin{aligned}
C_{\mu\nu\rho\sigma}={}&R_{\mu\nu\rho\sigma}
-\frac13(g_{\mu\rho}R_{\nu\sigma}-g_{\nu\rho}R_{\mu\sigma}
-g_{\mu\sigma}R_{\nu\rho}+g_{\nu\sigma}R_{\mu\rho})\\
&+\frac1{12}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})R,
\qquad C^2=R_{\mu\nu\rho\sigma}^2-\frac43R_{\mu\nu}^2+\frac16R^2.
\end{aligned}\tag{G02b}
```

These bosonic Riemann symmetries must not be assumed for an arbitrary
unconstrained hatted curvature. The full $`\widehat C`$ is R03 below.

### G03 — Conventional constraints and supercovariantization

```math
R_{\mu\nu}{}^a(P)=2\partial_{[\mu}e_{\nu]}{}^a
+2\omega_{[\mu}{}^{ab}e_{\nu]b}+2b_{[\mu}e_{\nu]}{}^a
-\frac12\bar\psi_{[\mu}\gamma^a\psi_{\nu]}=0,
\quad \gamma^\mu\widehat R_{\mu\nu}(Q)=0,
\quad e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0.
\tag{G03a}
```

These solve for $`\omega,\phi,f`$, respectively; they are not field equations.
W(3.12) implies $`\mathcal R_{\mu\nu}=\mathcal R_{\nu\mu}`$,
$`\widehat R(D)=0`$ and the corresponding cyclic Lorentz-curvature identity.
The gamma-trace condition also implies
$`\gamma_{[\mu\nu}\widehat R_{\rho\sigma]}(Q)=0`$ [W footnote5].

For a connection $`h_\mu{}^I`$ whose transformation is
$`\delta h_\mu{}^I=\partial_\mu\epsilon^I+ \epsilon^J h_\mu{}^A f_{AJ}{}^I+\epsilon^J M_{\mu J}{}^I`$,

```math
\widehat R_{\mu\nu}{}^I=2\partial_{[\mu}h_{\nu]}{}^I
+h_\nu{}^B h_\mu{}^A f_{AB}{}^I
-2h_{[\mu}{}^J M_{\nu]J}{}^I.
\tag{G03b}
```

The structure functions include matter-dependent terms. This W(3.6) rule,
not blind replacement by hats, fixes the connection completions and X01.

### G04 — Frames, gamma matrices and scalar density variations

```math
\delta e_a{}^\mu=-e_a{}^\nu\delta e_\nu{}^b e_b{}^\mu,
\quad \delta e=e\,e_a{}^\mu\delta e_\mu{}^a,
\quad \delta\gamma_\mu=\delta e_\mu{}^a\gamma_a,
\quad \delta\gamma^a=0.
\tag{G04a}
```

For example,

```math
\delta X_{ab}=e_a{}^\mu e_b{}^\nu\delta X_{\mu\nu}
+(\delta e_a{}^\mu)e_b{}^\nu X_{\mu\nu}
+e_a{}^\mu(\delta e_b{}^\nu)X_{\mu\nu}.
\tag{G04b}
```

Tangent curvature variations R05–R06/H02 already include frame variation;
do not add it a second time. Conversely, converting those laws to world
indices requires the two or three $`\delta e_\mu{}^a`$ terms.
$`\delta\epsilon_{abcde}=0`$, whereas world epsilon tensors vary with $`e`$.

## 3. Weyl transformations and component derivatives

### W01 — Common Weyl gauge fields; OP(2.1), W(4.1)

```math
\begin{aligned}
\delta e_\mu{}^a&=\tfrac12\bar\epsilon\gamma^a\psi_\mu,\\
\delta\psi_\mu^i&=(\partial_\mu+\tfrac12b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\epsilon^i
-V_\mu{}^{ij}\epsilon_j+i\gamma\!\cdot\!T\gamma_\mu\epsilon^i-i\gamma_\mu\eta^i,\\
\delta V_\mu{}^{ij}&=-\tfrac32i\bar\epsilon^{(i}\phi_\mu^{j)}
+4\bar\epsilon^{(i}\gamma_\mu\chi^{j)}
+i\bar\epsilon^{(i}\gamma\!\cdot\!T\psi_\mu^{j)}
+\tfrac32i\bar\eta^{(i}\psi_\mu^{j)},\\
\delta b_\mu&=\tfrac12i\bar\epsilon\phi_\mu-2\bar\epsilon\gamma_\mu\chi
+\tfrac12i\bar\eta\psi_\mu+2\Lambda_{K\mu}.
\end{aligned}\tag{W01}
```

Unless explicitly stated, displayed transformations include Q and S; the K
term is shown wherever nonzero. Ordinary Lorentz, SU(2), diffeomorphism and
weight transformations follow the displayed index/connection conventions.

### W02 — DW fields; OP(2.1)

```math
\begin{aligned}
\delta C_\mu&=-\tfrac i2\sigma\bar\epsilon\psi_\mu+\tfrac12\bar\epsilon\gamma_\mu\psi,\\
\delta B_{\mu\nu}&=\tfrac12\sigma^2\bar\epsilon\gamma_{[\mu}\psi_{\nu]}
+\tfrac i2\sigma\bar\epsilon\gamma_{\mu\nu}\psi+C_{[\mu}\delta_Q C_{\nu]},\\
\delta\psi^i&=-\tfrac14\gamma\!\cdot\!\widehat G\epsilon^i
-\tfrac i2\mathord{\not{\mathcal D}}\sigma\epsilon^i
+\sigma\gamma\!\cdot\!T\epsilon^i
-\tfrac i4\sigma^{-1}\epsilon_j\bar\psi^i\psi^j+\sigma\eta^i,\\
\delta\sigma&=\tfrac i2\bar\epsilon\psi.
\end{aligned}\tag{W02}
```

### W03 — Standard-Weyl matter; OP(2.11), W(3.16)

```math
\begin{aligned}
\delta T_{ab}&=\tfrac i2\bar\epsilon\gamma_{ab}\chi
-\tfrac{3i}{32}\bar\epsilon\widehat R_{ab}(Q),\\
\delta\chi^i&=\tfrac14\epsilon^iD-\tfrac1{64}\gamma\!\cdot\!\widehat R^{ij}(V)\epsilon_j
+\tfrac i8\gamma^{ab}\mathord{\not{\mathcal D}}T_{ab}\epsilon^i
-\tfrac i8\gamma^a\mathcal D^bT_{ab}\epsilon^i\\
&\quad-\tfrac14\gamma^{abcd}T_{ab}T_{cd}\epsilon^i+\tfrac16T^2\epsilon^i
+\tfrac14\gamma\!\cdot\!T\eta^i,\\
\delta D&=\bar\epsilon\mathord{\not{\mathcal D}}\chi
-\tfrac{5i}{3}\bar\epsilon\gamma\!\cdot\!T\chi-i\bar\eta\chi,
\qquad T^2=T_{ab}T^{ab}.
\end{aligned}\tag{W03}
```

$`T,\chi,D`$ may be treated as Standard-Weyl covariants in the first map
calculation; in the final DW theory they are D01 composites, not new fields.

### W04 — Explicit derivatives; OP(2.2),(2.12), with X02/X09

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\tfrac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=D_\mu^{(0)}\psi^i
+\tfrac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\tfrac i2\mathord{\not{\mathcal D}}\sigma\psi_\mu^i
+\tfrac i4\sigma^{-1}\psi_{\mu j}\bar\psi^i\psi^j
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i,\\
\mathcal D_\mu T_{ab}&=\partial_\mu T_{ab}-b_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}-\tfrac i2\bar\psi_\mu\gamma_{ab}\chi
+\tfrac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q),\\
\mathcal D_\mu\chi^i&=(\partial_\mu-\tfrac32b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\chi^i
-V_\mu{}^{ij}\chi_j-\tfrac14\psi_\mu^iD
+\tfrac1{64}\gamma\!\cdot\!\widehat R^{ij}(V)\psi_{\mu j}\\
&\quad-\tfrac i8\gamma^{ab}\mathord{\not{\mathcal D}}T_{ab}\psi_\mu^i
+\tfrac i8\gamma^a\mathcal D^bT_{ab}\psi_\mu^i
+\tfrac14\gamma^{abcd}T_{ab}T_{cd}\psi_\mu^i
-\tfrac16T^2\psi_\mu^i-\tfrac14\gamma\!\cdot\!T\phi_\mu^i,\\
\mathcal D_\mu D&=(\partial_\mu-2b_\mu)D
-\bar\psi_\mu\mathord{\not{\mathcal D}}\chi
+\tfrac{5i}{3}\bar\psi_\mu\gamma\!\cdot\!T\chi+i\bar\phi_\mu\chi.
\end{aligned}\tag{W04}
```

The last line is explicitly generated from W03/G01, not separately printed
in OP. The $`\chi`$ weight is $`3/2`$; OP's printed $`7/2`$ is audited in X02.
In the first DW-spinor derivative $`D_\mu^{(0)}`$ uses $`w=3/2`$.

## 4. Connections, curvatures and their variations

### R01 — Spin connection and gravitino curvature; OP(2.5),(2.6)

```math
\begin{aligned}
\omega_\mu{}^{ab}={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+2e_\mu{}^{[a}b^{b]}+\tfrac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\tfrac14\bar\psi^a\gamma_\mu\psi^b,\\
\widehat R'_{\mu\nu}{}^i(Q)={}&2\partial_{[\mu}\psi_{\nu]}^i
+\tfrac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i+b_{[\mu}\psi_{\nu]}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i={}&\tfrac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\tfrac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)={}&\widehat R'_{\mu\nu}{}^i(Q)-2i\gamma_{[\mu}\phi_{\nu]}^i.
\end{aligned}\tag{R01}
```

A prime does not denote a new convention: it specifically removes the
$`\phi`$ term here, and the $`f`$ term in R03 below.

### R02 — R-symmetry curvature; OP(2.7)

```math
\begin{aligned}
V_{\mu\nu}{}^{ij}&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}{}^{ij}(V)&=V_{\mu\nu}{}^{ij}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{R02}
```

### R03 — Working Lorentz curvature and K connection; X01 is mandatory

The following is reconstructed from W(3.4),(3.6),(3.20), with the source
errors of OP(2.7) isolated in X01. It is **not a literal quotation** of OP:

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)={}&R_{\mu\nu}{}^{ab}(\omega)
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\tfrac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\mathcal R_{\mu\nu}&=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad \mathcal R=\mathcal R_\mu{}^\mu,\\
f_\mu{}^a&=-\tfrac16\mathcal R_\mu{}^a+\tfrac1{48}e_\mu{}^a\mathcal R,\\
\widehat R_{\mu\nu}{}^{ab}(M)&=\widehat R'_{\mu\nu}{}^{ab}(M)
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\qquad
\widehat C_{abcd}=e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu cd}(M).
\end{aligned}\tag{R03}
```

W(3.11) instead calls
$`\mathcal R^W_{\mu\nu}=\widehat R'_{\mu\rho}{}^{ab}(M)e_a{}^\rho e_{\nu b}`$.
Thus $`\mathcal R^W_{\mu\nu}=-\mathcal R_{\mu\nu}`$ and W's
$`f_\mu{}^a=\mathcal R^W_\mu{}^a/6-e_\mu{}^a\mathcal R^W/48`$
is exactly the same connection. There is no additional Riemann-sign change.

### R04 — Dependent connection variations; W(3.2),(3.20),(3.21)

```math
\begin{aligned}
\delta\omega_\mu{}^{ab}={}&\tfrac i2\bar\epsilon\gamma^{ab}\phi_\mu
-\tfrac i2\bar\eta\gamma^{ab}\psi_\mu
-i\bar\epsilon\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_\mu\\
&-\tfrac12\bar\epsilon\gamma^{[a}\widehat R_\mu{}^{b]}(Q)
-\tfrac14\bar\epsilon\gamma_\mu\widehat R^{ab}(Q)
-4e_\mu{}^{[a}\bar\epsilon\gamma^{b]}\chi
-4\Lambda_K^{[a}e_\mu{}^{b]}.
\end{aligned}\tag{R04a}
```

The all-order S-connection variation is fixed by R01, not by filling the
ellipsis in W(3.21) with the bare algebra alone:

```math
\delta\phi_\mu^i=\frac i3\gamma^a\delta\widehat R'_{\mu a}{}^i(Q)
-\frac i{24}(\delta\gamma_\mu)\gamma^{ab}\widehat R'_{ab}{}^i(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}\delta\widehat R'_{ab}{}^i(Q).
\tag{R04b}
```

Use the explicit R01 polynomial and G04 frame variations for each primed
curvature here, with W01/W03 and the displayed full $`\delta\omega`$.
This defines a finite exact variation: $`\widehat R'(Q)`$ contains no $`\phi`$;
$`\delta\omega`$ contains $`\phi`$ but not $`\delta\phi`$.

For reference, the **M-dependent additions only** printed in W(3.21) are

```math
\begin{aligned}
(\delta\phi_\mu^i)_M={}&
-\tfrac i{12}(\gamma^{ab}\gamma_\mu-\tfrac12\gamma_\mu\gamma^{ab})
\widehat R_{ab}{}^i{}_j(V)\epsilon^j\\
&+\tfrac13[\mathord{\not{\mathcal D}}(\gamma\!\cdot\!T)\gamma_\mu
-\mathcal D_\mu(\gamma\!\cdot\!T)
+\gamma_\mu\gamma^c\mathcal D^aT_{ac}]\epsilon^i\\
&+i[-\gamma_{\mu abcd}T^{ab}T^{cd}
+8\gamma_\rho T^{\rho\sigma}T_{\mu\sigma}-2\gamma_\mu T^2]\epsilon^i
+\tfrac i3(8\gamma^bT_{\mu b}-\gamma_\mu\gamma\!\cdot\!T)\eta^i.
\end{aligned}\tag{R04c}
```

In addition to the bare $`D_\mu^{(0)}\eta+if_\mu{}^a\gamma_a\epsilon -i\Lambda_K^a\gamma_a\psi_\mu`$, the soft algebra can contribute terms
through its field-dependent structure functions. Thus R04c plus the bare
terms is **not** our definition of the full variation; R04b is.

W does not print the full $`\delta f`$. Use its **exact defining variation**:

```math
\begin{aligned}
\delta f_\mu{}^a&=-\tfrac16\delta(\mathcal R_{\mu\nu}e^{\nu a})
+\tfrac1{48}\delta(e_\mu{}^a g^{\rho\sigma}\mathcal R_{\rho\sigma}),\\
\delta\mathcal R_{\mu\nu}&=
(\delta\widehat R'_{\mu\rho}{}^{ab})e_b{}^\rho e_{\nu a}
+\widehat R'_{\mu\rho}{}^{ab}\delta(e_b{}^\rho e_{\nu a}).
\end{aligned}\tag{R04d}
```

R03 and G04 specify every factor in this differentiation; there is no
undefined new curvature variation. W(3.22), $`-5i\bar\eta\chi`$, is only the
**M-dependent correction** to $`\delta_S f_a{}^a`$, not its entire variation.

### R05 — Tangent gravitino-curvature variation; W(3.23)

```math
\begin{aligned}
\delta\widehat R_{ab}{}^i(Q)={}&
\tfrac16(\gamma_{ab}{}^{cd}-\gamma^{cd}\gamma_{ab}
-\tfrac12\gamma_{ab}\gamma^{cd})\widehat R_{cd}{}^i{}_j(V)\epsilon^j
+\tfrac14\widehat R_{ab}{}^{cd}(M)\gamma_{cd}\epsilon^i\\
&+2i[\mathcal D_{[a}(\gamma\!\cdot\!T)\gamma_{b]}
-\tfrac13\gamma_{[b}\mathcal D_{a]}(\gamma\!\cdot\!T)
-\tfrac13\gamma_{[a}\mathord{\not{\mathcal D}}(\gamma\!\cdot\!T)\gamma_{b]}
-\tfrac13\gamma_{ab}\gamma_d\mathcal D_c T^{cd}]\epsilon^i\\
&-8T_{ab}\eta^i+\tfrac{16}{3}T_{[a}{}^c\gamma_{b]c}\eta^i
+\tfrac43\gamma_{abcd}T^{cd}\eta^i.
\end{aligned}\tag{R05}
```

In the second derivative term the unambiguous meaning is
$`-\frac13[(\mathcal D_aT_{cd})\gamma_b\gamma^{cd} -(\mathcal D_bT_{cd})\gamma_a\gamma^{cd}]/2`$.
This spells out the source's $`-\mathcal D_{[a}\gamma_{b]}\gamma\cdot T/3`$;
it must not be set to zero by differentiating only $`\gamma_b`$.

### R06 — Tangent SU(2)-curvature variation and eliminated S curvature

```math
\begin{aligned}
\delta\widehat R_{ab}{}^{ij}(V)={}&
-\tfrac{3i}{2}\bar\epsilon^{(i}\widehat R_{ab}{}^{j)}(S)
-8\bar\epsilon^{(i}\gamma_{[a}\mathcal D_{b]}\chi^{j)}
+i\bar\epsilon^{(i}\gamma\!\cdot\!T\widehat R_{ab}{}^{j)}(Q)\\
&+8i\bar\epsilon^{(i}\gamma_{[a}\gamma\!\cdot\!T\gamma_{b]}\chi^{j)}
+\tfrac{3i}{2}\bar\eta^{(i}\widehat R_{ab}{}^{j)}(Q)
+8i\bar\eta^{(i}\gamma_{ab}\chi^{j)}.
\end{aligned}\tag{R06a}
```

W(3.19), with spinor index suppressed and full contractions C04:

```math
\begin{aligned}
\gamma\!\cdot\!\widehat R(S)&=-\tfrac83 T\!\cdot\!\widehat R(Q),\\
\gamma^\mu\widehat R_{\mu\nu}(S)&=-\tfrac i2\mathcal D^\mu\widehat R_{\mu\nu}(Q)
+\tfrac43\gamma_\nu T\!\cdot\!\widehat R(Q)
+2\gamma_bT^{b\mu}\widehat R_{\mu\nu}(Q),\\
\widehat R_{\mu\nu}(S)&=-i\mathord{\not{\mathcal D}}\widehat R_{\mu\nu}(Q)
-i\gamma_{[\mu}\mathcal D^\rho\widehat R_{\nu]\rho}(Q)
-\tfrac83\gamma_{\mu\nu}T\!\cdot\!\widehat R(Q)\\
&\quad+12\gamma_bT^{\rho b}\gamma_{[\mu}\widehat R_{\nu]\rho}(Q)
-3\gamma\!\cdot\!T\widehat R_{\mu\nu}(Q)
-8T^\rho{}_{[\mu}\widehat R_{\nu]\rho}(Q).
\end{aligned}\tag{R06b}
```

To avoid ambiguity in derivatives of curvatures: construct
$`\mathcal D_\mu\widehat R_{ab}(Q)`$ from G01 using weight $`3/2`$, the two
Lorentz covector connections, the doublet connection, and **minus R05 with
$`(\epsilon,\eta)=(\psi_\mu,\phi_\mu)`$**. Construct
$`\mathcal D_\mu\widehat R_{ab}^{ij}(V)`$ the same way from R06a with weight2
and its triplet connection. These are explicit replacement rules, not
ordinary bosonic derivatives. Both curvatures are K invariant.

### R07 — Exact Lorentz/Weyl-curvature variation recipe

A shortened independent formula for $`\delta\widehat C`$ is not printed in
these passages. Define $`\mathcal B_{\mu\nu}{}^{ab}`$ to be the five fermionic
terms in R03, so $`\widehat R'=R(\omega)+\mathcal B`$. Then

```math
\begin{aligned}
\delta\widehat R'_{\mu\nu}{}^{ab}
&=2D_{[\mu}^{(\omega)}\delta\omega_{\nu]}{}^{ab}
+\delta\mathcal B_{\mu\nu}{}^{ab},\\
\delta\widehat R_{\mu\nu}{}^{ab}(M)
&=\delta\widehat R'_{\mu\nu}{}^{ab}
+8\delta f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+8f_{[\mu}{}^{[a}\delta e_{\nu]}{}^{b]},\\
\delta\widehat C_{abcd}
&=\delta\big(e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu cd}(M)\big).
\end{aligned}\tag{R07}
```

The product operator in the first line is defined termwise:
$`\delta(\bar A\Gamma B)=(\delta A)^T\mathsf C\Gamma B+ \bar A(\delta\Gamma)B+\bar A\Gamma\delta B`$; factors $`T,e`$ also vary.
Substitute R04a–R04b, W01/W03, R05 and G04. R04d uses **primed** curvature,
which contains no $`f`$, so this recipe is finite and not circular. It supplies
all terms even when more cumbersome than a Fierz-reduced closed expression.
This is a derived Leibniz rule, not a claimed new source formula.

## 5. Gauge forms and full ungauged DW composites

### H01 — Strengths and form gauges; OP(2.3),(2.4)

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}+\tfrac32 C_{[\mu}G_{\nu\rho]},\\
\widehat G_{\mu\nu}&=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\tfrac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=H_{\mu\nu\rho}
-\tfrac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\tfrac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
\delta_\Lambda C_\mu&=\partial_\mu\Lambda,\qquad
\delta_\Lambda B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}-\tfrac12\Lambda G_{\mu\nu}.
\end{aligned}\tag{H01}
```

With forms normalized $`B=B_{\mu\nu}dx^\mu\wedge dx^\nu/2`$,
$`G=dC`$, $`H=dB+C\wedge G/2`$, hence $`dG=0`$, $`dH=G\wedge G/2`$.

### H02 — Tangent strength variations

Use H02 in the [component dictionary](COMPONENT_CONVENTIONS.md).
It contains the final $`G\psi`$ sign and the gauged linear-compensator
contribution; the ungauged restriction sets $`g=0`$.

### H03 — Supercovariant Bianchi identities; W(3.28)

```math
\mathcal D_{[a}\widehat G_{bc]}=\tfrac12\bar\psi\gamma_{[a}\widehat R_{bc]}(Q),
\qquad
\mathcal D_{[a}\widehat H_{bcd]}=\tfrac34\widehat G_{[ab}\widehat G_{cd]}.
\tag{H03}
```

The spinor on the first right-hand side is the dilatino, not $`\psi_a`$.
The bosonic limit of the second identity agrees with $`dH=G\wedge G/2`$.

### D01 — Complete auxiliary composites; OP(2.9)

```math
\begin{aligned}
T_{ab}={}&\tfrac18\sigma^{-2}
\left(\sigma\widehat G_{ab}+\tfrac16\epsilon_{abcde}\widehat H^{cde}
+\tfrac i4\bar\psi\gamma_{ab}\psi\right),\\
\chi^i={}&\tfrac i8\sigma^{-1}\mathord{\not{\mathcal D}}\psi^i
+\tfrac i{16}\sigma^{-2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\tfrac1{32}\sigma^{-2}\gamma\!\cdot\!\widehat G\psi^i
+\tfrac14\sigma^{-1}\gamma\!\cdot\!T\psi^i
+\tfrac i{32}\sigma^{-3}\psi_j\bar\psi^i\psi^j,\\
D={}&\tfrac14\sigma^{-1}\Box^c\sigma
+\tfrac18\sigma^{-2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\tfrac1{16}\sigma^{-2}\widehat G_{ab}\widehat G^{ab}
-\tfrac18\sigma^{-2}\bar\psi\mathord{\not{\mathcal D}}\psi\\
&-\tfrac1{64}\sigma^{-4}\bar\psi^i\psi^j\bar\psi_i\psi_j
-4i\sigma^{-1}\bar\psi\chi
+\left(-\tfrac{26}{3}T_{ab}+2\sigma^{-1}\widehat G_{ab}
+\tfrac i4\sigma^{-2}\bar\psi\gamma_{ab}\psi\right)T^{ab}.
\end{aligned}\tag{D01}
```

This formulation needs a patch with $`\sigma\ne0`$.
W(3.14)'s $`-\epsilon_{abcde}\widehat H^{edc}/6`$ equals OP's
$`+\epsilon_{abcde}\widehat H^{cde}/6`$ by antisymmetry; no orientation
change is needed.

### D02 — Superconformal Laplacian; OP(2.10)

```math
\Box^c\sigma=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\tfrac i2\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi
+\tfrac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\tfrac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\tag{D02}
```

$`f`$ is R03, including its fermions; do not replace this by an ordinary
scalar Laplacian before the full substitution and chosen gauge.

## 6. Linear and defining-vector multiplets

### L01 — Matching laws; OP(2.18)

```math
\begin{aligned}
\delta L^{ij}&=i\bar\epsilon^{(i}\varphi^{j)},\\
\delta\varphi^i&=-\tfrac i2\mathord{\not{\mathcal D}}L^{ij}\epsilon_j
-\tfrac i2\gamma^aE_a\epsilon^i+\tfrac12N\epsilon^i
-\gamma\!\cdot\!T L^{ij}\epsilon_j+3L^{ij}\eta_j,\\
\delta E_a&=-\tfrac i2\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
-2\bar\epsilon\gamma^b\varphi T_{ba}-2\bar\eta\gamma_a\varphi,\\
\delta N&=\tfrac12\bar\epsilon\mathord{\not{\mathcal D}}\varphi
+\tfrac{3i}{2}\bar\epsilon\gamma\!\cdot\!T\varphi
+4i\bar\epsilon^i\chi^jL_{ij}+\tfrac{3i}{2}\bar\eta\varphi.
\end{aligned}\tag{L01}
```

### L02 — Full derivatives; OP(2.19), G01

```math
\begin{aligned}
\mathcal D_\mu L^{ij}&=(\partial_\mu-3b_\mu)L^{ij}
+2V_\mu{}^{(i}{}_kL^{j)k}-i\bar\psi_\mu^{(i}\varphi^{j)},\\
\mathcal D_\mu\varphi^i&=(\partial_\mu-\tfrac72b_\mu
+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\varphi^i-V_\mu{}^{ij}\varphi_j
+\tfrac i2\mathord{\not{\mathcal D}}L^{ij}\psi_{\mu j}
+\tfrac i2\gamma^aE_a\psi_\mu^i\\
&\quad-\tfrac12N\psi_\mu^i+\gamma\!\cdot\!T L^{ij}\psi_{\mu j}
-3L^{ij}\phi_{\mu j},\\
\mathcal D_\mu E_a&=(\partial_\mu-4b_\mu)E_a+\omega_{\mu ab}E^b
+\tfrac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
+2\bar\psi_\mu\gamma^b\varphi T_{ba}+2\bar\phi_\mu\gamma_a\varphi,\\
\mathcal D_\mu N&=(\partial_\mu-4b_\mu)N
-\tfrac12\bar\psi_\mu\mathord{\not{\mathcal D}}\varphi
-\tfrac{3i}{2}\bar\psi_\mu\gamma\!\cdot\!T\varphi
-4i\bar\psi_\mu^i\chi^jL_{ij}-\tfrac{3i}{2}\bar\phi_\mu\varphi.
\end{aligned}\tag{L02}
```

The N line is generated from L01/G01. In particular the constraint is
$`\mathcal D^aE_a=0`$, not $`\partial^aE_a=0`$.

### L03 — Constrained form; OP(2.20)–(2.23)

```math
\mathcal D^aE_a=0,\qquad
E^\mu=-\tfrac1{12}\epsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda},\qquad
\delta_\Lambda E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]}.
\tag{L03a}
```

OP also introduces the dual two-form representation

```math
E_{\mu\nu\rho}=\epsilon_{\mu\nu\rho\sigma\lambda}E^{\sigma\lambda},
\qquad E^\mu=\mathcal D_\nu E^{\mu\nu}.
\tag{L03b}
```

$`E^{\mu\nu}`$ here is the dual representation of the three-form potential,
not an extra independent Maxwell field. $`\mathcal D E_3`$ includes its
supercovariant completions; it is not just $`dE_3`$ when fermions are retained.

### L04 — Literal potential transformations; OP(2.24), NOT an operational pair

```math
\delta E^{\mu\nu}=-\tfrac i2\bar\epsilon\gamma^{\mu\nu}\varphi
-\tfrac12\bar\psi_\rho^i\gamma^{\mu\nu\rho}\epsilon^jL_{ij}
-\partial_\rho\widetilde\Lambda^{\mu\nu\rho},\qquad
\delta E_{\mu\nu\rho}=-\bar\epsilon\gamma_{\mu\nu\rho}\varphi
+i\bar\psi_{[\mu}^i\gamma_{\nu\rho]}\epsilon^jL_{ij}.
\tag{L04}
```

These are literal extractions, **quarantined by X10**: they cannot both
hold with C01/C04/L03. Do not use them as working transformations. The
selected calculation uses the operational $`E_a`$ laws L01–L02 and its
divergence constraint. The direct E_a density bridge A02 avoids reliance
on the inconsistent potential laws.

### V01 — Abelian vector laws; OP(2.13) with g=0

```math
\begin{aligned}
\delta A_\mu&=-\tfrac i2\rho\bar\epsilon\psi_\mu+\tfrac12\bar\epsilon\gamma_\mu\lambda,
&\delta\rho&=\tfrac i2\bar\epsilon\lambda,\\
\delta\lambda^i&=-\tfrac14\gamma\!\cdot\!\widehat F\epsilon^i
-\tfrac i2\mathord{\not{\mathcal D}}\rho\epsilon^i+\rho\gamma\!\cdot\!T\epsilon^i
-Y^{ij}\epsilon_j+\rho\eta^i,\\
\delta Y^{ij}&=-\tfrac12\bar\epsilon^{(i}\mathord{\not{\mathcal D}}\lambda^{j)}
+\tfrac i2\bar\epsilon^{(i}\gamma\!\cdot\!T\lambda^{j)}
-4i\rho\bar\epsilon^{(i}\chi^{j)}+\tfrac i2\bar\eta^{(i}\lambda^{j)}.
\end{aligned}\tag{V01}
```

### V02 — Vector derivatives and curvature; OP(2.14)–(2.16)

```math
\begin{aligned}
\mathcal D_\mu\rho&=(\partial_\mu-b_\mu)\rho-\tfrac i2\bar\psi_\mu\lambda,\\
\mathcal D_\mu\lambda^i&=D_\mu^{(0)}\lambda^i
+\tfrac14\gamma\!\cdot\!\widehat F\psi_\mu^i
+\tfrac i2\mathord{\not{\mathcal D}}\rho\psi_\mu^i+Y^{ij}\psi_{\mu j}
-\rho\gamma\!\cdot\!T\psi_\mu^i-\rho\phi_\mu^i,\\
\widehat F_{\mu\nu}&=2\partial_{[\mu}A_{\nu]}
-\bar\psi_{[\mu}\gamma_{\nu]}\lambda+\tfrac i2\rho\bar\psi_{[\mu}\psi_{\nu]}.
\end{aligned}\tag{V02}
```

For $`\mathcal D_\mu Y^{ij}`$ use the weight2 triplet derivative minus V01's
$`\delta Y^{ij}`$ with parameters $`(\psi_\mu,\phi_\mu)`$. This also fixes it
without a further source lookup.

### V03 — Defining vector; OP(5.16),(5.17)

```math
(\rho,A_\mu,\lambda^i,Y^{ij})
=\left(\sigma,C_\mu,\psi^i,\tfrac i4\sigma^{-1}\bar\psi^{(i}\psi^{j)}\right).
\tag{V03}
```

Its Y-slot transforms as V01 with $`(\rho,\lambda)=(\sigma,\psi)`$ by
OP(5.17). It is not an independent auxiliary field in this identification.
This is a different map from M01–M04 and from a linear-to-vector compensator
construction. Use V01/W02 rather than the misprinted restatement (5.14)–(5.15).

### A01 — Full vector–linear density; OP(3.1)

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\tfrac12\bar\psi_a^i\gamma^a\lambda^jL_{ij}
-\tfrac1{12}\epsilon^{\mu\nu\rho\sigma\lambda}A_\mu\partial_\nu E_{\rho\sigma\lambda}\\
&+\rho\left(N+\tfrac12\bar\psi_a\gamma^a\varphi
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right).
\end{aligned}\tag{A01}
```

All epsilon symbols here have the tensor convention C01. The integrated
three-form coupling is equivalent, modulo a boundary term, to
$`+F_{\mu\nu}E^{\mu\nu}/2`$. The gravitino–gaugino term still contains
$`\lambda^j`$; OP(3.2)'s $`\psi^j`$ is a transcription inconsistency (X06).
Use A01 as the density anchor. Boundary equivalence is not equality of
unintegrated densities.

### A02 — Operational density in terms of E_a; OPall(3.1)–(3.2)

The companion local paper supplies the required explicit bridge:

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},
\qquad
P^a=-\frac1{12}e_\mu{}^a\epsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}.
\tag{A02a}
```

The first identity is OPall(3.2); the second identifies the ordinary
three-form part in the A01 density. The first is sufficient for the
**operational** density formula, with no E3 potential variation needed:

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\frac12\bar\psi_a^i\gamma^a\lambda^jL_{ij}+A_aP^a\\
&+\rho\left(N+\frac12\bar\psi_a\gamma^a\varphi
+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right).
\end{aligned}\tag{A02b}
```

Here $`A_a=e_a{}^\mu A_\mu`$. OPall(3.1) misprints the contracted gaugino
index as $`i`$ a second time; A01 fixes it unambiguously to $`j`$.
Calling P the ordinary part of E does **not** set physical fermions to zero
in a composite Weyl linear multiplet. Use the full first identity in A02a.
The later invariance test must include this completion. The optional
potential formulation has the unresolved literal-source conflict X10.

## 7. Selected Weyl-to-linear map, including its genuine gaps
### M01 — Scalar triplet

```math
\begin{aligned}
L^{ij}={}&\frac{i}{4}\overline{\widehat R}_{ab}{}^{(i}(Q)
                       \widehat R^{j)ab}(Q)
+\frac{256i}{3}\bar\chi^{(i}\chi^{j)}
+\frac{16}{3}\widehat R_{ab}{}^{ij}(V)T^{ab}.
\end{aligned}
\tag{M01}
```

The first two terms are explicit fermion bilinears. The third also has
implicit fermions through $`\widehat R(V)`$ and, after the Dilaton-Weyl map,
through $`T`$. Thus (5.8) is not wholly bosonic.

### M02 — Literal printed spinor; use M08 for calculations

```math
\begin{aligned}
\varphi^i={}&
-\frac18\gamma_{cd}\widehat R_{ab}{}^i(Q)\widehat C^{abcd}
-4i\gamma_c\widehat R_{ab}{}^i(Q)\mathcal D^aT^{bc}
+\frac{128}{3}\chi^iD
\\
&+8i\gamma_c\mathcal D^c\widehat R_{ab}{}^i(Q)T^{ab}
+8i\gamma_a\mathcal D^c\widehat R_{bc}{}^i(Q)T^{ab}
-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^i
\\
&+\frac{1024}{9}T^2\chi^i
+\frac{128i}{3}\gamma_a\mathcal D_b\chi^i T^{ab}
+\frac{16}{3}\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}
\\
&+\frac12\widehat R^{ab\,i}{}_{j}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j.
\end{aligned}
\tag{M02}
```

The source prints this fermionic component without a separate remainder
marker. It remains supercovariant: apparent linearity in the explicit
fermionic factors does not imply linearity in independent physical fermions.
Its Q-matching has now been calculated: M07/X12 find one coefficient
mismatch. Preserve this literal expression separately from the derived
spinor M08, adopted on 2026-09-18; transcription is not an all-order certification.

### M03 — Constrained vector with its printed omission

```math
\begin{aligned}
E_a={}&\frac1{16}\epsilon_{abcde}C^{bcfg}C^{de}{}_{fg}
-\frac1{12}\epsilon_{abcde}V^{bc}{}_{ij}V^{de\,ij}
\\
&+\mathcal D^b\left(
4C_{abcd}T^{cd}-\frac{64}{3}DT_{ab}
-\frac{128}{9}T_{ab}T^2-\frac{512}{3}T_{ac}T^{cd}T_{bd}
\right)
\\
&-32\epsilon_{abcde}\mathcal D^b\left(
\frac23T^{cf}\mathcal D_fT^{de}
+T^c{}_{f}\mathcal D^dT^{ef}\right)
+\text{fermions}.
\end{aligned}
\tag{M03}
```

The terminal “fermions” is present in the source. It is an unknown
completion in the printed source, not a term set to zero. The derived
singlet-slot candidate including fermions is now specified by M14.

### M04 — Scalar with its printed omission

```math
\begin{aligned}
N={}&\frac18C^{abcd}C_{abcd}
+\frac{64}{3}D^2+\frac{1024}{9}T^2D
-\frac{16}{3}C_{abcd}T^{ab}T^{cd}
-\frac13V_{ab}{}^{ij}V^{ab}{}_{ij}
\\
&-\frac{64}{3}\mathcal D_aT_{bc}\mathcal D^aT^{bc}
+\frac{64}{3}\mathcal D_bT_{ac}\mathcal D^aT^{bc}
-\frac{128}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}
\\
&-\frac{128}{3}\epsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
+1024T^4-\frac{2816}{27}(T^2)^2
+\text{fermions}.
\end{aligned}
\tag{M04}
```

The two explicit missing-completion locations are therefore M03 and M04.
They are not a reason to discard the already printed fermions in M01–M02.

### M05 — Locked procedure and matching residuals

Use $`T^4=T_{ab}T^{bc}T_{cd}T^{da}`$ and $`(T^2)^2=(T_{ab}T^{ab})^2`$,
OP(5.9). Retain every derivative ordering in M03–M04; no integration by
parts is implied in a multiplet identity.

1. M06/M07 give the scalar S/Q checks. The working map uses the
   derived spinor on 2026-09-18: set $`\varphi_W=\varphi_Q`$ as displayed
   fully in M08. Its S-law remains a required consistency calculation.
2. Use the completed termwise Q(M08) calculation M09, including the fully
   evaluated R04b/R07 and G01/G04 responses in notebook Part III. Define
   the residual
   ```math
\mathscr X^i=\delta\varphi_W^i
   +\frac i2\mathord{\not{\mathcal D}}L_W^{ij}\epsilon_j
   +\gamma\!\cdot\!T L_W^{ij}\epsilon_j-3L_W^{ij}\eta_j.
   ```
   After complete Clifford/Fierz and SU(2) reduction, require
   ```math
\mathscr X^i=\tfrac12N_W\epsilon^i-\tfrac i2\gamma^aE_{Wa}\epsilon^i.
   ```
   Match each physical fermion degree. Any other independent structure is
   a failed consistency condition, not a coefficient to discard.
3. Verify $`\delta E_{Wa}`$, $`\delta N_W`$ and $`\mathcal D^aE_{Wa}=0`$
   against L01–L03. No auxiliary field equation is allowed in this off-shell
   check. State and resolve any improvement/boundary ambiguity explicitly.
4. A03 records algebraic insertion of the current
   map into V03/A02 before the remaining law checks. The explicit result is
   recorded in A03 below; full invariance certification still requires step3.
   Use D01–D02 as full composite definitions. Expand hidden fermions before imposing
   the later source gauge $`\sigma=1,b_\mu=0,\psi^i=0`$; preserve the gravitino.
5. Audit the compatible two-derivative action and verify a background before
   its bosonic and fermionic spectrum. The proposed first background is
   fluxless Minkowski5, not a pre-verified vacuum.

S-invariance is complete (M06). The full Q-variation in step1 is complete
(M07), with a nonzero residual against literal M02 (X12). The working definition
fixes the working spinor to M08; this source discrepancy no longer blocks
using it. M09 now gives the full uncollected spinor Q-variation; S(varphi),
irreducible E/N matching and descendant checks remain required.

### M06 — Verified S-invariance of the printed scalar triplet

With the source ordering $`T_{[a}{}^c`$ in R05 (X11), the conventional
constraint $`\gamma^a\widehat R_{ab}(Q)=0`$ gives

```math
T_{[a}{}^c\gamma_{b]c}\widehat R^{ab\,i}(Q)
=T_{ab}\widehat R^{ab\,i}(Q),\qquad
\gamma_{abcd}T^{cd}\widehat R^{ab\,i}(Q)
=-2T_{ab}\widehat R^{ab\,i}(Q).
\tag{M06a}
```

The three terms of M01 therefore vary as

```math
\begin{aligned}
\delta_S L_R^{ij}&=-8iT_{ab}\bar\eta^{(i}\widehat R^{j)ab}(Q),\\
\delta_S L_\chi^{ij}&=-\frac{128i}{3}\bar\eta^{(i}\gamma\!\cdot\!T\chi^{j)},\\
\delta_S L_{VT}^{ij}&=+8iT_{ab}\bar\eta^{(i}\widehat R^{j)ab}(Q)
+\frac{128i}{3}\bar\eta^{(i}\gamma\!\cdot\!T\chi^{j)},\\
\delta_S L^{ij}&=0=\delta_S L_{ij}.
\end{aligned}\tag{M06b}
```

This is an exact off-shell algebraic consequence of the source S-laws and
conventional constraint, with no fermion truncation. The complete derivation
is DERIVATION-fermionic-map.md,
(S01)–(S46); finite-basis checks are implemented in [the S-invariance checker](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_map_s_invariance.py).
The Q-law of L is derived in M07. Literal M02 fails one coefficient
comparison; the derived spinor is now adopted as M08. Its Q-variation is given in M09; M10–M14 extract the singlet E/N coefficients.
Independent descendant laws are outside that calculation.

### M07 — Derived Q-variation and literal-spinor residual

Use $`\mathscr R_{ab}^i=\widehat R_{ab}^i(Q)`$,
$`K=\gamma^{ab}T_{ab}`$ and $`X^i=T^{ab}\mathscr R_{ab}^i`$.
The gamma-trace constraint implies

```math
T^{ab}T^c{}_a\mathscr R_{bc}^i=0,\qquad
T^{ab}T^{cd}\gamma_d\gamma_a\mathscr R_{bc}^i=\frac12KX^i.
\tag{M07a}
```

Contracting every term of R06b then gives the nonzero algebraic contribution

```math
T^{ab}\widehat R_{ab}^i(S)
=-iT^{ab}\gamma^c\mathcal D_c\mathscr R_{ab}^i
-iT^{ab}\gamma_a\mathcal D^c\mathscr R_{bc}^i+\frac13KX^i.
\tag{M07b}
```

The complete M01 variation with W03/R05/R06 is

```math
\begin{aligned}
\delta_Q L^{ij}&=i\bar\epsilon^{(i}\varphi_Q^{j)},\\
\varphi_Q^i&=\varphi_{\mathrm{M02}}^i-\frac83KX^i,\\
\delta_Q L^{ij}-i\bar\epsilon^{(i}\varphi_{\mathrm{M02}}^{j)}
&=-\frac{8i}{3}\bar\epsilon^{(i}KX^{j)}.
\end{aligned}\tag{M07c}
```

Thus the derived spinor is exactly the eleven-term M02 expression with
only the coefficient of $`\gamma_{ab}\widehat R_{cd}^i(Q)T^{ab}T^{cd}`$
changed from the **printed16/3** to the **derived8/3**. This is a consequence
of the unchanged v4 curvature/matter laws. The working map uses
this result as the working spinor M08 under lock v5. M02 remains literal;
$`\varphi_W=\varphi_Q`$ is the chosen calculation input. This adoption does
not certify its unperformed transformations or constitute a published erratum.

The full derivation, including all three summands, is notebook Part II,
Q01–Q64. Q48–Q56 prove M07a–b; Q63 displays the entire spinor. The companion
[Q-variation checker](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_map_q_variation.py) tests complete finite tensor/spinor bases and gives
a nonzero residual example. It reports PASS for the hand reduction and
FAIL for literal M02 matching. No EOM, gauge or fermion truncation is used.

### M08 — Adopted working spinor, 2026-09-18

**Spinor convention:** the working map uses the result derived from Q(L).
Set $`\varphi_W^i:=\varphi_Q^i`$. Its full expression, from notebook Q63, is

```math
\begin{aligned}
\varphi_W^i={}&
-\frac18\gamma_{cd}\widehat R_{ab}{}^i(Q)\widehat C^{abcd}
-4i\gamma_c\widehat R_{ab}{}^i(Q)\mathcal D^aT^{bc}
+\frac{128}{3}\chi^iD
\\
&+8i\gamma_c\mathcal D^c\widehat R_{ab}{}^i(Q)T^{ab}
+8i\gamma_a\mathcal D^c\widehat R_{bc}{}^i(Q)T^{ab}
-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^i
\\
&+\frac{1024}{9}T^2\chi^i
+\frac{128i}{3}\gamma_a\mathcal D_b\chi^i T^{ab}
+\frac{8}{3}\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}
\\
&+\frac12\widehat R^{ab\,i}{}_{j}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j.
\end{aligned}
\tag{M08}
```

Only the coefficient of $`(\gamma\cdot T)(T\cdot\widehat R(Q))`$ differs
from literal M02: working8/3, printed16/3. No field, derivative, curvature,
bar, SU(2), action or coupling normalization changes. The input identities
from v4 and the scalar's S/Q proofs therefore carry forward unchanged.

**Use M08** in M05's spinor residual and all subsequent construction.
The full termwise Q-variation is M09; M11 and the
[component derivations](../../../../computations/weyl_fermionic/derivations/README.md)
give the collected slots and invariant density. M08 alone does not establish
the spinor S-law or the full supercovariant divergence constraint. The nonzero comparison with literal M02 remains valid evidence.

### M09 — Complete termwise Q-variation of the adopted spinor

**Derived on 2026-09-18; input lock unchanged.** The complete hand calculation
is notebook Part III,
equations P01–P80 (with P05a/P23a). It uses M08 and the W/G/R inputs above,
physical $`g=0`$, no gauge fixing, no EOM, and no fermion truncation.

```math
\delta_Q\varphi_W^i=\sum_{n=1}^{11}\mathcal W_n^i,
\qquad \mathcal W_n^i=\text{explicit block (P}(46+2n)\text{)},
\qquad \#\text{ outer terms}=94.
\tag{M09}
```

This equality is **uncollected** in Clifford/Fierz structures. Its eleven
blocks are P48/P50/P52/P54/P56/P58/P60/P62/P64/P66/P68, in the exact
M08 term order. Their term counts are respectively
9,9,8,3,3,7,8,3,12,17,15. The finite, explicitly evaluated response
polynomials are now reusable results:

| Quantity needed | Complete evaluated expression in Part III |
|---|---|
| Frames, $`\delta\psi_\mu,\delta b_\mu,\delta V_\mu`$ | P06–P08 |
| $`\delta T,\delta\chi,\delta D,\delta\widehat R(Q)`$ | P09–P12 |
| $`\delta\widehat R(V)`$, with all S-curvature terms | P13–P15 |
| $`\delta\omega,\delta\phi_\mu`$, including bars and frame conversions | P16–P23 |
| $`\delta\widehat R'(M),\delta f_\mu,\delta\widehat C`$ | P24–P29 |
| $`\delta(\mathcal D_aT_{bc})`$ | P30–P32 |
| $`\delta(\mathcal D_a\chi^i)`$ | P33–P35 |
| $`\delta(\mathcal D_a\widehat R_{bc}^i(Q))`$ | P36–P38 |
| Cancellation of all derivatives of local $`\epsilon(x)`$ | P39–P46 |

All these expressions are explicit polynomials; no unevaluated variation
or omitted fermion remainder appears on their right sides. Follow that
substitution order: it has no cycle. $`\delta\widehat C`$ has two explicit
inverse-frame terms since its last two indices are already Lorentz
connection indices. The Majorana bar is linear and reverses gamma products;
there is no complex conjugation of $`i`$ in taking $`\bar p`$ or $`\bar\Phi`$.

P71/P73/P76 independently recover the recorded bosonic $`D^2,C^2,V^2`$
coefficients in M03–M04. The scoped checker
[verify_weyl_spinor_q_variation.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_spinor_q_variation.py) and the retained
[VARPHI-Q-TERM-LEDGER.json](../../../../computations/weyl_fermionic/inputs/component_ledgers/VARPHI-Q-TERM-LEDGER.json) reproduce the coefficient and Clifford/SU(2)
checks. Their PASS is not full multiplet closure. M10 completes the singlet Fierz extraction; M11
collects its Clifford ranks. Full P80 matching (M05 at $`\eta=0`$), including
the required $`N\epsilon/2`$ and $`-i\gamma^aE_a\epsilon/2`$ structures,
is outside the singlet extraction. The spinor S-law is outside its scope.

### M10 — Complete epsilon-right singlet calculation in ordinary fields

**Updated 2026-09-18; v5 input laws and adopted M08 unchanged.** Read
notebook Part IV.
The eleven $`F_n`$ are labels of M08's original terms, not new fields:

```math
\left.\delta_Q\varphi_W^i\right|_{\epsilon^i}
=\sum_{n=1}^{11}\left.\delta_QF_n^i\right|_{\epsilon^i}.
\tag{M10}
```

The suffix means the identity component in SU(2), extracted **after**
Fierz and Schouten. All ordered gamma structures are retained. The
traceless doublet coefficient is excluded by the stated scope.

| Required calculation | Notebook equations |
|---|---|
| Contracted Majorana/Fierz and symmetric-triplet Schouten | H01–H08 |
| Eleven product rules and the first 66 evaluated singlet origins | H13–H45, H40a |
| Third term in irreducible gamma form; curvature-square checks | H46–H49 |
| Six formerly retained origins and tensor-derivative product rule | H50–H52 |
| Covariant normal-frame evaluation, with all curvatures/fermion jets retained | H54–H56 |
| S-connection singlet at that point, derived from R04b | H57–H60, H59a–H59b |
| Explicit tensor-derivative Q-law, eleven terms | H61–H62 |
| Primed Lorentz curvature, eliminated S curvature, dependent f contraction | H63–H65b |
| Spinor-derivative Q-laws, all connection and S-generator products | H66–H67b |
| Actual Majorana transposes and Schouten coefficient addition | H68–H69 |
| All six retained origins: actual Fierz bilinears, antisymmetrizations expanded | H070–H147 |
| Full addition in original fields, no unevaluated variations | Section 28, H150–H182 |

All 72 nonzero singlet origins are evaluated: 66 earlier origins give
130 terms; the six H50 origins give 472 terms after explicitly expanding
antisymmetrizations in the Fierz pairings. Adding identical expressions
leaves 586 displayed terms. The other 22 original origins have zero
single-curvature SU(2) trace. Gamma products in the full sum retain their
order; the minimal $`N_W,E_{Wa}`$ expressions are given in M13–M14.
The singlet collection is not a closure proof.

For derivative/curvature calculations use H54–H69 directly; no PDF lookup
is needed. H54 is a local evaluation of covariant coefficients, not a
physical gauge or a fermion truncation. Connection values vanish only at
one point. Their variations and antisymmetric derivatives do not vanish.
H60 must not replace R04b as an arbitrary-frame connection law. H66/H67b
use $`\equiv`$ for equality modulo the already-parameter-right traceless
SU(2) terms; their fermion products still require Fierz before projection.

The [component suite](../../../../computations/weyl_fermionic/README.md) runs
`verify_weyl_h50_completion` for the displayed completion and
`verify_weyl_human_notation` for the 66-origin part. The checks certify their stated algebra
and addition; covariance restoration uses the analytic G01/G03 argument
H54–H55. The scalar/vector/bivector collection is now M11. Independent nonlinear closure and the full spinor S-law are outside
this coefficient-collection calculation; the triplet S-law has its
[separate component check](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_map_s_invariance.py).

### M11 — Collected Clifford coefficients of the full singlet

**Derived 2026-09-18; v5/M08 inputs unchanged.** The complete calculation is
notebook Part V,
Sections 30–36. G03–G13 there multiply gamma matrices and retain the correct
position of the inserted Fierz gamma; G14–G20 prove the two-form Schouten
reductions; G101–G702 show all 602 contribution reductions and Section 33.4
adds like contractions, including the cancellations. Its G707–G709 are
given below so this master remains a sufficient working reference.

Here the volume tensor is written as $`\varepsilon_{abcde}`$, and suppressed
spinor SU(2) indices are contracted as in C03. The coefficients have Weyl
weight four. Brackets on $`a,b`$ are weighted; vertical bars exclude dummy
indices. The rank-two sum is over all ordered pairs, without a prefactor
$`1/2`$. All hats and derivatives are full covariants. Derivative order is
preserved. No EOM, integration by parts, bosonic curvature pair-exchange
assumption or differential Bianchi identity enters this collection.

All coefficients below are added across the eleven original terms. They use
only the original physical fields. The complete result is

```math
\boxed{\left.\delta_Q\varphi_W^i\right|_{\epsilon^i}
 =\big[p+\gamma_a t^a+\gamma_{ab}k^{ab}\big]\epsilon^i.}
\tag{M11a}
```

#### M11b — Scalar coefficient

```math
\begin{aligned}
p={}&\frac{1}{16}\widehat C_{cdef}\,\widehat C^{cdef}\\
&-\frac{52}{3}\widehat C_{cdef}\,T^{cd}\,T^{ef}\\
&+8\widehat C_{cdef}\,T^{ce}\,T^{df}\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cdef}{}_{g}\,(\mathcal D_{h}T^{gh})\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{f}T^{gh})\\
&-\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{cde}{}_{gh}\,(\mathcal D^{g}T^{fh})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{d}T^{gh})\\
&-\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cef}{}_{gh}\,(\mathcal D^{g}T^{dh})\\
&+\frac{512}{9}D\,T_{cd}\,T^{cd}\\
&+\frac{32}{3}D^2\\
&-\frac{1408}{27}T_{cd}\,T^{cd}\,T_{ef}\,T^{ef}\\
&+512T_{cd}\,T^{c}{}_{e}\,T^{d}{}_{f}\,T^{ef}\\
&-\frac{64}{3}\varepsilon_{cdefg}\,T^{cd}\,T^{ef}\,(\mathcal D_{h}T^{gh})\\
&+\frac{64}{3}T_{cd}\,(\mathcal D_{e}\mathcal D^{c}T^{de})\\
&-\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{c}T^{de})\\
&+\frac{32}{3}(\mathcal D_{c}T_{de})\,(\mathcal D^{d}T^{ce})\\
&-\frac{1}{6}\widehat R(V)_{cd}{}^{rs}\,\widehat R(V)^{cd}{}_{rs}\\
&+\frac{113i}{16}\big(\overline{\widehat R(Q)_{ec}}\widehat R(Q)^{e}{}_{d}\big)\,T^{cd}\\
&-\frac{97i}{64}\big(\overline{\widehat R(Q)_{ef}}\gamma^{cd}\widehat R(Q)^{ef}\big)\,T_{cd}\\
&+\frac{3}{8}\big(\overline{\widehat R(Q)_{de}}\gamma^{c}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-\frac{112i}{3}\big(\overline{\widehat R(Q)_{cd}}\chi\big)\,T^{cd}\\
&-\frac{128}{3}\big(\bar\chi\gamma^{c}\mathcal D_{c}\chi\big)
\end{aligned}\tag{M11b}
```

#### M11c — Vector coefficient

```math
\begin{aligned}
t^a={}&-\frac{i}{32}\widehat C_{cdef}\,\widehat C^{cd}{}_{gh}\,\varepsilon^{efgha}\\
&+4i\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{df}\,T^{gh}\\
&+8i\widehat C_{cdef}\,\varepsilon^{cea}{}_{gh}\,T^{dg}\,T^{fh}\\
&-4i\widehat C_{cdef}\,\varepsilon^{cefa}{}_{g}\,T^{d}{}_{h}\,T^{gh}\\
&-\frac{22i}{3}\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cd}\,T^{gh}\\
&+4i\widehat C_{cdef}\,\varepsilon^{efa}{}_{gh}\,T^{cg}\,T^{dh}\\
&-\frac{i}{3}\widehat C^{a}{}_{cde}\,(\mathcal D^{c}T^{de})\\
&+\frac{8i}{3}\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{c}T^{de})\\
&-\frac{i}{3}\widehat C_{cd}{}^{a}{}_{e}\,(\mathcal D^{e}T^{cd})\\
&-4i(\mathcal D_{c}\widehat C^{c}{}_{d}{}^{a}{}_{e})\,T^{de}\\
&+4i(\mathcal D_{c}\widehat C_{de}{}^{ca})\,T^{de}\\
&+\frac{32i}{3}D\,(\mathcal D_{c}T^{ac})\\
&-\frac{32i}{3}(\mathcal D_{c}D)\,T^{ca}\\
&-\frac{256i}{3}T^{a}{}_{c}\,T^{c}{}_{d}\,(\mathcal D_{e}T^{de})\\
&+\frac{128i}{9}T^{a}{}_{c}\,T_{de}\,(\mathcal D^{c}T^{de})\\
&+\frac{256i}{3}T^{a}{}_{c}\,T_{de}\,(\mathcal D^{d}T^{ce})\\
&+\frac{64i}{9}T_{cd}\,T^{cd}\,(\mathcal D_{e}T^{ae})\\
&+\frac{256i}{3}T_{cd}\,T^{c}{}_{e}\,(\mathcal D^{d}T^{ae})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D^{e}\mathcal D_{g}T^{fg})\\
&-\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{cd}\,(\mathcal D_{g}\mathcal D^{e}T^{fg})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{e}T^{fg})\\
&-\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,T^{c}{}_{g}\,(\mathcal D^{d}\mathcal D^{g}T^{ef})\\
&+16i\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{e}T^{fg})\\
&+\frac{32i}{3}\varepsilon^{a}{}_{cdef}\,(\mathcal D^{c}T^{d}{}_{g})\,(\mathcal D^{g}T^{ef})\\
&+\frac{i}{24}\varepsilon^{a}{}_{cdef}\,\widehat R(V)^{cd}{}^{rs}\,\widehat R(V)^{ef}{}_{rs}\\
&-3i\big(\overline{\widehat R(Q)_{e}{}^{a}}\gamma^{c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{1}{4}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{a}\widehat R(Q)^{cd}\big)\\
&+\frac{1}{4}\big(\overline{\widehat R(Q)_{cd}}\mathcal D^{c}\widehat R(Q)^{da}\big)\\
&-\frac{1}{2}\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D_{d}\widehat R(Q)^{cd}\big)\\
&-\frac{1}{4}\big(\overline{\widehat R(Q)_{de}}\gamma^{ca}\mathcal D_{c}\widehat R(Q)^{de}\big)\\
&-16i\big(\overline{\widehat R(Q)^{a}{}_{c}}\gamma^{d}\chi\big)\,T^{c}{}_{d}\\
&-4\big(\overline{\widehat R(Q)_{c}{}^{a}}\mathcal D^{c}\chi\big)\\
&+4\big(\bar\chi\mathcal D_{c}\widehat R(Q)^{ca}\big)\\
&+\frac{64}{3}\big(\bar\chi\gamma^{ca}\mathcal D_{c}\chi\big)
\end{aligned}\tag{M11c}
```

#### M11d — Bivector coefficient

```math
\begin{aligned}
k^{ab}={}&4\widehat C^{[a}{}_{|cde|}\,T^{|c|b]}\,T^{de}\\
&-8\widehat C^{[a}{}_{|cde|}\,T^{|cd|}\,T^{|e|b]}\\
&+8\widehat C^{[a}{}_{|c|}{}^{b]}{}_{d}\,T^{c}{}_{e}\,T^{de}\\
&-\frac{8}{3}\widehat C_{cd}{}^{[a}{}_{|e|}\,T^{|cd|}\,T^{|e|b]}\\
&+\frac{1}{6}\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{e}T^{fg})\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cd[ab]}{}_{g}\,(\mathcal D^{g}T^{ef})\\
&+\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cde[ab]}\,(\mathcal D_{g}T^{fg})\\
&+\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{ce[ab]}{}_{g}\,(\mathcal D^{d}T^{fg})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{cef[ab]}\,(\mathcal D_{g}T^{dg})\\
&-\frac{1}{3}\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{c}T^{dg})\\
&-\frac{1}{12}\widehat C_{cdef}\,\varepsilon^{ef[ab]}{}_{g}\,(\mathcal D^{g}T^{cd})\\
&+(\mathcal D_{c}\widehat C^{c}{}_{def})\,\varepsilon^{ef[ab]}{}_{g}\,T^{dg}\\
&+(\mathcal D_{c}\widehat C_{defg})\,\varepsilon^{cfg[ab]}\,T^{de}\\
&+\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D^{b]}\mathcal D_{d}T^{cd})\\
&-\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D^{|c|}\mathcal D_{|d|}T^{b]d})\\
&-\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D_{|d|}\mathcal D^{b]}T^{cd})\\
&+\frac{32}{3}T^{[a}{}_{|c|}\,(\mathcal D_{|d|}\mathcal D^{|c|}T^{b]d})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{[a}\mathcal D^{b]}T^{cd})\\
&-\frac{32}{3}T_{cd}\,(\mathcal D^{[a}\mathcal D^{|c|}T^{b]d})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{[a}T^{b]d})\\
&+\frac{32}{3}T_{cd}\,(\mathcal D^{c}\mathcal D^{d}T^{[ab]})\\
&+\frac{59i}{32}\big(\overline{\widehat R(Q)^{[ab]}}\widehat R(Q)_{cd}\big)\,T^{cd}\\
&+\frac{29i}{32}\big(\overline{\widehat R(Q)_{de}}\gamma^{[a|c|}\widehat R(Q)^{|de|}\big)\,T_{|c|}{}^{b]}\\
&-\frac{45i}{8}\big(\overline{\widehat R(Q)_{d}{}^{[a}}\widehat R(Q)^{|d|}{}_{|c|}\big)\,T^{|c|b]}\\
&+\frac{27i}{16}\big(\overline{\widehat R(Q)_{e}{}^{[a}}\gamma^{b]c}\widehat R(Q)^{e}{}_{d}\big)\,T_{c}{}^{d}\\
&+\frac{47i}{8}\big(\overline{\widehat R(Q)^{[ab]}}\gamma^{cd}\chi\big)\,T_{cd}\\
&+\frac{32i}{3}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\chi\big)\,T^{|c|b]}\\
&-\frac{79i}{2}\big(\overline{\widehat R(Q)^{[a}{}_{|c|}}\gamma^{b]d}\chi\big)\,T^{c}{}_{d}\\
&+\frac{269i}{24}\big(\overline{\widehat R(Q)_{cd}}\gamma^{[ab]}\chi\big)\,T^{cd}
\end{aligned}\tag{M11d}
```

The sums have **22 scalar, 34 vector and 29 bivector contractions** in this
displayed tensor basis. Square brackets make the last coefficient explicitly
antisymmetric; they introduce no extra overall $`1/2`$ in M11a.
This is a complete reduction in **Clifford rank**. It is not a claim that all
Lorentz-tensor contractions are independent after every possible curvature
Bianchi identity or covariant-derivative commutator.

This is the exact collection of the supplied singlet, conditional on v5/M08.
It does not assert $`k^{ab}=0`$ or identify $`p=N_W/2`$, $`t^a=-iE_W^a/2`$
without completing the remaining multiplet-law terms. The full curvature
identities and ordered derivative commutators, the traceless SU(2) law and
S(varphi) are outside the rank collection. M12–M14 give the subsequent
bivector cancellation and canonical singlet coefficients.

Verification: [verify_weyl_clifford_collection.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_clifford_collection.py) checks exact
coefficient addition, all 1024 gamma-basis products, every displayed
intermediate reduction, and ten independent full-polynomial component
samples with two Grassmann generators. The [component-check runner](../../../../computations/weyl_fermionic/checks/reference_suite.py) generates
`CLIFFORD-COLLECTION-CHECKS.json` in its temporary workspace. The matrix checks certify this algebra;
they are not an independent nonlinear supersymmetry-closure proof.

## 8. Source discrepancies and resolved interfaces

These are project derivations/interpretations, **not published errata**.
This section records the component
of the working reference, so a routine calculation need not open the audit.

### X01 — Lorentz-curvature errors in OP(2.7)

The literal source contains both
$`+i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ and
$`-8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi`$.
Use R03 instead: omit the naked bilinear and use **+8** in the chi term.

Evidence: the naked bilinear has world Weyl weight $`-1`$, whereas
$`R_{\mu\nu}{}^{ab}(M)`$ has weight0, and it has no origin in W(3.4), the
soft-algebra Lorentz structure function or W(3.20). The three M-dependent
Q pieces of W(3.20) have coefficients $`(-1/2,-1/4,-4)`$; multiplying by
$`-2\bar\psi_{[\mu}`$ according to G03b gives $`(+1,+1/2,+8)`$.
The T-dependent structure function contributes the single T-bilinear in
R03. The $`\phi\psi`$ term is already in the undeformed curvature W(3.4).
This is the local-source reconciliation of the inherited chi correction.
It does not certify the later full nonlinear invariant.

### X02 — Chi weight in OP(2.12)

Literal: $`(\partial_\mu-7b_\mu/2+\cdots)\chi`$.
Working W04: $`(\partial_\mu-3b_\mu/2+\cdots)\chi`$.
W Table3 gives $`w(\chi)=3/2`$, also fixed by
$`\delta T\sim\bar\epsilon\chi`$ with $`w(T)=1,w(\epsilon)=-1/2`$.
The printed derivative would leave
$`-2(\partial_\mu\Lambda_D)\chi`$ under a local dilatation.
The $`7/2`$ weight belongs to $`\varphi`$, not $`\chi`$.

### X03 — Missing sigma in both short H variations

OP(2.8) and W(3.27) both print
$`+3i\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi/2`$.
H02 uses $`+3i\sigma\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi/2`$.
At a point set $`\psi_\mu=C=B=T=0`$, $`\sigma=s`$ constant, and retain
arbitrary $`\partial\psi`$ with constant $`\epsilon`$. W02 and H01 give
$`\delta H_{abc}=3\partial_{[a}\delta B_{bc]} =(3i/2)s\bar\epsilon\gamma_{[ab}\partial_{c]}\psi`$.
No other term supplies this principal derivative. Its weight must be3;
the literal term has weight2. The repair is therefore fixed independently
by direct differentiation and by weights. The remainder of H02 is an
extracted short law, not a newly certified all-order derivation.

### X04 — World/tangent and epsilon typography

W(3.27) gives tangent $`\delta\widehat G_{ab}`$; OP(2.8) prints the same
shape with world indices. Use H02 as the tangent law and G04 for actual
coordinate variations. Similarly W(A.12)'s upper-world epsilon notation
includes a density factor. Our tensor/density definitions are C01.
They must be used consistently in A01 and L03; no extra determinant may
be inferred from the source typography.

### X05 — Partial dependent-connection variations

W(3.21) expressly prints M-dependent additions, with an ellipsis; W(3.22)
expressly prints only the M-dependent S variation of the f trace.
Use R04b and R04d, differentiated from complete dependent definitions,
for full variations. A sum of the bare algebra and the printed additions
can miss field-dependent structure-function contributions.

### X06 — Repeated density and vector formulas

OP(3.2) prints $`\psi^j`$ in the term that is $`\lambda^j`$ in (3.1);
integration by parts cannot change a gaugino species. Use A01.
OP(5.14) restates $`\delta A_\mu`$ with $`\sigma`$ instead of $`\rho`$ and a
missing $`i`$; OP(5.15) drops the $`i`$ in $`\delta C_\mu`$.
Use the unambiguous original OP(2.13)/(2.1), V01/W02.

### X07 — Equivalent conventions that must not be repaired

The opposite-looking f/Ricci signs are identical because of the two Ricci
index contractions, R03. The opposite-looking epsilon-H signs in the
auxiliary T map are identical after reversing three H indices, D01.
W(A.14) dots are full contractions, C04; its last factorial literally
$`(n-5)!`$ is a typo for $`(5-n)!`$, as required by the dual tensor's rank.
C03 distinguishes fixed-index and SU(2)-contracted bilinear flips.

### X08 — Remaining qualifications

The printed M02 spinor and the short curvature laws must still pass the
planned nonlinear variation matching. The self-contained inputs do not
make M03/M04's omitted fermions known. The full gauge-preserving Poincare
transformations must be derived from the unfixed rules; OP(4.3) explicitly
qualifies its compensating parameters by a cubic-fermion truncation.
The earlier 2013/2016 compensator linear-to-vector Y-slot disagreement is
a separate unresolved issue for the **two-derivative** action. It is not
an input to M01–M05 and must be audited before constructing the total action.

### X09 — Tensor-derivative index/sign mismatch

OP(2.12) and (5.11) literally use $`-2\omega_\mu{}^c{}_{[a}T_{b]c}`$.
With the locked Lorentz connection, a covector has
$`\nabla_\mu X_a=\partial_\mu X_a+\omega_{\mu a}{}^bX_b`$.
The tensor-product rule therefore gives

```math
\nabla_\mu T_{ab}=\partial_\mu T_{ab}
+\omega_{\mu a}{}^cT_{cb}+\omega_{\mu b}{}^cT_{ac}
=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}
=\partial_\mu T_{ab}-2\omega_{\mu[a}{}^cT_{b]c}.
\tag{X09}
```

Use this explicit tensor-product rule in G01/W04. The source's minus sign
would be correct with the **other** index ordering $`\omega_{\mu[a}{}^c`$,
not with its displayed raised-c-first ordering. A spatial rotation with
$`\omega_{\mu23}=w,T_{13}=t`$ gives $`(\nabla_\mu T)_{12}=+wt`$ by Leibniz,
but the literal raised-c-first minus sign gives $`-wt`$. This interface is
checked independently in `verify_conventions.py`.

### X10 — Potential-law conflict; operational E_a route

The literal L04 laws do not agree with each other under the tensor duality
L03 and the source gamma orientation C04. In particular,
$`\epsilon^{\mu\nu\rho\sigma\lambda}\gamma_{\rho\sigma\lambda} =6i\gamma^{\mu\nu}`$. Thus $`\delta E_3=-\bar\epsilon\gamma_3\varphi`$
would yield $`\delta E^{\mu\nu}=+i\bar\epsilon\gamma^{\mu\nu}\varphi/2`$
at leading flat order, opposite to the printed two-form law. It likewise
opposes L01's principal derivative of $`\varphi`$. Variation of the tensor
duality also carries a determinant term absent from the printed two-form
formula. These are not resolved by silently renaming a tensor as a density.

**Decision:** L04 is stored as source evidence, not an adopted transformation.
Use L01–L02, the constraint in L03a, and the explicit E_a density A02.
A full consistent potential-law reconstruction is a separate optional task
if a potential presentation is later needed. The selected map completion
and density construction have an explicit route that does not require it.
The checker detects this conflict; it does not report it as a resolved PASS.

### X11 — Index ordering in the S variation

The R05 term uses $`T_{[a}{}^c`$, with $`T_a{}^c=-T^c{}_a`$.
The [component dictionary](COMPONENT_CONVENTIONS.md), X11, records the
index-ordering argument and its gamma-trace consequence.

## 9. Validation boundary and maintenance

The reproducible checker [verify_conventions.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_conventions.py) tests a concrete
4×4 Clifford representation, duality and bilinear/Fierz coefficients,
SU(2) raising/lowering, curvature traces/Ricci conversion and Weyl-weight
consistency. It also checks the distinguishing tests in X01–X03.
It cannot prove all local-SUSY identities or an unconstructed map.

Every new derivation must cite these IDs, declare physical fermion degree
and use the source-derived repairs consistently. A newly needed convention
or a failed identity belongs here with provenance and a check; do not add
an undocumented convention only inside a calculation. Changing an operative
sign/normalization requires a new lock version and downstream revalidation.

## M12 — Proven cancellation of the M11d singlet bivector

**Derived result, 2026-09-18; same lock v5.** Full hand proof: [bivector-cancellation.md](../../../../computations/weyl_fermionic/derivations/bivector-cancellation.md), B01–B36, also given in notebook
Part VI. This supersedes the earlier *open status* of the M11d remainder;
it preserves the displayed M11d polynomial for traceability.

With $`R_{ab}=\widehat R_{ab}(Q)`$ and $`C_{abcd}=\widehat C_{abcd}`$ only in
this subsection, G03's constrained curvatures satisfy pair exchange and
the cyclic identity, and $`\gamma^aR_{ab}=0`$ implies

```math
\gamma_{[ab}R_{cd]}=0,\qquad
\varepsilon_{abcde}R^{de}=2i(\gamma_aR_{bc}+\gamma_bR_{ca}+\gamma_cR_{ab}).
\tag{M12a}
```

The **full** covariant commutator required for M11d is

```math
[\mathcal D_a,\mathcal D_b]T_{cd}
=C_{ab c}{}^eT_{ed}+C_{ab d}{}^eT_{ce}
-\frac i2\bar R_{ab}\gamma_{cd}\chi+\frac{3i}{32}\bar R_{ab}R_{cd}.
\tag{M12b}
```

Its fermionic part is minus W03's Q-law with parameter $`R_{ab}(Q)`$.
For the two differentiated-curvature terms retain the complete Bianchi
identity derived from R03, not the bosonic identity:

```math
\begin{aligned}
\mathcal D_aC_{bcde}+\mathcal D_bC_{cade}+\mathcal D_cC_{abde}
={}&2\sum_{\mathrm{cyc}(abc)}[R(K)_{ab d}\eta_{ce}-R(K)_{ab e}\eta_{cd}]\\
&+\tfrac14\sum_{\mathrm{cyc}(abc)}[\bar R_{ab}\gamma_dR_{ce}
-\bar R_{ab}\gamma_eR_{cd}+\bar R_{ab}\gamma_cR_{de}]\\
&+2\sum_{\mathrm{cyc}(abc)}[\eta_{cd}\bar R_{ab}\gamma_e\chi
-\eta_{ce}\bar R_{ab}\gamma_d\chi].
\end{aligned}\tag{M12c}
```

$`R(K)`$ denotes the existing special-conformal curvature; its double-trace
identity gives $`12R(K)_{ab}{}^b=0`$ in these conventions. No field equation
is used. The proof calculates the two differentiated-curvature terms
separately, including the nonzero fermionic pieces, before cancelling them.

The gamma-trace/Schouten/Majorana reductions used in the final addition are

```math
\begin{aligned}
0={}&T^{cd}\bar R_{ab}R_{cd}
 +2\bar R_{c[a}\gamma_{b]d}R^c{}_eT^{de},\\
\bar R_{cd}\gamma_{ab}R^{cd}={}&4\bar R_{ca}R^c{}_b,\\
0={}&T^{cd}\bar R_{ab}\gamma_{cd}\chi
 -4\bar R_{[a|c|}\gamma_{b]d}\chi T^{cd}
 +T^{cd}\bar R_{cd}\gamma_{ab}\chi.
\end{aligned}\tag{M12d}
```

Equations M12b–M12d cancel **all 29 terms** of M11d, including the
dualized rank-three terms. The final bounded result is

```math
\boxed{k^{ab}=0,\qquad
\left.\delta_Q\varphi_W^i\right|_{\rm singlet}
=(p+\gamma_a t^a)\epsilon^i.}
\tag{M12e}
```

The verification script is [verify_weyl_bivector_cancellation.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_bivector_cancellation.py);
its finite component/Grassmann check is distinct from the analytic proof.
This is exact relative to v5/M08, off shell and without a fermion
truncation. It does not certify the traceless SU(2) sector, E/N matching,
S(varphi), the complete invariant, or a spectrum.

## M13 — Canonical scalar coefficient p of the full singlet

**Derived 2026-09-18, unchanged lock v5.** Notebook Part VII, SC01–SC33,
also [scalar-coefficient.md](../../../../computations/weyl_fermionic/derivations/scalar-coefficient.md),
reduces all 22 terms of M11b to the following 15 contractions. M11b remains
the traceable intermediate expression. All hats and derivatives are full.

The contraction of M12b needed to put the second derivatives in source order is

```math
\begin{aligned}
\frac{64}{3}T_{cd}\mathcal D_e\mathcal D^cT^{de}
={}&-\frac{64}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}
 +\frac{32}{3}\widehat C_{abcd}T^{ab}T^{cd}\\
&+\frac{32i}{3}T^{ab}\overline{\widehat R_{ab}(Q)}\chi
 -2iT^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_b(Q).
\end{aligned}\tag{M13a}
```

SC09–SC16 explicitly evaluate every Lorentz and Q-curvature contribution.
SC17–SC21 multiply the remaining gamma-two bilinear and derive
$`\bar R_{cd}\gamma_{ab}R^{cd}=4\bar R_{ca}R^c{}_b`$ with the contracted
Majorana sign. The three coefficient additions are

```math
-\frac{52}{3}+4+\frac{32}{3}=-\frac83,\qquad
\frac{113i}{16}-\frac{97i}{64}(4)-2i=-i,\qquad
-\frac{112i}{3}+\frac{32i}{3}=-\frac{80i}{3}.
\tag{M13b}
```

Five curvature–epsilon terms vanish individually by the constrained cyclic
curvature identity; no $`\varepsilon TT\mathcal DT`$ term is discarded.
The complete result is

```math
\boxed{
\begin{aligned}
p={}&\frac1{16}\widehat C_{abcd}\widehat C^{abcd}
+\frac{32}{3}D^2+\frac{512}{9}D\,T_{ab}T^{ab}
-\frac83\widehat C_{abcd}T^{ab}T^{cd}
-\frac16\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)\\
&-\frac{32}{3}(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})
+\frac{32}{3}(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})
-\frac{64}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{64}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
+512T_{ab}T^{bc}T_{cd}T^{da}
-\frac{1408}{27}(T_{ab}T^{ab})^2\\
&+\frac38\overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)
-iT^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)\\
&-\frac{80i}{3}T^{ab}\overline{\widehat R_{ab}(Q)}\chi
-\frac{128}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\end{aligned}
}
\tag{M13c}
```

The specified scalar contribution is $`p\epsilon^i`$. The bosonic restriction
matches half of M04 term by term, including the derivative order. L01 assigns
$`N_W=2p`$ to this extracted slot; its independent transformation law and full
multiplet closure remain unverified. There is no EOM, integration by parts,
fermion truncation, Dilaton-Weyl substitution or Poincare gauge fixing here.

The independent checker is [verify_weyl_scalar_canonicalization.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_scalar_canonicalization.py);
the [component-check runner](../../../../computations/weyl_fermionic/checks/reference_suite.py) generates
`SCALAR-CANONICALIZATION-CHECKS.json` in a temporary workspace. It checks all 22
to 15 terms, the intermediate identities, and the scalar trace of all 272
potentially scalar ordered matrix contributions for two component samples.
The retained explicit one-gamma kinetic bilinears are scalars multiplying
$`\epsilon^i`$, not external $`\gamma_a\epsilon^i`$ contributions.

## M14 — Canonical vector coefficient t^a of the full singlet

**Derived 2026-09-18; unchanged lock v5.** Notebook Part VIII,
VC01–VC44, also [vector-coefficient.md](../../../../computations/weyl_fermionic/derivations/vector-coefficient.md),
canonicalizes all34 terms of M11c. That starting polynomial remains
unchanged for traceability. All covariants and fermion orders are retained.
No EOM, gauge choice, integration by parts or omitted boundary term is used.

The ordered epsilon derivatives of M11c give an exact product derivative
plus two full commutators:

```math
\begin{aligned}
\text{M11c terms19--24}={}&16i\varepsilon^a{}_{cdef}\mathcal D^c
\left[\frac23T^d{}_g\mathcal D^gT^{ef}+T^d{}_g\mathcal D^eT^{fg}\right]\\
&+\frac{32i}{3}\varepsilon^a{}_{cdef}T^{cd}
 [\mathcal D^e,\mathcal D_g]T^{fg}
-\frac{40i}{3}\varepsilon^a{}_{cdef}T^d{}_g
 [\mathcal D^c,\mathcal D^e]T^{fg}.
\end{aligned}\tag{M14a}
```

Substitution of M12b cancels all five explicit epsilon–C–T² terms.
VC19–VC27 prove this using the six-index Schouten identity and curvature
trace-freeness. Retain its fermionic remainder: it changes both TRR and
TRchi coefficients. With $`R_{ab}=\widehat R_{ab}(Q)`$ only in the following identities,
the required reductions are

```math
\begin{aligned}
\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_gR^{fg}
 &=2iT^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -4iT_c{}^d\bar R_e{}^a\gamma^cR^e{}_d,\\
\varepsilon^a{}_{cdef}T^d{}_g\bar R^{ce}R^{fg}
 &=2iT^{cd}\bar R_{ec}\gamma^aR^e{}_d
 -2iT_c{}^d\bar R_e{}^a\gamma^cR^e{}_d,\\
\varepsilon^a{}_{cdef}T^{cd}\bar R^e{}_g\gamma^{fg}\chi
 &=2iT^{cd}\bar R_{cd}\gamma^a\chi
 +4iT^c{}_d\bar R^a{}_c\gamma^d\chi,\\
\varepsilon^a{}_{cdef}T^d{}_g\bar R^{ce}\gamma^{fg}\chi
 &=2iT^{cd}\bar R_{cd}\gamma^a\chi
 +2iT^c{}_d\bar R^a{}_c\gamma^d\chi,\\
-\frac14\bar R_{de}\gamma^{ca}\mathcal D_cR^{de}
 &=\frac12\bar R_{cd}\mathcal D^cR^{da}
 +\frac12\bar R_c{}^a\mathcal D_dR^{cd}.
\end{aligned}\tag{M14b}
```

VC28–VC38 show each gamma multiplication, dualization, six-term spinor
identity and Majorana flip. No further spinor re-pairing is needed.
The complete vector coefficient in original fields is

```math
\boxed{
\begin{aligned}
t^a={}&-\frac i{32}\varepsilon^{abcde}
 \widehat C_{bcfg}\widehat C_{de}{}^{fg}
+\frac i{24}\varepsilon^{abcde}
 \widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
&+\mathcal D_b\Big[
 -2i\widehat C^{ab}{}_{cd}T^{cd}
 +\frac{32i}{3}DT^{ab}
 +\frac{64i}{9}T^{ab}T_{cd}T^{cd}
 +\frac{256i}{3}T^a{}_cT^{cd}T^b{}_d\\
&\hspace{24mm}
 +4\overline{\widehat R(Q)^{ab}}\chi
 -\frac{32}{3}\bar\chi\gamma^{ab}\chi\Big]\\
&+16i\varepsilon^a{}_{bcde}\mathcal D^b\Big[
 \frac23T^{cf}\mathcal D_fT^{de}
 +T^c{}_f\mathcal D^dT^{ef}\Big]\\
&+\frac i2T^{cd}\overline{\widehat R(Q)_{ec}}
 \gamma^a\widehat R(Q)^e{}_d
-\frac{3i}{2}T_c{}^d\overline{\widehat R(Q)_e{}^a}
 \gamma^c\widehat R(Q)^e{}_d\\
&-8iT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi
-\frac{8i}{3}T^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
&+\frac14\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}
+\frac34\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}.
\end{aligned}}
\tag{M14c}
```

It contributes as $`\gamma_at^a\epsilon^i`$. Together M12, M13 and M14 give

```math
\left.\delta_Q\varphi_W^i\right|_{\rm singlet}
=(p+\gamma_at^a)\epsilon^i,\qquad
k^{ab}=0,\qquad N_W=2p,\qquad E_W^a=2it^a.
\tag{M14d}
```

N and E here are the extracted singlet-slot candidates under L01; their
independent descendant laws, full vector divergence, traceless SU(2)
matching and S(varphi) are outside the singlet-slot calculation. All eight bosonic vector coefficients
match M03 with the same derivative placement. The final vector has24
summands when its exact product derivatives are expanded; this is a
presentation count, not a claim of absolute tensor-basis independence.

The independent checker is [verify_weyl_vector_canonicalization.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_vector_canonicalization.py).
Its `VECTOR-CANONICALIZATION-CHECKS.json` report, generated in the
temporary workspace of the [component-check runner](../../../../computations/weyl_fermionic/checks/reference_suite.py), records six full
component/Grassmann comparisons, separate intermediate identities, exact
coefficient additions, finite gamma/duality/reality checks, the Schouten
volume contraction and272 original ordered-matrix vector projections on
two samples. It is an algebraic check relative to v5/M08/M12, not an
independent nonlinear closure or full-action certification.

### A03 — Full map-inserted density, 2026-09-21

Reference `UNG-WEYL2-MAP-DENSITY-v1`: complete derivation.
WA01–WA06 fix the source density, P/E bridge, defining vector and index
contractions. WA07–WA17 evaluate all nine contributions and their product
derivatives. WA24 collects every term; AD01–AD08 give the retained full
DW composites and covariant definitions. Native coefficient: sigma C²/8.

Inputs are M01/M08/M13/M14, consolidated as FM01–FM04. This is exact
algebraic substitution with no EOM, gauge fixing, fermion truncation or
full-density IBP. Independent map laws, U(1) current
conservation, nonlinear SUSY, primitive DW expansion and action normalization
are outside this algebraic substitution check.
The checker [verify_weyl_action_substitution.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_action_substitution.py) passed exact
coefficients, descendant transcription, endpoint collection and six
four-generator Grassmann samples. The physical lock remains v5.

## 11. Gauged extension — CO-GAUGED-DW-FULL-COVARIANTS-v1

The gauged construction in this section
extends the realization of the covariants to nonzero physical g, with
unchanged v5 metric, spinor, curvature and universal Weyl-map coefficients.
It does not replace the ungauged D01/H01/W04 formulas in their original
scope. Use GG03–GG05 in every slot for the gauged construction.

The independent compensator carries subscript c; the Weyl composite
carries W. No compensator orientation or g sign changes. Weight(g)=0
before gauge fixing. Full derivation and scoped checks:
[the gauged calculation](../../../../weyl2/action/details/construction.md),
reference `GAUGED-WEYL2-MAP-DENSITY-v1`.

### GG01 — Full improved-vector constraints

W(5.10)–(5.14), printed27/PDF28, in the
[Bergshoeff et al. source](../../../../references/bibliography.md). These source constraint names
are not new independent fields. Unlike truncated CO formulas, these are
full supercovariant expressions.

```math
\begin{aligned}
S^{ij}&=2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j,\\
\Gamma^i&=i\sigma\mathord{\not{\mathcal D}}\psi^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac14\gamma\!\cdot\!\widehat G\psi^i
+Y^{ij}\psi_j+2\sigma\gamma\!\cdot\!T\psi^i-8\sigma^2\chi^i,\\
\mathcal C&=-\frac14\widehat G_{ab}\widehat G^{ab}
-\frac12\bar\psi\mathord{\not{\mathcal D}}\psi
+\sigma\Box^c\sigma+\frac12(\mathcal D_a\sigma)(\mathcal D^a\sigma)
+Y^{ij}Y_{ij}+i\bar\psi\gamma\!\cdot\!T\psi\\
&\quad-16i\sigma\bar\psi\chi-\frac{104}{3}\sigma^2T_{ab}T^{ab}
+8\sigma\widehat G_{ab}T^{ab}-4\sigma^2D,\\
\mathcal H_a&=-\frac18\varepsilon_{abcde}\widehat G^{bc}\widehat G^{de}
-\mathcal D^b\left(8\sigma^2T_{ba}-\sigma\widehat G_{ba}
-\frac i4\bar\psi\gamma_{ba}\psi\right).
\end{aligned}\tag{GG01}
```

### GG02 — Gauged constraint multiplet

CO(5.2) and W(5.11),(5.13), with the compensator laws L01, give

```math
S^{ij}+gL_c^{ij}=0,\qquad \Gamma^i+g\varphi_c^i=0,\qquad
\mathcal C+gN_c=0,\qquad \mathcal H_a+gE_{ca}=0.
\tag{GG02}
```

The two explicit Q-variation chains are GC04–GC05; the defining-vector
Y Q/S checks are GC06. These define the target DW realization through
parent vector constraints; do not use them to eliminate an independent
field of the final higher-derivative action.

### GG03 — Complete gauged Y, chi and D

GC07–GC11 solve GG02, expand Y² and restore the cubic/quartic terms
missing from earlier truncated gauged calculations. T and every derivative
on the right use the same gauged realization.

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL_c^{ij}=0
\quad\Longrightarrow\quad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac{g}{2\sigma}L_c^{ij}.
\tag{GG03a}
```

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac i{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j\\
&-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i.
\end{aligned}\tag{GG03b}
```

```math
\begin{aligned}
D={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi
-\frac1{64\sigma^4}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{4i}{\sigma}\bar\psi\chi\\
&+\left(-\frac{26}{3}T_{ab}+\frac2\sigma\widehat G_{ab}
+\frac i{4\sigma^2}\bar\psi\gamma_{ab}\psi\right)T^{ab}
+\frac g{4\sigma^2}N_c
-\frac{ig}{16\sigma^4}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{GG03c}
```

### GG04 — Gauged forms and T

CO(5.5)–(5.8); the ordinary form gauge check is GC13. Supersymmetry
potential-law issues X10 remain separate from this bosonic form check.

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\qquad
\widehat G_{\mu\nu}=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\frac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32 C_{[\mu}G_{\nu\rho]}+\frac g2E_{c\,\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
\delta C_\mu&=\partial_\mu\Lambda,\qquad
\delta E_{c\,\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]},\qquad
\delta B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}
-\frac12\Lambda G_{\mu\nu}-\frac g2\Lambda_{\mu\nu}.
\end{aligned}\tag{GG04a}
```

```math
T_{ab}=\frac1{8\sigma^2}\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right),
\qquad
T_{ab}\big|_{\text{explicit }gE_c}=\frac g{96\sigma^2}
\varepsilon_{abcde}E_c{}^{cde}.
\tag{GG04b}
```

### GG05 — Full gauged defining-vector derivative and inherited connections

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\frac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=\left(\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\psi^i-V_\mu{}^{ij}\psi_j
+\frac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\psi_\mu^i\\
&\quad+\frac i{4\sigma}\psi_{\mu j}\bar\psi^i\psi^j
-\frac g{2\sigma}L_c^{ij}\psi_{\mu j}
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i.
\end{aligned}\tag{GG05}
```

Use D02 for the full box and W04 for D(T), D(chi), D(D), with the
GG composites in every occurrence. R01–R03 and R05/G01 remain the full
connection/curvature definitions, evaluated with GG03–GG04. GC15 displays
all terms of chi after inserting GG05; GC16–GC24 print the box, matter
and curvature derivatives, dependent connections and compensator derivatives.
Do not use an ungauged chi or T inside a hatted curvature.

### GG06 — Gauged density endpoint and checks

GA24 in the gauged calculation explicitly inserts FM01–FM04 and the
gauged defining vector into A01/A02. It has 73 grouped outer terms,
or 87 after its displayed product rules and bilinear flip. No fermion or
coupling expansion is used. Full covariants are retained as defined
objects; this is not a primitive-field polynomial or a nonlinear SUSY proof.

The additional explicit Y couplings have coefficients
`-ig/(8sigma)`, `-128ig/(3sigma)`, `-8g/(3sigma)` multiplying
`L_c RR`, `L_c chi chi`, and `L_c R(V)T`. All other gauging dependence
is in GG03–GG05 and its induced derivatives/curvatures. The full density
can contain g³ and g⁴; GC31 displays a nonzero test sector.

[verify_gauged_weyl_action.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_gauged_weyl_action.py) checks the unchanged map, new
coefficients, all 73 terms, the exact g=0 density, Y² and chi/D constraints,
chi's connection expansion and the new couplings on six Grassmann samples.
The source reports PASS for these checks. They do not establish full Weyl-map laws,
current conservation or action-level reality/SUSY invariance.
