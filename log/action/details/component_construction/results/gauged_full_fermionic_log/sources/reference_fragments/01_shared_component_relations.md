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
Use $`(L_{\log}^{ij},\varphi_{\log}^i,E_{\log a},N_{\log})`$ for the **LOG composite** after
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
\not{\mathcal D}=\gamma^a\mathcal D_a.
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
The source constraint consequences include $`\widehat R(D)=0`$ and the full Lorentz-curvature Bianchi identity. They do **not** justify symmetrizing the locked full primed Ricci $`\mathcal R_{\mu\nu}`$ in R03 or its dependent $`f_{ab}`$ at fermionic order. The earlier local statement doing so was corrected by the [ordered-connection audit](../step7/supercovariant/equivalence/README.md); only the bosonic specialization used there is symmetric. Keep the primed Ricci and $`f`$ indices ordered.
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
-\tfrac i2\not{\mathcal D}\sigma\epsilon^i
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
+\tfrac i8\gamma^{ab}\not{\mathcal D}T_{ab}\epsilon^i
-\tfrac i8\gamma^a\mathcal D^bT_{ab}\epsilon^i\\
&\quad-\tfrac14\gamma^{abcd}T_{ab}T_{cd}\epsilon^i+\tfrac16T^2\epsilon^i
+\tfrac14\gamma\!\cdot\!T\eta^i,\\
\delta D&=\bar\epsilon\not{\mathcal D}\chi
-\tfrac{5i}{3}\bar\epsilon\gamma\!\cdot\!T\chi-i\bar\eta\chi,
\qquad T^2=T_{ab}T^{ab}.
\end{aligned}\tag{W03}
```

$`T,\chi,D`$ may be treated as Standard-Weyl covariants in the Standard-Weyl LOG
construction; in the gauged DW theory use GG03–GG05, not new fields.

### W04 — Explicit derivatives; OP(2.2),(2.12), with X02/X09

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\tfrac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=D_\mu^{(0)}\psi^i
+\tfrac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\tfrac i2\not{\mathcal D}\sigma\psi_\mu^i
+\tfrac i4\sigma^{-1}\psi_{\mu j}\bar\psi^i\psi^j
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i,\\
\mathcal D_\mu T_{ab}&=\partial_\mu T_{ab}-b_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}-\tfrac i2\bar\psi_\mu\gamma_{ab}\chi
+\tfrac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q),\\
\mathcal D_\mu\chi^i&=(\partial_\mu-\tfrac32b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\chi^i
-V_\mu{}^{ij}\chi_j-\tfrac14\psi_\mu^iD
+\tfrac1{64}\gamma\!\cdot\!\widehat R^{ij}(V)\psi_{\mu j}\\
&\quad-\tfrac i8\gamma^{ab}\not{\mathcal D}T_{ab}\psi_\mu^i
+\tfrac i8\gamma^a\mathcal D^bT_{ab}\psi_\mu^i
+\tfrac14\gamma^{abcd}T_{ab}T_{cd}\psi_\mu^i
-\tfrac16T^2\psi_\mu^i-\tfrac14\gamma\!\cdot\!T\phi_\mu^i,\\
\mathcal D_\mu D&=(\partial_\mu-2b_\mu)D
-\bar\psi_\mu\not{\mathcal D}\chi
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
&+\tfrac13[\not{\mathcal D}(\gamma\!\cdot\!T)\gamma_\mu
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
-\tfrac13\gamma_{[a}\not{\mathcal D}(\gamma\!\cdot\!T)\gamma_{b]}
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
\widehat R_{\mu\nu}(S)&=-i\not{\mathcal D}\widehat R_{\mu\nu}(Q)
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

### H02 — Tangent strength variations; W(3.27), OP(2.8), X03/X04

```math
\begin{aligned}
\delta\widehat G_{ab}={}&-\tfrac i2\sigma\bar\epsilon\widehat R_{ab}(Q)
-\bar\epsilon\gamma_{[a}\mathcal D_{b]}\psi
+i\bar\epsilon\gamma_{[a}\gamma\!\cdot\!T\gamma_{b]}\psi
+i\bar\eta\gamma_{ab}\psi,\\
\delta\widehat H_{abc}={}&-\tfrac34\sigma^2\bar\epsilon\gamma_{[a}\widehat R_{bc]}(Q)
+\tfrac{3i}{2}\sigma\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi
+\tfrac{3i}{2}\bar\epsilon\gamma_{[ab}\psi\mathcal D_{c]}\sigma\\
&-\tfrac32\sigma\bar\epsilon\gamma_{[a}\gamma\!\cdot\!T\gamma_{bc]}\psi
-\tfrac32\bar\epsilon\gamma_{[a}\widehat G_{bc]}\psi
-\tfrac32\sigma\bar\eta\gamma_{abc}\psi.
\end{aligned}\tag{H02}
```

The $`\sigma`$ in the second line is the X03 source-derived repair.
These are tangent laws. For coordinate strengths use G04 to restore the
frame terms; OP's printed world-index $`\delta\widehat G_{\mu\nu}`$ must not
be read as the ordinary world variation with those terms omitted.

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
\chi^i={}&\tfrac i8\sigma^{-1}\not{\mathcal D}\psi^i
+\tfrac i{16}\sigma^{-2}\not{\mathcal D}\sigma\psi^i
-\tfrac1{32}\sigma^{-2}\gamma\!\cdot\!\widehat G\psi^i
+\tfrac14\sigma^{-1}\gamma\!\cdot\!T\psi^i
+\tfrac i{32}\sigma^{-3}\psi_j\bar\psi^i\psi^j,\\
D={}&\tfrac14\sigma^{-1}\Box^c\sigma
+\tfrac18\sigma^{-2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\tfrac1{16}\sigma^{-2}\widehat G_{ab}\widehat G^{ab}
-\tfrac18\sigma^{-2}\bar\psi\not{\mathcal D}\psi\\
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
\delta\varphi^i&=-\tfrac i2\not{\mathcal D}L^{ij}\epsilon_j
-\tfrac i2\gamma^aE_a\epsilon^i+\tfrac12N\epsilon^i
-\gamma\!\cdot\!T L^{ij}\epsilon_j+3L^{ij}\eta_j,\\
\delta E_a&=-\tfrac i2\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
-2\bar\epsilon\gamma^b\varphi T_{ba}-2\bar\eta\gamma_a\varphi,\\
\delta N&=\tfrac12\bar\epsilon\not{\mathcal D}\varphi
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
+\tfrac i2\not{\mathcal D}L^{ij}\psi_{\mu j}
+\tfrac i2\gamma^aE_a\psi_\mu^i\\
&\quad-\tfrac12N\psi_\mu^i+\gamma\!\cdot\!T L^{ij}\psi_{\mu j}
-3L^{ij}\phi_{\mu j},\\
\mathcal D_\mu E_a&=(\partial_\mu-4b_\mu)E_a+\omega_{\mu ab}E^b
+\tfrac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
+2\bar\psi_\mu\gamma^b\varphi T_{ba}+2\bar\phi_\mu\gamma_a\varphi,\\
\mathcal D_\mu N&=(\partial_\mu-4b_\mu)N
-\tfrac12\bar\psi_\mu\not{\mathcal D}\varphi
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
-\tfrac i2\not{\mathcal D}\rho\epsilon^i+\rho\gamma\!\cdot\!T\epsilon^i
-Y^{ij}\epsilon_j+\rho\eta^i,\\
\delta Y^{ij}&=-\tfrac12\bar\epsilon^{(i}\not{\mathcal D}\lambda^{j)}
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
+\tfrac i2\not{\mathcal D}\rho\psi_\mu^i+Y^{ij}\psi_{\mu j}
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
At nonzero g replace this ungauged Y slot by LOG-B02. It is distinct from
the LOG linear composite and from a linear-to-vector compensator construction. Use V01/W02 rather than the misprinted restatement (5.14)–(5.15).

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
in a composite LOG linear multiplet. Use the full first identity in A02a.
The later invariance test must include this completion. The optional
potential formulation records the literal-source conflict X10; the generic linear-potential law is now fixed by the derived (1,-3) coefficients and complete superform proof.

## Source-derived repairs and quarantined interfaces

These are project interpretations, not published errata. Original source formulas remain in the appendix. X11 describes an already fixed donor transcription; X08’s M labels belong to the donor Weyl-map history, not LOG inputs.

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
checked independently in [verify_conventions.py](../../../../../../../../computations/weyl_fermionic/src/reference_checks/verify_conventions.py).

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

### X11 — R05 index ordering and S-invariance

W(3.23), printed p.21/PDF p.22, fixes the R05 ordering as
$`+\frac{16}{3}T_{[a}{}^c\gamma_{b]c}\eta^i`$.
The alternative ordering
$`+\frac{16}{3}T^c{}_{[a}\gamma_{b]c}\eta^i`$
has the opposite sign because
$`T_a{}^c=\eta^{cd}T_{ad}=-\eta^{cd}T_{da}=-T^c{}_a`$.
The adopted ordering preserves $`\gamma^a\delta_S\widehat R_{ab}(Q)=0`$
and the cancellation in $`\delta_S L^{ij}`$. The [fermionic-map derivation](../../../../../../../../computations/weyl_fermionic/derivations/fermionic-map.md)
and [S-invariance checker](../../../../../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_map_s_invariance.py) give the algebra and the opposite-sign control.

## Gauged realization of the shared component covariants

Use these instead of the ungauged realization when g is nonzero. The project-derived full restoration is shown in GC01–GC24 below; its use in the Gold LOG multiplet is through the explicit source-frame bridge.

### GG01 — Full improved-vector constraints

W(5.10)–(5.14), printed27/PDF28, in the source linked by the [bibliography](../../../../../../../../references/bibliography.md). These source constraint names
are not new independent fields. Unlike truncated CO formulas, these are
full supercovariant expressions.

```math
\begin{aligned}
S^{ij}&=2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j,\\
\Gamma^i&=i\sigma\not{\mathcal D}\psi^i
+\frac i2\not{\mathcal D}\sigma\psi^i
-\frac14\gamma\!\cdot\!\widehat G\psi^i
+Y^{ij}\psi_j+2\sigma\gamma\!\cdot\!T\psi^i-8\sigma^2\chi^i,\\
\mathcal C&=-\frac14\widehat G_{ab}\widehat G^{ab}
-\frac12\bar\psi\not{\mathcal D}\psi
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
\chi^i={}&\frac i{8\sigma}\not{\mathcal D}\psi^i
+\frac i{16\sigma^2}\not{\mathcal D}\sigma\psi^i
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
-\frac1{8\sigma^2}\bar\psi\not{\mathcal D}\psi
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
+\frac i2\not{\mathcal D}\sigma\psi_\mu^i\\
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

