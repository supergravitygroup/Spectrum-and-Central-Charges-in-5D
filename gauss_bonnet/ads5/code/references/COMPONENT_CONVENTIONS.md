# Full field, variation, curvature and supercovariant-derivative reference

This is the component reference used by the Gauss–Bonnet calculations.
The concise [CONVENTIONS.md](CONVENTIONS.md) remains the convention lock;
the formulas below specify the LOG and Weyl component inputs,
including the superform and full covariant-derivative dictionary.

The component derivations retain
their intermediate steps. No field equation, vacuum choice, auxiliary elimination
or additional fluctuation gauge is introduced here.

## How to read the source layers

- **Common component frame:** C/G/W/R/H/D/L/V/A relations. These define the fields,
  Q/S/K transformations, ordinary and supercovariant curvatures, and complete
  covariantization rules before source gauge fixing. H01, H03, D01 and V03 give the ungauged formulas; H02 also includes
  the gauged linear-compensator contribution used in the product calculation.
- **Gauged component frame:** GG/GC relations replace the ungauged defining-vector
  composites and form strengths. They retain the independent linear compensator.
  The generic Standard-Weyl, vector and linear transformation laws remain the
  laws to covariantize; do not identify a composite with an independent field.
- **Gold native frame:** the superspace derivative towers and C24 appendix use
  their native Clifford algebra, spinor slots and generators. Apply the published
  conversion tables and the separately derived linear-slot bridge before mixing
  these expressions with component formulas.
- **Source gauge:** LOG-G and SC7/SC7D apply at the stated gauge and fermion order.
  The derivative dictionary includes the first and second derivatives of the
  dilatino, scalar Hessians, conformal boxes, inverse powers and ordered higher
  derivatives. Differentiate fully before imposing the gauge.
- **Corrections:** X01–X11, LOG-S1, FI24 and G-C24-A1l-repair retain their project-derived
  status. Literal L04 and literal C24 (A.1l) are comparison records; use the
  operational repaired formulas. The 2026-09-25 LOG certificate takes precedence
  over older construction-stage paragraphs within its retained-order scope.

Inside an excerpt, “this branch,” its lock name, local section number, and
certification statement refer to the **donor calculation**. They do not declare
a GB result. Links have been rebased to their original active files; frozen
versions define the component inputs. Bare source filenames identify the reference equations.
The adopted Weyl composite map and its independent open checks remain in
SOURCE_LOCK.md; this reference extracts the shared calculus,
not a new proof of that invariant's multiplet laws or normalization.

## Coverage and exactness

| Component category | Explicit material here | Qualification |
|---|---|---|
| All fields | Vielbein, gravitino, D/S/K/Lorentz/SU(2) connections, DW scalar/dilatino/forms, T/chi/D composites, linear compensator and defining vector; weights and Gold projections | Source-gauge identities do not remove derivative contributions |
| Variations | Q/S/K laws, form gauges, frame/gamma/epsilon/density variations, derivative chain rule, curvature variations, gauge compensators and operational three-form law | Full delta-phi, delta-f and delta-Lorentz/Weyl curvatures are exact defining variations where that is what the donor establishes |
| Curvatures | Ordinary Riemann/Ricci/Weyl; torsion, primed and full Q/M/V/S curvatures; G/H strengths and Bianchi identities; superspace torsion and all curvature slots | Keep full primed Ricci and f indices ordered; ungauged Bianchi identities retain their scope |
| Derivatives | Full D/M/U/Q/S/K covariantization; explicit matter, multiplet and curvature derivatives; gauged closure; ordered gauge-fixed Hessians and boxes; Gold spinor-derivative towers and full commutator appendix | Some higher derivatives are defined by ordered composition; a defining recipe is not an independently expanded polynomial |
| Functional variation | Left Grassmann variations, Majorana dependence, fermion degree, expansion factorials, boundary/equality rules | Detailed branch convention is CONVENTIONS.md section 8; no LOG-specific Euler operator or mass is imported |

For functional variations, put the independent odd variation on the left:

```math
\delta S=\int d^5x\,\delta\Psi^A\frac{\delta^L S}{\delta\Psi^A}.
```

The Majorana bar is dependent and linear: vary both factors of a quadratic
bilinear, then apply the locked flips and integration by parts. A factor of two
for a diagonal Majorana term follows only after this symmetrization; it must not
be inserted blindly for a mixed term. The parameter-contracted SUSY variation
is even, so its product rule has no extra graded sign. A bare odd supersymmetry
generator has a graded product rule. Bulk variations are initially compactly
supported. No AdS boundary condition or numerical background is selected here.

**Verification scope:** extraction fidelity, rendering, source integrity and the
inherited common-algebra checks. This reference does not certify full nonlinear
closure, resolve the full Weyl-to-target normalization, or derive the GB spectrum.

## Navigation

- [Field inventory and independent/dependent status](COMPONENT_CONVENTIONS.md#fields)
- [Indices, spinors, Clifford algebra, Fierz rules and weights](COMPONENT_CONVENTIONS.md#algebra)
- [Geometry, full covariantization and variation of frames](COMPONENT_CONVENTIONS.md#geometry)
- [Weyl and Dilaton-Weyl transformations and derivatives](COMPONENT_CONVENTIONS.md#weyl-laws)
- [Connections, curvatures and their variations](COMPONENT_CONVENTIONS.md#curvatures)
- [Ungauged forms, Bianchi identities and full DW composites](COMPONENT_CONVENTIONS.md#forms)
- [Linear and vector multiplets, full derivatives and BF current](COMPONENT_CONVENTIONS.md#multiplets)
- [Inherited component repairs and quarantined formulas](COMPONENT_CONVENTIONS.md#repairs)
- [Gauged constraints, composites, forms and transformations](COMPONENT_CONVENTIONS.md#gauged-map)
- [Full gauged composite derivation and derivative closure](COMPONENT_CONVENTIONS.md#gauged-closure)
- [Gold supergeometry and elementary derivative towers](COMPONENT_CONVENTIONS.md#superspace)
- [Projections and published Gold/component conversion tables](COMPONENT_CONVENTIONS.md#projection)
- [Derived linear-slot bridge and corrected ordinary current](COMPONENT_CONVENTIONS.md#linear-bridge)
- [Full superform pullback and operational three-form variation](COMPONENT_CONVENTIONS.md#potential)
- [Source gauge, compensating transformations and bosonic specialization](COMPONENT_CONVENTIONS.md#source-gauge)
- [Equality, integrations by parts and boundary conventions](COMPONENT_CONVENTIONS.md#boundary)
- [Ordered gauge-fixed derivatives, Hessians and conformal boxes](COMPONENT_CONVENTIONS.md#gauge-derivatives)
- [Why full primed Ricci and the K connection remain ordered](COMPONENT_CONVENTIONS.md#ordered-curvature)
- [Literal complete superspace commutator appendix](COMPONENT_CONVENTIONS.md#source-appendix)

The searchable [relation index](COMPONENT_INDEX.md) gives every equation tag and source span.

<a id="fields"></a>

## Field inventory and independent/dependent status

**Extraction:** results/ungauged_full_fermionic_weyl2/FIELD_LEDGER.md, lines 1–25; frozen input. Source wording follows; its scope labels remain in force.

**Gauged use:** the final defining-vector Y formula below is its g=0 specialization. Use GG03/GC04 for nonzero g.

## Field ledger

No propagating/auxiliary conclusion is inherited from a two-derivative EOM.

| Fields | Role in construction | Later treatment |
|---|---|---|
| e_mu^a, psi_mu^i | Vielbein and gravitino | Retain; derive diffeomorphism/local-SUSY constraints |
| b_mu, V_mu^ij | Dilatation and SU(2) connections | Source gauge b=0 later; retain V and its curvature |
| sigma, C_mu, B_munu, psi^i | Dilaton-Weyl matter fields | Defining-vector identification; later sigma=1, psi=0 |
| T_ab, chi^i, D | Standard-Weyl fields | Replace by full off-shell DW composites, not by auxiliary EOMs |
| omega_mu^ab, phi_mu^i, f_mu^a | Dependent Lorentz, S and K connections | Include torsion, fermions and convention constraints |
| L^ij, varphi^i, E_a, N | Original linear compensator | Required for Poincare two-derivative sector; retain varphi and N |
| E_munurho | Potential for constrained E_a | Vary potential/constraint consistently; not an unconstrained vector |
| Weyl composite linear multiplet | Built from Weyl fields/curvatures | Full four slots required in BF, distinct from original compensator |
| rho,A_mu,lambda^i,Y^ij | BF vector slots | Identify via OP (5.16), not a new physical vector multiplet |

The defining-vector map is
`rho=sigma`, `A_mu=C_mu`, `lambda^i=psi^i`,
`Y^ij=(i/4)sigma^-1 bar(psi)^(i psi^j)`
[Özkan–Pang (5.16), PDF p.20]. It is to be applied after the native-source
convention bridge. The linear-compensator fields are not identified with
the Weyl composite linear multiplet's four components.

Authoritative definitions and weights: master C02/C06; connections R01–R04;
DW map D01–D02; linear multiplet L01–L04; defining vector V03.

<a id="algebra"></a>

## Indices, spinors, Clifford algebra, Fierz rules and weights

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 132–307; frozen input. Source wording follows; its scope labels remain in force.

#### C01 — Geometry and orientation

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

#### C02 — SU(2) and names

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

#### C03 — Majorana bar and Grassmann rules

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

#### C04 — Clifford algebra and full contractions

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

#### C05 — Fierz and doublet identities

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

#### C06 — Weights, degree and units

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

<a id="geometry"></a>

## Geometry, full covariantization and variation of frames

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 308–432; frozen input. Source wording follows; its scope labels remain in force.

### 2. Geometry and the meaning of a derivative

#### G01 — Full covariantization

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

#### G02 — Lorentz and metric curvature

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

#### G03 — Conventional constraints and supercovariantization

```math
R_{\mu\nu}{}^a(P)=2\partial_{[\mu}e_{\nu]}{}^a
+2\omega_{[\mu}{}^{ab}e_{\nu]b}+2b_{[\mu}e_{\nu]}{}^a
-\frac12\bar\psi_{[\mu}\gamma^a\psi_{\nu]}=0,
\quad \gamma^\mu\widehat R_{\mu\nu}(Q)=0,
\quad e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0.
\tag{G03a}
```

These solve for $`\omega,\phi,f`$, respectively; they are not field equations.
The source constraint consequences include $`\widehat R(D)=0`$ and the full Lorentz-curvature Bianchi identity. They do **not** justify symmetrizing the locked full primed Ricci $`\mathcal R_{\mu\nu}`$ in R03 or its dependent $`f_{ab}`$ at fermionic order. Only the bosonic specialization has symmetric Ricci tensor. Keep the primed Ricci and $`f`$ indices ordered.
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

#### G04 — Frames, gamma matrices and scalar density variations

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

<a id="weyl-laws"></a>

## Weyl and Dilaton-Weyl transformations and derivatives

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 433–519; frozen input. Source wording follows; its scope labels remain in force.

### 3. Weyl transformations and component derivatives

#### W01 — Common Weyl gauge fields; OP(2.1), W(4.1)

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

#### W02 — DW fields; OP(2.1)

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

#### W03 — Standard-Weyl matter; OP(2.11), W(3.16)

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

#### W04 — Explicit derivatives; OP(2.2),(2.12), with X02/X09

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

<a id="curvatures"></a>

## Connections, curvatures and their variations

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 520–738; frozen input. Source wording follows; its scope labels remain in force.

### 4. Connections, curvatures and their variations

#### R01 — Spin connection and gravitino curvature; OP(2.5),(2.6)

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

#### R02 — R-symmetry curvature; OP(2.7)

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

#### R03 — Working Lorentz curvature and K connection; X01 is mandatory

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

#### R04 — Dependent connection variations; W(3.2),(3.20),(3.21)

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

#### R05 — Tangent gravitino-curvature variation; W(3.23)

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

#### R06 — Tangent SU(2)-curvature variation and eliminated S curvature

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

#### R07 — Exact Lorentz/Weyl-curvature variation recipe

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

<a id="forms"></a>

## Ungauged forms, Bianchi identities and full DW composites

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 739–835; frozen input. Source wording follows; its scope labels remain in force.

### 5. Gauge forms and full ungauged DW composites

#### H01 — Strengths and form gauges; OP(2.3),(2.4)

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

#### H02 — Tangent strength variations; W(3.27), OP(2.8), X03/X04

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
+\tfrac32\bar\epsilon\gamma_{[a}\widehat G_{bc]}\psi
-\tfrac32\sigma\bar\eta\gamma_{abc}\psi
+\tfrac g2\bar\epsilon\gamma_{abc}\varphi.
\end{aligned}\tag{H02}
```

The $`\sigma`$ factor in the second line follows from X03. The isolated
$`G\psi`$ and $`g\varphi`$ terms are fixed by the potential variation
in [the product-family input definitions](../../../product_backgrounds/supersymmetric_ads3_sigma2/fermionic_action_inputs.md), F24.3–F24.4.
These are tangent laws. For coordinate strengths use G04 to restore the
frame terms; OP's printed world-index $`\delta\widehat G_{\mu\nu}`$ must not
be read as the ordinary world variation with those terms omitted.

#### H03 — Supercovariant Bianchi identities; W(3.28)

```math
\mathcal D_{[a}\widehat G_{bc]}=\tfrac12\bar\psi\gamma_{[a}\widehat R_{bc]}(Q),
\qquad
\mathcal D_{[a}\widehat H_{bcd]}=\tfrac34\widehat G_{[ab}\widehat G_{cd]}.
\tag{H03}
```

The spinor on the first right-hand side is the dilatino, not $`\psi_a`$.
The bosonic limit of the second identity agrees with $`dH=G\wedge G/2`$.

#### D01 — Complete auxiliary composites; OP(2.9)

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

#### D02 — Superconformal Laplacian; OP(2.10)

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

<a id="multiplets"></a>

## Linear and vector multiplets, full derivatives and BF current

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 836–1016; frozen input. Source wording follows; its scope labels remain in force.

### 6. Linear and defining-vector multiplets

#### L01 — Matching laws; OP(2.18)

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

#### L02 — Full derivatives; OP(2.19), G01

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

#### L03 — Constrained form; OP(2.20)–(2.23)

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

#### L04 — Literal potential transformations; OP(2.24), NOT an operational pair

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

#### V01 — Abelian vector laws; OP(2.13) with g=0

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

#### V02 — Vector derivatives and curvature; OP(2.14)–(2.16)

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

#### V03 — Defining vector; OP(5.16),(5.17)

```math
(\rho,A_\mu,\lambda^i,Y^{ij})
=\left(\sigma,C_\mu,\psi^i,\tfrac i4\sigma^{-1}\bar\psi^{(i}\psi^{j)}\right).
\tag{V03}
```

Its Y-slot transforms as V01 with $`(\rho,\lambda)=(\sigma,\psi)`$ by
OP(5.17). It is not an independent auxiliary field in this identification.
At nonzero g replace this ungauged Y slot by LOG-B02. It is distinct from
the LOG linear composite and from a linear-to-vector compensator construction. Use V01/W02 rather than the misprinted restatement (5.14)–(5.15).

#### A01 — Full vector–linear density; OP(3.1)

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

#### A02 — Operational density in terms of E_a; OPall(3.1)–(3.2)

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

<a id="repairs"></a>

## Inherited component repairs and quarantined formulas

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 1017–1168; frozen input. Source wording follows; its scope labels remain in force.

### Source-derived repairs and quarantined interfaces

These are project interpretations, not published errata. Original source formulas remain in the appendix. X11 describes an already fixed donor transcription; X08’s M labels belong to the donor Weyl-map history, not LOG inputs.

#### X01 — Lorentz-curvature errors in OP(2.7)

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

#### X02 — Chi weight in OP(2.12)

Literal: $`(\partial_\mu-7b_\mu/2+\cdots)\chi`$.
Working W04: $`(\partial_\mu-3b_\mu/2+\cdots)\chi`$.
W Table3 gives $`w(\chi)=3/2`$, also fixed by
$`\delta T\sim\bar\epsilon\chi`$ with $`w(T)=1,w(\epsilon)=-1/2`$.
The printed derivative would leave
$`-2(\partial_\mu\Lambda_D)\chi`$ under a local dilatation.
The $`7/2`$ weight belongs to $`\varphi`$, not $`\chi`$.

#### X03 — Missing sigma in both short H variations

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

#### X04 — World/tangent and epsilon typography

W(3.27) gives tangent $`\delta\widehat G_{ab}`$; OP(2.8) prints the same
shape with world indices. Use H02 as the tangent law and G04 for actual
coordinate variations. Similarly W(A.12)'s upper-world epsilon notation
includes a density factor. Our tensor/density definitions are C01.
They must be used consistently in A01 and L03; no extra determinant may
be inferred from the source typography.

#### X05 — Partial dependent-connection variations

W(3.21) expressly prints M-dependent additions, with an ellipsis; W(3.22)
expressly prints only the M-dependent S variation of the f trace.
Use R04b and R04d, differentiated from complete dependent definitions,
for full variations. A sum of the bare algebra and the printed additions
can miss field-dependent structure-function contributions.

#### X06 — Repeated density and vector formulas

OP(3.2) prints $`\psi^j`$ in the term that is $`\lambda^j`$ in (3.1);
integration by parts cannot change a gaugino species. Use A01.
OP(5.14) restates $`\delta A_\mu`$ with $`\sigma`$ instead of $`\rho`$ and a
missing $`i`$; OP(5.15) drops the $`i`$ in $`\delta C_\mu`$.
Use the unambiguous original OP(2.13)/(2.1), V01/W02.

#### X07 — Equivalent conventions that must not be repaired

The opposite-looking f/Ricci signs are identical because of the two Ricci
index contractions, R03. The opposite-looking epsilon-H signs in the
auxiliary T map are identical after reversing three H indices, D01.
W(A.14) dots are full contractions, C04; its last factorial literally
$`(n-5)!`$ is a typo for $`(5-n)!`$, as required by the dual tensor's rank.
C03 distinguishes fixed-index and SU(2)-contracted bilinear flips.

#### X09 — Tensor-derivative index/sign mismatch

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
checked independently in [verify_conventions.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_conventions.py).

#### X10 — Potential-law conflict; operational E_a route

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
The selected map completion and density construction use the explicit
constrained-current route. The product calculation uses the potential
variation specified by GG04 and F24.3–F24.4.

#### X11 — Index ordering in the S variation

R05 uses W(3.23)'s term
$`+\frac{16}{3}T_{[a}{}^c\gamma_{b]c}\eta^i`$.
The ordering matters because
$`T_a{}^c=\eta^{cd}T_{ad}=-\eta^{cd}T_{da}=-T^c{}_a`$.
This ordering preserves $`\gamma^a\delta_S\widehat R_{ab}(Q)=0`$
and the cancellation in $`\delta_S L^{ij}`$.

<a id="gauged-map"></a>

## Gauged constraints, composites, forms and transformations

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 1169–1308; frozen input. Source wording follows; its scope labels remain in force.

### Gauged realization of the shared component covariants

Use these instead of the ungauged realization when g is nonzero. The project-derived full restoration is shown in GC01–GC24 below; its insertion into the Gold LOG multiplet uses the explicit source-frame bridge below.

#### GG01 — Full improved-vector constraints

W(5.10)–(5.14), printed27/PDF28, in the source linked by the [bibliography](../../../../references/bibliography.md). These source constraint names
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

#### GG02 — Gauged constraint multiplet

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

#### GG03 — Complete gauged Y, chi and D

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

#### GG04 — Gauged forms and T

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

#### GG05 — Full gauged defining-vector derivative and inherited connections

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

<a id="gauged-closure"></a>

## Full gauged composite derivation and derivative closure

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 1309–1821; frozen input. Source wording follows; its scope labels remain in force.

### Full gauged composite derivation and derivative closure

Frozen from the project gauged Weyl note; only shared realization formulas GC01–GC24 and GA01–GA03 are reused. No Weyl-specific multiplet component or completed-action claim is imported. `master` references below mean the shared equations already displayed in this file.

#### 3.1. Primary source inputs and their exact scope

The local Weyl-multiplet paper, W(5.10)–(5.14), printed p.27/PDF p.28,
gives the following **full supercovariant** improved-vector constraints.
We write its scalar constraint as $`\mathcal C`$ to distinguish it from
$`C_\mu`$; $`S^{ij},\Gamma^i,\mathcal C,\mathcal H_a`$ below are temporary
source constraint names, not additional physical fields:

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
\end{aligned}\tag{GC01}
```

Their Q laws, W(5.11),(5.13), are

```math
\begin{aligned}
\delta_Q S^{ij}&=i\bar\epsilon^{(i}\Gamma^{j)},\\
\delta_Q\Gamma^i&=-\frac i2\gamma^a\mathcal D_aS^{ij}\epsilon_j
-\frac i2\gamma^a\mathcal H_a\epsilon^i
+\frac12\mathcal C\epsilon^i-\gamma\!\cdot\!T S^{ij}\epsilon_j.
\end{aligned}\tag{GC02}
```

These have precisely the same component normalization as the compensator
Q laws in master L01. CO(5.2) fixes the gauged lowest constraint as
$`S^{ij}+gL_c^{ij}=0`$. This determines the spinor and scalar deformations
without importing the cubic/quartic omissions of the truncated CO formulas.
The source locator is W(5.10)–(5.14), printed27/PDF28; see the [bibliography](../../../../references/bibliography.md).

CO(5.5)–(5.8), PDF/printed pp.16–17, fixes the form sector:

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
\end{aligned}\tag{GC03}
```

The last line is an ordinary bosonic form gauge transformation, not an
adoption of the quarantined literal SUSY potential laws in master L04.

#### 3.2. The density, bridge and gauged defining vector

Master A01–A02 gives

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\frac12\bar\psi_m^i\gamma^m\lambda^jL_{ij}+A_aP^a
+\rho N+\frac\rho2\bar\psi_m\gamma^m\varphi
+\frac{i\rho}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{ij}.
\end{aligned}\tag{GA01}
```

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{GA02}
```

The first three defining-vector identifications remain
$`(\rho,A_\mu,\lambda^i)=(\sigma,C_\mu,\psi^i)`$.
Section 4.1 derives its fourth slot exactly, including its fermionic part.
The same full density is used at nonzero g; the gauging enters its
composite vector and background fields.

### 4. Detailed Derivation

#### 4.1. Solve the lowest gauged constraint and vary it

<!-- DONOR_CONVENTION_CONTEXT: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5, gauged_extension=CO-GAUGED-DW-FULL-COVARIANTS-v1 -->

From CO(5.2) and GC01,

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL_c^{ij}=0
\quad\Longrightarrow\quad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac{g}{2\sigma}L_c^{ij}.
\tag{GA03}
```

The factor $`1/(2\sigma)`$ multiplies both terms on the right of the
first equation. The scalar fixed-index flip makes the spinor bilinear
symmetric, so its written symmetrization changes no coefficient.
Since g is constant, GC02 and L01 give

```math
\delta_Q(S^{ij}+gL_c^{ij})
=i\bar\epsilon^{(i}\Gamma^{j)}+ig\bar\epsilon^{(i}\varphi_c^{j)}
=i\bar\epsilon^{(i}(\Gamma^{j)}+g\varphi_c^{j)}).
\tag{GC04}
```

The next constraint is therefore $`\Gamma^i+g\varphi_c^i=0`$.
Vary it and display every compensator term:

```math
\begin{aligned}
\delta_Q(\Gamma^i+g\varphi_c^i)={}&
-\frac i2\gamma^a\mathcal D_aS^{ij}\epsilon_j
-\frac i2\gamma^a\mathcal H_a\epsilon^i
+\frac12\mathcal C\epsilon^i-\gamma\!\cdot\!T S^{ij}\epsilon_j\\
&-\frac{ig}{2}\gamma^a\mathcal D_aL_c^{ij}\epsilon_j
-\frac{ig}{2}\gamma^aE_{ca}\epsilon^i
+\frac g2N_c\epsilon^i-g\gamma\!\cdot\!T L_c^{ij}\epsilon_j\\
={}&-\frac i2\gamma^a\mathcal D_a(S^{ij}+gL_c^{ij})\epsilon_j
-\frac i2\gamma^a(\mathcal H_a+gE_{ca})\epsilon^i
+\frac12(\mathcal C+gN_c)\epsilon^i
-\gamma\!\cdot\!T(S^{ij}+gL_c^{ij})\epsilon_j.
\end{aligned}\tag{GC05}
```

Thus the scalar and vector constraints are $`\mathcal C+gN_c=0`$ and
$`\mathcal H_a+gE_{ca}=0`$. This argument uses the full source covariants;
it does not discard higher fermions when adding the compensator multiplet.

It also checks the defining-vector Y law. Applying the chain rule to GA03
and comparing with the independent-vector transformation gives

```math
\begin{aligned}
2\sigma(\delta_QY^{ij}_{\rm composite}-\delta_QY^{ij}_{\rm vector})
&=-i\bar\epsilon^{(i}(\Gamma^{j)}+g\varphi_c^{j)})=0,\\
\delta_SY^{ij}_{\rm composite}&=\frac i2\bar\eta^{(i}\psi^{j)}.
\end{aligned}\tag{GC06}
```

For the first line, the variations of $`2\sigma Y^{ij}`$ other than
$`2\sigma\delta Y^{ij}`$ and those of $`-i\bar\psi^i\psi^j/2`$ are the
same on both sides of the defining constraint, leaving exactly the displayed
difference. For the second line, $`\delta_S\sigma=\delta_SL_c=0`$ and
$`\delta_S\psi^i=\sigma\eta^i`$: the two varied spinors in
$`i\bar\psi^{(i}\psi^{j)}/(4\sigma)`$ give
$`i(\bar\eta^{(i}\psi^{j)}+\bar\psi^{(i}\eta^{j)})/4 =i\bar\eta^{(i}\psi^{j)}/2`$ by the fixed-index scalar flip.

#### 4.2. Solve the spinor constraint, including its cubic term

Move $`-8\sigma^2\chi^i`$ to the other side of
$`\Gamma^i+g\varphi_c^i=0`$ and divide each term by $`8\sigma^2`$:

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\not{\mathcal D}\psi^i
+\frac i{16\sigma^2}\not{\mathcal D}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{8\sigma^2}Y^{ij}\psi_j
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac g{8\sigma^2}\varphi_c^i,\\
\frac1{8\sigma^2}Y^{ij}\psi_j
&=\frac i{32\sigma^3}(\bar\psi^i\psi^j)\psi_j
-\frac g{16\sigma^3}L_c^{ij}\psi_j.
\end{aligned}\tag{GC07}
```

The bilinear in the last line is even, so it commutes through $`\psi_j`$.
The full spinor composite, with no cubic remainder, is consequently

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\not{\mathcal D}\psi^i
+\frac i{16\sigma^2}\not{\mathcal D}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j\\
&-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i.
\end{aligned}\tag{GC08}
```

The last two terms reproduce the gauged part of CO(5.3), with its Y
substitution performed. The cubic term is supplied by the full GC01,
not inferred from the truncated two-derivative action.

#### 4.3. Solve the scalar constraint and expand every Y product

In $`\mathcal C+gN_c=0`$, move $`-4\sigma^2D`$ to the other side and divide
by $`4\sigma^2`$. The source coefficients become
$`-1/16,-1/8,1/4,1/8,1/4, i/4,-4i,-26/3,2,g/4`$, with the displayed
powers of sigma:

```math
\begin{aligned}
D={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{8\sigma^2}\bar\psi\not{\mathcal D}\psi
+\frac1{4\sigma^2}Y^{ij}Y_{ij}\\
&+\frac i{4\sigma^2}\bar\psi\gamma^{ab}\psi T_{ab}
-\frac{4i}{\sigma}\bar\psi\chi-\frac{26}{3}T_{ab}T^{ab}
+\frac2\sigma\widehat G_{ab}T^{ab}+\frac g{4\sigma^2}N_c.
\end{aligned}\tag{GC09}
```

Lower Y with the two epsilon tensors before multiplying. Both terms in
Y are even, and the lower triplet contraction is symmetric. Hence

```math
\begin{aligned}
Y^{ij}Y_{ij}
={}&\left(\frac i{4\sigma}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\right)
\left(\frac i{4\sigma}\bar\psi_i\psi_j-\frac g{2\sigma}L_{c\,ij}\right)\\
={}&-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{8\sigma^2}(\bar\psi^i\psi^j)L_{c\,ij}
-\frac{ig}{8\sigma^2}L_c^{ij}(\bar\psi_i\psi_j)
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}\\
={}&-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{4\sigma^2}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{GC10}
```

The first sign is $`i^2=-1`$. The two mixed terms have the same sign:
$`L_c^{ij}\bar\psi_i\psi_j=L_{c\,ij}\bar\psi^i\psi^j`$, since lowering
both indices contributes two epsilon tensors. No odd spinors are swapped.
Multiplying GC10 by $`1/(4\sigma^2)`$ and inserting it into GC09 gives

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
\end{aligned}\tag{GC11}
```

This includes the quartic term required by the g=0 master D01 and both
mixed Y products. The chi, box and gaugino derivative in this formula
are themselves the full gauged quantities; their fermions are not omitted.

#### 4.4. Solve the tensor relation and check the form gauge symmetry

CO(5.6) is $`\varepsilon_{abcde}\widehat H^{cde}/6 =8\sigma^2T_{ab}-\sigma\widehat G_{ab}-i\bar\psi\gamma_{ab}\psi/4`$.
Move its last two terms across and divide by $`8\sigma^2`$:

```math
T_{ab}=\frac1{8\sigma^2}\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right),
\qquad
T_{ab}\big|_{\text{explicit }gE_c}=\frac g{96\sigma^2}
\varepsilon_{abcde}E_c{}^{cde}.
\tag{GC12}
```

In the last expression the subscript c on E labels the compensator;
the superscript letters are its three tangent indices. The coefficient
is $`(1/8)(1/6)(1/2)=1/96`$, from GC03. Write the bosonic form definitions
with $`B=B_{\mu\nu}dx^\mu\wedge dx^\nu/2`$ and
$`E_c=E_{c\,\mu\nu\rho}dx^\mu\wedge dx^\nu\wedge dx^\rho/3!`$:

```math
\begin{aligned}
H&=dB+\frac12C\wedge G+\frac g2E_c,\qquad G=dC,\\
dH&=\frac12G\wedge G+\frac g2dE_c,\\
\delta H&=d\left(d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2\right)
+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2\\
&=-\frac12d\Lambda\wedge G-\frac12\Lambda\,dG
-\frac g2d\Lambda_2+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2=0.
\end{aligned}\tag{GC13}
```

The last equality uses $`dG=d^2C=0`$ and $`d^2\Lambda_1=0`$.
In components, dividing the four-form equation by four gives
$`\partial_{[\mu}H_{\nu\rho\sigma]} =3G_{[\mu\nu}G_{\rho\sigma]}/4 +g\partial_{[\mu}E_{c\,\nu\rho\sigma]}/2`$.
This checks the source factors independently. Its supercovariant form is
CO(5.5), interpreted with the complete constrained-vector realization.
No SUSY potential-law repair is assumed in this bosonic gauge check.

#### 4.5. Propagate the gauging through derivatives and connections

<!-- DONOR_CONVENTION_CONTEXT: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5, gauged_extension=CO-GAUGED-DW-FULL-COVARIANTS-v1 -->

Start with the full vector derivative, CO(2.16)/master V02, and insert GA03:

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
\end{aligned}\tag{GC14}
```

The connection term $`-gL_c^{ij}\psi_{\mu j}/(2\sigma)`$ is necessary
even if a later gauge sets the dilatino to zero. For clarity, insert all
terms of GC14 into the first term of GC08, not just its ordinary derivative:

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\gamma^\mu
\left[\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\psi^i-V_\mu{}^{ij}\psi_j\right]
+\frac i{32\sigma}\gamma^\mu\gamma\!\cdot\!\widehat G\psi_\mu^i
-\frac1{16\sigma}\gamma^\mu\not{\mathcal D}\sigma\psi_\mu^i\\
&-\frac1{32\sigma^2}\gamma^\mu\psi_{\mu j}\bar\psi^i\psi^j
-\frac{ig}{16\sigma^2}L_c^{ij}\gamma^\mu\psi_{\mu j}
-\frac i8\gamma^\mu\gamma\!\cdot\!T\psi_\mu^i-\frac i8\gamma^\mu\phi_\mu^i\\
&+\frac i{16\sigma^2}\not{\mathcal D}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j
-\frac g{16\sigma^3}L_c^{ij}\psi_j+\frac g{8\sigma^2}\varphi_c^i.
\end{aligned}\tag{GC15}
```

The coefficients on the first two lines are respectively
$`(i/8)(1/4)=i/32`$, $`(i/8)(i/2)=-1/16`$,
$`(i/8)(i/4)=-1/32`$, $`(i/8)(-g/2)=-ig/16`$, and
$`(i/8)(-1)=-i/8`$. No gamma matrices have been silently commuted.

The exact box, matter derivatives and dependent connections follow.
Every T, chi and D on their right means GC12, GC08 and GC11, respectively.
This is where gauging enters hatted quantities whose formula has no
explicit g. No curvature is evaluated using ungauged chi or T.

```math
\Box^c\sigma=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\tfrac i2\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi
+\tfrac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\tfrac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\tag{GC16}
```

```math
\begin{aligned}
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
\end{aligned}\tag{GC17}
```

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
\end{aligned}\tag{GC18}
```

```math
\begin{aligned}
V_{\mu\nu}{}^{ij}&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}{}^{ij}(V)&=V_{\mu\nu}{}^{ij}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{GC19}
```

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
\end{aligned}\tag{GC20}
```

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad
\mathcal D_a=e_a{}^\mu\mathcal D_\mu.
\tag{GC21}
```

Here $`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab} +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$ and the full derivative is a
derivation on tensor products. In GC21, $`\Phi`$ means the actual field
being differentiated. The second derivative of T acts on the first
derivative's tangent index and its S/K laws as well as on its tensor indices.
It cannot be replaced by a bosonic second derivative.

For the gravitino curvature, the full first derivative appearing in the
final result is explicitly the bosonic derivative (weight 3/2, both lower
Lorentz indices and the SU(2) doublet connection) plus these terms:

```math
\begin{aligned}
\mathcal D_\mu\widehat R_{ab}{}^i(Q)={}&
\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\widehat R_{ab}{}^i(Q)
+\omega_{\mu a}{}^c\widehat R_{cb}{}^i(Q)
+\omega_{\mu b}{}^c\widehat R_{ac}{}^i(Q)-V_\mu{}^{ij}\widehat R_{ab\,j}(Q)\\
&-\frac16\left(\gamma_{ab}{}^{cd}-\gamma^{cd}\gamma_{ab}
-\frac12\gamma_{ab}\gamma^{cd}\right)\widehat R_{cd}{}^i{}_j(V)\psi_\mu^j
-\frac14\widehat C_{ab}{}^{cd}\gamma_{cd}\psi_\mu^i\\
&-2i\left[\mathcal D_{[a}(\gamma\!\cdot\!T)\gamma_{b]}
-\frac13\gamma_{[b}\mathcal D_{a]}(\gamma\!\cdot\!T)
-\frac13\gamma_{[a}\not{\mathcal D}(\gamma\!\cdot\!T)\gamma_{b]}
-\frac13\gamma_{ab}\gamma_d\mathcal D_cT^{cd}\right]\psi_\mu^i\\
&+8T_{ab}\phi_\mu^i-\frac{16}{3}T_{[a}{}^c\gamma_{b]c}\phi_\mu^i
-\frac43\gamma_{abcd}T^{cd}\phi_\mu^i.
\end{aligned}\tag{GC22}
```

This is minus master R05 with $`(\epsilon,\eta)=(\psi_\mu,\phi_\mu)`$
added to the bosonic derivative, so the signs of all three S terms are
reversed relative to R05. There is no K term for this primary curvature.

For example, the derivative of the two explicit compensator terms in
GC08 is not zero and contains five contributions:

```math
\begin{aligned}
\mathcal D_\mu\left(-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i\right)
={}&\frac{3g}{16\sigma^4}(\mathcal D_\mu\sigma)L_c^{ij}\psi_j
-\frac g{16\sigma^3}(\mathcal D_\mu L_c^{ij})\psi_j
-\frac g{16\sigma^3}L_c^{ij}\mathcal D_\mu\psi_j\\
&-\frac g{4\sigma^3}(\mathcal D_\mu\sigma)\varphi_c^i
+\frac g{8\sigma^2}\mathcal D_\mu\varphi_c^i.
\end{aligned}\tag{GC23}
```

Here $`\mathcal D_\mu\sigma^{-n}=-n\sigma^{-n-1}\mathcal D_\mu\sigma`$;
there is no Grassmann minus from the even derivative. The required
compensator derivatives are

```math
\begin{aligned}
\mathcal D_\mu L_c^{ij}&=(\partial_\mu-3b_\mu)L_c^{ij}
+2V_\mu{}^{(i}{}_kL_c^{j)k}-i\bar\psi_\mu^{(i}\varphi_c^{j)},\\
\mathcal D_\mu\varphi_c^i&=\left(\partial_\mu-\frac72b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi_c^i-V_\mu{}^{ij}\varphi_{c\,j}
+\frac i2\not{\mathcal D}L_c^{ij}\psi_{\mu j}
+\frac i2\gamma^aE_{ca}\psi_\mu^i\\
&\quad-\frac12N_c\psi_\mu^i+\gamma\!\cdot\!T L_c^{ij}\psi_{\mu j}
-3L_c^{ij}\phi_{\mu j}.
\end{aligned}\tag{GC24}
```

GC23 exhibits the terms supplied when the complete chi definition is
differentiated. It is not an additional correction to add a second time
to GC17. GC17 already defines the full Standard-Weyl derivative, evaluated
with the gauged composites. This distinction prevents double counting.

The dependencies are finite: GC03 and GC12 determine T; GC18 then
fixes phi and R(Q); GC14–GC15 fix chi; GC19–GC20 fix R(V), f and C;
GC16 and GC11 determine D. GC17/GC21–GC24 fix all displayed derivatives.
The curvature expressions must use this same chain throughout.

<a id="superspace"></a>

## Gold supergeometry and elementary derivative towers

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 1822–2102; frozen input. Source wording follows; its scope labels remain in force.

### Gold source equations and the Bergshoeff component-convention bridge

This reference gives the source equations and the published convention bridge.

<!-- ASSERT_CONVENTION: source_priority=local Sources PDFs before external literature, source_frame=Gold traceless Standard-Weyl superspace, conversion_target=Bergshoeff component frame only through explicit C24 Appendix C tables -->

This note preserves Gold source notation. A superscript `G` or `B` is added only in the bridge to distinguish the Gold and Bergshoeff frames. These superscripts are labels, not indices. At extraction start the inherited project `convention_lock` contained generic placeholders; the scoped existing project component locks are the comparison target, and this extraction does not replace them. Fourier transforms, state normalization, and quantum regularization do not enter this classical source extraction.

### Sources and scope

| ID | Local source | Version and page convention |
|---|---|---|
| S23 | Gold et al., superspace paper | arXiv:2302.14295v2. `PDF n` means the one-based page in this local file; printed page is usually `n-1`. |
| C24 | Gold et al., component paper and supplement | Local combined PDF contains arXiv:2311.00679v1, subsequently published in JHEP 07 (2024) 221. Main printed page is `PDF-1`; supplement printed page is `PDF-99`. |

S23 calls the theory five-dimensional `N=1`; the project uses the older five-dimensional `N=2` nomenclature for the same eight-real-supercharge setting. This is a naming convention, not an extra supersymmetry doubling. The sources use the traceless Standard-Weyl superspace frame. The gauged Dilaton-Weyl substitution is a later operation, not part of S23 (3.24)–(3.27).

**Symbol collisions that must remain explicit.** `W` is the real vector-multiplet scalar superfield; `W_{ab}` or `W_{alpha beta}` is the super-Weyl tensor. `X^{ij}` is the vector triplet, whereas `X_alpha^i`, `X_{alpha beta}^{ij}`, and `Y` are super-Weyl descendants. The source scalar `Y` is not the Bergshoeff vector triplet `Y^{ij}`. `F` is the linear-multiplet scalar, while `F_{ab}` is a vector-multiplet field strength. `G^{ij}` is a generic linear primary and `H_log^{ij}` the composite LOG primary. The constrained linear-multiplet vector is written `mathcal H^a` below, as in the source; it is not the project Dilaton-Weyl three-form `widehat H_{abc}`. The source three-form potential `b_{mnp}` is also different from the dilatation connection `b_m`.

### S23 definitions needed before the LOG primary

All equations in this section are source equations without a Bergshoeff-frame substitution. Tangent indices are `a,b=0,...,4`; spinor indices `alpha,beta=1,...,4`; `i,j=1,2` are `SU(2)` indices. Round/square brackets have unit weight. Spinor ordering and index placement are part of the formula and must not be changed without the source spinor rules.

#### Supergeometry and Weyl descendants [S23 (2.1)–(2.5), PDF7–8 / printed6–7]

```math
\begin{aligned}
\nabla_A&=E_A-\tfrac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}
-B_A\mathbb D-\mathfrak F_A{}^{\alpha i}S_{\alpha i}-\mathfrak F_A{}^aK_a,\\
[\nabla_A,\nabla_B\}&=-T_{AB}{}^C\nabla_C-\tfrac12R(M)_{AB}{}^{cd}M_{cd}
-R(J)_{AB}{}^{kl}J_{kl}-R(\mathbb D)_{AB}\mathbb D\\
&\quad-R(S)_{AB}{}^{\gamma k}S_{\gamma k}-R(K)_{AB}{}^cK_c,\\
W_{\alpha\beta}&=W_{\beta\alpha},\qquad K_AW_{\alpha\beta}=0,
\qquad\mathbb D W_{\alpha\beta}=W_{\alpha\beta},\\
\nabla_\gamma^kW_{\alpha\beta}
&=\nabla_{(\alpha}^kW_{\beta\gamma)}+\tfrac25\varepsilon_{\gamma(\alpha}\nabla^{\delta k}W_{\beta)\delta},\\
W_{\alpha\beta\gamma}{}^k&:=\nabla_{(\alpha}^kW_{\beta\gamma)},
\qquad X_\alpha{}^i:=\tfrac25\nabla^{\beta i}W_{\beta\alpha},\\
W_{\alpha\beta\gamma\delta}&:=\nabla_{(\alpha}^kW_{\beta\gamma\delta)k},
\quad X_{\alpha\beta}{}^{ij}:=\nabla_{(\alpha}^{(i}X_{\beta)}{}^{j)},
\quad Y:=i\nabla^{\gamma k}X_{\gamma k}.
\end{aligned}
```

The two-form/spinor conversion in S23 footnote4 (PDF8) is

```math
T_{ab}=(\Sigma_{ab})^{\alpha\beta}T_{\alpha\beta},
\qquad T_{\alpha\beta}=\tfrac12(\Sigma^{ab})_{\alpha\beta}T_{ab}.
```

This applies to `W`, `F`, and the corresponding two-form Weyl descendant. It does not identify the scalar `W` with any two-form.

#### Generator and spinor-derivative algebra [C24 Appendix A, PDF81–82 / printed80–81]

S23 describes this same traceless frame but delegates the complete algebra to earlier sources. C24 collects it explicitly. The needed generator relations [C24 (A.1)] are

```math
\begin{gathered}
[M_{ab},M_{cd}]=2\eta_{c[a}M_{b]d}-2\eta_{d[a}M_{b]c},\qquad
[M_{ab},\nabla_c]=2\eta_{c[a}\nabla_{b]},\\
M_{\alpha\beta}=\tfrac12(\Sigma^{ab})_{\alpha\beta}M_{ab},\qquad
[M_{\alpha\beta},\nabla_\gamma^i]=\varepsilon_{\gamma(\alpha}\nabla_{\beta)}^i,\\
[J^{ij},J^{kl}]=\varepsilon^{k(i}J^{j)l}+\varepsilon^{l(i}J^{j)k},\qquad
[J^{ij},\nabla_\alpha^k]=\varepsilon^{k(i}\nabla_\alpha^{j)},\\
[\mathbb D,\nabla_a]=\nabla_a,\qquad
[\mathbb D,\nabla_\alpha^i]=\tfrac12\nabla_\alpha^i,\\
[M_{ab},K_c]=2\eta_{c[a}K_{b]},\qquad
[M_{\alpha\beta},S_\gamma^i]=\varepsilon_{\gamma(\alpha}S_{\beta)}^i,
\qquad[J^{ij},S_\alpha^k]=\varepsilon^{k(i}S_\alpha^{j)},\\
[\mathbb D,K_a]=-K_a,\qquad[\mathbb D,S_\alpha^i]=-\tfrac12S_\alpha^i,
\qquad\{S_\alpha^i,S_\beta^j\}=-2i\varepsilon^{ij}(\Gamma^c)_{\alpha\beta}K_c,\\
[K_a,\nabla_b]=2\eta_{ab}\mathbb D+2M_{ab},\qquad
[K_a,\nabla_\alpha^i]=i(\Gamma_a)_\alpha{}^\beta S_\beta^i,\\
\{S_{\alpha i},\nabla_\beta^j\}=2\varepsilon_{\alpha\beta}\delta_i{}^j\mathbb D
-4\delta_i{}^jM_{\alpha\beta}+6\varepsilon_{\alpha\beta}J_i{}^j,\\
[S_{\beta i},\nabla_a]=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}
-\tfrac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}
+\tfrac18(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b
-\tfrac14W_{ab\beta i}K^b.
\end{gathered}
```

**Derived source repair (2026-09-25).** The preceding display preserves literal C24 (A.1l). Its last two K coefficients fail the SDD super-Jacobi identity. With all other locked C24 relations unchanged, the identity requires

```math
[S_{\beta i},\nabla_a]_{\rm consistent}=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}-\frac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}+\frac{i}{8}(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b-\frac{i}{4}W_{ab\beta i}K^b.
\tag{G-C24-A1l-repair}
```

This is a project-derived correction, not a claim of a published erratum. The independent exact test exhausts 122,880 coefficient equations in the linear Weyl-descendant sector: the corrected coefficients pass and the printed coefficients fail. See source-local Jacobi checks. It affects S acting on vector descendants, even when their elementary parent is K-primary. The scalar/vector reconstruction uses this corrected relation; it does not import the different frame-dependent $`WS`$ coefficient from the older source.

Write `T_{alpha beta}^{ij,c}` and `R_{alpha beta}^{ij,...}` for the slots with the two derivative labels `(alpha,i),(beta,j)`, not for an additional raising of the spinor labels. The full spinor anticommutator is

```math
\{\nabla_\alpha^i,\nabla_\beta^j\}
=-T_{\alpha\beta}^{ij,c}\nabla_c
-\tfrac12R(M)_{\alpha\beta}^{ij,cd}M_{cd}
-R(S)_{\alpha\beta}^{ij,\gamma k}S_{\gamma k}
-R(K)_{\alpha\beta}^{ij,c}K_c,
```

with the only nonzero coefficients [C24 (A.2a–d), PDF82 / printed81]

```math
\begin{aligned}
T_{\alpha\beta}^{ij,c}&=2i\varepsilon^{ij}(\Gamma^c)_{\alpha\beta},\\
R(M)_{\alpha\beta}^{ij,cd}&=2i\varepsilon^{ij}\varepsilon_{\alpha\beta}W^{cd}
+i\varepsilon^{ij}(\Gamma_b)_{\alpha\beta}\widetilde W^{bcd},\\
R(S)_{\alpha\beta}^{ij,\gamma k}&=\tfrac{3i}{4}\varepsilon^{ij}\varepsilon_{\alpha\beta}X^{\gamma k}
+i\varepsilon^{ij}\delta_{[\alpha}{}^\gamma X_{\beta]}{}^k,\\
R(K)_{\alpha\beta}^{ij,c}&=-\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}\nabla^bW_b{}^c
+\tfrac i2\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\nabla^d\widetilde W_{da}{}^c
-\tfrac i{32}\varepsilon^{ij}(\Gamma^c)_{\alpha\beta}Y\\
&\quad+\tfrac i4\varepsilon^{ij}\varepsilon_{\alpha\beta}\widetilde W^{cde}W_{de}
+\tfrac i2\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}
\left(W_{ad}W^{cd}-\tfrac3{16}W^{bd}W_{bd}\delta_a{}^c\right).
\end{aligned}
```

Here `widetilde W_{abc}=epsilon_{abcde}W^{de}/2` [C24 (2.19), PDF13 / printed12]. On the primary scalar `log W`, the Lorentz/S/K generators vanish, so the first anticommutator reduces to the torsion term. Once derivatives act, the descendants cease to be primary scalars and the curvature terms must be restored. The source-complete cache of C24 Appendix A also supplies the spinor–vector and vector–vector commutators (A.3)–(A.4), needed when reordering higher derivatives. The explicit towers below already give their required reduced action on the elementary superfields.

#### Complete Weyl spinor-derivative tower [S23 (2.6a–f), PDF9 / printed8]

```math
\begin{aligned}
\nabla_\gamma^kW_{\alpha\beta}
&=W_{\alpha\beta\gamma}{}^k+\varepsilon_{\gamma(\alpha}X_{\beta)}{}^k,\qquad\text{(S23-2.6a)}\\
\nabla_\alpha^iX_\beta^j
&=X_{\alpha\beta}{}^{ij}+\tfrac i8\varepsilon^{ij}\varepsilon_{\alpha\beta}Y
-\tfrac{3i}{2}\varepsilon^{ij}(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\rho}
-2i\varepsilon^{ij}W_\alpha{}^\rho W_{\beta\rho}\\
&\quad+\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}W^{\gamma\delta}W_{\gamma\delta}
-\tfrac i2\varepsilon^{ij}(\Gamma^a)_\beta{}^\rho\nabla_aW_{\alpha\rho},\qquad\text{(S23-2.6b)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda}{}^j
&=-\tfrac12\varepsilon^{ij}\left(W_{\alpha\beta\gamma\lambda}
+3i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda)}
+3i\varepsilon_{\alpha(\beta}(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda)\tau}\right)
-\tfrac32\varepsilon_{\alpha(\beta}X_{\gamma\lambda)}{}^{ij},\qquad\text{(S23-2.6c)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda\rho}
&=-4i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda\rho)}{}^i
-6iW_{\alpha(\beta\gamma}{}^iW_{\lambda\rho)}
+6iW_{\alpha(\beta}W_{\gamma\lambda\rho)}{}^i\\
&\quad+6i\varepsilon_{\alpha(\beta}\left(W_{\gamma\lambda}X_{\rho)}{}^i
-2(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda\rho)\tau}{}^i
-W_\gamma{}^\tau W_{\lambda\rho)\tau}{}^i\right),\qquad\text{(S23-2.6d)}\\
\nabla_\alpha^iX_{\beta\gamma}{}^{jk}
&=i\varepsilon^{i(j}\Big(-3W_{(\beta}{}^\lambda W_{\gamma)\alpha\lambda}{}^{k)}
-\varepsilon_{\alpha(\beta}W^{\rho\tau}W_{\gamma)\rho\tau}{}^{k)}
-W_{\alpha\lambda}W_{\beta\gamma}{}^{\lambda k)}-\tfrac32W_{\beta\gamma}X_\alpha{}^{k)}\\
&\qquad+\tfrac12W_{\alpha(\beta}X_{\gamma)}{}^{k)}
+\tfrac32\varepsilon_{\alpha(\beta}W_{\gamma)\lambda}X^{k)\lambda}
+2(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\gamma\rho}{}^{k)}\\
&\qquad+2(\Gamma^a)_{(\beta}{}^\rho\nabla_aW_{\gamma)\alpha\rho}{}^{k)}
-(\Gamma^a)_{\alpha(\beta}\nabla_aX_{\gamma)}{}^{k)}
+\varepsilon_{\alpha(\beta}(\Gamma^a)_{\gamma)\lambda}\nabla_aX^{k)\lambda}\Big),\qquad\text{(S23-2.6e)}\\
\nabla_\alpha^iY&=8(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta{}^i+8W_\alpha{}^\beta X_\beta{}^i.\qquad\text{(S23-2.6f)}
\end{aligned}
```

Nested round brackets in (2.6e) symmetrize the spinor and `SU(2)` index families separately; they do not include the intervening indices of the other family. Source S transformations and useful Bianchi identities [S23 (2.7)–(2.8), same page] are

```math
\begin{gathered}
\nabla_{(\alpha}{}^\gamma X_{\beta)\gamma}{}^{ij}
=-\tfrac12X^{\gamma(i}W_{\alpha\beta\gamma}{}^{j)},\qquad
\nabla_{(\alpha}{}^\lambda W_{\beta\gamma\tau)\lambda}
=3i\nabla_{(\alpha}{}^\lambda(W_{\beta\gamma}W_{\tau)\lambda}),\\
S_{\alpha i}W_{\beta\gamma\delta}{}^j=6\delta_i{}^j\varepsilon_{\alpha(\beta}W_{\gamma\delta)},
\quad S_{\alpha i}X_\beta{}^j=4\delta_i{}^jW_{\alpha\beta},\\
S_{\alpha i}W_{\beta\gamma\delta\rho}=24\varepsilon_{\alpha(\beta}W_{\gamma\delta\rho)i},
\quad S_{\alpha i}Y=8iX_{\alpha i},\\
S_{\alpha i}X_{\beta\gamma}{}^{jk}
=-4\delta_i{}^{(j}W_{\alpha\beta\gamma}{}^{k)}
+4\delta_i{}^{(j}\varepsilon_{\alpha(\beta}X_{\gamma)}{}^{k)}.
\end{gathered}
```

All these independent descendants are annihilated by `K_a`; their S transformations are generally nonzero.

#### Vector multiplet and differential operators [S23 (2.11)–(2.17), PDF10–11 / printed9–10]

```math
\begin{gathered}
W^*=W,\quad K_AW=0,\quad\mathbb DW=W,\qquad
\nabla_\alpha^{(i}\nabla_\beta^{j)}W=\tfrac14\varepsilon_{\alpha\beta}\nabla^{\gamma(i}\nabla_\gamma^{j)}W,\\
\lambda_\alpha^i=-i\nabla_\alpha^iW,\qquad
X^{ij}=\tfrac i4\nabla^{\alpha(i}\nabla_\alpha^{j)}W
=-\tfrac14\nabla^{\alpha(i}\lambda_\alpha^{j)},\\
F_{\alpha\beta}=-\tfrac i4\nabla_{(\alpha}^k\nabla_{\beta)k}W-W_{\alpha\beta}W
=\tfrac14\nabla_{(\alpha}^k\lambda_{\beta)k}-W_{\alpha\beta}W,\\
\nabla_\alpha^i\lambda_\beta^j
=-2\varepsilon^{ij}(F_{\alpha\beta}+W_{\alpha\beta}W)
-\varepsilon_{\alpha\beta}X^{ij}-\varepsilon^{ij}\nabla_{\alpha\beta}W,\qquad\text{(S23-2.13a)}\\
\begin{aligned}
\nabla_\alpha^iF_{\beta\gamma}
&=-i\nabla_{\alpha(\beta}\lambda_{\gamma)}^i-i\varepsilon_{\alpha(\beta}\nabla_{\gamma)}{}^\delta\lambda_\delta^i
-\tfrac{3i}{2}W_{\beta\gamma}\lambda_\alpha^i-W_{\alpha\beta\gamma}{}^iW\\
&\quad+\tfrac i2W_{\alpha(\beta}\lambda_{\gamma)}^i
-\tfrac{3i}{2}\varepsilon_{\alpha(\beta}W_{\gamma)}{}^\delta\lambda_\delta^i,
\end{aligned}\qquad\text{(S23-2.13b)}\\
\nabla_\alpha^iX^{jk}
=2i\varepsilon^{i(j}\left(\nabla_\alpha{}^\beta\lambda_\beta^{k)}
-\tfrac12W_{\alpha\beta}\lambda^{\beta k)}+\tfrac{3i}{4}X_\alpha{}^{k)}W\right),\qquad\text{(S23-2.13c)}\\
\nabla_{(\alpha}{}^\gamma F_{\beta)\gamma}=\tfrac12\lambda^{\gamma k}W_{\alpha\beta\gamma k},\qquad\text{(S23-2.14)}\\
S_\alpha^i\lambda_\beta^j=-2i\varepsilon_{\alpha\beta}\varepsilon^{ij}W,
\quad S_\alpha^iF_{\beta\gamma}=4\varepsilon_{\alpha(\beta}\lambda_{\gamma)}^i,
\quad S_\alpha^iX^{jk}=-2\varepsilon^{i(j}\lambda_\alpha^{k)},\qquad\text{(S23-2.15)}\\
\nabla^{ij}:=\nabla^{\alpha(i}\nabla_\alpha^{j)},\qquad
\Delta^{ijkl}:=-\tfrac1{96}\varepsilon^{\alpha\beta\gamma\delta}
\nabla_\alpha^{(i}\nabla_\beta^j\nabla_\gamma^k\nabla_\delta^{l)}
=-\tfrac1{32}\nabla^{(ij}\nabla^{kl)}.
\end{gathered}
```

`K_a` annihilates the vector descendants. The real prepotential has weight `-2`, and `W=-(3i/40) nabla_{ij} Delta^{ijkl} V_{kl}` [S23 (2.16)]. In component expressions the source uses the same symbol for the superfield and its `theta=0` projection. `Box:=nabla^a nabla_a` is the superconformal covariant d'Alembertian, not a scalar Levi–Civita Laplacian.

### Generic linear multiplet [S23 (2.20)–(2.24), PDF11–12 / printed10–11]

```math
\nabla_\alpha^{(i}G^{jk)}=0,\qquad K_AG^{ij}=0,\qquad
\mathbb DG^{ij}=3G^{ij},\qquad (G^{ij})^*=\varepsilon_{ik}\varepsilon_{jl}G^{kl}.
```

The complete identities needed to differentiate a primary linear multiplet are

```math
\begin{aligned}
\nabla_\alpha^iG^{jk}&=2\varepsilon^{i(j}\varphi_\alpha^{k)},\\
\nabla_\alpha^i\varphi_\beta^j
&=-\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}F
+\tfrac i2\varepsilon^{ij}\mathcal H_{\alpha\beta}+i\nabla_{\alpha\beta}G^{ij},\\
\nabla_\alpha^iF&=-2\nabla_\alpha{}^\beta\varphi_\beta^i
-3W_{\alpha\beta}\varphi^{\beta i}-\tfrac32X_{\alpha j}G^{ij},\\
\nabla_\alpha^i\mathcal H_a
&=4(\Sigma_{ab})_\alpha{}^\beta\nabla^b\varphi_\beta^i
-\tfrac32(\Gamma_a)_\alpha{}^\beta W_{\beta\gamma}\varphi^{\gamma i}
-\tfrac12(\Gamma_a)_\gamma{}^\beta W_{\beta\alpha}\varphi^{\gamma i}.
\end{aligned}
```

The descendants, conservation law, and S transformations are

```math
\begin{gathered}
\varphi_\alpha^i:=\tfrac13\nabla_{\alpha j}G^{ij},\qquad
F:=\tfrac i{12}\nabla^{\gamma i}\nabla_\gamma^jG_{ij}
=-\tfrac i4\nabla^{\gamma k}\varphi_{\gamma k},\\
\mathcal H_{abcd}:=\tfrac i{12}\varepsilon_{abcde}(\Gamma^e)^{\alpha\beta}
\nabla_\alpha^i\nabla_\beta^jG_{ij}=\varepsilon_{abcde}\mathcal H^e,\\
\mathcal H^a=-\tfrac1{4!}\varepsilon^{abcde}\mathcal H_{bcde},
\qquad\nabla_a\mathcal H^a=0,\\
K_a\varphi_\alpha^i=K_aF=K_a\mathcal H_b=0,\\
S_\alpha^i\varphi_\beta^j=-6\varepsilon_{\alpha\beta}G^{ij},
\quad S_\alpha^iF=6i\varphi_\alpha^i,
\quad S_\alpha^i\mathcal H_b=-8i(\Gamma_b)_\alpha{}^\beta\varphi_\beta^i.
\end{gathered}
```

<a id="projection"></a>

## Projections and published Gold/component conversion tables

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 2283–2379; frozen input. Source wording follows; its scope labels remain in force.

### Supplement notation and projections [C24 supplement §1, PDF103 / printed4]

The underlining and hatting conventions in (1.1a–b) mean weighted symmetrization and antisymmetrization, without exchanging the order of the Grassmann factors:

```math
\lambda_{\underline i}^{\alpha}\lambda_{\underline j}^{\beta}
:=\lambda_{(i}^{\alpha}\lambda_{j)}^{\beta}
=\tfrac12\lambda_i^\alpha\lambda_j^\beta+\tfrac12\lambda_j^\alpha\lambda_i^\beta,
\qquad
W_{c\hat a}W_{\hat b d}:=W_{c[a}W_{b]d}
=\tfrac12W_{ca}W_{bd}-\tfrac12W_{cb}W_{ad}.
```

The source projections (1.2a–b), and the immediately following curvature identification, are

```math
\chi_\alpha^i=\frac{3i}{32}X_\alpha^i|,
\qquad D=-\frac3{128}Y|,
\qquad\Phi_{ab}{}^{ij}=-\frac{3i}{4}X_{ab}{}^{ij}|.
\tag{C24-supp-1.2}
```

The last relation corresponds to `R(J)_{ab}^{ij}` in the superspace notation. Solving the first two gives `X_alpha^i|=-(32i/3)chi_alpha^i` and `Y|=-(128/3)D`. These inverse formulas follow algebraically; they are not new independent source equations. In the supplement, raw `R` and `f` use different typography from the main paper. Preserve the geometric and dependent-connection meanings, not only the visual glyphs. The supplement says its longer expressions can differ from the main text by algebra and sometimes integrations by parts; compare densities only with their boundary representatives recorded.

### Published Gold-to-Bergshoeff bridge [C24 Appendix C, Tables4–6]

The following uses the **Bergshoeff et al. column**. C24 also provides other convention systems; mixing a de Wit entry into this column is not permitted. Source: Tables4–5, PDF91 / printed90; Table6, PDF92 / printed91. The paragraph immediately before Table4 (PDF90 / printed89) explicitly explains the field-dependent S/K shifts and cancellation in the fully covariant vector derivative.

#### Algebra and Weyl multiplet

```math
\begin{gathered}
\eta_G^{ab}=\eta_B^{ab},\qquad
\Gamma_G^a=i\gamma_B^a,\qquad
\Sigma_G^{ab}=\tfrac12\gamma_B^{ab},\qquad
\varepsilon_G^{abcde}=-\varepsilon_B^{abcde},\\
\psi_m^{Gi}=\psi_\mu^{Bi},\qquad
\mathcal V_m^{G,i}{}_j=-V_\mu^{B,i}{}_j,\qquad
\omega_m^{G,ab}=-\omega_\mu^{B,ab},\\
i\phi_m^{Gi}=-\phi_\mu^{Bi}+\tfrac13T_{ab}^B\gamma_B^{ab}\psi_\mu^{Bi},\\
\mathfrak f_m^{G,a}=-f_\mu^{B,a}+\tfrac13\psi_\mu^{Bi}\gamma_B^a\chi_i^B,\\
w_G^{ab}=\tfrac{16}{3}T_B^{ab},\qquad\chi_G^i=\chi_B^i,\qquad D_G=D_B.
\end{gathered}\tag{C24-Table4-fields}
```

`m` and `mu` are the same curved index under the naming conversion. The spinor contractions in the table are source contractions; a Majorana bar cannot be inserted or moved by typography alone. Here `w_ab=W_ab|`, using the two-form version of [C24 (2.15a), PDF12 / printed11].

The corresponding curvatures satisfy

```math
\begin{aligned}
R_G(Q)_{ab}{}^i&=\tfrac12R_B(Q)_{ab}{}^i,\\
R_G(M)_{ab}{}^{cd}&=-R_B(M)_{ab}{}^{cd},\\
R_G(J)_{ab}{}^i{}_j&=-R_B(V)_{ab}{}^i{}_j,\\
iR_G(S)_{ab}{}^i&=-\tfrac12R_B(S)_{ab}{}^i
+\tfrac16T_{cd}^B\gamma_B^{cd}R_B(Q)_{ab}{}^i,\\
R_G(K)_{ab}{}^c&=-R_B(K)_{ab}{}^c
+\tfrac13R_B(Q)_{ab}{}^i\gamma_B^c\chi_i^B.
\end{aligned}\tag{C24-Table4-curvatures}
```

The minus in `R(M)` is a frame-convention map. It does not license flipping a project metric Riemann tensor in isolation while keeping unchanged its connection/generator conventions.

#### Supersymmetry parameters [C24 Table5]

A Gold `delta_Q(xi_G)+delta_S(eta_G)+delta_K(Lambda_G)` becomes a Bergshoeff transformation with

```math
\epsilon_B^i=2\xi_G^i,\qquad
\eta_B^{\prime i}=-2i\eta_G^i+\tfrac23T_{ab}^B\gamma_B^{ab}\xi_G^i,\qquad
\Lambda_K^{\prime Ba}=-\Lambda_K^{Ga}+\tfrac23\xi_G^i\gamma_B^a\chi_i^B.
\tag{C24-Table5}
```

Therefore the conversion of a Q rule includes induced S and K rules. Converting only the gamma matrices, the fields, or `epsilon=2xi` does not convert a complete transformation. The source states that these shifts cancel the corresponding gravitino terms in the S/K connections, leaving the same fully covariant vector derivative after generator-normalization conversion. This statement concerns the **whole derivative**, not a termwise equality of the named connections.

#### Vector multiplet [C24 Table6]

```math
W_G=\sigma_B,\qquad\lambda_G^i=-\psi_B^i,\qquad X_G^{ij}=2Y_B^{ij}.
\tag{C24-Table6}
```

For a generic vector scalar called `rho` in the project, relabel `sigma_B` to `rho` only after identifying which vector is under discussion. The defining vector later has `rho=sigma` and `A=C`. Table6 itself does not list the vector potential or a full linear-multiplet normalization map.

<a id="linear-bridge"></a>

## Derived linear-slot bridge and corrected ordinary current

**Extraction:** [results/gauged_full_fermionic_log/LOG_CONVENTIONS.md](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md), lines 54–332; frozen input. Source wording follows; its scope labels remain in force.

### 2. Convention Ledger

Import master C01–C06, G01–G04, R01–R07, L01–L04, V01–V03, A01–A02 and X01–X11 with their stated scopes. For immediate use:

```math
\begin{gathered}
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad \gamma^{01234}=i,\\
\epsilon_B^{01234}=+1,\qquad \epsilon_{B01234}=-1,\qquad
\epsilon_B^{\mu\nu\rho\sigma\lambda}=e^{-1}[\mu\nu\rho\sigma\lambda],\\
X^i=\varepsilon^{ij}X_j,\qquad X_i=X^j\varepsilon_{ji},\qquad
\varepsilon_{12}=\varepsilon^{12}=1,\qquad
\bar\zeta=\zeta^T\mathsf C.
\end{gathered}
\tag{LOG-S1-01}
```

Frame/world indices run from 0 to 4; doublet indices run from 1 to 2. Antisymmetrization and symmetrization have unit weight. The bar is linear: $`\overline{i\zeta}=i\bar\zeta`$. Fields and SUSY parameters are Grassmann odd, while the parameter-contracted variation is even. In a doublet contraction $`\bar u_i M v^i=-\bar u^i M v_i`$. No Fourier or quantum-state convention enters this step.

The component Riemann convention is master G01/R03: $`R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$, with the corresponding fixed Ricci contraction. Gold uses the converted connection and curvature below. Do not identify the two raw tensors by their names.

The published Weyl bridge is

```math
\begin{aligned}
\Gamma_G^a&=i\gamma^a,&\Sigma_G^{ab}&=\tfrac12\gamma^{ab},&
\epsilon_G^{abcde}&=-\epsilon_B^{abcde},\\
\psi_{\mu G}^i&=\psi_\mu^i,&\omega_{\mu G}^{ab}&=-\omega_\mu^{ab},&
\mathcal V_{\mu G}{}^i{}_j&=-V_\mu{}^i{}_j,\\
w_{Gab}&=\tfrac{16}{3}T_{ab},&\chi_G^i&=\chi^i,&D_G&=D,\\
i\phi_{\mu G}^i&=-\phi_\mu^i+\tfrac13T_{ab}\gamma^{ab}\psi_\mu^i,&
f_{\mu G}{}^a&=-f_\mu{}^a+\tfrac13\bar\psi_\mu^i\gamma^a\chi_i.
\end{aligned}
\tag{LOG-S1-02}
```

The parameter and curvature conversions needed with it are

```math
\begin{gathered}
\epsilon_B^i=2\xi_G^i,\qquad
\eta_B^i=-2i\eta_G^i+\tfrac23T_{ab}\gamma^{ab}\xi_G^i,\qquad
\Lambda_{KB}^a=-\Lambda_{KG}^a+\tfrac23\bar\xi_G^i\gamma^a\chi_i,\\
R_G(Q)_{ab}^i=\tfrac12 R_B(Q)_{ab}^i,\qquad
R_G(M)_{ab}{}^{cd}=-R_B(M)_{ab}{}^{cd},\qquad
R_G(J)_{ab}{}^i{}_j=-R_B(V)_{ab}{}^i{}_j.
\end{gathered}
\tag{LOG-S1-03}
```

These relations include field-dependent redefinitions of Q by S and K. C24 Appendix C identifies the **whole** covariant vector derivative after these shifts. It does not identify each connection independently. Scalar and spinor descendants must retain that full derivative. The remaining R(S)/R(K) entries are imported directly from the main file's Table 4; they are not dropped or independently rederived here.

### 3. Definitions and Required Identities

Write the defining component vector as $`(\rho,A_\mu,\lambda^i,Y^{ij})`$ and a generic component linear multiplet as $`(L^{ij},\varphi^i,N,E_a)`$. Later these become respectively the defining dilaton vector and the composite LOG multiplet. They do not denote the independent compensator.

C24 Table 6 and the vector-potential law (2.38d) give

```math
W_G=\rho,\quad v_{\mu G}=-A_\mu,\quad
\lambda_G^i=-\lambda^i,\quad X_G^{ij}=2Y^{ij},\quad
F_{Gab}=-\widehat F_{ab}.
\tag{LOG-S1-04}
```

For example (2.38d) becomes $`\delta v_\mu=(i/2)\rho\bar\epsilon\psi_\mu-(1/2)\bar\epsilon\gamma_\mu\lambda`$, the negative of master V01's $`\delta A_\mu`$. The Abelian gauge parameters likewise differ by a sign. Substitution in C24 (2.37), with the same spinor order, gives the last equality including the gravitino completion.

The necessary Clifford, transpose and doublet identities are

```math
\begin{gathered}
(\gamma^{ab})^T\mathsf C=-\mathsf C\gamma^{ab},\qquad
(L^{ij}\epsilon_j)_k=-L_{kj}\epsilon^j,\\
T_{bc}\gamma^{bc}\gamma_a=T_{bc}\gamma_a{}^{bc}-2T_{ab}\gamma^b,\qquad
\gamma_{abc}=-\tfrac i2\epsilon_{Babcde}\gamma^{de},\\
\epsilon_B^{abcde}\gamma_{cde}=6i\gamma^{ab},\qquad
\epsilon_B^{abcde}\gamma_{de}=2i\gamma^{abc}.
\end{gathered}
\tag{LOG-S1-05}
```

The $`E_a`$ in a linear multiplet is supercovariant. The **ordinary conserved current** in its BF coupling is a different quantity:

```math
\begin{aligned}
P^a&=E^a+Q_1^a+Q_2^a,\\
Q_1^a&=\tfrac i2\bar\psi_b\gamma^{ba}\varphi,\qquad
Q_2^a=\tfrac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},\\
P^a&=-\tfrac1{12}e_\mu{}^a\epsilon_B^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda},\qquad
\partial_\mu(eP^\mu)=0.
\end{aligned}
\tag{LOG-S1-06}
```

The last identity follows from commuting partial derivatives and antisymmetry; it uses no equation of motion. The potential representation is local. OPall's phrase “bosonic part” means the ordinary field strength stripped of supercovariant bilinears; it does not justify setting the physical fermions to zero.

### 4. Detailed Derivation

#### 4.1 Four covariant linear slots

Start with a nonzero real normalization $`a`$ and unknown $`b,c,d`$:

```math
G_{Gij}=aL_{ij},\qquad \varphi_{Gi}=b\varphi_i,
\qquad F_G=cN,\qquad \mathcal H_{Ga}=dE_a.
\tag{LOG-S1-07}
```

The two triplet laws are $`\delta G_{Gij}=-2\bar\xi_{(i}\varphi_{Gj)}`$ and $`\delta(aL_{ij})=2ia\bar\xi_{(i}\varphi_{j)}`$. Thus $`b=-ia`$.

After lowering the component spinor law, its T and S terms are $`\gamma\cdot T L_{ij}\epsilon_B^j-3L_{ij}\eta_B^j`$. Applying (LOG-S1-03) cancels their T terms and leaves $`6iL_{ij}\eta_G^j`$. The entire law then gives

```math
\delta(-ia\varphi_i)
=a\gamma^b\mathcal D_bL_{ij}\xi_G^j
-a\gamma^bE_b\xi_{Gi}-iaN\xi_{Gi}+6aL_{ij}\eta_G^j.
\tag{LOG-S1-08}
```

C24 (2.52b) gives respectively the same derivative and S coefficients and $`d/2`$, $`-ic/2`$ for its E and N terms. Therefore $`d=-2a`$ and $`c=2a`$.

For the scalar law the Majorana-transposed parameter is $`\bar\eta_B=-2i\bar\eta_G-(2/3)\bar\xi_G\gamma\cdot T`$. Both sources give

```math
\delta F_G=2a\bar\xi_G\not{\mathcal D}\varphi
+4ia\bar\xi_G\gamma\cdot T\varphi
+16ia\bar\xi_G^i\chi^jL_{ij}+6a\bar\eta_G\varphi.
\tag{LOG-S1-09}
```

For the vector law, use the last two Clifford identities in (LOG-S1-05) on the shifted S term. Both sources give

```math
\begin{aligned}
\delta\mathcal H_{Ga}={}&2ia\bar\xi_G\gamma_{ab}\mathcal D^b\varphi
-\tfrac{8a}{3}T_{ab}\bar\xi_G\gamma^b\varphi\\
&+\tfrac{4ia}{3}\epsilon_{Babcde}T^{bc}\bar\xi_G\gamma^{de}\varphi
-8ia\bar\eta_G\gamma_a\varphi.
\end{aligned}
\tag{LOG-S1-10}
```

Every intermediate scalar/vector coefficient and the rank-three reduction are given in the independent audit, sections 4.2–4.3. Thus all four **covariant Q/S laws** match. These homogeneous laws leave $`a`$ free. Choose $`a=-1/2`$ so that the six nonform density terms have unit component normalization:

```math
\boxed{G_G^{ij}=-\tfrac12L^{ij},\qquad
\varphi_G^i=\tfrac i2\varphi^i,\qquad
F_G=-N,\qquad \mathcal H_G^a=E^a.}
\tag{LOG-S1-11}
```

In particular, when the generic primary is replaced by $`H_{\log W}^{ij}`$,

```math
L_{\log}^{ij}=-2H_{\log W}^{ij},\qquad
\varphi_{\log B}^i=-2i\varphi_{\log G}^i,\qquad
N_{\log}=-F_{\log G},\qquad E_{\log}^a=\mathcal H_{\log G}^a.
\tag{LOG-S1-12}
```

This is a map of the slots. It is not the computation of their composite contents, which begins in step 2.

#### 4.2 Explicit chi curvature: index order resolves the apparent sign

Define the two antisymmetrized expressions with their order visible:

```math
K_{ab}{}^{cd}=\delta_{[a}^{[c}\bar\psi_{b]}\gamma^{d]}\chi,
\qquad J_{ab}{}^{cd}=\bar\psi_{[a}\delta_{b]}^{[c}\gamma^{d]}\chi=-K_{ab}{}^{cd}.
\tag{LOG-S1-13}
```

For example $`4K=\delta_a^c\bar\psi_b\gamma^d\chi-\delta_b^c\bar\psi_a\gamma^d\chi-\delta_a^d\bar\psi_b\gamma^c\chi+\delta_b^d\bar\psi_a\gamma^c\chi`$. In C24 (2.18c), the f shift contributes $`(8/3)K`$, and the explicit $`(16i/3)\delta\psi_{Gi}\Gamma_G\chi_G^i`$ contributes $`(16/3)K`$, including the doublet-contraction minus. Using $`R_G(M)=-R_B(M)`$ gives

```math
R_B(M)\big|_{\text{explicit }\psi\chi}
=-\left(\tfrac83+\tfrac{16}{3}\right)K=-8K=+8J.
\tag{LOG-S1-14}
```

This agrees with master R03's project-corrected **$`+8\bar\psi_{[a}\delta_{b]}^{[c}\gamma^{d]}\chi`$**. It does not agree with literal OP's $`-8`$ multiplying that same J order. The comparison holds the B-frame f, phi and R(Q) slots fixed after conversion; it does not count their implicit chi dependence a second time. It checks the disputed explicit sector, not every term of the full curvature algebra.

#### 4.3 Seven BF terms and the form residual

Expand the overall minus sign in S23 (3.2b)/C24 (3.2b) before converting. Written spinor order is maintained throughout.

| Gold density term, including its outer sign | Result using (LOG-S1-04), (LOG-S1-11) |
|---|---|
| $`-X_{Gij}G_G^{ij}`$ | $`Y^{ij}L_{ij}`$ |
| $`-W_GF_G`$ | $`\rho N`$ |
| $`-2\lambda_G^i\varphi_{Gi}`$ | $`i\bar\lambda\varphi`$ |
| $`+W_G\psi_{ai}\Gamma_G^a\varphi_G^i`$ | $`\rho\bar\psi_a\gamma^a\varphi/2`$ |
| $`+i\psi_{ai}\Gamma_G^a\lambda_{Gj}G_G^{ij}`$ | $`-\bar\psi_a^i\gamma^a\lambda^jL_{ij}/2`$ |
| $`-iW_G\psi_{ai}\Sigma_G^{ab}\psi_{bj}G_G^{ij}`$ | $`i\rho\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}/4`$ |
| $`-v_{Ga}\mathcal H_G^a`$ | $`A_aE^a`$, whereas the component density requires $`A_aP^a`$ |

For example the fourth row has coefficients $`(i)(i/2)(-1)=+1/2`$, where the last sign is the lowered-first doublet contraction. The third row gives $`-2(-1)(i/2)=i`$. The last row is an actual discrepancy when fermions are retained:

```math
\ell_{G,\mathrm{printed}}-\ell_{VL}
=-A_a(Q_1^a+Q_2^a).
\tag{LOG-S1-15}
```

It vanishes in the bosonic limit. A bosonic normalization check alone could not expose it. A current with $`\mathcal D_aE^a=0`$ cannot silently replace a current with $`\partial_\mu(eP^\mu)=0`$ in an ordinary Abelian gauge coupling.

The full component density retained as the operational source formula is

```math
\begin{aligned}
\ell_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\tfrac12\bar\psi_a^i\gamma^a\lambda^jL_{ij}+A_aP^a\\
&+\rho\left(N+\tfrac12\bar\psi_a\gamma^a\varphi
+\tfrac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right).
\end{aligned}
\tag{LOG-S1-16}
```

For arbitrary $`a`$, all six nonform terms instead have the common multiplier $`-2a`$. The choice in (LOG-S1-11) sets that multiplier to one; it does not fix the form discrepancy by rescaling.

#### 4.4 Ordinary form representative and a local supersymmetry diagnostic

The bosonic form definitions and orientations imply

```math
b_{G\mu\nu\rho}=-\tfrac12E_{\mu\nu\rho},\qquad
h_G^a=-\tfrac16\epsilon_G^{abcde}\partial_b b_{Gcde}=P^a.
\tag{LOG-S1-17}
```

In particular, an ordinary Gold form coupling would obey

```math
-v_{Ga}h_G^a\simeq_{\partial}
\tfrac1{12}\epsilon_G^{abcde}f_{Gab}b_{Gcde}
=-\tfrac1{24}\epsilon_B^{abcde}F_{Bab}E_{cde}
\simeq_{\partial} A_aP^a,
\tag{LOG-S1-18}
```

where $`f_G=dv_G`$, $`F_B=dA`$ are ordinary field strengths. In a curved chart the integrations by parts use $`e\epsilon^{\mu\nu\rho\sigma\lambda}`$, the constant coordinate symbol. Only these displayed equalities discard a divergence.

C24 (3.2b) prints $`\mathcal H`$, while its potential version (3.2c) has the ordinary form term in (LOG-S1-18), leaving its other terms unchanged. Also, the printed C24 (2.50) completion converts to

```math
\mathcal H_G^a=h_G^a+Q_1^a-Q_2^a.
\tag{LOG-S1-19}
```

The explicit superfour-form pullback proves the required relation $`\mathcal H_G^a=h_G^a-Q_1^a-Q_2^a`$. Literal source minus required is **$`2Q_1^a`$ only**. The earlier plus-$`Q_2`$ conversion in this ledger and note 07 came from lowering the second spinor index on the wrong side: the tensor is $`M\mathsf C^T=-M\mathsf C`$, yielding the bilinear kernel $`-\mathsf C M`$. The corrected (LB42)–(LB44) and the superform certification, (FI03)–(FI18), give all intermediate steps. Original-PDF glyph positions confirm the source doublet placement; a guessed reversal is not a correction. Evidence is saved in the glyph audit.

There is an independent diagnostic. In a local flat frame keep only derivatives of the local Q parameter, set $`\delta\psi_b=\partial_b\epsilon`$, and write a possible potential law as

```math
\delta E_{\mu\nu\rho}
=\alpha\bar\epsilon\gamma_{\mu\nu\rho}\varphi
+i\beta\bar\psi_{[\mu}^i\gamma_{\nu\rho]}\epsilon^jL_{ij}
+\text{form gauge transformation}.
\tag{LOG-S1-20}
```

Define $`U^a=\partial_b\bar\epsilon\gamma^{ab}\varphi`$ and $`V^a=\partial_b\bar\epsilon^i\gamma^{abc}\psi_c^jL_{ij}`$. The epsilon/gamma identities and the Grassmann rank-three flip give

```math
\begin{aligned}
\delta P^a\big|_{\partial\epsilon}&=-\tfrac{i\alpha}{2}U^a-\tfrac\beta6V^a,\\
\delta Q_1^a\big|_{\partial\epsilon}&=-\tfrac i2U^a,\qquad
\delta Q_2^a\big|_{\partial\epsilon}=\tfrac12V^a,\\
\delta E^a\big|_{\partial\epsilon}
&=-\tfrac i2(\alpha-1)U^a-\left(\tfrac\beta6+\tfrac12\right)V^a.
\end{aligned}
\tag{LOG-S1-21}
```

Thus supercovariance requires $`\alpha=1`$, $`\beta=-3`$ in this ansatz. Those are the coefficients obtained by converting **C24 (2.54)**. Literal OP (2.24) instead has $`\alpha=-1`$, $`\beta=1`$ and fails this test. This sharpens the already quarantined master X10 issue.

The component current (LOG-S1-06), density (LOG-S1-16), and potential law with $`(\alpha,\beta)=(1,-3)`$ are now derived by the superform certification, (FI09)–(FI31). The graded superfour-form pullback supplies the full potential law; the closed superfive-form supplies generic BF invariance. The original arXiv:1410.8682v2 (8.28)–(8.29) explicitly uses the ordinary dual $`h_G`$ in the vector coupling, resolving the C24/S23 (3.2b) symbol mismatch. These are **derived repairs**, kept separate from literal source displays. This closes FORM-01 for a genuine linear multiplet without promoting the principal test above to a complete proof of the expanded LOG polynomials.

<a id="potential"></a>

## Full superform pullback and operational three-form variation

This derivation gives the full superform pullback and the operational potential law used below; its stated scope applies.

### 2. The index-lowering calculation which fixes the local audit error

The source convention, already correctly used by Step 2 (S2-02) and Step 6 (S6-02), is

```math
M_{\alpha\beta}=\varepsilon_{\beta\gamma}M_\alpha{}^\gamma.
\tag{FI03}
```

The summed $`\gamma`$ is the column index of $`M`$ but the column index of $`\varepsilon`$ too. Thus this is multiplication by the **transpose** of the lower metric:

```math
M_{\downarrow\downarrow}=MC^T=-MC,\qquad U:=\varepsilon^{\uparrow\uparrow}=-C,\qquad U^T=C.
\tag{FI04}
```

For two independent lower spinor columns $`u,v`$, keeping their order unchanged gives

```math
u^\alpha M_\alpha{}^\beta v_\beta=u^T U^T Mv=\bar uMv,\qquad u^\alpha M_{\alpha\beta}v^\beta=u^TU^T(-MC)Uv=-\bar uMv.
\tag{FI05}
```

The second result uses $`(-MC)(-C)=MC^2=-M`$. No Grassmann interchange was used to obtain its minus. Equivalently, the full kernel is $`U^T(-MC)U=-CM`$.

Old note 07 (LB42) used $`MC`$ instead of $`MC^T`$. Its algebraic identity $`U^T(MC)U=CM`$ is true for that matrix, but that matrix is **not** $`\Sigma_{\alpha\beta}`$ under (FI03). Its claimed application to C24 (2.50) is therefore false. This is the specific local error, rather than a change to the source or to the Step 2–6 tensor conventions.

For later use define the component bilinears

```math
Q_1^a:=\frac i2\bar\psi_b\gamma^{ba}\varphi,\qquad Q_2^a:=\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{FI06}
```

The two raw Gold contractions convert separately:

```math
2(\Sigma_G^{ab})_\alpha{}^\beta\psi_{bi}^{\alpha}\varphi_{G\beta}^{i}=\frac i2\bar\psi_{bi}\gamma^{ab}\varphi^i=-\frac i2\bar\psi_b^i\gamma^{ab}\varphi_i=Q_1^a,
\tag{FI07}
```

and

```math
\frac i2\epsilon_G^{abcde}(\Sigma_{Gbc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G_G^{ij}=-\frac i8\epsilon_B^{abcde}\bar\psi_d^i\gamma_{bc}\psi_e^jL_{ij}=Q_2^a.
\tag{FI08}
```

The first coefficient in (FI08) is $`(i/2)(-1)(-1/2)(-1/2)=-i/8`$: orientation, generator/raised-spinor kernel, and triplet respectively. Both lowered SU(2) indices are converted together with the upper triplet, producing $`L_{ij}`$ without an additional sign. The last equality uses $`\epsilon_B^{abcde}\gamma_{bc}=2i\gamma^{ade}`$.

### 3. The entire four-form pullback

Write $`\Phi_4=d\mathcal B_3`$. Source (8.3) uses the reversed basis order

```math
\Phi_4=\frac1{4!}E^D\wedge E^C\wedge E^B\wedge E^A\Phi_{ABCD},\qquad E^a\Vert=e^a,\qquad E_i^\alpha\Vert=\frac12\psi_i^\alpha.
\tag{FI09}
```

The second projection is C24 (2.12)–(2.13); $`\Vert`$ means the pullback to $`\theta=d\theta=0`$. Source (8.6a–c) gives all nonzero components:

```math
\Phi_{ab\,\alpha^i\beta^j}=8i(\Sigma_{ab})_{\alpha\beta}G_G^{ij},\qquad \Phi_{abc\,\alpha}^{i}=-2\epsilon_{Gabcde}(\Sigma^{de})_\alpha{}^\beta\varphi_{G\beta}^{i},\qquad \Phi_{abcd}=\epsilon_{Gabcde}\mathcal H_G^e,
\tag{FI10}
```

while components with three or four spinor legs vanish. These formulas contain no truncation in the independent linear multiplet fields.

Here is the combinatorial sign, rather than an assumed bosonic pullback. For a $`p`$-form term with $`k`$ fermionic legs, there are $`\binom pk`$ placements. The $`k`$ factors $`E_i^\alpha\Vert`$ give $`2^{-k}`$. Moving the fermionic tensor slots to the right, together with moving their world indices to the front of the antisymmetrization, gives $`(-1)^{k(p-k)}`$. The reversed vielbein product reverses the order of the $`k`$ odd gravitino coefficients; returning them to ascending world-index order gives $`(-1)^{k(k-1)/2}`$. Thus

```math
c_{p,k}=2^{-k}\binom pk(-1)^{k(p-k)+k(k-1)/2}.
\tag{FI11}
```

For $`p=5`$, this yields $`(1,5/2,-5/2,-5/4,5/16,1/32)`$, exactly the independently printed source (8.27). For $`p=4`$, the first three coefficients are $`(1,-2,-3/2)`$. The remaining two multiply vanishing components in (FI10). Consequently the ordinary four-form components are exactly

```math
h_{abcd}=\Phi_{abcd}|-2\psi_{[a i}^{\alpha}\Phi_{bcd]\,\alpha}^{i}|-\frac32\psi_{[a i}^{\alpha}\psi_{b j}^{\beta}\Phi_{cd]\,\alpha^i\beta^j}|=4\partial_{[a}b_{G bcd]},
\tag{FI12}
```

with inverse vielbeins understood in the last expression if the chosen frame is not coordinate. A completely unambiguous curved-coordinate version is $`h_{mnpq}=4\partial_{[m}b_{Gnpq]}`$ followed by conversion of all four indices to tangent indices.

Now use the ordinary dual

```math
h_G^a=-\frac1{24}\epsilon_G^{abcde}h_{bcde}.
\tag{FI13}
```

The top component gives $`\mathcal H_G^a`$ because $`\epsilon_G^{abcde}\epsilon_{Gbcdef}=-24\delta^a_f`$. The single-gravitino term in (FI12) is $`+4\psi_{[b}\epsilon_{Gcde]fg}\Sigma^{fg}\varphi_G`$. After contraction its coefficient is

```math
-\frac4{24}\epsilon_G^{abcde}\epsilon_{Gcdefg}\psi_{bi}\Sigma^{fg}\varphi_G^i=-\frac16(-6)(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)\psi_{bi}\Sigma^{fg}\varphi_G^i=2\psi_{bi}\Sigma^{ab}\varphi_G^i.
\tag{FI14}
```

The two-gravitino term is $`-(3/2)8i\psi_{[b i}^{\alpha}\psi_{c j}^{\beta}(\Sigma_{de]})_{\alpha\beta}G^{ij}`$. Its dual gives $`+i\epsilon_G^{abcde}(\Sigma_{bc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G^{ij}/2`$. Therefore

```math
h_G^a=\mathcal H_G^a+2(\Sigma_G^{ab})_\alpha{}^\beta\psi_{bi}^{\alpha}\varphi_{G\beta}^{i}+\frac i2\epsilon_G^{abcde}(\Sigma_{Gbc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G_G^{ij}=E^a+Q_1^a+Q_2^a.
\tag{FI15}
```

The corresponding local potential normalization, fixed already by the bosonic top slot, is

```math
b_{Gmnp}=-\frac12E_{mnp},\qquad P^a:=h_G^a=-\frac1{12}\epsilon_B^{abcde}e_b{}^m e_c{}^n e_d{}^p e_e{}^q\partial_m E_{npq},\qquad E^a=P^a-Q_1^a-Q_2^a.
\tag{FI16}
```

This normalization is now a full superform identification, locally modulo a closed three-form and the two-form gauge parameter, rather than only a bosonic guess.

The source (8.5) Bianchi identity is $`d\Phi_4=0`$. Its tangent-component consequence is source (8.9): $`\nabla^a\mathcal H_{Ga}+5iX^{\gamma k}\varphi_{G\gamma k}=\widehat\nabla^a\mathcal H_{Ga}=0`$. The hat here is the source **traceless superspace frame**, whose vector connection differs from the original frame; it is not a removal of fermion terms. C24 uses this traceless frame and prints its covariant constraint as $`\nabla^a\mathcal H_{Ga}=0`$. Transporting the full derivative gives the project constraint $`\mathcal D^aE_a=0`$. Independently, the ordinary pullback has

```math
\partial_m(eP^m)=0,
\tag{FI17}
```

because its divergence is proportional to the symmetric $`\partial_m\partial_n`$ contracted with the antisymmetric coordinate epsilon. Equations (FI17) and $`\mathcal D\cdot E=0`$ are two descriptions of this Bianchi identity; they are not permission to replace $`P`$ by $`E`$ in an ordinary Abelian coupling.

**Literal-source discrepancy.** Solving (FI15) for $`\mathcal H_G`$ requires minus signs in front of both raw Gold bilinears. C24 (2.50) instead prints plus in front of the single-gravitino bilinear and minus in front of the double-gravitino bilinear. Its exact conversion is

```math
\mathcal H_G^{a}\big|_{\mathrm{C24\ literal}}=h_G^a+Q_1^a-Q_2^a,\qquad \mathcal H_G^a\big|_{\mathrm{superform}}=h_G^a-Q_1^a-Q_2^a,\qquad \Delta_{\mathrm{literal-required}}\mathcal H_G^a=2Q_1^a.
\tag{FI18}
```

Thus only the first source completion sign is inconsistent with this form reconstruction. The old local plus-$`Q_2`$ conversion was the separate error diagnosed in §2. The raw printed formula must remain preserved as a source record; (FI18) is a derived correction under the fixed dictionary, not a claim that a published erratum exists.

### 4. Derivation of the full potential law

For a superform potential the covariant local supersymmetry variation, including a redefinition of its gauge parameter, is the contraction with its field strength:

```math
\delta_\xi\mathcal B_3=i_\xi\Phi_4+d\Lambda_2.
\tag{FI19}
```

This is the Cartan identity $`\mathcal L_\xi\mathcal B_3=i_\xi d\mathcal B_3+d(i_\xi\mathcal B_3)`$, with the latter term absorbed in $`d\Lambda_2`$. In source component ordering $`(i_\xi\Phi)_{ABC}=\xi^D\Phi_{DABC}`$. When taking the pullback the parameter stays to the right of the reversed vielbein coefficients until the Grassmann signs have been taken. For no gravitino, moving the first spinor slot through three vector slots gives a minus. For one gravitino there are three positions. In position $`r=0,1,2`$, moving the two fermion slots past vectors gives $`(-1)^{2+(2-r)}`$, and the world antisymmetrization gives $`(-1)^r`$; their product is plus in every case. Each vielbein supplies $`1/2`$. Thus

```math
\delta b_{Gabc}=-\xi_i^\alpha\Phi_{abc\,\alpha}^i|+\frac32\psi_{[a i}^{\alpha}\xi_j^\beta\Phi_{bc]\,\alpha^i\beta^j}|+3\partial_{[a}\Lambda_{bc]}.
\tag{FI20}
```

There are no further gravitino terms: the requisite three-spinor components of $`\Phi`$ vanish. Inserting (FI10) gives

```math
\delta b_{Gabc}=2\epsilon_{Gabcde}\xi_i^\alpha(\Sigma^{de})_\alpha{}^\beta\varphi_{G\beta}^i+12i\psi_{[a i}^{\alpha}\xi_j^\beta(\Sigma_{bc]})_{\alpha\beta}G_G^{ij}+3\partial_{[a}\Lambda_{bc]}.
\tag{FI21}
```

In the second term, $`\Sigma_{\alpha\beta}\xi^\beta=(-MC)(-C)\xi_\downarrow=-M\xi_\downarrow`$. Converting both SU(2) indices together with $`G^{ij}`$ then gives

```math
\delta b_{Gmnp}=2\epsilon_{Gabcde}e_m^ae_n^be_p^c(\xi_i\Sigma^{de}\varphi_G^i)-12i(\psi_{[m}^{i}\Sigma_{np]}\xi^j)G_{Gij}+3\partial_{[m}\Lambda_{np]}.
\tag{FI22}
```

This reproduces **both terms of literal C24 (2.54)** with their exact coefficients and index order. It is the full local potential transformation modulo its form gauge symmetry, not only a determination of the coefficients of $`\partial\xi`$.

For transparency the first project coefficient follows from

```math
2\epsilon_G\xi_i\Sigma_G\varphi_G^i=-\frac i4\epsilon_B\bar\epsilon_{Bi}\gamma_2\varphi^i=\frac i4\epsilon_B\bar\epsilon_B\gamma_2\varphi=-\frac12\bar\epsilon_B\gamma_3\varphi.
\tag{FI23}
```

The last step uses $`\epsilon_{Babcde}\gamma^{de}=2i\gamma_{abc}`$. The second coefficient is $`(-12i)(1/2)(1/2)(-1/2)=3i/2`$. Dividing both by $`b_G/E_3=-1/2`$ yields

```math
\boxed{\delta E_{mnp}=\bar\epsilon_B\gamma_{mnp}\varphi-3i\bar\psi_{[m}^{i}\gamma_{np]}\epsilon_B^jL_{ij}+3\partial_{[m}\Lambda^{(B)}_{np]}.}
\tag{FI24}
```

This also explains the earlier independent cancellation of the principal parameter derivatives in $`E=P-Q_1-Q_2`$. Literal OP (2.24) has coefficients $`(-1,+1)`$ and is incompatible with (FI24) under the already fixed covariant slot/current map. Their ratios are not a common potential rescaling. Its discrepancy remains a quarantined literal source formula; the complete superform construction now supports the operational $`(+1,-3)`$ law.

The geometry proves more than a principal test: $`d\Phi=0`$ implies $`\delta\Phi=\mathcal L_\xi\Phi`$ with all curvature and connection terms included. Commutators of superdiffeomorphisms close by the graded Lie bracket; choosing the covariant representative (FI19) changes closure only by a form-gauge transformation. No component equation of motion is used. On a gauge-fixed realization, the compensating superconformal transformation is composed with this same identity; it does not change the form definition or require expanding every curvature.

### 5. Closed BF form, normalization and all seven component slots

Let the defining vector one-form be $`V`$, with $`F_2=dV`$, and let $`\Sigma_G`$ be the source curvature-induced five-form. Source **(8.19), (8.22), (8.25)** gives

```math
d\Sigma_G=F_2\wedge\Phi_4,\qquad \mathfrak J=V\wedge\Phi_4-\Sigma_G,\qquad d\mathfrak J=F_2\wedge\Phi_4-V\wedge d\Phi_4-d\Sigma_G=0.
\tag{FI25}
```

The overall sign here is the literal (8.25). The opposite sign also defines a closed form but reverses the action normalization; it is not silently substituted. The action is $`S=\int_{M^5}i^*\mathfrak J`$. Source (8.12) gives

```math
\delta_\xi S=\int i^*(\mathcal L_\xi\mathfrak J)=\int i^*\big(i_\xi d\mathfrak J+d(i_\xi\mathfrak J)\big)=\int d\big(i^*i_\xi\mathfrak J\big).
\tag{FI26}
```

For the Abelian transformation $`\delta V=d\alpha`$,

```math
\delta_\alpha\mathfrak J=d\alpha\wedge\Phi_4=d(\alpha\Phi_4),
\tag{FI27}
```

and the linear potential gauge transformation leaves $`\Phi_4`$ unchanged. The covariant superforms are superconformal, as required by source (8.14)–(8.15); their induced action is invariant up to these boundary terms. This establishes the generic off-shell BF invariant without expanding its many composite terms. It assumes the defining vector constraints and the actual linear-multiplet constraint, not just a collection of fields named $`L,\varphi,N,E`$.

We also reproduce the nonform density rather than relying only on closedness. The nonzero source (8.22) entries are

```math
\Sigma_{abc\,\alpha^i\beta^j}=-4i\epsilon_{Gabcde}(\Sigma^{de})_{\alpha\beta}\rho G_G^{ij},\qquad \Sigma_{abcd\,\alpha}^{i}=2\epsilon_{Gabcde}(\Gamma^e)_\alpha{}^\beta(\rho\varphi_{G\beta}^i+i\lambda_{G\beta j}G_G^{ji}),\qquad \Sigma_{abcde}=-\epsilon_{Gabcde}(\rho F_G+X_G^{ij}G_{Gij}+2\lambda_G^{\alpha k}\varphi_{G\alpha k}).
\tag{FI28}
```

Let the final parenthesis be $`S_0`$, and let $`Z^i:=\rho\varphi_G^i+i\lambda_{Gj}G_G^{ji}`$. Using (FI11) for $`p=5`$, the top term contributes $`S_0`$. The one-gravitino coefficient is $`(5/2)2/5!=1/24`$, and $`\epsilon_G^{abcde}\epsilon_{Gbcdef}=-24\delta^a_f`$, so it contributes $`-\psi_{ai}\Gamma^a Z^i`$. For the two-gravitino term the coefficient is $`(-5/2)(-4i)/5!=i/12`$; contracting two epsilons yields $`-6(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)`$, hence $`-i\psi_{ai}^\alpha\psi_{bj}^\beta(\Sigma^{ab})_{\alpha\beta}\rho G_G^{ij}`$. The raised-spinor identity (FI05) converts that last contraction to **plus** $`i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}`$. Therefore

```math
\frac1{5!}\epsilon_G^{abcde}(\Sigma_G\Vert)_{abcde}=S_0-\psi_{ai}\Gamma^a\varphi_G^i\rho-i\psi_{ai}\Gamma^a\lambda_{Gj}G_G^{ij}+i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}.
\tag{FI29}
```

The $`V\wedge\Phi_4`$ term contains the **ordinary pullback** $`h_{mnpq}`$, not just its purely tangent superfield component. By (FI13) its scalar density is $`-v_{Ga}h_G^a`$. Subtracting (FI29), as required in (FI25), gives source **(8.28)**:

```math
e^{-1}\mathcal L_G=-v_{Ga}h_G^a-\rho F_G-X_G^{ij}G_{Gij}-2\lambda_G^{\alpha k}\varphi_{G\alpha k}+\psi_{ai}\Gamma^a\varphi_G^i\rho+i\psi_{ai}\Gamma^a\lambda_{Gj}G_G^{ij}-i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}.
\tag{FI30}
```

Source **(8.29)** explicitly identifies the ordinary four-form in this term as $`h_{mnpq}=4\partial_{[m}b_{Gnpq]}`$; source **(8.30)** integrates it by parts. Therefore the use of a calligraphic covariant $`\mathcal H`$ in C24/S23 (3.2b), while retaining the other six coefficients, is a source symbol/interface error. It can be repaired either by writing $`h_G`$ there, or by explicitly adding its $`h_G-\mathcal H_G`$ completion. It is not an identically conserved improvement which may be omitted: $`\partial(eE)`$ is generally nonzero while $`\partial(eP)=0`$.

Each coefficient in (FI30) can now be checked without any expansion of the composite linear multiplet:

| Source contribution | Conversion factors, including the displayed action sign | Project contribution |
|---|---|---|
| $`-v_Gh_G`$ | $`-(-1)(1)`$ | $`A_aP^a`$ |
| $`-X_GG_G`$ | $`-(2)(-1/2)`$ | $`Y^{ij}L_{ij}`$ |
| $`-\rho F_G`$ | $`-(-1)`$ | $`\rho N`$ |
| $`-2\lambda_G\varphi_G`$ | $`-2(-1)(i/2)`$ | $`i\bar\lambda\varphi`$ |
| $`+\rho\psi_i\Gamma\varphi_G^i`$ | $`(i)(i/2)(-1)`$, last minus from SU(2) | $`\rho\bar\psi_a\gamma^a\varphi/2`$ |
| $`+i\psi_i\Gamma\lambda_{Gj}G_G^{ij}`$ | $`i(i)(-1)(-1/2)`$ | $`-\bar\psi_a^i\gamma^a\lambda^jL_{ij}/2`$ |
| $`-i\rho\psi_i\Sigma\psi_jG_G^{ij}`$ | $`-i(1/2)(-1/2)`$ | $`i\rho\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}/4`$ |

The resulting exact generic density is

```math
\boxed{\ell_{VL}=Y^{ij}L_{ij}+i\bar\lambda\varphi-\frac12\bar\psi_a^i\gamma^a\lambda^jL_{ij}+A_aP^a+\rho\left(N+\frac12\bar\psi_a\gamma^a\varphi+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right),\qquad P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.}
\tag{FI31}
```

The ordinary form representative is $`A\cdot P\simeq_\partial-\epsilon_B^{abcde}F_{Bab}E_{cde}/24`$, using $`F_B=dA`$ and the divergence current $`J^b=-\epsilon_B^{abcde}A_aE_{cde}/12`$. In curved coordinates $`e\epsilon^{mnpqr}`$ is the constant coordinate symbol. This is the only integration by parts used for the density comparison. The local component equalities (FI15) and (FI24) do not use integration by parts.

<a id="source-gauge"></a>

## Source gauge, compensating transformations and bosonic specialization

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 2458–2642; frozen input. Source wording follows; its scope labels remain in force.

FI24 supplies the potential law used with this component dictionary. No independent all-order closure claim is made.

### Target gauge, normalization and Gold 2025 benchmark

#### LOG-G01 — Target gauge and independent fields

G25 (7), (25), (27), PDF6,14; OP (4.1)–(4.2), PDF13:

```math
\sigma=1,\quad b_\mu=0,\quad\psi^i=0,\qquad
L_c^{ij}=\frac{\delta^{ij}}{\sqrt2}L,\qquad
V_a^{ij}=V_a'{}^{ij}+\frac12\delta^{ij}V_a,\quad
\delta_{ij}V_a'{}^{ij}=0.
\tag{LOG-G01}
```

The retained independent fields are
$`e_\mu{}^a,\psi_\mu^i,C_\mu,B_{\mu\nu},L,E_{c\,\mu\nu\rho},N_c, \varphi_c^i,V_\mu,V_\mu'{}^{ij}`$.
$`\omega,\phi,f,T,\chi,D,Y`$ are their explicitly defined covariants.
The compensator gauge assumes $`L\ne0`$ locally. Do not set $`L=1`$, $`N_c=0`$,
$`E_c=0`$, $`V'=0`$ or $`\varphi_c=0`$ as part of this construction.

#### LOG-G02 — Gauge preservation: defining equations and kinematic solutions

This is a local algebraic consequence of V01/W01 and GG03–GG05, not a quotation
of truncated OP (4.3). On LOG-G01, $`\mathcal D_\mu\sigma=0`$ but

```math
\mathcal D_\mu\psi^i\big|_{\rm gauge}
=\frac14\gamma\!\cdot\!\widehat G\,\psi_\mu^i
-\frac g2 L_c^{ij}\psi_{\mu j}
-\gamma\!\cdot\!T\,\psi_\mu^i-\phi_\mu^i\ne0.
\tag{LOG-G02a}
```

The first compensating parameter follows by setting the full defining-vector
spinor variation to zero, without setting its covariant derivative to zero:

```math
0=\delta\psi^i\big|_{\rm gauge}
=-\frac14\gamma\!\cdot\!\widehat G\epsilon^i
+\gamma\!\cdot\!T\epsilon^i-Y^{ij}\epsilon_j+\eta^i,
\qquad Y^{ij}\big|_{\rm gauge}=-\frac g2L_c^{ij},
\tag{LOG-G02b}
```
```math
\eta^i=\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\epsilon^i
-\frac g2L_c^{ij}\epsilon_j.
\tag{LOG-G02c}
```

$`\delta\sigma=\Lambda_D\sigma+i\bar\epsilon\psi/2=0`$ fixes
$`\Lambda_D=0`$ on this gauge. Consequently the $`b_\mu`$ equation is

```math
0=\frac i2\bar\epsilon\phi_\mu-2\bar\epsilon\gamma_\mu\chi
+\frac i2\bar\eta\psi_\mu+2\Lambda_{K\mu},\qquad
\Lambda_{K\mu}=-\frac i4\bar\epsilon\phi_\mu
+\bar\epsilon\gamma_\mu\chi-\frac i4\bar\eta\psi_\mu.
\tag{LOG-G02d}
```

For the compensator orientation set $`n^{ij}=\delta^{ij}/\sqrt2`$,
$`n_{ij}n^{ij}=1`$. The exact defining equation for the broken R-symmetry
compensators is

```math
0=(\delta^{(i}_k\delta^{j)}_l-n^{ij}n_{kl})
\left[i\bar\epsilon^{(k}\varphi_c^{l)}
+2\Lambda_U^{(k}{}_m L_c^{l)m}\right].
\tag{LOG-G02e}
```

The component along $`n^{ij}`$ gives $`\delta L`$, and the unbroken U(1) parameter
remains free. These equations are fully specified reusable inputs. Expanding all
combined field transformations, reconciling the potential law and proving their
closure is still a construction/verification task; it is not certified here.

#### LOG-G03 — Couplings, weights and the action convention

The definition for this branch is

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,
\left(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\rm LOG}\right),\qquad
[\kappa_5^2]=-3,\quad[\lambda_{\rm LOG}]=-2.
\tag{LOG-G03}
```

Square brackets are engineering mass dimensions after fixing the compensator
scale; Weyl weights before that fixing are a different grading. The overall
Newton factor is a declared branch convention. $`\lambda_{\rm LOG}`$ multiplies
the G25-normalized invariant directly: its bosonic curvature-only coefficients
are $`-R_{ab}R^{ab}/6+R^2/24`$. A coefficient multiplying raw S23 BF before the
full field/linear-slot conversion is a different parameter until that conversion
has been checked. Do not borrow the factor $`-2`$ from a Weyl or two-derivative
branch. We do not claim the full raw-S23-to-G25 fermionic density normalization
has been verified merely by matching the curvature-only part.

Before gauge fixing, $`w(g)=0`$, $`w(\sigma)=1`$, $`w(L_c)=3`$,
$`w(N_c)=w(E_{ca})=4`$, $`w(\varphi_c)=7/2`$, and the BF density has weight5.
In the unrescaled gauge-fixed G25 frame, the engineering assignments useful for
checking LOG-B03 are
$`[\nabla]=[g]=[G_{ab}]=[H_{ab}]=[N_c]=[E_{ca}]=[V_a]=1`$,
$`[L]=0`$, $`[R]=[V_{ab}^{ij}]=2`$.
The compensator scale relates these assignments to the conformal weights;
they must not be interchanged inside a pre-gauge formula.

#### LOG-G04 — Bosonic form conventions and shorthand

G25 notation immediately below (8), PDF7; CO (5.5)–(5.8), PDF17:

```math
\begin{gathered}
G=dC,\qquad H=dB+\tfrac12C\wedge G+\tfrac g2E_c,\qquad
dH=\tfrac12G\wedge G+\tfrac g2dE_c,\\
H^{ab}=-\tfrac1{12}\epsilon^{abcde}H_{cde},\qquad
H_{abc}=\epsilon_{abcde}H^{de},\qquad
T_{ab}\big|_{\sigma=1,\mathrm{bos}}=\tfrac18(G_{ab}-2H_{ab}),\\
H^2=H_{ab}H^{ab},\quad G^2=G_{ab}G^{ab},\quad
H^2_{ab}=H_a{}^cH_{bc},\quad G^2_{ab}=G_a{}^cG_{bc},\\
H^4=H^{2ab}H^2_{ab},\qquad G^4=G^{2ab}G^2_{ab},\qquad
L^2=L_c^{ij}L_{c\,ij}.
\end{gathered}\tag{LOG-G04}
```

The source two-form $`H_{ab}`$ equals $`-\tfrac12(\star H_3)_{ab}`$ with the
stated epsilon tensor. It is neither the three-form potential nor its field
strength. The inverse follows from C01: the contracted epsilons give $`-2!3!`$,
whose product with $`-1/12`$ is +1. The last scalar is the square of the gauge-fixed
$`L`$ in LOG-G01, since $`\delta^{ij}\delta_{ij}=2`$.

#### LOG-G05 — Bosonic covariant derivative and R curvature

G25 (2), PDF5, and notation following (8), PDF7:

```math
\nabla_a=e_a{}^\mu(\partial_\mu-\omega_\mu{}^{bc}M_{bc}
-b_\mu\mathbb D-V_\mu^{ij}U_{ij}),\qquad
V_{ab}^{ij}=2e_a{}^\mu e_b{}^\nu\partial_{[\mu}V_{\nu]}^{ij}
-2V_{[a}^{k(i}V_{b]k}^{j)}.
\tag{LOG-G05}
```

$`\mathbb D`$ is the dilatation generator, not the auxiliary scalar D.
This is the bosonic derivative of the G25 displayed action. It does not replace
the full superconformal derivative G01/GC21 in fermionic calculations.
Even after LOG-G01, $`\nabla_a L_c^{ij}`$ includes the R-connection acting on
both triplet indices; a constant value of L does not remove that connection.

#### LOG-B01 — Literal bosonic G25 map (1)

Source: G25 PDF4–5. These are the **bosonic restriction** of the map; no
omitted fermions are set to zero inside the full action. GG03–GG05 supply the
scoped full project realization to be transported through the Gold bridge.

```math
\begin{aligned}
Y^{ij}_{\rm bos}&=-\frac g{2\sigma}L_c^{ij},\\
T_{ab}^{\rm bos}&=\frac1{8\sigma}G_{ab}
+\frac1{48\sigma^2}\epsilon_{abcde}H^{cde},\\
D_{\rm bos}&=\frac1{4\sigma}\nabla^a\nabla_a\sigma
+\frac1{8\sigma^2}\nabla^a\sigma\nabla_a\sigma-\frac1{32}R
-\frac1{16\sigma^2}G^{ab}G_{ab}
-\left(\frac{26}{3}T^{ab}-\frac2\sigma G^{ab}\right)T_{ab}
+\frac g{4\sigma^2}N_c+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{LOG-B01}
```

The $`-R/32`$ agrees with the bosonic $`f_a{}^a/2`$ from D02, since R03 gives
$`f_a{}^a=-R/16`$. Keep the full superconformal box in the fermionic realization.

#### LOG-B02 — Defining vector, G25 (4)

G25 PDF5–6 supplies the fourth slot including its explicit fermions:

```math
(\rho,A_\mu,\lambda^i,Y^{ij})=
\left(\sigma,C_\mu,\psi^i,
\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\right).
\tag{LOG-B02}
```

This map is used only after forming the Standard-Weyl BF invariant. It is not
S23's LOG composite, and the independent compensator $`L_c`$ is not $`L_{\log}`$.

<a id="boundary"></a>

## Equality, integrations by parts and boundary conventions

**Extraction:** [results/gauged_full_fermionic_log/CONVENTIONS.md](LOG_MASTER.md), lines 2697–2708; frozen input. Source wording follows; its scope labels remain in force.

#### LOG-G07 — Equality and boundary conventions

Write exact local equalities with $`=`$. For integration by parts, write the
current explicitly:
$`e\ell_1-e\ell_2=\partial_\mu(eJ^\mu)`$.
Write $`\ell|_{\rm gauge}`$, $`\ell|_{\rm bos}`$ or
$`\ell+O(\text{fermion}^{n})`$ whenever that restriction is used. No field
equation of the final higher-derivative theory is permitted merely because a
field was auxiliary in the two-derivative theory. Grassmann variations use
left functional derivatives if Euler equations are later formed, with the odd
variation moved to the left before reading its coefficient.

<a id="gauge-derivatives"></a>

## Ordered gauge-fixed derivatives, Hessians and conformal boxes

**Extraction:** results/gauged_full_fermionic_log/STEP_07_COMPOSITES_SUBSTITUTED_CURVATURES_COMPACT.md, lines 40–486; frozen input. Source wording follows; its scope labels remain in force.

### 2. Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, source_lock=GAUGED-LOG-CONVENTIONS-v1 -->

Tangent/world indices run over five dimensions, spinor indices over four components, and $`i,j=1,2`$. Use $`\eta=(-,+,+,+,+)`$, $`\epsilon^{01234}=1`$, $`\gamma^{01234}=i`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, and unit-weight (anti)symmetrization. The Majorana bar is linear, $`\bar u=u^T\mathsf C`$, including on a coefficient $`i`$; spinors are odd. Right lowering is $`u_i=u^j\varepsilon_{ji}`$ with $`\varepsilon_{12}=\varepsilon^{12}=1`$. The fixed-doublet bilinear exchange signs for gamma rank $`0,1,2`$ are $`+,+,-`$; a contracted doublet reversal supplies its separate minus.

Use the project Riemann sign $`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$. The Ricci contraction is fixed by (SC7-06). Before gauge evaluation the conformal weights of $`(\sigma,\psi^i,\widehat G,\widehat H_{ab},L_c,\varphi_c,N_c,g)`$ are $`(1,3/2,2,3,3,7/2,4,0)`$. On the fixed scale their engineering dimensions are $`(0,1/2,1,1,0,1/2,1,1)`$; $`\mathcal D_a`$ has dimension one. The LOG slots have dimensions $`3,7/2,4,4`$. The coupling is $`S=(2\kappa_5^2)^{-1}\int e(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\log})`$, $`[\lambda_{\rm LOG}]=-2`$.

There is one component derivative convention throughout the active calculation: $`\mathcal D_a`$ is full and supercovariant. $`D`$ without an index is the auxiliary scalar; it is never a derivative. Gold's $`\nabla_A`$ remains its source superspace notation in the earlier superspace derivations; the bridge is applied once at Step 6. Fourier/state normalization and renormalization are not involved.

### 3. Definitions and Required Identities

#### 3.1 Full derivative, box and gauge evaluation

The Weyl-squared definition GC21 is used verbatim in meaning:

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad \mathcal D_a=e_a{}^\mu\mathcal D_\mu,\qquad \Box^c\Phi:=\mathcal D^a\mathcal D_a\Phi.
\tag{SC7-01}
```

Each generator acts on the actual field or descendant to its right. For example, in $`\mathcal D_a\mathcal D_b\Phi`$ the outer derivative acts on the tangent index $`b`$ and the Q/S/K transformation of $`\mathcal D_b\Phi`$. The superscript $`c`$ means conformal; it is not an index or a fermion-order label. Adjacent contracted derivatives alone are abbreviated by $`\Box^c`$. Ordered expressions such as $`\mathcal D^a\mathcal D_b\mathcal D_a\Phi`$ stay in that order. The use of this operator does not import the Weyl-squared composite or its normalization.

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad L_c^{ij}=\frac{L}{\sqrt2}\delta^{ij},\qquad V_\mu{}^{ij}=V'_\mu{}^{ij}+\frac12\delta^{ij}V_\mu .
\tag{SC7-02}
```

**Evaluation convention for every final formula:** $`\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi`$ means $`(\mathcal D_{a_1}\cdots\mathcal D_{a_n}\Phi)|_{\rm gauge}`$, with all derivatives taken before (SC7-02). We suppress the repeated vertical bar in §6. The symbols $`\sigma`$ and $`\psi^i`$ there occur only inside such derivatives. They introduce no independent scalar or dilatino after gauge fixing. In particular,

```math
\mathcal D_a\sigma|_{\rm gauge}=0,\qquad
\mathcal D_a\psi^i|_{\rm gauge}=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\phi_a^i,\qquad
\Box^c\sigma|_{\rm gauge}=2f_a{}^a-\frac i2\bar\psi_a\mathcal D^a\psi-2\bar\psi_a\gamma^a\chi.
\tag{SC7-03}
```

These are definitions for interpreting surviving descendants, not extra terms to add to a density already written with full derivatives. Master GC14, GC16 supply them. Section 4.4 gives the explicit first derivatives, Hessians and boxes, with the connection contributions evaluated. Higher ordered descendants remain full operators with the same inherited transformation law; they are not obtained by differentiating the numerical gauge values as ordinary functions.

The independent compensator has, in this notation,

```math
\mathcal D_aL_c^{ij}=\frac{\delta^{ij}}{\sqrt2}\partial_aL+\frac{L}{\sqrt2}\left(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\right)-i\bar\psi_a^{(i}\varphi_c^{j)}.
\tag{SC7-04}
```

The last term is retained implicitly whenever $`\mathcal D_aL_c^{ij}`$ occurs in §6. Constant $`L`$ does not remove the connection terms. The source is Weyl GC24/master L02.

#### 3.2 Strengths, curvature constraints and dependent connections

The strength conventions at the gauge are

```math
\widehat G_{\mu\nu}=2\partial_{[\mu}C_{\nu]}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\qquad
\widehat H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}+\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{c\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\qquad
\widehat H_{ab}:=-\frac1{12}\epsilon_{abcde}\widehat H^{cde}.
\tag{SC7-05}
```

When differentiated, the hats mean the full definitions before gauge evaluation, Weyl GC03. In particular $`\widehat G`$ before the gauge also contains $`-\bar\psi_{[\mu}\gamma_{\nu]}\psi`$ and the coefficient of its gravitino bilinear is $`i\sigma/2`$; the three-form includes $`-3i\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi/2`$ and the coefficient $`-3\sigma^2/4`$. Their undifferentiated dilatino terms vanish at the gauge, but are part of the inherited derivative definitions.

The conventional constraints are $`R(P)=0`$, $`\gamma^a\widehat R(Q)_{ab}^i=0`$, and $`\widehat R(M)_{acb}{}^c=0`$. Their connection solutions are

```math
\begin{aligned}
\omega_\mu{}^{ab}&=\omega_\mu{}^{ab}(e)+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu+\frac14\bar\psi^a\gamma_\mu\psi^b,\qquad
\phi_a^i=\frac i3\gamma^b\widehat R'(Q)_{ab}^i-\frac i{24}\gamma_a\gamma^{bc}\widehat R'(Q)_{bc}^i,\\
f_{ab}&=-\frac16\mathcal R_{ab}+\frac1{48}\eta_{ab}\mathcal R,\qquad f_a{}^a=-\frac1{16}\mathcal R,\qquad
\mathcal R_{\mu\nu}:=\widehat R'(M)_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a},\quad\mathcal R:=\mathcal R_\mu{}^\mu .
\end{aligned}\tag{SC7-06}
```

Here $`\widehat R'(Q)=\widehat R(Q)+2i\gamma_{[a}\phi_{b]}`$ and $`\widehat R'(M)=\widehat R(M)-8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}`$ omit the S and K connections respectively. Master GC18–GC20 define the primed curvatures before those connections are inserted, including the project-corrected $`+8\bar\psi e\gamma\chi`$ term. The trace follows directly from $`-1/6+5/48=-1/16`$. No trace constraint is imposed on $`R'(Q)`$ or $`\mathcal R_{ab}`$.

For consistency with the Weyl calculation, hats on the three retained curvatures are printed in §6; $`\widehat C_{abcd}=\widehat R(M)_{abcd}`$. Curvatures keep their full gauged definitions, and no field-strength or curvature is expanded into a connection polynomial there.

#### 3.3 Gauged composite identities before differentiation

The identities to be substituted, before (SC7-02), are

```math
\begin{aligned}
Y^{ij}&=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}-\frac g{2\sigma}L_c^{ij},\qquad
T_{ab}=\frac{\widehat G_{ab}}{8\sigma}-\frac{\widehat H_{ab}}{4\sigma^2}+\frac{i}{32\sigma^2}\bar\psi\gamma_{ab}\psi,\\
\chi^i&=\frac i{8\sigma}\gamma^a\mathcal D_a\psi^i+\frac i{16\sigma^2}\gamma^a(\mathcal D_a\sigma)\psi^i-\frac1{32\sigma^2}\gamma^{ab}\widehat G_{ab}\psi^i+\frac1{4\sigma}\gamma^{ab}T_{ab}\psi^i-\frac g{16\sigma^3}L_c^{ij}\psi_j+\frac g{8\sigma^2}\varphi_c^i+\text{high fermi terms},\\
D&=\frac1{4\sigma}\Box^c\sigma+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)-\frac1{16\sigma^2}\widehat G^2-\frac1{8\sigma^2}\bar\psi\gamma^a\mathcal D_a\psi+\frac1{4\sigma^2}Y^{ij}Y_{ij}+\frac i{4\sigma^2}T_{ab}\bar\psi\gamma^{ab}\psi-\frac{4i}{\sigma}\bar\psi\chi-\frac{26}{3}T^2+\frac2\sigma\widehat G_{ab}T^{ab}+\frac g{4\sigma^2}N_c.
\end{aligned}\tag{SC7-07}
```

The $`Y`$ and $`T`$ identities are complete. Only the cubic term of $`\chi`$ is suppressed here; its full expression is master GC08. Inserting $`Y,T,\chi`$ recursively in $`D`$ generates the full even identity through degree two. Differentiation is even and does not reduce total fermion degree, so discarded cubic/quartic pieces cannot feed the retained slots. The two-index $`\widehat H`$ is only the conventional dual in (SC7-05); it is unrelated to the LOG triplet.

### 4. Detailed Derivation

#### 4.1 Recover the gauge values without changing the derivative

Set $`\sigma=1`$, undifferentiated $`\psi^i=0`$, and $`\mathcal D_a\sigma=0`$ in (SC7-07), retaining its differentiated spinor and conformal box. This gives

```math
Y^{ij}=-\frac g2L_c^{ij},\qquad T_{ab}=\frac18(\widehat G_{ab}-2\widehat H_{ab}),\qquad
\chi^i=\frac i8\gamma^a\mathcal D_a\psi^i+\frac g8\varphi_c^i.
\tag{SC7-08}
```

For $`D`$, insert $`T=(\widehat G-2\widehat H)/8`$ into its three flux terms. Their coefficients are

```math
\begin{aligned}
-\frac1{16}\widehat G^2-\frac{26}{3}T^2+2\widehat G_{ab}T^{ab}
&=\left(-\frac1{16}-\frac{13}{96}+\frac14\right)\widehat G^2+\left(\frac{13}{24}-\frac12\right)\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2\\
&=\frac5{96}\widehat G^2+\frac1{24}\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2.
\end{aligned}\tag{SC7-09}
```

Since $`Y^{ij}Y_{ij}=g^2L_c^{ij}L_{cij}/4`$, the scalar composite is

```math
D=\frac14\Box^c\sigma+\frac5{96}\widehat G^2+\frac1{24}\widehat G_{ab}\widehat H^{ab}-\frac{13}{24}\widehat H^2+\frac g4N_c+\frac{g^2}{16}L_c^{ij}L_{cij}.
\tag{SC7-10}
```

Its curvature and gravitino terms are inside $`\Box^c\sigma`$. Using (SC7-03) only to identify them gives $`\Box^c\sigma=-\mathcal R/8-i\bar\psi_a\mathcal D^a\psi/2-2\bar\psi_a\gamma^a\chi`$. This relation is not applied to expand the final component collection.

#### 4.2 Differentiate before evaluating the gauge

The even covariant derivative obeys

```math
\mathcal D_a(UV)=(\mathcal D_aU)V+U\mathcal D_aV,\qquad
\mathcal D_a\sigma^{-n}=-n\sigma^{-n-1}\mathcal D_a\sigma,
\tag{SC7-11}
```

and, without interchanging derivatives or fermions,

```math
\mathcal D_a\mathcal D_b(UV)=(\mathcal D_a\mathcal D_bU)V+(\mathcal D_bU)(\mathcal D_aV)+(\mathcal D_aU)(\mathcal D_bV)+U\mathcal D_a\mathcal D_bV.
\tag{SC7-12}
```

For example, first differentiating $`Y`$ in (SC7-07) gives

```math
\begin{aligned}
\mathcal D_bY^{ij}={}&-\frac{i}{4\sigma^2}(\mathcal D_b\sigma)\bar\psi^i\psi^j+\frac i{4\sigma}\left[\overline{\mathcal D_b\psi^i}\psi^j+\bar\psi^i\mathcal D_b\psi^j\right]
+\frac g{2\sigma^2}(\mathcal D_b\sigma)L_c^{ij}-\frac g{2\sigma}\mathcal D_bL_c^{ij}.
\end{aligned}\tag{SC7-13}
```

Its value at the gauge is $`-g\mathcal D_bL_c^{ij}/2`$. Apply the second derivative to (SC7-13), rather than to this gauge value. The factors of undifferentiated $`\psi`$ and first $`\mathcal D\sigma`$ vanish only after that operation. The surviving terms are

```math
\mathcal D_a\mathcal D_bY^{ij}=-\frac g2\mathcal D_a\mathcal D_bL_c^{ij}+\frac g2L_c^{ij}\mathcal D_a\mathcal D_b\sigma
+\frac i4\left[\overline{\mathcal D_b\psi^i}\mathcal D_a\psi^j+\overline{\mathcal D_a\psi^i}\mathcal D_b\psi^j\right]+\text{high fermi terms}.
\tag{SC7-14}
```

The two spinors stay in their original order; no Grassmann interchange is used. Contracting $`a,b`$ is permitted only after retaining these terms.

For $`T`$, the first derivative of the full identity is

```math
\begin{aligned}
\mathcal D_bT_{cd}={}&\frac1{8\sigma}\mathcal D_b\widehat G_{cd}-\frac1{8\sigma^2}(\mathcal D_b\sigma)\widehat G_{cd}-\frac1{4\sigma^2}\mathcal D_b\widehat H_{cd}+\frac1{2\sigma^3}(\mathcal D_b\sigma)\widehat H_{cd}\\
&+\frac i{32\sigma^2}\left[\overline{\mathcal D_b\psi}\gamma_{cd}\psi+\bar\psi\gamma_{cd}\mathcal D_b\psi\right]-\frac i{16\sigma^3}(\mathcal D_b\sigma)\bar\psi\gamma_{cd}\psi.
\end{aligned}\tag{SC7-15}
```

Differentiating this and then evaluating the gauge gives

```math
\begin{aligned}
\mathcal D_aT_{bc}&=\frac18\mathcal D_a\widehat G_{bc}-\frac14\mathcal D_a\widehat H_{bc},\\
\mathcal D_a\mathcal D_bT_{cd}&=\frac18\mathcal D_a\mathcal D_b\widehat G_{cd}-\frac14\mathcal D_a\mathcal D_b\widehat H_{cd}-\frac18(\mathcal D_a\mathcal D_b\sigma)\widehat G_{cd}+\frac12(\mathcal D_a\mathcal D_b\sigma)\widehat H_{cd}\\
&\quad+\frac i{32}\left[\overline{\mathcal D_b\psi}\gamma_{cd}\mathcal D_a\psi+\overline{\mathcal D_a\psi}\gamma_{cd}\mathcal D_b\psi\right]+\text{high fermi terms}.
\end{aligned}\tag{SC7-16}
```

For the spinor composite, differentiation of the six retained terms in (SC7-07) leaves, on the gauge,

```math
\begin{aligned}
\mathcal D_c\chi^i={}&\frac i8\gamma^a\mathcal D_c\mathcal D_a\psi^i-\frac1{32}\gamma^{ab}\widehat G_{ab}\mathcal D_c\psi^i+\frac14\gamma^{ab}T_{ab}\mathcal D_c\psi^i-\frac g{16}L_c^{ij}\mathcal D_c\psi_j+\frac g8\mathcal D_c\varphi_c^i+\text{high fermi terms}\\
={}&\frac i8\gamma^a\mathcal D_c\mathcal D_a\psi^i-\frac1{16}\gamma^{ab}\widehat H_{ab}\mathcal D_c\psi^i-\frac g{16}L_c^{ij}\mathcal D_c\psi_j+\frac g8\mathcal D_c\varphi_c^i+\text{high fermi terms}.
\end{aligned}\tag{SC7-17}
```

The $`\widehat G`$ coefficient cancels because $`-1/32+(1/4)(1/8)=0`$. The second and third terms in the last line would be lost by differentiating only the gauge value in (SC7-08). The subscript c on $`\varphi_c,L_c`$ labels the independent compensator, while a derivative index $`c`$ is a tangent index.

For $`\mathcal D_eD`$, the scalar product-rule contributions from the two fermionic terms in (SC7-07) are

```math
\begin{aligned}
-\frac18\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-4i\overline{\mathcal D_e\psi}\chi
&=\left(-\frac18+\frac12\right)\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c\\
&=\frac38\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c.
\end{aligned}\tag{SC7-18}
```

The coefficient $`+1/2`$ is $`(-4i)(i/8)`$. The other derivatives of terms containing undifferentiated $`\psi`$ or $`\mathcal D\sigma`$ vanish on this first-derivative evaluation. Differentiating the flux products and $`Y^2`$ gives the complete retained expression

```math
\begin{aligned}
\mathcal D_eD={}&\frac14\mathcal D_e\Box^c\sigma+\frac5{48}\widehat G^{ab}\mathcal D_e\widehat G_{ab}+\frac1{24}\left(\widehat H^{ab}\mathcal D_e\widehat G_{ab}+\widehat G^{ab}\mathcal D_e\widehat H_{ab}\right)-\frac{13}{12}\widehat H^{ab}\mathcal D_e\widehat H_{ab}\\
&+\frac g4\mathcal D_eN_c+\frac{g^2}{8}L_{cij}\mathcal D_eL_c^{ij}+\frac38\overline{\mathcal D_e\psi}\gamma^a\mathcal D_a\psi-\frac{ig}{2}\overline{\mathcal D_e\psi}\varphi_c+\text{high fermi terms}.
\end{aligned}\tag{SC7-19}
```

The superscript $`c`$ in $`\Box^c`$ is its fixed conformal label, not the free derivative index $`e`$. These four product-rule identities are checked against independent explicitly entered expressions with zero exact coefficient residual.

#### 4.3 Substitute into the LOG slots and canonicalize

Every occurrence of $`Y,T,\chi,D`$, including ordered derivatives of them, is processed by (SC7-07), (SC7-11) and (SC7-12) before applying (SC7-02). There are no explicit gravitino-connection additions to this operation: they already belong to $`\mathcal D`$. For example, the original triplet term $`2\sigma^{-1}\Box^cY^{ij}`$ becomes

```math
2\sigma^{-1}\Box^cY^{ij}|_{\rm gauge}=-g\Box^cL_c^{ij}+gL_c^{ij}\Box^c\sigma+i\overline{\mathcal D_a\psi^i}\mathcal D^a\psi^j.
\tag{SC7-20}
```

Both contracted bilinears in (SC7-14) are identical by dummy relabeling and metric contraction, with no spinor exchange. The coefficient is $`2(i/4)\cdot2=i`$. Other original triplet terms supply the remaining coefficients in §6.1; (SC7-20) is this one input term, not the whole triplet.

Dummy names are then normalized and inverse metrics contracted. Clifford chains use

```math
\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab},\qquad
\gamma^{ab}\gamma^c=\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b,\qquad
\gamma^{abc}=-\frac i2\epsilon^{abcde}\gamma_{de},\quad\gamma^{abcd}=i\epsilon^{abcde}\gamma_e.
\tag{SC7-21}
```

The general recursion and epsilon-pair reductions are canonical CTF-07–CTF-12. The fixed-doublet spinor exchange uses $`\bar u\Gamma_pv=-\tau_p\bar v\Gamma_pu`$, where $`\tau_p=(-1,-1,+1)`$ for ranks $`0,1,2`$. These signs are applied before collecting equal monomials. The curvature trace rules are

```math
\gamma^a\widehat R(Q)_{ab}=0,\qquad
\gamma^{ac}\widehat R(Q)_{ab}=\widehat R(Q)^c{}_b,\qquad
\overline{\widehat R(Q)_{ab}}\gamma^{ac}=-\overline{\widehat R(Q)^c{}_b},\qquad
\widehat R(M)_{acb}{}^c=0.
\tag{SC7-22}
```

The rank-two identity follows from $`\gamma^{ac}=\eta^{ac}-\gamma^c\gamma^a`$; its bar has the rank-two transpose sign. The metric and gamma tensors are covariantly constant, so an ordered full derivative of these zero constraints is also zero. No derivative permutation is used. All four output slots pass a second full algebraic reduction with zero coefficient difference.

<a id="gauge-fixed-derivatives"></a>

#### 4.4 Gauge-fixed derivative dictionary — reference only

This section supplies the gauge-evaluated derivatives that were left implicit in (SC7-03). **None of these formulas is inserted into the LOG multiplet or the BF density in §6.** Throughout this section a vertical bar means (SC7-02), after taking the indicated full supercovariant derivatives. The dilatino is $`\psi^i`$; the gravitino is $`\psi_a^i`$. The S connection is $`\phi_a^i`$; the independent compensator spinor is $`\varphi_c^i`$.

**Sources and scope.** First derivatives: Weyl-squared GC14, equivalently master V01–V03 and OP (2.14)–(2.16). Scalar box: Weyl-squared GC16. Connection solutions and transformations: Weyl-squared GC18–GC20 and master R04a–R04c, anchored to W (3.9)–(3.12), (3.20)–(3.21). The Hessians and spinor box below are derived from these definitions. They are off shell, retain two fermions for the scalar and one for the spinor, and use no integration by parts or background equation. Higher omitted degrees are denoted $`+\text{high fermi terms}`$. The truncation is a formal fermion-degree truncation, not a small-curvature approximation.

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), gamma_volume=+i, bar=linear Majorana, derivative=full supercovariant mathcal D, derivative_order=preserved, gauge_evaluation=after differentiation -->

##### 4.4.1 First derivatives and the Dirac derivative

Begin with the ungauge-fixed GC14 formula rather than with the numerical gauge values:

```math
\begin{aligned}
\mathcal D_a\sigma&=(\partial_a-b_a)\sigma-\frac i2\bar\psi_a\psi,\\
\mathcal D_a\psi^i&=e_a{}^\mu\left[\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\psi^i-V_\mu{}^{ij}\psi_j\right]+\frac14\gamma\!\cdot\!\widehat G\,\psi_a^i+\frac i2\gamma^b\mathcal D_b\sigma\,\psi_a^i+\frac i{4\sigma}\psi_{aj}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\psi_{aj}-\sigma\gamma\!\cdot\!T\,\psi_a^i-\sigma\phi_a^i.
\end{aligned}\tag{SC7D-01}
```

Here $`\partial_a=e_a{}^\mu\partial_\mu`$ occurs only inside an explicitly written definition; it does not replace $`\mathcal D_a`$. Substituting the gauge values removes the first bracket, $`\mathcal D_b\sigma`$ and the dilatino bilinear. The flux coefficient is $`\widehat G/4-(\widehat G-2\widehat H)/8=(\widehat G+2\widehat H)/8`$. Thus

```math
\boxed{\left.\mathcal D_a\sigma\right|=0,\qquad \left.\mathcal D_a\psi^i\right|=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\phi_a^i.}\tag{SC7D-02}
```

Inserting the gamma-trace constraint solution for $`\phi_a`$ from (SC7-06) gives its explicit curvature form:

```math
\left.\mathcal D_a\psi^i\right|=\frac18\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\psi_{aj}-\frac i3\gamma^b\widehat R'(Q)_{ab}^i+\frac i{24}\gamma_a\gamma^{bc}\widehat R'(Q)_{bc}^i.
\tag{SC7D-03}
```

The prime is essential: the gamma-trace constraint applies to $`\widehat R(Q)`$, not to $`\widehat R'(Q)`$. Contracting the solved connection first gives $`\gamma^a\phi_a=i(1/3-5/24)\gamma^{ab}\widehat R'(Q)_{ab}=i\gamma^{ab}\widehat R'(Q)_{ab}/8`$. Therefore

```math
\boxed{\left.\not{\mathcal D}\psi^i\right|=\frac18\gamma^a\gamma^{bc}(\widehat G_{bc}+2\widehat H_{bc})\psi_a^i-\frac g2L_c^{ij}\gamma^a\psi_{aj}-\frac i8\gamma^{ab}\widehat R'(Q)_{ab}^i.}\tag{SC7D-04}
```

This also gives $`\chi^i=(i/8)(\not{\mathcal D}\psi^i)|+g\varphi_c^i/8`$ in (SC7-08), with no additional projection factor.

##### 4.4.2 Scalar Hessian and conformal box

The transformations of the first scalar descendant, evaluated only after taking the variation, are

```math
\left.\delta_Q(\epsilon)\mathcal D_b\sigma\right|=\frac i2\bar\epsilon\left.\mathcal D_b\psi\right|+2\bar\epsilon\gamma_b\chi,\qquad
\left.\delta_S(\eta)\mathcal D_b\sigma\right|=0,\qquad
\left.\delta_K(\Lambda_K)\mathcal D_b\sigma\right|=-2\Lambda_{Kb}.
\tag{SC7D-05}
```

The $`2\chi`$ term comes from $`-\sigma\delta_Qb_b`$ in W01; the $`-2\Lambda_{Kb}`$ term comes from the K variation of that same connection. The terms in $`\delta_Qb_b`$ and $`\delta_Q\psi_b`$ proportional to $`\phi_b`$ combine with the spinor derivative in (SC7D-02). The S law before the gauge is proportional to the dilatino and hence vanishes here. These are transformations of the **unfixed descendant**, not supersymmetry transformations tangent to the gauge slice.

The partial, Lorentz and dilatation contributions to the outer derivative of $`\mathcal D_b\sigma`$ vanish on this gauge because its gauge value is identically zero. In (SC7-01) the negative Q variation gives the first two fermionic terms, and the negative K variation gives $`+2f_{ab}`$. Consequently,

```math
\left.\mathcal D_a\mathcal D_b\sigma\right|=2f_{ab}-\frac i2\bar\psi_a\left.\mathcal D_b\psi\right|-2\bar\psi_a\gamma_b\chi
=-\frac13\mathcal R_{ab}+\frac1{24}\eta_{ab}\mathcal R-\frac i2\bar\psi_a\left.\mathcal D_b\psi\right|-\frac i4\bar\psi_a\gamma_b\gamma^c\left.\mathcal D_c\psi\right|-\frac g4\bar\psi_a\gamma_b\varphi_c.
\tag{SC7D-06}
```

The second equality uses both solved composites, $`f_{ab}`$ and $`\chi`$. It does not symmetrize $`a,b`$ or exchange their derivatives. Trace the first equality with $`\eta^{ab}`$ and use $`2f_a{}^a=-\mathcal R/8`$:

```math
\boxed{\left.\Box^c\sigma\right|=-\frac18\mathcal R-\frac i2\bar\psi_a\left.\mathcal D^a\psi\right|-\frac i4\bar\psi_a\gamma^a\gamma^b\left.\mathcal D_b\psi\right|-\frac g4\bar\psi_a\gamma^a\varphi_c.}\tag{SC7D-07}
```

For an expression with no remaining dilatino derivatives, insert (SC7D-02) into these two occurrences. Right lowering gives $`\bar\psi_a{}^i\varepsilon_{ji}L_c^{jk}\psi_{bk}=-L_c^{jk}\bar\psi_{aj}\psi_{bk}`$; this accounts for both negative $`igL_c`$ coefficients below. No two odd fields are interchanged:

```math
\begin{aligned}
\left.\Box^c\sigma\right|={}&-\frac18\mathcal R-\frac i{16}(\widehat G_{bc}+2\widehat H_{bc})\bar\psi_a\gamma^{bc}\psi^a-\frac{ig}{4}L_c^{ij}\bar\psi_{ai}\psi^a{}_j+\frac i2\bar\psi_a\phi^a\\
&-\frac i{32}(\widehat G_{cd}+2\widehat H_{cd})\bar\psi_a\gamma^a\gamma^b\gamma^{cd}\psi_b-\frac{ig}{8}L_c^{ij}\bar\psi_{ai}\gamma^a\gamma^b\psi_{bj}+\frac i4\bar\psi_a\gamma^a\gamma^b\phi_b-\frac g4\bar\psi_a\gamma^a\varphi_c+\text{high fermi terms}.
\end{aligned}\tag{SC7D-08}
```

All $`\phi_a`$ in this reference formula have the solved relation (SC7-06); $`\mathcal R_{ab}`$ is the retained primed curvature contraction. Thus neither introduces an independent field. Equation (SC7D-08) expands the derivative definition only, and is not a replacement performed in §6.

##### 4.4.3 Transformations needed for the spinor Hessian

At one-fermion order the connection parameters $`\psi_a,\phi_a`$ multiply the **bosonic** Q/S transformations of $`\mathcal D_b\psi`$. It is enough to determine those transformations at degree zero; their degree-two corrections would contribute three fermions. Temporarily keep the source composites $`Y^{ij}=-gL_c^{ij}/2`$ and $`T_{ab}=(\widehat G_{ab}-2\widehat H_{ab})/8`$ visible to show the origin of each term.

The bosonic part of the S-connection variation follows from its defining projector (SC7-06). Varying the primed gravitino curvature first gives

```math
\begin{aligned}
\left.\delta_Q\widehat R'(Q)_{ab}^i\right|_{0}={}&\frac14R_{ab}{}^{cd}(\omega)\gamma_{cd}\epsilon^i-\widehat R(V)_{ab}^{ij}\epsilon_j
+i\left[(\mathcal D_a\gamma\!\cdot\!T)\gamma_b-(\mathcal D_b\gamma\!\cdot\!T)\gamma_a\right]\epsilon^i-\left[\gamma\!\cdot\!T\gamma_a,\gamma\!\cdot\!T\gamma_b\right]\epsilon^i,\\
\left.\delta_Q\phi_b^i\right|_0={}&\frac i3\gamma^c\left.\delta_Q\widehat R'(Q)_{bc}^i\right|_0-\frac i{24}\gamma_b\gamma^{cd}\left.\delta_Q\widehat R'(Q)_{cd}^i\right|_0 .
\end{aligned}\tag{SC7D-09}
```

Here the label $`0`$ counts dynamical fermions, excluding the variation parameter. To obtain the first line, substitute $`\delta_Q\psi_a=(\partial_a+\omega_a\gamma/4-V_a)\epsilon+i\gamma\!\cdot\!T\gamma_a\epsilon`$ into GC18. The terms containing one derivative of $`\epsilon`$ from differentiating $`T\gamma\epsilon`$ cancel those from the explicit $`T\gamma\delta\psi`$ connection; two derivatives leave $`R(\omega)/4-\widehat R(V)`$. The product of the two $`iT`$ terms gives the displayed negative commutator. Frame variations and variations of $`T`$ multiplying a gravitino have two dynamical fermions and are outside this bosonic transformation.

In the second line, the gamma variation likewise multiplies a fermionic curvature and contributes only at degree two. Applying that projector to the curvature, derivative and $`T^2`$ terms separately gives

```math
\begin{aligned}
\left.\delta_Q\phi_b^i\right|_0={}&if_b{}^c\gamma_c\epsilon^i+\frac i{12}\left(\gamma^{cd}\gamma_b-\frac12\gamma_b\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\epsilon_j\\
&+\frac13\left[\gamma^c\gamma^{de}(\mathcal D_cT_{de})\gamma_b-\gamma^{cd}\mathcal D_bT_{cd}+\gamma_b\gamma^c\mathcal D^dT_{dc}\right]\epsilon^i\\
&+i\left[-\gamma_{bcdef}T^{cd}T^{ef}+8\gamma^cT_c{}^dT_{bd}-2\gamma_bT^{cd}T_{cd}\right]\epsilon^i,\\
\left.\delta_S\phi_b^i\right|_0={}&e_b{}^\mu\left[\left(\partial_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\eta^i-V_\mu{}^{ij}\eta_j\right]+\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\eta^i.
\end{aligned}\tag{SC7D-10}
```

For the $`R(\omega)`$ contraction the trace-free Lorentz curvature drops from this projector, and the Ricci pieces give $`if_b{}^c\gamma_c`$ using (SC7-06). For the other contractions use $`\gamma^{cd}\gamma_b=\gamma_b{}^{cd}-2\delta_b{}^{[c}\gamma^{d]}`$, $`\gamma_b\gamma^{cd}=\gamma_b{}^{cd}+2\delta_b{}^{[c}\gamma^{d]}`$, and (SC7-21). The first identity includes the contracted antisymmetric tensor; in particular $`T_{cd}\gamma^{cd}\gamma_b=T_{cd}\gamma_b{}^{cd}-2T_{bc}\gamma^c`$. These gamma projections are checked componentwise in the verification described in §5. The $`\widehat R(V)`$ coefficient is **positive** in the all-upper triplet notation: the mixed-index version of R04c has a minus sign, and $`\widehat R(V)^i{}_j\epsilon^j=-\widehat R(V)^{ij}\epsilon_j`$ supplies the second minus.

Equation (SC7D-10) is only the bosonic part of the connection variation. It does not replace the full all-order defining variation R04b.

Now vary (SC7D-01). Terms where a bosonic field is varied and then multiplied by a dynamical spinor have degree two and do not enter this step. The ordinary derivative of $`\delta_Q\psi`$ contributes the negative derivative of $`\widehat G/4-T`$ and of $`Y`$. Its terms proportional to a derivative of the parameter cancel against those from $`\delta_Q\psi_b`$. The surviving transformations are

```math
\begin{aligned}
\left.\delta_Q(\epsilon)\mathcal D_b\psi^i\right|_0={}&-\left[\frac14\gamma^{cd}\mathcal D_b\widehat G_{cd}-\gamma^{cd}\mathcal D_bT_{cd}\right]\epsilon^i+\frac g2(\mathcal D_bL_c^{ij})\epsilon_j
+i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma\!\cdot\!T\gamma_b\epsilon^i-\frac{ig}{2}L_c^{ij}\gamma\!\cdot\!T\gamma_b\epsilon_j-\left.\delta_Q\phi_b^i\right|_0,\\
\left.\delta_S(\eta)\mathcal D_b\psi^i\right|_0={}&-i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma_b\eta^i+\frac{ig}{2}L_c^{ij}\gamma_b\eta_j-\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\eta^i,\qquad
\left.\delta_K\mathcal D_b\psi^i\right|=0.
\end{aligned}\tag{SC7D-11}
```

For S, the ordinary derivative of $`\delta_S\psi=\sigma\eta`$ cancels the ordinary derivative in $`\delta_S\phi_b`$. The K transformation of this first descendant is proportional to the undifferentiated dilatino and vanishes at the gauge. It is the Q transformation of $`\phi_b`$ that supplies the surviving $`f`$ term below.

##### 4.4.4 Full second derivative of the dilatino

For a lower tangent index, the explicit Lorentz connection is $`-\omega_a{}^c{}_b`$. In GC17, $`2\omega_a{}^c{}_{[b}T_{d]c}=-\omega_a{}^c{}_bT_{cd}-\omega_a{}^c{}_dT_{bc}`$ fixes this sign. Therefore, at the declared order,

```math
\begin{aligned}
\left.\mathcal D_a\mathcal D_b\psi^i\right|={}&e_a{}^\mu\left(\partial_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\left[\mathcal D_b\psi^i\right]_{\rm gauge}-\omega_a{}^c{}_b\left.\mathcal D_c\psi^i\right|-V_a{}^{ij}\left.\mathcal D_b\psi_j\right|\\
&+\left[\frac14\gamma^{cd}\mathcal D_b\widehat G_{cd}-\gamma^{cd}\mathcal D_bT_{cd}\right]\psi_a^i-\frac g2(\mathcal D_bL_c^{ij})\psi_{aj}-i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma\!\cdot\!T\gamma_b\psi_a^i+\frac{ig}{2}L_c^{ij}\gamma\!\cdot\!T\gamma_b\psi_{aj}+if_b{}^c\gamma_c\psi_a^i\\
&+\frac i{12}\left(\gamma^{cd}\gamma_b-\frac12\gamma_b\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\psi_{aj}+\frac13\left[\gamma^c\gamma^{de}(\mathcal D_cT_{de})\gamma_b-\gamma^{cd}\mathcal D_bT_{cd}+\gamma_b\gamma^c\mathcal D^dT_{dc}\right]\psi_a^i\\
&+i\left[-\gamma_{bcdef}T^{cd}T^{ef}+8\gamma^cT_c{}^dT_{bd}-2\gamma_bT^{cd}T_{cd}\right]\psi_a^i+i\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)\gamma_b\phi_a^i-\frac{ig}{2}L_c^{ij}\gamma_b\phi_{aj}+\frac i3\left(8\gamma^cT_{bc}-\gamma_b\gamma\!\cdot\!T\right)\phi_a^i+\text{high fermi terms}.
\end{aligned}\tag{SC7D-12}
```

The first line means a partial derivative of the **known gauge-evaluated expression (SC7D-02)** with its written Lorentz and SU(2) connections. It is not another full $`\mathcal D`$ and is not named with a competing derivative symbol. The remaining lines are exactly $`-\delta_Q(\psi_a)\mathcal D_b\psi-\delta_S(\phi_a)\mathcal D_b\psi`$ from (SC7D-10)–(SC7D-11). This states every contribution of the outer full derivative. The $`\mathcal D\widehat G`$, $`\mathcal DT`$, and $`\mathcal DL_c`$ on those lines retain the same full supercovariant meaning as elsewhere. Replacing their connection-only parts by full derivatives changes the displayed odd result only at degree three, because these differences are bilinear and each is multiplied by a gravitino.

Here is the product-rule content of the first line, without introducing a second derivative notation. Its partial-derivative contribution is

```math
\begin{aligned}
\partial_\mu\left[\mathcal D_b\psi^i\right]_{\rm gauge}={}&\frac18\gamma^{cd}\left[(\partial_\mu\widehat G_{cd}+2\partial_\mu\widehat H_{cd})\psi_b^i+(\widehat G_{cd}+2\widehat H_{cd})\partial_\mu\psi_b^i\right]\\
&-\frac g2\left[(\partial_\mu L_c^{ij})\psi_{bj}+L_c^{ij}\partial_\mu\psi_{bj}\right]-\partial_\mu\phi_b^i.
\end{aligned}\tag{SC7D-13}
```

The remaining three written connections in the first line of (SC7D-12) act on this tensor-spinor's spinor, tangent and doublet indices. They combine with (SC7D-13); neither a derivative of $`\psi^i=0`$ nor a zero scalar derivative has been substituted for that line.

##### 4.4.5 Gauge-fixed spinor box with the algebraic composites inserted

Contract $`a,b`$ in (SC7D-12). The tangent connection gives $`-\eta^{ab}\omega_a{}^c{}_b=\omega_b{}^{bc}`$ after using antisymmetry of the last two connection indices; hence the divergence contains $`+\omega_b{}^{ba}`$. Insert $`T=(\widehat G-2\widehat H)/8`$, $`\mathcal D_bT_{cd}=(\mathcal D_b\widehat G_{cd}-2\mathcal D_b\widehat H_{cd})/8`$ from (SC7-16), and the solved $`f`$ from (SC7-06). The coefficients of the flux-product, mixed-compensator, derivative-flux and flux-square terms are respectively $`-i/64`$, $`ig/16`$, $`1/24`$ and $`i/64`$. This gives the specified box explicitly:

```math
\begin{aligned}
\left.\Box^c\psi^i\right|={}&\left(\partial^a+\omega_b{}^{ba}+\frac14\omega^{a cd}\gamma_{cd}\right)\left[\mathcal D_a\psi^i\right]_{\rm gauge}-V^{aij}\left.\mathcal D_a\psi_j\right|+\frac18\gamma^{cd}\mathcal D_a(\widehat G_{cd}+2\widehat H_{cd})\psi^{ai}-\frac g2(\mathcal D_aL_c^{ij})\psi^a{}_j\\
&-\frac i{64}\gamma^{cd}(\widehat G_{cd}+2\widehat H_{cd})\gamma^{ef}(\widehat G_{ef}-2\widehat H_{ef})\gamma_a\psi^{ai}+\frac{ig}{16}L_c^{ij}\gamma^{cd}(\widehat G_{cd}-2\widehat H_{cd})\gamma_a\psi^a{}_j+i\left(-\frac16\mathcal R_a{}^b+\frac1{48}\delta_a{}^b\mathcal R\right)\gamma_b\psi^{ai}\\
&+\frac i{12}\left(\gamma^{cd}\gamma_a-\frac12\gamma_a\gamma^{cd}\right)\widehat R(V)_{cd}^{ij}\psi^a{}_j+\frac1{24}\left[\gamma^b\gamma^{cd}\mathcal D_b(\widehat G_{cd}-2\widehat H_{cd})\gamma_a-\gamma^{cd}\mathcal D_a(\widehat G_{cd}-2\widehat H_{cd})+\gamma_a\gamma^b\mathcal D^c(\widehat G_{cb}-2\widehat H_{cb})\right]\psi^{ai}\\
&+\frac i{64}\left[-\gamma_{abcde}(\widehat G^{bc}-2\widehat H^{bc})(\widehat G^{de}-2\widehat H^{de})+8\gamma^b(\widehat G_b{}^c-2\widehat H_b{}^c)(\widehat G_{ac}-2\widehat H_{ac})-2\gamma_a(\widehat G^{bc}-2\widehat H^{bc})(\widehat G_{bc}-2\widehat H_{bc})\right]\psi^{ai}\\
&+\frac i8\gamma^{cd}(\widehat G_{cd}+2\widehat H_{cd})\gamma_a\phi^{ai}-\frac{ig}{2}L_c^{ij}\gamma^a\phi_{aj}+\frac i{24}\left[8\gamma^b(\widehat G_{ab}-2\widehat H_{ab})-\gamma_a\gamma^{cd}(\widehat G_{cd}-2\widehat H_{cd})\right]\phi^{ai}+\text{high fermi terms}.
\end{aligned}\tag{SC7D-14}
```

The occurrence $`[\mathcal D_a\psi]_{\rm gauge}`$ on the first line is the explicit field expression (SC7D-02) or (SC7D-03), with its partial derivative expanded in (SC7D-13). It is not an unspecified box or another independent field. Likewise $`\phi_a`$ has (SC7-06), and the curvatures remain compact. Every $`\mathcal D`$ in the formula is full and supercovariant. The gamma products are deliberately factorized with their order fixed; their reduction to the rank-at-most-two Clifford basis agrees with the previously canonicalized derivative calculation. No changes of fermion order or integrations by parts are hidden in (SC7D-14).

##### 4.4.6 Inverse powers and higher ordered boxes

The full even product rule gives, before imposing the gauge,

```math
\mathcal D_a\mathcal D_b\sigma^{-n}=n(n+1)\sigma^{-n-2}(\mathcal D_a\sigma)(\mathcal D_b\sigma)-n\sigma^{-n-1}\mathcal D_a\mathcal D_b\sigma.
\tag{SC7D-15}
```

Thus $`\mathcal D_a\sigma^{-n}|=0`$, but the Hessian and box are nonzero in general:

```math
\left.\mathcal D_a\mathcal D_b\sigma^{-n}\right|=-n\left.\mathcal D_a\mathcal D_b\sigma\right|,\qquad \left.\Box^c\sigma^{-n}\right|=-n\left.\Box^c\sigma\right|.
\tag{SC7D-16}
```

For the higher ordered operators already present in §6, the definitions remain

```math
\begin{aligned}
\left.\mathcal D_a\Box^c\sigma\right|&:=\left.\mathcal D_a\mathcal D^b\mathcal D_b\sigma\right|,\qquad
\left.\Box^c\mathcal D_a\sigma\right|:=\left.\mathcal D^b\mathcal D_b\mathcal D_a\sigma\right|,\qquad
\left.(\Box^c)^2\sigma\right|:=\left.\mathcal D^a\mathcal D_a\mathcal D^b\mathcal D_b\sigma\right|,\\
\left.\mathcal D_a\Box^c\psi^i\right|&:=\left.\mathcal D_a\mathcal D^b\mathcal D_b\psi^i\right|,\qquad
\left.\Box^c\mathcal D_a\psi^i\right|:=\left.\mathcal D^b\mathcal D_b\mathcal D_a\psi^i\right|,\qquad
\left.(\not{\mathcal D})^2\psi^i\right|:=\left.\Box^c\psi^i\right|+\frac12\gamma^{ab}\left.[\mathcal D_a,\mathcal D_b]\psi^i\right|.
\end{aligned}\tag{SC7D-17}
```

The first two operators on each line are different. More explicitly, for either scalar or spinor $`\Phi`$, the exact difference is

```math
[\Box^c,\mathcal D_a]\Phi=\mathcal D^b[\mathcal D_b,\mathcal D_a]\Phi+[\mathcal D^b,\mathcal D_a]\mathcal D_b\Phi.
\tag{SC7D-18}
```

Both commutators are the full superconformal commutators of (SC7-01), including their action on the lower tangent index in the second term. Equations (SC7D-17)–(SC7D-18) define the higher ordered operators; they do not claim to be a connection expansion of every third or fourth derivative. Such an expansion is deferred with the implicit fermionic dependence. In particular, one must not apply an ordinary derivative to the **gauge-only equalities** (SC7D-06), (SC7D-08) or (SC7D-14) and regard it as the next full descendant. The parent, unfixed transformation law is needed for that operation.

The entries (SC7D-02)–(SC7D-04), (SC7D-06)–(SC7D-08) and (SC7D-12)–(SC7D-14) are the gauge-fixed first/second derivative dictionary. Their use is optional during a later BF or spectrum calculation; §6 retains its canonical full-supercovariant form.

<a id="ordered-curvature"></a>

## Why full primed Ricci and the K connection remain ordered

Only the bosonic parts of the full primed Ricci and K connection may be treated as symmetric. The source used here is the project's locked curvature relation R03/GC20, including its recorded $`\psi\chi`$ completion, together with the solved $`f`$ relation (SC7-06). Define $`J_{ab}=\bar\psi_a\gamma_b\chi`$. In the independent $`\chi`$ sector the weighted antisymmetrizations give

```math
\left.\widehat R'_{acbd}(M)\right|_{\chi}=2(\eta_{cb}J_{ad}-\eta_{cd}J_{ab}-\eta_{ab}J_{cd}+\eta_{ad}J_{cb}),\qquad
\left.\mathcal R_{ab}\right|_{\chi}=-6J_{ab}-2\eta_{ab}J_c{}^c,\qquad \left.\mathcal R\right|_{\chi}=-16J_c{}^c.
\tag{SC7A-03}
```

Inserting these two contractions into (SC7-06) gives

```math
\left.f_{ab}\right|_{\chi}=-\frac16(-6J_{ab}-2\eta_{ab}J_c{}^c)+\frac1{48}\eta_{ab}(-16J_c{}^c)=J_{ab},\qquad
\left.f_{[ab]}\right|_{\chi}=\bar\psi_{[a}\gamma_{b]}\chi.
\tag{SC7A-04}
```

This term survives at two fermions. It is not removed by the dilatino gauge, since the gravitino and compensator spinor inside $`\chi`$ remain. The full primed Ricci tensor and K connection therefore retain their ordered indices.

<a id="source-appendix"></a>

## Literal complete superspace commutator appendix

C24 Appendix A, PDF pp.81–83 / printed pp.80–82: (A.1)–(A.4), including all spinor–vector and vector–vector torsions and curvatures. These are byte-preserved, visually inspected source images. They retain the printed (A.1l); use the project-derived `G-C24-A1l-repair` in the working algebra. The beginning of Appendix B visible on the last page is outside this convention extraction. Native Gold symbols require the conversion tables above.

### C24 PDF page 81

C24 Appendix A, PDF page 81

### C24 PDF page 82

C24 Appendix A, PDF page 82

### C24 PDF page 83

C24 Appendix A, PDF page 83

