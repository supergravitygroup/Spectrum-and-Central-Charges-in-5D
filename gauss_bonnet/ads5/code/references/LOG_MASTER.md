# Conventions and source equations: full fermionic gauged LOG invariant

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Scope:** This reference supplies the conventions for the [LOG component construction](../../../../log/action/README.md) through two physical fermions. Its [derivations and checks](../../../../references/source_evidence/README.md) state the scope of each component calculation.

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Supercovariant derivative convention.** Use the full supercovariant $`\mathcal D_a`$ and the conformal box $`\Box^c=\mathcal D^a\mathcal D_a`$, exactly as in the [fermionic gauged Weyl-squared calculation](../../../../weyl2/action/details/construction.md), GC14–GC24. Its Q/S/K and implicit fermionic contributions stay inside the operators. Gauge evaluation follows each ordered differentiation; derivatives of the fixed dilaton/dilatino are not silently set to zero. The active LOG endpoint uses this policy. Gold superspace source formulas retain $`\nabla_A`$ until the complete bridge is applied.

**Convention identifiers:** `GAUGED-LOG-CONVENTIONS-v1` and
`GAUGED-LOG-G25-S23-PROCEDURE-v1`.

This is the reusable calculation reference for the locked procedure. It contains
equations, not only citations: transcribed working relations first, followed by
the complete cached source equations needed for the long component expressions.
The searchable source transcriptions below retain equation and page locators.
For exact index placement, consult the corresponding published source in the [bibliography](../../../../references/bibliography.md).

The lock establishes notation, provenance, source equations and permitted
conversions. It is **not** a proof of the complete composite map or invariant.
The adopted source equations and locally derived corrections are identified
separately; each supporting check states the identity it establishes.

The separate [LOG working conventions and step 1 derivation](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md)
record the checked covariant four-slot Q/S map, six nonform BF terms, bosonic
normalization and explicit chi-curvature reconciliation. The full superform derivation
now resolves the generic current/potential/BF interface for a genuine linear
multiplet, with explicit repairs of the incompatible printed formulas. This main
file preserves literal source formulas; the working ledger distinguishes those
from derived repairs and from verification of the particular LOG polynomials. The [current evidence manifest](../../../../references/source_evidence/manifest.json) and repository artifact hashes identify the retained evidence and convention documents. The source's convention-check script is not supplied as a runnable module here.

**Retained-order construction.** The [component calculation](../../../../computations/log_fermionic/README.md) provides the primary, descendants, projection, canonicalization and BF density. The [current/form comparison](../../../../references/source_evidence/log/derivations/form-interface.md) and [bosonic comparison](../../../../references/source_evidence/log/derivations/bosonic.md) state their respective identities and residuals.

## Problem and target

Construct the off-shell five-dimensional invariant by the fixed sequence

```math
H_{\log W}^{ij}\ [\mathrm{S23}\ (3.24)\text{--}(3.26)]
\longrightarrow S_{\log}^{\mathrm{Standard\ Weyl}}\ [\mathrm{S23}\ (3.27)]
\longrightarrow\text{gauged DW maps}\ [\mathrm{G25}\ (1),(4)]
\longrightarrow\text{gauges}\ [\mathrm{G25}\ (7),(25)],\text{ split }(27).
\tag{LOG-P01}
```

Keep the gravitino and independent linear-compensator spinor. No fermion-degree
truncation, auxiliary elimination, dualization, background equation or EFT
expansion is made in the source reference. The gauge-unfixed composite construction
uses a nonvanishing vector compensator: choose a real positive local patch
$`W>0`$ corresponding to $`\sigma>0`$, so $`\log W`$ and inverse powers are defined.
Multiplying W by a constant changes its logarithm by a constant annihilated by
the defining spinor derivatives. The target gauge is imposed only after BF insertion.

## Navigation and provenance

| Section / relation IDs | Read for |
|---|---|
| C01–C06 | Metric, orientation, SU(2), linear Majorana bar, Clifford/Fierz algebra and Weyl weights |
| G01–G04; W01–W04; R01–R07 | Geometry, full covariant derivatives, transformations, dependent connections and curvatures |
| H01–H03; D01–D02 | Ungauged baseline strengths and composite auxiliaries; use the gauged replacements below when $`g\ne0`$ |
| L01–L04; V01–V03; A01–A02 | General multiplet laws, constrained form, defining vector and the full component density |
| X01–X11 | Printed discrepancies, project repairs and quarantined formulas |
| GG01–GG05; GC01–GC24 | Full improved-vector constraints, gauged composites and explicit gauged derivatives |
| Gold-source section | S23 primary, descendants, full BF action, superspace identities and C24 convention bridge |
| LOG-G01–G07; LOG-B01–B03 | Target gauge, normalization, bosonic G25 map and complete literal bosonic LOG benchmark |
| LOG-CORR01–LOG-CORR05 | Existing gauged Bianchi/E-sector and descendant corrections; full corrected bosonic comparison |
| LOG-S1-01–LOG-S1-24 in [LOG_CONVENTIONS.md](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md) | Derived step 1 bridge, density comparison, curvature reconciliation and current/potential diagnostics |
| Source-equation appendix | Full C24 descendant and higher-derivative expressions, source laws and precise visual index placements |

Source identifiers and PDF numbering:

| Key | Source | Page convention |
|---|---|---|
| S23 | Gold et al., *On curvature-squared invariants of minimal five-dimensional supergravity from superspace*, arXiv:2302.14295v2 | PDF page = printed page + 1 |
| C24 | Gold et al., *Components of curvature-squared invariants of minimal supergravity in five dimensions*, local arXiv:2311.00679v1; published JHEP07(2024)221 | Main PDF = printed +1; appended supplement PDF = supplement printed +99 |
| G25 | Gold et al., *On five-dimensional curvature squared supergravity and holography*, arXiv:2504.10856v1 | PDF page = printed page |
| W | Bergshoeff et al., *Weyl multiplets of N=2 conformal supergravity in five dimensions*, local hep-th/0104113v4 | PDF = printed +1; local filename prefix2013 is not the publication year |
| OP | Özkan–Pang, *Supersymmetric Completion of Gauss–Bonnet Combination in Five Dimensions*, corrected arXiv:1301.6622v4 | PDF = printed |
| CO | Coomans–Özkan, internally gauged D=5 supergravity, arXiv:1210.4704v3 | PDF = printed |
| OPall | Özkan–Pang, *All Off-Shell R² Invariants in Five Dimensional N=2 Supergravity*, arXiv:1306.1540v3 | Only density (3.1)–(3.2), PDF8, used here |

The numbered sources and their versions are listed in the [bibliography](../../../../references/bibliography.md).
The [current evidence manifest](../../../../references/source_evidence/manifest.json) identifies the retained repository evidence; source-page numbers below refer to the cited publications.
For component calculation, Gold's five-dimensional N=1 and the project's N=2
refer here to the same eight-real-supercharge theory; no doubling of fields is implied.

### Reading rules

1. Use Gold source notation inside S23/C24 formulas. Use project/Bergshoeff
   notation inside C/G/W/R/H/D/L/V/A/GG/GC formulas. Apply the complete bridge
   before mixing expressions, including field-dependent S/K parameter shifts.
2. $`\psi_\mu^i`$ is the gravitino, $`\psi^i`$ the defining-vector dilatino,
   $`\phi_\mu^i`$ the S connection, and $`\varphi_c^i`$ the independent compensator
   spinor. A LOG descendant carries a LOG label; it is not $`\varphi_c^i`$.
3. Gold $`W`$ is the scalar vector superfield; $`W_{ab}`$ is the super-Weyl tensor
   and its projection is $`w_{ab}`$. Gold $`X^{ij}`$ is the vector auxiliary, while
   $`X_\alpha^i,Y`$ without that triplet role are Weyl-superfield descendants.
   Gold $`F_{\log}`$ is a scalar descendant, not $`F_{ab}`$ or $`G_{ab}`$.
4. An unhatted field strength, a hatted one, a three-form potential and its
   constrained dual vector are distinct objects. Composite derivatives retain
   the Q/S/K connection terms even on a constant-compensator gauge slice.
5. The full gauged GG/GC formulas supersede the ungauged realization W02,
   W04's dilatino line, H01/H03, D01 and V03 when used at nonzero physical g.
   The universal Standard-Weyl and abstract vector/linear laws keep their form.
6. The density uses the constrained-vector expression A02.
7. Every later calculation states its fermion order, off-shell status, boundary
   representative and relation IDs. A source-page cache is an exact reference,
   not a machine-parsed algebra expression or a completed substitution.

## Convention ledger: project component frame

The following common geometric/component relations are frozen from the already
source-audited project Weyl reference, with scope restricted to common structures.
The Weyl-squared composite map, its action and its adopted spinor coefficient are
not imported as LOG inputs. Every project repair below retains its status.
No ungauged-only scope statement is imposed on this gauged branch.

<!-- LOG_BRANCH_CONVENTIONS: scope=gauged_full_fermionic_log; metric_signature=(-,+,+,+,+); natural_units=hbar=c=1; source_lock=GAUGED-LOG-CONVENTIONS-v1; procedure_lock=GAUGED-LOG-G25-S23-PROCEDURE-v1 -->

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
The source constraint consequences include $`\widehat R(D)=0`$ and the full Lorentz-curvature Bianchi identity. They do **not** justify symmetrizing the locked full primed Ricci $`\mathcal R_{\mu\nu}`$ in R03 or its dependent $`f_{ab}`$ at fermionic order. The earlier local statement doing so was corrected by the ordered-connection audit; only the bosonic specialization used there is symmetric. Keep the primed Ricci and $`f`$ indices ordered.
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

These are project interpretations, not published errata. Original source formulas remain in the appendix. X11 fixes the index ordering of the S variation.

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

### X08 — Weyl-map scope

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
checked independently in [verify_conventions.py](../../../../computations/weyl_fermionic/src/reference_checks/verify_conventions.py).

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

## Gauged realization of the shared component covariants

Use these instead of the ungauged realization when g is nonzero. The project-derived full restoration is shown in GC01–GC24 below; its insertion into the Gold LOG multiplet uses the explicit source-frame bridge below.

### GG01 — Full improved-vector constraints

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

## Full gauged composite derivation and derivative closure

Frozen from the project gauged Weyl note; only shared realization formulas GC01–GC24 and GA01–GA03 are reused. No Weyl-specific multiplet component or completed-action claim is imported. `master` references below mean the shared equations already displayed in this file.

### 3.1. Primary source inputs and their exact scope

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

### 3.2. The density, bridge and gauged defining vector

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

## 4. Detailed Derivation

### 4.1. Solve the lowest gauged constraint and vary it

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

### 4.2. Solve the spinor constraint, including its cubic term

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

### 4.3. Solve the scalar constraint and expand every Y product

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

### 4.4. Solve the tensor relation and check the form gauge symmetry

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

### 4.5. Propagate the gauging through derivatives and connections

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

## Gold source equations and the Bergshoeff component-convention bridge

This reference gives the source equations and the published convention bridge.

<!-- ASSERT_CONVENTION: source_priority=local Sources PDFs before external literature, source_frame=Gold traceless Standard-Weyl superspace, conversion_target=Bergshoeff component frame only through explicit C24 Appendix C tables -->

This note preserves Gold source notation. A superscript `G` or `B` is added only in the bridge to distinguish the Gold and Bergshoeff frames. These superscripts are labels, not indices. At extraction start the inherited project `convention_lock` contained generic placeholders; the scoped existing project component locks are the comparison target, and this extraction does not replace them. Fourier transforms, state normalization, and quantum regularization do not enter this classical source extraction.

## Sources and scope

| ID | Local source | Version and page convention |
|---|---|---|
| S23 | Gold et al., superspace paper | arXiv:2302.14295v2. `PDF n` means the one-based page in this local file; printed page is usually `n-1`. |
| C24 | Gold et al., component paper and supplement | Local combined PDF contains arXiv:2311.00679v1, subsequently published in JHEP 07 (2024) 221. Main printed page is `PDF-1`; supplement printed page is `PDF-99`. |

S23 calls the theory five-dimensional `N=1`; the project uses the older five-dimensional `N=2` nomenclature for the same eight-real-supercharge setting. This is a naming convention, not an extra supersymmetry doubling. The sources use the traceless Standard-Weyl superspace frame. The gauged Dilaton-Weyl substitution is a later operation, not part of S23 (3.24)–(3.27).

**Symbol collisions that must remain explicit.** `W` is the real vector-multiplet scalar superfield; `W_{ab}` or `W_{alpha beta}` is the super-Weyl tensor. `X^{ij}` is the vector triplet, whereas `X_alpha^i`, `X_{alpha beta}^{ij}`, and `Y` are super-Weyl descendants. The source scalar `Y` is not the Bergshoeff vector triplet `Y^{ij}`. `F` is the linear-multiplet scalar, while `F_{ab}` is a vector-multiplet field strength. `G^{ij}` is a generic linear primary and `H_log^{ij}` the composite LOG primary. The constrained linear-multiplet vector is written `mathcal H^a` below, as in the source; it is not the project Dilaton-Weyl three-form `widehat H_{abc}`. The source three-form potential `b_{mnp}` is also different from the dilatation connection `b_m`.

## S23 definitions needed before the LOG primary

All equations in this section are source equations without a Bergshoeff-frame substitution. Tangent indices are `a,b=0,...,4`; spinor indices `alpha,beta=1,...,4`; `i,j=1,2` are `SU(2)` indices. Round/square brackets have unit weight. Spinor ordering and index placement are part of the formula and must not be changed without the source spinor rules.

### Supergeometry and Weyl descendants [S23 (2.1)–(2.5), PDF7–8 / printed6–7]

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

### Generator and spinor-derivative algebra [C24 Appendix A, PDF81–82 / printed80–81]

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

### Complete Weyl spinor-derivative tower [S23 (2.6a–f), PDF9 / printed8]

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

### Vector multiplet and differential operators [S23 (2.11)–(2.17), PDF10–11 / printed9–10]

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

## Generic linear multiplet [S23 (2.20)–(2.24), PDF11–12 / printed10–11]

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

## Complete LOG primary [S23 (3.24)–(3.25)]

The defining relation [S23 (3.24), PDF20 / printed19] is

```math
H_{\log W}^{ij}=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W
=\frac{3i}{1280}\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
\tag{S23-3.24}
```

Work on a patch on which `W` is nonzero and a logarithm can be chosen. The six derivatives remove the irrelevant constant shift of the logarithm. The source's footnote5 explicitly records an overall minus sign relative to the older superspace reference [20]; do not import the latter's LOG action sign without conversion.

For readability only, define `P_n^{ij}` as the coefficient of `W^{-n}`. This grouping is project notation; the right-hand sides below reproduce all terms of S23 (3.25), PDF21–22 / printed20–21, without dropping fermions or integrating by parts:

```math
H_{\log W}^{ij}=\sum_{n=0}^{6}W^{-n}P_n^{ij}.
```

```math
P_0^{ij}=-\frac{3i}{8}W_{ab}X^{abij}+\frac{51i}{64}X^{\alpha i}X_\alpha^j.
\tag{S23-3.25-P0}
```

```math
\begin{aligned}
P_1^{ij}={}&\frac9{64}X^{ij}Y-\frac{3i}{8}F_{ab}X^{abij}-\frac12\Box X^{ij}
-\frac9{64}X^{ij}W^{ab}W_{ab}+\frac14W^{ab}W_{ab}{}^{\alpha(i}\lambda_\alpha^{j)}\\
&-\frac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}
+\frac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}.
\end{aligned}\tag{S23-3.25-P1}
```

```math
\begin{aligned}
P_2^{ij}={}&\frac12X^{ij}\Box W+\frac12(\nabla^aW)\nabla_aX^{ij}
+\frac14F^{ab}W_{ab}{}^{\alpha(i}\lambda_\alpha^{j)}
-\frac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}
-\frac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j\\
&-\frac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}
-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}\\
&+\frac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j
+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}
+\frac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&+\frac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j
-\frac38X^{ij}X^{\alpha k}\lambda_{\alpha k}.
\end{aligned}\tag{S23-3.25-P2}
```

```math
\begin{aligned}
P_3^{ij}={}&\frac18X^{ij}F^{ab}F_{ab}-\frac18X^{ij}X^{kl}X_{kl}
-\frac14X^{ij}(\nabla^aW)\nabla_aW\\
&-\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}
-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}
+\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}
+\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}\\
&-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}
+\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W
+\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}\\
&-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}
-\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW
+\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&+\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j
-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&-\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}
-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}.
\end{aligned}\tag{S23-3.25-P3}
```

```math
\begin{aligned}
P_4^{ij}={}&-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j(\nabla^aW)\nabla_aW
-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW\\
&+\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW
+\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j
+\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j\\
&-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}
-\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}
-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j\\
&-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}
-\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}\\
&-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}
-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}\\
&+\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}
+\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}.
\end{aligned}\tag{S23-3.25-P4}
```

```math
\begin{aligned}
P_5^{ij}={}&\frac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW
+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}
+\frac38X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l},\\
P_6^{ij}={}&\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}
+\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}.
\end{aligned}\tag{S23-3.25-P5-P6}
```

This is the full primary (including quartic and sextic fermions); it is not the fully expanded action. A useful transcription fingerprint is the term count by power: `(2,7,12,18,14,3,2)`, totaling 58 summands before any identities or integrations by parts. Gold 2025's shorter primary does not replace it for full fermionic work.

## LOG descendants and the full BF density

Source [S23 (3.26a–c), PDF22 / printed21]:

```math
\varphi_{\log W}^{\alpha i}=\frac13\nabla_j^\alpha H_{\log W}^{ij},
\qquad F_{\log W}=\frac i{12}\nabla_i^\alpha\nabla_{\alpha j}H_{\log W}^{ij},
\qquad\mathcal H_{\log W}^a=\frac i{12}(\Gamma^a)^{\alpha\beta}
\nabla_{\alpha i}\nabla_{\beta j}H_{\log W}^{ij}.
\tag{S23-3.26}
```

The general BF action [S23 (3.2a–b), PDF14 / printed13] is

```math
\begin{aligned}
S_{\rm BF}&=\int d^{5|8}z\,E\,\Omega W
=\int d^{5|8}z\,E\,G^{ij}V_{ij}\\
&=-\int d^5x\,e\Big[
v_a\mathcal H^a+WF+X_{ij}G^{ij}+2\lambda^{\alpha k}\varphi_{\alpha k}
-\psi_{ai}{}^\alpha(\Gamma^a)_\alpha{}^\beta\varphi_\beta{}^iW\\
&\hspace{37mm}-i\psi_{ai}{}^\alpha(\Gamma^a)_\alpha{}^\beta\lambda_{\beta j}G^{ij}
+i\psi_{ai}{}^\alpha(\Sigma^{ab})_\alpha{}^\beta\psi_{b\beta j}WG^{ij}\Big].
\end{aligned}\tag{S23-3.2}
```

Here `E=Ber(E_M{}^A)` is the superspace measure and `e` the component vielbein determinant. `U|:=U(x,theta)|_{theta=0}`. `v_m=V_m|` and `f_{mn}=2 partial_[m v_n]`. The component supercovariant strengths are [S23 (3.3)–(3.4), same page; C24 (2.37),(2.50), PDF18,22]

```math
\begin{aligned}
F_{ab}&=f_{ab}+i(\Gamma_{[a})_\alpha{}^\beta\psi_{b]k}{}^\alpha\lambda_\beta{}^k
+\tfrac i2W\psi_{[ak}{}^\gamma\psi_{b]\gamma}{}^k,
\qquad f_{ab}=e_a{}^me_b{}^nf_{mn},\\
\mathcal H^a&=h^a+2(\Sigma^{ab})_\alpha{}^\beta\psi_{bi}{}^\alpha\varphi_\beta{}^i
-\tfrac i2\varepsilon^{abcde}(\Sigma_{bc})_{\alpha\beta}\psi_{di}{}^\alpha\psi_{ej}{}^\beta G^{ij}.
\end{aligned}
```

The LOG action is the same density evaluated on the composite multiplet [S23 (3.27a–b), PDF22 / printed21; C24 (5.9a–b), PDF41 / printed40]:

```math
\begin{aligned}
S_{\log W}&=\int d^{5|8}z\,E\,V_{ij}H_{\log W}^{ij}\\
&=-\int d^5x\,e\Big[v_a\mathcal H_{\log W}^a+WF_{\log W}
+X_{ij}H_{\log W}^{ij}+2\lambda^k\varphi_{k\log W}\\
&\hspace{24mm}-\psi_{ai}\Gamma^a\varphi_{\log W}^iW
-i\psi_{ai}\Gamma^a\lambda_jH_{\log W}^{ij}
+i\psi_{ai}\Sigma^{ab}\psi_{bj}WH_{\log W}^{ij}\Big].
\end{aligned}\tag{S23-3.27;C24-5.9}
```

The implicit spinor contractions in the last display are fixed by the explicit general density above. The bracket has **seven summands**: `v H`, `W F`, `X G`, `2 lambda varphi`, and the three explicit gravitino terms. Neither the overall minus nor any explicit gravitino coupling may be discarded.

S23's text immediately after (3.27) defers the expanded descendants. Their full component support is C24 supplement §2.2.1 (`varphi`, PDF106–112 / printed7–13), §2.2.2 (`F`, PDF113–121 / printed14–22), §2.2.3 (`mathcal H^a`, PDF121–149 / printed22–50). The scalar and vector page ranges overlap on PDF121 at their subsection boundary. These are distinct from the bosonic-only supplement §3.1. The master source cache, rather than this compact equation list, carries the lengthy expanded descendants.

## Supplement notation and projections [C24 supplement §1, PDF103 / printed4]

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

## Published Gold-to-Bergshoeff bridge [C24 Appendix C, Tables4–6]

The following uses the **Bergshoeff et al. column**. C24 also provides other convention systems; mixing a de Wit entry into this column is not permitted. Source: Tables4–5, PDF91 / printed90; Table6, PDF92 / printed91. The paragraph immediately before Table4 (PDF90 / printed89) explicitly explains the field-dependent S/K shifts and cancellation in the fully covariant vector derivative.

### Algebra and Weyl multiplet

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

### Supersymmetry parameters [C24 Table5]

A Gold `delta_Q(xi_G)+delta_S(eta_G)+delta_K(Lambda_G)` becomes a Bergshoeff transformation with

```math
\epsilon_B^i=2\xi_G^i,\qquad
\eta_B^{\prime i}=-2i\eta_G^i+\tfrac23T_{ab}^B\gamma_B^{ab}\xi_G^i,\qquad
\Lambda_K^{\prime Ba}=-\Lambda_K^{Ga}+\tfrac23\xi_G^i\gamma_B^a\chi_i^B.
\tag{C24-Table5}
```

Therefore the conversion of a Q rule includes induced S and K rules. Converting only the gamma matrices, the fields, or `epsilon=2xi` does not convert a complete transformation. The source states that these shifts cancel the corresponding gravitino terms in the S/K connections, leaving the same fully covariant vector derivative after generator-normalization conversion. This statement concerns the **whole derivative**, not a termwise equality of the named connections.

### Vector multiplet [C24 Table6]

```math
W_G=\sigma_B,\qquad\lambda_G^i=-\psi_B^i,\qquad X_G^{ij}=2Y_B^{ij}.
\tag{C24-Table6}
```

For a generic vector scalar called `rho` in the project, relabel `sigma_B` to `rho` only after identifying which vector is under discussion. The defining vector later has `rho=sigma` and `A=C`. Table6 itself does not list the vector potential or a full linear-multiplet normalization map.

## Conversion and homogeneity checks

These are direct algebraic checks, not a nonlinear action/SUSY validation.

1. **Clifford sign.** With the project Bergshoeff `\{\gamma_B^a,\gamma_B^b\}=2\eta^{ab}`, Table4 gives `\{\Gamma_G^a,\Gamma_G^b\}=-2\eta^{ab}`. For signature `(-++++)`, `(gamma_B^0)^2=-1` and `(Gamma_G^0)^2=+1`, while `(gamma_B^1)^2=+1` and `(Gamma_G^1)^2=-1`. Thus the shared metric does not mean the two Clifford anticommutators have the same sign. Also `Sigma_G^{ab}=-[Gamma_G^a,Gamma_G^b]/4=gamma_B^{ab}/2`, using `gamma^{ab}=gamma^{[a}gamma^{b]}`.
2. **Projection inverses.** Substituting `X|=-(32i/3)chi` into `chi=(3i/32)X|` gives `chi`, and substituting `Y|=-(128/3)D` into `D=-3Y|/128` gives `D`. Combining with Table4 gives `W_ab|=16 T_ab/3` and leaves `chi,D` unchanged between G and B.
3. **Primary weights.** `w(W)=w(W_ab)=1`, `w(lambda)=w(X_alpha)=w(W_abc-spinor)=3/2`, `w(X^{ij})=w(F_ab)=w(Y)=w(X_ab^{ij})=2`, `w(nabla_a)=1`, `w(nabla_alpha)=1/2`. Each displayed `P_n` has weight `3+n`, so `W^{-n}P_n` has weight3. For example `W^{-6}lambda^6` has `-6+6(3/2)=3`; `W^{-1}Box X^{ij}` has `-1+2+2=3`; `W_ab X^{abij}` has `1+2=3`. Six spinor derivatives in (3.24) have weight3; the inhomogeneous constant dilatation shift of `log W` is killed.
4. **BF weights.** The linear slots have `(w(G),w(varphi),w(F),w(mathcal H))=(3,7/2,4,4)`, and the tangent fields have `w(v_a)=1`, `w(psi_a)=1/2`. All seven BF terms have weight5: e.g. `W F=1+4`, `lambda varphi=3/2+7/2`, `psi psi W G=1/2+1/2+1+3`.
5. **BF normalization boundary.** `X_G G=2Y_B G` follows from Table6, but this alone does not determine `G` relative to the project's normalized `L^{ij}` or the overall Gold-to-project density conversion. A complete matching gate must compare scalar, triplet, form, spinor, and gravitino slots together, using their Q/S transformations and Table5. No equality between full component actions is inferred from a single bosonic slot.
6. **Orientation test.** Table4 maps every displayed upper five-index epsilon with a factor `-1`; two epsilon factors map with `+1`. It is not consistent to change epsilon in the CS term while leaving it unconverted in the corresponding Hodge dual.

<a id="deliberate-boundaries-and-pending-matching-checks"></a>

## Scope of the convention and matching checks

- The full S23 primary is transcribed above. The compact descendant definitions are exact. The long descendants and higher component derivatives are available in the local source cache; they need algebraic expansion and checking during calculations, not rediscovery of their source locations.
- S23 (3.27) and C24 (5.9b) are Standard-Weyl BF constructions. Their published local supersymmetry does not by itself prove a new, explicitly expanded, project-corrected gauged action.
- C24 Tables4–6 establish the published Gold/Bergshoeff bridge. They do not contain a full Gold linear-multiplet-to-project `L,varphi,E,N` normalization table. The branch derives that covariant normalization in LOG_CONVENTIONS.md. The full superform interface completes the generic current/potential/BF comparison, preserving explicit derived repairs of the incompatible printed formulas. Checking the actual expanded LOG multiplet remains distinct from this generic conversion.
- Project-specific corrected fermionic curvature signs cannot be promoted to the printed C24 bridge. Compare them explicitly when substituting dependent connections.
- Gauging introduces its own deformed composite map; the Table4 Standard-Weyl bridge is not that gauged map. Gold2025's `f.t.` placeholders and lower-order primary are not full fermionic replacements.

## Extraction verification record

S23 PDF9–12, PDF14 and PDF21–22, and C24 PDF81–82, PDF91, PDF103 were rendered and visually inspected for coefficients, positions, symmetrizations, and projection factors. The complete primary was checked line by line against the source images, including its continuation onto PDF22. The source field frame is retained. Every formula block has a local source/equation/page cue; `P_n` grouping and the checks are explicitly identified as project organization or algebraic consequences.

Executed checks: **PASS** for the Weyl weight of all 58 primary summands, **PASS** for all 25 Clifford anticommutators in each frame, **PASS** for all 25 bivector conversions, **PASS** for both projection inverses. This verifies transcription-level homogeneity and convention conversions; it does not verify cancellations in the complete supersymmetry variation.

The following dependency-free Python is a reusable version of the executed checks. The monomial strings are ordered exactly as the displayed `P_n` terms. `w` is the scalar, `W` the Weyl two-form, `l` the gaugino, `x` the Weyl spinor, `u` the Weyl three-spinor descendant, `X` the vector triplet, `Z` the Weyl two-form triplet. The `d`/`box` prefixes count one/two vector derivatives.

```python
from fractions import Fraction as Q

weights = dict(w=1, W=1, l=Q(3,2), x=Q(3,2), u=Q(3,2),
               X=2, F=2, Y=2, Z=2, dw=2, dW=2, dl=Q(5,2),
               dx=Q(5,2), dX=3, dF=3, boxw=3, boxX=4, boxl=Q(7,2))
terms = {
    0: ['W Z', 'x x'],
    1: ['X Y', 'F Z', 'boxX', 'X W W', 'W u l', 'x dl', 'l dx'],
    2: ['X boxw', 'dw dX', 'F u l', 'l boxl', 'dl dl', 'W l dl',
        'l l dW', 'Y l l', 'F x l', 'W W l l', 'W W l l', 'X x l'],
    3: ['X F F', 'X X X', 'X dw dw', 'F l dl', 'F l dl', 'l l dF',
        'X l dl', 'X l dl', 'l dX l', 'l l boxw', 'dw l dl', 'dw l dl',
        'W l l dw', 'W F l l', 'W F l l', 'X W l l', 'x l l l', 'x l l l'],
    4: ['l l dw dw', 'X l l dw', 'F l l dw', 'F F l l', 'F F l l',
        'X F l l', 'X X l l', 'X X l l', 'l l l dl', 'l l l dl',
        'l l l dl', 'l l l dl', 'W l l l l', 'W l l l l'],
    5: ['l l l l dw', 'F l l l l', 'X l l l l'],
    6: ['l l l l l l', 'l l l l l l'],
}
assert tuple(map(len, terms.values())) == (2,7,12,18,14,3,2)
for n, group in terms.items():
    for k, term in enumerate(group, 1):
        assert sum(weights[f] for f in term.split()) - n == 3, (n,k,term)

I = ((1,0),(0,1))
s1, s2, s3 = ((0,1),(1,0)), ((0,-1j),(1j,0)), ((1,0),(0,-1))
def kron(A, B):
    return tuple(tuple(A[i//2][j//2]*B[i%2][j%2] for j in range(4)) for i in range(4))
def scale(c, A):
    return tuple(tuple(c*x for x in row) for row in A)
def add(A, B):
    return tuple(tuple(x+y for x,y in zip(ra,rb)) for ra,rb in zip(A,B))
def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))
I4 = kron(I,I)
gamma = [scale(1j,kron(s3,s3)), kron(s1,I), kron(s2,I), kron(s3,s1), kron(s3,s2)]
Gamma = [scale(1j,g) for g in gamma]
for a in range(5):
    for b in range(5):
        eta = (-1 if a == 0 else 1) if a == b else 0
        assert add(mm(gamma[a],gamma[b]),mm(gamma[b],gamma[a])) == scale(2*eta,I4)
        assert add(mm(Gamma[a],Gamma[b]),mm(Gamma[b],Gamma[a])) == scale(-2*eta,I4)
        commG = add(mm(Gamma[a],Gamma[b]),scale(-1,mm(Gamma[b],Gamma[a])))
        commB = add(mm(gamma[a],gamma[b]),scale(-1,mm(gamma[b],gamma[a])))
        assert scale(-Q(1,4),commG) == scale(Q(1,4),commB)
assert Q(3,32)*1j*(-Q(32,3)*1j) == 1
assert -Q(3,128)*(-Q(128,3)) == 1
print('PASS: 58 primary weights; 2x25 Clifford checks; 25 bivectors; 2 inverses')
```

## Target gauge, normalization and Gold 2025 benchmark

### LOG-G01 — Target gauge and independent fields

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

### LOG-G02 — Gauge preservation: defining equations and kinematic solutions

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

### LOG-G03 — Couplings, weights and the action convention

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

### LOG-G04 — Bosonic form conventions and shorthand

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

### LOG-G05 — Bosonic covariant derivative and R curvature

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

### LOG-B01 — Literal bosonic G25 map (1)

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

### LOG-B02 — Defining vector, G25 (4)

G25 PDF5–6 supplies the fourth slot including its explicit fermions:

```math
(\rho,A_\mu,\lambda^i,Y^{ij})=
\left(\sigma,C_\mu,\psi^i,
\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\right).
\tag{LOG-B02}
```

This map is used only after forming the Standard-Weyl BF invariant. It is not
S23's LOG composite, and the independent compensator $`L_c`$ is not $`L_{\log}`$.

### LOG-B03 — Literal printed G25 (11), with known project corrections

Source: G25 PDF9, visually checked. Here the source symbols $`L^{ij},N`$ mean
the independent compensator $`L_c^{ij},N_c`$, and $`H_{ab}`$ has LOG-G04's meaning.
No project coefficient repair or integration by parts is applied in this block.
This is the printed source record, not the corrected bosonic acceptance target.
See LOG-CORR01–LOG-CORR05 for the existing project corrections and full corrected density.

```math
\begin{aligned}
\ell_{\rm LOG}^{\rm G25,bos}={}&
-\frac16R_{ab}R^{ab}+\frac1{24}R^2
+\frac16R^{ab}G^2_{ab}+\frac13RH_{ab}G^{ab}
-\frac43R_{ab}H^{ac}G^b{}_c-\frac13RH^2\\
&-\frac1{12}\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij}
+\frac16V^{abij}V_{ab\,ij}-2(H^2)^2
+\frac{16}{3}H^2_{ab}H^{ac}G^b{}_c-\frac43H^2H_{ab}G^{ab}\\
&+\frac23H_{ab}H_{cd}(G^{ab}G^{cd}-2G^{ac}G^{bd})
+\frac23H^2G^2-\frac43H^{2ab}G^2_{ab}
-\frac13H_{ab}G^{ab}G^2+G^2_{ab}H^{ac}G^b{}_c\\
&-\frac1{48}(G^2)^2-\frac1{24}G^4
-\frac16\nabla_cG^{ac}\nabla^bG_{ab}
+2\nabla_aH_{bc}\nabla^{[a}H^{bc]}\\
&+\frac1{48}\epsilon^{abcde}\nabla^fG_{ef}(4H_{ab}-G_{ab})(4H_{cd}-G_{cd})\\
&+\frac g6\left(RN-4NH_{ab}G^{ab}-2NG^2
+V_{ab}^{ij}L_{ij}(G^{ab}+4H^{ab})+12NH^2-6\nabla^a\nabla_aN\right)\\
&-\frac{g^2}{24}\left(2RL^2-L^2(G^2-4G^{ab}H_{ab}-24H^2)
+4N^2+6\nabla^aL^{ij}\nabla_aL_{ij}\right)
+\frac23NL^2g^3+\frac5{24}L^4g^4.
\end{aligned}\tag{LOG-B03}
```

The term $`-g\nabla^2N`$ is retained as printed. Any removal from the integrated
action requires an explicit boundary current and conditions. All monomials
have engineering dimension4 with LOG-G03. The existing definition-derived
bosonic corrections are recorded in LOG-CORR01–LOG-CORR05. Reproducing the
uncorrected printed block is not an acceptance test for the full invariant.

### LOG-G06 — Optional independent checks among invariants

G25 (13), PDF10, and (22)–(23), PDF13:

```math
\mathcal L_{\rm Riem^2}=\mathcal L_{\rm Weyl^2}+2\mathcal L_{\rm LOG},
\qquad
\mathcal L_{\rm GB}=\mathcal L_{\rm Weyl^2}-4\mathcal L_{\rm LOG},
\qquad H_{\rm GB}^{ij}=H_{\rm Weyl^2}^{ij}-4H_{\rm LOG}^{ij}.
\tag{LOG-G06}
```

Use only after the unreduced representatives and normalizations agree. These
identities do not replace the locked direct LOG construction or justify combining
background-reduced equations from other branches.

### LOG-G07 — Equality and boundary conventions

Write exact local equalities with $`=`$. For integration by parts, write the
current explicitly:
$`e\ell_1-e\ell_2=\partial_\mu(eJ^\mu)`$.
Write $`\ell|_{\rm gauge}`$, $`\ell|_{\rm bos}`$ or
$`\ell+O(\text{fermion}^{n})`$ whenever that restriction is used. No field
equation of the final higher-derivative theory is permitted merely because a
field was auxiliary in the two-derivative theory. Grassmann variations use
left functional derivatives if Euler equations are later formed, with the odd
variation moved to the left before reading its coefficient.

## Existing project result: corrected bosonic LOG invariant

**Bosonic comparison:** previously derived result used in this
construction. These are project-derived corrections, not a published erratum
and not a completed fermionic invariant. Gold's printed Eq. (11), retained as
LOG-B03, must not be used as an unquestioned target to which coefficients are fitted.

The detailed local derivation is
[weyl_log_from_definitions.tex](../inputs/action_sources/10_weyl_log_from_definitions.tex):
`eq:Bianchi-expanded`, `eq:L-Yraw`, `eq:L-YD`, L1–L13,
`eq:L-final-expanded` (Eq. (52) in the accompanying report), and the boundary
currents `eq:Log-mixed-current`, `eq:twoform-boundary-id`, `eq:Log-D-boundary`.
Its checks are in verify_weyl_log_definition_map.py.
The earlier missing-terms literature audit
records the quadratic omission; the definition-derived report gives the full
bosonic E sector. Its negative literature conclusion is dated 2026-08-20,
not a new search or a claim that an author erratum exists.

### LOG-CORR01 — The gauged Bianchi contribution that must be retained

Here $`E^a,L^{ij},N`$ denote the independent compensator slots, as in LOG-B03;
$`E_{abc}`$ is its three-form potential. With LOG-G04's Gold Hodge convention,
the existing derivation gives

```math
E^a=-\frac1{12}\epsilon^{abcde}\nabla_bE_{cde},\qquad
\nabla_bH^{ab}=-\frac1{16}\epsilon^{abcde}G_{bc}G_{de}
+\frac g2E^a.
\tag{LOG-CORR01}
```

Source within the project: `eq:Bianchi-expanded`, derived from the full
$`H_3=dB+\tfrac12C\wedge G+\tfrac g2E_3`$ definition. Using the ungauged
divergence identity during derivative reduction loses the $`gE^a/2`$ contribution.

### LOG-CORR02 — Explicit E terms in the corrected representative

In the boundary representative of `eq:L-final-expanded`, the complete explicit
E block is

```math
\begin{aligned}
\ell_{\rm LOG}^{\rm def}\big|_{\text{explicit }E}
={}&\frac{g^2}{3}E_aE^a+\frac g3E_a\nabla_bG^{ab}\\
&-\frac g{24}\epsilon^{abcde}E_aG_{bc}G_{de}
-\frac{2g}{3}\epsilon^{abcde}E_aH_{bc}H_{de}.
\end{aligned}
\tag{LOG-CORR02}
```

The first two terms give the earlier quadratic correction about a background
with vanishing $`E,G,H`$; the epsilon terms are cubic in these fluctuations.
These terms are already present in the corrected density below. Do not add
them twice. This block alone is not a declaration that the entire difference
between two arbitrary boundary representatives consists of four monomials:
derivative ordering, quartic identities and boundary currents must also match.

### LOG-CORR03 — Scalar-descendant projection used once

The raw C24 descendant, and its component projection, enter the existing
derivation as

```math
F_{\rm LOG}\big|_{Y,w}
=\frac3{2048}Y^2+\frac{69}{1024}w^{ab}w_{ab}Y+\cdots,
\qquad D=-\frac3{128}Y\big|.
\tag{LOG-CORR03a}
```

Consequently, with $`w^2=w^{ab}w_{ab}`$,

```math
\frac3{2048}Y^2\longmapsto\frac83D^2,\qquad
\frac{69}{1024}w^2Y\longmapsto-\frac{23}{8}w^2D.
\tag{LOG-CORR03b}
```

The BF minus sign then contributes $`+23w^2D/8`$ to the action. C24 (4.8b)
prints $`+368w^2D/3`$ in the descendant, inconsistent with the raw supplement
and its defining projection. That number equals a second multiplication by
$`-128/3`$, suggesting a repeated conversion; this does not establish how the
authors obtained it. **C24 (5.20) already has the consistent $`+23w^2D/8`$
action coefficient.** No further scalar term is to be added to that action
or to G25 (11). Anchors: supplement (1.2b), §2.2.2; main (4.8b), (5.20);
project `eq:L-Yraw`, `eq:L-YD`. This bosonic projection check does not
substitute for matching every fermionic slot.

### LOG-CORR04 — Standard-frame curvature canonicalization

Reducing the raw descendant gives

```math
\ell_{\rm LOG}^{\rm S}\supset
\frac14R^{\rm S}_{abcd}F_{\rm S}^{ab}F_{\rm S}^{cd}
+\frac38R^{\rm S}_{abcd}w_{\rm S}^{ab}w_{\rm S}^{cd}.
\tag{LOG-CORR04a}
```

The second coefficient is $`3/8`$ from the raw supplement §3.1, whereas
C24 (5.20) and the earlier intermediate ledger print $`1/4`$. The reduction
uses C24 (2.21)'s tensor commutator and retains the explicit boundary current.
It has been checked independently in 24 exact-arithmetic tensor-jet cases
across two metric signatures. This establishes a source-to-source mismatch
conditional on the raw supplement. The complete calculated bosonic certificate
now additionally reproduces the entire corrected ledger from the newly calculated
LOG scalar/vector/BF components, including this sector. Full details and original page
anchors are in the direct source audit,
with the independent checker.
Under $`w_{\rm S}^{ab}=2(G^{ab}-2H^{ab})/3`$ and
$`R^{\rm S}_{abcd}=-R_{abcd}`$, the correction to that earlier ledger is

```math
\begin{aligned}
\delta\ell_{\rm LOG}^{\text{old ledger}}
&=\frac18R^{\rm S}_{abcd}w_{\rm S}^{ab}w_{\rm S}^{cd}\\
&=-\frac1{18}R_{abcd}(G^{ab}-2H^{ab})(G^{cd}-2H^{cd}).
\end{aligned}
\tag{LOG-CORR04b}
```

Anchors: L1–L13, especially `eq:L-standard-ledger` and
`eq:L-Riemann-correction-map`. This repairs the earlier definition-derived
intermediate ledger; it is **not an extra Riemann term to append to G25 (11)**.
After the derivative commutator reduction, L10–L12 cancel the full explicit
$`R_{abcd}GG`$, $`R_{abcd}GH`$ and $`R_{abcd}HH`$ sector in the final corrected LOG
representative. The final expression below already includes this cancellation.

### LOG-CORR05 — Full corrected bosonic comparison

The following is given by the existing `eq:L-final-expanded`, with only
LaTeX macro expansion and Markdown layout changes. It uses the original Gold
fields, LOG-G04's Hodge convention and the original derivation's curvature
bridge. The notation $`\simeq_{\partial}`$ means equality up to the explicit
currents listed above; it is not a pointwise equality of densities.

```math
\begin{aligned}
\ell_{\rm LOG}^{\rm def,bos}\simeq_{\partial}{}&
-\frac1{12}\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij}
+\frac16V_{ab}^{ij}V^{ab}_{ij}
+\frac g6V_{ab}^{ij}L_{ij}G^{ab}
+\frac{2g}{3}V_{ab}^{ij}L_{ij}H^{ab}
\\
&-\frac16R_{ab}R^{ab}+\frac1{24}R^2
+\frac16R_{ab}G^{ac}G^b{}_c
-\frac43R_{ab}G^{ac}H^b{}_c
\\
&+R\left(\frac g6N-\frac{g^2}{12}L^{ij}L_{ij}
+\frac13G_{ab}H^{ab}-\frac13H_{ab}H^{ab}\right)
\\
&-\frac{g^2}{6}N^2+\frac{2g^3}{3}N L^{ij}L_{ij}
+\frac{5g^4}{24}(L^{ij}L_{ij})^2
\\
&+gN\left(-\frac13G_{ab}G^{ab}-\frac23G_{ab}H^{ab}
+2H_{ab}H^{ab}\right)
\\
&+g^2L^{ij}L_{ij}\left(\frac1{24}G_{ab}G^{ab}
-\frac16G_{ab}H^{ab}-H_{ab}H^{ab}\right)
\\
&-\frac1{48}(G_{ab}G^{ab})^2
-\frac13(G_{ab}G^{ab})(G_{cd}H^{cd})
+\frac23(G_{ab}G^{ab})(H_{cd}H^{cd})
\\
&+\frac43(G_{ab}H^{ab})^2
-\frac43(G_{ab}H^{ab})(H_{cd}H^{cd})
-2(H_{ab}H^{ab})^2
\\
&-\frac1{24}G_{ab}G^{bc}G_{cd}G^{da}
+G_{ab}G^{bc}G_{cd}H^{da}
-\frac43G_{ab}G^{bc}H_{cd}H^{da}
\\
&-\frac83G_{ab}H^{bc}G_{cd}H^{da}
+\frac{16}{3}G_{ab}H^{bc}H_{cd}H^{da}
\\
&-\frac16(\nabla_bG^{ab})(\nabla^cG_{ac})
+\frac23(\nabla_aH_{bc})
\left(\nabla^aH^{bc}+\nabla^bH^{ca}+\nabla^cH^{ab}\right)
\\
&-\frac{g^2}{4}(\nabla_aL^{ij})(\nabla^aL_{ij})
\\
&+\frac1{48}(\nabla^bG_{ab})\epsilon^{acdef}G_{cd}G_{ef}
+\frac13(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}H_{ef}
\\
&-\frac16(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}G_{ef}
\\
&+\frac1{12}(\epsilon^{abcde}G_{bc}G_{de})
(\epsilon_{a}{}^{fghi}H_{fg}H_{hi})
\\
&+\frac g3E_a\nabla_bG^{ab}
-\frac g{24}E_a\epsilon^{abcde}G_{bc}G_{de}
-\frac{2g}{3}E_a\epsilon^{abcde}H_{bc}H_{de}
+\frac{g^2}{3}E_aE^a.
\end{aligned}
\tag{LOG-CORR05}
```

This is the existing bosonic result to reproduce, or explicitly reconcile
term by term, when checking the new full-fermionic construction. Its fermionic
partners must follow from the full primary, descendants and BF density;
they cannot be inferred by adding these bosonic terms to an abbreviated action.
The complete calculated bosonic certificate now reproduces this entire density
from the actual calculated zero-fermion slots with explicit boundary currents.
The unrestricted fermionic component and nonlinear supersymmetry checks remain separate. No prior spectrum
conclusion is imported by recording this bosonic result.

## Comparison of component conventions

The [component evidence guide](../../../../references/source_evidence/README.md) and [current evidence manifest](../../../../references/source_evidence/manifest.json) identify the retained convention comparisons and source records. The source versions and equation locators are listed above.

The new reference adopts the current common 5D geometry, linear Majorana bar,
NW–SE SU(2) contractions and Clifford orientation. It keeps Gold superspace
expressions in their own explicit frame until conversion. The old handoff's
extra determinant in the world epsilon tensor was a transcription error; the
component expression uses the corrected world tensor. Older extraction files
and source-specific earlier expressions are distinguished from the current
LOG authority. The independently checked diagnostic is

```math
e_\mu{}^a=2\delta_\mu{}^a\ \Rightarrow\ e=32,\qquad
\epsilon^{01234}_{\rm world}=(2^{-1})^5=\frac1{32}
=e^{-1}[01234],\qquad e\epsilon^{01234}_{\rm world}=1.
\tag{LOG-CHECK01}
```

The project-derived +8 chi curvature repair, chi weight3/2, missing sigma in
the short H variation and tensor-derivative index/sign repair are recorded in
X01–X11 with their evidence. They are not labeled as published Gold formulas.
The separate older 2013/2016 two-derivative composite Y-slot discrepancy does
not define the LOG multiplet and is not silently resolved here.

The source convention-check record identifies the algebraic and source-integrity tests. Its scope is the stated reference identities and transcription; it is distinct from certification of the complete invariant.

The LOG calculation uses the scoped conventions and explicit frame conversions recorded here.

## Component reference equations

The published input equations
are available in this file and its local, hashed image/text assets. The short
working equations are transcribed; the very long component polynomials are
preserved literally in the source-equation appendix. Relation IDs identify the corresponding source equations. No claim is made that every long
polynomial has been independently rederived or converted to the project frame.

## Convention dependence and remaining uncertainties

- C24 Tables4–6 specify Weyl/vector fields and Q/S/K parameter shifts. They
  are supplemented by the step 1 derivation in LOG_CONVENTIONS.md. Its
  covariant four-slot Q/S map, six nonform BF terms, explicit chi-curvature
  interface and bosonic normalization probe pass. The [full superform
  derivation](SOURCE_LOCK.md) resolves FORM-01
  for a genuine linear multiplet: the ordinary-current BF coupling and full
  potential law are derived. Literal C24 (2.50) differs by $`2Q_1`$ only; the
  earlier $`2(Q_1+Q_2)`$ claim was a local second-spinor-index lowering error.
  C24/S23 (3.2b) requires the ordinary dual. These repairs remain separate
  from source transcriptions and from checking the actual LOG polynomials.
- Project-derived gauged composites restore the omissions of CO (5.3)–(5.4)
  through the complete improved-vector constraints. Their transportation into
  the Gold LOG density and all-order consistency require the stated bridge.
- OP's paired potential SUSY laws are quarantined (X10). The linear potential
  law with coefficients $`(1,-3)`$ is now derived from the complete superform
  contraction. This closes the generic linear-potential interface; it does not
  independently certify the separate gauged H-potential realization.
- LOG-G02 gives exact gauge-preservation equations and immediate kinematic
  solutions in the declared component frame. Full combined transformation laws,
  their closure and the nonlinear invariant variation are not certified here.
- G25 (11) is preserved as a literal source record. LOG-CORR01–LOG-CORR05
  carry the existing definition-derived bosonic corrections and corrected
  comparison density. The complete calculated bosonic certificate now reproduces its full
  bosonic body from the calculated multiplet with explicit boundary currents.
  This closes that bosonic comparison; unrestricted fermionic checks remain
  separate, and matching the uncorrected printed action is insufficient.
- Neither raw source text nor a hash check proves a 44-page descendant
  polynomial. The cited source equations determine its coefficients and indices;
  each algebraic validation states what was actually checked.

The [bibliography](../../../../references/bibliography.md) provides the original publications for source comparisons; the displayed equation and page locators specify the relations used here.

## Subsequent retained-order certification — 2026-09-25

The reference-task limits above describe what its own integrity checker establishes. The later [complete branch certificate](../../../../log/action/README.md) independently closes defining-projector, full curved-primary, retained projection/canonicalization/reality, generic current/BF and complete bosonic gates. Its supersymmetry conclusion uses the verified multiplet and closed BF superform. It does not certify omitted higher-fermion action terms or separately expand all gauge-preserving transformation commutators. Source transcriptions and project-derived repairs remain distinct.

## Source-equation appendix: exact saved equations and searchable text

This appendix contains searchable source transcriptions with stable page identifiers. The [bibliography](../../../../references/bibliography.md) links the published sources for checking exact upper/lower positions, underlines and bracket glyphs. Plain-text order is not a Grassmann or index-order rule. The page identifiers below locate source text, rather than bundled page images or PDF caches.

The full C24 LOG descendants span PDF106–149. The scalar/vector transition occurs on PDF121; the vector/bosonic-action transition occurs on PDF149. Nothing is truncated at those boundaries. Supplement §3.1 on PDF149 is bosonic only. Full higher-derivative expansions occupy PDF300–327.

| Input group | Cached PDF pages | Equation role |
|---|---|---|
| S23 | 7–14 | [Superconformal algebra, Weyl/vector/linear descendants and BF](LOG_MASTER.md#src-s23-p007) |
| S23 | 20–22 | [LOG primary, complete expanded superfield, descendant definitions and action](LOG_MASTER.md#src-s23-p020) |
| C24 | 8–24 | [Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF](LOG_MASTER.md#src-c24-p008) |
| C24 | 32–37 | [Main4.2: LOG primary and descendants, including full4.8a](LOG_MASTER.md#src-c24-p032) |
| C24 | 41–41 | [Main5.9: full component LOG BF density](LOG_MASTER.md#src-c24-p041) |
| C24 | 81–83 | [AppendixA: conformal superspace derivative algebra](LOG_MASTER.md#src-c24-p081) |
| C24 | 90–92 | [AppendixC: convention bridge and Tables4–6](LOG_MASTER.md#src-c24-p090) |
| C24 | 103–103 | [Supplement1: raw index conventions and X/Y component projections](LOG_MASTER.md#src-c24-p103) |
| C24 | 106–113 | [Supplement2.2.1: complete LOG spinor descendant; scalar starts on113](LOG_MASTER.md#src-c24-p106) |
| C24 | 113–121 | [Supplement2.2.2: complete LOG scalar descendant; vector starts on121](LOG_MASTER.md#src-c24-p113) |
| C24 | 121–149 | [Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149](LOG_MASTER.md#src-c24-p121) |
| C24 | 300–308 | [Supplement5.1: full degauged higher Weyl derivatives](LOG_MASTER.md#src-c24-p300) |
| C24 | 308–324 | [Supplement5.2: full degauged higher vector derivatives](LOG_MASTER.md#src-c24-p308) |
| C24 | 324–327 | [Supplement5.3: full degauged higher linear derivatives](LOG_MASTER.md#src-c24-p324) |
| G25 | 4–10 | [Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13](LOG_MASTER.md#src-g25-p004) |
| G25 | 13–14 | [Relations22–23; gauge25, reference26 and connection split27](LOG_MASTER.md#src-g25-p013) |
| W | 15–25 | [Full Weyl geometry, constraints, transformations and soft algebra](LOG_MASTER.md#src-w-p015) |
| W | 28–29 | [Improved-vector constraints5.10–5.14 and their descendants](LOG_MASTER.md#src-w-p028) |
| W | 32–34 | [AppendixA: all 5D Clifford, symplectic-Majorana, SU(2), Fierz and duality conventions](LOG_MASTER.md#src-w-p032) |
| OP | 4–11 | [Multiplets, derivatives, curvatures, forms, full composites and density](LOG_MASTER.md#src-op-p004) |
| OP | 13–14 | [Gauge4.1, retained fields4.2 and truncated compensating transformations4.3](LOG_MASTER.md#src-op-p013) |
| OP | 28–29 | [Appendices: gamma/spinor and notation conventions](LOG_MASTER.md#src-op-p028) |
| CO | 4–8 | [Weyl, vector and linear multiplet transformations and covariant structures](LOG_MASTER.md#src-co-p004) |
| CO | 16–17 | [Gauged map5.2–5.8 and explicit higher-fermion omission statement](LOG_MASTER.md#src-co-p016) |
| OPall | 8–8 | [3.1–3.2: operational E_a density and P/E completion](LOG_MASTER.md#src-opall-p008) |

### S23: cached source equations

Source PDF: 2023-Gold-On-curvature-squared-invariants-from-superspace.pdf. SHA-256: `7461b1548e04efb4836f2e0ea0f4f9e5d53566d52b112ab5c452332e36e3849a`.

<a id="src-s23-p007"></a>

<details>
<summary>S23-p007 — PDF page 7: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p007: PDF page 7](https://arxiv.org/pdf/2302.14295v2#page=7) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2      Superconformal multiplets in 5D N = 1 superspace
    In this section we review several superconformal multiplets which will serve as build-
ing blocks for the various curvature-squared invariants presented in this work. After
describing the standard Weyl multiplet of conformal supergravity in 5D N = 1 conformal
superspace, we move on to the discussion of the Abelian vector and off-shell linear mul-
tiplets. Here we make use of the approach and results given in [20]. We refer the reader
to [49,64–66,80–83] for other works on flat and curved superspace and off-shell multiplets
in five dimensions.

2.1     The standard Weyl multiplet

     The standard Weyl multiplet of 5D N = 1 conformal supergravity [61] is associated
with the gauging of the superconformal algebra F2 (4). The multiplet contains 32 + 32
physical components described by a set of independent gauge fields: the vielbein em a ,
the gravitino ψm iα , the SU(2)R gauge field φm ij , and a dilatation gauge field bm . The
other gauge fields associated with the remaining gauge symmetries: the spin connection
ωm ab , the S-supersymmetry connection φm iα , and the special conformal connection fm a
are composite fields, i.e., they are algebraically determined in terms of the other fields by
imposing constraints on some of the curvature tensors. The standard Weyl multiplet also
comprises a set of covariant auxiliary fields: a real antisymmetric tensor wab , a fermion
χiα , and a real auxiliary scalar D.
   The 5D N = 1 conformal superspace is parametrised by local bosonic (xm ) and
fermionic (θi ) coordinates z M = (xm , θiµ ), where m = 0, 1, 2, 3, 4, µ = 1, · · · , 4, and
i = 1, 2. To perform the gauging of the superconformal algebra, one introduces covariant
derivatives ∇A = (∇a , ∇iα ) which have the form
                              1
      ∇A = EA − ωA b Xb = EA − ΩA ab Mab − ΦA ij Jij − BA D − FA B KB ,             (2.1a)
                              2
                              1
                        = EA − ΩA ab Mab − ΦA ij Jij − BA D − FA αi Sαi − FA a Ka . (2.1b)
                              2
Here EA = EA M ∂M is the inverse super-vielbein, Mab are the Lorentz generators, Jij are
generators of the SU(2)R R-symmetry group, D is the dilatation generator, and KA =
(Ka , Sαi ) are the special superconformal generators. The super-vielbein one-form is E A =
dz M EM A with EM A EA N = δM    N
                                   and EA M EM B = δAB . We associate with each generator
Xa = (Mab , Jij , D, Sαi , Ka ) a connection super one-form ω a = (Ωab , Φij , B, Fαi , Fa ) =
dz M ωM a = E A ωA a .

                                              6
```

</details>

<a id="src-s23-p008"></a>

<details>
<summary>S23-p008 — PDF page 8: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p008: PDF page 8](https://arxiv.org/pdf/2302.14295v2#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
      The algebra of covariant derivatives
                                           1
                  [∇A , ∇B } = −TAB C ∇C − R(M)AB cd Mcd − R(J)AB kl Jkl
                                           2
                               − R(D)AB D − R(S)AB γk Sγk − R(K)AB c Kc ,                    (2.2)

is constrained to be expressed in terms of a single primary superfield, the super-Weyl
tensor Wαβ .4 It has the following properties

                        Wαβ = Wβα ,      KA Wαβ = 0 ,      DWαβ = Wαβ ,                      (2.3)

and satisfies the Bianchi identity
                                                 2
                            ∇kγ Wαβ = ∇k(α Wβγ) + εγ(α ∇δk Wβ)δ .                            (2.4)
                                                 5
In (2.2) TAB C is the torsion, and R(M)AB cd , R(J)AB kl , R(D)AB , R(S)AB γk , and R(K)AB c
are the curvatures associated with Lorentz, SU(2)R , dilatation, S-supersymmetry, and
special conformal boosts, respectively.
   The full algebra of covariant derivatives (2.2) (including the explicit expressions for
the torsion and curvature components in terms of the descendant superfields) are given
in Refs. [20] and [75]. To make use of results of [20] it is important to note that in this
paper we make use of the “traceless” frame conventional constraints for the conformal
superspace algebra employed in appendix C of [20] as well as in [75]. We also refer the
reader to these papers for the description of how to reduce superspace results to standard
component fields.
      It is useful to introduce the dimension-3/2 superfields
                                                          2
                           Wαβγ k := ∇k(α Wβγ) ,    Xαi := ∇βi Wβα ,                        (2.5a)
                                                          5
and the dimension-2 descendant superfields constructed from spinor covariant derivatives
of Wαβ :
                                                      (i   j)
                Wαβγδ := ∇k(α Wβγδ)k ,    Xαβ ij := ∇(α Xβ) ,    Y := i∇γk Xγk .            (2.5b)

It can be checked that only the superfields (2.5) and their vector derivatives appear upon
taking successive spinor derivatives of Wαβ . The following relations define the tower of
  4
    Here and in what follows, an antisymmetric rank-2 tensor Tab = −Tba can equivalently be written
as: Tab = (Σab )αβ Tαβ and Tαβ = 1/2 (Σab )αβ Tab .

                                                7
```

</details>

<a id="src-s23-p009"></a>

<details>
<summary>S23-p009 — PDF page 9: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p009: PDF page 9](https://arxiv.org/pdf/2302.14295v2#page=9) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
covariant fields in the standard Weyl multiplet and are particularly useful for analysing
the structure of curvature-squared invariants:

  ∇kγ Wαβ = Wαβγ k + εγ(α Xβ)   k
                                    ,                                                       (2.6a)
                         i             3i
     ∇iα Xβj = Xαβ ij + εij εαβ Y − εij (Γa )α ρ ∇a Wβρ − 2iεij Wα ρ Wβρ
                         8              2
                 i ij                  i
               + ε εαβ W γδ Wγδ − εij (Γa )β ρ ∇a Wαρ ,                                     (2.6b)
                 2                     2
                 1                                                           
 ∇iα Wβγλ j = − εij Wαβγλ + 3i(Γa )α(β ∇a Wγλ) + 3iεα(β (Γa )γ τ ∇a Wλ)τ
                 2
                 3
               − εα(β Xγλ) ij ,                                                             (2.6c)
                 2
 ∇iα Wβγλρ = −4i(Γa )α(β ∇a Wγλρ) i − 6iWα(βγ i Wλρ) + 6iWα(β Wγλρ) i
                                                                       
                                i
               +6iεα(β Wγλ Xρ)     − 2(Γa )γ τ ∇a Wλρ)τ i − Wγ τ Wλρ)τ i ,                  (2.6d)
                                                                                 3
 ∇iα Xβγ jk = iεi(j − 3W(β λ Wγ)αλ k) − εα(β W ρτ Wγ)ρτ k) − Wαλ Wβγ λk) − Wβγ Xαk)
                                                                                  2
                        1          k)    3
                      + Wα(β Xγ) + εα(β Wγ)λ X k)λ + 2(Γa )α ρ ∇a Wβγρ k)
                        2                2                                               
                                                              k)
                      + 2(Γa )(β ρ ∇a Wγ)αρ k) − (Γa )α(β ∇a Xγ) + εα(β (Γa )γ)λ ∇a X k)λ , (2.6e)
      ∇iα Y = 8(Γa )α β ∇a Xβi + 8Wα β Xβi .                                               (2.6f)

Due to (2.4), the Xαβ ij and Wαβγδ dimension-2 superfields of the standard Weyl multiplet
obey the following Bianchi identities:
                                              1
                             ∇(α γ Xβ)γ ij = − X γ(i Wαβγ j) ,                             (2.7a)
                                              2               
                             ∇(α Wβγτ )λ = 3i∇(α λ Wβγ Wτ )λ .
                                λ
                                                                                           (2.7b)

The independent descendant superfields of Wαβ are all annihilated by Ka . However, under
S-supersymmetry, they transform as follows:

                     Sαi Wβγδ j = 6δij εα(β Wγδ) ,     Sαi Xβj = 4δij Wαβ ,                (2.8a)
                     Sαi Wβγδρ = 24εα(β Wγδρ)i ,       Sαi Y = 8iXαi ,                     (2.8b)
                                       (j             (j      k)
                     Sαi Xβγ jk = −4δi Wαβγ k) + 4δi εα(β Xγ) .                            (2.8c)

   The conformal supergravity gauge group G is generated by covariant general coor-
dinate transformations, δcgct , associated with a local superdiffeomorphism parameter ξ A
and standard superconformal transformations, δH , associated with the local superfield pa-
rameters: the dilatation σ, Lorentz Λab = −Λba , SU(2)R Λij = Λji , and special conformal

                                                8
```

</details>

<a id="src-s23-p010"></a>

<details>
<summary>S23-p010 — PDF page 10: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p010: PDF page 10](https://arxiv.org/pdf/2302.14295v2#page=10) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
transformations ΛA = (η αi , ΛaK ). The covariant derivatives transform as

                                     δG ∇A = [K, ∇A ] ,                            (2.9a)

where
                                 1
                     K = ξ C ∇C + Λab Mab + Λij Jij + σD + ΛA KA .                 (2.9b)
                                 2
A covariant (or tensor) superfield U transforms as

                                δG U = (δcgct + δH )U = KU .                       (2.10)

The superfield U is a superconformal primary of dimension ∆ if KA U = 0 (it suffices to
require that Sαi U = 0) and DU = ∆U.

2.2     The Abelian vector multiplet

   In conformal superspace [20], a 5D N = 1 Abelian vector multiplet [83,84] is described
by a real primary superfield W of dimension 1,

                       (W )∗ = W ,      KA W = 0 ,        DW = W .                (2.11a)

The superfield W obeys the Bianchi identity

                                    j)   1
                                ∇(i            γ(i j)
                                 α ∇β W = εαβ ∇ ∇γ W .                           (2.11b)
                                         4

   Let us introduce the following descendants constructed from spinor derivatives of W :
                                               i           1 α(i j)
                  λiα := −i∇iα W ,     X ij := ∇α(i ∇j)
                                                     αW = − ∇   λα .              (2.12a)
                                              4            4
These superfields, along with
                          i                     1
                  Fαβ := − ∇k(α ∇β)k W − Wαβ W = ∇k(α λβ)k − Wαβ W ,             (2.12b)
                          4                     4
satisfy the following identities:

                  ∇iα λjβ = −2εij Fαβ + Wαβ W − εαβ X ij − εij ∇αβ W ,
                                                
                                                                                  (2.13a)
                                                          3i
                 ∇iα Fβγ = −i∇α(β λiγ) − iεα(β ∇γ) δ λiδ − Wβγ λiα − Wαβγ i W
                                                          2
                              i            3i
                            + Wα(β λiγ) − εα(β Wγ) δ λiδ ,                       (2.13b)
                             2             2

                                              9
```

</details>

<a id="src-s23-p011"></a>

<details>
<summary>S23-p011 — PDF page 11: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p011: PDF page 11](https://arxiv.org/pdf/2302.14295v2#page=11) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                    
                                       β k) 1         3i k) 
                ∇iα X jk = 2iεi(j                 βk)
                                     ∇α λβ − Wαβ λ + Xα W .                                (2.13c)
                                            2         4
We also note that Fαβ = 21 (Σab )αβ Fab . Due to (2.11b), a dimension-2 superfield of a vector
multiplet in the traceless frame obeys the following Bianchi identity:
                                                 1
                                     ∇(α γ Fβ)γ = λγk Wαβγk .                               (2.14)
                                                 2
   The actions of the S-supersymmetry generator on the descendants are given by

      Sαi λjβ = −2iεαβ εij W ,       Sαi Fβγ = 4εα(β λiγ) ,       Sαi X jk = −2εi(j λk)
                                                                                     α ,    (2.15)

while all the fields are annihilated by the Ka generators.
    In 5D N = 1 conformal superspace, there exists a prepotential formulation for the
Abelian vector multiplet, which, was developed in [20], see also [64, 66, 80, 81] for earlier
related analysis in other superspaces. The authors of [20] introduced a real primary
superfield Vij of dimension −2, DVij = −2Vij . It was also shown that Vij transforms
as an isovector under SU(2)R transformations and is the 5D analogue of Mezincescu’s
prepotential [85–87] for the 4D N = 2 Abelian vector multiplet. This then allows us to
represent the field strength W as
                                             3i
                                     W =−       ∇ij ∆ijkl Vkl ,                             (2.16)
                                             40
where we have defined the operators
                         1 αβγδ (i j k l)      1
                ∆ijkl := − ε   ∇α ∇β ∇γ ∇δ = − ∇(ij ∇kl) = ∆(ijkl) ,                       (2.17a)
                        96                    32
                   ij   α(i j)
                  ∇ := ∇ ∇α .                                                              (2.17b)

It should be noted that Vij in (2.16) is defined modulo gauge transformations of the form

                          δVkl = ∇pα Λα klp ,         Λα klp = Λα (klp) ,                   (2.18)

with the gauge parameter Λα klp being a primary superfield,
                                                           5
                          Sαi Λβ jkl = 0 ,      DΛβ jkl = − Λβ jkl .                        (2.19)
                                                           2

2.3    The linear multiplet

   The linear multiplet [88–98], or O(2) multiplet, can be described in terms of the
primary superfield Gij = Gji , which is characterised by the properties

                                 ∇(i
                                  αG
                                     jk)
                                         =0,                                               (2.20a)

                                                 10
```

</details>

<a id="src-s23-p012"></a>

<details>
<summary>S23-p012 — PDF page 12: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p012: PDF page 12](https://arxiv.org/pdf/2302.14295v2#page=12) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                               KA Gij = 0 ,              DGij = 3Gij .                       (2.20b)

We assume Gij to be real, (Gij )∗ = εik εjl Gkl .
   The component structure of Gij is characterised by the following tower of identities:

          ∇iα Gjk = 2εi(j ϕk)
                           α ,                                                               (2.21a)
                      i             i
          ∇iα ϕjβ = − εij εαβ F + εij Hαβ + i∇αβ Gij ,                                       (2.21b)
                      2             2
                                            3
           ∇α F = −2∇α ϕβ − 3Wαβ ϕβi − Xαj Gij ,
               i           β i
                                                                                             (2.21c)
                                            2
             i                β b i   3                1
          ∇α Ha = 4(Σab )α ∇ ϕβ − (Γa )α Wβγ ϕγi − (Γa )γ β Wβα ϕγi ,
                                           β
                                                                                             (2.21d)
                                      2                2
where we have defined the independent descendants superfields
                               1
                         ϕiα := ∇αj Gij ,                                                    (2.22a)
                               3
                                i                  i
                          F := ∇γi ∇jγ Gij = − ∇γk ϕγk ,                                     (2.22b)
                               12                  4
                                i
                       Habcd := εabcde (Γe )αβ ∇iα ∇jβ Gij ≡ εabcde He .                     (2.22c)
                               12
Here Ha obeys the differential condition
                                                      1
                           ∇a H a = 0 ,        Ha := − εabcde Hbcde .                         (2.23)
                                                      4!
The descendants (2.22) are all annihilated by Ka . Under the action of S-supersymmetry,
they transform as follows:

             Sαi ϕjβ = −6εαβ Gij ,       Sαi F = 6iϕiα ,        Sαi Hb = −8i(Γb )α β ϕiβ .    (2.24)

We refer the reader to [20] for a superform description of the linear multiplet.
   As described in [20], the linear multiplet constraints (2.20) may be solved in terms of
an arbitrary primary real dimensionless scalar prepotential Ω,

                                     Sαi Ω = 0 ,         DΩ = 0 ,                             (2.25)

and the solution is
                                                   3i ijkl
                                      Gij = −         ∆ ∇kl Ω .                               (2.26)
                                                   40
A crucial property of Gij defined by (2.26) is that it is invariant under gauge transforma-
tions of Ω of the form
                                      i
                                δΩ = − (Γa )αβ ∇iα ∇jβ Baij ,                                 (2.27)
                                      2

                                                    11
```

</details>

<a id="src-s23-p013"></a>

<details>
<summary>S23-p013 — PDF page 13: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p013: PDF page 13](https://arxiv.org/pdf/2302.14295v2#page=13) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
where the gauge parameter is assumed to have the properties
                  Ba ij = Ba ji ,    Sαi Ba jk = 0 ,   DBa ij = −Ba ij ,              (2.28)
and is otherwise arbitrary.
    To conclude this section we introduce another result that will be used in the rest
of the paper. Given a system of n Abelian vector multiplets W I , with I = 1, 2, . . . n,
all satisfying (2.11), we can construct the following composite linear multiplet and its
descendants [20]:
                       n                           o
               ij           J ij K       αJ (i j)K
            H = CJK 2W X            − iλ      λα     ,                           (2.29a)
                       
                                                     3
             ϕiα = CJK iX ij J λK        J βiK
                                αj − 2iFαβ λ      − Xαi W J W K − 2iW J ∇αβ λβiK
                                                     2
                                                             
                                    J  βiK             J βiK
                         − i(∇αβ W )λ        − 3iWαβ W λ       ,                 (2.29b)
                       
              F = CJK X ijJ XijK − F abJ Fab K
                                               + 4W J ✷W K + 2(∇a W J )∇a W K
                                                              39 ab
                         + 2i(∇α β λiJ  αK
                                    β )λi  − 6W ab Fab
                                                    J
                                                       WK −      W Wab W J W K
                                                               8     
                      3
                     + Y W J W K + 6X αi λJαi W K − 3iWαβ λαiJ λβK
                                                                i   ,                (2.29c)
                      8
                   
                      1         bc J de K        b
                                                   
                                                     J K 3        J  K
                                                                       
           Ha = CJK − εabcde F F          + 4∇ W Fba + Wba W W
                      2                                  2
                                               
                     + 2i(Σba )αβ ∇b (λiJ K
                                       α λβi )    ,                                  (2.29d)

where ✷ := ∇a ∇a and CJK = C(JK) is a constant symmetric in J and K. Equation (2.29)
is the superspace analogue of the composite linear multiplet constructed in [61].

3    Superconformal actions
   In this section, we review a main action principle that was used in [20] to construct var-
ious locally superconformally invariants (including curvature-squared ones) in superspace.
A simple way to define it is based on a full superspace integral
                     Z
             S[L] = d5|8 z E L ,       d5|8 z := d5 x d8 θ , E := Ber(EM A ) ,          (3.1)

where the Lagrangian L is a conformal primary superfield of dimension +1, DL = L. This
invariant can be proven to be locally superconformal invariant, that is, invariant under
the supergravity gauge transformations (2.9).

                                              12
```

</details>

<a id="src-s23-p014"></a>

<details>
<summary>S23-p014 — PDF page 14: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p014: PDF page 14](https://arxiv.org/pdf/2302.14295v2#page=14) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3.1    BF action

    The action involving the product of a linear multiplet with an Abelian vector multiplet
is referred to as the BF action. Analogous to the component superconformal tensor
calculus, this plays a fundamental role in the construction of general supergravity-matter
couplings, see [57–63] for the 5D case, and it was a main building block for the invariants
introduced in [20] that we focus on. In superspace the BF action may be described by
                               Z                 Z
                         SBF = d z E ΩW = d5|8 z E Gij Vij .
                                   5|8
                                                                                     (3.2a)

As implied by the equation above, the BF action can be written in different ways, see [20]
for even more variants. In the first form in (3.2a), it involves the field strength of the
vector multiplet, W , and the prepotential of the linear multiplet, Ω. By using (2.26),
(2.16), and then integrating by parts, one may obtain the equivalent form of the BF
action involving Mezincescu’s prepotential Vij and the field strength Gij described by the
right-hand side of (3.2a). One may also prove that the functionals d5|8 z E ΩW and
                                                                         R
R 5|8
  d z E Gij Vij are, respectively, invariant under the gauge transformations (2.27) and
(2.18), thanks to the defining differential constraints satisfied by W and Gij , eqs. (2.11b)
and (2.20a).
   In components, and in our notation, the BF action takes the form [20]
         Z      
 SBF = − d5 x e va Ha + W F + Xij Gij + 2λαk ϕαk
                                                                                                          (3.2b)
                  − ψa αi (Γa )α β ϕiβ W − iψa αi (Γa )α β λβj Gij + iψa αi (Σab )α β ψbβj W Gij       .

In (3.2b), we have defined the usual component projection to θ = 0, i.e., U(z)| := U(z)|θ=0 .
We associate the same symbol for the covariant component fields and the corresponding
superfields, when the interpretation is clear from the context. Here vm := Vm | denotes
a real Abelian gauge connection. Its real field strength is fmn := Fmn | = 2∂[m vn] . Note
that the field strength fmn may be expressed in terms of the bar-projected, covariant field
strength Fab := Fab | via the relation
                                               i
            Fab = fab + i(Γ[a )α β ψb] αk λkβ + W ψ[a γk ψb] kγ , fab := ea m eb n fmn . (3.3)
                                               2
When projected to components, the lowest component of the covariant superfield Ha
satisfies the constraint ∇a Ha = 0 , where Ha := Ha |. It holds that
                                                  i
                  Ha = ha + 2(Σab )α β ψb αi ϕiβ − εabcde (Σbc )αβ ψd αi ψe βj Gij . (3.4)
                                                  2
The constraint ∇a Ha = 0 implies the existence of a gauge three-form potential, bmnp , and
its exterior derivative hmnpq := 4∂[m bnpq] . See [20] and [75] for more details.

                                                   13
```

</details>

<a id="src-s23-p020"></a>

<details>
<summary>S23-p020 — PDF page 20: LOG primary, complete expanded superfield, descendant definitions and action</summary>

[S23-p020: PDF page 20](https://arxiv.org/pdf/2302.14295v2#page=20) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
Eqs. (3.22) play an important role in analysing superconformal primary equations of
motion in the next section. The resulting expression coincides, up to notations, to the
results of [25]. We will give the full component expressions (3.22) in a follow-up paper.
   By inserting the components of the composite linear multiplet (3.21) and (3.22) into
the BF action (3.2), one may construct the following higher-derivative invariant in a
standard Weyl multiplet background [20]
                  Z
                                 ij
          SWeyl = d5|8 z E Vij HWeyl                                            (3.23a)
                     Z       
                                                          ij
                = − d5 x e va HWeyl a
                                      + W FWeyl + Xij HWeyl    + 2λk ϕk Weyl
                                                                             
                            a i              a    ij           ab        ij
                     − ψai Γ ϕWeyl W − iψai Γ λj HWeyl + iψai Σ ψbj W HWeyl , (3.23b)

where the spinor indices here are suppressed. This defines a locally supersymmetric
extension of the Weyl squared term [25, 27, 30, 32].

3.6     log W

   We now consider a composite linear superfield which includes a supersymmetric Ricci
tensor-squared term. In superspace, it was described for the first time in [20] in analogy
with the construction of a higher-derivative chiral invariant in 4D N = 2 supergravity [33].
The composite superfield makes use of the standard Weyl multiplet coupled to the off-shell
vector multiplet compensator. It takes the form5

                    ij           3i ijkl           3i
                   Hlog W = −       ∆ ∇kl log W =      ∇(ij ∇kl) ∇kl log W .                      (3.24)
                                 40               1280
In general such a linear multiplet could be defined by replacing W with any primary
scalar superfield of weight q for which it is possible to prove that (3.24) satisfies all the
linear multiplet constraints, eq. (2.20), see [20]. However, for various applications, we
choose to construct it in terms of the vector multiplet superfield strength, W . Due to the
complexity in computing the action of six spinor derivatives on the “log multiplet,” the
                          ij
component analysis of Hlog   W has not appeared so far. This calculation can be performed
                                                                                      ij
with the aid of the Cadabra software. Here we find that the full expression of Hlog      W in
terms of the descendant superfields of the vector and standard Weyl multiplets is given
   5
     Note that there is an overall minus sign difference between the definition of the log W invariant in
this paper and the one of [20].

                                                   19
```

</details>

<a id="src-s23-p021"></a>

<details>
<summary>S23-p021 — PDF page 21: LOG primary, complete expanded superfield, descendant definitions and action</summary>

[S23-p021: PDF page 21](https://arxiv.org/pdf/2302.14295v2#page=21) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
by

 ij       3i              51i αi j
Hlog W = −   Wab X abij +     X Xα
          8 (             64
                  9 ij       3i             1            9                    1
        +W −1       X Y − Fab X abij − ✷X ij − X ij W ab Wab + W ab Wab α(i λj)            α
                 64           8             2            64                   4
                                                               )
                   3                 j)   3                 j)
               − (Γa )αβ Xα(i ∇a λβ + (Γa )αβ λ(i   α ∇a X β
                   4                      4
              (
                 1 ij          1                   1                       i α(j i)
        +W −2      X ✷W + ∇a W ∇a X ij + F ab Wab α(i λj)
                                        
                                                                    α − λ       ✷λα
                 2             2                   4                       2
                    i                    3i                             j)   3i a αβ i j c
                 − ∇a λαi ∇a λjα − ǫabcde (Σab )αβ Wde λ(i
                             
                                                                 α ∇c λ β −     (Γ ) λα λβ ∇ Wac
                    4                   16                                    8
                    3i             3                  j)     3i
                 + Y λαi λjα + (Σab )αβ F ab Xα(i λβ +           W ab Wab λαi λjα
                    64             8                        128        )
                     9i abcde      αβ         i j      3 ij αk
                 +      ǫ     (Γa ) Wbc Wde λα λβ − X X λαk
                    256                                8
              (
                 1 ij ab          1               1
        +W −3      X F Fab − X ij X kl Xkl − X ij ∇a W ∇a W
                                                                 
                 8                8               4
               i                              j)     i a αβ     (i b j)
              − ǫabcde (Σab )αβ Fde λ(iα ∇c λβ − (Γ ) Fab λα ∇ λβ
               8                                     4
               i                            i                          i
              − (Γa )αβ λiα λjβ ∇c Fac + (Γa )αβ X ij λkα ∇a λβk + (Γa )αβ X k(i λj)
                                                                                  α ∇a λβk
               4                            4                          4
               i                                  i            3i a  α(i
              − (Γa )αβ λ(i         j)l
                                         λβl + λαi λjα ✷W +         ∇ W λ ∇a λj)
                                        
                          α ∇a X                                                 α
               4                                 4             4
               i                           b j)     3i a αβ                   3i
              − (Σab )αβ ∇a W λ(i                      (Γ ) Wab λiα λjβ ∇b W + Wab F ab λαi λjα
                                  
                                     α ∇ λβ −
               2                                    16                        32
               9i abcde       αβ            i j       3i    αβ ij     ab k
              + ǫ       (Γa ) Wbc Fde λα λβ − (Σab ) X W λα λβk
               64                                    32 )
               3i                        3i
              − X αk λ(iαλ
                           βj)
                                λβk − X αk λβi λjβ λαk
                8                        8
             (
                 3i                             3i
        +W −4 − λαi λjα ∇a W ∇a W − (Γa )αβ X k(i λj)
                                  
                                                              α λβk ∇a W
                16                               8
                  3i a αβ                  3i                 3i
                 +  (Γ ) Fab λiα λjβ ∇b W + F ab Fab λαi λjα + ǫabcde (Γa )αβ Fbc Fde λiα λjβ
                  8                        32                 64
                  3i                        3i ij kl α         3i
                 − (Σab ) X F λα λβk − X X λk λαl − X kl Xkl λαi λjα
                         αβ ij ab k
                  16                        16                 32
                  15 a αβ i j γk              9 a αβ (i ρj) k
                 − (Γ ) λα λβ λ ∇a λγk − (Γ ) λα λ λβ ∇a λρk
                  64                         32

                                             20
```

</details>

<a id="src-s23-p022"></a>

<details>
<summary>S23-p022 — PDF page 22: LOG primary, complete expanded superfield, descendant definitions and action</summary>

[S23-p022: PDF page 22](https://arxiv.org/pdf/2302.14295v2#page=22) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                        15 a αβ (i ρj) k             15
                       −   (Γ ) λα λ λρ ∇a λβk − (Γa )αβ λρi λjρ λkα ∇a λβk
                        32                           64                              )
                         9                              9
                       + (Σab )αβ W ab λ(i
                                        αλ
                                           ρj) k
                                              λβ λρk + (Σab )αβ W ab λρi λjρ λkα λβk
                        32                             64
                   (
              −5 3 a αβ (i ρj) k              3
         +W        (Γ ) λα λ λβ λρk ∇a W + (Σab )αβ F ab λρi λjρ λkα λβk
                 8                            8
                                       )
                   3
                + X kl λαi λjα λβk λβl
                   8
               (                                          )
            −6   3i αi j βk l γ          3i αi k βj l γ
         +W         λ λα λ λβ λk λγl + λ λα λ λβ λk λγl .                                 (3.25)
                 32                      16

Using the explicit expression (3.25), together with the relations (2.6), (2.8c), (2.13), and
                                ij
(2.15), we have shown that Hlog    W is indeed a primary and linear superfield satisfying
                                                                                        ij
(2.20). Furthermore, we have computed the descendants of the primary superfield Hlog       W
defined as
                                            1      ij
                                 ϕαlogi W = ∇αj Hlog  W ,                                (3.26a)
                                            3
                                             i          ij
                                 Flog W = ∇αi ∇αj HlogW    ,                             (3.26b)
                                            12
                                   a         i a αβ          ij
                                 Hlog   W =    (Γ ) ∇αi ∇βj HlogW .                      (3.26c)
                                            12
By using (3.25) and the BF action, eqs. (3.2a) and (3.2b), one may construct the following
locally superconformal invariant in a standard Weyl multiplet background
                    Z
                                   ij
           Slog W = d5|8 z E Vij Hlog   W                                          (3.27a)
                      Z       
                          5           a                       ij       k
                  = − d x e va Hlog      W + W Flog W + Xij Hlog W + 2λ ϕk log W
                                                                             
                          a i                a    ij             ab      ij
                    −ψai Γ ϕlog W W − iψai Γ λj Hlog W + iψai Σ ψbj W Hlog W .     (3.27b)

The resulting component action includes, for example, a (✷✷W ) term which, upon gauge-
fixing W = 1, includes a Ricci tensor squared combination. A more detailed discussion
of the (fairly involved) component structure of (3.26) will be given elsewhere.

                                                 21
```

</details>

### C24: cached source equations

Source PDF: 2024-Gold-Components-of-curvature-squared-invariants.pdf. SHA-256: `0e30ca2f64d6e7e8e08f653f08a85883a06c74377c2fb57f578dc01c00fedca2`.

<a id="src-c24-p008"></a>

<details>
<summary>C24-p008 — PDF page 8: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p008: PDF page 8](https://arxiv.org/pdf/2311.00679v1#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
and applications of our results. We accompany our paper with three appendices and
a long supplementary file. Appendix A collects results about conformal superspace in
the traceless frame of [30, 96]. In appendix B we present several equations that we have
                                                                  a
used to turn the result we have obtained in Cadabra for the Hlog    descendant of the Log
multiplet to its simplified form given in equations (4.8c) and (4.8d). Finally, in appendix
C we explain how to map our notations and conventions to the ones of some other groups.

2       Superconformal multiplets

   This section is devoted to a review of several superconformal multiplets in five di-
mensions which are the building blocks for the various supersymmetric curvature-squared
invariants discussed in this paper. We will first describe the standard Weyl multiplet
and then move on to the off-shell Abelian vector and linear multiplets. For each of the
previously mentioned multiplets, we will present both their formulations in superspace
and components for completeness. Our analysis follows the superspace and components
notation and results of [30, 31, 96].3

2.1     The standard Weyl multiplet

   We begin by describing the standard Weyl multiplet in conformal superspace and
components.

2.1.1    The standard Weyl multiplet in superspace

   In five dimensions, the standard Weyl multiplet [83] is associated with the gauging of
the superconformal algebra F2 (4). The multiplet contains 32 + 32 physical components
described by a set of independent gauge fields: the vielbein em a , the gravitino ψm iα , the
SU(2)R gauge field φm ij , and a dilatation gauge field bm . The other fields associated
with the remaining gauge symmetries: the spin connection ωm ab , the S-supersymmetry
connection φm iα , and the special conformal connection fm a are composite, meaning that
they are determined in terms of the other fields by imposing some appropriate curvature
constraints. The standard Weyl multiplet also contains a set of matter fields: a real
antisymmetric tensor wab , a fermion χiα , and a real auxiliary scalar D.
   3
     For various discussions on off-shell multiplets in five dimensions, see also other works based on
superspace, e.g., [71, 86–88, 98–102], and component approaches, e.g., [72–85].

                                                  7
```

</details>

<a id="src-c24-p009"></a>

<details>
<summary>C24-p009 — PDF page 9: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p009: PDF page 9](https://arxiv.org/pdf/2311.00679v1#page=9) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
     The N = 1 conformal superspace is parametrised by local bosonic (xm ) and fermionic
(θi ) coordinates z M = (xm , θiµ ), where m = 0, 1, 2, 3, 4, µ = 1, · · · , 4, and i = 1, 2. To
gauge the superconformal algebra, one introduces covariant derivatives ∇A = (∇a , ∇iα )
which have the form
                              1
      ∇A = EA − ωA b Xb = EA − ΩA ab Mab − ΦA ij Jij − BA D − FA B KB ,             (2.1a)
                              2
                              1
                        = EA − ΩA ab Mab − ΦA ij Jij − BA D − FA αi Sαi − FA a Ka . (2.1b)
                              2

Here EA = EA M ∂M is the inverse super-vielbein, Mab are the Lorentz generators, Jij are
generators of the SU(2)R R-symmetry group, D is the dilatation generator, and KA =
(Ka , Sαi ) are the special superconformal generators. The super-vielbein one-form is E A =
dz M EM A with EM A EA N = δM       N
                                       and EA M EM B = δAB . Associated with each generator
Xa = (Mab , Jij , D, Sαi , Ka ) is the connection super one-form ω a = (Ωab , Φij , B, Fαi , Fa ) =
dz M ωM a = E A ωA a .
      The algebra of covariant derivatives

                                           1
                  [∇A , ∇B } = −TAB C ∇C − R(M)AB cd Mcd − R(J)AB kl Jkl
                                           2
                               − R(D)AB D − R(S)AB γk Sγk − R(K)AB c Kc ,                    (2.2)

is constrained to be expressed in terms of a single primary superfield, the super-Weyl
tensor Wαβ ,4 which has the following properties

                       Wαβ = Wβα ,       KA Wαβ = 0 ,     DWαβ = Wαβ ,                       (2.3)

and satisfies the Bianchi identity

                                                 2
                            ∇kγ Wαβ = ∇k(α Wβγ) + εγ(α ∇δk Wβ)δ .                            (2.4)
                                                 5

In (2.2), TAB C is the torsion, while R(M)AB cd , R(J)AB kl , R(D)AB , R(S)AB γk , and R(K)AB c
are the curvatures associated with Lorentz, SU(2)R , dilatation, S-supersymmetry, and
special conformal boosts, respectively.
   In this paper we make use of the “traceless” frame conventional constraints for the
conformal superspace algebra employed in appendix C of [30] as well as in [96]. The full
  4
    Here and in what follows, an antisymmetric rank-2 tensor Tab = −Tba can equivalently be written
as: Tab = (Σab )αβ Tαβ and Tαβ = 1/2 (Σab )αβ Tab .

                                                8
```

</details>

<a id="src-c24-p010"></a>

<details>
<summary>C24-p010 — PDF page 10: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p010: PDF page 10](https://arxiv.org/pdf/2311.00679v1#page=10) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
algebra of covariant derivatives (2.2) (including the explicit expressions for the torsion
and curvature tensors) are given in appendix A of our paper.
   Let us introduce the dimension-3/2 superfields

                                                         2
                         Wαβγ k := ∇k(α Wβγ) ,     Xαi := ∇βi Wβα ,                     (2.5a)
                                                         5
and the following dimension-2 descendant superfields

                                                    (i   j)
              Wαβγδ := ∇k(α Wβγδ)k ,    Xαβ ij := ∇(α Xβ) ,   Y := i∇γk Xγk .           (2.5b)

It can be checked that only the superfields (2.5) and their vector derivatives appear upon
taking successive spinor derivatives of Wαβ . Specific relations that connect the various
descendant fields which we will need later are given below:

  ∇kγ Wαβ = Wαβγ k + εγ(α Xβ)  k
                                   ,                                                     (2.6a)
                         i            3i
     ∇iα Xβj = Xαβ ij + εij εαβ Y − εij (Γa )α ρ ∇a Wβρ − 2iεij Wα ρ Wβρ
                         8            2
                 i ij                i
               + ε εαβ W γδ Wγδ − εij (Γa )β ρ ∇a Wαρ ,                                  (2.6b)
                 2                   2
                 1                                                        
 ∇iα Wβγλ j = − εij Wαβγλ + 3i(Γa )α(β ∇a Wγλ) + 3iεα(β (Γa )γ τ ∇a Wλ)τ
                 2
                 3
               − εα(β Xγλ) ij ,                                                          (2.6c)
                 2
 ∇iα Wβγλρ = −4i(Γa )α(β ∇a Wγλρ) i − 6iWα(βγ i Wλρ) + 6iWα(β Wγλρ) i
                                                                      
                                i
               +6iεα(β Wγλ Xρ)    − 2(Γa )γ τ ∇a Wλρ)τ i − Wγ τ Wλρ)τ i ,                (2.6d)
                                                                              3
 ∇iα Xβγ jk = iεi(j − 3W(β λ Wγ)αλ k) − εα(β W ρτ Wγ)ρτ k) − Wαλ Wβγ k)λ − Wβγ Xαk)
                                                                               2
                        1         k)   3            k)λ       a ρ          k)
                      + Wα(β Xγ) + εα(β Wγ)λ X + 2(Γ )α ∇a Wβγρ
                        2              2                                              
                                                            k)
                      + 2(Γ )(β ∇a Wγ)αρ k) − (Γa )α(β ∇a Xγ) + εα(β (Γa )γ)λ ∇a X k)λ , (2.6e)
                           a    ρ

      ∇iα Y = 8(Γa )α β ∇a Xβi + 8Wα β Xβi .                                            (2.6f)

As implied by (2.4), the dimension-2 superfields Xαβ ij and Wαβγδ obey the following
Bianchi identities in the traceless frame:
                                             1
                            ∇(α γ Xβ)γ ij = − X γ(i Wαβγ j) ,                           (2.7a)
                                             2               
                            ∇(α Wβγτ )λ = 3i∇(α λ Wβγ Wτ )λ .
                               λ
                                                                                        (2.7b)

                                               9
```

</details>

<a id="src-c24-p011"></a>

<details>
<summary>C24-p011 — PDF page 11: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p011: PDF page 11](https://arxiv.org/pdf/2311.00679v1#page=11) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
The independent descendant superfields of Wαβ , specifically Wαβγ k , Xαi , Wαβγδ , Xαβ ij , Y ,
are all annihilated by Ka . However, under S-supersymmetry, they transform as follows:

                     Sαi Wβγδ j = 6δij εα(β Wγδ) ,    Sαi Xβj = 4δij Wαβ ,               (2.8a)
                     Sαi Wβγδρ = 24εα(β Wγδρ)i ,       Sαi Y = 8iXαi ,                   (2.8b)
                                     (j            (j      k)
                     Sαi Xβγ jk = −4δi Wαβγ k) + 4δi εα(β Xγ) .                          (2.8c)

We also stress that in the paper, and in the supplementary file, we will often use the
following notation:

                                                     3i
                              Φab ij := R(J)ab ij = − Xab ij .                            (2.9)
                                                     4

    The gauge group of conformal supergravity is denoted by G. It is generated by covari-
ant general coordinate transformations, δcgct , associated with a local superdiffeomorphism
parameter ξ A and standard superconformal transformations, δH , associated with the lo-
cal superfield parameters: the dilatation σ, Lorentz Λab = −Λba , SU(2)R Λij = Λji , and
special conformal (bosonic and fermionic) transformations ΛA = (η αi , ΛaK ). The covariant
derivatives transform as

                                      δG ∇A = [K, ∇A ] ,                                (2.10a)

with
                                 1
                     K = ξ C ∇C + Λab Mab + Λij Jij + σD + ΛA KA .                      (2.10b)
                                 2
A covariant (or tensor) superfield U transforms as

                                δG U = (δcgct + δH )U = KU .                             (2.11)

The superfield U is said to be superconformal primary of dimension ∆ if KA U = 0 (it
suffices to require that Sαi U = 0) and DU = ∆U.

2.1.2   The standard Weyl multiplet in components

    Let us now explain how to systematically obtain various component fields of the stan-
dard Weyl multiplet from the superspace geometry described in the subsection 2.1.1. The
vielbein (em a ) and gravitini (ψm iα ) appear as the coefficients of dxm of the super-vielbein

                                               10
```

</details>

<a id="src-c24-p012"></a>

<details>
<summary>C24-p012 — PDF page 12: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p012: PDF page 12](https://arxiv.org/pdf/2311.00679v1#page=12) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
E A = (E a , Eiα ) = dz M EM A ,

                           em a (x) := Em a (z)| ,      ψm iα (x) := 2Em iα (z)| ,                     (2.12)

where a single vertical line next to a superfield denotes the usual component projection to
θ = 0, i.e., V (z)| := V (z)|θ=0 . This operation can be written in a coordinate-independent
way using the so-called double-bar projection [103, 104]

                           ea = dxm em a = E a || ,        ψαi = dxm ψm iα = 2Eαi || ,                 (2.13)

where the double-bar denotes setting θ = dθ = 0. The remaining fundamental and
composite one-forms are also obtained by taking the projections of the corresponding
superspace one-forms,

         φij := Φij || ,     b := B|| ,   ω ab := Ωab || ,    φαi := 2 Fαi || ,   fa := Fa || .        (2.14)

   The covariant matter fields are contained within the super-Weyl tensor Wαβ and its
independent descendants,

                                Wαβ := Wαβ | ,                                                        (2.15a)
                                        3i i     3i
                                 χiα :=    Xα | = ∇βi Wβα | ,                                         (2.15b)
                                        32       80
                                           3         3i k
                                 D := −       Y|= −    ∇ ∇βk W αβ | .                                 (2.15c)
                                          128       320 α

The other components of the super Weyl tensor are given by Wab iα := Wab iα |, Wαβγδ :=
Wαβγδ | and Φab ij := Φab ij | = − 3i4 Xab ij | = − 3i4 (Σab )αβ Xαβ ij |.5 These will turn out to be
composite and expressed in terms of the component curvatures.
   Taking the double-bar projection of ∇ = E A ∇A , the component vector covariant
derivative ∇a is defined to coincide with the projection of the superspace derivative ∇a |,

                 1             1                              1
   em a ∇a = ∂m − ψm αi ∇iα | − ωm ab Mab − bm D − φm ij Jij − φm αi Sαi − fm a Ka .                   (2.16)
                 2             2                              2

Here, the projected spinor covariant derivative ∇iα | corresponds to the generator of Q-
supersymmetry. It is defined such that if U = U|, then Qiα U := ∇iα |U := (∇iα U)|. For
the other generators, e.g., Mab U = (Mab U)|, there is no ambiguity in identifying the bar
   5
    In the case of Wαβ , Wab iα , Φab ij , and Wαβγδ , unless specified, it should be clear from the context if
we refer to the superfields or their component projections.

                                                      11
```

</details>

<a id="src-c24-p013"></a>

<details>
<summary>C24-p013 — PDF page 13: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p013: PDF page 13](https://arxiv.org/pdf/2311.00679v1#page=13) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
projection; hence, local diffeomorphisms, Q-supersymmetry transformations, and so forth
descend naturally from their corresponding rule in superspace.
       The component supercovariant curvature tensors are given by

                                                          1
            [∇a , ∇b ] = −R(P )ab c ∇c − R(Q)ab αi ∇iα | − R(M)ab cd Mcd − R(J)ab ij Jij
                                                          2
                         − R(D)ab D − R(S)ab Sγk − R(K)ab c Kc .
                                             γk
                                                                                               (2.17)

We have introduced R(P )ab c = Tab c | and R(Q)ab iα = Tab iα |. R(M)ab cd , R(J)ab ij , R(D)ab ,
R(S)ab γk , and R(K)ab c coincide with the lowest components of the corresponding super-
space curvature tensors given in appendix A.
    The constraints on the superspace curvatures determine how to supercovariantise a
given component curvature by taking the double-bar projection of the superspace torsion
and each of the curvature two forms. One then finds [30]6

                                                    i
               R(P )ab c = 2 ea m eb n D[m en] c − ψaj Γc ψb j ,                             (2.18a)
                                                    2
               R(Q)ab α = ea eb D[m ψn] α + i(Γ[a φb] i )α
                      i      m n            i

                              1                                     
                           + Wcd 3(Σcd Γ[a )α β − (Γ[a Σcd )α β ψb] iβ ,                     (2.18b)
                              8
              R(M)ab = R(ω)ab cd + 8 δ[a [c fb] d] − 2 ψ[aj Σcd φb] j
                     cd

                              16i [c         d] i
                                                         
                                                                     cdi    [c      d]i
                                                                                        
                           +      δ[a ψb]i Γ χ − iψ[ai Γb] R(Q) + 2Γ R(Q)b]
                               3
                              i                   i
                           + ψaj ψb j W cd − (ψaj Γe ψb j )W̃ cde ,                           (2.18c)
                              2                   4
                     ij             ij        (i           (i
               R(J)ab = R(φ)ab − 3 ψ[a φb] j) − 8i ψ[a Γb] χj) ,                             (2.18d)
                                                                      8i
                R(D)ab = 2 ea m eb n ∂[m bn] + 4 f[ab] + ψ[aj φb] j + ψ[aj Γb] χj ,           (2.18e)
                                                                       3
where we have also defined
                                              1
                                       W̃abc = εabcde W de .                                   (2.19)
                                              2
In (2.18), we have introduced the spin, dilatation, and SU(2)R covariant derivative

                          1
                 Dm = ∂m − ωm bc Mbc − bm D − φm ij Jij ,            Da = ea m Dm .            (2.20)
                          2
   6
    When defining products of spinors, the spinor indices are sometimes suppressed. The spinor indices
should be viewed as contracted from top left to bottom right.

                                                  12
```

</details>

<a id="src-c24-p014"></a>

<details>
<summary>C24-p014 — PDF page 14: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p014: PDF page 14](https://arxiv.org/pdf/2311.00679v1#page=14) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
Note that the covariant derivative Da obeys the following commutation relation

                                     1
                       [Da , Db ] = − R(ω)ab cd Mcd − R(φ)ab ij Jij ,                  (2.21)
                                     2
where the curvatures takes the form
                                                                         
                              cd        m   n         cd        ce      d
                      R(ω)ab := 2ea eb ∂[m ωn] − ω[m ωn]e ,                           (2.22a)
                                                                          
                      R(φ)ab ij := 2 ea m eb n ∂[m φn] ij + φ[m k(i φj) n]k .         (2.22b)

The component curvatures turn out to obey “traceless” conventional constraints [30]

               R(P )ab c = 0 ,      (Γa )α β R(Q)ab iβ = 0 ,      R(M)ab cb = 0 ,      (2.23)

thus allowing us to solve for the composite connections as follows:

                         i
     ωabc = ω(e)abc + (ψak Γc ψb k + ψck Γb ψa k − ψbk Γa ψc k ) + 2b[b ηc]a ,        (2.24a)
                         4
              2            1                     1                              
    i φm i = (Γ[p δm q] + Γm Σpq ) D[p ψq] i + Wcd 3Σcd Γ[p ψq] i − Γ[p Σcd ψq] i ,   (2.24b)
              3            4                      8
                1              1                   i                   i
       fa b = − R(ω)ac bc + δa b R(ω)cd cd − ψcj Γ[b R(Q)a c]j − ψcj Γa R(Q)bcj
                6              48                 6                   12
                1                 1                       2i
              + ψ[aj Σbd φd] j − δa b (ψcj Σcd φd j ) − (ψaj Γb χj )
                3                 24                       3
                 i                   i
              − ψaj ψc j W bc + (ψaj Γe ψd j )W̃ bde
                12                 24
                  i                                            
              +     δa b 2(ψcj ψd j )W cd − (ψcj Γe ψd j )W̃ cde .                    (2.24c)
                192

Here ω(e)abc = − 12 (Cabc + Ccab − Cbca ) is the usual torsion-free spin connection expressed
in terms of the anholonomy coefficient Cmn a := 2∂[m en] a . The Riemann tensor is denoted
by R(ω)ab cd = Rab cd , whereas Ra b = Rac bc and R = Rab ab correspond to Ricci tensor and
Ricci scalar, respectively. The dilatation curvature R(D)ab now vanishes due to eqs. (2.24).
It is worth noting that in the traceless frame φm i has no dependence upon the matter
field χi , and fa b has no dependence upon D. This choice minimises the dependence of
the covariant derivatives upon some matter “auxiliary” fields and will simplify part of the
analysis in the coming sections.
   The supersymmetry transformations of the fundamental gauge connections of the Weyl
multiplet can be derived directly from the transformations of their corresponding super-
space one-forms. We restrict to all local superconformal transformations except local

                                                13
```

</details>

<a id="src-c24-p015"></a>

<details>
<summary>C24-p015 — PDF page 15: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p015: PDF page 15](https://arxiv.org/pdf/2311.00679v1#page=15) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
translations (covariant general coordinate transformations). We denote such transforma-
tions by δ = δQ + δH and define the operator

                              1
                 δ = ξiα Qiα + λab Mab + λij Jij + λD D + λa Ka + η αi Sαi .                    (2.25)
                              2
Here, the local component parameters are respectively defined as the θ = 0 components
of the corresponding superfield parameters, ξiα := ξiα |, λab := Λab |, λij := Λij |, λD := σ|,
λa := ΛaK |, and η αi := η αi |. The local superconformal transformations of the independent
connection fields of the standard Weyl multiplet are given by [30]

             δem a = i (ξi Γa ψm i ) − λD em a + λa b em b ,                                  (2.26a)
                                   1                           
            δψm iα = 2Dm ξαi − Wcd (Γm Σcd )α β − 3(Σcd Γm )α β ξβi + 2i (Γm η i )α
                                   4
                        1 ab                               1
                     + λ (Σab ψm i )α + λi j ψm jα − λD ψm iα ,                               (2.26b)
                        2                                  2
            δφm = ∂m λ − 2φm k λ + 3ξ φm − 3η (i ψm j) + 8iξ (i Γm χj) ,
                ij         ij         (i  j)k     (i    j)
                                                                                              (2.26c)
                                8i
              δbm = ∂m λD − ξi Γm χi − ξi φm i − ψm i ηi − 2λm .                              (2.26d)
                                3

In like fashion, one can derive the transformations δωm ab , δφmα i , and δfma , which we omit
since these fields are composite. For the covariant matter fields, the transformations are
given by [30]

                             32i
     δWab = 2i ξi R(Q)ab i −     ξi Σab χi − 2λ[a c Wb]c + λD Wab ,                            (2.26e)
                              3
           1            1                           3                                           
     δχαi = ξ αi D − (ξj Σab )α R(J)ab ij −           (∇a Wbc ) 3(ξ i Γa Σbc )α + (ξ i Σbc Γa )α
           2           16                         128
               3                               3i
           +      Wab Wcd εabcde (ξ i Γe )α + (η i Σab )α Wab
              256                              16
              1 ab i                         3
           − λ (χ Σab )α + λi j χαj + λD χαi ,                                                  (2.26f)
              2                              2
      δD = 2i ξi Γa ∇a χi + iWab (ξi Σab χi ) + 2ηi χi + 2λD D ,                               (2.26g)

where
                                                  16i
           ∇a Wbc = Da Wbc − iψai R(Q)bc i +          ψai Σbc χi ,                            (2.27a)
                                                   3
                             1          3i                 1
           ∇a χαi = Da χαi − ψa αi D − (φa i Σbc )α Wbc + (ψaj Σbc )α R(J)bc ij
                             4          32                32
                       3           
                                        i b cd α      i cd b α
                                                               
                    +     (∇b Wcd ) 3(ψa Γ Σ ) + (ψa Σ Γ )
                      256

                                                 14
```

</details>

<a id="src-c24-p016"></a>

<details>
<summary>C24-p016 — PDF page 16: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p016: PDF page 16](https://arxiv.org/pdf/2311.00679v1#page=16) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                            3
                       −       Wbc Wde εbcdef (ψa i Γf )α .                                   (2.27b)
                           512
For completeness, we give the following projection rules of the vector covariant derivative
action on the descendant component fields

                          1                                                          
   ∇a Wβγ iλ = Da Wβγ iλ − ψa iα Wαβγλ + 3i(Γa )α(β ∇a Wγλ) + 3iεα(β (Γa )γ τ ∇a Wλ)τ
                          2
               +iψaj(β Φγλ) ij + 3φa i(β Wγλ) ,                                        (2.27c)
      ∇a D = Da D − iψa αi (Γa )α β ∇a χiβ − iψa αi Wα β χiβ + φa iα χαi ,                      (2.27d)
                           3        
  ∇a Φβγ jk = Da Φβγ jk + ψa α(j − 3W(β λ Wγ)αλ k) − εα(β W ρτ Wγ)ρτ k) − Wαλ Wβγ k)λ
                           8
                                       16i          k)
                   + 16iWβγ χk)  α −        Wα(β χγ) − 16iεα(β Wγ)λ χk)λ + 2(Γa )α ρ ∇a Wβγρ k)
                                        3
                                                  32i a             k)    32i                       
                   + 2(Γa )(β ρ ∇a Wγ)αρ k) +          (Γ )α(β ∇a χγ) −       εα(β (Γa )γ)λ ∇a χk)λ
                                                    3                      3
               3i α(j                     (j k)
              − φa Wαβγ k) − 16φa (β χγ) ,                                                      (2.27e)
                2                                                                          
  ∇a Wβγλρ = Da Wβγλρ + iψa αi 2(Γa )α(β ∇a Wγλ iρ) + 3Wα(β iγ Wλρ) − 3Wα(β Wγλ iρ)
                         32i                                                       
              +3iψa αi(β −      Wγλ χiρ) − 2(Γa )γ τ ∇a Wλρ)τ i − Wγ τ Wλρ)τ i
                             3
                      i
              +12φa(β Wγδρ)i .                                                                  (2.27f)

2.2     The Abelian vector multiplet

    Following the presentation and conventions of [31, 96], let us turn to the description
of an off-shell Abelian vector multiplet.

2.2.1   The Abelian vector multiplet in superspace

    To describe the Abelian vector multiplet [101, 105] in conformal superspace [30], we
introduce a real primary superfield W of dimension 1,

                        (W )∗ = W ,           KA W = 0 ,       DW = W .                       (2.28a)

The superfield W is subject to the Bianchi identity

                                       j)   1
                                   ∇(i            γ(i j)
                                    α ∇β W = εαβ ∇ ∇γ W .                                     (2.28b)
                                            4

                                                    15
```

</details>

<a id="src-c24-p017"></a>

<details>
<summary>C24-p017 — PDF page 17: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p017: PDF page 17](https://arxiv.org/pdf/2311.00679v1#page=17) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
Acting with spinor covariant derivatives on W gives the following descendants:

                                                  i           1 α(i j)
                  λiα := −i∇iα W ,        X ij := ∇α(i ∇j)
                                                        αW = − ∇   λα .                    (2.29a)
                                                 4            4
These superfields, along with

                          i                     1
                  Fαβ := − ∇k(α ∇β)k W − Wαβ W = ∇k(α λβ)k − Wαβ W ,                       (2.29b)
                          4                     4
satisfy the identities:

                  ∇iα λjβ = −2εij Fαβ + Wαβ W − εαβ X ij − εij ∇αβ W ,
                                                
                                                                                           (2.30a)
                                                           3i
                 ∇iα Fβγ = −i∇α(β λiγ) − iεα(β ∇γ) δ λiδ − Wβγ λiα − Wαβγ i W
                                                           2
                              i            3i
                            + Wα(β λiγ) − εα(β Wγ) δ λiδ ,                                 (2.30b)
                             2             2
                  i    jk      i(j
                                   
                                     β k)     1        βk)    3i k) 
                 ∇α X = 2iε ∇α λβ − Wαβ λ + Xα W .                                         (2.30c)
                                              2               4
Due to (2.28b), a dimension-2 superfield of a vector multiplet in the traceless frame obeys
the following Bianchi identity:

                                              1
                                  ∇(α γ Fβ)γ = λγk Wαβγk .                                  (2.31)
                                              2
It is useful to note that the S-supersymmetry generator acts on the descendants as

       Sαi λjβ = −2iεαβ εij W ,      Sαi Fβγ = 4εα(β λiγ) ,       Sαi X jk = −2εi(j λk)
                                                                                     α ,    (2.32)

while all the superfields are annihilated by Ka .
   It is worth noting that there exists a prepotential formulation for the Abelian vector
multiplet which was developed in [30], see also [86, 88, 98, 99] for related works in other
superspaces. The formulation of [30] is based on a real primary superfield Vij of dimension
−2, i.e., DVij = −2Vij . Here Vij transforms as an isovector under SU(2)R transformations
and is the 5D analogue of Mezincescu’s prepotential [106–108] for the 4D N = 2 Abelian
vector multiplet. This then allows us to represent the field strength W as

                                             3i
                                  W =−          ∇ij ∆ijkl Vkl ,                             (2.33)
                                             40

                                                 16
```

</details>

<a id="src-c24-p018"></a>

<details>
<summary>C24-p018 — PDF page 18: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p018: PDF page 18](https://arxiv.org/pdf/2311.00679v1#page=18) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
where we have defined the operators

                         1 αβγδ (i j k l)      1
                ∆ijkl := − ε   ∇α ∇β ∇γ ∇δ = − ∇(ij ∇kl) = ∆(ijkl) ,                          (2.34a)
                        96                    32
                   ij   α(i j)
                  ∇ := ∇ ∇α .                                                                 (2.34b)

Let us also point out that Vij in (2.33) is defined modulo gauge transformations of the
form

                            δVkl = ∇pα Λα klp ,         Λα klp = Λα (klp) ,                    (2.35)

with the gauge parameter Λα klp being a dimension −5/2 primary superfield,

                                                              5
                            Sαi Λβ jkl = 0 ,       DΛβ jkl = − Λβ jkl .                        (2.36)
                                                              2

2.2.2   The Abelian vector multiplet in components

    The component structure of the vector multiplet follows directly from the superfield
definitions (2.29). It contains a real scalar field W := W |, gaugini λiα := λiα |, a triplet
of auxiliary fields X ij := X ij |, and a real Abelian gauge connection vm := Vm | or, equiv-
alently, its real field strength fmn := Fmn | = 2∂[m vn] . The field strength fmn may be
expressed in terms of the covariant field strength Fab := Fab | via the relation

                                              i
           Fab = fab + i(Γ[a )α β ψb] αk λkβ + ψ[a γk ψb] kγ W ,     fab := ea m eb n fmn .    (2.37)
                                              2
The dilatation weights of the vector multiplet fields are summarised in Table 1.

                                     W         λiα X ij     Fab    vm
                                   D 1         3/2 2         2      0

                    Table 1: Dilatation weights of the Abelian vector multiplet.

   The transformations of the component fields in a standard Weyl multiplet background
can be obtained from the corresponding superfields. They read

              δW = iξi λi + λD W ,                                                            (2.38a)
              δλiα = −(Σab ξ i )α Fab − (Σab ξ i )α Wab W + ξαj X ij + (Γa ξ i )α ∇a W
                      1                              3
                     + λab (Σab λi )α + λi j λjα + λD λiα + 2iηα i W ,                        (2.38b)
                      2                              2

                                                   17
```

</details>

<a id="src-c24-p019"></a>

<details>
<summary>C24-p019 — PDF page 19: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p019: PDF page 19](https://arxiv.org/pdf/2311.00679v1#page=19) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                            i
              δX ij = −2iξ (i Γa ∇a λj) − ξ (i Σab λj) Wab − 16i(ξ (i χj) )W
                                           2
                      +2λ(i k X j)k − 2η (i λj) + 2λD X ij ,                                      (2.38c)
               δvm = i(ξ i ψmi )W − i(ξ i Γm λi ) + ∂m λV ,                                       (2.38d)

where
                                      i
                     ∇a W = Da W − ψai λi ,                                                       (2.39a)
                                      2
                                      1                        1
                     ∇a λiα = Da λiα + (Σbc ψa i )α Fbc + Wbc W − ψaαj X ij
                                      2                          2
                               1 b i
                              − (Γ ψa )α ∇b W − iφaα i W .                                        (2.39b)
                               2
For completeness, we include
                                                  
                                                            k) 1          3i        
        ∇a X   jk
                    = Da X   jk
                                  + iψa αi εi(j       ∇α β λβ − Wαβ λβk) + Xαk) W       + φα(j k)
                                                                                           a λα , (2.39c)
                                              2              4
                          i α                               3
         ∇a Fβγ = Da Fβγ + ψa i ∇α(β λiγ) + εα(β ∇γ) δ λiδ + Wβγ λiα − iWαβγ i W
                          2                                 2
                                                 
                       1          3
                     − Wα(β λiγ) + εα(β Wγ) δ λiδ + 2φa i(β λγ)i .                                (2.39d)
                       2          2

Note that we have also included in (2.38d) the gauge field transformation parametrised
by the local real parameter λV .

2.3     The linear multiplet

   We now turn to the discussion of the off-shell linear multiplet coupled to conformal
supergravity.

2.3.1   The linear multiplet in superspace

   The linear multiplet [109–119], or O(2) multiplet, can be described in terms of the
dimension three primary superfield Gij = Gji with the properties

                                      ∇(i
                                       αG
                                          jk)
                                              =0,                                                 (2.40a)
                                       KA Gij = 0 ,             DGij = 3Gij ,                     (2.40b)

where Gij is assumed to be real, (Gij )∗ = εik εjl Gkl .

                                                           18
```

</details>

<a id="src-c24-p020"></a>

<details>
<summary>C24-p020 — PDF page 20: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p020: PDF page 20](https://arxiv.org/pdf/2311.00679v1#page=20) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    The following tower of descending identities is useful to elaborate on the component
structure of the superfield Gij :

          ∇iα Gjk = 2εi(j ϕk)
                           α ,                                                              (2.41a)
                      i              i
          ∇iα ϕjβ = − εij εαβ F + εij Hαβ + i∇αβ Gij ,                                      (2.41b)
                      2             2
                                               3
           ∇iα F = −2∇α β ϕiβ − 3Wαβ ϕβi − Xαj Gij ,                                        (2.41c)
                                               2
                                       3                 1
          ∇iα Ha = 4(Σab )α β ∇b ϕiβ − (Γa )α β Wβγ ϕγi − (Γa )γ β Wβα ϕγi ,                (2.41d)
                                       2                 2
with the independent descendant superfields being defined as

                              1
                        ϕiα := ∇αj Gij ,                                                    (2.42a)
                              3
                               i                  i
                         F := ∇γi ∇jγ Gij = − ∇γk ϕγk ,                                     (2.42b)
                              12                  4
                               i
                      Habcd := εabcde (Γe )αβ ∇iα ∇jβ Gij ≡ εabcde He .                     (2.42c)
                              12
Here Ha obeys the differential condition

                                                     1
                          ∇a H a = 0 ,        Ha := − εabcde Hbcde .                         (2.43)
                                                     4!
The descendants (2.42) are all annihilated by Ka . Under the action of S-supersymmetry,
they transform as follows:

            Sαi ϕjβ = −6εαβ Gij ,       Sαi F = 6iϕiα ,        Sαi Hb = −8i(Γb )α β ϕiβ .    (2.44)

We refer the reader to [30] for a superform description of the linear multiplet.
   There exists a prepotential formulation for the linear multiplet in superspace [30]. The
constraints (2.40) may be solved in terms of an arbitrary primary real dimensionless scalar
prepotential Ω,

                                    Sαi Ω = 0 ,         DΩ = 0 ,                             (2.45)

which leads to
                                                  3i ijkl
                                     Gij = −         ∆ ∇kl Ω .                               (2.46)
                                                  40

                                                   19
```

</details>

<a id="src-c24-p021"></a>

<details>
<summary>C24-p021 — PDF page 21: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p021: PDF page 21](https://arxiv.org/pdf/2311.00679v1#page=21) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
An important property of Gij defined by (2.46) is that it is invariant under gauge trans-
formations of Ω of the form
                                       i
                                 δΩ = − (Γa )αβ ∇iα ∇jβ Baij ,                          (2.47)
                                       2
where the gauge parameter is assumed to have the properties

                   Ba ij = Ba ji ,    Sαi Ba jk = 0 ,    DBa ij = −Ba ij ,              (2.48)

and is otherwise arbitrary.
    It is useful to note that given a system of n Abelian vector multiplets W I , with I =
1, 2, . . . n, all satisfying (2.28), we can construct the following composite linear multiplet
and its descendants [30]:
                     n                           o
           H ij = CJK 2W J X ij K − iλαJ (i λj)K
                                             α     ,                                   (2.49a)
                     
                                                   3
           ϕiα = CJK iX ij J λK       J βiK
                              αj − 2iFαβ λ      − Xαi W J W K − 2iW J ∇αβ λβiK
                                                   2
                                                           
                                  J  βiK             J βiK
                       − i(∇αβ W )λ       − 3iWαβ W λ        ,                         (2.49b)
                     
            F = CJK X ijJ XijK − F abJ FabK
                                             + 4W J ✷W K + 2(∇a W J )∇a W K
                                                                 39 ab
                          + 2i(∇α β λiJ  αK
                                     β )λi  − 6W ab Fab
                                                     J
                                                        WK −        W Wab W J W K
                                                                  8     
                       3
                      + Y W J W K + 6X αi λJαi W K − 3iWαβ λαiJ λβK
                                                                 i   ,                 (2.49c)
                       8
                    
                       1                                  3            
            Ha = CJK − εabcde F bc J F de K + 4∇b W J Fba
                                                       K
                                                          + Wba W J W K
                       2                                   2
                                                 
                      + 2i(Σba )αβ ∇b (λiJ  K
                                         α λβi )   ,                                   (2.49d)

where ✷ := ∇a ∇a and CJK = C(JK) is a constant symmetric in J and K. Equation
(2.49) is the superspace analogue of the composite linear multiplet constructed for the
first time in [83]. Note that it is possible to create a composite linear multiplet from a
single Abelian vector multiplet by setting CJK = 1 when J = K = 1 and zero otherwise.
This case will play an important role.

                                               20
```

</details>

<a id="src-c24-p022"></a>

<details>
<summary>C24-p022 — PDF page 22: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p022: PDF page 22](https://arxiv.org/pdf/2311.00679v1#page=22) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2.3.2     The linear multiplet in components

   The components of the linear multiplet follows directly from the superfield description:
an SU(2)R triplet of Lorentz scalar fields Gij = Gij | ; a spinor field ϕαi = ϕαi | ; a scalar field
F = F |; and a covariant closed anti-symmetric four-form field strength Habcd := Habcd |.
The latter is equivalent to a conserved dual vector Ha := −1/4! εabcde Hbcde .7 It holds that

                                                     i
                     Ha = ha + 2(Σab )α β ψb αi ϕiβ − εabcde (Σbc )αβ ψd αi ψe βj Gij .                  (2.50)
                                                     2
The covariant conservation equation for Ha is

                                                 ∇a Ha = 0 .                                             (2.51)

The constraint implies that there exists a gauge three-form potential, bmnp , and its exterior
derivative, such that hmnpq := 4∂[m bnpq] , with bmnp := Bmnp |.
    The local superconformal transformations of the covariant fields can be derived using
(2.41) and (2.44), which give

                  δGij = −2ξ(i ϕj) − 2λ(i k Gj)k + 3λD Gij ,                                            (2.52a)
                           i          i
                  δϕαi = − ξαi F − Ha (Γa ξi )α − i(Γa ξ j )α ∇a Gij + 6ηα j Gij
                          2           2
                          1 ab                         7
                         + λ (Σab ϕi )α − λi j ϕjα + λD ϕαi ,                                          (2.52b)
                          2                            2
                                        3
                   δF = 2ξ i Γa ∇a ϕi − (ξ i Σab ϕi )Wab + 16i(ξ i χj )Gij
                                        2
                                i
                         +6i η ϕi + 4λD F ,                                                             (2.52c)
                                            1                1
                  δHa = −4ξ i Σab ∇b ϕi − (ξ i Γb ϕi )Wab + εabcde W bc (ξ i Σde ϕi )
                                            2                2
                              b                      i
                         +λa Hb + 4λD Ha − 8iη Γa ϕi ,                                                 (2.52d)

where

         ∇a Gij = Da Gij + ψa(i ϕj) ,                                                 (2.53a)
                           i          i            i
         ∇a ϕαi = Da ϕαi + ψaαi F + (Γb ψai )α Hb + (Γb ψa j )α ∇b Gij − 3φaα j Gij . (2.53b)
                           4          4            2
   7
    The Levi-Civita tensor with world indices is defined as εmnpqr := εabcde ea m eb n ec p ed q ee r , such that
εabcde and εabcde are normalised as ε01234 = −ε01234 = 1.

                                                       21
```

</details>

<a id="src-c24-p023"></a>

<details>
<summary>C24-p023 — PDF page 23: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p023: PDF page 23](https://arxiv.org/pdf/2311.00679v1#page=23) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
For completeness, we also have

                                          3
        ∇a F = Da F − (Γb ψai )α ∇b ϕiα + ψai β Wαβ ϕiα − 8iGij ψaj α χiα + 3iφai α ϕiα ,(2.53c)
                                          2
                                            3                     1
       ∇a Hb = Da Hb − 2(Σbc ψai )α ∇c ϕiα + (Γb ψai )α W αβ ϕiβ + ψai β Wαβ (Γb ϕi )α
                                            4                     4
               +4i(Γb φai )α ϕiα .                                                       (2.53d)

The locally superconformal transformations of bmnp are

            δbmnp = 2 εabcde em a en b ep c (ξi Σde ϕi ) − 12i(ψ[m i Σnp] ξ j )Gij + 3∂[m lnp] ,   (2.54)

where we have also included the gauge transformation δl bmnp = 3∂[m lnp] leaving hmnpq and
Ha invariant. The dilatation weights of the O(2) multiplet are summarised in Table 2.

                                        Gij    ϕαi F        Ha     bmnp
                                   D     3     7/2 4        4       0

                     Table 2: Dilatation weights of the off-shell O(2) multiplet.

3     Superconformal actions

   In this section we review a main action principle that has played an important role in
constructing various locally superconformal invariants including the two-derivative gauged
supergravity action. The reader should refer to [30] for a more complete analysis.

3.1     BF action

    Consider a full superspace integral
                     Z
            S[L] = d5|8 z E L ,       d5|8 z := d5 x d8 θ ,               E := Ber(EM A ) ,         (3.1)

where the Lagrangian L is a conformal primary superfield of dimension +1, i.e, DL = L.
The above action is locally superconformal, that is, invariant under the supergravity gauge
transformations (2.10).

                                                    22
```

</details>

<a id="src-c24-p024"></a>

<details>
<summary>C24-p024 — PDF page 24: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p024: PDF page 24](https://arxiv.org/pdf/2311.00679v1#page=24) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    One of the main building blocks for the construction of general supergravity-matter
couplings [79–85] and higher-derivative invariants in [30] is the so-called BF action prin-
ciple. It is based on an appropriate product of a linear multiplet with an Abelian vector
multiplet, which may be described by the following form in superspace
                              Z                Z
                        SBF = d z E ΩW = d5|8 z E Gij Vij .
                                  5|8
                                                                                     (3.2a)

As shown above, the BF action can be written in different ways, see [30] for even more
variants. In the first form in (3.2a), it involves the field strength of the vector multiplet,
W , and the prepotential of the linear multiplet, Ω. Equivalently, the BF action can be
written in terms of the Mezincescu’s prepotential Vij and the field strength Gij of the
linear multiplet described by the right-hand side of (3.2a). In addition, the functionals
R 5|8
   d z E ΩW and d5|8 z E Gij Vij are, respectively, invariant under the gauge transfor-
                    R

mations (2.47) and (2.35), thanks to the defining differential constraints satisfied by W
and Gij , (2.28b) and (2.40a).
   In components, and in our notation, the BF action takes the form [30]
                   Z         
         SBF = −       d5 x e va Ha + W F + Xij Gij + 2λαk ϕαk
                                                                                                
                −ψa αi (Γa )α β ϕiβ W − iψa αi (Γa )α β λβj Gij + iψa αi (Σab )α β ψbβj W Gij       (3.2b)
                                    1
                 Z          
              = − d5 x e − εabcde fab bcde + W F + Xij Gij + 2λαk ϕαk
                                   12
                                                                                              
                 −ψa αi (Γa )α β ϕiβ W − iψa αi (Γa )α β λβj Gij + iψa αi (Σab )α β ψbβj W Gij ,    (3.2c)

where it should be noted that sometimes we associate the same symbol for the covariant
component fields and the corresponding superfields, when the interpretation is clear from
the context.

3.2    Vector multiplet compensator

   The two-derivative action for the vector multiplet compensator can be constructed via
the BF action principle (3.2a), with the linear multiplet being a composite superfield. We
            ij
denote by HVM  the composite linear multiplet (2.49),

                            ij                       i
                           HVM = i(∇α(i W )∇j)
                                             α W + W∇
                                                       α(i j)
                                                          ∇α W
                                                    2
                               = −iλαi λjα + 2W X ij .                                               (3.3)

                                                   23
```

</details>

<a id="src-c24-p032"></a>

<details>
<summary>C24-p032 — PDF page 32: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p032: PDF page 32](https://arxiv.org/pdf/2311.00679v1#page=32) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
We also note the relation

             ∇a ∇b Wcd = Da Db Wcd − 2fab Wcd + 4fa[c Wd]b − 4faf ηb[c Wd] f + · · · ,              (4.5)

with
                          1     1                                        1
                   fab = − Rab + ηab R + . . . ,             fa a = −      R + ... ,                (4.6)
                          6     48                                      16
and the ellipsis corresponding to omitted fermionic contributions. Having obtained the
full component expressions, the first non-trivial check we have done is to show that the
                a                                         a
divergence of HWeyl  vanishes up to fermions, that is ∇a HWeyl = 0. One can show that this
holds with the use of the Bianchi identities on Cabcd and Φab ij , along with the fact that
        ab                             ab
∇a ∇b H̃Weyl = 0 up to fermions as H̃Weyl  is a K-invariant, SU(2)-singlet, antisymmetric
tensor. In addition, we have checked explicitly that all the component fields described in
(4.3) are K-primary.

4.2     Log

   As an extension of the higher-derivative chiral invariant in 4D N = 2 supergravity [45],
Ref. [30] proposed a composite linear superfield which describes a supersymmetric Ricci
                                                     ij
tensor-squared term. This primary superfield, Hlog      , makes use of the standard Weyl
multiplet coupled to the off-shell vector multiplet compensator. It is given by9

                      ij        3i ijkl           3i
                     Hlog =−       ∆ ∇kl log W =      ∇(ij ∇kl) ∇kl log W .                         (4.7)
                                40               1280
Due to the complexity in computing the action of up to eight spinor derivatives on the
                                                 ij
“log multiplet”, the component structure of Hlog     has just been studied recently. With
                                                                   ij
the aid of the Cadabra software [94, 95], the full expression of Hlog in its expanded form
in terms of the descendants of W and Wαβ appeared for the first time in [31]. Its lowest
               ij
component, Hlog   |, is given by

 ij      1             272i αi j
Hlog =     Wab Φabij −     χ χα
         2      (       3
                              1       1        9              1
         +W −1 − 6X ij D + Fab Φabij − ✷X ij − X ij W ab Wab + W ab Wab α(i λj)
                                                                             α
                              2       2       64              4
   9
    Note the overall minus sign difference between the definition of the log W invariant in this paper and
the one of [30].

                                                   31
```

</details>

<a id="src-c24-p033"></a>

<details>
<summary>C24-p033 — PDF page 33: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p033: PDF page 33](https://arxiv.org/pdf/2311.00679v1#page=33) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                                       )
                             j)                j)
          + 8i(Γa )αβ χ(i            a αβ (i
                       α ∇a λβ − 8i(Γ ) λα ∇a χβ

          (
     −2       1 ij          1                      1                   i α(j i)
                X ✷W + ∇a W ∇a X ij + F ab Wab α(i λj)
                                    
+W                                                              α − λ        ✷λα
              2             2                      4                   2
                 i                   3i                             j)   3i a αβ i j c
              − ∇a λαi ∇a λjα − εabcde (Σab )αβ Wde λ(i
                          
                                                             α ∇c λ β −     (Γ ) λα λβ ∇ Wac
                 4                   16                                   8
                                                   j)   3i
              − 2iDλαi λjα − 4i(Σab )αβ F ab χ(iα λβ +      W ab Wab λαi λjα
                                                       128         )
                  9i abcde                       j
              +      ε     (Γa )αβ Wbc Wde λiα λβ + 4iX ij χαk λαk
                 256
          (
              1 ij ab    1               1
+W −3           X F Fab − X ij X kl Xkl − X ij ∇a W ∇a W
                                                   
              8          8               4
           i                              j)    i a αβ     (i b j)
          − εabcde (Σab )αβ Fde λ(i
                                  α ∇c λβ − (Γ ) Fab λα ∇ λβ
           8                                    4
           i a αβ i j c                i a αβ ij k                i
          − (Γ ) λα λβ ∇ Fac + (Γ ) X λα ∇a λβk + (Γa )αβ X k(i λj)          α ∇a λβk
           4                           4                          4
           i                                 i            3i a  α(i
          − (Γa )αβ λ(i        j)l
                                     λβl + λαi λjα ✷W +        ∇ W λ ∇a λj)
                                   
                     α ∇a X                                                 α
           4                                 4            4
           i                          b j)     3i a αβ                   3i
          − (Σab )αβ ∇a W λ(i                     (Γ ) Wab λiα λjβ ∇b W + Wab F ab λαi λjα
                             
                                α ∇ λβ −
           2                                   16                        32
           9i abcde      αβ             i j      3i    αβ ij      ab k
          + ε       (Γa ) Wbc Fde λα λβ − (Σab ) X W λα λβk
           64                                   32)

          − 4χαk λ(i
                  αλ
                     βj)
                         λβk − 4χαk λβi λjβ λαk
          (
                  3i αi j            3i
+W −4                λ λα ∇a W ∇a W − (Γa )αβ X k(i λj)
                              
              −                                      α λβk ∇a W
                  16                 8
               3i a αβ                       3i                 3i
              +   (Γ ) Fab λiα λjβ ∇b W + F ab Fab λαi λjα + εabcde (Γa )αβ Fbc Fde λiα λjβ
               8                             32                 64
               3i                             3i                 3i
              − (Σab )αβ X ij F ab λkα λβk − X ij X kl λαk λαl − X kl Xkl λαi λjα
               16                             16                 32
               15 a αβ i j γk                   9 a αβ (i ρj) k
              − (Γ ) λα λβ λ ∇a λγk − (Γ ) λα λ λβ ∇a λρk
               64                              32
               15 a αβ (i ρj) k                 15
              − (Γ ) λα λ λρ ∇a λβk − (Γa )αβ λρi λjρ λkα ∇a λβk
               32                               64                             )
                9                                  9
              + (Σab )αβ W ab λ(i
                                αλ
                                    ρj) k
                                        λβ λρk + (Σab )αβ W ab λρi λjρ λkα λβk
               32                                 64
          (
              3 a αβ (i ρj) k          3
+W −5           (Γ ) λα λ λβ λρk ∇a W + (Σab )αβ F ab λρi λjρ λkα λβk
              8                        8

                                          32
```

</details>

<a id="src-c24-p034"></a>

<details>
<summary>C24-p034 — PDF page 34: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p034: PDF page 34](https://arxiv.org/pdf/2311.00679v1#page=34) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                       )
                 3 kl αi j β
               + X λ λα λk λβl
                 8
              (                                                   )
                3i                  γ      3i                γ
        +W −6      λαi λjα λβk λlβ λk λγl + λαi λkα λβj λlβ λk λγl .                  (4.8a)
                32                         16

                                                            ij
The full expressions of the descendant component fields of Hlog , including the fermionic
terms, are very involved and can be found in the supplementary file. In this subsection,
                                                                             ij
we will only present the bosonic sectors. The component Flog = 12i ∇αi ∇αj Hlog | takes the
form
         1                 8             368 ab        1
 Flog = − W ab W cd Cabcd + D 2 + 4✷D +     W Wab D − Φabij Φabij
         2                 3              3            6
                           1                39           1005 ab
        +2Wcd∇c ∇a W ad − Wcd ∇a ∇c W ad + Wcd ✷W cd −        W Wab W cd Wcd
                           2                16           2048
         9                  3               33               9
        − ∇a Wab ∇c W bc − ∇a W bc ∇b Wac + ∇a W bc ∇a Wbc + εabcde Wbc Wde ∇f Waf
         4 (                4               16              16
                                   1             3
        +W −1 − Fcd ∇c ∇a W ad − Fcd ∇a ∇c W ad + Fcd ✷W cd + 2Wcd ∇c ∇a F ad
                                   2             2
                     1                                            1
                    + Wcd ✷F cd − 4D✷W − ✷✷W − 4∇a W ∇a D − W ab F cd Cabcd
                     2                                            4
                     9 c                 9                    3
                    − Wa Wcb ∇a ∇b W + Wcd ∇a W ∇c W ad − Wcd ∇a W ∇a W cd
                     2                   2                   16
                     9                    3                3
                    + Wcd ∇c W ∇a W ad − W cd Wcd ✷W − ∇a Fab ∇c W bc
                     2                   32                2
                                                                               )
                     3 a bc           9 abcde
                    + ∇ F ∇a Wbc + ε           2Wcd Fef ∇f Wab + Wbc Wde ∇f Faf
                     2                16
                (
                                  1           1                   75 ab
        +W −2       − F ab Fab D − Fcd ✷F cd + F ab F cd Cabcd −     W Wab F cd Fcd
                                  2           4                  128
                     9                   3                   3
                    + W ab Wbc F cdFda − Fcd ∇a W ∇a W cd − Wcd ∇a W ∇a F cd
                     4                   2                   2
                     3 cd
                    − W Fcd ✷W + 2D∇a W ∇a W + 2∇a W ∇a ✷W + ✷W ✷W
                     2
                     1 a b                             1           1
                    + ∇ ∇ W ∇a ∇b W + 3X ij Xij D + X ij ✷Xij + ∇a X ij ∇a Xij
                     2                                 2           4
                     9 c                    3                       1
                    + Wa Wcb ∇a W ∇b W + W cd Wcd ∇a W ∇a W − ∇a F bc ∇a Fbc
                     4                      64                      4
                     1 ij ab           9 ij                3
                    − X F Φabij +         X Xij W ab Wab + εabcde Wcd Fef ∇f Fab
                     2                128                  8

                                               33
```

</details>

<a id="src-c24-p035"></a>

<details>
<summary>C24-p035 — PDF page 35: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p035: PDF page 35](https://arxiv.org/pdf/2311.00679v1#page=35) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                                )
                       3
                      − εabcde Fbc Fde ∇f Waf
                       8
                  (
                       3                   3
        +W −3         − W ab F cd Fab Fcd + W ab F cd Fac Fbd − Fa c Fcb ∇a ∇b W
                       4                   2
                                                             1
                      + Fcd ∇a W ∇a F cd + Fcd ∇c W ∇a F ad + F cd Fcd ✷W
                                                             4
                        3 cd                    3
                      + W Fcd ∇a W ∇a W − ∇a W ∇a W ✷W − ∇a W ∇b W ∇a ∇b W
                        2                       2                                  )
                        3 ij             3 ij a              1 abcde          f
                      − X Xij ✷W − X ∇ W ∇a Xij − ε                  Fbc Fde ∇ Faf
                        4                2                   8
                  (
             −4           3 ab               3                   3
        +W            −      F Fab F cd Fcd + F ab Fbc F cd Fda + Fa c Fcb ∇a W ∇b W ∇a W
                          32                 8                   2
                       3                 3                 3
                      − F cdFcd ∇a W − X ij Xij F ab Fab + (∇a W ∇a W )2
                       8                 16                8 )
                       9                    3
                      + X ij Xij ∇a W ∇a W + X ij Xij X kl Xkl
                       8                    32
        + fermions .                                                                        (4.8b)

                                                                               ij
                                                     a
    The initial expression for the top component, Hlog  = 12i (Γa )αβ ∇αi ∇βj Hlog |, obtained
from the computer algebra program Cadabra, is quite extensive and contains 261 terms in
the bosonic part alone. For completeness, this expression is given in appendix B. However,
there are ample opportunities for simplification by utilising the algebra of commutators
(A.4), symmetry properties of the Weyl tensor and the Bianchi identities (2.7), (2.31).
Additionally, many terms in the expression can be further combined as they exhibit similar
structures and are linearly dependent, see appendix B.
                                           a
   The ultimate goal is to express Hlog       in terms of total derivatives as much as possible,
           a          ab
that is, Hlog = ∇b H̃log + . . . . The reason is that, once coupled to the vector potential va in
                                                                             ab
the component BF action (3.2b), this term will be proportional to Fab H̃log     upon integration
by parts. This task, however, proves to be challenging, as determining the most suitable
combinations of terms to combine into total derivatives is not obvious beforehand. Despite
these difficulties, the expression provided by Cadabra remains approachable, and progress
has been made by manually combining terms to reach a final expression of the form

                   a          1 abcde               3
                  Hlog =        ε     Φbc ij Φdeij − ∇b C abcd Wcd
                             12                     8
                               3 −1
                             − W ∇b C abcd Fcd + ∇b H̃log ab
                                                              + fermions ,                  (4.8c)
                               8

                                                    34
```

</details>

<a id="src-c24-p036"></a>

<details>
<summary>C24-p036 — PDF page 36: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p036: PDF page 36](https://arxiv.org/pdf/2311.00679v1#page=36) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
        ab
where H̃log is antisymmetric and is given by

     ab              9                    3                    3
   H̃log = −4W ab D + εabcde Wcd ∇f Wef + εabcde Wcf ∇f Wde − W ab W cd Wcd
                     4                    4                   32
            9 ac       bd    3 abcd      3    ab
           − W Wcd W − C Wcd + ✷W
            2 (              2           2
                            3                  3                  3
           +W −1 4F ab D + εabcde Fcf ∇f Wde + εabcde Fde ∇f Wcf + εabcde Wde ∇f Fcf
                            4                  2                  2
                           3                   9
                         + εabcde Wef ∇f Fcd + εcdef [b∇a] W WcdWef + 3∇c W [b c ∇a] W
                           4                   8
                                                                75
                         + 6∇[a Wc b] ∇c W + 3W ab ✷W + ✷F ab + W cd Wcd F ab
                                                               )32
                         + 9W c[aWcd F b]d + Φab ij X ij − C abcd Fcd
                     (
                −2       1 abcde             1                   3
           +W              ε     Fcf ∇f Fde + εabcde Fcd ∇f Fef − εabcde Wcd Fef ∇f W
                         4                   2                   8
                           3                      3                       1
                         + εabcde Wcf Fde ∇f W + εcdef [aWcd Fef ∇b] W − F ab ✷W
                           8                      8                       2
                                                           3
                         + F c[a∇b] ∇c W + ∇[a W ∇c F b]c − W ab ∇c W ∇c W + 3W c[aFcd F b]d
                                                           2                            )
                           3               3                1               3
                         + W ab F cdFcd + F c[a Wcd F b]d − ∇c W ∇c F ab + F ab W cdFcd
                           4               2                2               2
                     (
                         1 cdef [a                1
           +W −3           ε       Fcd Fef ∇b] W + F ab ∇c W ∇c W
                         4                        2
                                                                            )
                           1                               1
                          + F ab F cd Fcd + F ac Fcd F db + X ij Xij F ab       .                  (4.8d)
                           4                               4

   We also note the following useful relations (up to fermions)

         ∇a ∇b W = Da Db W − 2fab W + . . . ,                                                      (4.9a)
        ∇a ∇b X ij = Da Db X ij − 4fab X ij + . . . ,                                              (4.9b)
        ∇a ∇b Fcd = Da Db Fcd − 4fab Fcd + 4fa[c Fd]b − 4faf ηb[c Fd] f + . . . ,                  (4.9c)
          ∇a ✷W = Da Db D b W − 2Da (fb b W ) + 2fab D b W + . . . ,                               (4.9d)
           ✷✷W = Da D a Db D b W − 2Da D a (fbb W ) + 4fab D a D b W
                          +2D a fab D b W − 6fa a Db D b W − 4fab fab W + 12faa fb b W + . . . ,   (4.9e)
         ∇a ∇b D = Da Db D − 4fab D + . . . .                                                      (4.9f)

                                                    35
```

</details>

<a id="src-c24-p037"></a>

<details>
<summary>C24-p037 — PDF page 37: Main4.2: LOG primary and descendants, including full4.8a</summary>

[C24-p037: PDF page 37](https://arxiv.org/pdf/2311.00679v1#page=37) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                                  a
    It is useful to express the component field Hlog  in terms of the degauged covariant
derivative Da . Degauging all the covariant derivative ∇a in (4.8c) but not those implicit
     ab
in H̃log results in the following expression:

                      a       1 abcde
                     Hlog =      ε    Φbc ij Φdeij + Db H̃log
                                                          ab
                                                              − fbc K c H̃log
                                                                          ab
                              12
                                3                  3
                              − Db C abcd Wcd − W −1 Db C abcd Fcd .               (4.10a)
                                8                  8
This can equivalently be written as

                         a       1 abcde
                        Hlog =      ε    Φbc ij Φdeij + Db (H̃log
                                                              ab      ab
                                                                  + Ĥlog ),       (4.10b)
                                 12
        ab
where Ĥlog is antisymmetric and is explicitly defined as

                        5                       5
                ab
              Ĥlog =      RW ab + Rc[a W b] c + RF ab W −1 + Rc[a F b] c W −1 .   (4.10c)
                        16                      16
In order to derive (4.10b), we have made use of the following Riemann tensor properties

                              C abcd = Rabcd + 4η c[afb]d − 4η d[a fb]c ,          (4.11a)
                          D[a Rbc]de = 0 ,                                         (4.11b)
                           Dd Rabcd = −2D [a Rb]c ,                                (4.11c)
                                      1
                            Da Rab = D a R .                                       (4.11d)
                                      2
Having obtained the full component expressions, the first non-trivial check we have done
                                    a                                       a
is to show that the divergence of Hlog vanishes up to fermions, that is ∇a Hlog = 0. Unlike
                  ab
the Weyl case, H̃log is not K-invariant. Therefore,

                    ab      1
            ∇a ∇b H̃log = − R(K)ab c Kc H̃log
                                          ab
                            2
                          3
                        = ∇b Cabcd ∇a W cd + W −1 ∇a F cd − W −2 F cd ∇a W .
                                                                          
                                                                                    (4.12)
                          8
The above identity, along with the following relation

                                        ∇a ∇b C abcd = 0 ,                          (4.13)
                                          ∇[a Φbc] ij = 0 ,                         (4.14)

            a
implies ∇a Hlog = 0. In addition, we have checked explicitly the K-invariance of all the

                                                36
```

</details>

<a id="src-c24-p041"></a>

<details>
<summary>C24-p041 — PDF page 41: Main5.9: full component LOG BF density</summary>

[C24-p041: PDF page 41](https://arxiv.org/pdf/2311.00679v1#page=41) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
   Finally, in order to extract the K-connections, which encode the Ricci tensor contri-
butions, we degauge the action (5.6). Making use of (2.27) and (4.9), and setting W = 1,
the bosonic part of the Weyl-squared Lagrangian reads

          1                          1
LWeyl = − εabcde va Rbc ef Rdeef + εabcde va Φbc ij Φdeij
          8                          6
                          3                  1                                3
        −4Fab W D − Fab R Wcd − RFab W ab − Fab R[a c W b]c − Fab W ab W cd Wcd
                 ab              abcd
                          4                  8                              32
          9       ac        db   9 abcde               f   3 abcde                   128 2
        + Fab W Wcd W + ε                Fab Wcf Dd We + ε         Fab Wcf D f Wde −    D
          8                      8                         4                          3
                           2              1                1             1        3
        −8W ab Wab D + Φabij Φabij − Rabcd Rabcd + Rab Rab − R2 − Rabcd Wab Wcd
                           3              4                3            24        8
          81 ab          cd                c     bd    3      bd    a     3      ab
        − W Wbc W Wda + 3Wcd D Db W − Rab W W d + RW Wab
          32                                           2                 16
          33 ab            cd        3 a ce              3 a ce
        +     W Wab W Wcd − D W Dc Wae + D W Da Wce
          128                        2                   2
           9 abcde             f              ab    ij
        − ε        Wab Wcd D Wef + Xij W Φab .                                            (5.7)
          16
Note that we have also used
                                  1             2           2
                   Cabcd = Rabcd + ηc[a ηb]d R − ηc[a Rb]d + ηd[a Rb]c .                 (5.8)
                                  6             3           3
The action (5.7), up to a change of notations, coincides with the result of [37].

5.2    Log

   Making use of the BF action principle, eqs. (3.2a) and (3.2b), the primary superfield
 ij
Hlog can be used to define the following locally superconformal invariant in a standard
Weyl multiplet background
                     Z
                                   ij
              Slog = d5|8 z E Vij Hlog                                                  (5.9a)
                       Z       
                           5          a                    ij
                   = − d x e va Hlog    + W Flog + Xij Hlog     + 2λk ϕk log
                                                                           
                           a i             a    ij            ab        ij
                     −ψai Γ ϕlog W − iψai Γ λj Hlog + iψai Σ ψbj W Hlog .               (5.9b)

                                                                 ij
   As can be seen from the expressions of the descendants of Hlog   given in (4.8) and
the supplementary file for fermionic counterpart, the component form of (5.9b) is fairly

                                              40
```

</details>

<a id="src-c24-p081"></a>

<details>
<summary>C24-p081 — PDF page 81: AppendixA: conformal superspace derivative algebra</summary>

[C24-p081: PDF page 81](https://arxiv.org/pdf/2311.00679v1#page=81) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
A      Conformal superspace summary

   Here we collect results about conformal superspace in the traceless frame of [30] fo-
cusing on the ingredients relevant to our discussion in the paper. We adhere with the
notations and conventions of [30]. The reader should also look at [96], where some typos
from [30] were fixed.
   The Lorentz generators act on the superspace covariant derivatives ∇A = (∇a , ∇iα ) in
the following way

                                [Mab , Mcd ] = 2ηc[a Mb]d − 2ηd[a Mb]c ,                            (A.1a)
                                     [Mab , ∇c ] = 2ηc[a ∇b] ,                                      (A.1b)
                                 [Mαβ , ∇iγ ] = εγ(α ∇iβ) ,                                         (A.1c)

where Mαβ = 1/2(Σab )αβ Mab . The SU(2)R and dilatation generators satisfy

                      [J ij , J kl ] = εk(i J j)l + εl(i J j)k , [J ij , ∇kα ] = εk(i ∇j)
                                                                                       α            (A.1d)
                                                               1
                        [D, ∇a ] = ∇a , [D, ∇iα ] = ∇iα .                                           (A.1e)
                                                               2
The Lorentz and SU(2)R generators act on the special conformal generators KA = (Ka , Sαi )
according to the rules

                                                               i
          [Mab , Kc ] = 2ηc[a Kb] ,       [Mαβ , Sγi ] = εγ(α Sβ)     [J ij , Sαk ] = εk(i Sαj) ,   (A.1f)

while the dilatation generator acts on KA as

                                                                     1
                               [D, Ka ] = −Ka ,         [D, Sαi ] = − Sαi .                         (A.1g)
                                                                     2
The generators KA obey the only nontrivial anti-commutation relation

                                       {Sαi , Sβj } = −2i εij (Γc )αβ Kc .                          (A.1h)

The algebra of KA with ∇A is given by

     [Ka , ∇b ] = 2ηab D + 2Mab ,                                                                   (A.1i)
     [Ka , ∇iα ] = i(Γa )α β Sβi ,                                                                  (A.1j)
    {Sαi , ∇jβ } = 2εαβ δij D − 4δij Mαβ + 6εαβ Ji j ,                                              (A.1k)

                                                       80
```

</details>

<a id="src-c24-p082"></a>

<details>
<summary>C24-p082 — PDF page 82: AppendixA: conformal superspace derivative algebra</summary>

[C24-p082: PDF page 82](https://arxiv.org/pdf/2311.00679v1#page=82) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                  1                   i                    i
     [Sβi , ∇a ] = i(Γa )β α ∇αi − Wa b (Γb )β α Sαi + (Γa Γb )β γ Xγi Kb − Wabβi K b .   (A.1l)
                                  4                   8                    4

    The anticommutator of two spinor derivatives, {∇iα , ∇jβ }, has the following non-zero
torsion and curvatures

          Tαi jβ c = 2iεij (Γc )αβ ,                                                      (A.2a)
    R(M)iα jβ cd = 2iεij εαβ W cd + iεij (Γb )αβ W̃ bcd ,                                 (A.2b)
                   3i
    R(S)iα jβ γk = εij εαβ X γk + iεij δ[αγ
                                            Xβ] k
                                                  ,                                       (A.2c)
                   4
                      i                   i                    i
     R(K)iα jβ c = − εij εαβ ∇b Wb c + εij (Γa )αβ ∇d W̃da c − εij (Γc )αβ Y
                      2                   2                   32
                      i ij                    i                  3          
                   + ε εαβ W̃c de Wde + εij (Γa )αβ Wad W cd − W bd Wbd δa c .            (A.2d)
                      4                      2                   16

The non-vanishing torsion and curvatures in the spinor-vector commutator [∇b , ∇iα ] are:

                  1                                
       Tb iα γk = δki 3(Γb )α β Wβ γ − Wα β (Γb )β γ ,                                 (A.3a)
                  4
                     1
     R(D)b iα = − (Γb )α γ Xγi ,                                                      (A.3b)
                     4
                     3
    R(J)b iα jk = − (Γb )α γ εi(j Xγk) ,                                               (A.3c)
                     4
                                      1              1 [c
   R(M)b iα cd = −(Γb )α γ W cdiγ − εb cdef Wef iα + δb (Γd] )α γ Xγi ,               (A.3d)
                                      4              2
                   1
   R(S)b iα γj = Xcd ij (Σcd Γb − 2Γb Σcd )α γ
                  16
                     3i                        i
                  − εij ∇[b Wcd] (Σcd )α γ − εij ∇d W dc (Σcb )α γ
                      8                       8
                     3i ij d               i
                  + ε ∇ Wdb δαγ − εij ∇c W̃cb d (Γd )α γ
                     16                    8
                      i ij cde                   3i
                  + ε W̃ Wde (Σcb )α γ − εij W̃bde W de δα γ
                     16                          32
                     i ij                    3i
                  + ε Wbd W cd (Γc )α γ − εij W cd Wcd (Γb )α γ ,                      (A.3e)
                     4                       64
                  1                       1                  1            1
    R(K)b iα c = (Γc )α β ∇d Wdb iβ + (Γb )α β ∇d W d ciβ + ∇α β Wb ciβ − εb cdef ∇d Wef iα
                  6                      12                  6           24
                     1 c β                1
                  + (Γ )α ∇b Xβi + W de (3Γb Σde Γc − Σde Γb Γc )α β Xβi
                     8                   64
                      1                      1
                  − W̃bde (Γc )α β W deiβ + δb c W de Wde iα
                     48                      8
                      1                       1
                  + (Σb c )α β Wde iβ W de − W de (Σde )α β Wb c β i
                     12                      12

                                               81
```

</details>

<a id="src-c24-p083"></a>

<details>
<summary>C24-p083 — PDF page 83: AppendixA: conformal superspace derivative algebra</summary>

[C24-p083: PDF page 83](https://arxiv.org/pdf/2311.00679v1#page=83) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                       13             11            13
                   +      Wbd W dciα + Wbd iα W dc − (Γb )α β Wde iβ W̃ dec .                     (A.3f)
                       48             48            96
The commutator of two vector derivatives [∇a , ∇b ] has the following non-zero torsion and
curvatures:
                           i
                Tab αi = − Wab αi ,                                                               (A.4a)
                           2
                           3i
             R(J)ab = − Xab ij ,
                   ij
                                                                                                  (A.4b)
                           4
                   cd      1      αβ    cd γδ
                                                             
            R(M)ab = − (Σab ) (Σ ) iWαβγδ + 3W(αβ Wγδ) ,                                          (A.4c)
                           4
                           1 β              1
             R(S)ab α = − ∇α Wabβ i − (Γ[a )α β ∇c Wb]cβ i
                    i
                           2                2
                           1                 1                3
                         − Wα Wabβ + (Σab )α β W cdWcdβ i + W c [a Wb]cα i ,
                              β        i
                                                                                                  (A.4d)
                           8                16                8
                         1                    i           j i
             R(K)ab c = ∇d R(M)ab cd − Wab αj (Γc )α β Xβ − Wd[a αj (Γb] )α β Wβcd j
                         4                   16             8
                           i
                         + Wad αi (Γc )α β Wb d β i .                                             (A.4e)
                           8

B      Building blocks
                                  a
    The following is the bosonic Hlog expression obtained from Cadabra:

       3               3              149                            25
 a
Hlog = 32 W a b ∇b Y + 32 Y ∇b W ab + 256 εe1 debc Wbc ∇e1 ∇a Wde − 512 εe1 debc Wbc ∇a ∇e1 Wde +
4203                            133 a                          43 a
     ε
8192 bce1 de
             ∇a W bc ∇e1 W de + 256 ε e1 dbc Wbc ∇e1 ∇e Wde + 256 ε e1 deb Wbc ∇c ∇e1 Wde −
 73
    ε cdb Wb a ∇e ∇e1 Wcd − 273
128 ee1                     512
                                                          33 a
                                εadebc Wbc ∇e1 ∇e1 Wde − 128 ε ee1 d b Wbc ∇e ∇e1 W dc −
31 a                          85 a                         81
64
   ε e1 deb Wbc ∇e1 ∇c Wde + 128 ε e1 dbc Wbc ∇e ∇e1 Wde + 256 εee1d bc Wbc ∇e ∇e1 W ad +
5211 a                          99
4096
     ε e1 bcd ∇e1 Wbc ∇e Wde − 2048 εebe1cd ∇e W ab ∇e1 W cd − 4203
                                                               8192
                                                                    εabcde ∇e1 Wbc ∇e1 Wde −
1329 a                          99 a b                         3
4096
     ε e1 bde ∇e1 Wbc ∇c Wde − 1024 ε e e1 d ∇e Wbc ∇e1 W dc − 32 F a b W −1 ∇b Y −
 3
32
   Y W −1 ∇b F ab + 137                               25
                        ε debc Fbc W −1 ∇e1 ∇a Wde − 512
                    256 e1
                                                         εe1 debc Fbc W −1 ∇a ∇e1 Wde −
 89 a                              249 adebc                         15
256
    ε e1 deb Fbc W −1 ∇c ∇e1 Wde − 512 ε     Fbc W −1 ∇e1 ∇e1 Wde − 256 εee1d bc Fbc W −1 ∇e ∇e1 W ad +
1 a                               61 a                               7
8
  ε e1 deb Fbc W −1 ∇e1 ∇c Wde + 256 ε e1 dbc Fbc W −1 ∇e1 ∇e Wde − 128 εee1 cdb Fb a W −1 ∇e ∇e1 Wcd +
 37 a                               3 a
128
    ε e1 dbc Fbc W −1 ∇e ∇e1 Wde + 128 ε ee1 d b Fbc W −1 ∇e ∇e1 W dc − 13
                                                                        32
                                                                           εa e1 bcd Wde W −1 ∇e1 ∇e Fbc −

                                                   82
```

</details>

<a id="src-c24-p090"></a>

<details>
<summary>C24-p090 — PDF page 90: AppendixC: convention bridge and Tables4–6</summary>

[C24-p090: PDF page 90](https://arxiv.org/pdf/2311.00679v1#page=90) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                        19                    33                   221
       +εabcde     −       Fee4 ∇b W ∇e4 Wcd + Fde ∇e4 W ∇e4 Wbc −     Fee ∇e4 W ∇b Wcd
                       512                    64                   512 4
                                                                                            !
                       5                 5                    83
                   + Fde ∇e4 W ∇b Wce4 − Fde ∇b W ∇e4 Wce4 −     Fee ∇b W ∇c Wd e4
                       32                8                   256 4
                                                                        !
        abcde   3           e4    3      e4           3          e4
     =ε       (− Fee4 ∇b W ∇ Wcd − Fee4 ∇ W ∇b Wcd − Fde ∇b W ∇ Wce4 ,
                4                 4                   2
                                                                                            (B.1j)
                 11                     153                      19
(11) = εabcde       Wee4 ∇b W ∇e4 Fcd +     Wde ∇e4 W ∇e4 Fbc −     Wee4 ∇e4 W ∇b Fcd
                 32                     256                     128
                                                                                        !
                 37                       61                     9
                  − Wde ∇e4 W ∇b Fce4 −       Wde ∇b W ∇e4 Fce4 + Wee4 ∇b W ∇c Fd e4
                 64                      128                     64
                                                               !
                  81                       25
       +εbcdef −     Wef ∇b W ∇c F a d −      Wef ∇b W ∇a Fcd
                 128                      128
                                                                            !
               3                      3                      3
     = εabcde − Wee4 ∇b W ∇e4 Fcd + Wde ∇e4 W ∇e4 Fbc − Wde ∇b W ∇e4 Fce4 .
               4                      8                      2
                                                                                            (B.1k)

C     Different 5D N = 1 notation and conventions

    Table 4 provides a brief translation scheme between our conventions and other groups
[81, 83, 97] that worked on the superconformal tensor calculus in five dimensions.
    It is important to note that the definitions of supersymmetry are different between
the various groups. Here the differences amount to not only to normalisations, but also
to additional field-dependent S and K transformations in the definition of δQ . That is,
given a transformation δQ + δS + δK in our conventions with respective parameters ξαi , ηαi ,
                                         ′
and ΛaK , we will find a transformation δQ + δS′ + δK
                                                    ′
                                                      with new parameters εi , η ′i , and Λ′a
                                                                                           K
given in Table 5.
    We also emphasise that each group uses the same vector derivative Da , corresponding
to our ∇a , modulo differing overall normalisations of the superconformal generators. The
additional gravitino-dependent terms in the S-supersymmetry and special conformal con-
nections in Table 4 cancel against additional terms found within δQ , so that the vector
derivative is unchanged.

                                              89
```

</details>

<a id="src-c24-p091"></a>

<details>
<summary>C24-p091 — PDF page 91: AppendixC: convention bridge and Tables4–6</summary>

[C24-p091: PDF page 91](https://arxiv.org/pdf/2311.00679v1#page=91) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
Our conventions      de Wit and Katmadas                       Bergshoeff et al.                          Fujita et al.

       η ab                        η ab                                  η ab                                 −η ab
       Γa                         −iγ a                                  iγ a                                  γa
                                                                        1 ab
       Σab                         1 ab
                                   2
                                     γ                                  2
                                                                          γ                                  − 21 γ ab
     εabcde                     −iε   abcde
                                                                       −ε abcde
                                                                                                             εabcde

      ψm i                         ψµ i                                  ψµ i                                 2 ψµ i
      Vm i j                     − 21 Vµj i                            −Vµ i j                                Vµ i j
      ωm ab                        ωµ ab                               −ωµ ab                                −ωµ ab
      i φm i                       φµ i                       −φµ i + 31 Tab γ ab ψµ i               2 φµ i − 23 vab γ ab ψµ i
      fm a              −fµ a + 31 ψµi γ a χi                  −fµ a + 13 ψµ i γ a χi                −fµ a + 24i ψµ i γ a χi
                                                                        16 ab                               4 ab
       w ab                      −4T ab                                  3
                                                                           T                                3
                                                                                                              v
                                                                                                            1 i
       χi                           χi                                   χ  i
                                                                                                            32
                                                                                                               χ
                                                                                                       1
       D                            D                                    D                            16
                                                                                                         (D − 83 v ab vab )
                                1                                  1
    R(Q)ab i                    2
                                  R(Q)ab i                         2
                                                                     R(Q)ab i                               R(Q)ab i
   R(M)ab cd                    R(M)ab cd                         −R(M)ab cd                              −R(M)ab cd
    R(J)ab i j             − 12 R(V)abj i                            −R(V )ab i j                          R(U)ab i j
   i R(S)ab i             1
                          2
                            R(S)ab i                    − 12 R(S)ab i + 16 Tcd γ cd R(Q)ab i    R(S)ab i − 31 vcd γ cd R(Q)ab i
    R(K)ab c       −R(K)ab c + 13 R(Q)abi γ c χi          −R(K)ab c + 31 R(Q)ab i γ c χi       −R(K)ab c + 24i R(Q)ab i γ c χi

                                 Table 4: Conventions for Weyl multiplet

         de Wit and Katmadas                      Bergshoeff et al.                       Fujita et al.

                  εi = 2 ξ i                            εi = 2 ξ i                             εi = ξ i
                 η ′i = 2iη i                 η ′i = −2iη i + 23 Tab γ ab ξ i        η ′i = iη i + 31 vab γ ab ξ i
                     2                                   2 i a                                  i i a
          Λ′a    a         a i
           K = −ΛK + 3 ξi γ χ                 Λ′a    a
                                               K = −ΛK + 3 ξ γ χi                   Λ′a    a
                                                                                     K = −ΛK + 24 ξ γ χi

                                  Table 5: Conventions for δQ + δS + δK

   For completeness, we also give in Table 6 the relation between our conventions for the
vector multiplet and the other groups.

References
[1] D. Z. Freedman, P. van Nieuwenhuizen and S. Ferrara, “Progress toward a theory of supergravity,”
    Phys. Rev. D 13, 3214 (1976).

                                                            90
```

</details>

<a id="src-c24-p092"></a>

<details>
<summary>C24-p092 — PDF page 92: AppendixC: convention bridge and Tables4–6</summary>

[C24-p092: PDF page 92](https://arxiv.org/pdf/2311.00679v1#page=92) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
        Our conventions        de Wit and Katmadas Bergshoeff et al. Fujita et al.

                 W                          σ                         σ                   M
                 λi                        Ωi                        −ψ i               −2Ωi
                X ij                      2Y ij                     2Y ij               2Y ij

                            Table 6: Conventions for vector multiplet

 [2] S. Deser and B. Zumino, “Consistent supergravity,” Phys. Lett. B 62, 335 (1976).

 [3] P. K. Townsend, “Cosmological constant in supergravity,” Phys. Rev. D 15, 2802 (1977).

 [4] P. Breitenlohner, “A geometric interpretation of local supersymmetry,” Phys. Lett. B 67, 49 (1977):
     “Some invariant Lagrangians for local supersymmetry,” Nucl. Phys. B124, 500 (1977).

 [5] W. Siegel, “The superfield supergravity action,” Harvard preprint HUTP-77/A080 (Dec., 1977).

 [6] W. Siegel and S. J. Gates Jr. “Superfield supergravity,” Nucl. Phys. B 147, 77 (1979).

 [7] W. Siegel, “A polynomial action for a massive, self-interacting chiral superfield coupled to super-
     gravity,” Harvard preprint HUTP-77/A077 (Dec., 1977).

 [8] J. Wess and B. Zumino, “Superfield Lagrangian for supergravity,” Phys. Lett. B 74, 51 (1978).

 [9] K. S. Stelle and P. C. West, “Minimal auxiliary fields for supergravity,” Phys. Lett. B 74, 330 (1978).

[10] S. Ferrara and P. van Nieuwenhuizen, “The auxiliary fields of supergravity,” Phys. Lett. B 74, 333
     (1978).

[11] M. F. Sohnius and P. C. West, “An alternative minimal off-shell version of N=1 supergravity,” Phys.
     Lett. B 105, 353 (1981).

[12] M. Sohnius and P. C. West, “The tensor calculus and matter coupling of the alternative minimal
     auxiliary field formulation of N = 1 supergravity,” Nucl. Phys. B 198, 493 (1982).

[13] S. J. Gates, M. T. Grisaru, M. Rocek and W. Siegel, “Superspace Or One Thousand and One Lessons
     in Supersymmetry,” Front. Phys. 58, 1-548 (1983) [arXiv:hep-th/0108200 [hep-th]].

[14] J. Wess and J. Bagger, Supersymmetry and Supergravity, Princeton University Press, Princeton,
     1992.

[15] I. Buchbinder and S. M. Kuzenko. Ideas and methods of supersymmetry and supergravity: Or a walk
     through superspace, IOP, Bristol (1998).

[16] D. Z. Freedman and A. Van Proeyen, Supergravity, Cambridge Univ. Press, 2012.

[17] S. M. Kuzenko, E. S. N. Raptakis and G. Tartaglino-Mazzucchelli, “Superspace approaches to N = 1
     supergravity,” [arXiv:2210.17088 [hep-th]].

[18] S. Sethi, “Supersymmetry Breaking by Fluxes,” JHEP 10 (2018), 022 [arXiv:1709.03554 [hep-th]].

                                                    91
```

</details>

<a id="src-c24-p103"></a>

<details>
<summary>C24-p103 — PDF page 103: Supplement1: raw index conventions and X/Y component projections</summary>

[C24-p103: PDF page 103](https://arxiv.org/pdf/2311.00679v1#page=103) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
computed directly by Cadabra including all bosonic and fermionic contributions. The
only exceptions where we present only the bosonic contribution are the four (fermionic)
derivative supercurrent descendants of sections 4.2.5, 4.3.5, and 4.4.5 as well as the BF
action for the log invariant given in 3.1 in which we have written the superconformally
covariant vector derivative ∇a in terms of thee degauged covariant derivative Da , gauged
fixed W = 1, and removed fermions.
   Due to the computational source of these results, a unique symmetric and antisym-
metric index notation is used denoted by underlining and hatting indices, respectively.
For example

                                              1         1
                        λαi λβj := λα(i λβj) = λαi λβj + λαj λβi ,                      (1.1a)
                                              2         2
                                                  1             1
                      Wcâ Wb̂d := Wc[a Wb]d = Wca Wbd − Wcb Wad .                      (1.1b)
                                                  2             2
These are employed only when a field has explicit symmetric or antisymmetric indices by
construction. Note also that two descendants of the super-Weyl tensor Wαβ = 12 (Σab )αβ Wab
are written here in their form prior to component projection being Y and Xαi . These pro-
jections are trivial however.

                                            3i i
                                      χiα :=   X |,                                     (1.2a)
                                            32 α
                                               3
                                       D := −     Y| .                                  (1.2b)
                                              128

Also recall Φab ij = − 3i4 Xab ij . These redefinitions and projections should be applied de-
pending on the context of the results (either looking at genuine superfield dependants
or at component results). We trust the reader will have enough information to decide
depending on the context and their need. Also keep in mind the difference in notation
between this file and the main paper of the Riemann tensor and its contractions (R → R)
as well as the composite connection (f → f).
    Each subsection of this document is titled after a single field or object, and the contents
therein include its component structure. Be aware that in most cases the bosonic parts
of the results are larger than and may not appear at a glance to match those of the main
paper [1]. This is because there are various simplifications (e.g., algebraic manipulations,
sometimes integration by parts) that are performed by hand on the results given in [1].
   This file is organised as follows. In sections 2.1 and 2.2, we give results for the descen-
                                                 ij         ij
dants of the composite primary superfields, HWeyl     and Hlog W , respectively, both of which

                                               4
```

</details>

<a id="src-c24-p106"></a>

<details>
<summary>C24-p106 — PDF page 106: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p106: PDF page 106](https://arxiv.org/pdf/2311.00679v1#page=106) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2.2     Log

2.2.1    ϕiα log

   3           3
− 512 Y Xαj − 16 Wαβ ∇βρ Xρj − 83 Xρj ∇ρβ Wαβ − 34 W β ρ ∇ρλ Wαβλ j − 83 Fαβ W −1 ∇βρ Xρj −

 X W −1∇ρβ Fαβ − 21 Φα βj i Xβi − 32
3 j
4 ρ
                                   3               15
                                     ∇βρ ∇βρ Xαj + 16 W β ρ ∇α ρ Xβj − 27
                                                                       16
                                                                          X jβ ∇α ρ Wβρ −
3 β
4
  F ρ W −1 ∇ρλ Wαβλ j + 27
                        32
                           Wαβ Xρj W −1 ∇βρ W − 27
                                                32
                                                   Wα β Wβ ρ Xρj − 285
                                                                   256
                                                                       W βρWβρ Xαj −
1
2
  iΦαβ j i W −1 ∇βρ λiρ + 91 iλiρ W −1 ∇ρβ Φαβ ji + 32
                                                     3
                                                       iY W −1 ∇α β λjβ + 64
                                                                           3
                                                                             iλjβ W −1 ∇α β Y −
 3
64
   iFα β Y λjβ W −2 + 64
                       3
                         iX j i Y λiα W −2+ 83 F β ρ W −1 ∇α ρ Xβj + 34 W βρ ∇α λ Wβρλ j −
3                      3
  F β Fβ ρ Xρj W −2 − 16
4 α
                         F βρ Fβρ Xαj W −2 − 27
                                             16
                                                Wα β Fβ ρ Xρj W −1 + 27
                                                                     16
                                                                        W βρ Fαβ Xρj W −1 −
27
16
   W βρ Fβρ Xαj W −1 − 21 Wα β W ρλ Wβρλ j + 38 Xiβ W −1 ∇α β X ji − 34 X j i W −1 ∇α β Xβi +
3 j
8
                       9
  X i Fα β Xβi W −2 + 16 λiα X jβ Xβi W −1 − 43 λβi Xαj Xβi W −1 + 38 λβi Xβj Xαi W −1 +
 3 jβ
16
                    3
   λ Xiα Xβi W −1+ 32 Xik X ik Xαj W −2 + 34 iWβρ W −1 ∇α β ∇ρλ λjλ + 19 iλj W −1 ∇λβ ∇α ρ Wβρ +
                                                                      32 λ

 5
   iλj W −1 ∇α β ∇λρ Wβρ + 63
32 λ                       64
                              iW −1 ∇α β Wβρ ∇ρλ λjλ − 64
                                                       15
                                                          iW −1 ∇βλ Wβρ ∇α ρ λjλ −
1                          3                            1
4
  iWαβ W −1 ∇λ β ∇λρ λjρ + 32 iλjα W −1 ∇λ β ∇λρ Wβρ + 16 iλjρ W −1 ∇λ β ∇λρ Wαβ +
 3
   iλj W −1 ∇λ ρ ∇λβ Wαβ + 15
32 ρ                       64
                                                        3
                              iW −1 ∇λ β Wαβ ∇λρ λjρ − 32 iW −1 ∇λ ρ Wαβ ∇λβ λjρ −
 9
64
   iW −1 ∇λ β Wβρ ∇λρ λjα − 12 iFαβ F ρ λ W −3 ∇βλ λjρ + 21 iFαβ λjρ W −3 ∇βλ Fρλ +
3
8
  iFαβ λjρ W −2∇βλ Wρλ − 21 iFα β λjλ W −3 ∇λρ Fβρ − 13
                                                     16
                                                        iFα β λjλ W −2 ∇λρ Wβρ +
 1
16
   iF β ρ λjα W −2 ∇ρλ Wβλ − 21 iF β ρ λjλ W −3 ∇ρλ Fαβ − 16
                                                           7
                                                             iF β ρ λjλ W −2 ∇ρλ Wαβ −
3
8
  iWαλ F β ρ W −2 ∇λρ λjβ − 98 iWαβ W ρ λ W −1 ∇βλ λjρ + 41 iWαλ λjβ W −2 ∇λρ Fβρ +
 9
16
                           9
   iWαβ λjρ W −1 ∇βλ Wρλ + 16 iWα β Wβρ W −1 ∇ρλ λjλ − 12 iWα β λjλ W −2 ∇λρ Fβρ +
23
64
   iWα β λjλ W −1 ∇λρ Wβρ + 38 iW ρ λ Fαβ W −2 ∇λβ λjρ + 83 iW β ρ Fαβ W −2 ∇ρλ λjλ −
 9
32
   iW β ρ Wβλ W −1 ∇ρλ λjα − 59
                             64
                                iW β ρ λjα W −1 ∇ρλ Wβλ − 38 iW β ρ λjλ W −2 ∇ρλ Fαβ +
23
64
   iW β ρ λjλ W −1∇ρλ Wαβ − 38 iW ρ λ λjρ W −2 ∇λβ Fαβ + 16
                                                          9
                                                            iW β ρ λjβ W −1 ∇ρλ Wαλ −
 3
64
   iY λjβ W −2 ∇α β W − 14 iFαβ λiρ W −3 ∇βρ X ji − 16
                                                     3
                                                       iWαβ λiρ W −2 ∇βρ X ji + 14 iX j i Fαβ W −3 ∇βρ λiρ +
3
8
  iX j i Wαβ W −2 ∇βρ λiρ + 16 iX j i λiρ W −3 ∇ρβ Fαβ + 16
                                                          3
                                                            iX j i λiρ W −2 ∇ρβ Wαβ +

                                                     7
```

</details>

<a id="src-c24-p107"></a>

<details>
<summary>C24-p107 — PDF page 107: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p107: PDF page 107](https://arxiv.org/pdf/2311.00679v1#page=107) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3
   iλ X j W −2 ∇βρ λiρ + 32
16 iα β
                         5
                            iλiα Xβi W −2 ∇βρ λjρ − 18 iλiα λiρ W −2 ∇ρβ Xβj − 32
                                                                                5
                                                                                  iλiβ Xαj W −2 ∇βρ λiρ −
 1                       1
   iλ X i W −2 ∇ρβ λjα + 32
32 iρ β
                                                     1
                            iλjα Xiβ W −2 ∇βρ λiρ − 16                          1
                                                       iλjα λiρ W −2 ∇ρβ Xβi − 16 iλjβ Xiα W −2 ∇βρ λiρ +
 1                      3
   iλj X W −2 ∇ρβ λiα + 16
32 ρ iβ
                           iλjρ λiα W −2 ∇ρβ Xβi − 18 iλjβ λiρ W −2 ∇βρ Xαi − 83 Xβj W −1 ∇ρ β ∇α ρ W −
3
8
  W −1 ∇αρ W ∇ρβ Xβj − 32
                        3
                          W −1 ∇βρ W ∇βρ Xαj − 83 F β ρ Xβj W −2 ∇α ρ W + 27
                                                                          32
                                                                             W β ρ Xβj W −1 ∇α ρ W +

  F W −1 ∇α λ Wβρλ j − 12 Fα β F ρλ Wβρλ j W −2 − 21 iCα βρλ Fβρ λjλ W −2 + 94 iWα β W ρλ Fβρ λjλ W −2 −
3 βρ
4

9
4
  iWα λ W βρ Fβρ λjλ W −2 − 18 Wα λ F βρ Wλβρ j W −1 − 87 W ρλ Fα β Wρλβ j W −1 +
9
8
  W βλ Fβ ρ Wαλρ j W −1 − 12 iCα βρλ Wβρ λjλ W −1 − 16
                                                    81
                                                       iWα β Wβ ρ Wρ λ λjλ W −1 −
81
32
   iWα β W ρλ Wρλ λjβ W −1 + 12 iΦβ ρj i W −1 ∇β α λiρ − 91 iλρi W −1 ∇α β Φβρ ji + 38 X j i Xβi W −2 ∇α β W +
1
2
  iΦβρj i Fβρ λiα W −2 − 41 iΦβρj i Wαβ λiρ W −1 + 34 iΦα βj i Wβ ρ λiρ W −1 + 34 iΦβρj i Wβρ λiα W −1 +
1 j                                                   1 β iρ                1 jβ ρ
4
  X i F βρ Wαβρ i W −2 + 14 X j i W βρ Wαβρ i W −1 − 12 λi X Wαβρ j W −1 + 12 λ Xi Wαβρ i W −1 −
 3
128
    Y λjβ λiα λiβ W −3 + 41 iFβρ λjλ W −3 ∇βλ ∇α ρ W + 16
                                                        3
                                                          iWβρ λjλ W −2 ∇βλ ∇α ρ W −
3
8
  iWβρ λjλ W −2 ∇α β ∇ρλ W − 16
                              9
                                iWβρ W −2 ∇α β W ∇ρλ λjλ − 16
                                                            3
                                                              iWβρ W −2 ∇βλ W ∇α ρ λjλ −
1 j                       49
 iλ W −3∇α β W ∇λρ Fβρ − 128
4 λ
                             iλjλ W −2 ∇α β W ∇λρ Wβρ + 128
                                                        25
                                                            iλjλ W −2 ∇λβ W ∇α ρ Wβρ −
1
8
  iFαβ W −3 ∇λ β W ∇λρ λjρ − 81 iFαβ W −3 ∇λ ρ W ∇λβ λjρ + 81 iWαβ λjρ W −2 ∇λ β ∇λρ W −
                               1
 3
16
   iWαβ W −2 ∇λ ρ W ∇λβ λjρ + 128 iλjα W −2 ∇λ β W ∇λρ Wβρ + 18 iλjρ W −3 ∇λ ρ W ∇λβ Fαβ +
1 j                       15                             1
 iλ W −3∇λ β W ∇λρ Fαβ + 128
8 ρ
                             iλjρ W −2 ∇λ ρ W ∇λβ Wαβ + 16 iλjρ W −2 ∇λ β W ∇λρ Wαβ +
3
4
  iFαβ F ρ λ λjρ W −4 ∇βλ W − 43 iFα β Fβρ λjλ W −4 ∇ρλ W + 34 iWαλ F β ρ λjβ W −3 ∇λρ W +
 9
16
                               3
   iWαβ W ρ λ λjρ W −2 ∇βλ W − 16 iWα β Fβρ λjλ W −3 ∇ρλ W + 16
                                                             9
                                                                iWα β Wβρ λjλ W −2 ∇ρλ W −
 3
16
   iW β ρ Fαβ λjλ W −3 ∇ρλ W + 16
                               9                              27
                                  iW β λ Fβρ λjα W −3 ∇λρ W + 64 iW β ρ Wβλ λjα W −2 ∇ρλ W −
 1
   iλβ Wαβρ j W −2 ∇ρλ λiλ + 12
12 i
                              1
                                iλβi Wαβρ i W −2 ∇ρλ λjλ + 24
                                                           1
                                                              iλjλ λβi W −2 ∇λρ Wαβρ i −
1 jβ                       1
6
  iλ Wαβρi W −2 ∇ρλ λiλ − 24 iλjβ λiλ W −2 ∇λρ Wαβρ i − 83 iX j i Fαβ λiρ W −4 ∇βρ W −
 9
16
                               1
   iX j i Wαβ λiρ W −3 ∇βρ W + 32 iλiα λiρ Xβj W −3 ∇ρβ W − 11 iλj λ X i W −3 ∇ρβ W −
                                                            96 α iρ β

 1                        1
   iλj λ X i W −3 ∇ρβ W + 24
96 ρ iα β
                             iλjβ λiρ Xαi W −3 ∇βρ W + 64
                                                       3
                                                          Xαj W −2 ∇βρ W ∇βρ W −

  F Wβρλ j W −2 ∇α λ W − 14 W βρ Wβρλ j W −1 ∇α λ W + 24
1 βρ
4
                                                      1
                                                         λiβ W −3 ∇α β λjρ ∇ρλ λiλ −
 7                            1                             1 j
   λ W −3 ∇α ρ λjρ ∇βλ λiλ − 24
24 iβ
                                λiβ W −3 ∇βλ λjρ ∇α ρ λiλ + 24 λβ λiρ W −3 ∇ρλ ∇α β λiλ +

                                                       8
```

</details>

<a id="src-c24-p108"></a>

<details>
<summary>C24-p108 — PDF page 108: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p108: PDF page 108](https://arxiv.org/pdf/2311.00679v1#page=108) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1 j                      1 j                            1 j
  λ λ W −3 ∇α β ∇ρλ λiλ + 24
24 β iρ
                             λβ W −3 ∇α β λiρ ∇ρλ λiλ − 24 λβ λiρ W −3 ∇βλ ∇α ρ λiλ −
 1 j
  λ λ W −3 ∇α ρ ∇βλ λiλ − 16 λjβ λiρ W −3 ∇βρ ∇α λ λiλ − 16 λjβ W −3 ∇α ρ λiρ ∇βλ λiλ −
24 β iρ

 1 j                        1                               1
  λ W −3 ∇α λ λiρ ∇βρ λiλ + 24
24 β
                               λiβ W −3 ∇λ β λjα ∇λρ λiρ − 48 λiβ W −3 ∇λ β λjρ ∇λρ λiα −
 1                            1 j                          1 j
   λ W −3 ∇λ ρ λjρ ∇λβ λiα − 24
48 iβ
                                λα λiβ W −3 ∇λ β ∇λρ λiρ + 24 λβ λiα W −3 ∇λ β ∇λρ λiρ +
 1 j                         1 j
  λ W −3 ∇λ β λiα ∇λρ λiρ + 48
16 β
                               λβ W −3 ∇λ ρ λiα ∇λβ λiρ − 83 Fαβ λjρ λλi W −4 ∇βρ λiλ −
3
  F λjρλiλ W −4 ∇βλ λiρ − 38 Fαβ λjρλiρ W −4 ∇βλ λiλ + 81 Fα β λjρ λiλ W −4 ∇ρλ λiβ +
8 αβ

1
  F β λjρ λiβ W −4 ∇ρλ λiλ − 21 Fα β λjβ λiρ W −4 ∇ρλ λiλ − 14 F β ρ λiα λiλ W −4 ∇ρλ λjβ −
2 α

  F ρ λjα λiβ W −4 ∇ρλ λiλ + 14 F β ρ λjλ λiα W −4 ∇ρλ λiβ + 18 F β ρ λjλ λiβ W −4 ∇ρλ λiα +
1 β
8

  F ρ λjβ λiα W −4 ∇ρλ λiλ − 18 F β ρ λjβ λiλ W −4 ∇ρλ λiα − 35
1 β
8                                                            96
                                                                Wαβ λjρ λλi W −3 ∇βρ λiλ −
37
96
   Wαβ λjρ λiλ W −3 ∇βλ λiρ − 35
                              96
                                                             1
                                 Wαβ λjρ λiρ W −3 ∇βλ λiλ − 96 Wα β λiβ λiρ W −3 ∇ρλ λjλ +
 1
96
                               7
   Wα β λjρ λiλ W −3 ∇ρλ λiβ + 24                              7
                                  Wα β λjρ λiβ W −3 ∇ρλ λiλ − 32 Wα β λjβ λiρ W −3 ∇ρλ λiλ −
1
4
  W β ρ λiα λiλ W −3 ∇ρλ λjβ − 32
                                3
                                  W β ρ λiα λiβ W −3 ∇ρλ λjλ + 32
                                                               3
                                                                  W β ρ λiβ λiλ W −3 ∇ρλ λjα +
1
8
                                1
  W β ρ λjα λiλ W −3 ∇ρλ λiβ − 32 W β ρ λjα λiβ W −3 ∇ρλ λiλ + 18 W β ρ λjλ λiα W −3 ∇ρλ λiβ +
 1
32
   W β ρ λjλ λiβ W −3∇ρλ λiα + 18 W β ρ λjβ λiα W −3 ∇ρλ λiλ − 81 W β ρ λjβ λiλ W −3 ∇ρλ λiα −
 1 j β i
  λ λ λ W −3 ∇λρ Wβρ + 14 λjλ λiα λiβ W −4 ∇λρ Fβρ + 32
32 α i λ
                                                     9 j
                                                        λλ λiα λiβ W −3 ∇λρ Wβρ −
1 j β i               5 j β i
 λ λ λ W −4 ∇ρλ Fαβ − 32
4 ρ i λ
                         λρ λi λλ W −3 ∇ρλ Wαβ − 14 λjβ λiα λiλ W −4 ∇λρ Fβρ −
1 jβ
4
                            5
  λ λiα λiλ W −3 ∇λρ Wβρ + 64 Xik λjα λiβ W −4 ∇βρ λkρ − 13 X λj λi W −4 ∇βρ λkρ +
                                                         64 ik β α

 9
   X λj λi W −4 ∇βρ λkα + 64
64 ik β ρ
                          21 j                           1
                             X i λiα λkβ W −4 ∇βρ λkρ + 64 X j i λiβ λkρ W −4 ∇βρ λkα +
 5
64
   X j i λkαλiβ W −4 ∇βρ λkρ + 18 λkα λkβ λiρ W −4 ∇βρ X ji + 64
                                                               3 j
                                                                 λα λiβ λkρ W −4 ∇βρ X ik −
 3 j
  λ λ λ W −4 ∇βρ X ik + 81 iW −1 ∇ρλ ∇ρλ ∇α β λjβ − 38 iFβρ λjλ W −4 ∇α β W ∇ρλ W +
32 β iα kρ

 9
16
   iWβρ λjλ W −3 ∇α β W ∇ρλ W + 16
                                1                             1
                                   iλjβ W −1 ∇λ ρ ∇α λ Wβρ + 32 iλjβ W −1 ∇αλ ∇λρ Wβρ +
 3
32
   iW −1 ∇αλ W β ρ ∇λρ λjβ + 64
                              3
                                iW −1 ∇λ ρ W β ρ ∇α λ λjβ − 32
                                                             3
                                                               iWαβ λjρ W −3 ∇λ β W ∇λρ W −
1
8
  iFα β W −2 ∇ρλ ∇ρλ λjβ − 16
                           1
                              iWα β W −1 ∇ρλ ∇ρλ λjβ + 18 iλjβ W −2 ∇ρλ ∇ρλ Fαβ −
1
8
  iW −2 ∇ρλ Fα β ∇ρλ λjβ + 32
                           3
                              iW −1 ∇ρλ Wα β ∇ρλ λjβ − 16
                                                        5
                                                          iF β ρ λjλ W −2 ∇α ρ Wβλ +
1
4
  iF βρ Fβρ W −3 ∇α λ λjλ − 16
                             1
                               iF βρ λjλ W −2 ∇α λ Wβρ − 16
                                                         17
                                                            iF βρ λjβ W −2 ∇α λ Wρλ +

                                                       9
```

</details>

<a id="src-c24-p109"></a>

<details>
<summary>C24-p109 — PDF page 109: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p109: PDF page 109](https://arxiv.org/pdf/2311.00679v1#page=109) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                              9
3
8
  iW β λ Fβ ρ W −2 ∇α λ λjρ + 16 iW βρ Wβλ W −1 ∇α λ λjρ − 34 iW β λ λjρW −2 ∇α λ Fβρ −
23
64
   iW β ρ λjλ W −1 ∇α ρ Wβλ − 15
                              32
                                 iW βρ Wβρ W −1 ∇α λ λjλ + 11
                                                           64
                                                              iW βρ λjλ W −1 ∇α λ Wβρ −
23
64
   iW βρ λjβ W −1 ∇α λ Wρλ − 32 iFα β Fβ ρ Fρ λ λjλ W −4 − 43 iFα β F ρλ Fρλ λjβ W −4 −
3
2
  iWα β Fβ ρ Fρ λ λjλ W −3 − 83 iWα λ F βρ Fβρ λjλ W −3 − 27
                                                          16
                                                             iWα λ Wλ β Fβ ρ λjρ W −2 +
9
4
  iW βρ Fαβ Fρ λ λjλ W −3 − 23 iW ρλ Fα β Fρλ λjβ W −3 + 23 iW ρλ Fα β Fρβ λjλ W −3 −
15
32
   iW ρλ Wρλ Fα β λjβ W −2 + 27
                             16
                                iW ρβ Wρ λ Fαβ λjλ W −2 − 18 iX j i X i k X k l λlα W −4 −
 5                            1                            1
32
   iX j i Xkl X kl λiα W −4 + 16 iX j i W −2 ∇βρ ∇βρ λiα − 16 iλiα W −2 ∇βρ ∇βρ X ji +
 1                           3
16
   iW −2 ∇βρ X j i ∇βρ λiα + 16 iW β ρ λiβ W −2 ∇α ρ X ji − 14 iX j i F β ρ W −3 ∇α ρ λiβ −
3                              1                             9
8
  iX j i W β ρ W −2 ∇α ρ λiβ + 12 iX j i λiβ W −3 ∇α ρ Fβρ + 16 iX j i λiβ W −2 ∇α ρ Wβρ +
 1                          1
   iλ X jβ W −2 ∇α ρ λiβ − 32
16 iρ
                              iλiρ X iβ W −2 ∇α ρ λjβ + 32
                                                         1
                                                           iλρi Xβj W −2 ∇α β λiρ + 81 iλρi Xβi W −2 ∇α β λjρ −
11 β i                   3
  iλ Xβ W −2 ∇α ρ λjρ + 32
32 i
                           iλjρ Xiβ W −2 ∇α ρ λiβ − 16
                                                     1
                                                       iλjρ λβi W −2 ∇α ρ Xβi − 16
                                                                                 3
                                                                                   iλjρ Xiβ W −2 ∇α β λiρ −
 1
32
                            1
   iλjβ Xiβ W −2 ∇α ρ λiρ + 16 iλjβ λiρ W −2 ∇α ρ Xβi − 41 iλjρ λiρ W −2 ∇α β Xβi + 12
                                                                                     1
                                                                                       iλjλ λβi Wαβρ i W −3∇λρ W −
 1
12
                                 1
   iλjβ λiλ Wαβρ i W −3 ∇λρ W − 16                          11
                                   iFα β λiβ λiρ Xρj W −3 + 16 iFα β λjβ λρi Xρi W −3 −
 1
16
   iFα β λjρ λiβ Xρi W −3 + 83 iFα β λjρ λiρ Xβi W −3 + 16
                                                         5                          5
                                                           iF βρ λiα λiβ Xρj W −3− 16 iF βρ λiβ λiρ Xαj W −3 −
 1
16
                             7
   iF βρ λjα λiβ Xρi W −3 − 16 iF βρ λjβ λiα Xρi W −3 + 18 iF βρ λjβ λiρ Xαi W −3 − 18 iWα β λiβ λiρ Xρj W −2 +
23
32
   iWα β λjβ λρi Xρi W −2 − 18 iWα β λjρλiβ Xρi W −2 + 32
                                                        9                           3
                                                          iWα β λjρ λiρ Xβi W −2 + 16 iW βρ λiα λiβ Xρj W −2 −
 9
32
                             3
   iW βρ λiβ λiρ Xαj W −2 − 32 iW βρ λjα λiβ Xρi W −2 − 38 iW βρ λjβ λiα Xρi W −2 + 32
                                                                                     9
                                                                                       iW βρ λjβ λiρ Xαi W −2 +
3
4
  iX j i Fα β Fβ ρ λiρ W −4 + 83 iX j i F βρ Fβρ λiα W −4 + 98 iX j i Wα β Fβ ρ λiρ W −3 +
 9
16
   iX j i Wα β Wβ ρ λiρ W −2 − 98 iX j i W βρ Fαβ λiρ W −3 + 34 iX j i W βρ Fβρ λiα W −3 +
 3
16
   iX j i W βρ Wβρ λiα W −2 − 18 iXik X ik W −3 ∇α β λjβ − 12
                                                           1
                                                              iXik λjβ W −3 ∇α β X ik −
 1
24
   iXik λiβ W −3 ∇α β X jk + 81 iX j i X i k W −3∇α β λkβ − 16 iX j i λkβ W −3 ∇α β X ik +
 3
16
   iXik X ik Fα β λjβ W −4 + 48
                             5
                                iXik X ik Wα β λjβ W −3 + 16
                                                           1
                                                             iXik λjα λiβ Xβk W −3 −
 1
16
                           1
   iXik λjβ λiα Xβk W −3+ 32                         1
                             iXik λjβ λiβ Xαk W −3 + 16 iXik λiα λkβ Xβj W −3 + 32
                                                                                5
                                                                                   iXik λiβ λkβ Xαj W −3 +
 1
48
   iX j i X i k Wα β λkβ W −3 − 12 iX j i λiα λβk Xβk W −3 − 32
                                                              7                            3
                                                                iX j i λiβ λkβ Xαk W −3 − 16 iX j i λkα λiβ Xβk W −3 −
 1
16
   iX j i λkα λkβ Xβi W −3 − 83 λjβ λiρ W −4 ∇α β W ∇ρλ λiλ − 16
                                                               1 j
                                                                 λβ λiρ W −4 ∇ρλ W ∇α β λiλ +

                                                        10
```

</details>

<a id="src-c24-p110"></a>

<details>
<summary>C24-p110 — PDF page 110: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p110: PDF page 110](https://arxiv.org/pdf/2311.00679v1#page=110) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1 j
 λ λ λi W −4 ∇βρ ∇α λ W + 38 λjβ λiρ W −4 ∇α ρ W ∇βλ λiλ + 16
8 β iρ λ
                                                           1 j
                                                              λβ λiρ W −4 ∇βλ W ∇α ρ λiλ +
 1 j
  λ λ W −4 ∇α λ W ∇βρ λiλ + 14 λjβ λiρ W −4 ∇βρ W ∇α λ λiλ + 16
16 β iρ
                                                              1
                                                                λiα λiβ W −4 ∇λ β W ∇λρ λjρ +
 1
                                 λα λiβ W −4 ∇λ β W ∇λρ λiρ − 18 λjβ λiα W −4 ∇λ β W ∇λρ λiρ −
                               1 j
   λ λi W −4 ∇λ ρ W ∇λβ λjρ + 16
16 iα β

 1 j
  λ λ W −4 ∇λ ρ W ∇λβ λiρ + 12 Fαβ λjρ λiρ λiλ W −5 ∇βλ W − 21 Fα β λjρ λiβ λiλ W −5 ∇ρλ W −
16 β iα

  F ρ λjλ λiα λiβ W −5 ∇ρλ W + 21 F β ρ λjβ λiα λiλ W −5 ∇ρλ W + 16
1 β
2
                                                                 9
                                                                    Wαβ λjρ λiρ λiλ W −4 ∇βλ W −
 3
32
                                  9
   Wα β λjρ λiβ λiλ W −4 ∇ρλ W − 32                                3
                                    W β ρ λjα λiβ λiλ W −4 ∇ρλ W + 32 W β ρ λjλ λiα λiβ W −4 ∇ρλ W +
 3
16
   W β ρ λjβ λiα λiλ W −4 ∇ρλ W − 16
                                   1                              5
                                     Xik λjα λiβ λkρ W −5 ∇βρ W + 16 Xik λjβ λiα λkρ W −5 ∇βρ W +
 3
16
                                  1
   X j i λkαλiβ λkρ W −5 ∇βρ W − 16 iλjβ W −2 ∇ρλ ∇ρλ ∇α β W − 16
                                                                1
                                                                  iW −2 ∇α β W ∇ρλ ∇ρλ λjβ −
1
8
  iW −2 ∇ρλ W ∇ρλ ∇α β λjβ − 18 iW −2 ∇α β λjβ ∇ρλ ∇ρλ W − 16
                                                            1
                                                              iW −2 ∇ρλ λjβ ∇ρλ ∇α β W −
1
4
  iF β ρ W −3 ∇αλ W ∇λρ λjβ − 16
                               3
                                 iW β ρ λjβ W −2 ∇λ ρ ∇α λ W − 16
                                                                3
                                                                  iW β ρ W −2 ∇αλ W ∇λρ λjβ +
1 jβ
4
                          49
  iλ W −3 ∇αλ W ∇λρ Fβρ + 128 iλjβ W −2 ∇αλ W ∇λρ Wβρ + 18 iFα β λjβ W −3 ∇ρλ ∇ρλ W +
 3
16
   iFα β W −3 ∇ρλ W ∇ρλ λjβ − 16
                               1
                                 iWα β λjβ W −2 ∇ρλ ∇ρλ W − 16
                                                             3
                                                               iλjβ W −3 ∇ρλ W ∇ρλ Fαβ +
 5
32
   iλjβ W −2 ∇ρλ W ∇ρλ Wαβ + 34 iF βρ Fβλ λjρ W −4 ∇α λ W − 38 iF βρ Fβρ λjλ W −4∇α λ W −
27
16
                                 21
   iW β λ Fβ ρ λjρ W −3 ∇α λ W + 16 iW βλ Fβρ λjλ W −3 ∇α ρ W − 16
                                                                 9
                                                                   iW βρ Fβρ λjλ W −3 ∇α λ W −
 3
64
   iW βρ Wβρ λjλ W −2 ∇α λ W + 24
                               1                                11
                                  iX j i λiβ W −3 ∇ρ β ∇α ρ W + 48 iX j i W −3 ∇αρ W ∇ρβ λiβ +
 1                                7                            1
48
   iX j i W −3 ∇ρ β W ∇α ρ λiβ − 48 iλiβ W −3 ∇αρ W ∇ρβ X ji + 48 iλiβ W −3 ∇ρ β W ∇α ρ X ji −
 5                              7                             11
48
   iX j i λiα W −3 ∇βρ ∇βρ W − 96 iX j i W −3 ∇βρ W ∇βρ λiα + 96 iλiα W −3 ∇βρ W ∇βρ X ji +
3
8
                                 3
  iX j i F β ρ λiβ W −4 ∇α ρ W + 16                                 1
                                    iX j i W β ρ λiβ W −3 ∇α ρ W − 12 iλβi Wβ ρ λ j W −2 ∇α λ λiρ +
 1
   iλβ Wβ ρ λ i W −2∇α λ λjρ − 61 iλjβ Wβ ρ λi W −2 ∇α λ λiρ + 32
12 i
                                                               1
                                                                  iλβi λiρ Xβj W −3 ∇α ρ W +
35 j β i
                           iλ λiρ Xβi W −3 ∇α ρ W + 25
                        29 jβ
  iλ λ Xβ W −3 ∇α ρ W − 96
96 ρ i                                              48
                                                       iλjρ λiρ Xβi W −3 ∇α β W −
1
6
  iF βρ λiα λiλ Wβρλ j W −3 − 16 iF βρ λjβ λλi Wαρλ i W −3 + 61 iF βρ λjλ λiα Wβρλ i W −3 +
1
6
                              1
  iF βρ λjλ λiβ Wαρλ i W −3 + 24 iWα β λρi λiλ Wβρλ j W −2 − 24
                                                              1
                                                                iWα β λjρλλi Wβρλ i W −2 −
 5
24
   iW βρ λiα λiλ Wβρλ j W −2 + 18 iW βρ λiβ λiλ Wαρλ j W −2 − 16
                                                               1
                                                                 iW βρ λjα λλi Wβρλ i W −2 +
 1
16
   iW βρ λjβ λλi Wαρλ i W −2 + 13
                               48
                                                              3
                                  iW βρ λjλλiα Wβρλ i W −2 − 16 iW βρ λjλ λiβ Wαρλ i W −2+
 1
24
                              5
   iW βρ λjλλiλ Wαβρ i W −2 + 32 iXik X ik λjβ W −4∇α β W − 41 iX j i X i k λkβ W −4 ∇α β W −

                                                      11
```

</details>

<a id="src-c24-p111"></a>

<details>
<summary>C24-p111 — PDF page 111: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p111: PDF page 111](https://arxiv.org/pdf/2311.00679v1#page=111) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1
48
                             1
   iXki λjβ λkρWαβρ i W −3 + 48 iX j k λkβ λρi Wαβρ i W −3 + 48
                                                              1
                                                                iX j i λβk λkρWαβρ i W −3 −
 7
   Φ β λj λiρ λkρ W −3 + 16
48 α ik β
                          3                            1
                            Φα β ik λjρλiβ λkρ W −3 + 48 Φα βj i λiρ λkβ λkρ W −3 +

   Φ ik λjβ λiα λkρ W −3 − 36
 1 βρ
12
                            1 βρj                     1 βρj
                              Φ i λiα λkβ λkρ W −3 − 36 Φ i λkα λiβ λkρ W −3 + 81 Xik X ik λjβ λlα λlβ W −5 −
1
  X X i l λjβ λkα λlβ W −5 + 38 X j i Xkl λiα λkβ λlβ W −5 + 24
4 ik
                                                             1
                                                                λiβ W −3 ∇λ β λjρ ∇α λ λiρ +
 1 j ρ                      1 j
  λ λ W −3 ∇λ β ∇α λ λiρ + 24
24 β i
                              λβ W −3 ∇αλ λρi ∇λβ λiρ − 24
                                                         1 jβ
                                                           λ λiρ W −3 ∇λ ρ ∇α λ λiβ −
1 j                         1
 λ λ λi W −5 ∇α ρ W ∇βλ W + 24
4 β iρ λ
                               λiα λiβ W −3 ∇ρλ ∇ρλ λjβ + 24
                                                          1
                                                             λiα W −3 ∇ρλ λjβ ∇ρλ λiβ −
 1 β
  λ W −3 ∇ρλ λjβ ∇ρλ λiα − 24
32 i
                            1 jβ                        1 jβ
                              λ λiα W −3 ∇ρλ ∇ρλ λiβ − 48 λ λiβ W −3 ∇ρλ ∇ρλ λiα −

   λ W −3 ∇ρλ λiα ∇ρλ λiβ + 18 F β ρ λjβ λλi W −4 ∇α ρ λiλ − 18 F β ρ λjλ λiβ W −4 ∇α ρ λiλ +
 1 jβ
32

  F ρ λjλ λiλ W −4 ∇α ρ λiβ − 38 F βρ λiβ λiρ W −4 ∇α λ λjλ − 18 F βρ λjλ λiβ W −4 ∇α λ λiρ +
1 β
4

1 βρ j
8
                           3
  F λβ λiλ W −4∇α λ λiρ − 32 W β ρ λiβ λiλ W −3 ∇α ρ λjλ + 18 W β ρ λjβ λλi W −3 ∇α ρ λiλ −
 1
32
   W β ρ λjλ λiβ W −3 ∇α ρ λiλ + 38 W β ρ λjλ λiλ W −3 ∇α ρ λiβ − 32
                                                                   1
                                                                     W βρ λiβ λiλ W −3 ∇α λ λjρ −
 5
32
   W βρ λiβ λiρ W −3 ∇α λ λjλ − 32
                                 3
                                   W βρ λjλ λiβ W −3 ∇α λ λiρ + 18 W βρ λjβ λiλ W −3 ∇α λ λiρ −
 1
32
   W βρ λjβ λiρ W −3 ∇α λ λiλ + 32
                                 1 j β iρ                   1 jβ ρ i
                                   λλ λi λ W −3 ∇α λ Wβρ − 32 λ λi λλ W −3 ∇α λ Wβρ −

   λ λiλ λiβ W −3 ∇α ρ Wβρ −Fα β Fβ ρ λjλ λiρ λiλ W −5 + 32 Fα β F ρλ λjβ λiρ λiλ W −5 −
 7 jλ
32

  F Fβρ λjλλiα λiλ W −5 + F βρ Fβ λ λjρ λiα λiλ W −5 − 98 Wα β Fβ ρ λjλ λiρ λiλ W −4 +
1 βρ
2

19
16
   Wα λ F βρ λjλ λiβ λiρ W −4 + 18 Wα λ F βρ λjβ λiλ λiρ W −4 − 98 Wα β Wβ ρ λjλλiρ λiλ W −3 +
35
32
   Wα β W ρλ λjβ λiρ λiλ W −3 − 19
                                16
                                   Wα β W ρλ λjρ λiβ λiλ W −3 + 89 W βρ Fαβ λjλ λiρ λiλ W −4 −
3
4
  W ρλ Fα β λjρ λiλ λiβ W −4 + 34 W ρλ Fα β λjβ λiρ λiλ W −4 − 89 W βρ Fβρ λjλ λiα λiλ W −4+
9
8
  W βλ Fβ ρ λjλ λiα λiρ W −4 − 89 W βλ Fβ ρ λjρ λiα λiλ W −4 − 33
                                                               64
                                                                  W βρ Wβρ λjλ λiα λiλ W −3 +
9
8
                                3
  W βρ Wβ λ λjρ λiα λiλ W −3 + 64 Xik λjβ λiρ W −4 ∇α β λkρ − 64
                                                               3
                                                                 Xik λjβ λiρ W −4 ∇α ρ λkβ +
 3                           3
   X λjβ λiβ W −4 ∇α ρ λkρ + 16
64 ik
                                                             5
                                Xik λiβ λkβ W −4 ∇α ρ λjρ − 64 X j i λiβ λρk W −4 ∇α β λkρ −
 3
64
   X j i λiβ λkρW −4 ∇α ρ λkβ − 13
                                64
                                   X j i λiβ λkβ W −4 ∇α ρ λkρ + 18 X j i λβk λkρ W −4 ∇α ρ λiβ +
 5 j ρ
                            λ λiβ λkρ W −4 ∇α ρ X ik − 43 Xik Fα β λjβ λiρ λkρ W −5 −
                          5 jβ
  λ λ λ W −4 ∇α β X ik + 32
64 β i kρ

17
   X W β λjβ λiρ λkρ W −4 + 32
32 ik α
                             1                            3
                               Xik Wα β λjρλiβ λkρ W −4 + 16 Xik W βρ λjβ λiα λkρ W −4 −
3 j                           1
4
  X i F βρ λiα λkβ λkρ W −5 + 32 X j i Wα β λiρ λkβ λkρ W −4 − 38 X j i W βρ λiα λkβ λkρ W −4 −

                                                       12
```

</details>

<a id="src-c24-p112"></a>

<details>
<summary>C24-p112 — PDF page 112: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113</summary>

[C24-p112: PDF page 112](https://arxiv.org/pdf/2311.00679v1#page=112) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                 3 j ρ kβ
 3
16
   X j i W βρ λkαλiβ λkρ W −4 + 64                           λ λkα λkρ λβi Xβi W −4 −
                                                          27 jρ
                                   λα λk λ λiρ Xβi W −4 + 64
 3 jρ                       3 jβ                        9 jρ
32
   λ λkα λkβ λiρ Xβi W −4 + 64 λ λkα λkρλiρ Xβi W −4 − 64 λ λiα λkρ λkβ Xβi W −4 +
 9 jβ
32
                           1
   λ λkβ λkρλiρ Xαi W −4 + 16 iλjβ W −3 ∇ρλ W ∇λβ ∇α ρ W + 16
                                                           1
                                                              iλjβ W −3 ∇ρ β W ∇λ ρ ∇α λ W +
 1
16
   iW −3 ∇αρ W ∇ρ λ W ∇λβ λjβ + 16
                                 1
                                   iW −3 ∇αρ W ∇λ β W ∇ρλ λjβ + 16
                                                                 1
                                                                   iλjβ W −3 ∇α β W ∇ρλ ∇ρλ W +
 3
   iλj W −3 ∇ρλ W ∇ρλ ∇α β W + 32
32 β
                                3
                                  iW −3 ∇α β W ∇ρλ W ∇ρλ λjβ + 16
                                                                1
                                                                  iW −3 ∇ρλ W ∇ρλ W ∇α β λjβ +
3
8
  iF β ρ λjβ W −4 ∇αλ W ∇λρ W − 32
                                 9
                                   iW β ρ λjβ W −3 ∇αλ W ∇λρ W − 32
                                                                  3
                                                                    iFα β λjβ W −4 ∇ρλ W ∇ρλ W +
 3
32
   iWα β λjβ W −3 ∇ρλ W ∇ρλ W − 14 iX j i λiβ W −4 ∇αρ W ∇ρβ W + 64
                                                                 5
                                                                    iX j i λiα W −4 ∇βρ W ∇βρ W +
 5
   iλj λ λi λλ W −5 ∇βρ λkλ + 16
16 β iα ρ k
                              3
                                 iλjβ λiα λiρ λkλ W −5 ∇βλ λkρ + 16
                                                                 5
                                                                    iλjβ λiα λiρ λkρ W −5 ∇βλ λkλ −
 1
   iλj λρ λi λ W −5 ∇βλ λkα − 16
16 β i λ kρ
                               3                                 1
                                 iλjβ λiα λiρ λkλW −5 ∇ρλ λkβ − 16 iλjβ λiα λiρ λkβ W −5∇ρλ λkλ +
 5                                 1                                   3 j ρ
16
   iλjβ λiα λiβ λkρ W −5 ∇ρλ λkλ + 16 iλjβ λiβ λiρ λkλ W −5 ∇ρλ λkα − 16 λβ λi W −4 ∇αλ W ∇λβ λiρ −
 1 j ρ                        3 jβ                         1 jβ
  λ λ W −4 ∇λ β W ∇α λ λiρ − 16
16 β i
                                λ λiρ W −4 ∇αλ W ∇λρ λiβ + 16 λ λiρ W −4 ∇λ ρ W ∇α λ λiβ −
 5 jβ
16
                               3
   λ λiβ W −4 ∇αλ W ∇λρ λiρ − 32 λiα λiβ W −4 ∇ρλ W ∇ρλ λjβ + 16
                                                               1 jβ
                                                                 λ λiα λiβ W −4 ∇ρλ ∇ρλ W +
 3 jβ                         1 jβ
32
   λ λiα W −4 ∇ρλ W ∇ρλ λiβ + 32 λ λiβ W −4 ∇ρλ W ∇ρλ λiα − 21 F β ρ λjλ λiβ λiλ W −5 ∇α ρ W +
3 βρ j
4
  F λλ λiβ λiρ W −5 ∇α λ W − 15
                             32
                                                                9
                                W β ρ λjλ λiβ λiλ W −4 ∇α ρ W + 32 W βρ λjλ λiβ λiρ W −4 ∇α λ W −
 9
32
   W βρ λjβ λiρ λiλ W −4 ∇α λ W − 16
                                   7
                                     Xik λjβ λiρ λkρ W −5 ∇α β W − 16
                                                                   5
                                                                      Xik λjβ λiβ λkρ W −5 ∇α ρ W +
 1
16
   X j i λiβ λkβ λkρ W −5 ∇α ρ W + 14 λjα λβk λkρ λλi Wβρλ i W −4 − 41 λjβ λiα λρk λkλWβρλ i W −4 −

   λ λkλ λkβ λρi Wαβρ i W −4 − 32
 1 jλ
32
                                  λ λiλ λβk λkρ Wαβρ i W −4 − 32
                                1 jλ                           1 jβ λ kρ
                                                                 λ λk λ λiλ Wαβρ i W −4 −
 3
   iλj W −4 ∇α β W ∇ρλ W ∇ρλ W − 16
64 β
                                  5
                                    iλjβ λiα λiρ λkρλkλ W −6 ∇βλ W + 16
                                                                     5
                                                                        iλjβ λiα λiρ λkβ λkλ W −6 ∇ρλ W +
1 jβ                           1 jβ                            1
4
  λ λiβ λiρ W −5 ∇αλ W ∇λρ W − 16 λ λiα λiβ W −5 ∇ρλ W ∇ρλ W + 16 iXik λjβ λiα λkρ λlβ λlρ W −6 −
 3
16
                                   9
   iXik λjβ λlα λiβ λkρ λlρ W −6 + 16                                  1
                                      iXik λjβ λlα λiρ λkρ λlβ W −6 − 32 iX j i λiα λβk λkρ λlβ λlρ W −6 −
 1
16
   iX j i λkα λiβ λkρλlβ λlρ W −6 + 41 iλjβ λiβ λρk λkλ W −5 ∇α λ λiρ − 41 iλjβ λiβ λiρ λkρ W −5 ∇α λ λkλ +
 5
16
   iFα β λjβ λρi λiλ λkρ λkλ W −6 − 58 iFα β λjρλiβ λiλ λkρ λkλ W −6 − 45 iF βρ λjλ λiα λiλ λkβ λkρ W −6+
 9
32
   iWα β λjβ λρi λiλ λkρ λkλ W −5 − 16
                                     9                                 9
                                       iWα β λjρλiβ λiλ λkρλkλ W −5 − 32 iW βρ λjβ λiα λiλ λkρ λkλ W −5 +
21
32
   iW βρ λjλλiα λiβ λkρλkλ W −5− 21
                                 32
                                                                    5
                                    iW βρ λjλλiα λiλ λkβ λkρ W −5 + 32 iλjβ λρi λiλ λkρ λkλ W −6 ∇α β W +
 5
16
                                         λ λiα λiβ λρk λkλ λlρ λlλ W −7 − 38 λjβ λiα λiρ λkβ λkλ λlρ λlλ W −7
                                      3 jβ
   iλjβ λiβ λiρ λkρ λkλ W −6 ∇α λ W + 16

                                                         13
```

</details>

<a id="src-c24-p113"></a>

<details>
<summary>C24-p113 — PDF page 113: Supplement2.2.1: complete LOG spinor descendant; scalar starts on113; Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p113: PDF page 113](https://arxiv.org/pdf/2311.00679v1#page=113) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2.2.2    Flog

   3                        81                            3         69
− 32 i(Γa )αβ Xiα ∇a Xβi − 128 i(Σab )αβ W ab Xiα Xβi + 2048 Y 2 + 1024 W ab Wab Y +
39
16
   Wab ∇c ∇c W ab − 12 Wab ∇c ∇a W cb +2Wab ∇a ∇c W cb+ 16
                                                         9 eabcd
                                                           ǫ     Wab Wcd ∇e1 Wee1 −
1005
2048
     W ab W cdWab Wcd − 12 W ab W cd Wac Wbd − 11
                                               16
                                                  iW ab Wab α i Xαi +
33
   ∇ W ∇c W ab − 94 ∇a Wab ∇c W bc − 34 ∇c Wab ∇a W cb− 13 Cabcd W ab W cd +
16 c ab

1
2
  Wa b W ac W d b Wdc − 13 Cabcd W ac W bd − 34 iW ab Wa cα i Wbcα i − 32 W −1 ∇a λαi ∇a Xαi +
3
2
  (Σab )βα W −1 ∇a λiβ ∇b Xαi + 27
                                16
                                                                  3 cd ab
                                   (Γa )βα Wab λiβ W −1 ∇b Xαi + 16 ǫ e (Σcd )βα Fab λiβ W −2 ∇e Xαi −
3
8
  (Γa )βα Fab λiβ W −2 ∇b Xαi + 23 Fab W −1 ∇c ∇c W ab − 12 Fab W −1 ∇c ∇a W cb −
                      9 ee1 cda
Fab W −1 ∇a ∇c W cb + 16 ǫ      Wcd Fab W −1 ∇b Wee1 + 98 ǫe1 e cab Wcd Fab W −1 ∇e1 W ed −
 9 ecdab
16
   ǫ     Wcd Fab W −1 ∇e1 Wee1 − 98 ǫe1 deca Wc b Fab W −1 ∇e1 Wde + 32
                                                                      5
                                                                        W cd W ab Wcd Fab W −1 −
1                           5
8
  W ca W db Wcd Fab W −1 − 16 iF ab Wab α i Xαi W −1 + 98 W −1 ∇c Fab ∇c W ab −
3
2
  W −1 ∇a Fab ∇c W bc + 43 W −1 ∇c Fab ∇a W cb+ 16
                                                 9 acdee1
                                                   ǫ      Wcd Wee1 W −1 ∇b Fab +
 1 cd ab
32
   ǫ e (Σcd )βα λiβ Xαi W −2 ∇e Fab + 38 (Γa )βα λiβ Xαi W −2 ∇b Fab +
3 α                                              27
 X W −1 ∇a ∇a λiα −(Σab )αβ Xiα W −1 ∇a ∇b λiβ + 16
4 i
                                                    (Γa )βα λiβ Xαi W −1 ∇b Wab −
27
16
   (Γa )αβ Wab Xiα W −1 ∇b λiβ − 81 Φab ji (Σab )βα λjβ Xαi W −1 − 16 Φab ij Φab ij −
 3
   ∇ ∇a Y + 43 W −1 ∇a λαi ∇b Wabα i − 256
32 a
                                        53
                                           ǫe abcd Wab λαi W −1 ∇e Wcdα i −
 9                                     9 eabcd
128
    (Γc )βα W ab λiβ W −1 ∇c Wabα i − 128 ǫ    (Σee1 )βα Wab λiβ W −1 ∇e1 Wcdα i −
 9 de                                           9
64
   ǫ e1 ac (Σde )βα Wa b λiβ W −1 ∇e1 Wcbα i − 64 (Γc )βα W a b λiβ W −1 ∇b Wcaα i +
 9                                    27
64
   (Γa )βα Wa b λiβ W −1 ∇c Wbcα i − 128 ǫe abcd Fab λαi W −2 ∇e Wcdα i −
 1                     5
   C W ab F cd W −1 − 32
12 abcd
                         W cd Wcd Wab F ab W −1 − 18 W cd Wca Wdb F ab W −1 +
1                             1
4
  Wa c W d c Wdb F ab W −1 − 12 Cabcd W cd F ab W −1 − 61 Cabcd W ac F bd W −1 −
3                              3
4
  iF ab Wa cα i Wbcα i W −1 − 16 Wab W −1 ∇c W ∇c W ab + 92 Wab W −1∇c W ∇a W cb+
9                          3                                       25 abcd
2
  Wab W −1 ∇a W ∇c W cb − 128 W ab Wab α i (Γc )α β W −1 ∇c λiβ − 256 ǫ             α
                                                                           e Wab Wcd i W
                                                                                         −1 e i
                                                                                           ∇ λα −
 3 eabcd                                     3 deac
128
    ǫ    (Σee1 )αβ Wab Wcdαi W −1 ∇e1 λiβ − 64 ǫ             αβ b
                                                    e1 (Σde ) Wa Wcbαi W
                                                                         −1 e1 i
                                                                           ∇ λβ +

                                                      14
```

</details>

<a id="src-c24-p114"></a>

<details>
<summary>C24-p114 — PDF page 114: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p114: PDF page 114](https://arxiv.org/pdf/2311.00679v1#page=114) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3                                    3
64
   (Γc )αβ W a b Wcaαi W −1 ∇b λiβ − 64 (Γa )αβ Wa b Wbcαi W −1 ∇c λiβ +
1
2
  iΦabij (Γa )αβ λiα W −2 ∇b λjβ − 16 Wab α i Φabi j λjα W −1 + 32
                                                                3
                                                                   Wab α i (Γc )α β λiβ W −1 ∇c W ab −
 3                                     1
64
   Wab α i ǫab e cd λiα W −1 ∇e Wcd + 128 Wab α i ǫabecd (Σee1 )α β λiβ W −1 ∇e1 Wcd −
 1                                                  7
64
   Wab α i ǫade e1 c (Σde )α β λiβ W −1 ∇e1 W bc + 32 Wab α i (Γc )α β λiβ W −1 ∇a W bc +
 3
16
   Wab α i (Γa )α β λiβ W −1 ∇c W bc − 34 λαi W −1 ∇a ∇a Xαi + 34 (Σab )βα λiβ W −1 ∇a ∇b Xαi −
 1                                    1
16
   (Σab )αβ W ab W cdWcdαi λiβ W −1 + 16 W ab Wab W cdα i (Σcd )α β λiβ W −1 −
1                                         1
4
  W ab Wa c Wb dα i (Σcd )α β λiβ W −1 + 16 W ab W cd Wab α i (Σcd )α β λiβ W −1 −
 1 abcee1
32
   ǫ      Wab Wcd Wee1 α i (Γd )α β λiβ W −1 + 18 W ab Wa c Wbc α i λiα W −1 −
 1 abce                           −1 1
16
   ǫ         e1 αβ    d       i
        e1 (Γ ) Wab Wc Wedαi λβ W   + 4 (Σcd )αβ W ab Wac Wbdαi λiβ W −1 −
1                                   13
4
  (Σac )αβ W ab W cdWbdαi λiβ W −1− 64 Wab α i ǫabe e1 d (Σec )α β λiβ W −1 ∇e1 W cd−
 13                                                3
128
    Wab α i ǫaee1 cd (Σee1 )α β λiβ W −1 ∇b Wcd − 32 i(Γa )αβ Y λiα W −2 ∇a λiβ +
 3                  3                   27
32
   Y W −1 ∇a ∇a W + 32 W −1 ∇a W ∇a Y − 32 W ab Fab λαi Xαi W −2 −
27                                        3                     3
   ǫ cdab (Γe )βα Wcd Fab λiβ Xαi W −2 + 128
64 e
                                             F ab Fab Y W −2 + 64 i(Σab )αβ F ab Y λiα λiβ W −3 −
3                                9                     3
4
  (Γa )βα Xij λiβ W −2 ∇a Xαj − 128 Xij X ij Y W −2 − 32 iXij Y λiα λjα W −3 −

   ǫ e (Σcd )αβ Fab Xiα W −2 ∇e λiβ + 83 (Γa )αβ Fab Xiα W −2∇b λiβ −
 3 cd ab
16

3 eabcd                          75
8
  ǫ     Fab Fcd W −2 ∇e1 Wee1 − 128 W cd Wcd F ab Fab W −2− 18 W ab W cdFab Fcd W −2 −
1
8
                            3
  W ac W bd Fab Fcd W −2 − 16 ǫe abcd (Γe )βα Fab Fcd λiβ Xαi W −3 + 43 (Γa )αβ Xij Xαi W −2 ∇a λjβ −
1                                                        9 β
  Φ X ij F ab W −2 + 43 (Σab )βα Xij F ab λiβ Xαj W −3 + 16
2 abij
                                                            λi λjβ X iα Xαj W −2−
11 α β i           7 β α i
  λ λ X X j W −2 + 16
16 i j α β
                      λi λj Xα Xβj W −2 + 81 λαj λjβ Xiα Xβi W −2 +
 9
   X X ij W ab Wab W −2 + 167
128 ij
                              X X ij λαk Xαk W −3 − 14 i(Σa c )αβ Wab λiα W −2 ∇c ∇b λiβ +
                          384 ij

3                                      1
8
  i(Σab )αβ W ab λiα W −2 ∇c ∇c λiβ + 16 iǫcde ab (Γc )αβ Wab λiα W −2 ∇d ∇e λiβ −
1
4
  iWab λαi W −2 ∇a ∇b λiα +i(Σa c )αβ Wab λiα W −2 ∇b ∇c λiβ + 12 Wab W −1 ∇c ∇c F ab +
                        3
2Wcb W −1 ∇c ∇a F ab − 32 W ab Wab W −1 ∇c ∇c W + 92 W a b Wac W −1 ∇b ∇c W −
1
  ǫ ab W −1 ∇c W ∇d ∇e Wab + 83 i(Σab )αβ λiα λiβ W −2 ∇c ∇c W ab +
2 cde

1
4
  i(Σca )αβ λiα λiβ W −2 ∇c ∇b W ab + 12 i(Σca )αβ λiα λiβ W −2 ∇b ∇c W ab +

                                                       15
```

</details>

<a id="src-c24-p115"></a>

<details>
<summary>C24-p115 — PDF page 115: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p115: PDF page 115](https://arxiv.org/pdf/2311.00679v1#page=115) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
9
4
  i(Σac )αβ λiα W −2 ∇b W ab ∇c λiβ + 38 i(Σab )αβ λiα W −2 ∇c W ab ∇c λiβ +
 3
   iǫ ab e (Γc )αβ λiα W −2 ∇d Wab ∇e λiβ + 34 iλαi W −2 ∇a Wab ∇b λiα −
16 cd

9
  ǫ ab de W −1 ∇c Wab ∇d ∇e W + 41 λαi W −1 ∇a ∇b Wabα i −i(Σa c )αβ Fab W −3 ∇c λiα ∇b λiβ +
8 c

1
4
  i(Σab )αβ F ab W −3 ∇c λiα ∇c λiβ − 81 iǫcde ab (Γc )αβ Fab W −3 ∇d λiα ∇e λiβ +
1                            3
4
  iFab W −3 ∇a λαi ∇b λiα + 16 iǫe cdab Wcd Fab λαi W −3 ∇e λiα + 38 i(Γc )αβ W ab Fab λiα W −3 ∇c λiβ +
3
4
  i(Γc )αβ Wc a Fab λiα W −3 ∇b λiβ + 38 iǫe e1 cda (Σe b )αβ Wcd Fab λiα W −3 ∇e1 λiβ −
 3 ee1 cab
16
   iǫ      (Σee1 )αβ Wcd Fab λiα W −3 ∇d λiβ − 34 iǫecdab (Σee1 )αβ Wcd Fab λiα W −3 ∇e1 λiβ +
 1 abcd               −2 e i    3                                     3
16
   ǫ             α
        e Fab Wcd i W   ∇ λα + 32 iǫe abcd Fab Fcd λαi W −4 ∇e λiα − 16 i(Γc )αβ F ab Fab λiα W −4 ∇c λiβ +
3
4
  i(Γa )αβ Fa b Fbc λiα W −4 ∇c λiβ − 38 iǫe e1 abc (Σe d )αβ Fab Fcd λiα W −4 ∇e1 λiβ +
 3 ee1 abc
16
   iǫ      (Σee1 )αβ Fab Fcd λiα W −4 ∇d λiβ + 14 F ab Fab W −3 ∇c ∇c W +

F a b Fac W −3 ∇b ∇c W − 34 W cd F ab Fcd Fab W −3 + 23 W cd F ab Fca Fdb W −3 +
5
2
  W dc Wda F ab Fcb W −2 − 12 i(Σab )αβ λiα W −3 ∇c F ab ∇c λiβ + 41 iλαi W −3 ∇a Fab ∇b λiα +
1                                      1 e
2
  i(Σac )αβ λiα W −3 ∇b F ab ∇c λiβ − 32 iǫ e1 b cd (Σea )αβ Wcd λiα λiβ W −3 ∇e1 F ab −
 1 ee1 abc
64
   iǫ      (Σee1 )αβ Wcd λiα λiβ W −3 ∇d Fab − 18 ǫeabcd Fab Fcd W −3 ∇e1 Fee1 −
 3 cee1 ab
16
   ǫ       Wee1 Fab W −2 ∇d Fcd − 81 ǫe1 cdea We b Fab W −2 ∇e1 Fcd +Fab W −3 ∇c W ∇c F ab +
                         3 e
Fab W −3 ∇a W ∇c F cb + 16 iǫ e1 d ab (Σec )αβ Fab λiα λiβ W −4 ∇e1 F cd +
 3 ee1 cda
32
   iǫ      (Σee1 )αβ Fab λiα λiβ W −4 ∇b Fcd − 12 i(Σa c )αβ Fab λiα W −3 ∇c ∇b λiβ −
1
4
  i(Σab )αβ F ab λiα W −3 ∇c ∇c λiβ − 12 i(Σa c )αβ Fab λiα W −3 ∇b ∇c λiβ +
3 e                                               3 ee1 cda
8
  iǫ e1 d ab (Σec )αβ Fab λiα λiβ W −3 ∇e1 W cd+ 16 iǫ      (Σee1 )αβ Fab λiα λiβ W −3 ∇b Wcd −
11                                        15
32
   i(Σcd )αβ W cd W ab Fab λiα λiβ W −3 − 32 i(Σab )αβ W cdWcd F ab λiα λiβ W −3 +
19
 8
   i(Σda )αβ W cb Wdc Fab λiα λiβ W −3 + 21 i(Σcd )αβ W ca W db Fab λiα λiβ W −3 +
 81                              1                                       1
128
    W ac Fa b Wcb α i λiα W −2 + 16 (Σab )αβ F ab F cd Wcdαi λiβ W −3 − 16 F ab Fab W cdα i (Σcd )α β λiβ W −3 +
1 ab                                   1
4
  F Fa c Wb dα i (Σcd )α β λiβ W −3 − 16 F ab F cd Wab α i (Σcd )α β λiβ W −3+
 1 abcee1
32
   ǫ      Fab Fcd Wee1 α i (Γd )α β λiβ W −3 − 18 F ab Fa c Wbc α i λiα W −3 +
 1 abce                           −3 1
16
   ǫ         e1 αβ    d       i
        e1 (Γ ) Fab Fc Wedαi λβ W   − 4 (Σcd )αβ F ab Fac Wbdαi λiβ W −3 +

                                                       16
```

</details>

<a id="src-c24-p116"></a>

<details>
<summary>C24-p116 — PDF page 116: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p116: PDF page 116](https://arxiv.org/pdf/2311.00679v1#page=116) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
4
  (Σac )αβ F ab F cdWbdαi λiβ W −3 − 38 iΦabij F ab λiα λjα W −3 − 16 iǫ c Φdeij (Γc )αβ Fab λiα λjβ W −3 +
                                                                    1 de ab

 9 ecdab                                       9 de
32
   iǫ    (Σee1 )αβ Fab λiα λiβ W −3 ∇e1 Wcd − 16 iǫ e1 c a (Σde )αβ Fab λiα λiβ W −3 ∇e1 W cb +
 25                                      27
256
    (Σab )αβ W cd F ab Wcdαi λiβ W −2 + 256 W ab Fab W cdα i (Σcd )α β λiβ W −2 −
27                                        27
64
   W ac Fa b Wb dα i (Σcd )α β λiβ W −2 + 256 W cd F ab Wab α i (Σcd )α β λiβ W −2 −
 27 cdaee1                                       27 cabe
512
    ǫ      Wcd Fab Wee1 α i (Γb )α β λiβ W −2 − 256 ǫ         e1 αβ d          i
                                                         e1 (Γ ) Wc Fab Wedαi λβ W
                                                                                   −2
                                                                                      +
27
64
   (Σbd )αβ W ac Fab Wcdαi λiβ W −2 − 27
                                      64
                                         (Σca )αβ W cd F ab Wdbαi λiβ W −2 +
 3 ecdab                                       3 de
32
   iǫ    (Σee1 )αβ Fab λiα λiβ W −4 ∇e1 Fcd − 16 iǫ e1 c a (Σde )αβ Fab λiα λiβ W −4 ∇e1 F cb −
 7                                    7 eabcd
64
   (Γc )βα F ab λiβ W −2 ∇c Wabα i − 64 ǫ     (Σee1 )βα Fab λiβ W −2 ∇e1 Wcdα i −
 7 de                                           7
32
   ǫ e1 ac (Σde )βα Fa b λiβ W −2 ∇e1 Wcbα i − 32 (Γc )βα F a b λiβ W −2 ∇b Wcaα i +
 7                                    9 ecdab
32
   (Γa )βα Fa b λiβ W −2 ∇c Wbcα i + 64 iǫ    (Σee1 )αβ Wab λiα λiβ W −2 ∇e1 Wcd +
 7 eabcd                                       5 de
64
   iǫ    (Σee1 )αβ Wcd λiα λiβ W −3 ∇e1 Fab + 32 iǫ e1 a c (Σde )αβ Wcb λiα λiβ W −3 ∇e1 F ab +
 3 cdee1 a
16
   ǫ       Wee1 Fab W −2 ∇b Fcd + 38 ǫe1 c eab Wed Fab W −2 ∇e1 F cd− 128
                                                                       9
                                                                          iǫe abcd Wab Wcd λαi W −2 ∇e λiα +
15                                      9
64
   i(Γc )αβ W ab Wab λiα W −2 ∇c λiβ + 16 i(Γa )αβ Wa b Wbc λiα W −2 ∇c λiβ −
 9 e                                              9 ee1 abc
32
   iǫ e1 abc (Σe d )αβ Wab Wcd λiα W −2 ∇e1 λiβ + 64 iǫ     (Σee1 )αβ Wab Wcd λiα W −2 ∇d λiβ +
 9 eabcd
64
   iǫ    (Σee1 )αβ Wab Wcd λiα W −2 ∇e1 λiβ − 34 i(Σa c )αβ Wab W −2 ∇c λiα ∇b λiβ +
3                                      3
4
  i(Σab )αβ W ab W −2 ∇c λiα ∇c λiβ − 16 iǫcde ab (Γc )αβ Wab W −2 ∇d λiα ∇e λiβ −
1                                                  23 abcd
2
  Wab W −2 ∇c W ∇c F ab −2Wcb W −2 ∇a W ∇c F ab − 512 ǫ             α   i
                                                           e Wab Wcd i λα W
                                                                            −2 e
                                                                              ∇ W−
 81
256
    i(Σab )αβ W ab W cd Wcd λiα λiβ W −2 + 89
                                           64
                                              i(Σcd )αβ W ab Wca Wdb λiα λiβ W −2 +
1
8
  iΦabij W ab λiα λjα W −2 − 18 iǫde c ab Φdeij (Γc )αβ Wab λiα λjβ W −2 + 256
                                                                           19
                                                                               W ab Wab α i (Γc )α β λiβ W −2 ∇c W +
 19 eabcd                                      19 deac
256
    ǫ     (Σee1 )αβ Wab Wcdαi λiβ W −2 ∇e1 W + 128 ǫ            αβ b       i
                                                       e1 (Σde ) Wa Wcbαi λβ W
                                                                               −2 e1
                                                                                 ∇ W−
 19                                     19
128
    (Γc )αβ W a b Wcaαi λiβ W −2 ∇b W + 128 (Γa )αβ Wa b Wbcαi λiβ W −2 ∇c W +
1 ab
8
  F Wab α i (Γc )α β W −2 ∇c λiβ + 81 ǫeabcd (Σee1 )αβ Fab Wcdαi W −2 ∇e1 λiβ +
1 deac
4
  ǫ             αβ b
       e1 (Σde ) Fa Wcbαi W   ∇ λβ − 41 (Γc )αβ F a b Wcaαi W −2 ∇b λiβ +
                            −2 e1 i

1
4
  (Γa )αβ Fa b Wbcαi W −2 ∇c λiβ − 32 W ab Fab W −2 ∇c ∇c W −W a c Fab W −2 ∇c ∇b W +

W a c Fab W −2 ∇b ∇c W + 34 λαi W −2 ∇a W ∇a Xαi − 64
                                                    3
                                                      Y W −2 ∇a W ∇a W −

                                                      17
```

</details>

<a id="src-c24-p117"></a>

<details>
<summary>C24-p117 — PDF page 117: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p117: PDF page 117](https://arxiv.org/pdf/2311.00679v1#page=117) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 iλ W −3 ∇a X i j ∇a λjα − 12 i(Σab )αβ λiα W −3 ∇a X i j ∇b λjβ + 16
1 α
4 i
                                                                    3
                                                                      i(Γa )αβ Wab λiα λjβ W −3 ∇b X ij −
3
8
  i(Γa )αβ Fab λiα λjβ W −4 ∇b X ij + 41 iXij W −3 ∇a λiα ∇a λjα + 12 i(Σab )αβ Xij W −3 ∇a λiα ∇b λjβ +

  iǫ e (Σcd )αβ Xij Wab λiα W −3 ∇e λjβ + 38 i(Γa )αβ Xij Wab λiα W −3 ∇b λjβ +
3 cd ab
8

  iǫ e (Σcd )αβ Xij Fab λiα W −4 ∇e λjβ − 14 Xij F ab Wab αi λjα W −3 −
3 cd ab
8

1
  X W ab Wab αi λjα W −2 + 38 i(Γa )αβ Xij λiα λjβ W −4 ∇b Fab + 43 iXij λiα W −3 ∇a ∇a λjα +
4 ij

15
16
   i(Γa )αβ Xij λiα λjβ W −3 ∇b Wab − 64
                                       3                               9
                                         iXij W ab Wab λiα λjα W −3 − 128 iǫe abcd (Γe )αβ Xij Wab Wcd λiα λjβ W −3 −
 11
192
    iΦab ik (Σab )αβ X i j λkα λjβ W −3 + i(Γa )αβ λρi λjρXαi W −3 ∇a λjβ +
3 α i
 λ Xα W −2 ∇a ∇a W + 87 (Σab )βα λiβ Xαi W −2 ∇a ∇b W − 384
4 i
                                                         31
                                                            W abα i (Σab )βρ λjβ λjρ Xαi W −2 −
 7
192
    W abα i (Σab )βρ λiβ λjρXαj W −2 + 83 i(Γa )βα λjβ λjρ λiρ W −3 ∇a Xαi +
5
6
  i(Γa )βρ λjβ λαi Xαi W −3 ∇a λjρ − 34 Xiα W −2 ∇a W ∇a λiα − 32
                                                               11
                                                                  i(Γa )βα λiβ λρj Xαi W −3 ∇a λjρ +
 5                                    3
24
   i(Γa )βρ λjβ λjα Xiα W −3 ∇a λiρ + 32 i(Γa )βα λjβ λjρXiα W −3 ∇a λiρ +
1
  C F ab F cd W −2 + 18 Wab Wcd F ab F cdW −2 + 18 Wac Wbd F ab F cd W −2 −
6 abcd

1
4
  W d b Wdc Fa b F ac W −2 + 16 Cabcd F ac F bd W −2 + 24
                                                       1
                                                          i(Σcd )αβ Cabcd W ab λiα λiβ W −2 −
1                                       1
8
  i(Σac )αβ W ab W cdWbd λiα λiβ W −2 + 24 i(Σab )αβ Cabcd W cd λiα λiβ W −2 +
 1                                     1
12
   i(Σac )αβ Cabcd W bd λiα λiβ W −2 + 24 i(Σcd )αβ Cabcd F ab λiα λiβ W −3 +
 1                                        1
16
   i(Σcd )αβ W cd Wab F ab λiα λiβ W −3 + 16 i(Σcd )αβ Wca Wdb F ab λiα λiβ W −3 −
1                                        1
8
  i(Σca )αβ W cd Wdb F ab λiα λiβ W −3 + 24 i(Σab )αβ Cabcd F cd λiα λiβ W −3 +
 1                                      9
12
   i(Σac )αβ Cabcd F bd λiα λiβ W −3 − 16 i(Σab )βα W ab λjβ λjρ λiρ Xαi W −3 −
 9
256
    Y λαi λiβ λjαλjβ W −4 − 41 i(Γa )αβ λiα W −3 ∇b λiβ ∇a ∇b W − 14 iǫab cde (Σab )αβ λiα W −3 ∇c λiβ ∇d ∇e W −
1
4
  i(Γa )αβ λiα W −3 ∇b λiβ ∇b ∇a W − 54 i(Γa )αβ λiα W −3 ∇a λiβ ∇b ∇b W +
7                                        9
8
  i(Σa c )αβ Wab λiα λiβ W −3 ∇c ∇b W − 16 i(Σab )αβ W ab λiα λiβ W −3 ∇c ∇c W −
1
8
  i(Σa c )αβ Wab λiα λiβ W −3 ∇b ∇c W + 12 ǫcde ab Fab W −3 ∇c W ∇d ∇e W +
3
4
  i(Σa c )αβ Fab λiα λiβ W −4 ∇c ∇b W + 38 i(Σab )αβ F ab λiα λiβ W −4 ∇c ∇c W +
3
4
  i(Σa c )αβ Fab λiα λiβ W −4 ∇b ∇c W + 34 ǫcde ab Wab W −2 ∇c W ∇d ∇e W +
3
4
  i(Σa c )αβ Wab λiα W −3 ∇c W ∇b λiβ − 98 i(Σab )αβ W ab λiα W −3 ∇c W ∇c λiβ +

                                                      18
```

</details>

<a id="src-c24-p118"></a>

<details>
<summary>C24-p118 — PDF page 118: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p118: PDF page 118](https://arxiv.org/pdf/2311.00679v1#page=118) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3                                        3
4
  i(Σa c )αβ Wab λiα W −3 ∇b W ∇c λiβ + 64 W ab Wab W −2 ∇c W ∇c W −
9
4
  W a b Wac W −2 ∇b W ∇c W + 43 i(Σab )αβ λiα λiβ W −4 ∇c W ∇c F ab −
3
4
  i(Σca )αβ λiα λiβ W −4 ∇c W ∇b F ab − 14 i(Γa )αβ λiα W −3 ∇b W ∇a ∇b λiβ −
5
4
  i(Γa )αβ λiα W −3 ∇b W ∇b ∇a λiβ − 14 i(Γa )αβ λiα W −3 ∇a W ∇b ∇b λiβ −
 9
16
   i(Σab )αβ λiα λiβ W −3 ∇c W ∇c W ab − 83 i(Σca )αβ λiα λiβ W −3∇c W ∇b W ab −
3
8
  i(Σca )αβ λiα λiβ W −3 ∇b W ∇c W ab + 32 i(Σa c )αβ Fab λiα W −4 ∇c W ∇b λiβ +
3
4
  i(Σab )αβ F ab λiα W −4 ∇c W ∇c λiβ + 23 i(Σa c )αβ Fab λiα W −4 ∇b W ∇c λiβ +
3
2
  W ab Fab W −3 ∇c W ∇c W +i(Γa )αβ W −3 ∇b W ∇a λiα ∇b λiβ − 32 Fab W −2 ∇c W ∇c W ab +

 λ W −2 ∇a W ∇b Wabα i − 38 F ab Fab W −4 ∇c W ∇c W − 32 F a b Fac W −4 ∇b W ∇c W −
1 α
8 i

27
32
   i(Σab )αβ W cd F ab Fcd λiα λiβ W −4 + 27
                                           8
                                             i(Σda )αβ W dc F ab Fcb λiα λiβ W −4 −
45                                         9
64
   i(Σcd )αβ W cd F ab Fab λiα λiβ W −4 + 16 i(Σac )αβ W bd Fab Fcd λiα λiβ W −4 −
3 eabcd                                       1
8
  iǫ    (Σee1 )αβ Fab Fcd λiα W −4 ∇e1 λiβ + 32 iWab α i ǫabcd e (Σcd )βρ λiβ λjα W −3∇e λjρ −
 1
16
   iWab α i (Γa )βρ λiβ λjα W −3 ∇b λjρ − 21 Wab α i λiα W −2 ∇a ∇b W + 24
                                                                        1
                                                                           W abα i Wa c α i (Σbc )βρ λjβ λjρ W −2 +
 1
32
   W abα i Wabαj λiβ λjβ W −2 − 64
                                 1
                                   Wab α i Wcdαj ǫabcd e (Γe )βρ λiβ λjρ W −2 +
 1                                          3 cd ab
24
   W abα i Wa c αj (Σbc )βρ λiβ λjρ W −2 + 64 iǫ e (Σcd )βρ λjβ λjρ λαi W −3 ∇e Wabα i −
 3
64
   iWab α i ǫabcd e (Σcd )βρ λjαλjβ W −3 ∇e λiρ + 32
                                                   3
                                                     iWab α i (Γa )βρ λjα λjβ W −3 ∇b λiρ −
 3 cd ab                                      3
64
   iǫ e (Σcd )βρ λjβ λjα λiρ W −3 ∇e Wabα i + 32 i(Γa )βρ λjβ λjαλiρ W −3 ∇b Wabα i −
9
4
                               9
  iXij λiα W −4 ∇a W ∇a λjα − 32 iXij W ab Fab λiα λjα W −4 − 27 iǫ cdab (Γe )αβ Xij Wcd Fab λiα λjβ W −4 +
                                                              64 e

 77
128
    i(Σab )βρ W ab λjβ λjα λiρ Xαi W −3 − 139
                                          256
                                              i(Σab )βρ W ab λjβ λjρ λαi Xαi W −3 −
3 α i                  7
 λ Xα W −3 ∇a W ∇a W + 32
4 i
                          i(Γa )βα λjβ λρi Xαi W −3 ∇a λjρ − 18 i(Γa )βρ λiβ λjρX iα W −3 ∇a λjα −
1
2
                              1
  Wab α i W −2 ∇a W ∇b λiα − 16 (Γa )αβ (Γb )ρλ λiα λjβ W −4 ∇a λiρ ∇b λjλ +
 5                                     1
12
   i(Γa )βρ λiβ λαj Xαi W −3 ∇a λjρ + 48 iWab α i ǫabcd e (Σcd )βρ λjβ λjρ W −3 ∇e λiα +
21
32
   (Γa )αβ (Γb )ρλ λiα λjρ W −4 ∇a λiβ ∇b λjλ − 32
                                                 1
                                                   (Γa )αβ (Γb )ρλ λiα λjρ W −4 ∇a λjλ ∇b λiβ −
 1
48
   iWab α i ǫabcd e (Σcd )βρ λiβ λjρW −3 ∇e λjα + 18 iWab α i (Γa )βρ λiβ λjρ W −3 ∇b λjα +
 7
48
   iW ab Wab α i λiβ λjα λjβ W −3 + 192
                                    83
                                        i(Σa c )βρ W ab Wbc α i λiα λjβ λjρ W −3−

                                                       19
```

</details>

<a id="src-c24-p119"></a>

<details>
<summary>C24-p119 — PDF page 119: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p119: PDF page 119](https://arxiv.org/pdf/2311.00679v1#page=119) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1                                                   1
384
    iǫabcd e (Γe )βρ Wab Wcd α i λiβ λjρ λjα W −3 + 48 i(Σa c )βρ W ab Wbc α i λiβ λjρλjα W −3 +
 1
16
   (Γa )αβ (Γb )ρλ λiα λiρ λjβ W −4 ∇b ∇a λjλ + 16
                                                 3
                                                   (Γa )αβ (Γb )ρλ λiα λiρ λjβ W −4 ∇a ∇b λjλ +
 1
16
   (Γa )αβ (Γb )ρλ λiα λiρ W −4 ∇a λjβ ∇b λjλ + 16
                                                 1
                                                   (Γa )αβ (Γb )ρλ λiα λiρ W −4 ∇a λjλ ∇b λjβ −
1 α β
 λ λ W −4 ∇a λiα ∇a λjβ − 38 (Σab )αβ λiα λρj W −4 ∇a λiβ ∇b λjρ + 81 (Σab )αβ λiα λρj W −4 ∇a λiρ ∇b λjβ +
8 i j

 λ λ λjαW −4 ∇a ∇a λjβ − 18 (Σab )αβ λiα λiρ λjρW −4 ∇a ∇b λjβ + 16
1 α iβ
2 i
                                                                    λi λ W −4 ∇a λjα ∇a λjβ −
                                                                  1 α iβ

1
8
                                            ǫ e (Σcd )αβ Wab λiα λiβ λρj W −4 ∇e λjρ +
                                         27 cd ab
  (Σab )αβ λiα λiρ W −4 ∇a λjβ ∇b λjρ + 256

  ǫ e (Σcd )αβ Fab λiα λiβ λρj W −5 ∇e λjρ + 128
1 cd ab
4
                                              13
                                                 iF ab Wab α i λiβ λjα λjβ W −4 −
 13 abcd                              −4 13
256
    iǫ       e βρ      α   i      j
         e (Γ ) Fab Wcd i λβ λjρ λα W   + 32 i(Σa c )βρ F ab Wbc α i λiβ λjρ λjα W −4 +
 1
16
   i(Σa c )βρ F ab Wbc α i λiα λjβ λjρ W −4 − 137
                                              128
                                                  i(Σab )βρ F ab λjβ λjρ λαi Xαi W −4 −
9                                       7
8
  i(Σab )βα F ab λjβ λjρλiρ Xαi W −4 + 64 i(Σab )βρ F ab λjβ λjα λiρ Xαi W −4 −
 33 cd ab                                       19
256
    ǫ e (Σcd )αβ Wab λiα λiρ λjβ W −4 ∇e λjρ − 128 (Γa )αβ Wab λiα λiρ λjβ W −4 ∇b λjρ −
 1 cd ab
16
   ǫ e (Σcd )αβ Fab λiα λiρ λjβ W −5 ∇e λjρ − 85 (Γa )αβ Fab λiα λiρ λjβ W −5 ∇b λjρ +

  λ λ W −4 ∇a λiβ ∇a λjβ − 78 (Σab )αβ λρi λjρW −4 ∇a λiα ∇b λjβ + 125
 1 α
16 i jα                                                            256
                                                                       ǫcd e ab (Σcd )αβ Wab λiα λiρ λjρ W −4∇e λjβ +
 19
128
    (Γa )αβ Wab λiα λiρ λjρ W −4 ∇b λjβ + 16 ǫ e (Σcd )αβ Fab λiα λiρ λjρ W −5 ∇e λjβ −
                                          11 cd ab

3
8
  (Γa )αβ Fab λiα λiρ λjρW −5 ∇b λjβ − 128
                                        19
                                           (Σab )ρλ (Γc )αβ W ab λiρ λiα λjβ W −4 ∇c λjλ −
1
8
  (Σab )ρλ (Γc )αβ F ab λiρ λiα λjβ W −5 ∇c λjλ + 32
                                                   7
                                                     (Γa )αβ (Γb )ρλ λiα λjρW −4 ∇a λjβ ∇b λiλ +
 7
128
    (Σab )ρλ (Γc )αβ W ab λiρ λiα λjλ W −4 ∇c λjβ − 81 (Σab )ρλ (Γc )αβ F ab λiρ λiα λjλ W −5 ∇c λjβ +
 47
128
    (Σab )ρλ (Γc )αβ W ab λiρ λiλ λjα W −4 ∇c λjβ + 54 (Σab )ρλ (Γc )αβ F ab λiρ λiλ λjαW −5 ∇c λjβ −
1
8
  (Σab )αβ λiα λiβ W −4 ∇a λρj ∇b λjρ − 81 (Σab )αβ λiα λjβ W −4 ∇a λiρ ∇b λjρ +
 1
32
   (Γa )αβ (Γb )ρλ λiα λjρ W −4 ∇a λiλ ∇b λjβ + 41 (Γa )αβ λiα λiρ λjβ λjρ W −5 ∇b Fab +
1                                        9
8
  (Σab )αβ λiα λiρ λjβ W −4 ∇a ∇b λjρ + 16 (Γa )αβ λiα λiρ λjβ λjρ W −4 ∇b Wab −
 3                                                     3
128
    iWab α i ǫabcd e (Σcd )βρ λiβ λjα λjρ W −4 ∇e W − 64 iWab α i (Γa )βρ λiβ λjα λjρ W −4 ∇b W +
 9
256
    W ab Wab λαi λiβ λjαλjβ W −4 − 128
                                    27
                                       ǫe abcd (Γe )αβ Wab Wcd λiα λiρ λjβ λjρ W −4 −
105
256
    (Σab )αβ (Σcd )ρλ W ab W cdλiα λiβ λjρλjλ W −4 + 128
                                                     57
                                                         (Σab )αβ (Σcd )ρλ W ab W cd λiα λiρ λjβ λjλ W −4 +
 25 ab                                   119 ab
192
    Φ ij (Σab )αβ λiα λjρ λkβ λkρ W −4 + 384 Φ ij (Σab )αβ λiρ λjρ λkα λkβ W −4 −

                                                        20
```

</details>

<a id="src-c24-p120"></a>

<details>
<summary>C24-p120 — PDF page 120: Supplement2.2.2: complete LOG scalar descendant; vector starts on121</summary>

[C24-p120: PDF page 120](https://arxiv.org/pdf/2311.00679v1#page=120) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
8
  (Σab )αβ λiα λiβ λρj W −4∇a ∇b λjρ − 64
                                        3
                                          iWab α i ǫabcd e (Σcd )βρ λiα λjβ λjρ W −4 ∇e W −
3
8
  i(Γa )αβ Xij λiα λkβ W −4 ∇a X jk − 98 iXij λiα λjα W −4 ∇a ∇a W + 64
                                                                      9
                                                                        i(Σab )αβ Xij X i k W ab λjα λkβ W −4 −
61
64
   iXij λiβ λjα λkβ Xαk W −4 + 83
                               64
                                  iXij λiβ λjβ λαk Xαk W −4 + 11
                                                              64
                                                                 iXij λiβ λkβ λkαXαj W −4 −
 1
32
   (Γa )αβ Xij λiρ λkα λkρ W −5 ∇a λjβ + 32
                                          1
                                            (Γa )αβ Xij λiα λkβ λkρ W −5 ∇a λjρ +
1
2
  i(Γa )αβ Xij X ij λkα W −4 ∇a λkβ − 21
                                      16
                                         (Γa )αβ Xij λiρ λjρ λkαW −5 ∇a λkβ −
13
32
   (Γa )αβ Xij λiα λjρ λkβ W −5 ∇a λkρ + 18 i(Γa )αβ Xij X i k λjα W −4 ∇a λkβ −
33
32
   (Γa )αβ Xij λiα λjρ λkρ W −5 ∇a λkβ − 98 iλαi λjα W −4 ∇a W ∇a X ij + 83 (Γa )αβ λkα λkρ λiβ λjρ W −5 ∇a X ij +
1
2
  i(Γa )αβ λiα W −2 ∇b ∇b ∇a λiβ −W −1 ∇a ∇a ∇b ∇b W + 34 i(Γa )αβ λiα W −4 ∇a W ∇b W ∇b λiβ −
9
8
  i(Σa c )αβ Wab λiα λiβ W −4 ∇c W ∇b W + 27
                                          32
                                             i(Σab )αβ W ab λiα λiβ W −4 ∇c W ∇c W −

3i(Σa c )αβ Fab λiα λiβ W −5 ∇c W ∇b W − 34 i(Σab )αβ F ab λiα λiβ W −5 ∇c W ∇c W −
1
2
  i(Γa )αβ W −2 ∇a λiα ∇b ∇b λiβ − 12 Fab W −2 ∇c ∇c F ab − 14 i(Σab )αβ λiα λiβ W −3 ∇c ∇c F ab +
1
2
  i(Γa )αβ W −2 ∇b λiα ∇b ∇a λiβ − 14 W −2 ∇c Fab ∇c F ab − 32
                                                             3
                                                               F ab F cd Fab Fcd W −4 +
3 ab cd
8
  F F Fac Fbd W −4 − 83 i(Σab )αβ F ab F cdFcd λiα λiβ W −5 + 32 i(Σcd )αβ F ab Fca Fdb λiα λiβ W −5 −
 23                        27
    X X i k λjαXαk W −3 − 128
192 ij
                              i(Σab )αβ Xij X ij W ab λkα λkβ W −4 − 81 Xij X i k X j l X kl W −4 −
                                   5
5
8
  iXij X i k X j l λkα λlα W −5 + 32 Xij X ij Xkl X kl W −4 + 11
                                                              16
                                                                 iXij X ij Xkl λkα λlα W −5 +
1
  X W −2 ∇a ∇a X ij + 14 iλαi λjα W −3 ∇a ∇a X ij + 41 W −2 ∇a Xij ∇a X ij −
2 ij

 3
   X X ij F ab Fab W −4 − 38 iXij F ab Fab λiα λjα W −5 − 16
16 ij
                                                           3
                                                             iǫe abcd (Γe )αβ Xij Fab Fcd λiα λjβ W −5 −
3
  X X ij W −3 ∇a ∇a W − 23 Xij W −3 ∇a W ∇a X ij − 384
4 ij
                                                    37
                                                       iΦab ij (Σab )αβ X ij λkα λkβ W −3 −
 9
16
   i(Σab )αβ Xij X ij F ab λkαλkβ W −5 + 15
                                         8
                                            i(Γa )αβ λiα W −4 ∇b W ∇b W ∇a λiβ +

  iǫ cde (Σab )αβ λiα λiβ W −4 ∇c W ∇d ∇e W − 41 (Γa )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −5 ∇a ∇b W −
3 ab
8

5
8
  (Γa )αβ (Γb )ρλ λiα λiρ λjβ W −5 ∇a W ∇b λjλ − 38 (Γa )αβ (Γb )ρλ λiα λiρ λjβ W −5 ∇b W ∇a λjλ −

2λαi λiβ λjα W −5 ∇a W ∇a λjβ + 14 (Σab )αβ λiα λiρ λjρ W −5 ∇a W ∇b λjβ −
 9
   ǫ cdab (Γe )αβ Wcd Fab λiα λiρ λjβ λjρ W −5 + 21 (Σcd )αβ (Σab )ρλ W cd F ab λiα λiρ λjβ λjλ W −5 −
16 e

7
8
  (Σcd )αβ (Σab )ρλ W cdF ab λiα λiβ λjρ λjλ W −5 + 54 (Σab )αβ λiα λiρ λjβ W −5 ∇a W ∇b λjρ +

(Σab )αβ λiα λiβ λρj W −5 ∇a W ∇b λjρ + 49 iXij λiα λjα W −5 ∇a W ∇a W −

                                                       21
```

</details>

<a id="src-c24-p121"></a>

<details>
<summary>C24-p121 — PDF page 121: Supplement2.2.2: complete LOG scalar descendant; vector starts on121; Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p121: PDF page 121](https://arxiv.org/pdf/2311.00679v1#page=121) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
2
  (Γa )αβ Xij λiα λjβ λρk W −5 ∇a λkρ + 64
                                        55
                                           (Σab )αβ Xij W ab λiρ λjρ λkα λkβ W −5 +
17
32
   (Σab )αβ Xij W ab λiα λjρ λkβ λkρ W −5 +W −2 ∇a W ∇b ∇b ∇a W +W −2 ∇a W ∇a ∇b ∇b W +

W −2 ∇a ∇a W ∇b ∇b W + 12 W −2 ∇a ∇b W ∇a ∇b W + 89 Xij X ij W −4 ∇a W ∇a W +
11
   X X ij λαk λkβ λlα λlβ W −6 + 83 i(Σab )αβ Xij X i k F ab λjα λkβ W −5 − 16
64 ij
                                                                             9
                                                                               Xij X i k λjα λkβ λlα λlβ W −6 −
37
   X X λiα λjα λkβ λlβ W −6 + 58 (Γa )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −6 ∇a W ∇b W −
32 ij kl

 5
   ǫ abcd (Γe )αβ Fab Fcd λiα λiρ λjβ λjρ W −6 − 15
16 e                                             16
                                                    (Σab )αβ (Σcd )ρλ F ab F cdλiα λiβ λjρλjλ W −6 +
65
32
   (Σab )αβ Xij F ab λiρ λjρ λkαλkβ W −6+ 11
                                          64
                                             iW abα i (Σab )βρ X i j λjβ λkα λkρ W −4 +
39 β jρ
  λ λ λkβ λkρ λαi Xαi W −5 − 33
64 j
                                λβ λjρ λkβ λkα λiρ Xαi W −5 −W −3 ∇a W ∇b W ∇a ∇b W −
                             32 j

3
2
  W −3 ∇a W ∇a W ∇b ∇b W + 25
                           64
                              i(Γa )αβ λiα λiρ λjβ λjρ λλk W −6 ∇a λkλ −
 3
16
   W abα i (Σab )βρ λiλ λjα λjβ λkρλkλ W −5+ 16
                                              5
                                                i(Γa )αβ λiα λiρ λjβ λkρ λkλW −6 ∇a λjλ +
35
32
   i(Γa )αβ λiα λiρ λjρ λjλλkλ W −6 ∇a λkβ − 15
                                             32
                                                i(Γa )αβ λiα λiρ λjβ λjλλkρ W −6 ∇a λkλ +
35
64
   i(Γa )αβ λiα λρj λjλ λkρλkλ W −6 ∇a λiβ − 21 λαi λiβ λjαλjβ W −5 ∇a ∇a W +
3
8
  W −4 ∇a W ∇a W ∇b W ∇b W + 54 λαi λiβ λjαλjβ W −6 ∇a W ∇a W +
75
64
                                                105
   i(Σab )αβ W ab λiα λiρ λjβ λjλλkρ λkλ W −6 − 128 i(Σab )αβ W ab λiα λiβ λρj λjλ λkρ λkλ W −6 −
 5                                         7
16
   (Σab )αβ Xij F ab λiα λjρλkβ λkρ W −6 − 32 Xij Xkl λiα λjβ λkα λlβ W −6 −
 3
16
                                       33
   iXij λiα λjβ λkα λkρ λlβ λlρ W −7 + 32 iXij λiα λjα λβk λkρ λlβ λlρ W −7 −
45
32
   i(Σab )αβ F ab λiα λiβ λρj λjλ λkρ λkλ W −7 + 15
                                                 16
                                                    i(Σab )αβ F ab λiα λiρ λjβ λjλλkρ λkλ W −7 +

  λ λ λjα λjβ λρk λkλ λlρ λlλ W −8 − 21
21 α iβ
64 i
                                        λα λiβ λjα λjρλkβ λkλλlρ λlλ W −8
                                     32 i

           a
2.2.3     Hlog

                 3
 3
32
   W a b ∇b Y + 32 Y ∇b W ab + 23                          3
                                  ǫ debc Wbc ∇e1 ∇a Wde − 32
                               64 e1
                                                             ǫe1 debc Wbc ∇a ∇e1 Wde +
 567 bc
2048
     ǫ e1 de ∇a Wbc ∇e1 Wde + 38 ǫa e1 deb Wbc ∇e1 ∇c Wde + 83 ǫa e1 dbc Wbc ∇e ∇e1 Wde −
 1       bc                   43 a                          5 a
   ǫ
16 ee1 d
            Wbc ∇e ∇e1 W ad + 32 ǫ e1 dbc Wbc ∇e1 ∇e Wde − 32 ǫ e1 deb Wbc ∇c ∇e1 Wde −
 5
   ǫ cdb Wb a ∇e ∇e1 Wcd + 1743
32 ee1                     1024
                                                            3
                                ǫa e1 bcd ∇e1 Wbc ∇e Wde − 512 ǫebe1 cd ∇e W ab ∇e1 Wcd −

                                                       22
```

</details>

<a id="src-c24-p122"></a>

<details>
<summary>C24-p122 — PDF page 122: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p122: PDF page 122](https://arxiv.org/pdf/2311.00679v1#page=122) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 567 abcde                    3 a b                          3
2048
     ǫ     ∇e1 Wbc ∇e1 Wde − 256 ǫ e e1 d ∇e Wbc ∇e1 W dc − 32 F a b W −1 ∇b Y −
 3
32
   Y W −1 ∇b F ab − 15
                    16
                       i(Σa b )αβ Xiα ∇b Xβi + 29 ǫ debc Fbc W −1 ∇e1 ∇a Wde −
                                               64 e1

 3                               9 a
   ǫ debc Fbc W −1 ∇a ∇e1 Wde + 16
32 e1
                                   ǫ e1 dbc Fbc W −1 ∇e ∇e1 Wde + 18 ǫee1 d bc Fbc W −1 ∇e ∇e1 W ad +
 7 a                               1 a                              11
32
   ǫ e1 dbc Fbc W −1 ∇e1 ∇e Wde + 32 ǫ e1 deb Fbc W −1 ∇c ∇e1 Wde − 32 ǫee1 cdb Fb a W −1 ∇e ∇e1 Wcd +
3 a
4
  ǫ e1 bde Wde W −1 ∇e1 ∇c Fbc − 18 ǫa e1 bcd Wde W −1 ∇e ∇e1 Fbc + 64
                                                                    15 bc
                                                                       ǫ e1 de W −1 ∇a Fbc ∇e1 Wde +
3 a                              3 ab
4
  ǫ e1 bcd W −1 ∇e1 Fbc ∇e Wde + 32 ǫ e1 de W −1 ∇c Fbc ∇e1 Wde + 98 ǫebe1 cd W −1 ∇e F ab ∇e1 Wcd −
 1
   ǫ bcde Wde W −1 ∇e1 ∇a Fbc − 18 ǫa e1 bde Wde W −1 ∇c ∇e1 Fbc + 41 ǫa e1 bcd Wde W −1 ∇e1 ∇e Fbc +
16 e1

1
  ǫ bcd Wd a W −1 ∇e ∇e1 Fbc − 15
8 ee1
                                                               27 abc
                                  ǫ bcde W −1 ∇e1 Fbc ∇a Wde − 32
                               32 e1
                                                                  ǫ e1 d W −1 ∇e Fbc ∇e1 Wde +
15 a                               3
16
   ǫ e1 bde W −1 ∇e1 Fbc ∇c Wde + 32 F a b Y W −2 ∇b W +(Γb )αβ Xiα W −1 ∇b ∇a λiβ −
1
4
  (Γb )αβ Xiα W −1 ∇a ∇b λiβ − 38 (Γb )βα λiβ W −1 ∇b ∇a Xαi − 83 (Γb )βα λiβ W −1 ∇a ∇b Xαi −
3
4
  (Γb )βα W −1 ∇a λiβ ∇b Xαi − 34 (Γb )βα W −1 ∇b λiβ ∇a Xαi + 14 ǫabc de (Σbc )αβ Xiα W −1 ∇d ∇e λiβ −
3
4
  (Γa )αβ Xiα W −1 ∇b ∇b λiβ − 18 ǫabc de (Σbc )βα λiβ W −1 ∇d ∇e Xαi + 43 (Γa )βα λiβ W −1 ∇b ∇b Xαi −
3 abc
4
  ǫ de (Σbc )βα W −1∇d λiβ ∇e Xαi + 23 (Γa )βα W −1 ∇b λiβ ∇b Xαi − 14 W cd ∇b C a bcd −
3                     15                      9
8
  W bc Wbc ∇d W a d − 32 W a b W cd ∇b Wcd + 32 W a b Wcd ∇b W cd −
3
8
  W bc Wbd ∇d W a c + 38 W bc W a b ∇d Wcd + 83 Wb c Wdc ∇b W ad + 34 W ab Wc d ∇c Wbd +
3
8
  W ab W c b ∇d Wcd − 41 W bc ∇d Cbc a d − 14 W bd ∇c Cbc a d + 14 W bc ∇d C a bcd −
3
4
  iW a b α i ∇b Xαi + 27
                      16
                         iXiα ∇b W a bα i + 23 ∇c ∇c ∇b W ab − 15
                                                                8
                                                                  W −1 ∇b Wbc ∇c ∇a W +

2W a b W −1 ∇b ∇c ∇c W + 34 W −1∇a Wbc ∇b ∇c W + 32 W −1 ∇b W ab ∇c ∇c W +
3
4
  W −1 ∇c W a b ∇b ∇c W + 49 W −1 ∇c W a b ∇c ∇b W + 38 W −1 ∇b Wbc ∇a ∇c W +

3W −1 ∇b W ∇c ∇c W ab −2W −1 ∇c W ∇b ∇c W ab +2W −1∇b W ∇c ∇a Wbc +

W −1 ∇b W ∇a ∇c Wbc + 12 W −1 ∇c W ∇c ∇b W ab − 16
                                                 3
                                                   ǫe1 debc Fbc W −2 ∇a W ∇e1 Wde +
273
    ǫ debc Wbc W −1 ∇a W ∇e1 Wde − 39
256 e1
                                      ǫ debc Wbc W −1 ∇e1 W ∇a Wde −
                                   64 e1

73 a                                119 a
64
   ǫ e1 dbc Fbc W −2 ∇e1 W ∇e Wde − 128 ǫ e1 deb Fbc W −2 ∇c W ∇e1 Wde +
 71
    ǫ cdb Fb a W −2 ∇e W ∇e1 Wcd − 11
128 ee1                            64
                                      ǫa e1 deb Fbc W −2 ∇e1 W ∇c Wde +
 5 a                                  43
128
    ǫ e1 dbc Fbc W −2 ∇e W ∇e1 Wde − 128 ǫee1 d bc Fbc W −2 ∇e W ∇e1 W ad +

                                                       23
```

</details>

<a id="src-c24-p123"></a>

<details>
<summary>C24-p123 — PDF page 123: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p123: PDF page 123](https://arxiv.org/pdf/2311.00679v1#page=123) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3
   ǫ debc Wde Fbc W −2 ∇a ∇e1 W − 38 ǫe1 debc Wde Fbc W −2 ∇e1 ∇a W +
16 e1

 3
   ǫ bcde Wbc Wde W −1 ∇a ∇e1 W + 15
32 e1
                                     ǫ bcde Wbc Wde W −1 ∇e1 ∇a W −
                                  32 e1

 9 abcde                           1
16
   ǫ     Wbc Wde W −1 ∇e1 ∇e1 W + 16 ǫe1 bcde Wde W −2 ∇a W ∇e1 Fbc −
15 a                                 3 a
16
   ǫ e1 bde Wde W −2 ∇e1 W ∇c Fbc − 16 ǫ e1 bcd Wde W −2 ∇e W ∇e1 Fbc +
 1
   ǫ bcd Wd a W −2 ∇e W ∇e1 Fbc − 21 ǫa e1 bde Wde W −2 ∇c W ∇e1 Fbc −
16 ee1

5
  ǫ
8 ee1 b
        cd
           Wcd W −2 ∇e W ∇e1 F ab + 59
                                    64
                                       ǫa e1 dbc Wbc W −1 ∇e1 W ∇e Wde +
 85 a
128
    ǫ e1 deb Wbc W −1 ∇c W ∇e1 Wde − 35 ǫ cdb Wb a W −1 ∇e W ∇e1 Wcd +
                                     64 ee1

43 a                                53 a
64
   ǫ e1 deb Wbc W −1 ∇e1 W ∇c Wde + 128 ǫ e1 dbc Wbc W −1 ∇e W ∇e1 Wde +
19
   ǫ
64 ee1 d
         bc
            Wbc W −1 ∇e W ∇e1 W ad − 17
                                     64
                                                                  3 a
                                        ǫadebc Wbc ∇e1 ∇e1 Wde − 16 ǫ ee1 d b Wbc ∇e ∇e1 W dc +
 195 a
1024
     ǫ e1 bde ∇e1 Wbc ∇c Wde − 18 ǫe1 bcde Fbc Fde W −3 ∇e1 ∇a W − 21 ǫa e1 dbc Fbc W −3 ∇e1 W ∇e Fde −
 3
   ǫ debc Fbc W −2 ∇e1 W ∇a Wde − 14 ǫa e1 deb Wde Fbc W −2 ∇e1 ∇c W +
256 e1

1 a
2
  ǫ e1 dbc Wde Fbc W −2 ∇e ∇e1 W − 38 ǫee1 dbc Wd a Fbc W −2 ∇e ∇e1 W +
 1
   ǫ bcde Wde W −2 ∇e1 W ∇a Fbc − 92 W ab Wbc ∇d W dc + 32
32 e1
                                                         9
                                                           W bc Wbc ∇d W ad −
9
2
  W b c Wbd ∇c W ad − 21
                       4
                                              21 a
                         W a b Wcd ∇c W bd − 256 ǫ de bc λαi W −1 ∇d ∇e Wbcα i −

    ǫ de bc W −1 ∇d λαi ∇e Wbcα i − 18 Wbc α i ǫbcde e1 (Σde )α β W −1 ∇a ∇e1 λiβ +
255 a
512

1
4
  Wbc α i (Γb )α β W −1 ∇a ∇c λiβ − 14 W a b α i (Γc )α β W −1 ∇b ∇c λiβ + 18 Wbc α i ǫabc de W −1 ∇d ∇e λiα −
1
4
  Wbc α i ǫabcd e1 (Σde )α β W −1 ∇e1 ∇e λiβ + 14 Wbc α i ǫabde e1 (Σde )α β W −1 ∇c ∇e1 λiβ +
1
4
  Wbc α i (Γb )α β W −1 ∇c ∇a λiβ + 41 Wbc α i (Γa )α β W −1 ∇b ∇c λiβ + 14 Wb aα i ǫbcd ee1 (Σcd )α β W −1 ∇e ∇e1 λiβ −
1
4
  Wb aα i (Γb )α β W −1 ∇c ∇c λiβ − 41 W a b α i (Γc )α β W −1 ∇c ∇b λiβ − 512
                                                                            27 de
                                                                               ǫ e1 bc (Σde )βα λiβ W −1 ∇e1 ∇a Wbcα i −
1
8
  (Γb )βα λiβ W −1 ∇c ∇a Wbcα i + 18 (Γc )βα λiβ W −1 ∇c ∇b W a bα i − 256
                                                                        27 ad
                                                                           ǫ e1 bc (Σde )βα λiβ W −1 ∇e ∇e1 Wbcα i −
 27 ade                                       11
256
    ǫ e1 b (Σde )βα λiβ W −1 ∇e1 ∇c Wbcα i − 128 (Γa )βα λiβ W −1 ∇b ∇c Wbcα i −
1                                  11 cd
8
  (Γb )βα λiβ W −1 ∇a ∇c Wbcα i − 128 ǫ ee1 b (Σcd )βα λiβ W −1 ∇e ∇e1 Wb a α i +
1
8
  (Γb )βα λiβ W −1 ∇c ∇c Wb a α i + 81 (Γc )βα λiβ W −1 ∇b ∇c W a bα i −
 5 de                                          5 ad
512
    ǫ e1 bc (Σde )βα λiβ W −1 ∇a ∇e1 Wbcα i − 256 ǫ e1 bc (Σde )βα λiβ W −1 ∇e1 ∇e Wbcα i −
 5 ade                                        33 de
256
    ǫ e1 b (Σde )βα λiβ W −1 ∇c ∇e1 Wbcα i + 1024 ǫ e1 bc (Σde )βα W −1 ∇a λiβ ∇e1 Wbcα i +

                                                       24
```

</details>

<a id="src-c24-p124"></a>

<details>
<summary>C24-p124 — PDF page 124: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p124: PDF page 124](https://arxiv.org/pdf/2311.00679v1#page=124) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3
8
  (Γb )βα W −1 ∇a λiβ ∇c Wbcα i − 83 (Γc )βα W −1 ∇b λiβ ∇c W a bα i + 512
                                                                       33 ad
                                                                           ǫ e1 bc (Σde )βα W −1 ∇e1 λiβ ∇e Wbcα i +
 33 ade
512
    ǫ e1 b (Σde )βα W −1 ∇c λiβ ∇e1 Wbcα i − 129
                                             256
                                                 (Γa )βα W −1∇b λiβ ∇c Wbcα i +
3                                  63 cd
8
  (Γb )βα W −1 ∇c λiβ ∇a Wbcα i + 256 ǫ ee1 b (Σcd )βα W −1 ∇e λiβ ∇e1 Wb a α i −
3
8
  (Γb )βα W −1 ∇c λiβ ∇c Wb a α i − 83 (Γc )βα W −1 ∇c λiβ ∇b W a bα i +
 159 de
1024
     ǫ e1 bc (Σde )βα W −1 ∇e1 λiβ ∇a Wbcα i + 159
                                               512
                                                   ǫad e1 bc (Σde )βα W −1 ∇e λiβ ∇e1 Wbcα i +
159 ade
512
    ǫ e1 b (Σde )βα W −1 ∇e1 λiβ ∇c Wbcα i − 38 (Γb )αβ Xiα W −2 ∇a W ∇b λiβ −
3
4
  (Γb )αβ Xiα W −2 ∇b W ∇a λiβ + 11
                                 16
                                                                    5
                                    (Γb )βα λiβ Xαi W −2 ∇b ∇a W − 16 (Γb )βα λiβ Xαi W −2 ∇a ∇b W +
3
8
  (Γb )βα λiβ W −2 ∇a W ∇b Xαi + 34 (Γb )βα λiβ W −2 ∇b W ∇a Xαi − 83 ǫabc de (Σbc )αβ Xiα W −2 ∇d W ∇e λiβ +
9                                1 abc
8
  (Γa )αβ Xiα W −2 ∇b W ∇b λiβ + 16 ǫ de (Σbc )βα λiβ Xαi W −2 ∇d ∇e W −
3
8
  (Γa )βα λiβ Xαi W −2 ∇b ∇b W + 38 ǫabc de (Σbc )βα λiβ W −2 ∇d W ∇e Xαi −
9                                1 abcde
8
  (Γa )βα λiβ W −2 ∇b W ∇b Xαi + 12 ǫ    Φbcij Φde ij − 14 F cd W −1 ∇b C a bcd −
3
8
  W bc Fbc W −1 ∇d W a d − 83 W a d F bc W −1 ∇d Wbc + 153
                                                       32
                                                           Wcd F a b W −1 ∇b W cd −
 3
32
   W cd F a b W −1 ∇b Wcd − 38 Wd c Fbc W −1∇d W ab − 38 W ac F b c W −1 ∇d Wbd +
3
8
  W bd Fbc W −1 ∇c W a d + 83 W ad Fb c W −1 ∇b Wdc − 38 W bc F a b W −1 ∇d Wcd −
3
8
  Wc d F ab W −1 ∇c Wdb − 14 F bc W −1 ∇d Cbc a d − 41 F bd W −1 ∇c Cbc a d +
1 bc                   3                                 3
4
  F W −1 ∇d C a bcd − 32 i(Σa b )αβ Y λiα W −2 ∇b λiβ − 64 i(Σa b )αβ λiα λiβ W −2 ∇b Y +

Xij W −1∇b Φabij +Φa bij W −1 ∇b X ij +W −1 ∇c ∇c ∇b F ab − 32 W −2 ∇a W ∇b W ∇c Wbc +

F a b W −3 ∇b W ∇c ∇c W +2F a b W −3 ∇c W ∇c ∇b W −Fbc W −3 ∇b W ∇c ∇a W −

3W a b W −2 ∇b W ∇c ∇c W −W a b W −2 ∇c W ∇c ∇b W −2W a b W −2 ∇c W ∇b ∇c W +
3
2
  W −3 ∇c W ∇c W ∇b F ab −W −3 ∇a W ∇b W ∇c Fbc + 38 ǫe1 debc Wde Fbc W −3 ∇a W ∇e1 W −
 9
   ǫ bcde Wbc Wde W −2 ∇a W ∇e1 W + 38 ǫe1 bcde Fbc Fde W −4 ∇a W ∇e1 W −
16 e1

3 abcde
8
  ǫ     Fbc Fde W −4 ∇e1 W ∇e1 W − 83 ǫadebc Wde Fbc W −3 ∇e1 W ∇e1 W +
 9 abcde
16
   ǫ     Wbc Wde W −2 ∇e1 W ∇e1 W − 23
                                    64
                                       ǫadebc Fbc W −1 ∇e1 ∇e1 Wde −

   ǫ ee1 d b Fbc W −1 ∇e ∇e1 W dc + 34 ǫa e1 deb Wde Fbc W −3 ∇e1 W ∇c W −
 3 a
16

3 a                                   7 abcde
4
  ǫ e1 dbc Wde Fbc W −3 ∇e1 W ∇e W − 16 ǫ     Wde W −1 ∇e1 ∇e1 Fbc −

                                                     25
```

</details>

<a id="src-c24-p125"></a>

<details>
<summary>C24-p125 — PDF page 125: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p125: PDF page 125](https://arxiv.org/pdf/2311.00679v1#page=125) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
  ǫ
8 ee1 b
        cd
           Wcd W −1 ∇e ∇e1 F ab − 45
                                  64
                                     ǫabcde W −1 ∇e1 Fbc ∇e1 Wde + 32 F a b Fcd W −2 ∇b W cd−
3 ab
2
  F Fbc W −2 ∇d W dc + 43 F bc Fbc W −2 ∇d W ad − 32 F b c Fbd W −2 ∇c W ad −
3 a
2
  F b Fcd W −2 ∇c W bd + 41 F bc Fbc W −3 ∇d F ad + 38 W a d Fbc W −1 ∇d W bc −
3
8
  W a d Wbc W −1 ∇d F bc − 12 W b d Fbc W −2 ∇a F dc + 21 W a d Fbc W −2 ∇d F bc −
3
2
  Wbd F ab W −2 ∇c F cd + 41 Wcd F a b W −2 ∇b F cd+ 32 W bc Fbc W −2 ∇d F ad −

2W b d Fbc W −2 ∇c F ad −W b d Fbc W −2 ∇d F ac − 23 W ab Fbc W −2 ∇d F dc +
1
2
  W a d Fbc W −2 ∇b F dc − 39
                            8
                              Wbc F ab W −1 ∇d W dc + 38 W bc Fbc W −1 ∇d W ad −
39
 8
   W b d Fbc W −1 ∇c W ad + 83 W b d Fbc W −1 ∇d W ac + 39
                                                         8
                                                           Wcd F a b W −1 ∇c W db +
3
8
  W ab Fbc W −1 ∇d W dc − 39
                           8
                             W a d Fbc W −1 ∇b W dc −Wdc F a b W −2 ∇d F cb−
9
2
  W ad Wdc W −1 ∇b F bc + 75
                          32
                             W cd Wcd W −1 ∇b F ab − 29 W c d Wcb W −1 ∇d F ab +
3
4
  W a b Wdc W −1 ∇d F bc −F b c Fbd W −3 ∇c F ad −F ab Fbc W −3 ∇d F dc +
 5                                     1
32
   Wbc α i ǫabc de W −2 ∇d W ∇e λiα − 16 Wbc α i ǫabc de λiα W −2 ∇d ∇e W +
1                                                 5
8
  Wbc α i ǫbcde e1 (Σde )α β W −2 ∇a W ∇e1 λiβ − 16 Wbc α i (Γb )α β W −2 ∇a W ∇c λiβ +
 5
16
   W a b α i (Γc )α β W −2 ∇b W ∇c λiβ + 41 Wbc α i ǫabcd e1 (Σde )α β W −2 ∇e1 W ∇e λiβ −
1                                                 5
4
  Wbc α i ǫabde e1 (Σde )α β W −2 ∇c W ∇e1 λiβ − 16 Wbc α i (Γb )α β W −2 ∇c W ∇a λiβ −
 3                                      3
16
   Wbc α i (Γa )α β W −2 ∇b W ∇c λiβ − 16 Wb aα i ǫbcd ee1 (Σcd )α β W −2 ∇e W ∇e1 λiβ +
 5                                      5
16
   Wb aα i (Γb )α β W −2 ∇c W ∇c λiβ + 16 W a b α i (Γc )α β W −2 ∇c W ∇b λiβ +
 1                                                1
32
   Wbc α i ǫbcde e1 (Σde )α β W −2 ∇e1 W ∇a λiβ + 16 Wbc α i ǫabcd e1 (Σde )α β W −2 ∇e W ∇e1 λiβ −
 1                                                1
16
   Wbc α i ǫabde e1 (Σde )α β W −2 ∇e1 W ∇c λiβ + 16 Wbc α i ǫbcde e1 (Σde )α β λiβ W −2 ∇a ∇e1 W −
1
8
  Wbc α i (Γb )α β λiβ W −2 ∇a ∇c W + 18 W a b α i (Γc )α β λiβ W −2 ∇b ∇c W +
1
8
  Wbc α i ǫabcd e1 (Σde )α β λiβ W −2 ∇e1 ∇e W − 18 Wbc α i ǫabde e1 (Σde )α β λiβ W −2 ∇c ∇e1 W −
1
8
  Wbc α i (Γb )α β λiβ W −2 ∇c ∇a W − 18 Wbc α i (Γa )α β λiβ W −2 ∇b ∇c W −
1
8
  Wb aα i ǫbcd ee1 (Σcd )α β λiβ W −2 ∇e ∇e1 W + 81 Wb aα i (Γb )α β λiβ W −2 ∇c ∇c W +
1                                        83 de
8
  W a b α i (Γc )α β λiβ W −2 ∇c ∇b W + 6144 ǫ e1 bc (Σde )βα λiβ W −2 ∇a W ∇e1 Wbcα i −
 1                                    1
32
   (Γb )βα λiβ W −2 ∇a W ∇c Wbcα i + 32 (Γc )βα λiβ W −2 ∇b W ∇c W a bα i +

                                                      26
```

</details>

<a id="src-c24-p126"></a>

<details>
<summary>C24-p126 — PDF page 126: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p126: PDF page 126](https://arxiv.org/pdf/2311.00679v1#page=126) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 35 a                                   83 ad
3072
     ǫ de bc λαi W −2 ∇d W ∇e Wbcα i + 3072 ǫ e1 bc (Σde )βα λiβ W −2 ∇e1 W ∇e Wbcα i +
 83 ade                                          157
3072
     ǫ e1 b (Σde )βα λiβ W −2 ∇c W ∇e1 Wbcα i + 1536 (Γa )βα λiβ W −2 ∇b W ∇c Wbcα i −
 1                                    131 cd
32
   (Γb )βα λiβ W −2 ∇c W ∇a Wbcα i − 1536 ǫ ee1 b (Σcd )βα λiβ W −2 ∇e W ∇e1 Wb a α i +
 1                                     1
32
   (Γb )βα λiβ W −2 ∇c W ∇c Wb a α i + 32 (Γc )βα λiβ W −2 ∇c W ∇b W a bα i −
 179 de                                           179 ad
6144
     ǫ e1 bc (Σde )βα λiβ W −2 ∇e1 W ∇a Wbcα i − 3072 ǫ e1 bc (Σde )βα λiβ W −2 ∇e W ∇e1 Wbcα i −
 179 ade
3072
     ǫ e1 b (Σde )βα λiβ W −2 ∇e1 W ∇c Wbcα i − 34 (Γb )βα λiβ Xαi W −3 ∇a W ∇b W +
3                                   5
4
  (Γa )βα λiβ Xαi W −3 ∇b W ∇b W + 16 (Σbc )βα λiβ Xαi W −2 ∇a F bc +
3 a
8
  ǫ de bc (Γd )αβ Fbc Xiα W −2 ∇e λiβ − 38 ǫa de bc (Γd )βα Fbc λiβ W −2 ∇e Xαi −
27
16
   W a b Xiα W −1 ∇b λiα + 27
                           16
                                                      27 a
                              W a b λαi W −1 ∇b Xαi + 32 ǫ de bc (Γd )αβ Wbc Xiα W −1 ∇e λiβ −
27 a                                     1 a
32
   ǫ de bc (Γd )βα Wbc λiβ W −1 ∇e Xαi + 32 ǫ de bc (Γd )βα λiβ Xαi W −2 ∇e Fbc −
5
8
  (Σcb )βα λiβ Xαi W −2 ∇c F ab + 27                       27 a
                                     λα Xαi W −1 ∇b W ab − 32
                                  16 i
                                                              ǫ de bc (Γd )βα λiβ Xαi W −1 ∇e Wbc +
1
  X F a b W −3 ∇b X ij + 43 (Σa b )αβ Xij Xαi W −2 ∇b λjβ + 14 Xij X ij W −3 ∇b F ab −
2 ij

3
4
  (Σa b )βα Xij λiβ W −2 ∇b Xαj − 34 (Σa b )βα λjβ Xiα W −2 ∇b X ji + 61 C a bcd F cd W −2 ∇b W +
1
4
  W a d Wbc F bc W −2 ∇d W − 75
                             32
                                W cd Wcd F a b W −2 ∇b W − 14 W a b Wcd F bc W −2 ∇d W −
1
4
  W ad Wdc Fb c W −2 ∇b W − 14 W c b Wcd F ab W −2 ∇d W + 16 Cbc a d F bc W −2 ∇d W +
1
  C a F bd W −2 ∇c W − 61 C a bcd F bc W −2 ∇d W + 16 C a bcd W cd W −1 ∇b W −
6 bc d

1
4
  W bc W a b Wcd W −1 ∇d W − 14 W ab Wc d Wbd W −1 ∇c W + 16 Cbc a d W bc W −1 ∇d W +
1
  C a W bd W −1∇c W − 16 C a bcd W bc W −1∇d W + 48
6 bc d
                                                 5 abce1 e2
                                                    ǫ       Cbcde W de We1 e2 −
 121 adee1 e2
1024
     ǫ        W bc Wde We1 e2 Wbc + 563
                                    768
                                        ǫadee1 e2 W bc Wde We1 b We2 c + 25
                                                                         96
                                                                            ǫa b dee1 W bc Wde We1 e2 We2 c +
 5 adee1 e2                      5 abde1 e2                      5 cdee1 e2 ab
48
   ǫ        Cbcde W bc We1 e2 + 48 ǫ        Cbcde W ce We1 e2 − 96 ǫ       C cd Wee1 We2 b +
 283 cdee1 e2                       5 abde1 e2                        3 de
1536
     ǫ        W ab Wcd Wee1 We2 b + 24 ǫ       Cb c d e We1 c We2 e + 16 iǫ e1 bc (Σde )αβ Fbc λiα W −3 ∇e1 ∇a λiβ +
1
4
  i(Γb )αβ Fbc λiα W −3 ∇c ∇a λiβ + 18 iǫde e1 bc (Σde )αβ Fbc W −3 ∇a λiα ∇e1 λiβ −
1                                   25 de
4
  i(Γb )αβ Fbc W −3 ∇a λiα ∇c λiβ + 128 iǫ e1 bc (Σde )αβ Wbc λiα W −2 ∇e1 ∇a λiβ +
1                                   3 de
4
  i(Γb )αβ Wbc λiα W −2 ∇c ∇a λiβ + 32 iǫ e1 bc (Σde )αβ Wbc W −2 ∇a λiα ∇e1 λiβ −
3                                    5 de
8
  i(Γb )αβ Wbc W −2 ∇a λiα ∇c λiβ − 64 iǫ e1 bc (Σde )αβ λiα W −3 ∇e1 Fbc ∇a λiβ +

                                                      27
```

</details>

<a id="src-c24-p127"></a>

<details>
<summary>C24-p127 — PDF page 127: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p127: PDF page 127](https://arxiv.org/pdf/2311.00679v1#page=127) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                                   11 de
4
  i(Γb )αβ λiα W −3 ∇c Fbc ∇a λiβ + 256 iǫ e1 bc (Σde )αβ λiα W −2 ∇e1 Wbc ∇a λiβ +
3                                   139 debc
8
  i(Γb )αβ λiα W −2 ∇c Wbc ∇a λiβ + 1024 iǫ           αβ
                                             e1 (Σde ) λiα W
                                                             −2 a
                                                               ∇ Wbc ∇e1 λiβ −
1 a
8
  iǫ de bc Fbc W −3 ∇d λαi ∇e λiα − 12 iǫad e1 bc (Σde )αβ Fbc W −3 ∇e λiα ∇e1 λiβ −
1                                   1 a                                   3 a
4
  i(Γa )αβ Fbc W −3 ∇b λiα ∇c λiβ + 16 iǫ de bc Wbc λαi W −2 ∇d ∇e λiα − 16 iǫ de bc Wbc W −2 ∇d λαi ∇e λiα −
 5
128
    iǫde e1 bc (Σde )αβ Wbc λiα W −2 ∇a ∇e1 λiβ + 18 i(Γb )αβ Wbc λiα W −2 ∇a ∇c λiβ −
1
2
  i(Γc )αβ W a b λiα W −2 ∇b ∇c λiβ − 58 iǫad e1 bc (Σde )αβ Wbc λiα W −2 ∇e1 ∇e λiβ −
 5 ade
16
   iǫ e1 b (Σde )αβ Wbc λiα W −2 ∇c ∇e1 λiβ + 41 i(Γa )αβ Wbc λiα W −2 ∇b ∇c λiβ +
 9 cd
64
   iǫ ee1 b (Σcd )αβ Wb a λiα W −2 ∇e ∇e1 λiβ + 81 i(Γc )αβ W a b λiα W −2 ∇c ∇b λiβ −
3
8
  i(Γb )αβ Wb a λiα W −2 ∇c ∇c λiβ + 38 i(Γc )αβ W a b W −2 ∇c λiα ∇b λiβ −
15 ad                                          3 ade
16
   iǫ e1 bc (Σde )αβ Wbc W −2∇e λiα ∇e1 λiβ − 16 iǫ e1 b (Σde )αβ Wbc W −2 ∇e1 λiα ∇c λiβ −
 3 a bc
16
   iǫ d e λαi W −2 ∇d Wbc ∇e λiα − 83 i(Γc )αβ λiα W −2 ∇b W ab ∇c λiβ +
 7                                                 183 adebc
128
    iǫad ece1 (Σdb )αβ λiα W −2 ∇e W bc ∇e1 λiβ − 1024 iǫ    (Σde )αβ λiα W −2 ∇e1 Wbc ∇e1 λiβ +
3
8
  i(Γb )αβ λiα W −2 ∇c W ab ∇c λiβ − 129
                                     128
                                         iǫad e1 bc (Σde )αβ λiα W −2 ∇e1 Wbc ∇e λiβ −
 55 adeb                 −2 c              95 cd
512
    iǫ            αβ
         e1 (Σde ) λiα W   ∇ Wbc ∇e1 λiβ + 256 iǫ ebe1 (Σcd )αβ λiα W −2 ∇e W ab ∇e1 λiβ +
 1 debc
16
   iǫ            αβ
        e1 (Σde ) λiα W   ∇ Fbc ∇e1 λiβ + 41 i(Γc )αβ λiα W −3 ∇b F ab ∇c λiβ −
                        −3 a

 3 ad
16
   iǫ e1 bc (Σde )αβ λiα W −3 ∇e1 Fbc ∇e λiβ − 41 i(Γa )αβ λiα W −3 ∇b Fbc ∇c λiβ +
 9 cd
32
   iǫ ebe1 (Σcd )αβ λiα W −3 ∇e F ab ∇e1 λiβ + 14 i(Γb )αβ λiα W −3 ∇c F ab ∇c λiβ +
1
4
  i(Γc )αβ F a b λiα W −3 ∇c ∇b λiβ − 14 iǫad e1 bc (Σde )αβ Fbc λiα W −3 ∇e ∇e1 λiβ −
 3 ade                                         1 cd
16
   iǫ e1 b (Σde )αβ Fbc λiα W −3 ∇e1 ∇c λiβ − 16 iǫ ee1 b (Σcd )αβ Fb a λiα W −3 ∇e ∇e1 λiβ −
1
4
  i(Γb )αβ Fb a λiα W −3 ∇c ∇c λiβ + 14 i(Γc )αβ F a b λiα W −3 ∇b ∇c λiβ +
 1 de                                           1 ad
32
   iǫ e1 bc (Σde )αβ Fbc λiα W −3 ∇a ∇e1 λiβ − 16 iǫ e1 bc (Σde )αβ Fbc λiα W −3 ∇e1 ∇e λiβ −
 3 ad                                           1 de
16
   iǫ e1 bc (Σde )αβ Wbc λiα W −2 ∇e ∇e1 λiβ + 16 iǫ e1 bc (Σde )αβ λiα λiβ W −2∇e1 ∇a Wbc +
 19 ad                                          7 ade
128
    iǫ e1 bc (Σde )αβ λiα λiβ W −2 ∇e ∇e1 Wbc + 64 iǫ e1 b (Σde )αβ λiα λiβ W −2 ∇e1 ∇c Wbc −
 7 cd                                            1 de
64
   iǫ ee1 b (Σcd )αβ λiα λiβ W −2 ∇e ∇e1 W ab + 32 iǫ e1 bc (Σde )αβ λiα λiβ W −2 ∇a ∇e1 Wbc +
 5                                                5 ade
128
    iǫad e1 bc (Σde )αβ λiα λiβ W −2 ∇e1 ∇e Wbc + 64 iǫ e1 b (Σde )αβ λiα λiβ W −2 ∇c ∇e1 Wbc +

                                                       28
```

</details>

<a id="src-c24-p128"></a>

<details>
<summary>C24-p128 — PDF page 128: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p128: PDF page 128](https://arxiv.org/pdf/2311.00679v1#page=128) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                                      5 adbc
4
  i(Γc )αβ λiα W −3 ∇c F a b ∇b λiβ + 32 iǫ            αβ
                                              e1 (Σde ) λiα W
                                                              −3 e
                                                                ∇ Fbc ∇e1 λiβ +
 3 ade                                        123 adbc
16
   iǫ e1 b (Σde )αβ λiα W −3 ∇e1 Fbc ∇c λiβ + 512 iǫ            αβ
                                                       e1 (Σde ) λiα W
                                                                       −2 e
                                                                         ∇ Wbc ∇e1 λiβ +
 73 ade
256
    iǫ e1 b (Σde )αβ λiα W −2 ∇e1 Wbc ∇c λiβ − 78 iW a b α i Xαi W −1 ∇b W +
 3                                   23                             19
32
   i(Σa b )αβ Y λiα λiβ W −3 ∇b W + 1024 iǫabcde Wbc Wde α i Xαi + 512 i(Γa )αβ W bc Wbcαi Xβi −
 19 e1 bcde                            19
512
    iǫ      (Σe1 a )αβ Wbc Wdeαi Xβi + 256 iWb c Wdc α i ǫabdee1 (Σee1 )α β Xβi −
 19
256
                                  19
    iW ab Wbc α i (Γc )α β Xβi − 256 iWb c W a c α i (Γb )α β Xβi − 61 i(Γb )αβ Xij λiα W −3 ∇b ∇a λjβ −
 1
12
   i(Γb )αβ Xij λiα W −3 ∇a ∇b λjβ − 14 i(Γb )αβ Xij W −3 ∇a λiα ∇b λjβ − 61 i(Γb )αβ λiα λjβ W −3 ∇b ∇a X ij +
1
2
  i(Γb )αβ λiα W −3 ∇a X i j ∇b λjβ + 14 i(Γb )αβ λiα W −3 ∇b X i j ∇a λjβ +
1
4
  i(Γa )αβ Xij λiα W −3 ∇b ∇b λjβ − 14 iǫabc de (Σbc )αβ Xij W −3 ∇d λiα ∇e λjβ +
1
4
  i(Γa )αβ Xij W −3 ∇b λiα ∇b λjβ − 12
                                     1
                                       i(Γb )αβ λiα λjβ W −3 ∇a ∇b X ij +
1
4
  i(Γa )αβ λiα λjβ W −3 ∇b ∇b X ij + 14 iǫabc de (Σbc )αβ λiα W −3 ∇d X i j ∇e λjβ −
3
4
  i(Γa )αβ λiα W −3 ∇b X i j ∇b λjβ −Φa bij X ij W −2 ∇b W +W a b W −1 ∇c ∇c ∇b W −

F a b W −2 ∇c ∇c ∇b W −W −2 ∇b F ab ∇c ∇c W −W −2 ∇c F a b ∇c ∇b W −

W −2 ∇b W ∇c ∇c F ab −W −2 ∇c W ∇c ∇b F ab − 32 F a b W −4 ∇c W ∇c W ∇b W +

3W a b W −3 ∇c W ∇c W ∇b W + 18 ǫe1 debc Fbc W −3 ∇a W ∇e1 Fde − 18 ǫe1 debc Fbc W −3 ∇e1 W ∇a Fde +
1 adebc
2
  ǫ     Fbc W −3 ∇e1 W ∇e1 Fde + 12 ǫa ee1 d b Fbc W −3 ∇e W ∇e1 F dc +
 51 adebc                          7 a
256
    ǫ     Fbc W −2 ∇e1 W ∇e1 Wde + 16 ǫ ee1 d b Fbc W −2 ∇e W ∇e1 W dc +
13 abcde
32
   ǫ     Wde W −2 ∇e1 W ∇e1 Fbc + 38 ǫa ee1 b d Wdc W −2 ∇e W ∇e1 F bc −
117 adebc
256
    ǫ     Wbc W −1 ∇e1 W ∇e1 Wde − 12 ǫa ee1 d b Wbc W −1 ∇e W ∇e1 W dc +
1 a
4
  ǫ e1 deb Fbc W −3 ∇e1 W ∇c Fde − 14 ǫee1 d bc Fbc W −3 ∇e W ∇e1 F ad −
1 a
4
  ǫ e1 deb Fbc W −3 ∇c W ∇e1 Fde − 81 ǫa e1 dbc Wde Fbc W −2 ∇e1 ∇e W +
 3 adebc
16
   ǫ     Wde Fbc W −2 ∇e1 ∇e1 W + 14 ǫa ee1 db Wd c Fbc W −2 ∇e ∇e1 W −
1 a
8
  ǫ e1 deb Wde Fbc W −2 ∇c ∇e1 W − 43 F bc F a d Fbc W −4 ∇d W +3F ab F c b Fcd W −4 ∇d W −
1
4
  W bc W a d Fbc W −2 ∇d W −3W cdF a b Fcd W −3 ∇b W +6Wbd F bc F a c W −3 ∇d W −

3W c d F ab Fcb W −3 ∇d W +3W ac F b c Fbd W −3∇d W − 32 W a d F bc Fbc W −3 ∇d W −

                                                        29
```

</details>

<a id="src-c24-p129"></a>

<details>
<summary>C24-p129 — PDF page 129: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p129: PDF page 129](https://arxiv.org/pdf/2311.00679v1#page=129) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3W bc F a b Fcd W −3 ∇d W + 19
                            4
                               W cb Wcd F a b W −2 ∇d W + 19
                                                          4
                                                             W ad W b d Fbc W −2 ∇c W −
1
4
  W ac W b d Fbc W −2 ∇d W − 98 W dc W b d Fbc W −2 ∇a W − 32
                                                            3
                                                              Wbc α i ǫbcde e1 (Σde )α β λiβ W −3 ∇a W ∇e1 W +
3
8
  Wbc α i (Γb )α β λiβ W −3 ∇a W ∇c W − 38 W a b α i (Γc )α β λiβ W −3 ∇b W ∇c W −
 3                                                  3
16
   Wbc α i ǫabcd e1 (Σde )α β λiβ W −3 ∇e W ∇e1 W + 16 Wbc α i ǫabde e1 (Σde )α β λiβ W −3 ∇c W ∇e1 W −
 3                                        9                             53
16
   Wb aα i (Γb )α β λiβ W −3 ∇c W ∇c W − 32 F bc Wbc α i W −2 ∇a λiα + 512 F bc λαi W −2 ∇a Wbcα i −
 991                             107                           1
4096
     W bc Wbc α i W −1 ∇a λiα − 4096 W bc λαi W −1 ∇a Wbcα i + 32 Wbc α i λiα W −1 ∇a W bc +
 213
4096
     Wbc α i ǫbc e1 de (Γe1 )α β λiβ W −1 ∇a Wde + 18 W b c α i (Σbd )α β λiβ W −1 ∇a W cd+
163 b                          19
256
    F c λαi W −2∇c W a bα i − 256 F ab λαi W −2 ∇c Wbcα i − 12 F b c W a b α i W −2 ∇c λiα +

  F Wbc α i W −2 ∇c λiα − 81 (Σbc )αβ F bc W a dαi W −2 ∇d λiβ − 64
3 ab
4
                                                                  3 bcde
                                                                    ǫ         e1 αβ
                                                                         e1 (Γ ) Fbc Wdeαi W
                                                                                             −2 a i
                                                                                               ∇ λβ +
3
8
  (Σb d )αβ F bc Wcdαi W −2 ∇a λiβ − 41 (Σa d )αβ F bc Wbcαi W −2 ∇d λiβ +
1 a
8
  F b W cdα i (Σcd )α β W −2 ∇b λiβ + 41 F ab W c d α i (Σbc )α β W −2 ∇d λiβ −
1 b
4
  F c W adα i (Σbd )α β W −2 ∇c λiβ + 81 F bc W a d α i (Σbc )α β W −2 ∇d λiβ +
 1 abcde                                       1 bcde
32
   ǫ     Fbc Wde α i (Γe1 )α β W −2 ∇e1 λiβ − 32 ǫ              α    a β
                                                      e1 Fbc Wde i (Γ )α W
                                                                           −2 e1 i
                                                                             ∇ λβ −
1 abd
8
  ǫ ee1 (Γe )αβ Fb c Wdcαi W −2 ∇e1 λiβ − 12 (Σad )αβ F b c Wdbαi W −2 ∇c λiβ −
1
2
  (Σb a )αβ F bc Wcdαi W −2 ∇d λiβ − 14 (Σc d )αβ F ab Wbcαi W −2 ∇d λiβ −
 83
    ǫ bcde (Γe1 )βα Fbc λiβ W −2 ∇a Wdeα i − 203
3072 e1                                      384
                                                 (Σd b )βα F bc λiβ W −2 ∇a Wdcα i −
163
768
    (Σa d )βα F bc λiβ W −2 ∇d Wbcα i − 163
                                        768
                                            (Σcd )βα F a b λiβ W −2 ∇b Wcdα i +
221                                      19
384
    (Σbd )βα Fbc λiβ W −2 ∇c W a dα i − 384 (Σc b )βα F ab λiβ W −2 ∇d Wcdα i −
403                                       3 abcde
768
    (Σbc )βα F bc λiβ W −2 ∇d W a dα i + 128 ǫ    (Γe1 )βα Fbc λiβ W −2 ∇e1 Wdeα i −
 1
   ǫ bcde (Γa )βα Fbc λiβ W −2 ∇e1 Wdeα i + 101
16 e1                                       768
                                                ǫa ee1 bd (Γe )βα Fb c λiβ W −2 ∇e1 Wdcα i −
 19
384
    (Σa b )βα F bc λiβ W −2 ∇d Wcdα i − 221
                                        384
                                            (Σbd )βα F bc λiβ W −2 ∇d W a cα i +
163
384
    (Σc d )βα F ab λiβ W −2 ∇d Wcbα i − 163
                                        384
                                            (Σad )βα F b c λiβ W −2 ∇c Wdbα i −
1021                               893                             581
2048
     W b c W a b α i W −1 ∇c λiα + 2048 W ab Wbc α i W −1 ∇c λiα + 2048 W b c λαi W −1∇c W a bα i −
 69
2048
     W ab λαi W −1 ∇c Wbcα i + 1283
                               2048
                                    (Σbc )αβ W bc W a dαi W −1 ∇d λiβ −
 13 bcde                     −1 a i   13
2048
     ǫ        e1 αβ
         e1 (Γ ) Wbc Wdeαi W   ∇ λβ + 256 (Σb d )αβ W bc Wcdαi W −1 ∇a λiβ −

                                                       30
```

</details>

<a id="src-c24-p130"></a>

<details>
<summary>C24-p130 — PDF page 130: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p130: PDF page 130](https://arxiv.org/pdf/2311.00679v1#page=130) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 511
2048
     (Σa d )αβ W bc Wbcαi W −1 ∇d λiβ + 41 W a b W cdα i (Σcd )α β W −1 ∇b λiβ +
193
512
    W ab W c d α i (Σbc )α β W −1 ∇d λiβ − 12 W b c W adα i (Σbd )α β W −1 ∇c λiβ +
 193                                         449 abcde
1024
     W bc W a d α i (Σbc )α β W −1 ∇d λiβ + 8192 ǫ     Wbc Wde α i (Γe1 )α β W −1 ∇e1 λiβ −
 449 bcde                      −1 e1 i   449 abd
8192
     ǫ              α    a β
          e1 Wbc Wde i (Γ )α W   ∇ λβ − 2048 ǫ ee1 (Γe )αβ Wb c Wdcαi W −1 ∇e1 λiβ −
 511                                     385
1024
     (Σad )αβ W b c Wdbαi W −1 ∇c λiβ − 1024 (Σb a )αβ W bc Wcdαi W −1 ∇d λiβ +
225                                      449
512
    (Σbd )αβ W bc Wc a αi W −1 ∇d λiβ − 1024 (Σc d )αβ W ab Wbcαi W −1 ∇d λiβ −
 875
     ǫ bcde (Γe1 )βα Wbc λiβ W −1 ∇a Wdeα i − 1643
24576 e1                                      3072
                                                   (Σd b )βα W bc λiβ W −1 ∇a Wdcα i −
1047
2048
     (Σa d )βα W bc λiβ W −1 ∇d Wbcα i − 1047
                                         2048
                                              (Σcd )βα W a b λiβ W −1 ∇b Wcdα i +
 489                                      23
1024
     (Σbd )βα Wbc λiβ W −1 ∇c W a dα i − 1024 (Σc b )βα W ab λiβ W −1∇d Wcdα i +
 489                                       1 abcde
2048
     (Σbc )βα W bc λiβ W −1 ∇d W a dα i + 16 ǫ     (Γe1 )βα Wbc λiβ W −1 ∇e1 Wdeα i −
 3                                          233 a
   ǫ bcde (Γa )βα Wbc λiβ W −1 ∇e1 Wdeα i + 2048
32 e1
                                                 ǫ ee1 bd (Γe )βα Wb c λiβ W −1 ∇e1 Wdcα i −
 23                                       489
1024
     (Σa b )βα W bc λiβ W −1 ∇d Wcdα i − 1024 (Σbd )βα W bc λiβ W −1 ∇d W a cα i +
1047
1024
     (Σc d )βα W ab λiβ W −1 ∇d Wcbα i − 1047
                                         1024
                                              (Σad )βα W b c λiβ W −1 ∇c Wdbα i +
 1                                     9
12
   i(Σcd )αβ C a bcd λiα W −2 ∇b λiβ + 16 i(Σbc )αβ W bc W a d λiα W −2 ∇d λiβ +
15
16
   i(Σa d )αβ W bc Wbc λiα W −2 ∇d λiβ − 98 i(Σc b )αβ W ab Wcd λiα W −2 ∇d λiβ −
259
256
    i(Σbd )αβ W bc W a c λiα W −2 ∇d λiβ + 94 i(Σa b )αβ W bc Wcd λiα W −2 ∇d λiβ +
 1
12
   i(Σbc )αβ Cbc a d λiα W −2 ∇d λiβ − 317
                                       256
                                           i(Σc d )αβ W ab Wcb λiα W −2 ∇d λiβ +
 1                                      1
12
   i(Σbd )αβ Cbc a d λiα W −2 ∇c λiβ − 12 i(Σbc )αβ C a bcd λiα W −2 ∇d λiβ −
 5
32
   W a b α i (Σcd )α β λiβ W −1 ∇b W cd − 85 W b c α i (Σbd )α β λiβ W −1 ∇d W ac +
 5                                       5
16
   W bcα i (Σbc )α β λiβ W −1 ∇d W ad + 16 Wbc α i (Σa d )α β λiβ W −1 ∇d W bc +
5                                         5
8
  W b c α i (Σa b )α β λiβ W −1 ∇d W cd− 32 Wbc α i ǫabc e1 d (Γe )α β λiβ W −1 ∇e1 Wde +
 3                             3
32
   Wbc α i λiα W −1 ∇b W ac − 64 Wbc α i ǫab e1 de (Γe1 )α β λiβ W −1 ∇c Wde +
 3                                        3
16
   W b c α i (Σbd )α β λiβ W −1 ∇c W ad + 16 Wbc α i (Σa d )α β λiβ W −1 ∇b W cd +
 149                                                9
2048
     Wb aα i ǫb ee1 cd (Γe )α β λiβ W −1 ∇e1 Wcd + 16 W a d α i (Σbc )α β λiβ W −2 ∇d F bc −
 3                             1
32
   Wbc α i λiα W −2 ∇a F bc + 64 Wde α i ǫde e1 bc (Γe1 )α β λiβ W −2 ∇a Fbc +

                                                       31
```

</details>

<a id="src-c24-p131"></a>

<details>
<summary>C24-p131 — PDF page 131: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p131: PDF page 131](https://arxiv.org/pdf/2311.00679v1#page=131) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
8
  W d b α i (Σdc )α β λiβ W −2 ∇a F bc − 81 W c b α i (Σcd )α β λiβ W −2 ∇d F ab +
 1                                       1
16
   W cdα i (Σcd )α β λiβ W −2 ∇b F ab + 16 Wbc α i (Σa d )α β λiβ W −2 ∇d F bc +
1                                          1
8
  W d b α i (Σa d )α β λiβ W −2 ∇c F bc − 32 Wde α i ǫade e1 b (Γc )α β λiβ W −2 ∇e1 Fbc +
 5                            1
16
   Wcb α i λiα W −2 ∇c F ab − 32 Wde α i ǫad e1 bc (Γe1 )α β λiβ W −2 ∇e Fbc +
1
8
  W c d α i (Σcb )α β λiβ W −2 ∇d F ab + 81 Wdb α i (Σa c )α β λiβ W −2 ∇d F bc −
 3                               1
16
   W a b α i λiα W −2 ∇c F bc + 32 Wd aα i ǫd ee1 bc (Γe )α β λiβ W −2 ∇e1 Fbc −
1
8
  W adα i (Σdb )α β λiβ W −2 ∇c F bc − 81 W a b α i (Σdc )α β λiβ W −2 ∇d F bc +
3 a                                          27
4
  ǫ de bc (Γd )βα Fbc λiβ Xαi W −3 ∇e W    − 16 W a b λαi Xαi W −2 ∇b W +
27 a                                        31 a
32
   ǫ de bc (Γd )βα Wbc λiβ Xαi W −2 ∇e W − 768 ǫ e1 bde (Γc )βα Fbc λiβ W −2 ∇e1 Wdeα i +
 91                                          91 a
    ǫ bcd (Γe )βα Fb a λiβ W −2∇e1 Wcdα i + 1536
1536 ee1
                                                 ǫ e1 bcd (Γe1 )βα Fbc λiβ W −2 ∇e Wdeα i −
 1 bcd
16
   ǫ ee1 (Γe )αβ Fbc Wd a αi W −2 ∇e1 λiβ − 41 (Σbd )αβ Fbc W a dαi W −2∇c λiβ +
1
4
  (Σc d )αβ F ab Wcbαi W −2 ∇d λiβ − 18 (Σcd )αβ F a b Wcdαi W −2 ∇b λiβ −
 1 abde      c αβ           −2 e1 i   1 abcd      e1 αβ          −2 e i
16
   ǫ    e1 (Γ ) Fbc Wdeαi W   ∇ λβ − 16 ǫ    e1 (Γ ) Fbc Wdeαi W   ∇ λβ −
1                                     29 a
4
  (Σb c )αβ F ab Wcdαi W −2 ∇d λiβ − 1536 ǫ e1 bde (Γe1 )βα Fbc λiβ W −2 ∇c Wdeα i −
 29                                            63 bcde
    ǫ bcd (Γe )βα Fbc λiβ W −2 ∇e1 Wd a α i + 8192
1536 ee1
                                                   ǫ        a αβ
                                                       e1 (Γ ) Wbc Wdeαi W
                                                                           −1 e1 i
                                                                             ∇ λβ +
 63                                        63
1024
     W ab Wb cα i (Σcd )α β W −1 ∇d λiβ + 1024 W bc Wb aα i (Σcd )α β W −1 ∇d λiβ −
 63                                        63 abcd
1024
     W bc Wb dα i (Σcd )α β W −1 ∇a λiβ − 4096 ǫ             α    e β
                                                   e1 Wbc Wde i (Γ )α W
                                                                        −1 e1 i
                                                                          ∇ λβ −
 63 bcd                                         63 abde
4096
     ǫ ee1 Wbc Wd aα i (Γe )α β W −1 ∇e1 λiβ + 4096 ǫ             α    e1 β
                                                        e1 Wbc Wde i (Γ )α W
                                                                             −1 c i
                                                                               ∇ λβ −
 407 a                                           535
2048
     ǫ e1 bde (Γc )βα Wbc λiβ W −1 ∇e1 Wdeα i + 4096 ǫee1 bcd (Γe )βα Wb a λiβ W −1 ∇e1 Wcdα i +
 535 a                                            1
4096
     ǫ e1 bcd (Γe1 )βα Wbc λiβ W −1 ∇e Wdeα i + 4096 ǫbcd ee1 (Γe )αβ Wbc Wd a αi W −1 ∇e1 λiβ +
  1                                       1
1024
     (Σbd )αβ Wbc W a dαi W −1 ∇c λiβ − 1024 (Σc d )αβ W ab Wcbαi W −1 ∇d λiβ +
  1                                       1
2048
     (Σcd )αβ W a b Wcdαi W −1 ∇b λiβ + 4096 ǫabde e1 (Γc )αβ Wbc Wdeαi W −1 ∇e1 λiβ +
  1                                             1
4096
     ǫabcd e1 (Γe1 )αβ Wbc Wdeαi W −1 ∇e λiβ + 1024 (Σb c )αβ W ab Wcdαi W −1 ∇d λiβ +
 279 a                                           279
4096
     ǫ e1 bde (Γe1 )βα Wbc λiβ W −1 ∇c Wdeα i + 4096 ǫee1 bcd (Γe )βα Wbc λiβ W −1 ∇e1 Wd a α i −
 149                                                149
4096
     Wbc α i ǫbc e1 de (Γa )α β λiβ W −1 ∇e1 Wde − 2048 Wbc α i ǫbc ee1 d (Γe )α β λiβ W −1 ∇e1 W ad −

                                                        32
```

</details>

<a id="src-c24-p132"></a>

<details>
<summary>C24-p132 — PDF page 132: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p132: PDF page 132](https://arxiv.org/pdf/2311.00679v1#page=132) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                               11
4
  W a b α i X i j W −2 ∇b λjα + 24 Xji λjα W −2 ∇b W a bα i +iΦa bij λiα W −2 ∇b λjα +

iΦb cij (Σa b )αβ λiα W −2∇c λjβ + 12 iλαi λjα W −2 ∇b Φabij − 72
                                                                5 a
                                                                  iǫ becd (Γb )αβ λiα λjβ W −2 ∇e Φcdij −
3
  X X ij F a b W −4 ∇b W + 32 (Σa b )βα Xij λiβ Xαj W −3 ∇b W + 24
4 ij
                                                                1 abce1 e2
                                                                   ǫ       Cbcde F de Fe1 e2 W −2 +
 5 ae1 e2 de                             31 abcde
96
   ǫ         We1 e2 Wbc F bc Fde W −2 + 384 ǫ     W e1e2 We1 e2 Fbc Fde W −2 +
 5 ae1 e2 de                              5 a e1 de
96
   ǫ         We1 b We2 c F bc Fde W −2 + 48 ǫ b     We1 e2 We2 c F bc Fde W −2 +
 1 adee1 e2                          1 abde1 e2                           1 cdee1 e2 ab
24
   ǫ        Cbcde F bc Fe1 e2 W −2+ 24 ǫ        Cbcde F ce Fe1 e2 W −2 − 48 ǫ       C cd Fee1 Fe2 b W −2 +
139 e1 e2 bcd                            17 e1 e2 bcd
192
    ǫ         W ae We1 e2 Fbc Fde W −2 − 48 ǫ         We1 a We2 e Fbc Fde W −2 +
 25 e2 bcde                              1 ae2 bcd
192
    ǫ       W ae1 We2 e1 Fbc Fde W −2 + 32 ǫ       W e1 e We2 e1 Fbc Fde W −2 +
 1 abde1 e2                              7 ae1 e2 bd
12
   ǫ        Cb c d e Fe1 c Fe2 e W −2 + 12 ǫ         We1 c We2 e Fbc Fde W −2 −
 1 ae1 e2 bd                             5 abce1 e2
24
   ǫ         W ce We1 e2 Fbc Fde W −2 + 48 ǫ        Cbcde We1 e2 F de W −1 +
 53 adee1 e2                             7 ae1 e2 bc
384
    ǫ        Wde We1 e2 Wbc F bc W −1 + 384 ǫ        W de We1 e2 Wde Fbc W −1 +
221 adee1 e2                              53 a dee1
384
    ǫ        Wde We1 b We2 c F bc W −1 + 192 ǫ b    Wde We1 e2 We2 c F bc W −1 +
 5 adee1 e2                           5 abce1 e2                           5 ae1 e2 bc
48
   ǫ        Cbcde We1 e2 F bc W −1 + 128 ǫ       Cbcde W de Fe1 e2 W −1 + 96 ǫ         W de We1 d We2 e Fbc W −1 +
 17 a e1 bc                               13 bce2 ee1
192
    ǫ d     W de We1 e2 We2 e Fbc W −1 − 192 ǫ        Cbc ad We2 d Fee1 W −1 +
 27 ee1 e2 bc
128
    ǫ         W ad Wee1 We2 d Fbc W −1 + 13
                                         96
                                            ǫabde1 e2 Cbcde We1 e2 F ce W −1 +
 17 adee1 e2                          11 bce1 e2 e
384
    ǫ        Cbcde W bc Fe1 e2 W −1 + 192 ǫ        Cbc ad We1 e2 Fed W −1 +
 95 dee1 e2 b                             11 dee1 e2 b
384
    ǫ         W ac Wde We1 e2 Fbc W −1 + 384 ǫ         Wde We1 a We2 c Fbc W −1 +
307 aee1 e2 b                             1 cde2 ee1 ab
384
    ǫ         W dc Wee1 We2 d Fbc W −1 − 16 ǫ       C cd We2 b Fee1 W −1 +
 7 abde2 e1                              1 abde1 e2
24
   ǫ        Cb c d e We2 c Fe1 e W −1 + 96 ǫ        Cbcde W ce Fe1 e2 W −1 −
1 α
 iλ W −3 ∇a W ∇b ∇b λiα + 14 iλαi W −3 ∇b W ∇b ∇a λiα +i(Σbc )αβ λiα W −3 ∇b W ∇c ∇a λiβ −
4 i

1 α
 iλ W −3 ∇b λiα ∇b ∇a W − 12 i(Σbc )αβ λiα W −3 ∇b λiβ ∇c ∇a W − 41 iW −3 ∇b W ∇a λαi ∇b λiα +
4 i

3
2
  i(Σbc )αβ W −3 ∇b W ∇a λiα ∇c λiβ − 21 i(Σa b )αβ λiα W −3 ∇c W ∇b ∇c λiβ −
1
2
  i(Σa b )αβ λiα W −3 ∇b W ∇c ∇c λiβ − 25 i(Σa b )αβ λiα W −3∇c W ∇c ∇b λiβ +
1
2
  i(Σbc )αβ λiα W −3 ∇b W ∇a ∇c λiβ − 23 i(Σa b )αβ λiα W −3 ∇b λiβ ∇c ∇c W +
1 α
 iλ W −3 ∇a λiα ∇b ∇b W −i(Σa b )αβ λiα W −3 ∇c λiβ ∇c ∇b W −3i(Σa b )αβ W −3 ∇c W ∇b λiα ∇c λiβ +
4 i

                                                       33
```

</details>

<a id="src-c24-p133"></a>

<details>
<summary>C24-p133 — PDF page 133: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p133: PDF page 133](https://arxiv.org/pdf/2311.00679v1#page=133) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
2
  i(Σa b )αβ W −3 ∇b W ∇c λiα ∇c λiβ + 41 iǫa bcde (Γb )αβ W −3 ∇c W ∇d λiα ∇e λiβ −
 9 de
64
   iǫ e1 bc (Σde )αβ Fbc λiα W −4 ∇e1 W ∇a λiβ − 34 i(Γb )αβ Fbc λiα W −4 ∇c W ∇a λiβ −
 9 de                                             15 de
32
   iǫ e1 bc (Σde )αβ Fbc λiα W −4 ∇a W ∇e1 λiβ − 256 iǫ e1 bc (Σde )αβ Wbc λiα λiβ W −3 ∇e1 ∇a W −
 9                                                   21 de
256
    iǫde e1 bc (Σde )αβ Wbc λiα W −3 ∇a W ∇e1 λiβ − 128 iǫ e1 bc (Σde )αβ Wbc λiα W −3 ∇e1 W ∇a λiβ −
3
4
  i(Γb )αβ Wbc λiα W −3 ∇c W ∇a λiβ − 34 i(Γc )αβ F a b λiα W −4 ∇b W ∇c λiβ −
3 ade                                          9 cd
4
  iǫ e1 b (Σde )αβ Fbc λiα W −4 ∇c W ∇e1 λiβ + 16 iǫ ee1 b (Σcd )αβ Fb a λiα W −4 ∇e W ∇e1 λiβ +
3
4
  i(Γb )αβ Fb a λiα W −4 ∇c W ∇c λiβ + 83 iǫa de bc Fbc λαi W −4 ∇d W ∇e λiα +
 9 d
16
   iǫ ee1 bc (Σd a )αβ Fbc λiα W −4 ∇e W ∇e1 λiβ + 34 iǫad e1 bc (Σde )αβ Fbc λiα W −4 ∇e W ∇e1 λiβ +

   iǫ e1 b (Σde )αβ Fbc λiα W −4 ∇e1 W ∇c λiβ − 43 i(Γc )αβ F a b λiα W −4 ∇c W ∇b λiβ +
 3 ade
32

3
4
  i(Γa )αβ Fbc λiα W −4 ∇b W ∇c λiβ + 45
                                      32
                                         iǫad e1 bc (Σde )αβ Fbc λiα W −4 ∇e1 W ∇e λiβ +
3 a                                    27 de
8
  iǫ de bc Wbc λαi W −3 ∇d W ∇e λiα + 256 iǫ e1 bc (Σde )αβ Wbc λiα λiβ W −3 ∇a ∇e1 W +
 3 ad                                              3 adebc
32
   iǫ ee1 b (Σd c )αβ Wbc λiα λiβ W −3 ∇e ∇e1 W − 64 iǫ    (Σde )αβ Wbc λiα λiβ W −3 ∇e1 ∇e1 W +
 33 ad                                             23 ade
128
    iǫ e1 bc (Σde )αβ Wbc λiα λiβ W −3 ∇e1 ∇e W + 128 iǫ e1 b (Σde )αβ Wbc λiα λiβ W −3 ∇c ∇e1 W −
 9 cd
64
   iǫ ee1 b (Σcd )αβ Wb a λiα λiβ W −3 ∇e ∇e1 W + 34 i(Γc )αβ W a b λiα W −3 ∇b W ∇c λiβ +
165 ad                                             3 ade
128
    iǫ e1 bc (Σde )αβ Wbc λiα W −3 ∇e1 W ∇e λiβ + 16 iǫ e1 b (Σde )αβ Wbc λiα W −3 ∇c W ∇e1 λiβ +
 33 cd
128
    iǫ ee1 b (Σcd )αβ Wb a λiα W −3 ∇e W ∇e1 λiβ + 34 i(Γb )αβ Wb a λiα W −3 ∇c W ∇c λiβ +
 81 d
128
    iǫ ee1 bc (Σd a )αβ Wbc λiα W −3 ∇e W ∇e1 λiβ + 15
                                                    16
                                                       iǫad e1 bc (Σde )αβ Wbc λiα W −3 ∇e W ∇e1 λiβ +
 75 ade
128
    iǫ e1 b (Σde )αβ Wbc λiα W −3 ∇e1 W ∇c λiβ − 41
                                                 64
                                                    iǫad ee1 c (Σdb )αβ λiα λiβ W −3 ∇e W ∇e1 W bc +
 9 adebc                                        9 de
64
   iǫ    (Σde )αβ λiα λiβ W −3 ∇e1 W ∇e1 Wbc − 64 iǫ e1 bc (Σde )αβ λiα λiβ W −3 ∇e1 W ∇a Wbc −
 17 ad
128
    iǫ e1 bc (Σde )αβ λiα λiβ W −3 ∇e1 W ∇e Wbc − 11
                                                  64
                                                     iǫade e1 b (Σde )αβ λiα λiβ W −3 ∇c W ∇e1 Wbc −
23 cd                                              3 de
64
   iǫ ee1 b (Σcd )αβ λiα λiβ W −3 ∇e W ∇e1 W ab − 16 iǫ e1 bc (Σde )αβ Fbc λiα λiβ W −4 ∇e1 ∇a W +
 3 de                                             3 ade
32
   iǫ e1 bc (Σde )αβ λiα λiβ W −4 ∇a W ∇e1 Fbc − 16 iǫ e1 b (Σde )αβ λiα λiβ W −4 ∇c W ∇e1 Fbc −
3 cd                                              5
8
  iǫ ee1 b (Σcd )αβ λiα λiβ W −4 ∇e W ∇e1 F ab + 128 iǫad e1 bc (Σde )αβ λiα λiβ W −3 ∇e W ∇e1 Wbc −
 7 ade                                           3 abcde1
64
   iǫ e1 b (Σde )αβ λiα λiβ W −3 ∇e1 W ∇c Wbc − 16 iǫ     Wbc Wd eα i We1 eα i +
 9 bcdee1                          9 abdee1                         77 abcde
32
   iǫ     Wbc Wde α i We1 a α i − 16 iǫ     Wb c Wde α i We1 cα i + 256 iǫ   Fbc Wde α i Xαi W −1 +

                                                      34
```

</details>

<a id="src-c24-p134"></a>

<details>
<summary>C24-p134 — PDF page 134: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p134: PDF page 134](https://arxiv.org/pdf/2311.00679v1#page=134) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1                                  1
128
    i(Γa )αβ F bc Wbcαi Xβi W −1 − 128 iǫe1 bcde (Σe1 a )αβ Fbc Wdeαi Xβi W −1 +
 1                                              1
64
   iFb c Wdc α i ǫabdee1 (Σee1 )α β Xβi W −1 − 64 iF ab Wbc α i (Γc )α β Xβi W −1 −
 1
64
   iFb c W a c α i (Γb )α β Xβi W −1 + 38 i(Γb )αβ Xij λiα λjβ W −4 ∇b ∇a W +
3
4
  i(Γb )αβ Xij λiα W −4 ∇a W ∇b λjβ + 34 i(Γb )αβ Xij λiα W −4 ∇b W ∇a λjβ +
3
8
  i(Γb )αβ λiα λjβ W −4 ∇a W ∇b X ij + 34 i(Γb )αβ λiα λjβ W −4 ∇b W ∇a X ij −
3
8
  i(Γa )αβ Xij λiα λjβ W −4 ∇b ∇b W + 34 iǫabc de (Σbc )αβ Xij λiα W −4 ∇d W ∇e λjβ −
3
2
  i(Γa )αβ Xij λiα W −4 ∇b W ∇b λjβ − 89 i(Γa )αβ λiα λjβ W −4 ∇b W ∇b X ij −
 3 abcde
16
   ǫ     Φbcji (Σde )βα λjβ Xαi W −1 − 58 Φb a ji (Γb )βα λjβ Xαi W −1 +W −3∇c W ∇b W ∇c F ab −

3W −2 ∇c W ∇b W ∇c W ab − 14 ǫadebc Fbc W −2 ∇e1 ∇e1 Fde − 81 ǫabcde W −2 ∇e1 Fbc ∇e1 Fde −
 3 adee1 e2 bc                     3 adee1 e2 bc
64
   ǫ       F Fde Fe1 e2 Fbc W −4 + 16 ǫ      F Fde Fe1 b Fe2 c W −4 +
 3 cdee1 e2 ab                     3 ae1 e2 de
32
   ǫ       F Fcd Fee1 Fe2 b W −4 − 16 ǫ        We1 e2 F bc Fde Fbc W −3 +
3 ae1 e2 de
8
  ǫ         We1 e2 F bc Fdb Fec W −3 + 83 ǫbcdee1 W ae2 Fbc Fde Fe1 e2 W −3 −
27 adee1 e2
64
   ǫ        W bc Wde We1 e2 Fbc W −1 − 13
                                       64
                                          ǫae1 e2 bc W de We1 e2 Fbc Fde W −2 +
5 aee1 e2 d                             29 adee1 e2
4
  ǫ         Wee1 We2 b F bc Fdc W −2 − 128 ǫ        Wde We1 e2 F bc Fbc W −2 +
 3 abcde                                3 e2 cdee1
32
   ǫ     W e1 e2 Fbc Fde Fe1 e2 W −3 − 16 ǫ        We2 b F ab Fcd Fee1 W −3 −
 9 ee1 e2 cd                             419
32
   ǫ         Wee1 We2 b F ab Fcd W −2 + 8192 W bc Wbc α i λiα W −2 ∇a W −
 9                              17 b
64
   F bc Wbc α i λiα W −3 ∇a W + 32 F c W a b α i λiα W −3 ∇c W − 13
                                                                 32
                                                                    F ab Wbc α i λiα W −3 ∇c W +
 7                                      3
32
   (Σa d )αβ F bc Wbcαi λiβ W −3 ∇d W − 16 F a b W cdα i (Σcd )α β λiβ W −3 ∇b W +
3 b                                      3 abcde
8
  F c W adα i (Σbd )α β λiβ W −3 ∇c W − 128 ǫ    Fbc Wde α i (Γe1 )α β λiβ W −3 ∇e1 W +
 3 bcde                         −3 e1   3 abd
128
    ǫ             α    a β i
        e1 Fbc Wde i (Γ )α λβ W   ∇ W + 32 ǫ ee1 (Γe )αβ Fb c Wdcαi λiβ W −3 ∇e1 W +
 7                                       1
16
   (Σad )αβ F b c Wdbαi λiβ W −3 ∇c W + 16 (Σb a )αβ F bc Wcdαi λiβ W −3 ∇d W −
1                                       3
8
  (Σbd )αβ F bc Wc a αi λiβ W −3 ∇d W + 16 (Σc d )αβ F ab Wbcαi λiβ W −3 ∇d W +
19                                       961
32
   (Σbc )αβ F bc W a dαi λiβ W −3 ∇d W + 4096 W b c W a b α i λiα W −2 ∇c W −
 705                                65
4096
     W ab Wbc α i λiα W −2 ∇c W + 12288 ǫbcde e1 (Γe1 )αβ Wbc Wdeαi λiβ W −2 ∇a W −
 65                                      3841
1536
     (Σb d )αβ W bc Wcdαi λiβ W −2∇a W + 12288 (Σa d )αβ W bc Wbcαi λiβ W −2 ∇d W −

                                                       35
```

</details>

<a id="src-c24-p135"></a>

<details>
<summary>C24-p135 — PDF page 135: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p135: PDF page 135](https://arxiv.org/pdf/2311.00679v1#page=135) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 27                                          431
128
    W a b W cdα i (Σcd )α β λiβ W −2 ∇b W − 3072 W ab W c d α i (Σbc )α β λiβ W −2 ∇d W +
27                                          431
64
   W b c W adα i (Σbd )α β λiβ W −2 ∇c W − 6144 W bc W a d α i (Σbc )α β λiβ W −2 ∇d W −
 1727 abcde                                        1727 bcde
49152
      ǫ     Wbc Wde α i (Γe1 )α β λiβ W −2 ∇e1 W + 49152 ǫ             α    a β i
                                                             e1 Wbc Wde i (Γ )α λβ W
                                                                                     −2 e1
                                                                                       ∇ W+
 1727 abd
12288
      ǫ ee1 (Γe )αβ Wb c Wdcαi λiβ W −2 ∇e1 W + 3841
                                                6144
                                                     (Σad )αβ W b c Wdbαi λiβ W −2 ∇c W +
2111                                       239
6144
     (Σb a )αβ W bc Wcdαi λiβ W −2 ∇d W − 3072 (Σbd )αβ W bc Wc a αi λiβ W −2 ∇d W +
1727
6144
     (Σc d )αβ W ab Wbcαi λiβ W −2 ∇d W − 3487
                                          4096
                                               (Σbc )αβ W bc W a dαi λiβ W −2 ∇d W −
 3 bcde                        −3 e1    3
128
    ǫ        a αβ          i
        e1 (Γ ) Fbc Wdeαi λβ W   ∇ W − 16 F ab Wb cα i (Σcd )α β λiβ W −3 ∇d W −
 3                                         3
16
   F bc Wb aα i (Σcd )α β λiβ W −3 ∇d W + 16 F bc Wb dα i (Σcd )α β λiβ W −3 ∇a W +
 3 abcd                         −3 e1   3 bcd
64
   ǫ              α    e β i
        e1 Fbc Wde i (Γ )α λβ W   ∇ W + 64 ǫ ee1 Fbc Wd aα i (Γe )α β λiβ W −3 ∇e1 W −
 3 abde                         −3 c    1 bcd
64
   ǫ              α    e1 β i
        e1 Fbc Wde i (Γ )α λβ W   ∇ W + 64 ǫ ee1 (Γe )αβ Fbc Wd a αi λiβ W −3 ∇e1 W +
 1                                       1
16
   (Σbd )αβ Fbc W a dαi λiβ W −3 ∇c W − 16 (Σc d )αβ F ab Wcbαi λiβ W −3 ∇d W +
 1                                       1 abde
32
   (Σcd )αβ F a b Wcdαi λiβ W −3 ∇b W + 64 ǫ         c αβ          i
                                                e1 (Γ ) Fbc Wdeαi λβ W
                                                                       −3 e1
                                                                         ∇ W+
 1 abcd                        −3 e    1
64
   ǫ         e1 αβ         i
        e1 (Γ ) Fbc Wdeαi λβ W   ∇ W + 16 (Σb c )αβ F ab Wcdαi λiβ W −3 ∇d W −
 865 bcde                        −2 e1    865
49152
      ǫ        a αβ          i
          e1 (Γ ) Wbc Wdeαi λβ W   ∇ W − 6144 W ab Wb cα i (Σcd )α β λiβ W −2 ∇d W −
 865                                        865
6144
     W bc Wb aα i (Σcd )α β λiβ W −2 ∇d W + 6144 W bc Wb dα i (Σcd )α β λiβ W −2 ∇a W +
 865 abcd                         −2 e1    865 bcd
24576
      ǫ             α    e β i
          e1 Wbc Wde i (Γ )α λβ W   ∇ W + 24576 ǫ ee1 Wbc Wd aα i (Γe )α β λiβ W −2 ∇e1 W −
 865 abde                         −2 c    1249 bcd
24576
      ǫ             α    e1 β i
          e1 Wbc Wde i (Γ )α λβ W   ∇ W + 24576 ǫ ee1 (Γe )αβ Wbc Wd a αi λiβ W −2 ∇e1 W +
1249
6144
     (Σbd )αβ Wbc W a dαi λiβ W −2 ∇c W − 1249
                                          6144
                                               (Σc d )αβ W ab Wcbαi λiβ W −2 ∇d W +
 1249                                      1249 abde
12288
      (Σcd )αβ W a b Wcdαi λiβ W −2 ∇b W + 24576 ǫ        c αβ          i
                                                     e1 (Γ ) Wbc Wdeαi λβ W
                                                                            −2 e1
                                                                              ∇ W+
 1249 abcd
24576
      ǫ         e1 αβ         i
           e1 (Γ ) Wbc Wdeαi λβ W   ∇ W + 1249
                                  −2 e
                                          6144
                                               (Σb c )αβ W ab Wcdαi λiβ W −2 ∇d W −
 5
16
   (Γb )αβ λiα λiρ λjβ W −4 ∇b ∇a λjρ + 14 (Γb )αβ λiα λjβ W −4 ∇a λiρ ∇b λjρ +
1
4
  (Γb )αβ λiα λρj W −4 ∇a λiβ ∇b λjρ − 83 (Γb )αβ λiα λρj W −4 ∇a λiρ ∇b λjβ −
 1
16
   (Γb )αβ λiα λρj W −4 ∇a λjβ ∇b λiρ + 16
                                        7
                                           (Γb )αβ λiα λρj W −4 ∇a λjρ ∇b λiβ +
 7
16
   (Γb )αβ λρi λjρ W −4 ∇a λiα ∇b λjβ − 14 (Γb )αβ λiα λiρ W −4 ∇a λjρ∇b λjβ +
 3 abc                                         7
16
   ǫ de (Σbc )αβ λiα λiρ W −4 ∇d λjβ ∇e λjρ + 16 (Γa )αβ λiα λiρ W −4 ∇b λjβ ∇b λjρ −

                                                       36
```

</details>

<a id="src-c24-p136"></a>

<details>
<summary>C24-p136 — PDF page 136: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p136: PDF page 136](https://arxiv.org/pdf/2311.00679v1#page=136) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                                       3
4
  (Γb )αβ λiα λiρ W −4 ∇a λjβ ∇b λjρ − 16 (Γa )αβ λiα λjβ W −4 ∇b λiρ ∇b λjρ +

   ǫ de (Σbc )αβ λiα λρj W −4 ∇d λiβ ∇e λjρ + 81 (Γa )αβ λiα λρj W −4 ∇b λiβ ∇b λjρ −
 7 abc
32

   ǫ de (Σbc )αβ λiα λρj W −4 ∇d λiρ ∇e λjβ + 21 (Γa )αβ λiα λρj W −4 ∇b λiρ ∇b λjβ +
 5 abc
32

   ǫ de (Σbc )αβ λρi λjρ W −4 ∇d λiα ∇e λjβ − 83 (Γa )αβ λρi λjρ W −4 ∇b λiα ∇b λjβ +
13 abc
32

1
4
  (Σa c )ρλ (Γb )αβ λiρ λiα λjβ W −4 ∇b ∇c λjλ − 81 (Σa c )ρλ (Γb )αβ λiρ λiλ λjαW −4 ∇b ∇c λjβ −
1
8
  (Σa c )ρλ (Γb )αβ λiρ λiλ λjα W −4 ∇c ∇b λjβ − 81 (Σa c )ρλ (Γb )αβ λiρ λiλ W −4 ∇c λjα ∇b λjβ −
 1
16
   (Γb )αβ λiα λiρ λjρW −4 ∇b ∇a λjβ + 18 (Σa c )ρλ (Γb )αβ λiρ λiα λjλW −4 ∇b ∇c λjβ −
 1
16
   (Γb )αβ λiα λiρ λjρW −4 ∇a ∇b λjβ + 18 (Σa c )ρλ (Γb )αβ λiρ λiα λjλW −4 ∇c ∇b λjβ −
 1
16
   (Σa c )ρλ (Γb )αβ λiρ λjα W −4 ∇c λiβ ∇b λjλ + 23
                                                  16
                                                     (Σa c )ρλ (Γb )αβ λiρ λjα W −4 ∇c λiλ ∇b λjβ −
 3
16
   (Σa c )ρλ (Γb )αβ λiρ λjα W −4 ∇c λjβ ∇b λiλ + 16
                                                   9
                                                     (Σa c )ρλ (Γb )αβ λiρ λjα W −4 ∇c λjλ ∇b λiβ −
1
8
  (Σa c )ρλ (Γb )αβ λiρ λjλ W −4 ∇c λiα ∇b λjβ + 18 (Σa c )ρλ (Γb )αβ λiρ λiα W −4 ∇c λjλ ∇b λjβ +
1
8
  (Σa c )ρλ (Γb )αβ λiρ λiα W −4 ∇c λjβ ∇b λjλ + 18 (Σa c )ρλ (Γb )αβ λiα λjβ W −4∇c λiρ ∇b λjλ +
 1
12
   W a b α i X i j λjα W −3 ∇b W −iΦa bij λiα λjα W −3 ∇b W + 18 iǫacd be Φcdij (Γb )αβ λiα λjβ W −3∇e W +
 7
32
                                 121
   (Γa )ρα λjρλjβ Xiα Xβi W −2 + 384                                163
                                     (Γa )βρ λiβ λjρX iα Xαj W −2 − 192 (Γa )ρα λiρ λβj Xαi Xβj W −2 +
 79
192
    (Γa )ρβ λiρ λαj Xαi Xβj W −2 + 384
                                   121
                                       (Γa )αβ λρi λjρ Xαi Xβj W −2 + 384
                                                                      41
                                                                          (Γa )βα Xij X ij λkβ Xαk W −3 −
 41
192
    (Γa )βα Xij X i k λjβ Xαk W −3 +i(Σa b )αβ λiα W −2 ∇c ∇c ∇b λiβ +i(Σa b )αβ W −2 ∇b λiα ∇c ∇c λiβ +

i(Σa b )αβ W −2 ∇c λiα ∇c ∇b λiβ + 34 iλαi W −4 ∇a W ∇b W ∇b λiα −3i(Σbc )αβ λiα W −4 ∇a W ∇b W ∇c λiβ −
3
4
  i(Σbc )αβ λiα λiβ W −4 ∇b W ∇c ∇a W + 43 i(Σa b )αβ λiα λiβ W −4 ∇b W ∇c ∇c W +
3
2
  i(Σa b )αβ λiα λiβ W −4 ∇c W ∇c ∇b W − 43 iλαi W −4 ∇b W ∇b W ∇a λiα +
15
 4
   i(Σa b )αβ λiα W −4 ∇c W ∇c W ∇b λiβ + 23 i(Σa b )αβ λiα W −4 ∇b W ∇c W ∇c λiβ −
 45 de
256
    iǫ e1 bc (Σde )αβ Wbc λiα λiβ W −4 ∇a W ∇e1 W + 38 iǫde e1 bc (Σde )αβ Fbc λiα λiβ W −5 ∇a W ∇e1 W −
3 ad
4
  iǫ e1 bc (Σde )αβ Fbc λiα λiβ W −5 ∇e W ∇e1 W + 34 iǫade e1 b (Σde )αβ Fbc λiα λiβ W −5 ∇e1 W ∇c W −
117 ad                                               27 ade
128
    iǫ e1 bc (Σde )αβ Wbc λiα λiβ W −4 ∇e W ∇e1 W − 128 iǫ e1 b (Σde )αβ Wbc λiα λiβ W −4 ∇e1 W ∇c W +
 1 d                                              3 ad
64
   iǫ ee1 bc (Σd a )αβ Wbc λiα W −2 ∇e ∇e1 λiβ − 64 iǫ ee1 c (Σdb )αβ λiα λiβ W −2 ∇e ∇e1 W bc −
 3 adebc                                     1 d bc
32
   iǫ    (Σde )αβ λiα λiβ W −2 ∇e1 ∇e1 Wbc + 32 iǫ e e1 (Σd a )αβ λiα W −3 ∇e Fbc ∇e1 λiβ −

                                                       37
```

</details>

<a id="src-c24-p137"></a>

<details>
<summary>C24-p137 — PDF page 137: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p137: PDF page 137](https://arxiv.org/pdf/2311.00679v1#page=137) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3 adeb                 −3 c               1 d bc
32
   iǫ            αβ
        e1 (Σde ) λiα W   ∇ Fbc ∇e1 λiβ − 32 iǫ e e1 (Σd a )αβ λiα W −2 ∇e Wbc ∇e1 λiβ −
 7 adebc                                      1 d
32
   iǫ    (Σde )αβ Fbc λiα W −3 ∇e1 ∇e1 λiβ − 16 iǫ ee1 bc (Σd a )αβ Fbc λiα W −3 ∇e ∇e1 λiβ −
1 adebc                                      5 adebc
8
  iǫ    (Σde )αβ Fbc W −3 ∇e1 λiα ∇e1 λiβ − 32 iǫ    (Σde )αβ Wbc λiα W −2 ∇e1 ∇e1 λiβ −
 5
128
    iǫd ee1 bc (Σd a )αβ λiα λiβ W −2 ∇e ∇e1 Wbc − 15
                                                   64
                                                      iǫadebc (Σde )αβ λiα W −3 ∇e1 Fbc ∇e1 λiβ +
 3                                       49
32
   i(Σd b )αβ F bc Fdc λiα W −4 ∇a λiβ + 256 i(Σd b )αβ W bc Wdc λiα W −2 ∇a λiβ +
3
4
  i(Σbc )αβ F bc F a d λiα W −4 ∇d λiβ + 15
                                         16
                                            i(Σcd )αβ F a b λiα λiβ W −3 ∇b W cd +
3
2
  i(Σa b )αβ F bc Fcd λiα W −4 ∇d λiβ + 83 i(Σa d )αβ F bc Fbc λiα W −4 ∇d λiβ +
 9 a
64
   iǫ e1 bcd (Γe )αβ Fbc Fde λiα W −4∇e1 λiβ − 15
                                               64
                                                  iǫa e1 bcd (Γe1 )αβ Fbc Fde λiα W −4 ∇e λiβ −
3                                        9
2
  i(Σc b )αβ F ab Fcd λiα W −4 ∇d λiβ − 64 iǫee1 bcd (Γe )αβ Fbc Fd a λiα W −4 ∇e1 λiβ −
15                                        3
32
   i(Σc d )αβ F ab Fcb λiα W −4 ∇d λiβ − 128 iǫabcde (Γe1 )αβ Fbc Fde λiα W −4 ∇e1 λiβ −
33                                         9
32
   i(Σbd )αβ F bc F a c λiα W −4 ∇d λiβ + 16 i(Σbc )αβ F bc λiα λiβ W −3 ∇d W ad −
3
8
  i(Σb d )αβ Fbc λiα λiβ W −3 ∇d W ac − 83 i(Σab )αβ Fbc λiα λiβ W −3 ∇d W dc +
 9
16
   i(Σa d )αβ Fbc λiα λiβ W −3 ∇d W bc − 98 i(Σb d )αβ Fbc λiα λiβ W −3 ∇c W ad −
9
8
  i(Σa d )αβ Fbc λiα λiβ W −3 ∇b W dc + 89 i(Σdc )αβ F a b λiα λiβ W −3 ∇d W cb+
9
8
  i(Σbc )αβ F ab λiα λiβ W −3 ∇d W cd + 98 i(Σbc )αβ W a d F bc λiα W −3 ∇d λiβ +
 9
32
   i(Σcd )αβ W a b λiα λiβ W −2 ∇b W cd + 15
                                           8
                                             i(Σcd )αβ W cd F a b λiα W −3 ∇b λiβ −
9
4
  i(Σcd )αβ W cb F a b λiα W −3 ∇d λiβ + 94 i(Σa d )αβ W db Fbc λiα W −3 ∇c λiβ +
9                                        7
8
  i(Σa d )αβ W bc Fbc λiα W −3 ∇d λiβ + 128 iǫa e1 deb (Γc )αβ Wde Fbc λiα W −3 ∇e1 λiβ −
 17 a
128
    iǫ e1 dbc (Γe1 )αβ Wde Fbc λiα W −3 ∇e λiβ − 94 i(Σc b )αβ Wcd F ab λiα W −3 ∇d λiβ +
3                                        5
4
  i(Σa b )αβ Wcd F bc λiα W −3 ∇d λiβ − 256 iǫee1 dbc (Γe )αβ Wd a Fbc λiα W −3 ∇e1 λiβ −
3
4
  i(Σb d )αβ W ac Fbc λiα W −3 ∇d λiβ − 49 i(Σb d )αβ W ad Fbc λiα W −3 ∇c λiβ −
 29 adebc                                      9
512
    iǫ    (Γe1 )αβ Wde Fbc λiα W −3 ∇e1 λiβ − 128 iǫa ee1 db (Γe )αβ Wd c Fbc λiα W −3 ∇e1 λiβ +
 69 a                                             67 a
256
    iǫ e1 bcd (Γe )αβ Wbc Wde λiα W −2 ∇e1 λiβ − 256 iǫ e1 bcd (Γe1 )αβ Wbc Wde λiα W −2 ∇e λiβ −
 69                                             1
    iǫ bcd (Γe )αβ Wbc Wd a λiα W −2 ∇e1 λiβ + 512
256 ee1
                                                   iǫabcde (Γe1 )αβ Wbc Wde λiα W −2 ∇e1 λiβ +
1
4
  i(Σd b )αβ Wdc λiα λiβ W −3 ∇a F bc + 41 i(Σbc )αβ W a d λiα λiβ W −3 ∇d F bc +

                                                       38
```

</details>

<a id="src-c24-p138"></a>

<details>
<summary>C24-p138 — PDF page 138: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p138: PDF page 138](https://arxiv.org/pdf/2311.00679v1#page=138) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
15
16
   i(Σcd )αβ W cd λiα λiβ W −3 ∇b F ab − 11
                                          8
                                            i(Σc d )αβ Wcb λiα λiβ W −3 ∇d F ab −
9
8
  i(Σad )αβ Wdc λiα λiβ W −3 ∇b F bc + 18 i(Σa d )αβ Wbc λiα λiβ W −3 ∇d F bc −
7
8
  i(Σc b )αβ Wcd λiα λiβ W −3∇d F ab + 21 i(Σa b )αβ Wdc λiα λiβ W −3 ∇d F bc −
1
4
  i(Σdb )αβ W a c λiα λiβ W −3 ∇d F bc + 98 i(Σdb )αβ W ad λiα λiβ W −3 ∇c F bc +
 9
32
   i(Σbc )αβ W bc λiα λiβ W −2 ∇d W ad − 98 i(Σb d )αβ Wbc λiα λiβ W −2 ∇d W ac −
9
8
  i(Σab )αβ Wbc λiα λiβ W −2 ∇d W dc + 15
                                       16
                                          i(Σa d )αβ Wbc λiα λiβ W −2 ∇d W bc −
 9
16
   i(Σb d )αβ Wbc λiα λiβ W −2 ∇c W ad − 89 i(Σa d )αβ Wbc λiα λiβ W −2 ∇b W dc +
9                                        9
8
  i(Σdc )αβ W a b λiα λiβ W −2 ∇d W cb + 16 i(Σbc )αβ W ab λiα λiβ W −2 ∇d W cd +
 3
   iǫ bcde (Γe1 )αβ Fbc Fde λiα W −4 ∇a λiβ + 34 i(Σbc )αβ F ab λiα λiβ W −4 ∇d F cd −
128 e1

3
4
  i(Σb d )αβ Fbc λiα λiβ W −4 ∇d F ac + 83 i(Σbc )αβ F bc λiα λiβ W −4∇d F ad −
3
4
  i(Σab )αβ Fbc λiα λiβ W −4 ∇d F dc − 34 i(Σb d )αβ Fbc λiα λiβ W −4 ∇c F ad −
 7                                             5
   iǫ cdb (Γe )αβ Wcd Fb a λiα W −3 ∇e1 λiβ + 256
128 ee1
                                                  iǫa e1 dbc (Γe )αβ Wde Fbc λiα W −3 ∇e1 λiβ −
 43 a                                            29
256
    iǫ e1 deb (Γe1 )αβ Wde Fbc λiα W −3∇c λiβ + 512 iǫe1 debc (Γe1 )αβ Wde Fbc λiα W −3 ∇a λiβ −
 1                                             3 abcde1
   iǫ bcde (Γe1 )αβ Wbc Wde λiα W −2 ∇a λiβ − 16
512 e1
                                                 iǫ     Fbc Wd eα i We1 eα i W −1 +
 9 bcdee1                               9 abdee1
32
   iǫ     Fbc Wde α i We1 a α i W −1 − 16 iǫ     Fb c Wde α i We1 cα i W −1 −
3
2
  i(Γb )αβ Xij λiα λjβ W −5 ∇a W ∇b W + 23 i(Γa )αβ Xij λiα λjβ W −5 ∇b W ∇b W −
 7
   iλβ λ X iα W −3 ∇a λjα + 37
24 i jβ
                               iλα λβ X i W −3 ∇a λjβ − 96
                            96 i j α
                                                        19 β α i
                                                           iλi λj Xα W −3 ∇a λjβ +
3                                3 a
8
  iF a b λαi λjα W −4 ∇b X ij − 16 iǫ de bc (Γd )αβ Fbc λiα λjβ W −4 ∇e X ij +
 3                                9 a
16
   iW a b λαi λjα W −3 ∇b X ij − 32 iǫ de bc (Γd )αβ Wbc λiα λjβ W −3 ∇e X ij +
3
4
  iXij F a b λiα W −4 ∇b λjα − 38 iǫa de bc (Γd )αβ Xij Fbc λiα W −4 ∇e λjβ +
3
8
                                  iǫ de bc (Γd )αβ Xij Wbc λiα W −3 ∇e λjβ +
                                9 a
  iXij W a b λiα W −3 ∇b λjα − 16
3
8
                               3
  iXij λiα λjα W −4 ∇b F ab + 16                                iǫ de bc (Γd )αβ Xij λiα λjβ W −3 ∇e Wbc −
                                                              9 a
                                 iXij λiα λjα W −3 ∇b W ab − 32
13                                      21
48
   i(Σa b )βρ λjβ λjρ Xiα W −3 ∇b λiα + 128 i(Σa b )βρ λjβ λjρ λαi W −3 ∇b Xαi −
 3
   iλα λjβ Xiα W −3 ∇a λiβ + 31
32 j                         48
                                i(Σa b )βα λjβ λjρ Xiα W −3 ∇b λiρ + 61 i(Σa b )βρ λjβ λjαXiα W −3 ∇b λiρ −
 21                                      53
128
    i(Σa b )βρ λjβ λjαλiρ W −3 ∇b Xαi + 128 i(Σa b )βα λjβ λjρ λiρ W −3 ∇b Xαi −

                                                       39
```

</details>

<a id="src-c24-p139"></a>

<details>
<summary>C24-p139 — PDF page 139: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p139: PDF page 139](https://arxiv.org/pdf/2311.00679v1#page=139) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
35
96
                                         1
   i(Σa b )βρ λiβ λjρ X iα W −3 ∇b λjα + 48 i(Σa b )βα λiβ λρj Xαi W −3 ∇b λjρ +
17
32
   i(Σa b )βρ λiβ λαj Xαi W −3 ∇b λjρ − 11
                                        32
                                           i(Σa b )βα λjβ λρi Xαi W −3 ∇b λjρ +
85
48
   i(Σa b )βρ λjβ λαi Xαi W −3 ∇b λjρ + 131
                                        96
                                            i(Σa b )αβ λρi λjρ Xαi W −3 ∇b λjβ +
 1
12
   i(Γa )βρ (Γb )λα λjβ λjλ Xiα W −3 ∇b λiρ + 32
                                              1
                                                 i(Γa )βα (Γb )ρλ λjβ λjρ Xiα W −3 ∇b λiλ −
 43
256
                                                43
    i(Γa )βα (Γb )ρλ λjβ λjρ λiλ W −3 ∇b Xαi + 256 i(Γa )βρ (Γb )λα λjβ λjλ λiρ W −3 ∇b Xαi +
 19
192
    i(Γa )αβ (Γb )ρλ λiρ λjλXαi W −3 ∇b λjβ − 96
                                               7
                                                 i(Γa )βρ (Γb )λα λjβ λiλ Xαi W −3 ∇b λjρ −
 23
192
    i(Γa )βα (Γb )ρλ λjβ λiρ Xαi W −3∇b λjλ + 192
                                               11
                                                  i(Γa )βρ (Γb )λα λiβ λjλ Xαi W −3∇b λjρ −
23
48
   i(Γa )βα (Γb )ρλ λiβ λjρ Xαi W −3 ∇b λjλ + 192
                                              37
                                                  i(Γa )βρ (Γb )αλ λiβ λjρ Xαi W −3 ∇b λjλ +
                                      1
 1
12
   Wbc α i ǫabcde Φde i j λjα W −1 − 16 iXij X ij λαk W −4 ∇a λkα + 18 iXij X i k λjα W −4 ∇a λkα +
3
8
  i(Σa b )αβ Xij X ij λkα W −4 ∇b λkβ − 21 i(Σa b )αβ Xij λiα λkβ W −4 ∇b X jk +
1
8
  i(Σa b )αβ Xij λkα λkβ W −4 ∇b X ij + 81 ǫabcde Fbc Fde W −3 ∇e1 ∇e1 W −
 1                                                    1
64
   F bc Fde Wbc α i ǫadee1 e2 (Σe1 e2 )α β λiβ W −3 + 32 F bc Fd a Wbc α i (Γd )α β λiβ W −3+
 5 adee1 e2                                         1 bcdee1
64
   ǫ        (Σbc )αβ F bc Fde We1 e2 αi λiβ W −3 + 64 ǫ      Fbc Fd a Wee1 α i λiα W −3 +
 1                                     1
16
   (Γd )αβ F bc Fb a Wdcαi λiβ W −3 − 32 (Γd )αβ F bc Fd a Wbcαi λiβ W −3 −
 1                                     1
32
   (Γd )αβ F bc Fbc Wd a αi λiβ W −3 − 16 (Γd )αβ F bc Fdb Wc a αi λiβ W −3 +
 1 bcde1 e2                                        1 e2 cdee1
32
   ǫ        (Σae )αβ Fbc Fde We1 e2 αi λiβ W −3 − 32 ǫ        (Σe2 b )αβ F ab Fcd Wee1 αi λiβ W −3 −
 1                                     1 abcde1
16
   (Γa )αβ F bc Fb d Wcdαi λiβ W −3 − 32 ǫ      Fbc Fd e We1 e α i λiα W −3 +
 1 e2 bcde1                                         1
16
   ǫ        (Σe2 a )αβ Fbc Fd e We1 eαi λiβ W −3 + 16 F bc Fbd Wce α i ǫadee1 e2 (Σe1 e2 )α β λiβ W −3 +
 1                                        1
16
   F bc Fb a Wcd α i (Γd )α β λiβ W −3 − 16 F bc Fbd Wc aα i (Γd )α β λiβ W −3 −
 1
   F c Fd e Wce α i ǫabde1 e2 (Σe1 e2 )α β λiβ W −3 − 18 F ab Fc d Wbd α i (Γc )α β λiβ W −3 +
16 b

 1 ae1 e2 de                                       11 ae1 e2 de
48
   iǫ        (Σe1 e2 )αβ Cbcde F bc λiα λiβ W −3 + 384 iǫ       (Σe1 e2 )αβ Wde Wbc F bc λiα λiβ W −3 +
 3                                                       1
256
    iǫae1 e2 bc (Σe1 e2 )αβ W de Wde Fbc λiα λiβ W −3 − 384 iǫae1 e2 de (Σe1 e2 )αβ Wdb Wec F bc λiα λiβ W −3 +
 1 ae1 e2 d                            −3    1
16
   iǫ               αβ e     bc    i
         b (Σe1 e2 ) Wd Wec F λiα λβ W    + 192 iǫabce1 e2 (Σde )αβ Cbcde Fe1 e2 λiα λiβ W −3 −
 1                                                       1
192
    iǫae1 e2 bc (Σde )αβ W de We1 e2 Fbc λiα λiβ W −3 + 384 iǫade1 bc (Σee2 )αβ Wde We1 e2 Fbc λiα λiβ W −3 −
 1 ae2 e1 bc                                           1 e2 bcee1
64
   iǫ        (Σe2 d )αβ W de We1 e Fbc λiα λiβ W −3 − 48 iǫ       (Σe2 d )αβ Cbc a d Fee1 λiα λiβ W −3 +

                                                         40
```

</details>

<a id="src-c24-p140"></a>

<details>
<summary>C24-p140 — PDF page 140: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p140: PDF page 140](https://arxiv.org/pdf/2311.00679v1#page=140) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1                                                       1 e2 debc
192
    iǫe2 ee1 bc (Σe2 d )αβ W ad Wee1 Fbc λiα λiβ W −3 − 96 iǫ      (Σe2 e1 )αβ Wd a Wee1 Fbc λiα λiβ W −3 −
 1 e1 e2 ebc                                          1 ae1 e2 bd
64
   iǫ        (Σe1 e2 )αβ W ad Wed Fbc λiα λiβ W −3 + 24 iǫ        (Σe1 e2 )αβ Cbcde F ce λiα λiβ W −3 +
 1 ae1 e2 bc                                        1 e1 e2 bc
64
   iǫ        (Σe1 e2 )αβ Cbcde F de λiα λiβ W −3 − 48 iǫ              αβ a    ed    i
                                                           e (Σe1 e2 ) Cb cd F λiα λβ W
                                                                                        −3
                                                                                           −
 1                                                         1
192
    iǫe1 e2 b de (Σe1 e2 )αβ Wd a Wec F bc λiα λiβ W −3 − 192 iǫe1 e2 b de (Σe1 e2 )αβ Wde W a c F bc λiα λiβ W −3 −
 67 dbcee1                               97 adebe1
1536
     ǫ     Wd a Fbc Wee1 α i λiα W −2 + 768 ǫ      Wde Fb c We1 c α i λiα W −2 −
 805                                                     805
6144
     W de Fbc Wde α i ǫabce1 e2 (Σe1 e2 )α β λiβ W −2 + 3072 W cd Fb a Wcd α i (Γb )α β λiβ W −2 +
 469 adee1 e2                                         277 cdbee1
6144
     ǫ        (Σbc )αβ Wde F bc We1 e2 αi λiβ W −2 − 6144 ǫ      Wcd Fb a Wee1 α i λiα W −2 +
 61                                     133
1536
     (Γd )αβ W ab Fb c Wdcαi λiβ W −2 + 3072 (Γd )αβ Wd a F bc Wbcαi λiβ W −2 +
 205                                      205
3072
     (Γd )αβ W bc Fbc Wd a αi λiβ W −2 + 1536 (Γd )αβ Wdb F bc Wc a αi λiβ W −2 −
 133 debe1 e2                                        133 e2 cdee1
3072
     ǫ        (Σac )αβ Wde Fbc We1 e2 αi λiβ W −2 + 3072 ǫ        (Σe2 b )αβ Wcd F ab Wee1 αi λiβ W −2 +
 155                                     15 adbce1
1536
     (Γa )αβ W bd Fb c Wdcαi λiβ W −2 − 128 ǫ      Wd e Fbc We1 e α i λiα W −2 +
 9 e2 dbce1                                         9
64
   ǫ        (Σe2 a )αβ Wd e Fbc We1 eαi λiβ W −2 + 64 W bd Fbc Wde α i ǫacee1 e2 (Σe1 e2 )α β λiβ W −2 +
 9                                        9
64
   W bc Fb a Wcd α i (Γd )α β λiβ W −2 − 64 W bd Fbc Wd aα i (Γc )α β λiβ W −2 −
 9                                                      9
64
   Wd e Fb c Wec α i ǫadbe1 e2 (Σe1 e2 )α β λiβ W −2 − 64 W ad Fb c Wdc α i (Γb )α β λiβ W −2 −
 9                                        3
64
   Wc d F ab Wbd α i (Γc )α β λiβ W −2 + 256 Wde F bc Wbc α i ǫadee1 e2 (Σe1 e2 )α β λiβ W −2 +
 3                                         3 abce1 e2
128
    Wd a F bc Wbc α i (Γd )α β λiβ W −2 − 256 ǫ       (Σde )αβ W de Fbc We1 e2 αi λiβ W −2 −
 61                                      83
1536
     (Γd )αβ W bc Fb a Wdcαi λiβ W −2 + 1536 (Γb )αβ W cd Fbc Wd a αi λiβ W −2 +
 3                                      3 dbce1 e2
128
    (Γb )αβ W cd Fb a Wcdαi λiβ W −2 + 128 ǫ       (Σae )αβ Wde Fbc We1 e2 αi λiβ W −2 −
 3 e2 bcee1                                         3
128
    ǫ       (Σe2 d )αβ W ad Fbc Wee1 αi λiβ W −2 − 128 Wde Fb c We1 c α i ǫadebe1 λiα W −2 −
 61                                     3
1536
     (Γc )αβ Wc d F ab Wbdαi λiβ W −2 + 64 (Σe2 e1 )αβ Wde Fb c We1 cαi ǫae2 deb λiβ W −2 −
 3                                                  3 e1 e2 dbe
64
   (Σbe2 )αβ Wde F bc Wce1 αi ǫae2 dee1 λiβ W −2 + 64 ǫ         (Σe1 e2 )αβ Wd a Fb c Wecαi λiβ W −2 +
 61                                      5
1536
     (Γb )αβ W ad Fb c Wdcαi λiβ W −2 − 256 W bc Wde Wbc α i ǫadee1 e2 (Σe1 e2 )α β λiβ W −1 +
 3                                       23 adee1 e2
32
   W bc Wd a Wbc α i (Γd )α β λiβ W −1 + 256 ǫ       (Σbc )αβ W bc Wde We1 e2 αi λiβ W −1 +
 5 bcdee1                              17
256
    ǫ     Wbc Wd a Wee1 α i λiα W −1 + 128 (Γd )αβ W bc Wb a Wdcαi λiβ W −1 −
 5                                      5
128
    (Γd )αβ W bc Wd a Wbcαi λiβ W −1 − 128 (Γd )αβ W bc Wbc Wd a αi λiβ W −1 −

                                                         41
```

</details>

<a id="src-c24-p141"></a>

<details>
<summary>C24-p141 — PDF page 141: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p141: PDF page 141](https://arxiv.org/pdf/2311.00679v1#page=141) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3                                       3 bcde1 e2
128
    (Γd )αβ W bc Wdb Wc a αi λiβ W −1 + 32 ǫ        (Σae )αβ Wbc Wde We1 e2 αi λiβ W −1 −
 3 e2 cdee1                                         3
32
   ǫ        (Σe2 b )αβ W ab Wcd Wee1 αi λiβ W −1 − 16 (Γa )αβ W bc Wb d Wcdαi λiβ W −1 −
 17 abcde1                               17 e2 bcde1
256
    ǫ      Wbc Wd e We1 e α i λiα W −1 + 128 ǫ       (Σe2 a )αβ Wbc Wd e We1 eαi λiβ W −1 +
 17                                                    17
128
    W bc Wbd Wce α i ǫadee1 e2 (Σe1 e2 )α β λiβ W −1 + 128 W bc Wb a Wcd α i (Γd )α β λiβ W −1 −
 17                                       17
128
    W bc Wbd Wc aα i (Γd )α β λiβ W −1 − 128 Wb c Wd e Wce α i ǫabde1 e2 (Σe1 e2 )α β λiβ W −1 −
17                                        7
64
   W ab Wc d Wbd α i (Γc )α β λiβ W −1 − 256 Wbc Wd e We1 e α i ǫabcde1 λiα W −1 +
 7                                                   7
128
    (Σe2 e1 )αβ Wbc Wd e We1 eαi ǫae2 bcd λiβ W −1− 128 (Σbe2 )αβ W bc Wde Wce1 αi ǫae2 dee1 λiβ W −1 +
 7 e1 e2 bce                                         1
128
    ǫ        (Σe1 e2 )αβ Wb a Wc d Wedαi λiβ W −1 + 384 iǫabce1 e2 (Σde )αβ Cbcde We1 e2 λiα λiβ W −2 −
  7                                                      67
1536
     iǫadee1 e2 (Σbc )αβ W bc Wde We1 e2 λiα λiβ W −2 + 3072 iǫae1 e2 de (Σe1 e2 )αβ W bc Wde Wbc λiα λiβ W −2 −
  1                                                    19 ae2 dee1
1536
     iǫabcde1 (Σee2 )αβ Wbc Wde We1 e2 λiα λiβ W −2 − 768 iǫ       (Σe2 b )αβ W bc Wde We1 c λiα λiβ W −2 +
 7                                                     49
384
    iǫae1 e2 bc (Σe1 e2 )αβ Cbcde W de λiα λiβ W −2 + 1536 iǫae1 e2 de (Σe1 e2 )αβ W bc Wdb Wec λiα λiβ W −2 +
 29 ae1 e2 d                            −2    1
384
    iǫ               αβ bc e        i
          b (Σe1 e2 ) W Wd Wec λiα λβ W    − 256 iǫadee1 e2 (Σbc )αβ Cbcde We1 e2 λiα λiβ W −2 −
 1                                                     1
384
    iǫe2 cdee1 (Σe2 b )αβ C a bcd Wee1 λiα λiβ W −2 + 128 iǫe2 cdee1 (Σe2 b )αβ W ab Wcd Wee1 λiα λiβ W −2 −
 1 e2 bcde                                           13 e1 e2 cde
64
   iǫ      (Σe2 e1 )αβ Wbc Wd a Wee1 λiα λiβ W −2 − 768 iǫ        (Σe1 e2 )αβ W ab Wcd Web λiα λiβ W −2 −
 1                                                     1
192
    iǫae2 bce1 (Σe2 d )αβ Cbcd e We1 e λiα λiβ W −2 + 192 iǫe1 e2 bce (Σe1 e2 )αβ Cb a c d Wed λiα λiβ W −2 +
 19 ae1 e2 de                                        11 e2 bcee1
768
    iǫ        (Σe1 e2 )αβ Cbcde W bc λiα λiβ W −2 − 384 iǫ       (Σe2 d )αβ Cbc a d Wee1 λiα λiβ W −2 −
 1                                                      1
192
    iǫae2 dee1 (Σe2 b )αβ Cb c de We1 c λiα λiβ W −2 − 192 iǫe1 e2 bde (Σe1 e2 )αβ Cb c d a Wec λiα λiβ W −2 −
 11                                         11
3072
     Wd e Fbc We1 e α i ǫadbce1 λiα W −2 − 768 (Σe2 c )αβ Wd e Fbc We1 eαi ǫae2 dbe1 λiβ W −2 −
 11 e1 e2 bce                                        11 e1 e2 dbc
3072
     ǫ        (Σe1 e2 )αβ W ad Fbc Wedαi λiβ W −2 + 3072 ǫ        (Σe1 e2 )αβ Wd e Fbc W a eαi λiβ W −2 +
 5 ae1 e2 bd                                        5
96
   iǫ        (Σe1 e2 )αβ Cbcde W ce λiα λiβ W −2 − 192 iǫe1 e2 e bc (Σe1 e2 )αβ Cb a cd W ed λiα λiβ W −2 −
 5                                                         5
768
    iǫe1 e2 b de (Σe1 e2 )αβ W bc Wd a Wec λiα λiβ W −2 − 768 iǫe1 e2 b de (Σe1 e2 )αβ W bc Wde W a c λiα λiβ W −2 +
11
 8
   (Γb )αβ λiα λiρ λjβ W −5 ∇b W ∇a λjρ + 85 (Γb )αβ λiα λiρ λjρ W −5 ∇a W ∇b λjβ +
5
8
  (Γb )αβ λiα λiρ λjρ W −5 ∇b W ∇a λjβ + 83 (Γb )αβ λiα λiρ λjβ W −5∇a W ∇b λjρ −

  ǫ de (Σbc )αβ λiα λiρ λjβ W −5 ∇d W ∇e λjρ − 74 (Γa )αβ λiα λiρ λjβ W −5 ∇b W ∇b λjρ +
1 abc
8

ǫabc de (Σbc )αβ λiα λiρ λjρW −5 ∇d W ∇e λjβ − 54 (Γa )αβ λiα λiρ λjρW −5 ∇b W ∇b λjβ +

                                                         42
```

</details>

<a id="src-c24-p142"></a>

<details>
<summary>C24-p142 — PDF page 142: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p142: PDF page 142](https://arxiv.org/pdf/2311.00679v1#page=142) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
4
  (Γb )αβ λiα λiρ λjβ λjρ W −5 ∇b ∇a W − 21 (Σa c )ρλ (Γb )αβ λiρ λiα λjβ W −5 ∇b W ∇c λjλ +
3
2
  (Σa c )ρλ (Γb )αβ λiρ λiλ λjα W −5 ∇c W ∇b λjβ + 41 (Σa c )ρλ (Γb )αβ λiρ λiλ λjα W −5∇b W ∇c λjβ −
3
4
  (Σa c )ρλ (Γb )αβ λiρ λiα λjλ W −5 ∇c W ∇b λjβ − 41 (Σa c )ρλ (Γb )αβ λiρ λiα λjλW −5 ∇b W ∇c λjβ −
 1 adebc
16
   iǫ    Φdeij Fbc λiα λjα W −3 − 18 iΦbcij (Γa )αβ F bc λiα λjβ W −3 − 18 iǫadebc Φdeij Wbc λiα λjα W −2 +
1
8
  iΦab ij (Γc )αβ Wbc λiα λjβ W −2 − 18 iΦbcij (Γa )αβ W bc λiα λjβ W −2 − 18 iΦcbij (Γc )αβ W ab λiα λjβ W −2 −
 7 abcde
64
   ǫ                                1
         Xij Fbc Wde αi λjα W −3 − 96 (Γa )αβ Xij F bc Wbcα i λjβ W −3 + 96
                                                                         1 e1 bcde
                                                                            ǫ      (Σe1 a )αβ Xij Fbc Wdeα i λjβ W −3 −
 1
   X F c Wdc αi ǫabdee1 (Σee1 )α β λjβ W −3 + 48
48 ij b
                                              1
                                                 Xij F ab Wbc αi (Γc )α β λjβ W −3 +
 1
   X F c W a c αi (Γb )α β λjβ W −3 + 1536
48 ij b
                                       23 abcde
                                           ǫ    Xij Wbc Wde αi λjα W −2 −
 13
768
    (Γa )αβ Xij W bc Wbcα i λjβ W −2 + 768
                                       13 e1 bcde
                                           ǫ      (Σe1 a )αβ Xij Wbc Wdeα i λjβ W −2 −
 13
    X W c Wdc αi ǫabdee1 (Σee1 )α β λjβ W −2 + 384
384 ij b
                                                13
                                                   Xij W ab Wbc αi (Γc )α β λjβ W −2 +
 13
    X W c W a c αi (Γb )α β λjβ W −2 − 384
384 ij b
                                        7
                                           Wbc α i ǫabcde (Σde )βρ λjβ λjρ Xαi W −2 +
 1                                             1
24
   Wbc α i ǫabcde (Σde )βρ λiβ λjρ Xαj W −2 + 12 Wb aα i (Γb )βρ λiβ λjρXαj W −2 +
 7                                              7
768
    Wbc α i ǫabcde (Σde )ρβ λjα λjρ Xβi W −2 − 384 Wb aα i (Γb )ρβ λjα λjρ Xβi W −2 +
 1
384
    Wbc α i ǫabcde (Σde )ρβ λiα λjρXβj W −2 − 192
                                               1
                                                  Wb aα i (Γb )ρβ λiα λjρ Xβj W −2 +
 73
2304
                                                 71
     iǫabcde Φbcij (Σde )αβ X ij λkα λkβ W −3 + 1152 iǫabcde Φbcik (Σde )αβ X i j λkα λjβ W −3 +
 1
12
   iΦb a ik (Γb )αβ X i j λkα λjβ W −3 − 12 i(Σa b )αβ λiα λiβ W −3 ∇c ∇c ∇b W −
3                                           3
2
  i(Σa b )αβ λiα λiβ W −5 ∇b W ∇c W ∇c W + 128 iǫad e1 bc (Σde )αβ Wbc λiα λiβ W −3 ∇e ∇e1 W −
 11 ade
128
    iǫ e1 b (Σde )αβ Wbc λiα λiβ W −3 ∇e1 ∇c W − 38 iǫad ee1 c (Σdb )αβ λiα λiβ W −4 ∇e W ∇e1 F bc +
3 adebc                                        3 de
8
  iǫ    (Σde )αβ λiα λiβ W −4 ∇e1 W ∇e1 Fbc − 32 iǫ e1 bc (Σde )αβ λiα λiβ W −4 ∇e1 W ∇a Fbc +
27 adebc                                        1 d
64
   iǫ    (Σde )αβ Fbc λiα W −4 ∇e1 W ∇e1 λiβ − 16 iǫ ee1 bc (Σd a )αβ Wbc λiα λiβ W −3 ∇e ∇e1 W +
 51 adebc                                        3 d
256
    iǫ    (Σde )αβ Wbc λiα W −3 ∇e1 W ∇e1 λiβ − 16 iǫ ee1 bc (Σd a )αβ λiα λiβ W −4 ∇e W ∇e1 Fbc −
 3 ade                                           19 d
16
   iǫ e1 b (Σde )αβ λiα λiβ W −4 ∇e1 W ∇c Fbc − 128 iǫ ee1 bc (Σd a )αβ λiα λiβ W −3 ∇e W ∇e1 Wbc −
3
2
  i(Σbc )αβ F bc F a d λiα λiβ W −5 ∇d W + 23 i(Σc d )αβ F ab Fcb λiα λiβ W −5 ∇d W −

3i(Σa b )αβ F bc Fcd λiα λiβ W −5 ∇d W − 34 i(Σa d )αβ F bc Fbc λiα λiβ W −5 ∇d W +

3i(Σc b )αβ F ab Fcd λiα λiβ W −5 ∇d W + 32 i(Σbd )αβ F bc F a c λiα λiβ W −5 ∇d W −

                                                        43
```

</details>

<a id="src-c24-p143"></a>

<details>
<summary>C24-p143 — PDF page 143: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p143: PDF page 143](https://arxiv.org/pdf/2311.00679v1#page=143) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
27                                           9
16
   i(Σbc )αβ W a d F bc λiα λiβ W −4 ∇d W − 16 i(Σbc )αβ W bc W a d λiα λiβ W −3 ∇d W −
45
16
   i(Σcd )αβ W cd F a b λiα λiβ W −4 ∇b W + 27
                                            8
                                               i(Σcd )αβ W cb F a b λiα λiβ W −4 ∇d W −
27
 8
   i(Σa d )αβ W db Fbc λiα λiβ W −4 ∇c W − 27
                                           16
                                              i(Σa d )αβ W bc Fbc λiα λiβ W −4 ∇d W +
27
 8
   i(Σc b )αβ Wcd F ab λiα λiβ W −4 ∇d W + 98 i(Σb d )αβ W ac Fbc λiα λiβ W −4 ∇d W +
27                                         315
 8
   i(Σb d )αβ W ad Fbc λiα λiβ W −4 ∇c W + 256 i(Σc d )αβ W ab Wcb λiα λiβ W −3 ∇d W −
9                                         15
4
  i(Σa b )αβ W bc Wcd λiα λiβ W −3 ∇d W − 16 i(Σa d )αβ W bc Wbc λiα λiβ W −3 ∇d W +
9
8
  i(Σc b )αβ W ab Wcd λiα λiβ W −3 ∇d W + 261
                                          256
                                              i(Σbd )αβ W bc W a c λiα λiβ W −3 ∇d W +
3
4
  i(Σd b )αβ F bc Fdc λiα λiβ W −5 ∇a W − 98 i(Σa b )αβ Wcd F bc λiα λiβ W −4 ∇d W +
 27                                          3
128
    i(Σd b )αβ W bc Wdc λiα λiβ W −3 ∇a W − 32 iW bcα i (Σbc )βρ λjβ λjρ W −3 ∇a λiα +
 7                                             7
48
   iW b c α i (Σa b )βρ λjβ λjρ W −3 ∇c λiα − 48 iW abα i (Σbc )βρ λjβ λjρ W −3 ∇c λiα +
 9                                          19
512
    i(Σbc )βρ λjβ λjρ λαi W −3 ∇a Wbcα i + 256 i(Σab )βρ λjβ λjρ λαi W −3 ∇c Wbcα i −
 25                                            3
768
    i(Σb c )βρ λjβ λjρ λαi W −3 ∇c W a bα i + 32 iW bcα i (Σbc )βρ λiβ λjρ W −3 ∇a λjα −
 3                                   3
32
   iW a b α i λiβ λjβ W −3 ∇b λjα − 64 iWbc α i ǫabc de (Γd )βρ λiβ λjρ W −3 ∇e λjα −
 7                                            7
48
   iW b c α i (Σa b )βρ λiβ λjρ W −3 ∇c λjα + 48 iW abα i (Σbc )βρ λiβ λjρ W −3 ∇c λjα −
 9
512
                                            263
    i(Σbc )βρ λjβ λjα λiρ W −3 ∇a Wbcα i − 1536 iλβj λjα λiβ W −3 ∇b W a bα i −
 103 a                                             19
3072
     iǫ de bc (Γd )βρ λjβ λjαλiρ W −3 ∇e Wbcα i − 256 i(Σab )βρ λjβ λjαλiρ W −3 ∇c Wbcα i +
 25                                          1
768
    i(Σb c )βρ λjβ λjαλiρ W −3 ∇c W a bα i + 24 iW a b α i λjα λjβ W −3 ∇b λiβ +
 1
16
   iW bcα i (Σbc )βρ λjα λjβ W −3 ∇a λiρ + 16
                                            1
                                              iWbc α i ǫabc de (Γd )βρ λjα λjβ W −3 ∇e λiρ +
1
8
  iW b c α i (Σa b )βρ λjα λjβ W −3 ∇c λiρ + 24
                                             1
                                                iW abα i (Σbc )βρ λjα λjβ W −3 ∇c λiρ −
 1
96
   iW a b α i λiβ λjα W −3∇b λjβ − 32
                                    1
                                      iW bcα i (Σbc )βρ λiβ λjα W −3 ∇a λjρ −
 3                                                1
64
   iWbc α i ǫabc de (Γd )βρ λiβ λjαW −3 ∇e λjρ − 16 iW b c α i (Σa b )βρ λiβ λjα W −3 ∇c λjρ −
 5
48
   iW abα i (Σbc )βρ λiβ λjα W −3∇c λjρ − 32 iXij F a b λiα λjα W −5 ∇b W +

  iǫ de bc (Γd )αβ Xij Fbc λiα λjβ W −5 ∇e W − 16
3 a
4
                                                9
                                                  iXij W a b λiα λjα W −4∇b W +

   iǫ de bc (Γd )αβ Xij Wbc λiα λjβ W −4 ∇e W − 54 i(Σa b )βρ λjβ λjρ λαi Xαi W −4 ∇b W +
27 a
32

31
32
   i(Σa b )βρ λjβ λjα λiρ Xαi W −4 ∇b W − 61
                                          32
                                             i(Σa b )βα λjβ λjρλiρ Xαi W −4 ∇b W +

                                                        44
```

</details>

<a id="src-c24-p144"></a>

<details>
<summary>C24-p144 — PDF page 144: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p144: PDF page 144](https://arxiv.org/pdf/2311.00679v1#page=144) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
11
64
   i(Γa )βα (Γb )ρλ λjβ λjρ λiλ Xαi W −4 ∇b W − 11
                                                64
                                                   i(Γa )βρ (Γb )λα λjβ λjλ λiρ Xαi W −4 ∇b W −
 9
16
   i(Σa b )αβ Xij X ij λkα λkβ W −5 ∇b W − 83 i(Σa b )αβ Xij X i k λjα λkβ W −5 ∇b W −
5
4
  (Γb )αβ λiα λiρ λjβ λjρ W −6 ∇a W ∇b W + 45 (Γa )αβ λiα λiρ λjβ λjρ W −6 ∇b W ∇b W −

   ǫ de (Σbc )αβ λiα λiβ λρj W −4 ∇d ∇e λjρ − 16
 1 abc
16
                                                 ǫ de (Σbc )αβ λiα λiβ W −4 ∇d λρj ∇e λjρ +
                                               1 abc

 1 abc
16
   ǫ de (Σbc )αβ λiα λiρ λjβ W −4 ∇d ∇e λjρ + 83 (Γa )αβ λiα λiρ λjβ W −4 ∇b ∇b λjρ −
 1                                       1 abc
16
   (Γb )αβ λiα λiρ λjβ W −4 ∇a ∇b λjρ − 16 ǫ de (Σbc )αβ λiα λjβ W −4 ∇d λiρ ∇e λjρ −
1
8
  (Σbc )ρλ (Γa )αβ λiρ λiα λjβ W −4 ∇b ∇c λjλ + 14 (Σbc )ρλ (Γa )αβ λiρ λiα W −4 ∇b λjλ∇c λjβ −
 3
16
   (Σbc )ρλ (Γa )αβ λiρ λjα W −4 ∇b λiβ ∇c λjλ + 16
                                                  1
                                                    (Σbc )ρλ (Γa )αβ λiρ λjαW −4 ∇b λiλ ∇c λjβ −
 1
16
   (Σbc )ρλ (Γa )αβ λiα λjβ W −4 ∇b λiρ ∇c λjλ − 12 (Σbc )αβ F bc λiα λiβ λρj W −5 ∇a λjρ −
3
8
  (Σbc )αβ F bc λiα λiρ λjρ W −5 ∇a λjβ − 128
                                           69
                                              (Σbc )αβ W bc λiα λiβ λρj W −4 ∇a λjρ −
 15
128
                                             41
    (Σbc )αβ W bc λiα λiρ λjβ W −4 ∇a λjρ − 128 (Σbc )αβ W bc λiα λiρ λjρ W −4 ∇a λjβ +

  F b λαi λiβ λjα W −5 ∇b λjβ − 12 (Σab )αβ Fbc λiα λiβ λρj W −5 ∇c λjρ −(Σbc )αβ F ab λiα λiβ λρj W −5 ∇c λjρ +
3 a
8

1                                          5 a
8
  (Σbc )αβ F bc λiα λiρ λjβ W −5 ∇a λjρ − 16 ǫ de bc (Γd )αβ Fbc λiα λiρ λjβ W −5 ∇e λjρ −
1
4
  (Σab )αβ Fbc λiα λiρ λjβ W −5 ∇c λjρ − 45 (Σbc )αβ F ab λiα λiρ λjβ W −5 ∇c λjρ −

  ǫ de bc (Γd )αβ Fbc λiα λiρ λjρ W −5 ∇e λjβ −(Σab )αβ Fbc λiα λiρ λjρ W −5 ∇c λjβ +
1 a
2

1
2
  (Σbc )αβ F ab λiα λiρ λjρ W −5 ∇c λjβ + 14 (Σa d )αβ (Σbc )ρλ F bc λiα λiβ λjρW −5 ∇d λjλ −
1
4
  (Σa d )αβ (Σbc )ρλ F bc λiα λiρ λjβ W −5 ∇d λjλ + 23 (Σa d )αβ (Σbc )ρλ F bc λiα λjρ λjλ W −5 ∇d λiβ +
 45
128
    W a b λαi λiβ λjα W −4 ∇b λjβ − 64
                                    39
                                       (Σab )αβ Wbc λiα λiβ λρj W −4 ∇c λjρ −
67
64
   (Σbc )αβ W ab λiα λiβ λρj W −4 ∇c λjρ − 256
                                            97 a
                                               ǫ de bc (Γd )αβ Wbc λiα λiρ λjβ W −4 ∇e λjρ −
27                                        83
64
   (Σab )αβ Wbc λiα λiρ λjβ W −4 ∇c λjρ − 64 (Σbc )αβ W ab λiα λiρ λjβ W −4 ∇c λjρ −

    ǫ de bc (Γd )αβ Wbc λiα λiρ λjρW −4 ∇e λjβ − 25
 73 a
128                                              32
                                                    (Σab )αβ Wbc λiα λiρ λjρ W −4 ∇c λjβ +
1
4
  (Σbc )αβ W ab λiα λiρ λjρ W −4 ∇c λjβ + 64
                                           9
                                             (Σa d )αβ (Σbc )ρλ W bc λiα λiβ λjρ W −4 ∇d λjλ −
 9
64
   (Σa d )αβ (Σbc )ρλ W bc λiα λiρ λjβ W −4 ∇d λjλ − 32
                                                     15
                                                        (Σa d )αβ (Σbc )ρλ W bc λiα λiρ λjλW −4 ∇d λjβ +
3
4
  (Σa d )αβ (Σbc )ρλ W bc λiα λjρλjλ W −4 ∇d λiβ − 64
                                                    3
                                                      (Σa d )αβ (Σbc )ρλ λiα λiβ λjρλjλ W −4 ∇d W bc +
 3
64
   (Σa d )αβ (Σbc )ρλ λiα λiρ λjβ λjλ W −4 ∇d W bc + 128 λi λ λjα λjβ W −4 ∇b W ab −
                                                      27 α iβ

                                                        45
```

</details>

<a id="src-c24-p145"></a>

<details>
<summary>C24-p145 — PDF page 145: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p145: PDF page 145](https://arxiv.org/pdf/2311.00679v1#page=145) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    ǫ de bc (Γd )αβ λiα λiρ λjβ λjρ W −4 ∇e Wbc + 14 λαi λiβ λjαλjβ W −5 ∇b F ab +
 45 a
256

   ǫ e1 bc (Σde )ρλ (Γa )αβ Fbc λiρ λiα λjβ W −5 ∇e1 λjλ + 81 (Γa )αβ (Γb )ρλ Fbc λiα λiρ λjβ W −5 ∇c λjλ +
 3 de
16

1
4
  (Γa )αβ (Γb )ρλ Fbc λiα λiρ λjλ W −5 ∇c λjβ − 41 (Γc )αβ (Γb )ρλ Fb a λiα λiρ λjβ W −5 ∇c λjλ −
 1 aee1 bc
16
   ǫ       (Σee1 )ρλ (Γd )αβ Fbc λiρ λiα λjλW −5 ∇d λjβ − 81 (Γc )αβ (Γb )ρλ Fb a λiα λiρ λjλW −5 ∇c λjβ +
1 aee1 bc
4
  ǫ       (Σee1 )ρλ (Γd )αβ Fbc λiρ λiλ λjα W −5 ∇d λjβ + 256 ǫ e1 bc (Σde )ρλ (Γa )αβ Wbc λiρ λiα λjβ W −4 ∇e1 λjλ +
                                                          33 de

 15
128
    (Γa )αβ (Γb )ρλ Wbc λiα λiρ λjβ W −4 ∇c λjλ + 15
                                                  64
                                                     (Γa )αβ (Γb )ρλ Wbc λiα λiρ λjλW −4 ∇c λjβ +
 1 aee1 bc
32
   ǫ       (Σee1 )ρλ (Γd )αβ Wbc λiρ λiα λjβ W −4 ∇d λjλ − 64
                                                           11
                                                              (Γc )αβ (Γb )ρλ Wb a λiα λiρ λjβ W −4 ∇c λjλ −
 17 aee1 bc
256
    ǫ       (Σee1 )ρλ (Γd )αβ Wbc λiρ λiα λjλ W −4 ∇d λjβ − 128
                                                             23
                                                                (Γc )αβ (Γb )ρλ Wb a λiα λiρ λjλ W −4 ∇c λjβ +
 53 aee1 bc
256
    ǫ       (Σee1 )ρλ (Γd )αβ Wbc λiρ λiλ λjα W −4 ∇d λjβ + 14 (Γc )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −5 ∇c F ab +
 27
128
    (Γc )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −4 ∇c W ab + 14 (Γa )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −5 ∇c Fbc +
 27
128
    (Γa )αβ (Γb )ρλ λiα λiρ λjβ λjλ W −4 ∇c Wbc − 48
                                                   1
                                                     Wbc α i Wd e α i ǫabcde1 (Σe1 e )βρ λjβ λjρ W −2 −
 1
96
                                                      1
   Wbc α i Wd a α i ǫbcdee1 (Σee1 )βρ λjβ λjρ W −2 − 64 Wbc α i Wdeαj ǫabcde λiβ λjβ W −2 +
1                                         1
8
  Wb cα i W a cαj (Γb )βρ λiβ λjρ W −2 − 32 W bcα i Wbcαj (Γa )βρ λiβ λjρ W −2 −
 1                                                    1
48
   Wbc α i Wd e αj ǫabcde1 (Σe1 e )βρ λiβ λjρ W −2 − 96 Wbc α i Wd a αj ǫbcdee1 (Σee1 )βρ λiβ λjρ W −2 −
21
   X λiα λjβ λkα W −5 ∇a λkβ − 98 (Σa b )αβ Xij λiα λjρ λkρW −5 ∇b λkβ −
32 ij

 7
   X λiα λkα λkβ W −5 ∇a λjβ + 16
32 ij
                               15
                                  (Σa b )αβ Xij λiα λkβ λkρW −5 ∇b λjρ −
 3
16
   (Σa b )αβ Xij λiα λjρλkβ W −5 ∇b λkρ − 21
                                          16
                                             (Σa b )αβ Xij λiρ λjρ λkα W −5 ∇b λkβ −
 3
16
                                            1
   (Σa b )αβ Xij λiρ λkα λkβ W −5 ∇b λjρ − 16 (Σa b )αβ λkα λkβ λρi λjρW −5 ∇b X ij +
5
8
                                           1
  (Σa b )αβ λkα λkρλiβ λjρ W −5 ∇b X ij − 32 (Γa )αβ (Γb )ρλ Xij λiρ λjλ λkα W −5 ∇b λkβ −
 1                                                5
16
   (Γa )αβ (Γb )ρλ Xij λiα λjρ λkλ W −5 ∇b λkβ + 32 (Γa )αβ (Γb )ρλ Xij λiα λjρ λkβ W −5 ∇b λkλ −
1
4
  (Γa )αβ (Γb )ρλ Xij λiρ λkα λkλ W −5 ∇b λjβ − 32
                                                13
                                                   (Γa )αβ (Γb )ρλ Xij λiα λjβ λkρ W −5 ∇b λkλ +
 1
32
   (Γa )αβ (Γb )ρλ Xij λiα λkβ λkρ W −5 ∇b λjλ − 16
                                                  3
                                                    (Γa )αβ (Γb )ρλ λkα λkρ λiβ λjλW −5 ∇b X ij +
 3
16
   i(Γa )αβ Xij X ij Xkl λkα λlβ W −5 − 38 i(Γa )αβ Xij X i k X j l λkα λlβ W −5 −
3 adebc                                         45 adebc
8
  iǫ    (Σde )αβ Fbc λiα λiβ W −5 ∇e1 W ∇e1 W + 256 iǫ   (Σde )αβ Wbc λiα λiβ W −4 ∇e1 W ∇e1 W −
 3 adebc
32
   iǫ    (Σde )αβ Wbc W −2 ∇e1 λiα ∇e1 λiβ − 81 iǫadebc (Σde )αβ λiα λiβ W −3 ∇e1 ∇e1 Fbc −

                                                         46
```

</details>

<a id="src-c24-p146"></a>

<details>
<summary>C24-p146 — PDF page 146: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p146: PDF page 146](https://arxiv.org/pdf/2311.00679v1#page=146) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 9 ae1 e2 bc                                          9
64
   iǫ        (Σe1 e2 )αβ W de Fbc Fde λiα λiβ W −4 + 128 iǫabcde (Σe1 e2 )αβ W e1e2 Fbc Fde λiα λiβ W −4 +
 9 e1 bcde                                          9 e2 bcde
64
   iǫ      (Σae2 )αβ We1 e2 Fbc Fde λiα λiβ W −4 − 64 iǫ      (Σe2 e1 )αβ W ae1 Fbc Fde λiα λiβ W −4 −
 3                                                       1 dee1 bc
128
    iǫae1 e2 de (Σe1 e2 )αβ W bc Wde Fbc λiα λiβ W −3 − 64 iǫ      (Σae2 )αβ Wde We1 e2 Fbc λiα λiβ W −3 −
 3                                                    1 e2 dee1 b
128
    iǫbcdee1 (Σae2 )αβ Wbc Wde We1 e2 λiα λiβ W −2 − 32 iǫ        (Σe2 a )αβ Wde We1 c Fbc λiα λiβ W −3 +
 1 ae1 e2 eb                                          9 e1 e2 bcd
32
   iǫ        (Σe1 e2 )αβ W dc Wed Fbc λiα λiβ W −3 + 64 iǫ        (Σae )αβ We1 e2 Fbc Fde λiα λiβ W −4 +
 9 e2 e1 bcd                                          9 ae1 e2 bd
32
   iǫ        (Σe2 a )αβ We1 e Fbc Fde λiα λiβ W −4 + 32 iǫ        (Σe1 e2 )αβ W ce Fbc Fde λiα λiβ W −4 −
5                                           1
8
  iW bcα i (Σbc )βρ λiα λjβ λjρ W −4 ∇a W + 64 iW bcα i (Σbc )βρ λiβ λjα λjρ W −4 ∇a W +
 3
64
   iW a b α i λiβ λjα λjβ W −4 ∇b W + 128
                                      19
                                          iWbc α i ǫabc de (Γd )βρ λiβ λjα λjρ W −4 ∇e W −
 7                                              7
32
   iW b c α i (Σa b )βρ λiβ λjα λjρ W −4 ∇c W + 32 iW abα i (Σbc )βρ λiβ λjα λjρ W −4 ∇c W −
1
4
  iW b c α i (Σa b )βρ λiα λjβ λjρ W −4 ∇c W + 14 iW abα i (Σbc )βρ λiα λjβ λjρ W −4 ∇c W −
 33 adebc                                     3 adebc
128
    iǫ    (Σde )βρ Fbc λjβ λjρ λαi Xαi W −4 + 64 iǫ   (Σde )βρ Fbc λjβ λjαλiρ Xαi W −4 −
3                                       3 adebc
8
  i(Γb )βρ Fb a λjβ λjα λiρ Xαi W −4 − 16 iǫ    (Σde )βα Fbc λjβ λjρλiρ Xαi W −4 +
3
8
  i(Γb )βα Fb a λjβ λjρ λiρ Xαi W −4 − 38 i(Σbc )λα (Γa )βρ F bc λjλ λjβ λiρ Xαi W −4 +
 7
64
   i(Σbc )ρλ (Γa )βα F bc λjρλjβ λiλ Xαi W −4 − 128
                                                 65
                                                    i(Σbc )ρλ (Γa )βα F bc λjρλjλ λiβ Xαi W −4 −
1567 adebc                                      487 adebc
6144
     iǫ    (Σde )βρ Wbc λjβ λjρ λαi Xαi W −3 + 6144 iǫ    (Σde )βρ Wbc λjβ λjα λiρ Xαi W −3 −
1207
3072
     i(Γb )βρ Wb a λjβ λjαλiρ Xαi W −3 − 1207
                                         6144
                                              iǫadebc (Σde )βα Wbc λjβ λjρ λiρ Xαi W −3 +
1207
3072
     i(Γb )βα Wb a λjβ λjρλiρ Xαi W −3 − 1207
                                         3072
                                              i(Σbc )λα (Γa )βρ W bc λjλ λjβ λiρ Xαi W −3 +
1039
3072
     i(Σbc )ρλ (Γa )βα W bc λjρ λjβ λiλ Xαi W −3 − 1291
                                                   3072
                                                        i(Σbc )ρλ (Γa )βα W bc λjρ λjλ λiβ Xαi W −3 −
 3 adebc                                       15 adebc
32
   iǫ    (Σde )αβ Xij X ij Fbc λkα λkβ W −5 − 256 iǫ    (Σde )αβ Xij X ij Wbc λkα λkβ W −4 +
 3 adebc                                       15 adebc
16
   iǫ    (Σde )αβ Xij X i k Fbc λjα λkβ W −5 + 128 iǫ   (Σde )αβ Xij X i k Wbc λjα λkβ W −4 +
 73                                      47
128
    i(Γa )βρ Xij λiβ λjρ λαk Xαk W −4 − 128 i(Γa )βρ Xij λiβ λjα λkρXαk W −4 +
 73                                      33
128
    i(Γa )βα Xij λiβ λjρ λkρ Xαk W −4 + 128 i(Γa )βρ Xij λiβ λkρ λkα Xαj W −4 +
 47                                      7
128
    i(Γa )βα Xij λiρ λjρ λkβ Xαk W −4 + 128 i(Γa )βα Xij λiρ λkβ λkρ Xαj W −4 +

  ǫ de (Σbc )αβ λiα λiβ λρj W −5 ∇d W ∇e λjρ + 43 (Σbc )ρλ (Γa )αβ λiρ λiα λjβ W −5 ∇b W ∇c λjλ +
1 abc
2

15 a
16
   ǫ de bc (Γd )αβ Fbc λiα λiρ λjβ λjρ W −6 ∇e W − 15
                                                    8
                                                      (Σa d )αβ (Σbc )ρλ F bc λiα λiβ λjρλjλ W −6 ∇d W −

                                                        47
```

</details>

<a id="src-c24-p147"></a>

<details>
<summary>C24-p147 — PDF page 147: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p147: PDF page 147](https://arxiv.org/pdf/2311.00679v1#page=147) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 9
32
   W a b λαi λiβ λjα λjβ W −5 ∇b W + 63
                                     64
                                        ǫa de bc (Γd )αβ Wbc λiα λiρ λjβ λjρ W −5 ∇e W −
15
16
   (Σa d )αβ (Σbc )ρλ W bc λiα λiβ λjρλjλ W −5 ∇d W + 16
                                                      15
                                                         (Σa d )αβ (Σbc )ρλ W bc λiα λiρ λjβ λjλ W −5 ∇d W −

  F b λαi λiβ λjα λjβ W −6 ∇b W − 58 (Γa )αβ (Γb )ρλ Fbc λiα λiρ λjβ λjλ W −6 ∇c W +
5 a
8

5
8
  (Γc )αβ (Γb )ρλ Fb a λiα λiρ λjβ λjλ W −6 ∇c W − 32
                                                   9
                                                      (Γa )αβ (Γb )ρλ Wbc λiα λiρ λjβ λjλ W −5 ∇c W +
 9
32
   (Γc )αβ (Γb )ρλ Wb a λiα λiρ λjβ λjλ W −5 ∇c W + 45 (Σa b )αβ Xij λiα λjρλkβ λkρ W −6 ∇b W +
15
 8
   (Σa b )αβ Xij λiρ λjρ λkα λkβ W −6 ∇b W + 58 (Γa )αβ (Γb )ρλ Xij λiα λjρ λkβ λkλ W −6 ∇b W +
 3 adebc                                       1 e1 bcde
16
   iǫ    (Σde )αβ Fbc λiα λiβ W −4 ∇e1 ∇e1 W + 16 iǫ     (Σe1 a )βρ Fbc Wde α i λiα λjβ λjρ W −4 −
1                                                    21
8
  iFb c Wdc α i ǫabdee1 (Σee1 )βρ λiα λjβ λjρ W −4 + 128 i(Γa )βρ F bc Wbc α i λiβ λjρλjα W −4 +
 5 abcde
64
   iǫ    Fbc Wde α i λiβ λjαλjβ W −4+ 32
                                       1 e1 bcde
                                         iǫ      (Σe1 a )βρ Fbc Wde α i λiβ λjρ λjα W −4 −
 1                                                     1
16
   iFb c Wdc α i ǫabdee1 (Σee1 )βρ λiβ λjα λjρ W −4 − 16 iF ab Wbc α i (Γc )βρ λiβ λjα λjρ W −4 −
 1                                             1
16
   iFb c W a c α i (Γb )βρ λiβ λjα λjρ W −4 + 32 i(Σe1 e )βρ Fbc Wde α i ǫae1 bcd λiα λjβ λjρ W −4 +
 1 ee1 bcd
64
   iǫ                                                 1
           (Σee1 )βρ Fb a Wcd α i λiα λjβ λjρ W −4 + 256 iFbc Wde α i ǫabcde λiβ λjαλjβ W −4 −
 1                                             1
64
   i(Γb )βρ Fb c W a c α i λiβ λjρ λjα W −4 + 64 i(Σe1 e )βρ Fbc Wde α i ǫae1 bcd λiβ λjρ λjα W −4 +
 1                                                       1
128
    iǫee1 bcd (Σee1 )βρ Fb a Wcd α i λiβ λjρ λjα W −4 − 64 i(Γc )βρ F ab Wcb α i λiβ λjρ λjα W −4 +
 1171 e1 bcde                                           1267
12288
      iǫ      (Σe1 a )βρ Wbc Wde α i λiα λjβ λjρ W −3 − 6144 iWb c Wdc α i ǫabdee1 (Σee1 )βρ λiα λjβ λjρ W −3 +
 865
4096
                                               289 abcde
     i(Γa )βρ W bc Wbc α i λiβ λjρ λjα W −3 + 8192 iǫ    Wbc Wde α i λiβ λjα λjβ W −3 −
  19                                                     115
12288
      iǫe1 bcde (Σe1 a )βρ Wbc Wde α i λiβ λjρλjα W −3 + 6144 iWb c Wdc α i ǫabdee1 (Σee1 )βρ λiβ λjα λjρ W −3 −
1139
6144
     iW ab Wbc α i (Γc )βρ λiβ λjα λjρ W −3 − 1139
                                              6144
                                                   iWb c W a c α i (Γb )βρ λiβ λjαλjρ W −3 +
 5                                                       5
192
    i(Σe1 e )βρ Wbc Wde α i ǫae1 bcd λiα λjβ λjρ W −3 + 384 iǫee1 bcd (Σee1 )βρ Wb a Wcd α i λiα λjβ λjρ W −3 +
  5
1536
     iWbc Wde α i ǫabcde λiβ λjα λjβ W −3 − 384
                                             5
                                                i(Γb )βρ Wb c W a c α i λiβ λjρ λjα W −3 +
 5                                                       5
384
    i(Σe1 e )βρ Wbc Wde α i ǫae1 bcd λiβ λjρ λjα W −3 + 768 iǫee1 bcd (Σee1 )βρ Wb a Wcd α i λiβ λjρ λjα W −3 −
 5                                            1
384
    i(Γc )βρ W ab Wcb α i λiβ λjρ λjα W −3 + 768 i(Γa )αβ W bc Wbcαi λiρ λjβ λjρ W −3 −
 1                                                     1
768
    iǫe1 bcde (Σe1 a )αβ Wbc Wdeαi λiρ λjβ λjρ W −3 + 384 iWb c Wdc α i ǫabdee1 (Σee1 )α β λiρ λjβ λjρ W −3 −
 1                                             1
384
    iW ab Wbc α i (Γc )α β λiρ λjβ λjρ W −3 − 384 iWb c W a c α i (Γb )α β λiρ λjβ λjρ W −3 −
 9
128
    iWb aα i (Γb )βρ Xjk λiα λjβ λkρ W −4 + 128
                                             3
                                                iWbc α i ǫabcde (Σde )βρ X i j λjβ λkαλkρ W −4 −

                                                         48
```

</details>

<a id="src-c24-p148"></a>

<details>
<summary>C24-p148 — PDF page 148: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p148: PDF page 148](https://arxiv.org/pdf/2311.00679v1#page=148) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1
16
   iWb aα i (Γb )βρ X i j λjβ λkα λkρ W −4 + 384
                                              7 abcde
                                                 ǫ    Φbcij (Σde )αβ λiα λjρ λkβ λkρ W −4 −
 1                                    13 abcde
   Φ a (Γb )αβ λiα λjρλkβ λkρ W −4 + 768
96 b ij
                                         ǫ     Φbcij (Σde )αβ λiρ λjρ λkα λkβ W −4 +

   Φ ij (Σbc )ρλ (Γa )αβ λiα λjβ λkρ λkλ W −4 + 96
 3 bc
64
                                                1 bc
                                                   Φ ij (Σbc )ρλ (Γa )αβ λiρ λjα λkλ λkβ W −4 +
 9                                         11
64
   (Γa )αβ Xij X ij λkα λkρ λlβ λlρ W −6 − 16 (Γa )αβ Xij X i k λjα λkρ λlβ λlρ W −6 −
19
32
   (Γa )αβ Xij Xkl λiα λjβ λkρ λlρ W −6 − 32
                                           1
                                             (Γa )αβ Xij Xkl λiα λjρ λkβ λlρ W −6 +
1
8
  (Γa )αβ λiα λiρ λjρW −4 ∇b ∇b λjβ + 64
                                       5 abcde
                                         ǫ     Fbc Fde λαi λiβ λjα λjβ W −6 −
5                                          5
8
  (Γc )αβ F ab Fcb λiα λiρ λjβ λjρ W −6 + 16 (Γa )αβ F bc Fbc λiα λiρ λjβ λjρ W −6 −
15 ae1 e2 de
32
   ǫ         (Σe1 e2 )αβ (Σbc )ρλ F bc Fde λiα λiβ λjρ λjλ W −6 − 64
                                                                   5
                                                                     ǫe1 bcde (Γa )αβ (Γe1 )ρλ Fbc Fde λiα λiρ λjβ λjλ W −6 +
 9 adebc
64
   ǫ     Wde Fbc λαi λiβ λjα λjβ W −5 − 16
                                         9
                                           (Γc )αβ Wcb F ab λiα λiρ λjβ λjρ W −5 +
 9                                          9
16
   (Γa )αβ W bc Fbc λiα λiρ λjβ λjρ W −5 − 16 (Γb )αβ W ac Fbc λiα λiρ λjβ λjρ W −5 −
 7 ae1 e2 de
16
   ǫ         (Σe1 e2 )αβ (Σbc )ρλ Wde F bc λiα λiβ λjρλjλ W −5 − 32
                                                                  1 ae1 e2 de
                                                                    ǫ         (Σe1 e2 )αβ (Σbc )ρλ Wde F bc λiα λiρ λjβ λjλ W −5 +
 171 abcde
2048
     ǫ     Wbc Wde λαi λiβ λjαλjβ W −4 − 171
                                         256
                                             (Γc )αβ W ab Wcb λiα λiρ λjβ λjρ W −4 +
171
512
    (Γa )αβ W bc Wbc λiα λiρ λjβ λjρ W −4− 21
                                           64
                                              ǫae1 e2 de (Σe1 e2 )αβ (Σbc )ρλ W bc Wde λiα λiβ λjρλjλ W −4 +
177 ae1 e2 de
512
    ǫ         (Σe1 e2 )αβ (Σbc )ρλ W bc Wde λiα λiρ λjβ λjλ W −4 + 32
                                                                   9 ae1 e2 bc
                                                                      ǫ        (Σe1 e2 )αβ (Σde )ρλ W de Fbc λiα λiρ λjβ λjλ W −5 −
 9 ae1 e2 bc
32
   ǫ         (Σe1 e2 )αβ (Σde )ρλ W de Fbc λiα λiβ λjρλjλ W −5 − 64
                                                                  9
                                                                    ǫe1 debc (Γa )αβ (Γe1 )ρλ Wde Fbc λiα λiρ λjβ λjλ W −5 −
 171
     ǫ bcde (Γa )αβ (Γe1 )ρλ Wbc Wde λiα λiρ λjβ λjλ W −4 − 32
2048 e1
                                                             5 adebc
                                                               ǫ     (Σde )αβ Xij Fbc λiα λjρ λkβ λkρ W −6 +
5
8
  (Γb )αβ Xij Fb a λiα λjρ λkβ λkρ W −6 + 25
                                          64
                                             ǫadebc (Σde )αβ Xij Fbc λiρ λjρ λkα λkβ W −6 +
5
8
  (Σbc )ρλ (Γa )αβ Xij F bc λiα λjβ λkρ λkλ W −6 − 128
                                                    5 adebc
                                                       ǫ    (Σde )αβ Xij Wbc λiα λjρ λkβ λkρ W −5 +
 9                                         77 adebc
16
   (Γb )αβ Xij Wb a λiα λjρλkβ λkρ W −5 + 256 ǫ     (Σde )αβ Xij Wbc λiρ λjρ λkα λkβ W −5 +
 45
128
    (Σbc )ρλ (Γa )αβ Xij W bc λiα λjβ λkρ λkλ W −5 + 27
                                                     64
                                                        (Σbc )ρλ (Γa )αβ Xij W bc λiρ λjα λkλ λkβ W −5 +
31                                       15
64
   (Γa )βρ λjβ λjλλkρ λkλ λαi Xαi W −5 + 64 (Γa )βρ λjβ λjλλkρ λkα λiλ Xαi W −5 −
17
64
   (Γa )βρ λjβ λjλλiρ λkλ λkα Xαi W −5 + 25
                                         32
                                            (Γa )βα λjβ λjρ λkρ λkλλiλ Xαi W −5 +
 7
64
   (Γa )βα λiβ λρj λjλλkρ λkλ Xαi W −5 + 32
                                          5
                                            iλαi λiβ λjα λjβ λρk W −6 ∇a λkρ +

  iλ λ λjα λjρλkβ W −6 ∇a λkρ − 54 i(Σa b )αβ λiα λiρ λjβ λjλλkρ W −6 ∇b λkλ +
15 α iβ
16 i

15
 8
                                                5
   i(Σa b )αβ λiα λiρ λjρλjλ λkλ W −6 ∇b λkβ + 16 i(Σa b )αβ λiα λρj λjλλkρ λkλ W −6 ∇b λiβ +

                                                         49
```

</details>

<a id="src-c24-p149"></a>

<details>
<summary>C24-p149 — PDF page 149: Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149</summary>

[C24-p149: PDF page 149](https://arxiv.org/pdf/2311.00679v1#page=149) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
25
64
   i(Γa )αβ (Γb )ρλ λiα λiρ λjβ λjλ λγk W −6 ∇b λkγ − 32
                                                       5
                                                         i(Γa )αβ (Γb )ρλ λiα λiρ λjλλjγ λkγ W −6 ∇b λkβ +
15                                                     5
32
   i(Γa )αβ (Γb )ρλ λiα λiρ λjβ λjγ λkλ W −6 ∇b λkγ + 32 i(Γa )αβ (Γb )ρλ λiα λiρ λjβ λjγ λkγ W −6 ∇b λkλ +
 5
32
   i(Γa )αβ (Γb )ρλ λiα λiγ λjρλjγ λkλ W −6∇b λkβ + 25
                                                    64
                                                       i(Γa )αβ (Γb )ρλ λiα λiγ λjβ λjγ λkρ W −6 ∇b λkλ −
1
4
  (Γa )αβ λiα λiρ λjβ λjρ W −5 ∇b ∇b W − 14 W bcα i (Σbc )λγ (Γa )βρ λiβ λjαλjλ λkγ λkρ W −5 −
 1
32
   Wbc α i ǫabcde (Σde )βρ λiλ λjα λjβ λkρ λkλ W −5 + 16
                                                      1
                                                         Wb aα i (Γb )βρ λiλ λjα λjβ λkρλkλ W −5 −
 1
16
   Wbc α i ǫabcde (Σde )βρ λiλ λjα λjλ λkβ λkρ W −5 − 16
                                                      15
                                                         i(Σa b )αβ λiα λiβ λρj λjλλkρ λkλ W −7 ∇b W +
15
 8
   i(Σa b )αβ λiα λiρ λjβ λjλ λkρλkλ W −7 ∇b W − 15
                                                 16
                                                    i(Γa )αβ (Γb )ρλ λiα λiρ λjβ λjγ λkλ λkγ W −7 ∇b W +
 3
32
   i(Γa )αβ Xij λiα λjβ λρk λkλ λlρ λlλ W −7 − 83 i(Γa )αβ Xij λiα λjρλkβ λkλ λlρ λlλ W −7 +
3                                             9
4
  i(Γa )αβ Xij λiρ λjρ λkα λkλ λlβ λlλ W −7 + 16 i(Γa )αβ Xij λiρ λjλ λkα λkρ λlβ λlλ W −7 −
15 adebc
64
   iǫ    (Σde )αβ Fbc λiα λiβ λρj λjλ λkρλkλ W −7 + 15
                                                    32
                                                       iǫadebc (Σde )αβ Fbc λiα λiρ λjβ λjλ λkρλkλ W −7 −
15
16
   i(Σbc )ρλ (Γa )αβ F bc λiρ λiλ λjα λjγ λkβ λkγ W −7 − 15
                                                         64
                                                            iǫadebc (Σde )αβ Wbc λiα λiβ λρj λjλ λkρλkλ W −6 +
15 adebc
32
   iǫ    (Σde )αβ Wbc λiα λiρ λjβ λjλ λkρ λkλ W −6 + 45
                                                     64
                                                        i(Σbc )ρλ (Γa )αβ W bc λiρ λiα λjλ λjγ λkβ λkγ W −6 −
 75                                                       21
128
    i(Σbc )ρλ (Γa )αβ W bc λiρ λiλ λjα λjγ λkβ λkγ W −6 + 64 (Γa )αβ λiα λiρ λjβ λjρ λλk λkγ λlλ λlγ W −8 −
21
32
   (Γa )αβ λiα λiρ λjβ λjλ λkρ λkγ λlλ λlγ W −8

3      Curvature-squared actions

3.1      Log Degauged and Gauge-fixed bosonic Lagrangian

                               5
   1
− 12 νe ǫeabcd Φabij Φcd ij − 16 RW ab Fab + 13 Ra c W cbFab − 32
                                                                3
                                                                  RF ab Fab + 13 Rc a F ab Fcb −
 3
64
   W ab Fab Y + 34 ǫcdeab D e1 Wcd Wee1 Fab + 64
                                              3
                                                 W cd W ab Wcd Fab + 49 W cd Wca Wdb F ab +
11
   R W cd F ab − 43 Rca W c b F ab − 49 Dc D c Wab F ab + 128
12 cdab
                                                           3                3 eabcd e1
                                                              F ab Fab Y − 16 ǫ    D Wee1 Fab Fcd −
3 ee1 acd                     75
8
  ǫ       Wee1 D b Fab Fcd − 128 W cd Wcd F ab Fab + 94 W dc Wda F ab Fcb − 12 Φabij X ij F ab +
1
  R F ab F cd − 31 Rac F a b F cb − 16
3 abcd
                                     1 acdee1 b
                                       ǫ     D Fab Fcd Fee1 − 83 W cdF ab Fcd Fab +
3                     1
4
  W cd F ab Fca Fdb − 32 F ab F cdFab Fcd + 81 F ab F cdFac Fbd − 16
                                                                   1
                                                                     Xij X ij F ab Fab +

                                                        50
```

</details>

<a id="src-c24-p300"></a>

<details>
<summary>C24-p300 — PDF page 300: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p300: PDF page 300](https://arxiv.org/pdf/2311.00679v1#page=300) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3
   G G (Σab )αβ W ab λlρ λm
64 ik lm
                             −5    k    3            αβ  ab    −3 k
                          α G ϕjρ ϕβ − 64 iGij (Σab ) W F Xkα G ϕβ −

 3                                    3                         9
64
   iGij (Γa )αβ W Xkα G−3 ∇a W ϕkβ − 128 Gik W Y λkα G−3 ϕjα + 64                 α −5 l m
                                                                  iGik Gjl W λkβ Xm G ϕα ϕβ −
 3                                    9
   G (Γa )βα W λkβ Xlα G−3 ∇a Gj l + 64
64 ik
                                        iGik Glm W λlβ X mα G−5 ϕjβ ϕkα +
 3                                   3
   G (Γa )βα W λkβ Xαl G−3 ∇a Gij − 16
64 kl
                                       iGik Gjl (Σab )αβ Xk m F ab G−5 ϕlα ϕm
                                                                            β−

 3                                             3
16
   iGik Gjl (Σab )αβ W Xk m W ab G−5 ϕlα ϕm                    αβ k  −5 a  l m
                                          β − 16 iGik Gjl (Γa ) X m G ∇ W ϕα ϕβ +

1                            3
  G Xk l G−3 ∇a W ∇a Gj l + 32
4 ik
                               iGkl Xk m λlα G−5 ϕβi ϕjβ ϕm   15               m    nα −7 kβ l i1
                                                          α + 32 iGik Gjl Gmn X i1 λ G ϕ ϕβ ϕα −

 3                              3
16
   F Gij Gkl Xk m λlα G−5 ϕm                   αβ l  m −5 a  n k
                           α − 16 Gik Glm (Γa ) X n λα G ∇ Gj ϕβ +

 15
    G G Xk m λlα Xαm G−3
256 ij kl

5       Degauged Expressions

5.1       Weyl Multiplet

5.1.1      ∇c ∇d Wab

D c ∇d Wâb̂ − 12 ψ c i α ∇d Wâb̂α i − 12 (Σâb̂ )α β ψ c i β ∇d Xαi + 81 ǫde2 e3 ee1 (Σe2 e3 )α β ψ c i β Wee1 Wâb̂α i +
3                                   3                               1 d
8
  (Γe )α β ψ c i β W de Wâb̂α i − 16 (Γd )α β ψ c i β Wâb̂ Xαi − 32 ǫ âb̂ ee1 ψ c i α Wee1 Xαi +
 3 e2                                         3 de1 e2 e
32
   ǫ âb̂ ee1 (Σe2 d )α β ψ c i β Wee1 Xαi − 16 ǫ                 α   c β      i
                                                      â (Σe1 e2 ) β ψ i Wb̂e Xα −

3
8
  (Γe )α β δ d â ψ c i β Wb̂e Xαi + 12 (Γâ )α β ψ c i β Wb̂ d Xαi + 16
                                                                       1 de2
                                                                         ǫ âb̂ e (Σe2 e1 )α β ψ c i β Wee1 Xαi +
 1 d                                                   1
16
   ǫ âb̂ e2 e3 (Σee1 )α β ψ c i β W ee1 We2 e3 α i + 16 ǫâb̂ ee1 e2 ψ c i α We d We1 e2 α i +
1
4
  (Γâ )α β ψ c i β Wb̂ e W d eα i − 18 (Γe )α β ψ c i β Wâb̂ We d α i + 81 (Γb̂ )α β δ d â ψ c i β W ee1 Wee1 α i −
1
4
  (Γe1 )α β δ d â ψ c i β Wb̂ e We1 eα i + 81 ǫâb̂ ee2 e3 (Σde1 )α β ψ c i β Wee1 We2 e3 α i −

  ǫ âb̂ e1 e2 (Σe3 e )α β ψ c i β W de We1 e2 α i − 41 (Γd )α β ψ c i β Wâ e Wb̂eα i −
1 e3
8

1 d ee1 e2 c α
8
  ǫ â    ψ i Wee1 Wb̂e2 α i + 14 ǫe3 â ee1 e2 (Σe3 d )α β ψ c i β Wee1 Wb̂e2 α i +
1 de2 e3 ee1
4
  ǫ          (Σe2 e3 )α β ψ c i β Wâe Wb̂e1 α i + 41 (Γe )α β ψ c i β Wâ d Wb̂eα i −
1
4
  (Γe )α β ψ c i β Wâe Wb̂ d α i − 41 ǫde2 e3 âe (Σe2 e3 )α β ψ c i β W ee1 Wb̂e1 α i −

                                                              201
```

</details>

<a id="src-c24-p301"></a>

<details>
<summary>C24-p301 — PDF page 301: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p301: PDF page 301](https://arxiv.org/pdf/2311.00679v1#page=301) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1
4
  (Γe )α β δ d â ψ c i β We e1 Wb̂e1 α i + 41 (Γâ )α β ψ c i β W de Wb̂eα i + 81 ǫd âb̂ ee2 ψ c i α We e1 We2 e1 α i −
 1                                               1
   ǫ ee1 e2 e3 δ d â ψ c i α Wee1 We2 e3 α i + 16
16 b̂
                                                   ǫâb̂ ee1 e2 ψ c i α Wee1 We2 d α i −
1 d ee1 e2 c α                   1 e2 e3 ee1
8
  ǫ â    ψ i Wb̂e We1 e2 α i − 32 ǫ    b̂   (Σe2 e3 )α β δ d â ψ c i β Wee1 Xαi −
1
2
  i(Γd )α β φc i β Wâb̂α i − 41 iǫdee1 âb̂ (Σee1 )α β φc i β Xαi − 12 i(Γb̂ )α β δ d â φc i β Xαi −

2Wâb̂ f cd − 4δ d â Wb̂e f ce − 4Wâ d f c b̂

5.1.2      ∇a ∇b Xαi

D a ∇b Xαi − 31 i(Σcd )αβ ψ a j β ∇b Φcdij − 16
                                              1
                                                iψ ai α ∇b Y + 41 iǫee1 e2 cd (Σee1 )αβ ψ aiβ ∇b ∇e2 Wcd −
1                             5
4
  i(Γc )αβ ψ aiβ ∇b ∇d Wcd − 32 iǫe2 ee1 cd (Γe2 )αβ ψ aiβ Wcd ∇b Wee1 − 12 i(Σc e )αβ ψ aiβ Wcd ∇b W ed −
 1 ee1 e2 cd                                   7 bee1 e2 c
48
   iǫ        Φee1 ij (Σe2 b )αβ ψ a j β Wcd + 24 iǫ        Φe dij (Σe1 e2 )αβ ψ a j β Wcd −
1
4
  iΦdc ij (Γd )αβ ψ a j β W bc − 31 iΦbcij (Γd )αβ ψ a j β Wcd + 128
                                                                  1
                                                                     iǫbee1 cd (Σee1 )αβ ψ aiβ Wcd Y −
 1                          7
32
   i(Γc )αβ ψ aiβ Wc b Y + 256 iǫe2 ee1 cd (Γb )αβ ψ aiβ Wcd ∇e2 Wee1 − 12 i(Σc e )αβ ψ aiβ Wcd ∇d W be +
3
8
  i(Σde )αβ ψ aiβ W b c ∇c W de + 21 i(Σc e )αβ ψ aiβ Wcd ∇e W bd + 34 i(Σed )αβ ψ aiβ W b c ∇e W dc −
 3 b                                         13
32
   iǫ e2 ee1 c (Γd )αβ ψ aiβ Wcd ∇e2 Wee1 + 128 iǫe1 e2 dec (Γe1 )αβ ψ aiβ Wc b ∇e2 Wde −
1                                1 b
4
  i(Σcd )αβ ψ aiβ W cd∇e W be + 16 iǫ e2 ecd (Γe2 )αβ ψ aiβ Wcd ∇e1 Wee1 +
 1
16
   iψ ai α W b c ∇d W dc − 38 i(Σcd )αβ ψ aiβ W bc ∇e W de + 128
                                                              3
                                                                 iǫbe2 e3 ee1 (Σe2 e3 )αβ ψ aiβ W cd Wee1 Wcd +
 5                                 1 bee1 e2 e3
64
   i(Γe )αβ ψ aiβ W cd We b Wcd − 16 iǫ         (Σcd )αβ ψ aiβ W cd Wee1 We2 e3 −
 5                                  5 cdee1 e2
16
   i(Γe )αβ ψ aiβ W cd Wec W b d − 32 iǫ       (Σbe3 )αβ ψ aiβ Wcd Wee1 We2 e3 +
 5 e3 dee1 e2                                     1
32
   iǫ         (Σe3 c )αβ ψ aiβ W bc Wde We1 e2 + 256 iǫbee1 cd (Γe2 )αβ ψ aiβ Wcd ∇e2 Wee1 −
 3 b                                          1 bee1 e2 c
64
   iǫ e1 e2 e c (Γe1 )αβ ψ aiβ Wcd ∇e2 W ed + 24 iǫ       Φee1 ij (Σe2 d )αβ ψ a j β Wcd +
 1 ee1 e2 cd                                   1
48
   iǫ        Φe bij (Σe1 e2 )αβ ψ a j β Wcd + 128 iǫb e2 ecd(Γe1 )αβ ψ aiβ Wcd ∇e2 Wee1 −
 3                                             5
128
    iǫb e2 ee1 c (Γe2 )αβ ψ aiβ Wcd ∇d Wee1 + 16 i(Γd )αβ ψ aiβ W bc Wd e Wec +
 1
   iǫ
16 e1 e2 e
           cd
              (Γe1 )αβ ψ aiβ Wcd ∇e2 W be − 18 ǫbee1 cd (Σee1 )αρ ψ a j ρ X iβ Wcdβ j +
1                                  1 bee1 cd                                 1
4
  (Γc )αρ ψ a j ρ X iβ Wc b β j − 16 ǫ       (Σee1 )α ρ ψ a j β Xρi Wcdβ j + 16 (Γb )α ρ ψ a j β Xβi Xρj +

                                                               202
```

</details>

<a id="src-c24-p302"></a>

<details>
<summary>C24-p302 — PDF page 302: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p302: PDF page 302](https://arxiv.org/pdf/2311.00679v1#page=302) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1
16
                             1
   (Γb )βρ ψ a jα Xβi Xρj − 16 (Γb )αρ ψ a j ρ X iβ Xβj + 41 (Γb )β ρ ψ a j ρ Xβi Xαj +
 3
16
   (Γb )β ρ ψ a j ρ Xαi Xβj + 16
                               3
                                 (Γb )β ρ ψ aiρ Xjα Xβj + 12
                                                          1 bee2 cd
                                                             iǫ     Φe e1 ij (Σe2 e1 )αβ ψ a j β Wcd −
 1 dee1 e2 c
24
   iǫ        Φde ij (Σe1 e2 )αβ ψ a j β Wc b − 21 (Σcd )αβ φaiβ ∇b W cd + 16 ǫbcdee1 Φcd ij (Σee1 )αβ φa j β −
1                        1
  Φ bij (Γc )αβ φa j β + 16
3 c
                            (Γb )αβ φaiβ Y − 14 φai α ∇c W bc − 14 ǫb ee1 cd (Γe )αβ φaiβ ∇e1 Wcd −
1                                                 1 bcdee1 ai
2
  (Σb c )αβ φaiβ ∇d W cd−(Σdc )αβ φaiβ ∇d W bc − 16 ǫ     φ α Wcd Wee1 +
 1 e2 cdee1
16
   ǫ        (Σe2 b )αβ φaiβ Wcd Wee1 + 14 (Γd )αβ φaiβ W bc Wdc − 81 ǫbe2 cde (Σe2 e1 )αβ φaiβ Wcd Wee1 −
 1 e1 e2 cde
16
   ǫ         (Σe1 e2 )αβ φaiβ Wcd We b − 3Xαi f ab + 2(Σb c )α β Xβi f ac

5.1.3     ∇a ∇b Wαβγ i

                                    5                      3
  D a ∇b Wαβγ i −iψ aiρ ∇b Cαβγρ − 16 iψ aiρ Wγρ ∇b Wαβ − 16 iψ aiρ Wαβ ∇b Wγρ −
   5                       3                      3
   16
      iψ aiρ Wβρ ∇b Wαγ − 16 iψ aiρ Wαγ ∇b Wβρ − 16 iψ aiρ Wβγ ∇b Wαρ −
   5
   16
      iψ aiρ Wαρ ∇b Wβγ + 14 i(Γc )αρ ψ aiρ ∇b ∇c Wβγ + 14 i(Γc )βρ ψ aiρ ∇b ∇c Wαγ +
   1
   4
     i(Γc )γρ ψ aiρ ∇b ∇c Wαβ + 18 i(Γc )β ρ ψ ai α ∇b ∇c Wγρ + 81 i(Γc )γ ρ ψ ai α ∇b ∇c Wβρ +
   1
   8
     i(Γc )γ ρ ψ ai β ∇b ∇c Wαρ + 18 i(Γc )α ρ ψ ai β ∇b ∇c Wγρ + 18 i(Γc )α ρ ψ ai γ ∇b ∇c Wβρ +
   1
   8
     i(Γc )β ρ ψ ai γ ∇b ∇c Wαρ − 31 iψ a jα ∇b Φβγ ij − 13 iψ a jβ ∇b Φαγ ij −
   1
   3
     iψ a jγ ∇b Φαβ ij − 34 i(Γb )λ τ ψ aiτ Cαβγ ρ Wλρ + 16
                                                          3
                                                            i(Γb )λ τ ψ aiτ Wαβ Wγ ρ Wλρ +
   3                                 3                                  3
   16
      i(Γb )λ τ ψ aiτ Wαγ Wβ ρ Wλρ + 16 i(Γb )λ τ ψ aiτ Wα ρ Wβγ Wλρ + 16 i(Γb )ρ τ (Γc )α λ ψ aiτ Wρλ ∇c Wβγ +
   3                                        3
   16
      i(Γb )ρ τ (Γc )β λ ψ aiτ Wρλ ∇c Wαγ + 16 i(Γb )ρ τ (Γc )γ λ ψ aiτ Wρλ ∇c Wαβ −
   3                                         3
   32
      i(Γb )ρ τ (Γc )β λ ψ aiτ Wαρ ∇c Wγλ − 32 i(Γb )ρ τ (Γc )γ λ ψ aiτ Wαρ ∇c Wβλ −
   3                                         3
   32
      i(Γb )ρ τ (Γc )γ λ ψ aiτ Wβρ ∇c Wαλ − 32 i(Γb )ρ τ (Γc )α λ ψ aiτ Wβρ ∇c Wγλ −
   3                                         3
   32
      i(Γb )ρ τ (Γc )α λ ψ aiτ Wγρ ∇c Wβλ − 32 i(Γb )ρ τ (Γc )β λ ψ aiτ Wγρ ∇c Wαλ +
   1
   4
     iΦβγ ij (Γb )ρ λ ψ a j λ Wαρ + 41 iΦαγ ij (Γb )ρ λ ψ a j λ Wβρ + 14 iΦαβ ij (Γb )ρ λ ψ a j λ Wγρ +
   1                             7                               7
   4
     i(Γb )ρλ ψ aiτ Cαβγρ Wλτ − 16 i(Γb )ρλ ψ aiτ Wαβ Wγρ Wλτ − 16 i(Γb )ρλ ψ aiτ Wαγ Wβρ Wλτ −
   7
   16
      i(Γb )ρλ ψ aiτ Wαρ Wβγ Wλτ + 81 i(Σb c )α ρ ψ aiλ Wρλ ∇c Wβγ + 18 i(Σb c )β ρ ψ aiλ Wρλ ∇c Wαγ +

                                                          203
```

</details>

<a id="src-c24-p303"></a>

<details>
<summary>C24-p303 — PDF page 303: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p303: PDF page 303](https://arxiv.org/pdf/2311.00679v1#page=303) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                                 1
8
  i(Σb c )γ ρ ψ aiλ Wρλ ∇c Wαβ − 32 i(Γb )α ρ (Γc )β τ ψ aiλ Wρλ ∇c Wγτ −
1                                         1
32
   i(Γb )α ρ (Γc )γ τ ψ aiλ Wρλ ∇c Wβτ − 32 i(Γb )β ρ (Γc )γ τ ψ aiλ Wρλ ∇c Wατ −
1                                         1
32
   i(Γb )β ρ (Γc )α τ ψ aiλ Wρλ ∇c Wγτ − 32 i(Γb )γ ρ (Γc )α τ ψ aiλ Wρλ ∇c Wβτ −
1                                        1
32
   i(Γb )γ ρ (Γc )β τ ψ aiλ Wρλ ∇c Wατ + 12 iΦβγ ij (Γb )α ρ ψ a j λ Wρλ +
1                                  1
12
   iΦαγ ij (Γb )β ρ ψ a j λ Wρλ + 12 iΦαβ ij (Γb )γ ρ ψ a j λ Wρλ − 12 (Γb )ρ τ ψ a j τ Wαρ λj Wβγλ i −
1
2
  (Γb )λ τ ψ a j τ Wαβ ρi Wγλρ j − 21 (Γb )λ τ ψ a j τ Wαγ ρi Wβλρ j − 18 (Γb )α λ ψ a j τ Wβγ ρi Wλρτ j +
1
8
  (Γb )ρτ ψ a j λ Wαρλ j Wβγτ i − 81 (Γb )γ λ ψ a j τ Wαβ ρi Wλρτ j + 18 (Γb )ρλ ψ a j τ Wαβρ i Wγλτ j −
1
8
  (Γb )β λ ψ a j τ Wαγ ρi Wλρτ j + 18 (Γb )ρλ ψ a j τ Wαγρ i Wβλτ j − 16
                                                                       1
                                                                         (Γb )α λ ψ a j ρ Xλj Wβγρ i +
1
16
   (Γb )λρ ψ a jα Xλj Wβγρ i − 16
                                1
                                  (Γb )γ λ ψ a j ρ Xλj Wαβρ i + 16
                                                                1
                                                                   (Γb )λρ ψ a jγ Xλj Wαβρ i −
1
16
   (Γb )β λ ψ a j ρ Xλj Wαγρ i + 16
                                  1
                                    (Γb )λρ ψ a jβ Xλj Wαγρ i − 16
                                                                 1
                                                                   (Γb )αλ ψ a j λ X jρWβγρ i −
1                                 1                               1
16
   (Γb )ρ λ ψ a j λ Xαj Wβγρ i − 16 (Γb )γλ ψ a j λ X jρWαβρ i − 16 (Γb )ρ λ ψ a j λ Xγj Wαβρ i −
1
16
                                  1
   (Γb )βλ ψ a j λ X jρ Wαγρ i − 16 (Γb )ρ λ ψ a j λ Xβj Wαγρ i − 16
                                                                   3
                                                                     (Γb )ρ λ ψ a j λ Xρj Wαβγ i +
3                              3
16
   (Γb )ρ λ ψ aiλ XjρWαβγ j + 16 (Γb )ρ λ ψ a j λ Xρi Wαβγ j − 61 iΦρ λ ij (Γb )αρ ψ a j λ Wβγ −
1
6
  iΦρ λ ij (Γb )βρ ψ a j λ Wαγ − 16 iΦρ λ ij (Γb )γρ ψ a j λ Wαβ − 13 iΦα ρij (Γb )ρλ ψ a j λ Wβγ −
1
3
  iΦβ ρij (Γb )ρλ ψ a j λ Wαγ − 13 iΦγ ρij (Γb )ρλ ψ a j λ Wαβ + 32
                                                                 1
                                                                    i(Γb )α ρ (Γc )λ τ ψ aiτ Wβγ ∇c Wρλ +
1                                        1
32
   i(Γb )β ρ (Γc )λ τ ψ aiτ Wαγ ∇c Wρλ + 32 i(Γb )γ ρ (Γc )λ τ ψ aiτ Wαβ ∇c Wρλ +
3                                 3                                 3
16
   i(Σb c )ρ λ ψ aiλ Wβγ ∇c Wαρ + 16 i(Σb c )ρ λ ψ aiλ Wαγ ∇c Wβρ + 16 i(Σb c )ρ λ ψ aiλ Wαβ ∇c Wγρ +
5                                        5
32
   i(Γb )ρ τ (Γc )α λ ψ aiτ Wβγ ∇c Wρλ + 32 i(Γb )ρ τ (Γc )β λ ψ aiτ Wαγ ∇c Wρλ +
5                                         1
32
   i(Γb )ρ τ (Γc )γ λ ψ aiτ Wαβ ∇c Wρλ − 16 i(Σb c )α ρ ψ aiλ Wβγ ∇c Wρλ −
1                                  1                                 3
16
   i(Σb c )β ρ ψ aiλ Wαγ ∇c Wρλ − 16 i(Σb c )γ ρ ψ aiλ Wαβ ∇c Wρλ + 16 i(Σb c )ρλ ψ ai α Wβγ ∇c Wρλ +
3                                  3
16
   i(Σb c )ρλ ψ ai β Wαγ ∇c Wρλ + 16 i(Σb c )ρλ ψ ai γ Wαβ ∇c Wρλ − 18 i(Γb )α ρ ψ aiτ Wβγ Wρ λ Wλτ −
1
8
  i(Γb )β ρ ψ aiτ Wαγ Wρ λ Wλτ − 18 i(Γb )γ ρ ψ aiτ Wαβ Wρ λ Wλτ − 32
                                                                    3
                                                                      i(Γb )ατ ψ aiτ Wβγ W ρλ Wρλ −
3                                 3                                3
32
   i(Γb )βτ ψ aiτ Wαγ W ρλ Wρλ − 32 i(Γb )γτ ψ aiτ Wαβ W ρλ Wρλ + 16 i(Γb )ρτ ψ ai α Wβγ Wρ λ Wτ λ +
                                   3
3
16
   i(Γb )ρτ ψ ai β Wαγ Wρ λ Wτ λ + 16 i(Γb )ρτ ψ ai γ Wαβ Wρ λ Wτ λ + 45 φai α ∇b Wβγ +
5 ai
4
  φ β ∇b Wαγ + 54 φai γ ∇b Wαβ +(Γb )ρ λ φaiλ Cαβγρ + 21 (Γb )ρ λ φaiλ Wαβ Wγρ +

                                                     204
```

</details>

<a id="src-c24-p304"></a>

<details>
<summary>C24-p304 — PDF page 304: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p304: PDF page 304](https://arxiv.org/pdf/2311.00679v1#page=304) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
   1
   2
     (Γb )ρ λ φaiλ Wαγ Wβρ + 12 (Γb )ρ λ φaiλ Wαρ Wβγ + 12 (Σb c )αρ φaiρ ∇c Wβγ +
   1
   2
     (Σb c )βρ φaiρ ∇c Wαγ + 21 (Σb c )γρ φaiρ ∇c Wαβ − 18 (Γb )αλ (Γc )β ρ φaiλ ∇c Wγρ −
   1
   8
     (Γb )αλ (Γc )γ ρ φaiλ ∇c Wβρ − 18 (Γb )βλ (Γc )γ ρ φaiλ ∇c Wαρ − 81 (Γb )βλ (Γc )α ρ φaiλ ∇c Wγρ −
   1
   8
     (Γb )γλ (Γc )α ρ φaiλ ∇c Wβρ − 18 (Γb )γλ (Γc )β ρ φaiλ ∇c Wαρ + 31 Φβγ ij (Γb )αρ φa j ρ +
   1
     Φ ij (Γb )βρ φa j ρ + 31 Φαβ ij (Γb )γρ φa j ρ + 14 (Γb )α ρ φaiλ Wβγ Wρλ +
   3 αγ

   1
   4
     (Γb )β ρ φaiλ Wαγ Wρλ + 14 (Γb )γ ρ φaiλ Wαβ Wρλ − 3Wαβγ i f ab +

   2(Σb c )α ρ Wβγρ i f ac + 2(Σb c )γ ρ Wαβρ i f ac + 2(Σb c )β ρ Wαγρ i f ac

5.1.4      ∇a ∇b Y

D a ∇b Y + 4(Γc )α β ψ a i β ∇b ∇c Xαi − 52 (Σcd )α β ψ a i β Xαi ∇b W cd −

(Σcd )α β ψ a i β W cd ∇b Xαi +4(Σcd )α β ψ a i β W bc ∇d Xαi − 21 ǫb ee1 cd (Γe )α β ψ a i β Wcd ∇e1 Xαi +
                                                        1
2ψ a i α W b c ∇c Xαi +2(Σbc )α β ψ a i β Wcd ∇d Xαi − 16 (Γb )α β ψ a i β W cd Wcd Xαi −

         ψ i Wcd Wee1 Xαi + 21 ǫe2 cdee1 (Σe2 b )α β ψ a i β Wcd Wee1 Xαi −
 5 bcdee1 a α
16
   ǫ
3
2
  (Γd )α β ψ a i β W bc Wdc Xαi + 43 ǫbe2 cde (Σe2 e1 )α β ψ a i β Wcd Wee1 Xαi +
3 e1 e2 cde
8
  ǫ         (Σe1 e2 )α β ψ a i β Wcd We b Xαi − 14 (Γb )α β ψ a i β Y Xαi − 61 ǫbcdee1 Φcdi j (Σee1 )α β ψ a j β Xαi +

Φc b i j (Γc )α β ψ a j β Xαi − 12 (Σb c )α β ψ a i β Xαi ∇d W cd+ 41 ǫb ee1 cd (Γe )α β ψ a i β Xαi ∇e1 Wcd −
3 a α i
4
  ψ i Xα ∇c W bc +(Σdc )α β ψ a i β Xαi ∇d W bc −8i(Σb c )α β φa i β ∇c Xαi −

iǫbee1 cd (Σee1 )α β φa i β Wcd Xαi + i(Γc )α β φa i β Wc b Xαi − 4Y f ab

5.1.5      ∇c ✷Wab

                   3                                            3
D c ∇d ∇d Wâb̂ + 32 (Σde )α β ψ c i β W de Wâ e1 Wb̂e1 α i − 32 (Σde )α β ψ c i β W de Wb̂ e1 Wâe1 α i +
 1
32
   (Γd )α β ψ c i β Xαi ∇d Wâb̂ + 81 Φde i j (Σde )α β ψ c j β Wâb̂α i − 16
                                                                            1
                                                                              Φâb̂i j ψ c j α Xαi +
 1 ee1
32
   ǫ âb̂d Φee1 i j (Γd )α β ψ c j β Xαi + 81 Φâ d i j (Σb̂d )α β ψ c j β Xαi − 18 Φb̂ d i j (Σâd )α β ψ c j β Xαi +

                                                              205
```

</details>

<a id="src-c24-p305"></a>

<details>
<summary>C24-p305 — PDF page 305: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p305: PDF page 305](https://arxiv.org/pdf/2311.00679v1#page=305) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
121 e1 e2   de        α   c β      i e3     127   d α   c β      i e
512
    ǫ     e3 (Σe1 e2 ) β ψ i Wâb̂α ∇ Wde − 256 (Γ ) β ψ i Wâb̂α ∇ Wde −

 3        de c α i           15 e1
   ǫ
64 âb̂e1
            ψ i Xα ∇e1 Wde + 128 ǫ âb̂ de (Σe1 e2 )α β ψ c i β Xαi ∇e2 Wde −
 15 ee1                                        11
128
    ǫ b̂e2 d (Σee1 )α β ψ c i β Xαi ∇e2 Wâd + 32 (Γd )α β ψ c i β Xαi ∇b̂ Wâd −
25                                 15 ee1
64
   (Γb̂ )α β ψ c i β Xαi ∇d Wâd + 128 ǫ âe2 d (Σee1 )α β ψ c i β Xαi ∇e2 Wb̂d −
11                                 25                                 61
32
   (Γd )α β ψ c i β Xαi ∇â Wb̂d + 64 (Γâ )α β ψ c i β Xαi ∇d Wb̂d + 512 ǫâb̂e3 de (Σe1 e2 )α β ψ c i β Wdeα i ∇e3 W e1 e2 −
 3                                      61
   ǫ e1 de ψ c i α Wdeα i ∇e2 We1 e2 − 256
512 âb̂
                                           (Γb̂ )α β ψ c i β Wdeα i ∇d Wâ e +
 61                                      61                                    61
256
    (Γâ )α β ψ c i β Wdeα i ∇d Wb̂ e − 256 (Γd )α β ψ c i β Wdeα i ∇e Wâb̂ + 512 (Γb̂ )α β ψ c i β Wdeα i ∇â W de −
 61                                      61                                      61
256
    (Γd )α β ψ c i β Wdeα i ∇â Wb̂ e − 512 (Γâ )α β ψ c i β Wdeα i ∇b̂ W de + 256 (Γd )α β ψ c i β Wdeα i ∇b̂ Wâ e −
 67        de                                           67 e3
    ǫ
256 âb̂e2
              (Σe3 e1 )α β ψ c i β Wdeα i ∇e3 W e1 e2 + 256 ǫ âb̂ de (Σe3 e1 )α β ψ c i β Wdeα i ∇e2 W e1 e2 +
 3                                    61
   ǫ ee1 d ψ c i α Wâdα i ∇e2 Wee1 + 256
512 b̂e2
                                          (Γe )α β ψ c i β Wâdα i ∇e Wb̂ d −
 61                                      61                                     3 e2
256
    (Γb̂ )α β ψ c i β Wâdα i ∇e W ed − 256 (Γd )α β ψ c i β Wâdα i ∇e Wb̂e − 128 ǫ b̂e3 e1 d (Σe2 e )α β ψ c i β Wâdα i ∇e3 W ee1 +
 3 e2 e3 ee1 d                                          67
512
    ǫ          (Σe2 e3 )α β ψ c i β Wâdα i ∇b̂ Wee1 + 256 (Γe )α β ψ c i β Wâdα i ∇b̂ W ed −
 3 e2 e3 ee1                                        67
512
    ǫ   b̂   (Σe2 e3 )α β ψ c i β Wâdα i ∇d Wee1 + 256 (Γe )α β ψ c i β Wâdα i ∇d Wb̂e −
 3                                     61
   ǫ ee1 d ψ c i α Wb̂dα i ∇e2 Wee1 − 256
512 âe2
                                          (Γe )α β ψ c i β Wb̂dα i ∇e Wâ d +
 61                                     61                                      3 e2
256
    (Γâ )α β ψ c i β Wb̂dα i ∇e W ed + 256 (Γd )α β ψ c i β Wb̂dα i ∇e Wâe + 128 ǫ âe3 e1 d (Σe2 e )α β ψ c i β Wb̂dα i ∇e3 W ee1 −
 3 e2 e3 ee1 d                                          67
512
    ǫ          (Σe2 e3 )α β ψ c i β Wb̂dα i ∇â Wee1 − 256 (Γe )α β ψ c i β Wb̂dα i ∇â W ed+
 3 e2 e3 ee1                                         67
512
    ǫ   â   (Σe2 e3 )α β ψ c i β Wb̂dα i ∇d Wee1 − 256 (Γe )α β ψ c i β Wb̂dα i ∇d Wâe +
 9                              1 c α                       1
128
    ψ c i α W de Wde Wâb̂α i + 32 ψ i W de Wâb̂ Wdeα i + 256 ǫe3 dee1 e2 (Γe3 )α β ψ c i β Wde We1 e2 Wâb̂α i +
 1                                           1 c α                        1
16
   (Σe1 d )α β ψ c i β W de We1 e Wâb̂α i + 16 ψ i Wâ d Wb̂ e Wdeα i − 64 ǫb̂e3 ee1 e2 (Γe3 )α β ψ c i β Wâ d Wee1 We2 dα i +
 1                                            1
16
   (Σb̂d )α β ψ c i β W de Wâ e1 We1 eα i + 64 ǫâe3 ee1 e2 (Γe3 )α β ψ c i β Wb̂ d Wee1 We2 dα i −
 1                                            1
16
   (Σâd )α β ψ c i β W de Wb̂ e1 We1 eα i + 32 (Σb̂ e1 )α β ψ c i β W de Wâe1 Wdeα i −
 1                                           1
32
   (Σâ e1 )α β ψ c i β W de Wb̂e1 Wdeα i − 16 (Σb̂ e1 )α β ψ c i β W de Wâd We1 eα i +
 1                                           1
16
   (Σâ e1 )α β ψ c i β W de Wb̂d We1 eα i + 16 (Σâb̂ )α β ψ c i β W de W e1 d We1 eα i −
 1                                                     1
   ǫ de2 e3 (Γe1 )α β ψ c i β Wd e We1 e We2 e3 α i − 16
128 âb̂
                                                         (Σe1 d )α β ψ c i β W de Wb̂e Wâe1 α i +
 1                                                    1 c α
   ǫ dee1 e3 (Γe2 )α β ψ c i β Wde We1 e2 Wâe3 α i + 32
128 b̂
                                                         ψ i W de Wb̂d Wâeα i +

                                                           206
```

</details>

<a id="src-c24-p306"></a>

<details>
<summary>C24-p306 — PDF page 306: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p306: PDF page 306](https://arxiv.org/pdf/2311.00679v1#page=306) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 1                                           1
16
   (Σe1 d )α β ψ c i β W de Wb̂e1 Wâeα i + 128 ǫb̂e3 dee1 (Γe3 )α β ψ c i β Wde We1 e2 Wâe2 α i +
 1                                            1
16
   (Σe1 d )α β ψ c i β W de Wâe Wb̂e1 α i − 128 ǫâ dee1 e3 (Γe2 )α β ψ c i β Wde We1 e2 Wb̂e3 α i −
 1 c α                      1                                           1
32
   ψ i W de Wâd Wb̂eα i − 16 (Σe1 d )α β ψ c i β W de Wâe1 Wb̂eα i − 128 ǫâe3 dee1 (Γe3 )α β ψ c i β Wde We1 e2 Wb̂e2 α i −
 1                                                   1
   ǫ dee3 (Γe1 )α β ψ c i β Wde We1 e2 We3 e2 α i + 128
128 âb̂
                                                        ǫâb̂ dee1 (Γe3 )α β ψ c i β Wde We1 e2 We3 e2 α i −
 1                                                     1
   ǫ dee2 e3 (Γe1 )α β ψ c i β Wâd Wee1 We2 e3 α i + 128
128 b̂
                                                          ǫâ dee2 e3 (Γe1 )α β ψ c i β Wb̂d Wee1 We2 e3 α i −
1 c α
2
  ψ i ∇d ∇d Wâb̂α i − 12 (Σâb̂ )α β ψ c i β ∇d ∇d Xαi + 64
                                                          17 e1 e2
                                                             ǫ       de        α   c β     e3     i
                                                                   e3 (Σe1 e2 ) β ψ i Wde ∇ Wâb̂α −

19
32
   (Γd )α β ψ c i β Wde ∇e Wâb̂α i − 18 (Γd )α β ψ c i β Wâb̂ ∇d Xαi − 16
                                                                          1
                                                                            ǫâb̂e1 de ψ c i α Wde ∇e1 Xαi +
 3 e1                                            3 ee1
16
   ǫ âb̂ de (Σe1 e2 )α β ψ c i β Wde ∇e2 Xαi − 16 ǫ b̂e2 d (Σee1 )α β ψ c i β Wâd ∇e2 Xαi +
1
8
  (Γd )α β ψ c i β Wâd ∇b̂ Xαi − 41 (Γb̂ )α β ψ c i β Wâd ∇d Xαi + 16
                                                                     3 ee1
                                                                        ǫ âe2 d (Σee1 )α β ψ c i β Wb̂d ∇e2 Xαi −
1
8
  (Γd )α β ψ c i β Wb̂d ∇â Xαi + 41 (Γâ )α β ψ c i β Wb̂d ∇d Xαi + 64
                                                                      3 e1
                                                                        ǫ âb̂e2 e (Σe1 d )α β ψ c i β Xαi ∇e2 W de −
 3 e1 e2 de         α   c β i            3 e1 e2 de         α   c β i
256
    ǫ   b̂ (Σe1 e2 ) β ψ i Xα ∇â Wde + 256 ǫ   â (Σe1 e2 ) β ψ i Xα ∇b̂ Wde −

 1        e1 e2                                          1
   ǫ
64 âb̂e3
                (Σde )α β ψ c i β W de ∇e3 We1 e2 α i − 64 ǫâb̂ de1 e2 ψ c i α Wde ∇e We1 e2 α i +
 5                                      5                                     5
64
   (Γb̂ )α β ψ c i β W de ∇â Wdeα i − 32 (Γe )α β ψ c i β Wb̂ d ∇â Wedα i + 32 (Γb̂ )α β ψ c i β Wâ d ∇e Wdeα i −
 5                                     5                                      5
32
   (Γd )α β ψ c i β Wâb̂ ∇e Wdeα i − 32 (Γâ )α β ψ c i β Wb̂ d ∇e Wdeα i + 32 (Γe )α β ψ c i β Wâ d ∇b̂ Wedα i −
 5                                      1
64
   (Γâ )α β ψ c i β W de ∇b̂ Wdeα i − 32 ǫâb̂ de1 e2 (Σe e3 )α β ψ c i β Wde ∇e3 We1 e2 α i +
 1 e3                                                    1
32
   ǫ âb̂ e1 e2 (Σe3 d )α β ψ c i β Wde ∇e We1 e2 α i + 64 ǫb̂e2 dee1 ψ c i α Wde ∇e2 Wâe1 α i +
 5                                      1                                       5
32
   (Γe )α β ψ c i β Wb̂ d ∇e Wâdα i − 32 (Γb̂ )α β ψ c i β W d e ∇e Wâdα i − 32 (Γe )α β ψ c i β Wb̂d ∇d Wâeα i +
 1 e2                                                  1 e2 e3 dee1
16
   ǫ b̂e3 de1 (Σe2 e )α β ψ c i β Wde ∇e3 Wâe1 α i + 64 ǫ          (Σe2 e3 )α β ψ c i β Wde ∇b̂ Wâe1 α i +
 1                                      1 e2 e3 de
32
   (Γd )α β ψ c i β Wd e ∇b̂ Wâeα i − 64 ǫ                α   c β     e1      i
                                               b̂ (Σe2 e3 ) β ψ i Wde ∇ Wâe1 α +

 7                                     1                                         5
32
   (Γd )α β ψ c i β Wb̂d ∇e Wâeα i − 64 ǫâe2 dee1 ψ c i α Wde ∇e2 Wb̂e1 α i − 32 (Γe )α β ψ c i β Wâ d ∇e Wb̂dα i +
 1                                       5                                     1 e2
32
   (Γâ )α β ψ c i β W d e ∇e Wb̂dα i + 32 (Γe )α β ψ c i β Wâd ∇d Wb̂eα i − 16 ǫ âe3 de1 (Σe2 e )α β ψ c i β Wde ∇e3 Wb̂e1 α i −
 1 e2 e3 dee1                                           1
64
   ǫ          (Σe2 e3 )α β ψ c i β Wde ∇â Wb̂e1 α i − 32 (Γd )α β ψ c i β Wd e ∇â Wb̂eα i +
 1 e2 e3 de         α   c β     e1      i   7   d α   c β      e     i
64
   ǫ    â (Σe2 e3 ) β ψ i Wde ∇ Wb̂e1 α − 32 (Γ ) β ψ i Wâd ∇ Wb̂eα −

1 e1                                            1 e1 e2 de
8
  ǫ âb̂e2 d (Σe1 e )α β ψ c i β Wde ∇e2 Xαi − 32 ǫ                α   c β         i
                                                       b̂ (Σe1 e2 ) β ψ i Wde ∇â Xα +

 1 e1 e2 de         α   c β         i   3 e1 e2   de        α   c β       e3   i
32
   ǫ    â (Σe1 e2 ) β ψ i Wde ∇b̂ Xα + 32 ǫ    e3 (Σe1 e2 ) β ψ i Wâb̂ ∇ Wdeα +

                                                            207
```

</details>

<a id="src-c24-p307"></a>

<details>
<summary>C24-p307 — PDF page 307: Supplement5.1: full degauged higher Weyl derivatives</summary>

[C24-p307: PDF page 307](https://arxiv.org/pdf/2311.00679v1#page=307) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3 e1 e2                α   c β de e3   i   3      α   c β de        i
16
   ǫ     b̂de3 (Σe1 e2 ) β ψ i W ∇ Wâeα + 16 (Γd ) β ψ i W ∇b̂ Wâeα −

 3                                      3 e1 e2
16
   (Γb̂ )α β ψ c i β Wd e ∇d Wâeα i − 16 ǫ                    α   c β de e3   i
                                                âde3 (Σe1 e2 ) β ψ i W ∇ Wb̂eα −

 3                                      3                                     3 e1 e2
16
   (Γd )α β ψ c i β W de ∇â Wb̂eα i + 16 (Γâ )α β ψ c i β Wd e ∇d Wb̂eα i + 32 ǫ                    α   c β de e3  i
                                                                                      âb̂e3 (Σe1 e2 ) β ψ i W ∇ Wdeα −

 3                                      3
   ǫ dee1 ψ c i α Wde ∇e2 We1 e2 α i + 16
32 âb̂
                                          ǫâb̂ dee1 (Σe2 e3 )α β ψ c i β Wde ∇e3 We1 e2 α i +
 3                                     3 e2 dee1
   ǫ dee1 ψ c i α Wâd ∇e2 Wee1 α i + 16
32 b̂e2
                                         ǫ b̂    (Σe2 e3 )α β ψ c i β Wâd ∇e3 Wee1 α i +
 3 e1 e2   de        α   c β      e3    i   3 e1 e2     e         α   c β   d e3   i
16
   ǫ     e3 (Σe1 e2 ) β ψ i Wâd ∇ Wb̂eα − 16 ǫ     b̂e3 (Σe1 e2 ) β ψ i Wâ ∇ Wedα −

 3                                     3 e2 dee1
   ǫ dee1 ψ c i α Wb̂d ∇e2 Wee1 α i − 16
32 âe2
                                         ǫ â    (Σe2 e3 )α β ψ c i β Wb̂d ∇e3 Wee1 α i −
 3 e1 e2   de        α   c β      e3    i   3 e1 e2     e         α   c β   d e3   i
16
   ǫ     e3 (Σe1 e2 ) β ψ i Wb̂d ∇ Wâeα + 16 ǫ     âe3 (Σe1 e2 ) β ψ i Wb̂ ∇ Wedα −

1 e2 ee1 d
4
  ǫ b̂     (Σe2 e3 )α β ψ c i β Wâdα i ∇e3 Wee1 − 41 ǫe1 e2 e3 ed (Σe1 e2 )α β ψ c i β Wâdα i ∇e3 Wb̂e −
1 e1 e2                                  ed 1 e2 ee1 d
4
  ǫ                     α   c β     i e3
        b̂e3 e (Σe1 e2 ) β ψ i Wâdα ∇ W + 4 ǫ â      (Σe2 e3 )α β ψ c i β Wb̂dα i ∇e3 Wee1 +
1 e1 e2   ed        α   c β     i e3      1 e1 e2                 α   c β     i e3 ed
4
  ǫ     e3 (Σe1 e2 ) β ψ i Wb̂dα ∇ Wâe + 4 ǫ     âe3 e (Σe1 e2 ) β ψ i Wb̂dα ∇ W −

1
  ǫ e1 e2 d ψ c i α Wdeα i ∇e We1 e2 − 18 ǫb̂e2 e1 de ψ c i α Wdeα i ∇e2 Wâe1 +
8 âb̂

1                                     9
  ǫ e1 de ψ c i α Wdeα i ∇e2 Wb̂e1 + 128
8 âe2
                                         (Σâb̂ )α β ψ c i β W de Wde Xαi − 98 i(Σde )α β φc i β W de Wâb̂α i +
 9                      9
16
   iφc i α Wâb̂ Xαi − 32 iǫâb̂e1 de (Γe1 )α β φc i β Wde Xαi − 98 i(Σb̂ d )α β φc i β Wâd Xαi +
9
8
  i(Σâ d )α β φc i β Wb̂d Xαi + 11
                                  4
                                    iφc i α Wâ d Wb̂dα i − 11
                                                             4
                                                               iφc i α Wb̂ d Wâdα i −
1
4
  i(Γd )α β φc i β ∇d Wâb̂α i − 18 iǫâb̂e1 de φc i α ∇e1 Wdeα i + 14 iǫe1 âb̂ de (Σe1 e2 )α β φc i β ∇e2 Wdeα i −
1 ee1
4
  iǫ b̂e2 d (Σee1 )α β φc i β ∇e2 Wâdα i + 41 i(Γd )α β φc i β ∇b̂ Wâdα i − 14 i(Γb̂ )α β φc i β ∇d Wâdα i +
1 ee1
4
  iǫ âe2 d (Σee1 )α β φc i β ∇e2 Wb̂dα i − 14 i(Γd )α β φc i β ∇â Wb̂dα i + 14 i(Γâ )α β φc i β ∇d Wb̂dα i −
1 de
2
  iǫ âb̂e1 (Σde )α β φc i β ∇e1 Xαi − 21 i(Γb̂ )α β φc i β ∇â Xαi + 12 i(Γâ )α β φc i β ∇b̂ Xαi +

2∇d Wâb̂ f c d −4∇â Wb̂ d f c d +4∇b̂ Wâ d f c d −4∇d Wâd f c b̂ +4∇d Wb̂d f c â

                                                            208
```

</details>

<a id="src-c24-p308"></a>

<details>
<summary>C24-p308 — PDF page 308: Supplement5.1: full degauged higher Weyl derivatives; Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p308: PDF page 308](https://arxiv.org/pdf/2311.00679v1#page=308) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.2      Vector Multiplet

5.2.1     ∇a ∇b W

D a ∇b W − 12 iψ a i α ∇b λiα + 16
                                 1 bee1 cd
                                   iǫ      (Σee1 )α β ψ a i β Wcd λiα + 14 i(Γc )α β ψ a i β W bc λiα −
1
8
  (Γb )α β ψ a i β W Xαi + 12 (Γb )α β φa i β λiα − 2W f ab

5.2.2     ∇a ∇b λiα

   D a ∇b λiα − 21 (Σcd )αβ ψ aiβ ∇b F cd − 83 (Σcd )αβ ψ aiβ W cd∇b W −
   3
   8
     (Σcd )αβ ψ aiβ W ∇b W cd − 21 ψ a jα ∇b X ij + 12 (Γc )αβ ψ aiβ D b ∇c W −
   1
   4
                                     1
     i(Γc )αβ ψ aiβ ψ b j ρ ∇c λjρ + 16 i(Σcd )β ρ ψ ai α ψ b j ρ W cd λjβ − 16
                                                                              3
                                                                                i(Σcd )β ρ ψ aiρ ψ b jαW cd λjβ −
   3
   16
      i(Σcd )α β ψ ai ρ ψ b j ρ W cd λjβ − 16
                                            1                                   1
                                              i(Σcd )βρ ψ aiβ ψ b j ρ W cdλjα + 16 i(Σcd )αβ ψ aiρ ψ b j β W cd λjρ −

      ψ α ψ b j β W Xβj + 81 ψ aiβ ψ b jα W Xβj + 81 ψ ai β ψ b j β W Xαj +
   1 ai
   16

     ψ α φb j β λjβ − 12 ψ aiβ φb jαλjβ − 21 ψ ai β φb j β λjα −(Γc )αβ ψ aiβ W f b c −
   1 ai
   4

   1                            1 bee1 cd ai             3 e2 ee1 cd
   16
      (Γb )αβ ψ aiβ W cd Fcd − 32 ǫ      ψ α Wee1 Fcd + 32 ǫ         (Σe2 b )αβ ψ aiβ Wee1 Fcd −
   3 be1 e2 ec
   16
      ǫ        (Σe1 e2 )αβ ψ aiβ We d Fcd − 41 (Γc )αβ ψ aiβ W bd Fcd + 18 (Γd )αβ ψ aiβ Wdc F bc −
   7                             1 bcdee1 ai             1 e2 cdee1
   64
      (Γb )αβ ψ aiβ W W cd Wcd + 64 ǫ    ψ α W WcdWee1 + 16 ǫ       (Σe2 b )αβ ψ aiβ W Wcd Wee1 +
   1 bee1 cd
   16
      ǫ      (Σee1 )αβ ψ a j β X ij Wcd − 14 (Γc )αβ ψ a j β X ij Wc b + 21 (Σcd )αβ ψ aiβ W bc ∇d W −
   1 b
   16
      ǫ ee1 cd (Γe )αβ ψ aiβ Wcd ∇e1 W + 14 ψ ai α W b c ∇c W + 41 (Σbc )αβ ψ aiβ Wcd ∇d W +
   1 be2 ecd                               1 e1 e2 dec
   16
      ǫ      (Σe2 e1 )αβ ψ aiβ Wee1 Fcd + 32 ǫ         (Σe1 e2 )αβ ψ aiβ Wde Fc b +
   1                             1 be2 cde
   8
     (Γd )αβ ψ aiβ W W bc Wdc − 16 ǫ       (Σe2 e1 )αβ ψ aiβ W Wcd Wee1 −
   1 e1 e2 cde
   32
      ǫ        (Σe1 e2 )αβ ψ aiβ W Wcd We b − 81 ǫbee1 cd (Σee1 )αρ ψ a j ρ λiβ Wcdβ j +
   1
   4
                                     1 bee1 cd
     (Γc )αρ ψ a j ρ λiβ Wc b β j − 16 ǫ                                        1
                                               (Σee1 )α ρ ψ a j β λiρ Wcdβ j + 16 (Γb )α β ψ a j ρ λiρ Xβj +
   1
   16
      (Γb )ρβ ψ a jα λiρ Xβj − 16
                                1
                                  (Γb )αρ ψ a j ρ λiβ Xβj + 16
                                                            1
                                                               (Γb )β ρ ψ a j ρ λiβ Xαj +
   3
   16
      (Γb )β ρ ψ a j ρ λiα Xβj + 16
                                 3
                                    (Γb )β ρ ψ aiρ λjαXβj − 16
                                                             3
                                                               (Γb )β ρ ψ a j ρ λjα Xβi +

                                                           209
```

</details>

<a id="src-c24-p309"></a>

<details>
<summary>C24-p309 — PDF page 309: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p309: PDF page 309](https://arxiv.org/pdf/2311.00679v1#page=309) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
  1 bcdee1
  24
     ǫ     Φcd ij (Σee1 )αβ ψ a j β W − 41 Φc bij (Γc )αβ ψ a j β W − 14 (Σdc )αβ ψ aiβ W ∇d W bc −
  1 b                                    3 ai
  16
     ǫ ee1 cd (Γe )αβ ψ aiβ W ∇e1 Wcd + 16 ψ α W ∇c W bc + 81 (Σb c )αβ ψ aiβ W ∇d W cd −
  3 ai
  2
    iφ α ∇b W − 41 iǫbee1 cd (Σee1 )αβ φaiβ Fcd + 21 i(Γc )αβ φaiβ Fc b −
  1 bee1 cd
  4
    iǫ      (Σee1 )αβ φaiβ W Wcd + 43 i(Γc )αβ φaiβ W Wc b − 21 i(Γb )αβ φa j β X ij −

  i(Σb c )αβ φaiβ ∇c W − 3λiα f ab + 2(Σb c )α β λiβ f ac

5.2.3    ∇a ∇b X ij

  D a ∇b Xij −i(Γc )α β ψ aiβ D b ∇c λjα + 41 iǫee1 e2 cd (Σee1 )αβ ψ aiα ψ bjβ ∇e2 Fcd +
  1                                1 ee1
  2
    i(Γc )αβ ψ aiα ψ bjβ ∇d Fcd + 16 iǫ e2 cd (Σee1 )αβ ψ aiα ψ bjβ Wcd ∇e2 W +
  7                                 3 ee1
  8
    i(Γc )αβ ψ aiα ψ bjβ Wcd ∇d W + 16 iǫ e2 cd (Σee1 )αβ ψ aiα ψ bjβ W ∇e2 Wcd +
  9
  16
     i(Γc )αβ ψ aiα ψ bjβ W ∇d Wcd + 12 i(Γc )αβ ψ aiα ψ b k β ∇c Xj k − 12 iψ ai α ψ bjα ∇c ∇c W −
                                   7                           5
  i(Σcd )αβ ψ aiα ψ bjβ ∇c ∇d W + 16 iψ ai α ψ bjα W cd Fcd − 32 iǫe2 ee1 cd (Γe2 )αβ ψ aiα ψ bjβ Wee1 Fcd +
  1
  4
    i(Σc e )αβ ψ aiα ψ bjβ W ed Fcd + 27
                                      64
                                                                    9
                                         iψ ai α ψ bjα W W cdWcd − 64 iǫe2 cdee1 (Γe2 )αβ ψ aiα ψ bjβ W WcdWee1 −
  1
  8
    i(Σcd )αβ ψ aiα ψ b k β Xj k W cd − 81 i(Σcd )β ρ ψ aiρ ψ b k α λjβ Wcdα k −
  1                           1
  8
    iψ aiα ψ b k β λjβ Xαk + 16 iψ aiβ ψ b k α λjβ Xαk + 18 iψ ai β ψ b k β λαj Xαk −
  3                         3
  16
     iψ aiβ ψ bjα λkβ Xαk + 16 iψ aiβ ψ b k α λkβ Xjα − 38 iψ ai β ψ bjβ λαk Xαk +
  3
  8
    iψ aiα ψ bjβ λkβ Xαk + 83 iψ ai β ψ b k β λkαXjα − 38 iψ aiα ψ b k β λkβ Xjα −
  1
  4
    iΦcd j k (Σcd )αβ ψ aiα ψ b k β W + 21 (Γc )αβ ψ aiα φbjβ ∇c W + 12 (Σcd )αβ ψ aiα φbjβ F cd −
  5 ai
  2
    ψ α φb k α Xj k −i(Γc )α β ψ aiβ λjα f b c + 38 i(Σcd )α β ψ aiβ λjα ∇b W cd −
  3 aiα
  4
    ψ Xjα ∇b W − 34 ψ aiα W ∇b Xjα − i(Σcd )α β ψ aiβ W bc ∇d λjα +
  1 b
  8
    iǫ ee1 cd (Γe )α β ψ aiβ Wcd ∇e1 λjα − 12 iψ aiα W b c ∇c λjα − 12 i(Σbc )α β ψ aiβ Wcd ∇d λjα −
  1                                 1 bcdee1 aiα              5 e2 cdee1
  64
     i(Γb )α β ψ aiβ W cdWcd λjα + 16 iǫ    ψ Wcd Wee1 λjα − 64 iǫ       (Σe2 b )α β ψ aiβ Wcd Wee1 λjα +
  3 bee1 cd
  32
     ǫ      (Σee1 )α β ψ aiβ W WcdXjα − 38 (Γc )α β ψ aiβ W Wc b Xjα + 16
                                                                       5
                                                                          i(Γd )α β ψ aiβ W bc Wdc λjα −
  5 be2 cde                                    5 e1 e2 cde
  32
     iǫ     (Σe2 e1 )α β ψ aiβ Wcd Wee1 λjα − 64 iǫ        (Σe1 e2 )α β ψ aiβ Wcd We b λjα −

                                                          210
```

</details>

<a id="src-c24-p310"></a>

<details>
<summary>C24-p310 — PDF page 310: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p310: PDF page 310](https://arxiv.org/pdf/2311.00679v1#page=310) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
  1
  4
    (Γb )α β ψ a k β Xij Xαk − 38 (Γb )α β ψ aiβ Xjk Xαk + 38 (Γb )α β ψ a k β Xi k Xjα +
  1 bcdee1
  24
     iǫ    Φcdi k (Σee1 )α β ψ a k β λjα − 14 iΦc b i k (Γc )α β ψ a k β λjα +
  1                                  1 b
  8
    i(Σb c )α β ψ aiβ λjα ∇d W cd − 16 iǫ ee1 cd (Γe )α β ψ aiβ λjα ∇e1 Wcd +
  3
  16
     iψ aiα λjα ∇c W bc − 14 i(Σdc )α β ψ aiβ λjα ∇d W bc −2(Σb c )α β φaiβ ∇c λjα −
  1 bee1 cd
  8
    ǫ       (Σee1 )α β φaiβ Wcd λjα − 43 i(Γb )α β φaiβ W Xjα − 4Xij f ab

5.2.4     ∇c ∇d Fab

  D c ∇d Fâb̂ −i(Γâ )α β ψ c i β ∇d ∇b̂ λiα + 38 iψ c i α λiα ∇d Wâb̂ + 21 iψ c i α Wâb̂ ∇d λiα +
  9         ee1                                 5
    iǫ
  64 âb̂e2
                (Γe2 )α β ψ c i β λiα ∇d Wee1 + 32 iǫâb̂e2 ee1 (Γe2 )α β ψ c i β Wee1 ∇d λiα +
  1
  2
    i(Σâ e )α β ψ c i β Wb̂e ∇d λiα + 21 ψ c i α Wâb̂α i ∇d W + 12 ψ c i α W ∇d Wâb̂α i −
  3 d                                             3
  32
     iǫ âb̂e2 e (Γe1 )α β ψ c i β Wee1 ∇e2 λiα + 32 iǫâb̂e1 e2 e (Γe1 )α β ψ c i β We d ∇e2 λiα −
  1
  4
    i(Σee1 )α β δ d â ψ c i β W ee1 ∇b̂ λiα − 21 i(Σde )α β ψ c i β Wb̂e ∇â λiα − 16
                                                                                     1 d
                                                                                       iǫ âe2 ee1 (Γe2 )α β ψ c i β Wee1 ∇b̂ λiα −
  1                                                             1
  2
    iψ c i α Wb̂ d ∇â λiα +i(Σâe )α β ψ c i β W de ∇b̂ λiα − 256 iǫde2 e3 ee1 (Σe2 e3 )α β ψ c i β Wâb̂ Wee1 λiα +
  1                                      1
  16
     i(Γe )α β ψ c i β Wâb̂ We d λiα + 128 iǫe3 e4 ee1 e2 (Σe3 e4 )α β δ d â ψ c i β Wb̂e We1 e2 λiα −
  3
  16
     i(Γe1 )α β δ d â ψ c i β Wb̂ e We1 e λiα − 15
                                                 64
                                                    iǫe2 e3 âe e1 (Σe2 e3 )α β ψ c i β W de Wb̂e1 λiα −
  1
  4
    i(Γâ )α β ψ c i β W de Wb̂e λiα − 15
                                       64
                                          iǫde2 e3 âe (Σe2 e3 )α β ψ c i β W ee1 Wb̂e1 λiα +
  15 e3 e4                                              1
  64
     iǫ       e2        α d      c β
           b̂e (Σe3 e4 ) β δ â ψ i W
                                      ee1
                                          We2 e1 λiα − 32 i(Γb̂ )α β δ d â ψ c i β W ee1 Wee1 λiα −
  15 e2 e3                α   c β  ee1               3
  128
      iǫ   âb̂e (Σe2 e3 ) β ψ i W     W d e1 λiα + 256 iǫde2 e3 âb̂ (Σe2 e3 )α β ψ c i β W ee1 Wee1 λiα −
  23                                     41 e3
     iǫ ee1 e2 ψ c i α Wee1 We2 d λiα − 128
  256 âb̂
                                            iǫ âb̂ e1 e2 (Σe3 e )α β ψ c i β W de We1 e2 λiα −
   7
  128
      iǫd â ee1 e2 ψ c i α Wb̂e We1 e2 λiα + 38 iǫe3 â ee1 e2 (Σe3 d )α β ψ c i β Wb̂e We1 e2 λiα −
  3 de2 e3 ee1                                        1
  32
     iǫ        (Σe2 e3 )α β ψ c i β Wâe Wb̂e1 λiα + 16 i(Γe )α β ψ c i β Wâe Wb̂ d λiα +
  3 de2 e3 e1                   e       i    1 d       ee1
  32
     iǫ               α   c β
          â (Σe2 e3 ) β ψ i Wb̂ We1 e λα − 32 iǫ âb̂     (Γe2 )α β ψ c i β Wee1 ∇e2 λiα −
  3 d                                               7
  16
     iǫ âe1 e2 e (Γe1 )α β ψ c i β Wb̂e ∇e2 λiα − 256 iǫd âb̂ e2 e3 (Σee1 )α β ψ c i β W ee1 We2 e3 λiα +
  13                                                 1 de2 e3 ee1
     iǫ ee1 e2 (Σde3 )α β ψ c i β Wee1 We2 e3 λiα − 16
  64 âb̂
                                                       ǫ          (Σe2 e3 )α β ψ c i β W Wee1 Wâb̂α i +

                                                             211
```

</details>

<a id="src-c24-p311"></a>

<details>
<summary>C24-p311 — PDF page 311: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p311: PDF page 311](https://arxiv.org/pdf/2311.00679v1#page=311) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
1                                    17 de3 ee1
4
  (Γe )α β ψ c i β W We d Wâb̂α i + 32 iǫ â (Σe3 e2 )α β ψ c i β Wb̂e We1 e2 λiα +
9 e2 e3 ee1                                       1 d
64
   iǫ  â   (Σe2 e3 )α β ψ c i β Wb̂ d Wee1 λiα + 32 iǫ âb̂e2 e (Γe2 )α β ψ c i β Wee1 ∇e1 λiα −
7 d                                                   7 de3
64
   iǫ âb̂ ee2 (Σe1 e3 )α β ψ c i β Wee1 We2 e3 λiα + 64 iǫ âb̂ e2 (Σe3 e )α β ψ c i β W ee1 We2 e1 λiα +
 1                                                3 e4 ee1 e2
   iǫ ee1 e2 e3 δ d â ψ c i α Wee1 We2 e3 λiα + 64
256 b̂
                                                    iǫ b̂     (Σe4 e3 )α β δ d â ψ c i β Wee1 We2 e3 λiα +
1 de2 e3 ee1
16
   ǫ         (Σe2 e3 )α β ψ c i β Fee1 Wâb̂α i − 81 (Γe )α β ψ c i β Fe d Wâb̂α i +
1 d                                                    1
16
   ǫ âb̂ e2 e3 (Σee1 )α β ψ c i β F ee1 We2 e3 α i + 16 ǫâb̂ ee1 e2 ψ c i α Fe d We1 e2 α i +
1
4
  (Γâ )α β ψ c i β Fb̂ e W d eα i − 18 (Γe )α β ψ c i β Fâb̂ We d α i + 81 (Γb̂ )α β δ d â ψ c i β F ee1 Wee1 α i −
1
4
  (Γe1 )α β δ d â ψ c i β Fb̂ e We1 eα i + 18 ǫâb̂ ee2 e3 (Σde1 )α β ψ c i β Fee1 We2 e3 α i −

  ǫ âb̂ e1 e2 (Σe3 e )α β ψ c i β F de We1 e2 α i − 41 (Γd )α β ψ c i β Fâ e Wb̂eα i −
1 e3
8

1 d ee1 e2 c α
8
  ǫ â    ψ i Fee1 Wb̂e2 α i + 41 ǫe3 â ee1 e2 (Σe3 d )α β ψ c i β Fee1 Wb̂e2 α i +
1 de2 e3 ee1
4
  ǫ          (Σe2 e3 )α β ψ c i β Fâe Wb̂e1 α i + 41 (Γe )α β ψ c i β Fâ d Wb̂eα i −
1
4
  (Γe )α β ψ c i β Fâe Wb̂ d α i − 14 ǫde2 e3 â e (Σe2 e3 )α β ψ c i β Fe e1 Wb̂e1 α i −
1
4
  (Γe )α β δ d â ψ c i β Fe e1 Wb̂e1 α i + 14 (Γâ )α β ψ c i β F de Wb̂eα i + 81 ǫd âb̂ ee2 ψ c i α Fe e1 We2 e1 α i −
1                                              1
  ǫ ee1 e2 e3 δ d â ψ c i α Fee1 We2 e3 α i + 16
16 b̂
                                                  ǫâb̂ ee1 e2 ψ c i α Fee1 We2 d α i −

          ψ i Fb̂e We1 e2 α i + 41 (Γâ )α β ψ c i β Fb̂ d Xαi − 14 (Γd )α β ψ c i β Fâb̂ Xαi −
1 d ee1 e2 c α
8
  ǫ â
1                                     1 dee1                      1
4
  (Γe )α β δ d â ψ c i β Fb̂e Xαi − 24 iǫ              j c α i         d j      α   c β i
                                             âb̂ Φee1 i ψ j λα − 2 iΦâ i (Γb̂ ) β ψ j λα −

1
12
   iΦâb̂i j (Γd )α β ψ c j β λiα − 61 iǫdee2 âb̂ Φe e1 i j (Σe2 e1 )α β ψ c j β λiα −
1 ee1 e2 e3          j         α d      c β i   1       j  e α d      c β i
12
   iǫ       b̂ Φee1 i (Σe2 e3 ) β δ â ψ j λα + 6 iΦâei (Γ ) β δ b̂ ψ j λα +

1 ee1 e2            j    d α   c β i   1 dee1 e2         j         α   c β i
6
  iǫ     âb̂ Φee1 i (Σe2 ) β ψ j λα − 3 iǫ      b̂ Φâei (Σe1 e2 ) β ψ j λα −

1 d
64
   iǫ âb̂ ee1 (Γe2 )α β ψ c i β λiα ∇e2 Wee1 + 41 iψ c i α λiα ∇â W d b̂ − 12 i(Σâe )α β ψ c i β λiα ∇e W d b̂ −
1
4
  i(Σd e )α β ψ c i β λiα ∇e Wâb̂ + 83 i(Σâb̂ )α β ψ c i β λiα ∇e W de + 12 i(Σd e )α β ψ c i β λiα ∇â W e b̂ +
1                                     5 d
4
  i(Σâ d )α β ψ c i β λiα ∇e Wb̂e − 64 iǫ âb̂e2 e (Γe1 )α β ψ c i β λiα ∇e2 Wee1 −
1 d
64
   iǫ âb̂e2 e (Γe2 )α β ψ c i β λiα ∇e1 Wee1 − 41 i(Σee1 )α β δ d â ψ c i β λiα ∇b̂ W ee1 −
1
4
  i(Σâe )α β δ d b̂ ψ c i β λiα ∇e1 W ee1 − 81 iδ d â ψ c i α λiα ∇e Wb̂e − 12 i(Σe1 e )α β δ d â ψ c i β λiα ∇e1 W e b̂ +
1                                     1
2
  i(Σâe )α β ψ c i β λiα ∇b̂ W de + 16 iǫâb̂e2 ee1 (Γd )α β ψ c i β λiα ∇e2 Wee1 +

                                                             212
```

</details>

<a id="src-c24-p312"></a>

<details>
<summary>C24-p312 — PDF page 312: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p312: PDF page 312](https://arxiv.org/pdf/2311.00679v1#page=312) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
   3 d                                               5
   32
      iǫ âe1 e2 e (Γe1 )α β ψ c i β λiα ∇e2 Wb̂e − 64 iǫâb̂e1 e2 e (Γe1 )α β ψ c i β λiα ∇e2 W de −
   3 d                                             1 e4 ee1 e2 e3
   32
      iǫ âe2 ee1 (Γe2 )α β ψ c i β λiα ∇b̂ Wee1 + 32 iǫ          (Σâe4 )α β δ d b̂ ψ c i β Wee1 We2 e3 λiα +
   3 dee1 e2 e3
   32
      iǫ        (Σâb̂ )α β ψ c i β Wee1 We2 e3 λiα + 2(Σâb̂ )α β φc i β ∇d λiα −

  δ d â φc i α ∇b̂ λiα + 2(Σâ d )α β φc i β ∇b̂ λiα − 12 (Γd )α β φc i β Wâb̂ λiα +
   1 d                            1 e2
   8
     ǫ âb̂ ee1 φc i α Wee1 λiα + 16 ǫ âb̂ ee1 (Σe2 d )α β φc i β Wee1 λiα − 18 ǫde1 e2 â e (Σe1 e2 )α β φc i β Wb̂e λiα −
   1
   4
     (Γe )α β δ d â φc i β Wb̂e λiα + 34 (Γâ )α β φc i β Wb̂ d λiα − 81 ǫde2 âb̂ e (Σe2 e1 )α β φc i β Wee1 λiα −
   5 e2 e3 ee1
   16
      ǫ   b̂   (Σe2 e3 )α β δ d â φc i β Wee1 λiα + 21 i(Γd )α β φc i β W Wâb̂α i −

  4Fâb̂ f cd − 4δ d â Fb̂e f ce − 4Fâ d f c b̂

5.2.5      ∇a ✷W

D a ∇b ∇b W − 12 iψ a i α ∇b ∇b λiα + 32
                                      3 de
                                         iǫ e1 bc (Σde )α β ψ a i β λiα ∇e1 Wbc −
 9
32
   i(Γb )α β ψ a i β λiα ∇c Wbc + 18 iǫde e1 bc (Σde )α β ψ a i β Wbc ∇e1 λiα − 12 i(Γb )α β ψ a i β Wbc ∇c λiα +
                               9
1
8
  (Γb )α β ψ a i β Xαi ∇b W + 128 iψ a i α W bc Wbc λiα + 18 iΦbc i j (Σbc )α β ψ a j β λiα +
 1 a α
32
   ψ i W W bc Wbcα i +(Γb )α β φa i β ∇b λiα + 98 (Σbc )α β φa i β W bc λiα +

2∇b W f a b

5.2.6      ∇a ✷λiα

                  55                                   19
  D a ∇b ∇b λiα + 256 (Σbc )αβ ψ aiβ W W bc W de Wde − 32 (Σde )αβ ψ aiβ W W bc Wdb Wec +
   19 bcdee1                                    37
   256
       ǫ     (Γe2 )αβ ψ aiβ W Wbc Wde We1 e2 − 128 (Γd )αβ ψ aiβ W bc Wbc ∇d W +
   1
     ǫ bcde ψ ai α Wbc Wde ∇e1 W + 18 ǫe1 bcde (Σe1 e2 )αβ ψ aiβ Wbc Wde ∇e2 W −
   32 e1

   5 a                        1
   64
      ψ jα W bc λiβ Wbcβ j + 128 ǫe1 bcde (Γe1 )αρ ψ a j ρ Wbc λiβ Wdeβ j +
   1
   16
                                           3
      (Σd b )αρ ψ a j ρ W bc λiβ Wdcβ j − 64 (Σbc )β ρ ψ aiρ W bc λjα Xβj + 64
                                                                            3
                                                                               (Σbc )β ρ ψ a j ρ W bc λjα Xβi −
   23                                1
   64
      (Γd )αβ ψ aiβ W Wbc ∇d W bc − 128 ǫe1 debc ψ ai α W Wbc ∇e1 Wde +

                                                              213
```

</details>

<a id="src-c24-p313"></a>

<details>
<summary>C24-p313 — PDF page 313: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p313: PDF page 313](https://arxiv.org/pdf/2311.00679v1#page=313) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
63 e1 debc                                   17 ee1
256
    ǫ      (Σe1 e2 )αβ ψ aiβ W Wbc ∇e2 Wde + 128 ǫ e2 d b (Σee1 )αβ ψ aiβ W Wbc ∇e2 W dc +
1                                11                                1
32
   (Γd )αβ ψ aiβ W Wbc ∇b W dc + 64 (Γb )αβ ψ aiβ W Wbc ∇d W dc − 16 Φbc ij ψ a jα F bc +
1 ee1 bc
32
   ǫ d Φee1 ij (Γd )αβ ψ a j β Fbc + 14 Φd b ij (Σdc )αβ ψ a j β F bc − 32
                                                                         1
                                                                           Φbc ij ψ a jα W W bc +
 7 ee1 bc
192
    ǫ d Φee1 ij (Γd )αβ ψ a j β W Wbc + 11
                                        24
                                           Φd b ij (Σdc )αβ ψ a j β W W bc +
1 bc k                         1 bcde
8
  Φ j (Σbc )αβ ψ a k β X ij + 48 ǫ          ij         a β e1
                                      e1 Φbc (Σde )αβ ψ j ∇ W −

5                              3                              3
  Φ ij (Γb )αβ ψ a j β ∇c W − 32
8 bc
                                 (Γd )αβ ψ aiβ Fbc ∇d W bc − 64 ǫe1 debc ψ ai α Fbc ∇e1 Wde +
15 e1 debc
128
    ǫ      (Σe1 e2 )αβ ψ aiβ Fbc ∇e2 Wde − 15
                                           64
                                              ǫee1 e2 d b (Σee1 )αβ ψ aiβ Fbc ∇e2 W dc +
3                               9                              9 e1
16
   (Γd )αβ ψ aiβ Fbc ∇b W dc − 32 (Γb )αβ ψ aiβ Fbc ∇d W dc − 128 ǫ e2 e bc (Σe1 d )αβ ψ aiβ W Wbc ∇e2 W de −
 9 e1 e2 deb                                  3 de
256
    ǫ        (Σe1 e2 )αβ ψ aiβ W Wbc ∇c Wde + 32 ǫ e1 bc (Σde )αβ ψ a j β X ij ∇e1 Wbc −
9                                 9
32
   (Γb )αβ ψ a j β X ij ∇c Wbc − 16 (Σbc )αβ ψ aiβ ∇d W ∇d W bc + 78 (Σdb )αβ ψ aiβ ∇c W ∇d W bc +
1                                        3 ai                 13
  ǫ
32 dee1 bc
           (Γd )αβ ψ aiβ ∇e W ∇e1 W bc + 32 ψ α ∇b W ∇c Wbc + 16 (Σdb )αβ ψ aiβ ∇d W ∇c W bc +
 9                                  9                          3 a β
128
    (Σbc )αβ ψ aiβ W de Wde F bc + 128 ψ a jα X ij W bc Wbc − 64 ψ j W bc λiα Wbcβ j +
1 a β                     1
64
   ψ j W bc λiβ Wbcα j + 128 ǫe1 bcde (Γe1 )α β ψ a j ρ Wbc λiρ Wdeβ j +
1
16
   (Σd b )α β ψ a j ρ W bc λiρ Wdcβ j − 12 (Σbc )αβ ψ aiβ ∇d ∇d F bc − 41 (Σbc )αβ ψ aiβ W bc ∇d ∇d W −
3
8
  (Σbc )αβ ψ aiβ W ∇d ∇d W bc − 12 ψ a jα ∇b ∇b X ij + 21 (Γb )αβ ψ aiβ ∇c ∇c ∇b W −
1                              1                                3 e1 bcde
8
  (Γd )αβ ψ aiβ Wbc ∇d F bc − 16 ǫe1 bcde ψ ai α Wde ∇e1 Fbc + 16 ǫ       (Σe1 e2 )αβ ψ aiβ Wde ∇e2 Fbc +
3 ee1
8
  ǫ e2 b d (Σee1 )αβ ψ aiβ Wdc ∇e2 F bc − 21 (Γb )αβ ψ aiβ Wdc ∇d F bc +
1
4
  (Γd )αβ ψ aiβ Wdc ∇b F bc + 81 ǫde e1 bc (Σde )αβ ψ a j β Wbc ∇e1 X ij −
1
2
  (Γb )αβ ψ a j β Wbc ∇c X ij −(Σb d )αβ ψ aiβ Wbc ∇c ∇d W + 81 ǫdee1 bc (Γd )αβ ψ aiβ Wbc ∇e ∇e1 W +
1 ai
2
  ψ α Wbc ∇b ∇c W − 12 (Σb d )αβ ψ aiβ Wbc ∇d ∇c W + 64
                                                     3 e1
                                                        ǫ e2 e bc (Σe1 d )αβ ψ aiβ Fbc ∇e2 W de +
 3 e1 e2 deb
128
    ǫ        (Σe1 e2 )αβ ψ aiβ Fbc ∇c Wde − 18 ǫe1 e2 bcd (Σe1 e )αβ ψ aiβ Wde ∇e2 Fbc +
1 e1 e2 bde
16
   ǫ        (Σe1 e2 )αβ ψ aiβ Wde ∇c Fbc − 14 (Γb )αβ ψ aiβ Wb c Wcd ∇d W −
1 e1                                        1 e1 e2 bcd
8
  ǫ e2 bcd (Σe1 e )αβ ψ aiβ Wbc Wde ∇e2 W + 16 ǫ        (Σe1 e2 )αβ ψ aiβ Wbc Wde ∇e W +
1 e1                                          1 e1 e2 dbc
32
   ǫ e2 deb (Σe1 c )αβ ψ aiβ W Wbc ∇e2 Wde − 64 ǫ         (Σe1 e2 )αβ ψ aiβ W Wbc ∇e Wde −
3 de
16
   ǫ e1 bc (Σde )αρ ψ a j ρ λiβ ∇e1 Wbcβ j + 38 (Γb )αρ ψ a j ρ λiβ ∇c Wbcβ j −

                                                    214
```

</details>

<a id="src-c24-p314"></a>

<details>
<summary>C24-p314 — PDF page 314: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p314: PDF page 314](https://arxiv.org/pdf/2311.00679v1#page=314) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    ǫ e1 bc (Σde )αρ ψ a j ρ Wbc βj ∇e1 λiβ + 12 (Γb )αρ ψ a j ρ Wbc βj ∇c λiβ +
  1 de
  4

    ǫ e1 bc (Σde )α ρ ψ a j β Wbcβ j ∇e1 λiρ − 81 (Γb )α β ψ a j ρ Xβj ∇b λiρ +
  1 de
  8

  1
  8
    (Γb )βρ ψ a jα Xβj ∇b λiρ − 81 (Γb )αρ ψ a j ρ X jβ ∇b λiβ − 18 (Γb )β ρ ψ a j ρ Xαj ∇b λiβ +
  3
  16
     (Γb )β ρ ψ aiρ λjα ∇b Xβj + 38 (Γb )β ρ ψ aiρ Xjβ ∇b λjα − 16
                                                                 3
                                                                   (Γb )β ρ ψ a j ρ λjα ∇b Xβi +
  3                               1 de
  8
    (Γb )β ρ ψ a j ρ Xβi ∇b λjα + 24 ǫ e1 bc (Σde )αβ ψ a j β W ∇e1 Φbcij − 14 (Γb )αβ ψ a j β W ∇c Φbcij +
  1                                1
  4
    (Σdb )αβ ψ aiβ W ∇c ∇d W bc + 16 ǫdee1 bc (Γd )αβ ψ aiβ W ∇e ∇e1 W bc +
  3 ai
  16
     ψ α W ∇b ∇c Wbc + 18 (Σdb )αβ ψ aiβ W ∇d ∇c W bc + 16
                                                         9
                                                           iφai α W bc Fbc −
  9
    iǫ debc (Γe1 )αβ φaiβ Wde Fbc − 49 i(Σb d )αβ φaiβ W dc Fbc + 39
  32 e1                                                           64
                                                                     iφai α W W bc Wbc −
  11
     iǫ bcde (Γe1 )αβ φaiβ W Wbc Wde − 89 i(Σbc )αβ φa j β X ij W bc + 16
  64 e1
                                                                        1 de
                                                                          iǫ e1 bc (Σde )αβ φaiβ Wbc ∇e1 W +
  21
  8
     i(Γb )αβ φaiβ Wbc ∇c W − 11
                               8
                                 i(Σbc )α ρ φa j β λiρ Wbcβ j − 15
                                                                16
                                                                   iφaiβ λjαXβj +
  15 a β j
  16
     iφ j λα Xβi − 43 iΦbcij (Σbc )αβ φa j β W − 16
                                                  3 de
                                                    iǫ e1 bc (Σde )αβ φaiβ W ∇e1 Wbc +
  27
  16
     i(Γb )αβ φaiβ W ∇c Wbc −2iφai α ∇b ∇b W − 12 iǫde e1 bc (Σde )αβ φaiβ ∇e1 Fbc +

  i(Γb )αβ φaiβ ∇c Fbc −i(Γb )αβ φa j β ∇b X ij −2i(Σbc )αβ φaiβ ∇b ∇c W −

  4(Σbc )α β ∇c λiβ f ab

5.2.7    ∇a ✷Fab

                     7
  D c ∇d ∇d Fâb̂ + 128 iǫe1 e2 âb̂e3 (Σe1 e2 )α β ψ c i β W de Wde ∇e3 λiα + 13
                                                                               64
                                                                                  i(Γâ )α β ψ c i β W de Wde ∇b̂ λiα +
  7                                                      1
    iǫ dee1 e2 (Σâb̂ )α β ψ c i β Wde We1 e2 ∇e3 λiα − 32
  32 e3
                                                           iǫâ dee1 e2 ψ c i α Wde We1 e2 ∇b̂ λiα +
  1
  8
    i(Γd )α β ψ c i β Wâb̂ Wde ∇e λiα + 81 i(Γd )α β ψ c i β Wâd Wb̂e ∇e λiα −
  1                                                     1 e3 dee1 e2
    iǫ dee1 e2 (Σâe3 )α β ψ c i β Wde We1 e2 ∇e3 λiα + 16
  16 b̂
                                                           iǫ        (Σâe3 )α β ψ c i β Wde We1 e2 ∇b̂ λiα −
  55                                 19
  256
      iψ c i α W de Wâb̂ Wde λiα + 256 iǫe3 dee1 e2 (Γe3 )α β ψ c i β Wâb̂ Wde We1 e2 λiα +
  57                                              3
  64
     i(Σe1 d )α β ψ c i β W de Wâb̂ We1 e λiα − 32 iǫâb̂e3 e1 e2 (Γe3 )α β ψ c i β W de We1 e2 Wde λiα −
  83                                             19
  128
      i(Σâ e1 )α β ψ c i β W de Wb̂e1 Wde λiα + 32 iψ c i α W de Wâd Wb̂e λiα +
  95
  32
     i(Σâ e1 )α β ψ c i β W de Wb̂d We1 e λiα − 19 iǫ dee1 e2 (Γe3 )α β ψ c i β Wb̂d Wee1 We2 e3 λiα −
                                                 64 â

                                                          215
```

</details>

<a id="src-c24-p315"></a>

<details>
<summary>C24-p315 — PDF page 315: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p315: PDF page 315](https://arxiv.org/pdf/2311.00679v1#page=315) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
19                                                     19
   iǫ dee1 e2 (Γe3 )α β ψ c i β Wâd Wb̂e We1 e2 λiα − 64
64 e3
                                                          iǫâe3 ee1 e2 (Γe3 )α β ψ c i β Wb̂ d Wee1 We2 d λiα −
19                                              1
32
   i(Σâd )α β ψ c i β W de Wb̂ e1 We1 e λiα − 16 (Σd e1 )α β ψ c i β W e1 e Fde Wâb̂α i +
3 c α                       1
32
   ψ i W de Fâb̂ Wdeα i − 256 ǫe3 dee1 e2 (Γe3 )α β ψ c i β Wde Fâb̂ We1 e2 α i −
1                                             1
16
   (Σe1 d )α β ψ c i β W de Fâb̂ We1 eα i − 64 ǫâe3 ee1 e2 (Γe3 )α β ψ c i β Wee1 Fb̂ d We2 dα i −
1
8
  (Σee1 )α β ψ c i β Wâe Fb̂ d We1 dα i − 81 (Σâe )α β ψ c i β W ee1 Fb̂ d Wde1 α i −
 1                                                      1
   ǫ
256 âb̂e3
           e1 e2
                 (Γe3 )α β ψ c i β We1 e2 F de Wdeα i + 16 (Σâ e1 )α β ψ c i β Wb̂e1 F de Wdeα i +
1                                             1
16
   (Σe1 d )α β ψ c i β Wâb̂ F de We1 eα i − 16 (Σee1 )α β ψ c i β Wâ d Fb̂d Wee1 α i −
1
8
  (Σâ e1 )α β ψ c i β Wb̂d F de We1 eα i − 18 (Σde1 )α β ψ c i β Wâ e Fb̂d We1 eα i +
1
8
  (Σâd )α β ψ c i β Wb̂ e1 F de We1 eα i + 18 (Σâ e1 )α β ψ c i β W de Fb̂d We1 eα i −
1                                              3
16
   (Σâb̂ )α β ψ c i β W ee1 F d e Wde1 α i − 16 (Σâ d )α β ψ c i β W ee1 Fb̂d Wee1 α i +
 1                                                   1
   ǫ de2 e3 (Γe1 )α β ψ c i β We1 e Fde We2 e3 α i + 16
128 âb̂
                                                        (Σde )α β ψ c i β Wâ e1 F de Wb̂e1 α i +
1                                           1
8
  (Σe1 e )α β ψ c i β W ed Fâd Wb̂e1 α i + 16 (Σee1 )α β ψ c i β W ee1 Fâ d Wb̂dα i +
1
16
   (Σâ e1 )α β ψ c i β W de Fde Wb̂e1 α i − 18 (Σâe1 )α β ψ c i β W e1 e F d e Wb̂dα i +
1
8
  (Σe1 d )α β ψ c i β Wâe F de Wb̂e1 α i − 18 (Σe1 d )α β ψ c i β Wâe1 F de Wb̂eα i −
1
8
  (Σd e )α β ψ c i β W ee1 Fâd Wb̂e1 α i + 18 (Σâ d )α β ψ c i β W ee1 Fde Wb̂e1 α i −
7 e1 e2   de        α   c β     i  e3       1    d α   c β     i  e
64
   iǫ   e3 (Σe1 e2 ) β ψ i Wde λα ∇ Wâb̂ + 4 i(Γ ) β ψ i Wde λα ∇ Wâb̂ −

7         e1 e2                                          25
  iǫ
64 âb̂e3
                (Σde )α β ψ c i β W de λiα ∇e3 We1 e2 − 128 iǫâb̂ e1 e2 d ψ c i α Wde λiα ∇e We1 e2 −
9                                         1
32
   i(Γe )α β ψ c i β Wb̂d λiα ∇â W ed + 16 i(Γâ )α β ψ c i β Wde λiα ∇b̂ W de +
5                                        1
64
   i(Γd )α β ψ c i β Wâb̂ λiα ∇e Wde − 64 i(Γâ )α β ψ c i β Wb̂d λiα ∇e W ed −
3                                                     7 e3
  iǫ e1 e2 d (Σe e3 )α β ψ c i β Wde λiα ∇e3 We1 e2 + 32
64 âb̂
                                                         iǫ âb̂ e1 e2 (Σe3 d )α β ψ c i β Wde λiα ∇e We1 e2 +
3                                       1
  iǫ e1 de ψ c i α Wde λiα ∇e2 Wb̂e1 − 32
64 âe2
                                          i(Γe )α β ψ c i β Wb̂d λiα ∇d Wâe −
3
32
   i(Γe )α β ψ c i β Wb̂d λiα ∇e Wâ d − 14 i(Γâ )α β ψ c i β Wde λiα ∇d Wb̂ e +
1 e2
2
  iǫ âe3 e1 d (Σe2 e )α β ψ c i β Wde λiα ∇e3 Wb̂e1 − 18 iǫe2 e3 e1 de (Σe2 e3 )α β ψ c i β Wde λiα ∇â Wb̂e1 −
3
8
  i(Γd )α β ψ c i β Wde λiα ∇â Wb̂ e + 18 iǫe2 e3 â de (Σe2 e3 )α β ψ c i β Wde λiα ∇e1 Wb̂e1 +
7                                       5 e1 e2
64
   i(Γd )α β ψ c i β Wb̂d λiα ∇e Wâe + 64 iǫ                   α   c β     i  e3 de
                                                âb̂e3 (Σe1 e2 ) β ψ i Wde λα ∇ W +

                                                         216
```

</details>

<a id="src-c24-p316"></a>

<details>
<summary>C24-p316 — PDF page 316: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p316: PDF page 316](https://arxiv.org/pdf/2311.00679v1#page=316) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
15                                                       3
   iǫ e1 e2 de (Σâb̂ )α β ψ c i β Wde λiα ∇e3 We1 e2 − 64
64 e3
                                                           iǫâ e1 e2 de ψ c i α Wde λiα ∇b̂ We1 e2 −
3                                                      3 e3 e1 e2 de
  iǫ e1 e2 de (Σâe3 )α β ψ c i β Wde λiα ∇e3 We1 e2 + 32
32 b̂
                                                          iǫ         (Σâe3 )α β ψ c i β Wde λiα ∇b̂ We1 e2 −
1
  iǫ
32 âb̂e2 e1
              ψ i Wde λiα ∇e2 W e1 e + 81 iǫe2 b̂e3 e1 d (Σâe2 )α β ψ c i β Wde λiα ∇e3 W e1 e −
             d c α

1 e2 e3     d         α   c β     i       e1 e   1 e2 e3                 α   c β     i  d  e1 e
32
   iǫ   âb̂ (Σe2 e3 ) β ψ i Wde λα ∇e1 W      + 32 iǫ   âb̂e1 (Σe2 e3 ) β ψ i Wde λα ∇ W      −
1                                  1 de
8
  (Γd )α β ψ c i β Xαi ∇d Fâb̂ − 12 iǫ âb̂e1 Φdei j ψ c j α ∇e1 λiα − 16 iΦâb̂i j (Γd )α β ψ c j β ∇d λiα −
                                    11 de1
iΦâdi j (Γb̂ )α β ψ c j β ∇d λiα − 24 iǫ âb̂e2 Φd e i j (Σe1 e )α β ψ c j β ∇e2 λiα +
11 dee1 e2        j         α   c β     i   1        j  d α   c β     i
48
   iǫ      â Φdei (Σe1 e2 ) β ψ j ∇b̂ λα + 12 iΦâdi (Γ ) β ψ j ∇b̂ λα −

7                                         13                                3 e1 e2
48
   iΦde i j (Σde )α β ψ c j β Wâb̂ λiα + 48 iΦâ d i j ψ c j α Wb̂d λiα + 32 iǫ       d        j  e α   c β      i
                                                                                    âe Φe1 e2 i (Γ ) β ψ j Wb̂d λα +

5                                           13
24
   iΦâ e i j (Σe d )α β ψ c j β Wb̂d λiα − 24 iΦed i j (Σâe )α β ψ c j β Wb̂d λiα +
13 dee1          j         α   c β e2 i  19 dee1           j       α   c β e2 i
48
   iǫ   âb̂ Φdei (Σe1 e2 ) β ψ j ∇ λα − 24 iǫ   b̂e2 Φâdi (Σee1 ) β ψ j ∇ λα −

1 de j                                1
8
  Φ i (Σde )α β ψ c j β W Wâb̂α i − 32 iǫâb̂ de e2 (Γe1 )α β ψ c i β ∇e1 Wde ∇e2 λiα +
3
4
  iψ c i α ∇d Wâb̂ ∇d λiα + 12 i(Σde )α β ψ c i β ∇d Wâb̂ ∇e λiα − 21 iψ c i α ∇â Wb̂d ∇d λiα +

i(Σâe )α β ψ c i β ∇e Wb̂d ∇d λiα −i(Σde )α β ψ c i β ∇â W d b̂ ∇e λiα + 12 i(Σâe )α β ψ c i β ∇d Wb̂d ∇e λiα −

i(Σâd )α β ψ c i β ∇b̂ W d e ∇e λiα − 34 i(Σâb̂ )α β ψ c i β ∇d Wde ∇e λiα − 128
                                                                                5
                                                                                   iǫâb̂e1 d e2 (Γe )α β ψ c i β ∇e1 Wde ∇e2 λiα −
19
   iǫ     d
128 âb̂e1 e2
              (Γe1 )α β ψ c i β ∇e Wde ∇e2 λiα + 18 i(Σde )α β ψ c i β ∇â W de ∇b̂ λiα −
13                                        3
8
   i(Σâd )α β ψ c i β ∇e W de ∇b̂ λiα − 32 iǫâe1 e2 de (Γe1 )α β ψ c i β ∇e2 Wde ∇b̂ λiα +
13
16
   iψ c i α ∇d Wâd ∇b̂ λiα + 14 i(Σed )α β ψ c i β ∇e W d â ∇b̂ λiα + 64
                                                                        3 e1 e2
                                                                           iǫ     de        α   c β       i  e3
                                                                                e3 (Σe1 e2 ) β ψ i Wâb̂ λα ∇ Wde +

1 e1 e2     d         α   c β     i  e3  e   13        e1 de c α
16
   iǫ   âe3 (Σe1 e2 ) β ψ i Wde λα ∇ Wb̂ − 128 iǫâb̂      ψ i Wde λiα ∇e2 We1 e2 −
5         de                                             1
  iǫ
64 âb̂e2
             (Σe3 e1 )α β ψ c i β Wde λiα ∇e3 W e1 e2 + 16 iǫâe2 ee1 d ψ c i α Wb̂d λiα ∇e2 Wee1 +
43 e2 ee1 d                                           15 e1 e2
128
    iǫ â   (Σe2 e3 )α β ψ c i β Wb̂d λiα ∇e3 Wee1 − 128 iǫ      ed        α   c β      i  e3
                                                               e3 (Σe1 e2 ) β ψ i Wb̂d λα ∇ Wâe +

73 e1 e2                 α   c β      i  e3 ed 57 e1 e2   de        α   c β        i e3
128
    iǫ   âe3 e (Σe1 e2 ) β ψ i Wb̂d λα ∇ W − 512 ǫ     e3 (Σe1 e2 ) β ψ i W Wâb̂α ∇ Wde +

63                                        3
256
    (Γd )α β ψ c i β W Wâb̂α i ∇e Wde − 16 iǫâe1 de e2 (Γe1 )α β ψ c i β ∇b̂ Wde ∇e2 λiα +
21        de                                      9 e3
   iǫ
64 âb̂e1
             (Γe1 )α β ψ c i β ∇e2 Wde ∇e2 λiα + 32 iǫ âb̂ de (Σe3 e1 )α β ψ c i β Wde λiα ∇e2 W e1 e2 +
27 e2                                                     27 e2 e3 ee1 d
64
   iǫ âe3 e1 d (Σe2 e )α β ψ c i β Wb̂d λiα ∇e3 W ee1 − 256 iǫ          (Σe2 e3 )α β ψ c i β Wb̂d λiα ∇â Wee1 +
27 e2 e3 ee1                                          3
256
    iǫ  â   (Σe2 e3 )α β ψ c i β Wb̂d λiα ∇d Wee1 + 512 ǫâb̂e3 de (Σe1 e2 )α β ψ c i β W Wdeα i ∇e3 W e1 e2 +

                                                         217
```

</details>

<a id="src-c24-p317"></a>

<details>
<summary>C24-p317 — PDF page 317: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p317: PDF page 317](https://arxiv.org/pdf/2311.00679v1#page=317) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3                                        3
   ǫ e1 de ψ c i α W Wdeα i ∇e2 We1 e2 + 128
512 âb̂
                                             (Γâ )α β ψ c i β W Wdeα i ∇d Wb̂ e −
 3                                        3
256
    (Γd )α β ψ c i β W Wdeα i ∇e Wâb̂ − 256 (Γâ )α β ψ c i β W Wdeα i ∇b̂ W de −
 3                                         3
128
    (Γd )α β ψ c i β W Wdeα i ∇â Wb̂ e + 256 ǫâb̂e2 de (Σe3 e1 )α β ψ c i β W Wdeα i ∇e3 W e1 e2 −
 3 e3                                                      3
256
    ǫ âb̂ de (Σe3 e1 )α β ψ c i β W Wdeα i ∇e2 W e1 e2 + 256 ǫâe2 ee1 d ψ c i α W Wb̂dα i ∇e2 Wee1 −
 3                                         3
128
    (Γe )α β ψ c i β W Wb̂dα i ∇e Wâ d + 128 (Γâ )α β ψ c i β W Wb̂dα i ∇e W ed+
 3                                        3 e2
128
    (Γd )α β ψ c i β W Wb̂dα i ∇e Wâe − 64 ǫ âe3 e1 d (Σe2 e )α β ψ c i β W Wb̂dα i ∇e3 W ee1 +
 3 e2 e3 ee1 d                                            3
256
    ǫ          (Σe2 e3 )α β ψ c i β W Wb̂dα i ∇â Wee1 + 128 (Γe )α β ψ c i β W Wb̂dα i ∇â W ed −
 3 e2 e3 ee1                                           3
256
    ǫ   â   (Σe2 e3 )α β ψ c i β W Wb̂dα i ∇d Wee1 + 128 (Γe )α β ψ c i β W Wb̂dα i ∇d Wâe +
5                                                27
  iǫ
64 âb̂e2
          de
             (Γe1 )α β ψ c i β ∇e2 Wde ∇e1 λiα + 64 iǫâee1 d e2 (Γe )α β ψ c i β ∇e1 Wb̂d ∇e2 λiα −
 9                                 3
128
    ψ c i α W W de Wde Wâb̂α i − 256 ǫâb̂e3 de (Γe3 )α β ψ c i β W e1e2 Fde We1 e2 α i +
 1                                                     1
   ǫ dee1 e2 (Γe3 )α β ψ c i β Wâb̂ Fde We1 e2 α i + 64
256 e3
                                                         ǫâe3 dee2 (Γe3 )α β ψ c i β Wb̂ e1 Fde We2 e1 α i −
 1
   ǫ e1 e2 e3 (Γd )α β ψ c i β We1 e Fde We2 e3 α i −i(Γâ )α β ψ c i β ∇d ∇d ∇b̂ λiα +
128 âb̂

3
8
  iψ c i α λiα ∇d ∇d Wâb̂ + 12 iψ c i α Wâb̂ ∇d ∇d λiα + 64
                                                           9
                                                              iǫâb̂e1 de (Γe1 )α β ψ c i β λiα ∇e2 ∇e2 Wde +
3
  iǫ
16 âb̂e1
          de
             (Γe1 )α β ψ c i β Wde ∇e2 ∇e2 λiα + 21 i(Σâ d )α β ψ c i β Wb̂d ∇e ∇e λiα +

  ψ i Wâb̂α i ∇d ∇d W +ψ c i α ∇d W ∇d Wâb̂α i + 21 ψ c i α W ∇d ∇d Wâb̂α i −
1 c α
2

3            d                                     3
  iǫ
16 âb̂e1 e2
               (Γe )α β ψ c i β Wde ∇e1 ∇e2 λiα + 16 iǫâb̂e1 e2 d (Γe1 )α β ψ c i β Wde ∇e ∇e2 λiα −
1
2
  i(Σde )α β ψ c i β W de ∇â ∇b̂ λiα − 2i(Σâ d )α β ψ c i β Wde ∇e ∇b̂ λiα −
1
  iǫ
8 âe1 e2
          de
             (Γe1 )α β ψ c i β Wde ∇e2 ∇b̂ λiα −iψ c i α Wb̂d ∇d ∇â λiα +i(Σd e )α β ψ c i β Wb̂d ∇e ∇â λiα −
 5                                                         11 e2 e1 de
128
    iǫe1 e2 e3 de (Σe1 e2 )α β ψ c i β Wâb̂ Wde ∇e3 λiα + 32 iǫ â    (Σe2 e3 )α β ψ c i β Wde λiα ∇e3 Wb̂e1 +
9 e1 e2     e         α   c β   d     e3 i  3    e α   c β   d         i
32
   iǫ   âe3 (Σe1 e2 ) β ψ i Wb̂ Wed ∇ λα − 8 i(Γ ) β ψ i Wb̂ Wed ∇â λα +

1
2
  i(Γâ )α β ψ c i β Wb̂ d Wde ∇e λiα − 13 iǫ dee1 ψ c i α Wde We1 e2 ∇e2 λiα −
                                        64 âb̂

7                                                   5
  iǫ dee1 (Σe2 e3 )α β ψ c i β Wde We1 e2 ∇e3 λiα + 32
32 âb̂
                                                       iǫâe2 dee1 ψ c i α Wb̂d Wee1 ∇e2 λiα +
3 e2 dee1                                           3 e1 e2
4
  iǫ â   (Σe2 e3 )α β ψ c i β Wb̂d Wee1 ∇e3 λiα − 16 iǫ      de        α   c β           e3 i
                                                            e3 (Σe1 e2 ) β ψ i Wâd Wb̂e ∇ λα −

1
  iǫ
16 âb̂e2
          de
             (Γe1 )α β ψ c i β Wde ∇e2 ∇e1 λiα − 38 iǫâee1 e2 d (Γe )α β ψ c i β Wb̂d ∇e1 ∇e2 λiα −
11
   iǫ
128 âb̂e3
           e1 e2
                 (Σde )α β ψ c i β W de We1 e2 ∇e3 λiα + 29
                                                         64
                                                            iǫe3 âb̂ de (Σe3 e1 )α β ψ c i β Wde We1 e2 ∇e2 λiα −

                                                        218
```

</details>

<a id="src-c24-p318"></a>

<details>
<summary>C24-p318 — PDF page 318: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p318: PDF page 318](https://arxiv.org/pdf/2311.00679v1#page=318) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
11 e1 e2   de        α   c β          i e3   13   d α   c β          i e
64
   ǫ     e3 (Σe1 e2 ) β ψ i Wde Wâb̂α ∇ W + 32 (Γ ) β ψ i Wde Wâb̂α ∇ W −

11 e1 e2   de        α   c β       e3     i 13    d α   c β       e      i
64
   ǫ     e3 (Σe1 e2 ) β ψ i W Wde ∇ Wâb̂α + 32 (Γ ) β ψ i W Wde ∇ Wâb̂α +

17
   iǫ
128 âb̂e1 e2
              d
                (Γe1 )α β ψ c i β ∇e2 Wde ∇e λiα + 78 iǫe2 âe3 de (Σe2 e1 )α β ψ c i β Wb̂d Wee1 ∇e3 λiα −
7 e2 e3 dee1                                          7 e2 e3 ee1
32
   iǫ        (Σe2 e3 )α β ψ c i β Wb̂d Wee1 ∇â λiα + 32 iǫ  â   (Σe2 e3 )α β ψ c i β Wb̂d Wee1 ∇d λiα −
1            d                                     1
  iǫ
16 âb̂e1 e2
               (Γe1 )α β ψ c i β Wde ∇e2 ∇e λiα + 64 ǫâb̂e3 e1 e2 (Σde )α β ψ c i β W de We1 e2 α i ∇e3 W +
1                                         1
  ǫ de1 e2 ψ c i α Wde We1 e2 α i ∇e W − 16
64 âb̂
                                            (Γâ )α β ψ c i β Wb̂ d Wdeα i ∇e W −
1                                        1
32
   (Γd )α β ψ c i β Wâb̂ Wdeα i ∇e W − 32 (Γâ )α β ψ c i β W de Wdeα i ∇b̂ W −
1                                        1
16
   (Γe )α β ψ c i β Wb̂ d Wedα i ∇â W + 32 ǫâb̂ de1 e2 (Σe e3 )α β ψ c i β Wde We1 e2 α i ∇e3 W −
1 e3                                                      1
32
   ǫ âb̂ e1 e2 (Σe3 d )α β ψ c i β Wde We1 e2 α i ∇e W + 32 ǫâe2 dee1 ψ c i α Wde Wb̂e1 α i ∇e2 W −
1                                        1
16
   (Γe )α β ψ c i β Wâ d Wb̂dα i ∇e W + 16 (Γd )α β ψ c i β Wâd Wb̂eα i ∇e W +
1                                        1 e2
16
   (Γd )α β ψ c i β Wd e Wb̂eα i ∇â W + 16 ǫ âe3 de (Σe2 e1 )α β ψ c i β Wde Wb̂e1 α i ∇e3 W −
1 e2                                                    1 e2 e3 de1
16
   ǫ e3 dee1 (Σâe2 )α β ψ c i β Wde Wb̂e1 α i ∇e3 W − 16 ǫ    â   (Σe2 e3 )α β ψ c i β Wde Wb̂e1 α i ∇e W +
1                                        1
16
   (Γe )α β ψ c i β Wâd Wb̂eα i ∇d W − 16 (Γâ )α β ψ c i β W d e Wb̂dα i ∇e W +
1         e1 e2                                            1
  ǫ
64 âb̂e3
                (Σde )α β ψ c i β W W de ∇e3 We1 e2 α i + 64 ǫâb̂ de1 e2 ψ c i α W Wde ∇e We1 e2 α i −
1                                         1
32
   (Γâ )α β ψ c i β W W de ∇b̂ Wdeα i − 16 (Γe )α β ψ c i β W Wb̂ d ∇â Wedα i −
1                                         1
16
   (Γâ )α β ψ c i β W Wb̂ d ∇e Wdeα i − 32 (Γd )α β ψ c i β W Wâb̂ ∇e Wdeα i +
1                                                      1 e3
  ǫ de1 e2 (Σe e3 )α β ψ c i β W Wde ∇e3 We1 e2 α i − 32
32 âb̂
                                                         ǫ âb̂ e1 e2 (Σe3 d )α β ψ c i β W Wde ∇e We1 e2 α i +
1                                       1
  ǫ dee1 ψ c i α W Wde ∇e2 Wb̂e1 α i − 16
32 âe2
                                          (Γe )α β ψ c i β W Wâ d ∇e Wb̂dα i −
1                                          1
16
   (Γâ )α β ψ c i β W W d e ∇e Wb̂dα i + 16 (Γe )α β ψ c i β W Wâd ∇d Wb̂eα i +
1 e2                                                    1 e2 e3 dee1
8
  ǫ âe3 de1 (Σe2 e )α β ψ c i β W Wde ∇e3 Wb̂e1 α i + 32 ǫ          (Σe2 e3 )α β ψ c i β W Wde ∇â Wb̂e1 α i +
1                                         1 e2 e3 de
16
   (Γd )α β ψ c i β W Wd e ∇â Wb̂eα i − 32 ǫ                α   c β       e1      i
                                                 â (Σe2 e3 ) β ψ i W Wde ∇ Wb̂e1 α +

1                                        3 e1 e2
16
   (Γd )α β ψ c i β W Wâd ∇e Wb̂eα i + 32 ǫ       de        α   c β       e3   i
                                                 e3 (Σe1 e2 ) β ψ i Fâb̂ ∇ Wdeα −

3                                     3 e1 e2
16
   (Γd )α β ψ c i β Fâb̂ ∇e Wdeα i + 32 ǫ      de        α   c β     e3     i
                                              e3 (Σe1 e2 ) β ψ i Fde ∇ Wâb̂α −

3
16
   (Γd )α β ψ c i β Fde ∇e Wâb̂α i − 83 ǫe1 e2 âde3 (Σe1 e2 )α β ψ c i β F de ∇e3 Wb̂eα i −
3
8
  (Γd )α β ψ c i β Fd e ∇â Wb̂eα i − 83 (Γâ )α β ψ c i β F d e ∇e Wb̂dα i + 32
                                                                               3 e1 e2
                                                                                 ǫ                     α   c β de e3  i
                                                                                       âb̂e3 (Σe1 e2 ) β ψ i F ∇ Wdeα −

                                                         219
```

</details>

<a id="src-c24-p319"></a>

<details>
<summary>C24-p319 — PDF page 319: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p319: PDF page 319](https://arxiv.org/pdf/2311.00679v1#page=319) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3                                       3
16
   (Γâ )α β ψ c i β F de ∇b̂ Wdeα i − 32 ǫâb̂ dee1 ψ c i α Fde ∇e2 We1 e2 α i +
3
  ǫ dee1 (Σe2 e3 )α β ψ c i β Fde ∇e3 We1 e2 α i − 83 (Γe )α β ψ c i β Fâ d ∇e Wb̂dα i −
16 âb̂

3
  ǫ dee1 ψ c i α Fb̂d ∇e2 Wee1 α i − 83 ǫe2 â dee1 (Σe2 e3 )α β ψ c i β Fb̂d ∇e3 Wee1 α i +
16 âe2

3 e1 e2   de        α   c β      e3    i 3    e α   c β      d     i
8
  ǫ     e3 (Σe1 e2 ) β ψ i Fâd ∇ Wb̂eα + 8 (Γ ) β ψ i Fâd ∇ Wb̂eα −

3
8
  (Γd )α β ψ c i β Fâd ∇e Wb̂eα i + 83 ǫe1 e2 âe3 e (Σe1 e2 )α β ψ c i β Fb̂ d ∇e3 Wedα i −
3
8
  (Γe )α β ψ c i β Fb̂ d ∇â Wedα i − 38 (Γâ )α β ψ c i β Fb̂ d ∇e Wdeα i + 18 ǫe1 e2 e3 de (Σe1 e2 )α β ψ c i β Wâb̂α i ∇e3 Fde −
1
4
  (Γd )α β ψ c i β Wâb̂α i ∇e Fde + 81 ǫâb̂e3 e1 e2 (Σde )α β ψ c i β We1 e2 α i ∇e3 F de +
1
2
  (Γâ )α β ψ c i β Wedα i ∇e Fb̂ d − 14 (Γd )α β ψ c i β Wdeα i ∇e Fâb̂ − 14 (Γâ )α β ψ c i β Wdeα i ∇b̂ F de −
1
2
  (Γe )α β ψ c i β Wedα i ∇â Fb̂ d − 14 ǫâb̂e e1 e2 (Σe3 d )α β ψ c i β We1 e2 α i ∇e3 F de +
1 e3
4
  ǫ âb̂ e1 e2 (Σe3 d )α β ψ c i β We1 e2 α i ∇e F de − 12 (Γe )α β ψ c i β Wb̂dα i ∇e Fâ d +
1 e2 dee1
2
  ǫ â    (Σe2 e3 )α β ψ c i β Wb̂e1 α i ∇e3 Fde + 12 ǫe1 e2 e3 de (Σe1 e2 )α β ψ c i β Wb̂eα i ∇e3 Fâd +
1
2
  (Γe )α β ψ c i β Wb̂eα i ∇d Fâd − 21 (Γd )α β ψ c i β Wb̂eα i ∇e Fâd + 12 ǫe1 e2 âe3 d (Σe1 e2 )α β ψ c i β Wb̂eα i ∇e3 F de −
1
2
  (Γd )α β ψ c i β Wb̂eα i ∇â F de + 12 (Γâ )α β ψ c i β Wb̂eα i ∇d F de − 18 ǫâb̂ dee1 ψ c i α We1 e2 α i ∇e2 Fde +
1
  ǫ dee1 ψ c i α Wee1 α i ∇e2 Fb̂d − 21 (Γd )α β ψ c i β Xαi ∇â Fb̂d + 12 (Γâ )α β ψ c i β Xαi ∇d Fb̂d +
4 âe2

                                     1
1
  iǫ
24 âb̂e1 de
             ψ c j α λiα ∇e1 Φdeij + 12 i(Γd )α β ψ c j β λiα ∇d Φâb̂ ij − 12 i(Γâ )α β ψ c j β λiα ∇d Φb̂ dij −
1 e1                                               1 e1 e2
6
  iǫ âb̂e2 e (Σe1 d )α β ψ c j β λiα ∇e2 Φdeij − 12 iǫ                  α   c β
                                                           âde (Σe1 e2 ) β ψ j λiα ∇b̂ Φ
                                                                                         deij
                                                                                              +
1
6
  i(Γd )α β ψ c j β λiα ∇â Φb̂ dij − 61 iǫe1 âb̂de (Σe1 e2 )α β ψ c j β λiα ∇e2 Φdeij −
1 ee1                                             1
3
  iǫ âe2 d (Σee1 )α β ψ c j β λiα ∇e2 Φb̂ dij − 64 iǫâb̂e2 de (Γe1 )α β ψ c i β λiα ∇e2 ∇e1 Wde −
1
4
  i(Σde )α β ψ c i β λiα ∇d ∇e Wâb̂ − 14 iψ c i α λiα ∇d ∇â Wb̂d + 21 i(Σâe )α β ψ c i β λiα ∇d ∇e Wb̂d +
1
2
  i(Σed )α β ψ c i β λiα ∇e ∇â W d b̂ + 14 i(Σâe )α β ψ c i β λiα ∇e ∇d Wb̂d +
3                                       5
8
  i(Σâb̂ )α β ψ c i β λiα ∇d ∇e Wde − 64 iǫâb̂e1 e2 d (Γe )α β ψ c i β λiα ∇e1 ∇e2 Wde +
1
  iǫ
64 âb̂e1 e2
             d
               (Γe1 )α β ψ c i β λiα ∇e2 ∇e Wde − 14 i(Σde )α β ψ c i β λiα ∇â ∇b̂ W de −
1
4
  i(Σâd )α β ψ c i β λiα ∇b̂ ∇e W de − 18 iψ c i α λiα ∇â ∇d Wb̂d − 21 i(Σed )α β ψ c i β λiα ∇â ∇e W d b̂ −
1                                       1
2
  i(Σâd )α β ψ c i β λiα ∇e ∇b̂ W de + 16 iǫâb̂e2 de (Γe1 )α β ψ c i β λiα ∇e1 ∇e2 Wde +
3           d                                      5
  iǫ
32 âee1 e2
              (Γe )α β ψ c i β λiα ∇e1 ∇e2 Wb̂d + 64 iǫâb̂e1 e2 d (Γe1 )α β ψ c i β λiα ∇e ∇e2 Wde −

                                                          220
```

</details>

<a id="src-c24-p320"></a>

<details>
<summary>C24-p320 — PDF page 320: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p320: PDF page 320](https://arxiv.org/pdf/2311.00679v1#page=320) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3
  iǫ
32 âe1 e2
           de
              (Γe1 )α β ψ c i β λiα ∇e2 ∇b̂ Wde + 81 iΦdei j (Σâb̂ )α β ψ c j β W de λiα +
1                                         1 e1 e2
24
   iΦâb̂i j (Σde )α β ψ c j β W de λiα + 48 iǫ       d        j  e α   c β     i
                                                  âb̂ Φe1 e2 i (Γ ) β ψ j Wde λα +

1 e2
24
   iǫ b̂e1 de Φâe2 i j (Γe1 )α β ψ c j β Wde λiα + 16 iΦâdi j (Σb̂e )α β ψ c j β W de λiα +
1
  ǫ
4 âb̂e1
           φ i Wde ∇e1 λiα −(Γd )α β φc i β Wâb̂ ∇d λiα + 23 (Γâ )α β φc i β Wb̂d ∇d λiα −
         de c α

13 e1                                         13 e1 e2 de                         i
8
  ǫ âb̂e2 d (Σe1 e )α β φc i β Wde ∇e2 λiα + 16 ǫ                α   c β
                                                      â (Σe1 e2 ) β φ i Wde ∇b̂ λα +

7                                 5
4
  (Γd )α β φc i β Wb̂d ∇â λiα + 16 (Σde )α β φc i β W de Wâb̂ λiα − 27
                                                                       8
                                                                         (Σâd )α β φc i β W de Wb̂e λiα +
15
32
   (Σâb̂ )α β φc i β W de Wde λiα + 12 ǫâb̂ dee1 (Γe2 )α β φc i β Wde We1 e2 λiα −
5
  ǫ dee1 (Γe2 )α β φc i β Wb̂d Wee1 λiα − 58 (Σde )α β φc i β Wâd Wb̂e λiα −
32 âe2

   ǫ âb̂ de (Σe1 e2 )α β φc i β Wde ∇e2 λiα + 17
13 e1
16                                              8
                                                  ǫee1 âe2 d (Σee1 )α β φc i β Wb̂d ∇e2 λiα +
9
8
  i(Σde )α β φc i β W W de Wâb̂α i + 11
                                      2
                                         iφc i α Fâ d Wb̂dα i − 43 Φâb̂i j φc j α λiα +
3 ee1
8
  ǫ âb̂d Φee1 i j (Γd )α β φc j β λiα +3Φâ d i j (Σb̂d )α β φc j β λiα − 38 (Γd )α β φc i β λiα ∇d Wâb̂ +
9         de c α i           15 e1
  ǫ
16 âb̂e1
            φ i λα ∇e1 Wde − 32 ǫ âb̂ de (Σe1 e2 )α β φc i β λiα ∇e2 Wde +
9 ee1
16
   ǫ âe2 d (Σee1 )α β φc i β λiα ∇e2 Wb̂d + 43 (Γd )α β φc i β λiα ∇â Wb̂d +
15                                21 e1
8
   (Γâ )α β φc i β λiα ∇d Wb̂d + 16 ǫ âb̂e2 e (Σe1 d )α β φc i β λiα ∇e2 W de +
21 e1 e2 de         α   c β i                    α   c β    d i
32
   ǫ    â (Σe1 e2 ) β φ i λα ∇b̂ Wde + 2(Σâb̂ ) β φ i ∇d ∇ λα −

2φc i α ∇â ∇b̂ λiα +4(Σâd )α β φc i β ∇d ∇b̂ λiα + 41 i(Γd )α β φc i β Wâb̂α i ∇d W +
1
  iǫ
8 âb̂e1
           φ i Wdeα i ∇e1 W − 41 iǫe1 âb̂ de (Σe1 e2 )α β φc i β Wdeα i ∇e2 W −
         de c α

1 ee1
2
  iǫ âe2 d (Σee1 )α β φc i β Wb̂dα i ∇e2 W + 21 i(Γd )α β φc i β Wb̂dα i ∇â W −
1
2
  i(Γâ )α β φc i β Wb̂dα i ∇d W + 41 i(Γd )α β φc i β W ∇d Wâb̂α i + 18 iǫâb̂e1 de φc i α W ∇e1 Wdeα i −
1 e1
4
  iǫ âb̂ de (Σe1 e2 )α β φc i β W ∇e2 Wdeα i − 21 iǫee1 âe2 d (Σee1 )α β φc i β W ∇e2 Wb̂dα i +
1
2
  i(Γd )α β φc i β W ∇â Wb̂dα i − 21 i(Γâ )α β φc i β W ∇d Wb̂dα i −8∇â Fb̂ d f c d −

8∇d Fâd f c b̂ − 2∇d Fâb̂ f c d

                                                         221
```

</details>

<a id="src-c24-p321"></a>

<details>
<summary>C24-p321 — PDF page 321: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p321: PDF page 321](https://arxiv.org/pdf/2311.00679v1#page=321) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.2.8     ✷2 W

                                          3 cd ab
Da ∇a ∇b ∇b W − 12 iψai α ∇a ∇b ∇b λiα + 32 iǫ e (Σcd )α β ψe1 i β λiα ∇e1 ∇e Wab −
 9                                 13 cd ab
32
   i(Γa )α β ψci β λiα ∇c ∇b Wab + 128 iǫ e (Σcd )α β ψe1 i β ∇e Wab ∇e1 λiα −
11                                 9 cdab
32
   i(Γa )α β ψci β ∇b Wab ∇c λiα + 64 iǫ          α       β e1    e i
                                          e (Σcd ) β ψe1 i ∇ Wab ∇ λα −

3
8
  i(Γa )α β ψci β ∇c Wab ∇b λiα + 18 iǫcd e ab (Σcd )α β ψe1 i β Wab ∇e1 ∇e λiα −
1
2
  i(Γa )α β ψci β Wab ∇c ∇b λiα + 18 (Γa )α β ψbi β Xαi ∇b ∇a W + 64
                                                                  3
                                                                     iψci α Wab λiα ∇c W ab +
 57                                            3
    iǫ cdab (Γe )α β ψe1 i β Wab λiα ∇e1 Wcd + 16
2048 e
                                                  i(Σa c )α β ψdi β Wab λiα ∇d W cb+
 11
128
    iψci α W ab Wab ∇c λiα − 18 i(Σab )α β ψcj β λiα ∇c Φabij + 24
                                                                 1
                                                                   iΦab i j (Σab )α β ψcj β ∇c λiα +
 1                        1                            15
   ψ α W Wabα i ∇c W ab + 32
32 ci
                             ψci α W W ab ∇c Wabα i + 128 ψci α W ab Wabα i ∇c W +

   iǫ e (Σcd )α β ψ e i β Wab ∇e1 ∇e1 λiα − 41 i(Γa )α β ψ b i β Wab ∇c ∇c λiα +
 1 cd ab
16

 3                           9
16
   iψci α Wab λiα ∇a W cb + 512 iǫee1 cda (Γe )α β ψ e1 i β Wab λiα ∇b Wcd −
 3
16
   i(Σa c )α β ψdi β Wab λiα ∇b W cd + 83 i(Σdc )α β ψ d i β Wab λiα ∇a W cb +
 9                                       3
64
   i(Σab )α β ψ c i β W ab λiα ∇d Wcd − 16 i(Σcd )α β ψ c i β Wab λiα ∇d W ab −
 9                                       15
32
   i(Σa d )α β ψ d i β Wab λiα ∇c W cb + 512 iǫee1 cab (Γd )α β ψ e i β Wab λiα ∇e1 Wcd −
 3                                       27                             15
64
   i(Σcd )α β ψ a i β Wab λiα ∇b W cd + 128 iψ a i α Wab λiα ∇c W cb + 1024 iǫee1 cda (Γe )α β ψ b i β Wab λiα ∇e1 Wcd +
 9                                        3
64
   i(Σa c )α β ψ b i β Wab λiα ∇d W cd − 32 i(Σdc )α β ψ a i β Wab λiα ∇d W cb −
 1                                             1
   iǫ abcd (Γe )α β ψe1 i β Wab Wcd ∇e1 λiα + 64
128 e
                                                 i(Σc a )α β ψdi β W ab Wcb ∇d λiα +
 1                              1
16
   iψ b i α W a b Wac ∇c λiα + 128 iǫee1 abc (Γe )α β ψ e1 i β Wab Wcd ∇d λiα +
1
8
  i(Σac )α β ψ b i β Wab Wcd ∇d λiα − 38 i(Σda )α β ψ d i β W ab Wbc ∇c λiα −
5
8
  i(Σad )α β ψ c i β W ab Wcb ∇d λiα + 18 i(Σab )α β ψ c i β W ab Wcd ∇d λiα +
 1                                       11
32
   i(Σcd )α β ψ c i β W ab Wab ∇d λiα + 128 iǫee1 abc (Γd )α β ψ e i β Wab Wcd ∇e1 λiα +
 3                                            9
   iǫ abc (Γe )α β ψ d i β Wab Wcd ∇e1 λiα + 512
128 ee1
                                                 iǫe1 cdab (Γe )α β ψ e i β Wab λiα ∇e1 Wcd −
 9         a                                     3
   iǫ
512 dee1 c
             (Γd )α β ψ e i β Wab λiα ∇e1 W cb− 16 i(Σa d )α β ψci β Wab λiα ∇d W cb+
 15                                             3
    iǫ abcd (Γe )α β ψ e1 i β Wab Wcd ∇e λiα + 256
256 e1
                                                   iǫe1 abcd (Γe )α β ψ e i β Wab Wcd ∇e1 λiα −

                                                        222
```

</details>

<a id="src-c24-p322"></a>

<details>
<summary>C24-p322 — PDF page 322: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p322: PDF page 322](https://arxiv.org/pdf/2311.00679v1#page=322) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 9                                                      9
256
    iǫee1 e2 cd (Σee1 )α β ψ e2 i β W ab Wcd Wab λiα + 512 i(Γc )α β ψ d i β W ab Wcd Wab λiα +
 27                                                  9
    iǫ cdee1 (Σab )α β ψ e2 i β W ab Wcd Wee1 λiα − 512
512 e2
                                                        iǫabcde ψ e1 i α Wab Wcd Wee1 λiα −
 9                                      27 e2 abcd
64
   i(Γc )α β ψ d i β W ab Wca Wdb λiα + 256 iǫ     (Σe2 e )α β ψ e1 i β Wab Wcd Wee1 λiα −
 27 abcde                                           1
256
    iǫ    (Σe1 e2 )α β ψ e2 i β Wab Wcd Wee1 λiα − 32 iΦabi j (Γc )α β ψ c j β W ab λiα −
 1 cd ab                          9
64
   iǫ e Φcdi j ψ e j α Wab λiα + 128 iǫcdeab Φcdi j (Σee1 )α β ψ e1 j β Wab λiα +
15 cde                                            5
64
   iǫ e1 a Φc b i j (Σde )α β ψ e1 j β Wab λiα − 32 iΦc a i j (Γc )α β ψ b j β Wab λiα +
 5                                       1
16
   iΦb ci j (Γa )α β ψ c j β Wab λiα − 1024 ǫee1 e2 cd (Σee1 )α β ψ e2 i β W W ab Wcd Wabα i +
 3                                         1
512
    (Γc )α β ψ d i β W W ab Wcd Wabα i − 1024 ǫe2 cdee1 (Σab )α β ψ e2 i β W W ab Wcd Wee1 α i −
  1                                        1
1024
     ǫabcee1 ψ d i α W Wab Wcd Wee1 α i + 512 (Γc )α β ψ d i β W W ab Wab Wcdα i +
 3                                        1
256
    (Γd )α β ψ c i β W W ab Wca Wdbα i − 128 (Γc )α β ψ d i β W W ab Wca Wdbα i −
 1 e2 abee1                                           1 abcee1
256
    ǫ       (Σe2 c )α β ψ d i β W Wab Wcd Wee1 α i + 256 ǫ     (Σd e2 )α β ψ e2 i β W Wab Wcd Wee1 α i −
 1                                          1
256
    (Γd )α β ψ d i β W W ab W c a Wcbα i + 256 ǫe1 abce ψ e1 i α W Wab Wc d Wedα i −
 3 e1 abce                                            3 ee1
512
    ǫ      (Σe1 e2 )α β ψ e2 i β W Wab Wc d Wedα i + 512 ǫ e2 cd (Σee1 )α β ψ e2 i β W W ab Wca Wdbα i −
 3 ee1                                                3
512
    ǫ e2 ac (Σee1 )α β ψ e2 i β W Wa b Wc d Wbdα i − 256 (Γa )α β ψ d i β W Wa b W c d Wbcα i +
  3                                             69
    iǫ cdab (Γe )α β ψ e1 i β Wab λiα ∇e Wcd + 1024
2048 e1
                                                    iǫee1 cda (Γb )α β ψ e i β Wab λiα ∇e1 Wcd +
 15                                           1 cde
    iǫ cab (Γe )α β ψ d i β Wab λiα ∇e1 Wcd + 64
512 ee1
                                                 iǫ e1 a Φcdi j (Σe b )α β ψ e1 j β Wab λiα −
 1                                                 1 e1
128
    iǫcee1 ab Φcdi j (Σee1 )α β ψ d j β Wab λiα − 256 ǫ e2 ace (Σe1 b )α β ψ e2 i β W Wab Wc d Wedα i −
  1                                                       1
1024
     ǫe1 e2 abc (Σe1 e2 )α β ψ e i β W Wab Wc d Wdeα i + 1024 ǫe1 e2 abe (Σe1 e2 )α β ψ d i β W Wab W c d Wecα i −
3
8
  (Γa )α β ψ a i β Xαi ∇b ∇b W − 41 iΦabi j ψ a j α ∇b λiα − 24
                                                              1 bc
                                                                iǫ ade Φbci j (Γa )α β ψ d j β ∇e λiα +
1
2
  iΦa bi j (Σac )α β ψ b j β ∇c λiα + 16 iΦa bi j (Σac )α β ψ c j β ∇b λiα − 32
                                                                              3 ce
                                                                                iǫ e1 ab Φc d i j (Σed )α β ψ e1 j β Wab λiα +
 3 cdee1 a
64
   iǫ      Φcdi j (Σee1 )α β ψ b j β Wab λiα − 18 i(Γc )α β ψ a i β ∇c Wab ∇b λiα −
 1                                  1 c ab
   iǫ ab e ψ c i α ∇d Wab ∇e λiα + 64
16 cd
                                      iǫ e e1 (Σcd )α β ψ e i β ∇d Wab ∇e1 λiα +
 3 cd a                                        3
64
   iǫ e e1 (Σcd )α β ψ b i β ∇e Wab ∇e1 λiα + 16 i(Γc )α β ψ a i β ∇b Wab ∇c λiα −
1                                    1 cd
8
  i(Γa )α β ψ b i β ∇c Wab ∇c λiα + 16 iǫ ee1 a (Σcd )α β ψ e i β ∇e1 Wab ∇b λiα −
 1                                    1 c
16
   i(Γc )α β ψ c i β ∇a Wab ∇b λiα − 16 iǫ ee1 ab (Σcd )α β ψ e i β ∇e1 Wab ∇d λiα +

                                                          223
```

</details>

<a id="src-c24-p323"></a>

<details>
<summary>C24-p323 — PDF page 323: Supplement5.2: full degauged higher vector derivatives</summary>

[C24-p323: PDF page 323](https://arxiv.org/pdf/2311.00679v1#page=323) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
 3 cd a                                        27
64
   iǫ e e1 (Σcd )α β ψ e i β ∇b Wab ∇e1 λiα + 1024 iǫee1 cab (Γe )α β ψ e1 i β Wab λiα ∇d Wcd +
 5                                                5 c ab
128
    iǫcd e ab (Σcd )α β ψ e i β ∇e1 Wab ∇e1 λiα + 64 iǫ e e1 (Σcd )α β ψ d i β ∇e Wab ∇e1 λiα +
 1 cd ab                                    1
48
   ǫ e (Σcd )α β ψe1 i β ∇e W ∇e1 Wabα i − 12 ǫcde ab ψ c i α ∇d W ∇e Wabα i −
 1 c                                            1 cd
24
   ǫ ee1 ab (Σcd )α β ψ e i β ∇d W ∇e1 Wabα i + 12 ǫ ee1 a (Σcd )α β ψ b i β ∇e W ∇e1 Wabα i +
 1 cd
24
   ǫ ee1 a (Σcd )α β ψ e i β ∇e1 W ∇b Wabα i + 61 (Γc )α β ψ c i β ∇a W ∇b Wabα i −
 1 cd ab                                   1 c
48
   ǫ e (Σcd )α β ψe1 i β ∇e1 W ∇e Wabα i + 24 ǫ ee1 ab (Σcd )α β ψ e i β ∇e1 W ∇d Wabα i −
 1 cd                                           1
24
   ǫ ee1 a (Σcd )α β ψ e i β ∇b W ∇e1 Wabα i + 384 ǫe1 abcd (Γe )α β ψ e1 i β Wab Wcdα i ∇e W −
 7                                       11 c α
192
    (Σcd )α β ψ c i β W ab Wabα i ∇d W − 64 ψ i W a b Wacα i ∇b W − 11
                                                                    96
                                                                       (Σad )α β ψ c i β W ab Wcbα i ∇d W −
11                                      1
96
   (Σac )α β ψ d i β Wab Wcdα i ∇b W − 192 (Σab )α β ψ c i β W ab Wcdα i ∇d W −
 5                                     7
32
   (Σc a )α β ψdi β W ab Wcbα i ∇d W + 96 (Σc d )α β ψ d i β W a b Wcaα i ∇b W −
19                                       1
96
   (Σda )α β ψ d i β W ab Wbcα i ∇c W + 192 ǫee1 abc (Γd )α β ψ e i β Wab Wcdα i ∇e1 W +
 19                                            7
    ǫ abc (Γe )α β ψ e1 i β Wab Wcdα i ∇d W − 192
384 ee1
                                                  (Σcd )α β ψ a i β Wab Wcdα i ∇b W −
19                                      1
96
   (Σac )α β ψ b i β Wab Wcdα i ∇d W − 192 ǫee1 acd (Γe )α β ψ b i β Wab Wcdα i ∇e1 W −
11 b α                      7                                         3
64
   ψ i W a b Wacα i ∇c W − 96 (Σc d )α β ψ b i β W a b Wcaα i ∇d W + 128 ǫee1 acd (Γb )α β ψ e i β Wab Wcdα i ∇e1 W +
 3                                           13
   ǫ abc (Γe )α β ψ d i β Wab Wcdα i ∇e1 W + 768
128 ee1
                                                 ǫe abcd (Γe )α β ψe1 i β Wab Wcdα i ∇e1 W +

(Γa )α β φbi β ∇b ∇a λiα + 21
                           16
                              (Σab )α β φci β λiα ∇c W ab + 11
                                                             8
                                                               (Σab )α β φci β W ab ∇c λiα +
1                              9 a α i            3
2
  (Γa )α β φa i β ∇b ∇b λiα − 32 φ i λα ∇b Wab + 32 ǫcde ab (Γc )α β φd i β λiα ∇e Wab +
3                                9
8
  (Σca )α β φbi β λiα ∇c W ab − 16 (Σca )α β φc i β λiα ∇b W ab − 34 φa i α Wab ∇b λiα +
1                                                                  9
  ǫ ab (Γc )α β φd i β Wab ∇e λiα +(Σa c )α β φc i β Wab ∇b λiα − 128
8 cde
                                                                      (Γc )α β φc i β W ab Wab λiα +
 9 eabcd                                   1 abcd
128
    ǫ    (Σee1 )α β φe1 i β Wab Wcd λiα − 16 ǫ          j      α   e β i
                                                  e Φabi (Σcd ) β φ j λα +

1                            1                                    1
  Φ j (Γa )α β φb j β λiα + 128
8 abi
                                i(Γc )α β φc i β W W ab Wabα i + 256 iǫe abcd φe i α W Wab Wcdα i −
 1                                             1 de
128
    iǫeabcd (Σee1 )α β φe1 i β W Wab Wcdα i − 64 iǫ e1 ac (Σde )α β φe1 i β W Wa b Wcbα i −
 1                                   1                                   9
64
   i(Γa )α β φc i β W Wa b Wbcα i + 64 i(Γc )α β φb i β W W a b Wcaα i + 32 (Γa )α β φc i β Wa b Wbc λiα −
 9 e                                          9 ee1 abc
64
   ǫ e1 abc (Σe d )α β φe1 i β Wab Wcd λiα + 128 ǫ      (Σee1 )α β φd i β Wab Wcd λiα +
1 a α
4
  iφ i Wabα i ∇b W + 2∇a ∇b W fab − 6∇a ∇a W f b b

                                                        224
```

</details>

<a id="src-c24-p324"></a>

<details>
<summary>C24-p324 — PDF page 324: Supplement5.2: full degauged higher vector derivatives; Supplement5.3: full degauged higher linear derivatives</summary>

[C24-p324: PDF page 324](https://arxiv.org/pdf/2311.00679v1#page=324) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.3     Linear Multiplet

5.3.1    ∇a ∇b Gij

  Da ∇b Gij +ψaj α ∇b ϕiα − 18 ǫee1 b cd (Σee1 )α β ψaj β Wcd ϕiα − 12 (Γc )α β ψaj β Wbc ϕiα −
  3
    G (Γb )α β ψak β Xαk − 83 Gik (Γb )α β ψaj β Xαk + 38 Gi k (Γb )α β ψak β Xjα +
  8 ij

  i(Γb )α β φaj β ϕiα − 6Gij fab

5.3.2    ∇a ∇b ϕiα

  D a ∇b ϕiα + 14 iψ ai α ∇b F − 41 i(Γc )αβ ψ aiβ ∇b Hc + 12 i(Γc )αβ ψ a j β ∇b ∇c Gij −
  1 bee1 cd
  32
     iǫ     F (Σee1 )αβ ψ aiβ Wcd + 81 iF (Γc )αβ ψ aiβ Wc b − 16
                                                                1
                                                                  iHb (Σcd )αβ ψ aiβ W cd+
                               1 be1 cd
  1
  8
    iHc (Σb d )αβ ψ aiβ W cd− 32 iǫ e He1 (Γe )αβ ψ aiβ Wcd − 18 iHc ψ ai α W bc +
  1
  4
    iHd (Σdc )αβ ψ aiβ W bc + 18 i(Σcd )αβ ψ a j β W cd ∇b Gij + 21 i(Σcd )αβ ψ a j β W bc ∇d Gij −
  1 b
  16
     iǫ ee1 cd (Γe )αβ ψ a j β Wcd ∇e1 Gij + 41 iψ a jαW b c ∇c Gij + 14 i(Σbc )αβ ψ a j β Wcd ∇d Gij −
  1 bee1 cd
  8
    ǫ       (Σee1 )αρ ψ a j ρ Wcd βj ϕiβ + 41 (Γc )αρ ψ a j ρ Wc bβj ϕiβ + 16
                                                                           1 bee1 cd
                                                                              ǫ      (Σee1 )α ρ ψ a j β Wcdβ j ϕiρ −
  1
  16
     (Γb )α β ψ a j ρ Xβj ϕiρ + 16
                                1
                                   (Γb )βρ ψ a jα Xβj ϕiρ − 16
                                                             1
                                                               (Γb )αρ ψ a j ρ X jβ ϕiβ −
  1
  16
                                 7
     (Γb )β ρ ψ a j ρ Xαj ϕiβ − 16 (Γb )β ρ ψ a j ρ Xβj ϕiα + 16
                                                              3
                                                                 (Γb )β ρ ψ aiρ Xjβ ϕjα +
  3
  16
     (Γb )β ρ ψ a j ρ Xβi ϕjα + 81 iǫbcdee1 Φcdj k Gij (Σee1 )αβ ψ a k β − 34 iΦc b j k Gij (Γc )αβ ψ a k β +
  3
  8
    iGij (Σcd )αβ ψ a j β ∇b W cd − 43 iGij (Σdc )αβ ψ a j β ∇d W bc − 16
                                                                        3 b
                                                                          iǫ ee1 cd Gij (Γe )αβ ψ a j β ∇e1 Wcd +
  9
  16
     iGij ψ a jα ∇c W bc + 83 iGij (Σb c )αβ ψ a j β ∇d W cd − 64
                                                                9
                                                                  iGij (Γb )αβ ψ a j β W cdWcd +
  9 bcdee1 ij a             3 e2 cdee1 ij
  64
     iǫ   G ψ jαWcd Wee1 − 32 iǫ      G (Σe2 b )αβ ψ a j β Wcd Wee1 +
  3
  4
    iGij (Γd )αβ ψ a j β W bc Wdc − 83 iǫbe2 cde Gij (Σe2 e1 )αβ ψ a j β Wcd Wee1 −
  3 e1 e2 cde ij
  16
     iǫ      G (Σe1 e2 )αβ ψ a j β Wcd We b + 27 φa jα ∇b Gij − 14 F (Γb )αβ φaiβ −
  1 b ai
  4
    H φ α − 21 Hc (Σb c )αβ φaiβ +(Σb c )αβ φa j β ∇c Gij − 43 Gij (Γc )αβ φa j β Wc b −

  7ϕiα f ab + 2(Σb c )α β ϕiβ f ac

                                                          225
```

</details>

<a id="src-c24-p325"></a>

<details>
<summary>C24-p325 — PDF page 325: Supplement5.3: full degauged higher linear derivatives</summary>

[C24-p325: PDF page 325](https://arxiv.org/pdf/2311.00679v1#page=325) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.3.3    ∇a ∇b F

  D a ∇b F − (Γc )α β ψ a i β ∇b ∇c ϕiα − 98 (Σcd )α β ψ a i β ∇b W cdϕiα −

  (Σcd )α β ψ a i β W cd∇b ϕiα + 34 ψ a j α Xiα ∇b Gij − 43 Gi j ψ a j α ∇b Xαi −

  (Σcd )α β ψ a i β W bc ∇d ϕiα + 18 ǫb ee1 cd (Γe )α β ψ a i β Wcd ∇e1 ϕiα − 21 ψ a i α W b c ∇c ϕiα −
  1                                3                                   3 bcdee1 a α
  2
    (Σbc )α β ψ a i β Wcd ∇d ϕiα + 64 (Γb )α β ψ a i β W cd Wcd ϕiα − 16 ǫ     ψ i Wcd Wee1 ϕiα +
  15 e2 cdee1                                     3 bee1 cd
  64
     ǫ        (Σe2 b )α β ψ a i β Wcd Wee1 ϕiα + 32 ǫ       Gi j (Σee1 )α β ψ a j β Wcd Xαi −
  3
    G j (Γc )α β ψ a j β Wc b Xαi − 15
  8 i                               16
                                       (Γd )α β ψ a i β W bc Wdc ϕiα + 15
                                                                       32
                                                                          ǫbe2 cde (Σe2 e1 )α β ψ a i β Wcd Wee1 ϕiα +
  15 e1 e2 cde
  64
     ǫ         (Σe1 e2 )α β ψ a i β Wcd We b ϕiα − 21 F (Γb )α β ψ a i β Xαi − 81 ǫbcdee1 Φcdi j (Σee1 )α β ψ a j β ϕiα +
  3
    Φ b j (Γc )α β ψ a j β ϕiα − 38 (Σb c )α β ψ a i β ∇d W cd ϕiα + 16
  4 c i
                                                                      3 b
                                                                        ǫ ee1 cd (Γe )α β ψ a i β ∇e1 Wcd ϕiα −

     ψ i ∇c W bc ϕiα + 43 (Σdc )α β ψ a i β ∇d W bc ϕiα + 4iφa i α ∇b ϕiα +
  9 a α
  16

  2i(Σb c )α β φa i β ∇c ϕiα − 83 iǫbee1 cd (Σee1 )α β φa i β Wcd ϕiα − 34 iGi j (Γb )α β φa j β Xαi −

  8F f ab

5.3.4    ∇a ∇b Hc

                                            3 e1 e2 de        α   a β b     i
  D a ∇b Hc −2(Σcd )α β ψ a i β ∇b ∇d ϕiα + 16 ǫ   c (Σe1 e2 ) β ψ i ∇ Wde ϕα +

  3                                9 e1 e2 de
  4
    (Γd )α β ψ a i β ∇b Wcd ϕiα + 32 ǫ               α   a β     b i
                                          c (Σe1 e2 ) β ψ i Wde ∇ ϕα +

  1
  2
    (Γd )α β ψ a i β Wcd ∇b ϕiα − 14 (Γb )α β ψ a i β Wcd ∇d ϕiα − 18 ǫb ce1 de ψ a i α Wde ∇e1 ϕiα +
  3 e1                                         5 bee1
  8
    ǫ ce2 de (Σe1 b )α β ψ a i β Wde ∇e2 ϕiα + 16 ǫ     d       α   a β     e2 i
                                                      e2 (Σee1 ) β ψ i Wcd ∇ ϕα −

  1
  2
    (Γd )α β ψ a i β Wc b ∇d ϕiα + 38 ǫbe1 e2 c d (Σe1 e2 )α β ψ a i β Wde ∇e ϕiα +
  1
  4
    (Γd )α β δ b c ψ a i β Wde ∇e ϕiα − 12 (Γc )α β ψ a i β W b d ∇d ϕiα + 45 ψ a i α W bd Wcd ϕiα +
  3
  4
    (Σc e )α β ψ a i β W bd Wed ϕiα − 25 (Σcd )α β ψ a i β W de W b e ϕiα −(Σe d )α β ψ a i β W bd Wce ϕiα −
  27
     ǫ dee1 (Γe2 )α β ψ a i β Wde We1 b ϕiα − 14 δ b c ψ a i α W de Wde ϕiα +
  64 ce2

  1
  2
    (Σc b )α β ψ a i β W de Wde ϕiα + 143
                                       64
                                          (Σe1 d )α β δ b c ψ a i β W de We1 e ϕiα +

                                                          226
```

</details>

<a id="src-c24-p326"></a>

<details>
<summary>C24-p326 — PDF page 326: Supplement5.3: full degauged higher linear derivatives</summary>

[C24-p326: PDF page 326](https://arxiv.org/pdf/2311.00679v1#page=326) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
3                                    19
8
  (Σb d )α β ψ a i β W de Wce ϕiα + 256 ǫe3 dee1 e2 (Γe3 )α β δ b c ψ a i β Wde We1 e2 ϕiα −
9 b                                           5
32
   ǫ e2 dee1 (Γe2 )α β ψ a i β Wcd Wee1 ϕiα + 16 (Σde )α β ψ a i β W de Wc b ϕiα −
21                                              19 bdee1 e2
   ǫ dee1 e2 (Γb )α β ψ a i β Wde We1 e2 ϕiα − 128
256 c
                                                   ǫ        (Γc )α β ψ a i β Wde We1 e2 ϕiα +
1 be1 e2 de
32
   ǫ        (Σe1 e2 )α β ψ a i β Wde ∇c ϕiα + 18 ǫbe1 ce2 d (Σe1 e )α β ψ a i β Wde ∇e2 ϕiα −
1 e1 e2   de        α b     a β     e3 i   5 b dee1
16
   ǫ    e3 (Σe1 e2 ) β δ c ψ i Wde ∇ ϕα − 32 ǫ c    (Γe2 )α β ψ a i β Wde We1 e2 ϕiα −
1 be1 de                                   1 ee1
16
   ǫ c (Σe1 e2 )α β ψ a i β Wde ∇e2 ϕiα − 16 ǫ ce2 d (Σee1 )α β ψ a i β Wd b ∇e2 ϕiα −
1 be1 e2 de
16
   ǫ        Hc (Σe1 e2 )α β ψ a i β Wdeα i + 18 Hc (Γd )α β ψ a i β Wd b α i −
1 d
8
  H (Γb )α β ψ a i β Wcdα i + 18 ǫe1 e2 c de He1 (Σe2 b )α β ψ a i β Wdeα i +
1 bee1 e2 d
8
  ǫ         He (Σe1 e2 )α β ψ a i β Wcdα i + 81 Hb (Γd )α β ψ a i β Wcdα i − 18 Hd (Γd )α β ψ a i β Wc b α i +
1 be1 e2 d e         α   a β    i 1 e    d α b     a β    i
8
  ǫ     c H (Σe1 e2 ) β ψ i Wdeα + 8 H (Γ ) β δ c ψ i Wdeα −

1 d                              1 be1 de
8
  H (Γc )α β ψ a i β W b dα i − 16 ǫ c He1 ψ a i α Wdeα i − 18 Hb (Γc )α β ψ a i β Xαi +
1
  H (Γd )α β δ b c ψ a i β Xαi − 21 Hc (Γb )α β ψ a i β Xαi + 13 Φde i j (Σde )α β δ b c ψ a j β ϕiα −
8 d

Φc b i j ψ a j α ϕiα + 16 ǫbee1 cd Φee1 i j (Γd )α β ψ a j β ϕiα − 23 Φc d i j (Σb d )α β ψ a j β ϕiα −

2Φbd i j (Σcd )α β ψ a j β ϕiα + 41 (Γd )α β δ b c ψ a i β ∇e Wde ϕiα + 21 (Γd )α β ψ a i β ∇d W b c ϕiα −
1 b                              1 be1 de
4
  ǫ ce1 de ψ a i α ∇e1 Wde ϕiα + 16 ǫ c (Σe1 e2 )α β ψ a i β ∇e2 Wde ϕiα +
1 bee1   d       α   a β e2    i   1   b α   a β d     i
4
  ǫ    e2 (Σee1 ) β ψ i ∇ Wcd ϕα − 4 (Γ ) β ψ i ∇ Wcd ϕα +

1 ee1
4
  ǫ ce2 d (Σee1 )α β ψ a i β ∇e2 W bd ϕiα − 12 (Γd )α β ψ a i β ∇c W bd ϕiα −
3                                 3 be1
4
  (Γc )α β ψ a i β ∇d W bd ϕiα + 16 ǫ e2 de (Σce1 )α β ψ a i β ∇e2 Wde ϕiα +
1 be1 e2 d         α   a β e     i    3 be1 e2 de
8
  ǫ     c (Σe1 e2 ) β ψ i ∇ Wde ϕα − 16 ǫ         (Σe1 e2 )α β ψ a i β ∇c Wde ϕiα +
5 e1
16
   ǫ ce2 de (Σe1 b )α β ψ a i β ∇e2 Wde ϕiα + 81 ǫbe1 ce2 e (Σe1 d )α β ψ a i β ∇e2 W de ϕiα +

5i(Γc )α β φa i β ∇b ϕiα −iǫbde ce1 (Σde )α β φa i β ∇e1 ϕiα −i(Γd )α β δ b c φa i β ∇d ϕiα −
1
2
  i(Σde )α β δ b c φa i β W de ϕiα + 43 iφa i α Wc b ϕiα − 14 iǫb ce1 de (Γe1 )α β φa i β Wde ϕiα −
1
2
  i(Σbd )α β φa i β Wcd ϕiα +3i(Σcd )α β φa i β W bd ϕiα −8Hc f ab −2Hb f a c +

2Hd δ b c f ad

                                                           227
```

</details>

<a id="src-c24-p327"></a>

<details>
<summary>C24-p327 — PDF page 327: Supplement5.3: full degauged higher linear derivatives</summary>

[C24-p327: PDF page 327](https://arxiv.org/pdf/2311.00679v1#page=327) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.3.5    ∇a ✷Gij

                  3                                    3
  D a ∇b ∇b Gij + 32 Gik (Σbc )α β ψ a j β W bc Xαk − 32 Gi k (Σbc )α β ψ a k β W bc Xjα −
  3
  8
    (Γb )α β ψ a k β Xαk ∇b Gij − 14 Φbc i k (Σbc )α β ψ a k β ϕjα − 16
                                                                      3 de
                                                                        ǫ e1 bc (Σde )α β ψ a j β ∇e1 Wbc ϕiα +
  9                                 9 a α                 3
  16
     (Γb )α β ψ a j β ∇c Wbc ϕiα − 64 ψ j W bc Wbc ϕiα + 32 Gij ψ a k α W bc Wbcα k +

  ψ a j α ∇b ∇b ϕiα − 14 ǫde e1 bc (Σde )α β ψ a j β Wbc ∇e1 ϕiα +(Γb )α β ψ a j β Wbc ∇c ϕiα −
  3
    G (Γb )α β ψ a j β ∇b Xαk + 34 (Γb )α β ψ a j β Xkα ∇b Gi k + 83 Gi k (Γb )α β ψ a k β ∇b Xjα +
  8 ik

  3
  4
    (Γb )α β ψ a k β Xiα ∇b Gj k + 49 i(Σbc )α β φa j β W bc ϕiα + 15
                                                                    8
                                                                      iGik φa j α Xαk −
  15
  8
     iGi k φa k α Xjα + 2i(Γb )α β φa j β ∇b ϕiα − 6∇b Gij f a b

References
[1] G. Gold, J. Hutomo, S. Khandelwal, and G. Tartaglino-Mazzucchelli, “Components of curvature-
    squared invariants of minimal supergravity in five dimensions,” [arXiv:2311.????? [hep-th]]

                                                       228
```

</details>

### G25: cached source equations

Source PDF: 2025-Gold-On five-dimensional curvature squared supergravity and holography.pdf. SHA-256: `9f68932315dc9d72547b36d4fdefcdf8752eb6ff8d8ddeb3619fe6f7a575e8d8`.

<a id="src-g25-p004"></a>

<details>
<summary>G25-p004 — PDF page 4: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p004: PDF page 4](https://arxiv.org/pdf/2504.10856v1#page=4) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
4                                                     Authors Suppressed Due to Excessive Length

based on the off-shell dilaton Weyl multiplet. For the results in components, our
notation and conventions correspond to that of [10]. We denote the spacetime indices
by µ , ν , · · · , Lorentz indices by a, b, · · · , SU(2) indices by i, j, · · · , and spinor indices
by α , β , · · · .

2.1 Standard Weyl

The standard Weyl multiplet of 5D N = 1 conformal supergravity [10] is com-
prised of a set of independent gauge fields: the vielbein eµ a , the gravitino ψµ iα , the
SU(2) gauge fields Vµ i j , and a dilatation gauge field bµ . The other gauge fields as-
sociated with the remaining symmetries, including the spin connection ωµ ab , the
S-supersymmetry connection φµ iα , and the special conformal connection f µ a , are
composite fields, i.e., they are determined in terms of the other fields by imposing
certain curvature constraints. The standard Weyl multiplet also contains a set of mat-
ter fields: a real antisymmetric tensor Tab , a fermion χαi , and a real scalar D. A more
detailed discussion of the superconformal transformations of the various fields can
be found, e.g., in [10, 24].

2.2 Gauged Dilaton-Weyl

Let us consider a variant multiplet of conformal supergravity, known as the gauged
dilaton Weyl multiplet [24].1 This multiplet is obtained by coupling the standard
Weyl multiplet to on-shell vector and linear multiplets. The vector multiplet con-
sists of a scalar field σ , the gaugino ψαi , an abelian gauge vector Cµ with field
strength Gµν = 2∂[µ Cν ] , and an SU(2) triplet of auxiliary fields Y i j = Y (i j) . The
linear multiplet contains an SU(2) triplet of scalars Li j = L(i j) , a gauge three-form
Eµνρ , a scalar N, and an SU(2) doublet ϕαi . In the gauged dilaton Weyl multiplet,
the independent gauge fields remain the same as the standard Weyl, but the matter
content is replaced with {σ ,Cµ , Bµν , Li j , Eµνρ , N, ψ i , ϕ i }. The bosonic matter fields
of the vector and the standard Weyl multiplet are then expressed as follows [24]
                              g
                    Y i j = − σ −1 Li j + f.t. ,
                              2
                            1 −1          1
                    Tab = σ Gab + σ −2 εabcde H cde + f.t. ,
                            8            48

1 Note that the definition of a dilaton Weyl multiplet is not unique. For instance, in five dimensions

a (hyper) dilaton Weyl multiplet based on an on-shell hypermultiplet in the background of the
standard Weyl multiplet was constructed in [45], which might also be used for alternative gaugings.
In this paper we work with the gauged (vector) dilaton Weyl multiplet of [24], see also [13] for its
superspace construction.
```

</details>

<a id="src-g25-p005"></a>

<details>
<summary>G25-p005 — PDF page 5: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p005: PDF page 5](https://arxiv.org/pdf/2504.10856v1#page=5) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
On five-dimensional curvature squared supergravity and holography                       5

                          1 −1 a       1                  1
                    D=      σ ∇ ∇a σ + σ −2 (∇a σ )∇a σ − R
                          4            8                  32
                             1 −2 ab      26 ab        −1 ab
                          − σ G Gab − ( T − 2σ G )Tab
                            16            3
                            g −2    g2 −4 2
                          + σ N + σ L + f.t. ,                                        (1)
                            4       16
where “f.t.” stands for omitted fermionic terms and Habc = ea µ eb ν ec ρ Hµνρ denotes
the three-form field strength Hµνρ := 3∂[µ Bνρ ] + 23 C[µ Gνρ ] + 12 gEµνρ . In the above,
the covariant derivative is denoted by
                                                                 
                    ∇a = ea µ ∂µ − ωµ bc Mbc − bµ D − Vµ i jUi j ,                     (2)

with Mab , D, and Ui j being the Lorentz, dilatation, and SU(2) generators, respec-
tively. The dilatation connection b µ is pure gauge and will be set to zero throughout.
The mapping (1) allows us to easily convert every invariant involving a coupling to
the standard Weyl multiplet to that written in terms of the gauged dilaton Weyl mul-
tiplet. The ungauged map and the models can simply be obtained by setting g = 0
in (1). In this case, the fields of the linear multiplet decouple from the map (1), and
the multiplet reduces to the ungauged dilaton Weyl multiplet with 32 + 32 off-shell
degrees of freedom [10, 29].

2.3 Curvature-squared actions in the gauged dilaton Weyl
    background

2.3.1 BF action

In the superconformal tensor calculus, the so-called BF action principle plays a
fundamental role in the construction of general supergravity-matter couplings, see
[13, 47, 29, 48, 10, 8, 9] for the 5D case. It is based on an appropriate product of a
linear multiplet with an Abelian vector multiplet:

                          e−1 LBF = Aa E a + ρ N + Yi j Li j + f.t. .                 (3)

Here we use {ρ , Aµ , Yi j , λαi } to denote the field content in an arbitrary vector mul-
tiplet, and the bosonic part of the constrained vector Ea is related to the three-form
                                   1
gauge field Eabc via Ea = − 12       εabcde ∇b E cde . Furthermore, in our construction we
consider the case in which the linear multiplet fields Li j , N and Ea are composite
of the vector multiplet. The BF-action thus yields a vector-coupled action in the
(gauged) dilaton Weyl background. Using the off-shell map given in [56], a vector
multiplet can be identified with fields in the gauged dilaton Weyl multiplet as
                      1                g
               Y i j → iσ −1 ψ̄ i ψ j − σ −1 Li j ,                 ρ →σ,
                      4                2
```

</details>

<a id="src-g25-p006"></a>

<details>
<summary>G25-p006 — PDF page 6: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p006: PDF page 6](https://arxiv.org/pdf/2504.10856v1#page=6) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
6                                                 Authors Suppressed Due to Excessive Length

                 Aµ → Cµ ,                                         λ i → ψi ,             (4)

which gives rise to off-shell models that are purely expressed in terms of the fields
of the (gauged) dilaton Weyl multiplet. By appropriately choosing primary com-
posite linear multiplets, eq. (3) becomes the building block for constructing various
curvature-squared invariants.
   Within the superconformal approach, supersymmetric completions of the Weyl
tensor squared and the Ricci scalar squared were constructed for the first time, re-
spectively in [39] and [55]. The third independent invariant necessary to obtain all
the curvature-squared models in five dimensions includes the Ricci tensor-squared
term. In the standard Weyl multiplet background, this invariant was defined in su-
perspace in [13].

2.3.2 Weyl2

As an example, we first consider the composite linear multiplet superfield that is
used to construct the off-shell Weyl tensor squared invariant. It is a composite of the
standard Weyl multiplet superfields, that is
                             i                 3i             3i
          LiWeyl
            j       ij
                 → HWeyl := − W αβ γ iWαβ γ j + W αβ Xαβ i j − X α i Xαj ,                (5)
                             2                 2              4
together with its (bosonic) descendants which are defined by
                                    i α       ij
                           NWeyl =    ∇ ∇α j HWeyl |,                                    (6a)
                                   12 i
                                    i                   ij
                             a
                            EWeyl = (Γ a )αβ ∇α i ∇β j HWeyl |,                          (6b)
                                   12
with ∇iα being the conformal superspace spinor derivative. In the above, the primary
                     ij           a
component fields LWeyl , NWeyl , EWeyl are obtained by bar-projection, which corre-
sponds to setting θ = 0, see [13, 33] for details.
   In deriving the off-shell Weyl-squared invariant, one may start by first substitut-
ing the resulting composite multiplet (5) and (6) into (3). This yields the explicit
form of the invariant written in the standard Weyl basis. Its corresponding form in
the gauged dilaton Weyl background can be obtained by making use of the map (1)
and (4). In this paper, we will only present the bosonic sector of the off-shell Weyl-
squared invariant in the gauged dilaton Weyl background, and upon imposing the
gauge conditions

                           σ =1,         bµ = 0 ,       ψi = 0 .                          (7)

The action is given by
                   1                           1                        2
    e−1 LWeyl 2 = − ε abcdeCa Rbc f g Rde f g + ε abcdeCaVbc i jVdei j + V abi jVabi j
                   8                           6                        3
```

</details>

<a id="src-g25-p007"></a>

<details>
<summary>G25-p007 — PDF page 7: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p007: PDF page 7](https://arxiv.org/pdf/2504.10856v1#page=7) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
On five-dimensional curvature squared supergravity and holography                             7

                    1                1             1
                  − Rabcd Rabcd + Rab Rab − R2
                    4                3            12
                    1
                  + Rabcd (G G − 2H H − 3H abGcd )
                               ab cd         ab cd
                    3
                    4                16         2    1              4
                  − Rab H ac Gb c + Rab Hab       + RHab Gab − RH 2 − 4(H 2 )2
                    3                 3              3              3
                       4    16 2         cd    40 2 a cd 8 2 2
                  − 8H − H Hcd G − Had H c G + H G
                             3                 3                  3
                    2           ab cd       1 2 2
                  + Hab Hcd G G + (G )
                    3                      12
                    16 2 2ab 4                           1
                  − Hab G − Hab Hcd Gac Gbd − Hab Gab G2 + 2G2abGc b Hca
                     3             3                     3
                    1                     8                     1
                  − (∇a Gbc )∇a Gbc + (∇a Hbc )∇a H bc − G4
                    3                      3                    2
                    4 abcde
                  + ε       Hab Hcd ∇ f Ge f − 2ε abcde Hb f (∇a Hc f )Gde
                    3
                    2                              1
                  − ε abcde Hab (∇ f Gc f )Gde − ε abcde (∇ f Ga f )Gbc Gde
                    3                             24
                      4                  4                   4
                  − g − NHab Gab + NG2 − 8NH 2 + Vab i j Li j H ab
                          3               3                   3
                          2 ij         ab    2 
                       − Vab Li j G − RN
                        3                   3                             
                     2 1 2 ab             1 2 2                8        1
                  +g       L H Gab − L G + 2L2 H 2 − N 2 + RL2
                         3                3                    3        6
                    4 3 2 1 4 4
                  − g NL − g L ,                                               (8)
                    3           6

where Vab i j = 2ea µ eb ν ∂[µ Vν ] i j −2V[a k(iVb]k j) . Furthermore, we have used the follow-
                             1 abcde
ing notations: H ab = − 12     ε         Hcde , H 2 = H ab Hab , G2 = Gab Gab , Hab
                                                                                  2 := H c H ,
                                                                                          a   bc
G2ab := Ga c Gbc , G4 = G2ab G2ab , and H 4 = H 2ab Hab        2 .

2.3.3 Log

In superspace, the composite linear superfield associated with the “Log multiplet”
is described by
                                       3i (i j kl)
                     LiLog
                        j      ij
                           → HLog :=       ∇ ∇ ∇kl logW .                      (9)
                                      1280
                                    ij
Here, the primary superfield HLog is obtained by making use of the standard Weyl
multiplet and by acting with six spinor covariant derivatives on W , with W being the
superfield describing the primary field strength of a compensating vector multiplet.
                                      j)
In (9), we have denoted ∇i j = ∇α (i ∇α , and the primary field LiLog
                                                                   j     ij
                                                                      = HLog |θ =0 is ob-
tained by projection to the lowest θ = 0 component. The rest of the composite Log
multiplet is then obtained by further acting with up to two more spinor covariant
```

</details>

<a id="src-g25-p008"></a>

<details>
<summary>G25-p008 — PDF page 8: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p008: PDF page 8](https://arxiv.org/pdf/2504.10856v1#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
8                                            Authors Suppressed Due to Excessive Length
                 ij
derivatives on HLog . Due to the complexity of computing up to eight supersymme-
try transformations, the explicit form of the Log multiplet, including all fermionic
terms, has been obtained only recently with the aid of the Cadabra software [58, 59].
The expression of the lowest component, (9), in its expanded form in terms of the
descendants of W and Wαβ was obtained in [33]. It takes the form

 ij   1              272i α i j
HLog = Wab Φ abi j −     χ χα
      2     (         3
                          1           1        9
      +W −1 − 6X i j D + Fab Φ abi j − X i j − X i jW abWab
                          2           2        64
                                                                            )
                 1 ab        j)              (i     j)             (i    j)
               + W Wab α (i λα + 8i(Γ a )αβ χα ∇a λβ − 8i(Γ a )αβ λα ∇a χβ
                 4
               (
                 1 ij      1                 1            j)    i         i)
         +W −2     X W + ∇aW ∇a X i j + F abWab α (i λα − λ α ( j λα
                 2         2                  4                 2
                 i a α i            3i                      (i    j)
                −   ∇ λ ∇a λαj − ε abcde (Σab )αβ Wde λα ∇c λβ − 2iDλ α iλαj
                4                   16
                3i              j                          (i j)
              − (Γ a )αβ λαi λβ ∇cWac − 4i(Σab)αβ F ab χα λβ + 4iX i j χ α k λα k
                 8                                                        )
                  9i abcde                           3i
              +      ε     (Γa )αβ WbcWde λαi λβj +     W abWab λ α i λαj
                256                                 128
              (
            −3 1 i j ab         1              1          
         +W       X F Fab − X i j X kl Xkl − X i j ∇aW ∇aW
                8               8              4
                i                     (i     j)    i                (i j)
              − ε abcde (Σab )αβ Fde λα ∇c λβ − (Γ a )αβ Fab λα ∇b λβ
                8                                  4
                i              j         i
              − (Γ a )αβ λαi λβ ∇c Fac + (Γ a )αβ X i j λαk ∇a λβ k
                4                        4
                i a αβ k(i j)               i            (i          
              + (Γ ) X λα ∇a λβ k − (Γ a )αβ λα ∇a X j)l λβ l
                4                           4
                i αi j           3i a  α (i          j)    i              (i j)
              + λ λα W +           ∇ W λ ∇a λα − (Σab )αβ ∇aW λα ∇b λβ
                4                4                          2
                3i                              3i
              − (Γ a )αβ Wab λαi λβj ∇bW + Wab F ab λ α i λαj
                16                             32                          )
                9i abcde      αβ          i j      3i        αβ i j ab k
              + ε        (Γa ) Wbc Fde λα λβ − (Σab ) X W λα λβ k
                64                                 32
              (
                   3i                        3i                j)
         +W −4 − λ α i λαj ∇aW ∇aW − (Γ a )αβ X k(i λα λβ k ∇aW
                   16                         8
                    3i a αβ                 3i
                +     (Γ ) Fab λαi λβj ∇bW + F ab Fab λ α i λαj
                    8                       32
```

</details>

<a id="src-g25-p009"></a>

<details>
<summary>G25-p009 — PDF page 9: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p009: PDF page 9](https://arxiv.org/pdf/2504.10856v1#page=9) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
On five-dimensional curvature squared supergravity and holography                      9

                   3i abcde                          3i
                  +   ε     (Γa )αβ Fbc Fde λαi λβj − (Σab )αβ X i j F ab λαk λβ k
                   64                                16 )
                   3i i j kl α          3i kl           j
                  − X X λk λα l − X Xkl λ α i λα
                   16                   32
         + higher fermions .                                                         (10)

    We have suppressed the higher-fermion terms, as they do not contribute to the
bosonic sector. Inserting the resulting composite multiplet into (3) yields the ex-
plicit form of a new “Log invariant” which was presented in [34] in the standard
Weyl basis. Then, the Log invariant in the gauged dilaton Weyl background can
be obtained by employing the map (1) and (4). In this paper, it suffices to present
its bosonic sector in the gauge (7). The gauged Log invariant in the dilaton Weyl
background, which includes a Ricci-squared term, reads
               1            1      1           1          4
   e−1 LLog = − Rab Rab + R2 + Rab G2ab + RHab Gab − Rab H ac Gb c
               6           24      6           3          3
               1    2    1 abcde                 1 abi j
              − RH − ε           CaVbc Vdei j + V Vabi j − 2(H 2 )2
                                      ij
               3        12                       6
               16 2 ac b        4 2      ab     2                        
              + Hab H G c − H Hab G + Hab Hcd Gab Gcd − 2Gac Gbd
                3               3               3
               2 2 2 4 2ab 2          1                           1
              + H G − H Gab − Hab G G + G2ab H ac Gb c − (G2 )2
                                              ab 2
               3          3           3                           48
                1 4 1         ac b                 [a bc]
              − G − ∇c G ∇ Gab + 2∇aHbc ∇ H
               24      6
                1 abcde f
              + ε       ∇ Ge f (4Hab − Gab )(4Hcd − Gcd )
               48
               g
              + RN − 4NHabGab − 2NG2 + Vab i j Li j (Gab + 4H ab) + 12NH 2
               6              
                     − 6∇a ∇a N
                  g2                                                             
                −      2RL2 − L2 (G2 − 4GabHab − 24H 2) + 4N 2 + 6∇a Li j ∇a Li j
                  24
                  2 2 3 5 4 4
                + NL g + L g .                                                    (11)
                  3          24

2.3.4 Scalar curvature squared

In order to construct the supersymmetric completion of the Ricci scalar-squared in-
variant, one may start by defining a composite vector multiplet in terms of a linear
multiplet. This composite vector multiplet is then substituted into the vector mul-
tiplet action obtained using (3). The bosonic sector of the gauged scalar curvature-
squared invariant in the gauged dilaton Weyl background, (1) and in the gauge (7),
is given by:
```

</details>

<a id="src-g25-p010"></a>

<details>
<summary>G25-p010 — PDF page 10: Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13</summary>

[G25-p010: PDF page 10](https://arxiv.org/pdf/2504.10856v1#page=10) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
10                                                  Authors Suppressed Due to Excessive Length

       e−1 LR2 =Yi j Yi j − 2∇a (NL−1 )∇a (NL−1 )
                    1
                − εabcdeCa Gbc Gde + NL−1 Gab Gab − N 2 L−2 Gab Gab
                    8
                                         1
                + 4N 2 L−2 H ab Gab − Gab Gab − 4NL−1 Hab Gab
                                         4
                                          1            1       5     1
                     2 1 ij a
                +g          L ∇ ∇a Li j − RL2 − H 2 L2 + G2 L2 − N 2 − E a Ea
                          4                4            8       2     2
                            1        
                        − ∇a L∇a L
                            2
                                  1
                − 4gN 3 L−2 + g4 L4 ,                                        (12a)
                                 16
where,
                                                                    
     Gab =4∇[a (L−1 Eb] ) + 2L−1 Li j (Vab i j ) − 2L−3 Li j ∇[a Lik ∇b] Lk j ,
           1                                                 
     Yi j = L−1 4∇a ∇a Li j − 2RLi j − 8H 2Li j + G2 Li j
           4                                                                           
            + L−3 −N 2 Li j − E a Ea Li j − 2E a Lk(i ∇a Lk j) − Lkl ∇a Lk(i ∇a L j)l       .   (12b)

2.4 Gauged Riemann-squared Action

In this section, we construct the gauged Riemann-squared action. It turns out that the
supersymmetric extension of the gauged Riemann-squared invariant can be achieved
by taking a linear combination of the new curvature-squared Log invariant and the
Weyl-squared invariant. By closely examining (11) and (8), it becomes evident that
the following combination

                                  LRiem2 = LWeyl2 + 2LLog                                        (13)

provides an off-shell supersymmetric description of the gauged Riemann-squared
invariant. Accordingly, we can define the corresponding composite linear multiplet
  ij
HRiem 2 for the Riemann-squared invariant as

                                   ij        ij        ij
                                  HRiem 2 = HWeyl2 + 2HLog .                                     (14)

The resulting bosonic sector of gauged Riemann-squared Lagrangian is given by
                      1
       e−1 LRiem2 = − ε abcdeCa Rbc f g Rde f g + V abi jVabi j
                      8
                      1                1
                    − Rabcd Rabcd + Rabcd (Gab Gcd − 2H abH cd − 3H abGcd )
                      4                3
                                       16        2      1
                    − 4RabH ac Gb c + Rab Hab       + Rab G2ab + RHabGab − 2RH 2
                                        3               3
```

</details>

<a id="src-g25-p013"></a>

<details>
<summary>G25-p013 — PDF page 13: Relations22–23; gauge25, reference26 and connection split27</summary>

[G25-p013: PDF page 13](https://arxiv.org/pdf/2504.10856v1#page=13) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
On five-dimensional curvature squared supergravity and holography                   13

which is topological in four dimensions, meaning it does not contribute dynamically
to the field equations. The GB combination, known for being ghost-free, plays a fun-
damental role in higher-derivative corrections and anomaly cancellation [62, 54].
In fact, it is expected to control the leading-order α ′ corrections in string theory
[63, 27]. In five dimensions, the ungauged GB invariant has been constructed off-
shell and fully classified [56, 55, 13]. However, the supersymmetric gauged GB
invariant has remained absent from the literature. Interestingly, we find that the su-
persymmetric extension of the gauged GB invariant can be formulated as a linear
combination of the new curvature-squared Log invariant and the Weyl-squared in-
variant. By closely examining (11) and (8), it becomes evident that the following
combination

                                LGB = LWeyl2 − 4LLog ,                           (22)

provides an off-shell supersymmetric description of the gauged GB invariant. Ac-
                                                                       ij
cordingly, we can define the corresponding composite linear multiplet HGB for the
GB invariant as
                                   ij      ij          ij
                                 HGB = HWeyl2 − 4HLog .                          (23)

The resulting gauged GB Lagrangian is given by
              1                            1     1
  e−1 LGB = − Rabcd Rabcd + RabRab − R2 − ε abcdeCa Rbc f g Rde f g
              4                            4     8
              1 abcde         ij        1
            + ε        CaVbc Vdei j + Rabcd (Gab Gcd − 2H abH cd − 3H abGcd )
              2                         3
                                 16 ab 2 2 ab 2
            + 4RabH G c + R Hab − R Gab − RHabGab + 4(H 2)2
                      ac b
                                 3             3
                  4       2                                  1
            − 8H + 8Had H c G − 2HabHcd Gab Gcd + (G2 )2
                              a    cd
                                                             6
            + 4HabHcd Gac Gbd + HabGab G2 − 2G2abGc b Hca
              1                       8                   1
            − (∇a Gbc )∇a Gbc + (∇a Hbc )∇a H bc − G4
              3                       3                   3
              2
            + ∇c Gac ∇b Gab − 8∇a Hbc ∇[a H bc]
              3
                                             1
            − 2ε abcde Hb f (∇a Hc f )Gde − ε abcde (∇ f Ga f )Gbc Gde
                                            8             
               + g 4NHab Gab − 4Vabi j Li j H ab + 4∇a ∇a N
                                                                               
                                 1                          1
               + g2 L2 H ab Gab − L2 G2 + 6L2H 2 − 2N 2 + RL2 + ∇a Li j ∇a Li j
                                 2                          2
               − 4g3NL2 − g4 L4 .                                                (24)
```

</details>

<a id="src-g25-p014"></a>

<details>
<summary>G25-p014 — PDF page 14: Relations22–23; gauge25, reference26 and connection split27</summary>

[G25-p014: PDF page 14](https://arxiv.org/pdf/2504.10856v1#page=14) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
14                                             Authors Suppressed Due to Excessive Length

3 On-shell Analysis and holographic central charges

In this section, we investigate the on-shell analysis of the quadratic curvature cor-
rections to 5D minimal gauged supergravity by applying proper field redefinitions,
which allows us to extract the central charges and obtain the corrected thermody-
namic quantities. Based on previous work [60, 44, 53], we find that the computa-
tion of the leading higher curvature contributions to the Euclidean action of AdS
black holes is drastically simplified once the higher curvature terms are expressed
in terms of powers of the Weyl tensor. Due to the fact that the Weyl tensor vanishes
sufficiently fast near the AdS boundary, we can avoid some of the complications
typically introduced by higher-derivative GHY terms or boundary counterterms. In
the next section, we will illustrate how to compute the leading higher curvature
contributions to thermodynamic quantities based on the redefined action.

3.1 On-shell Analysis

The conformal supergravity in a gauged dilaton Weyl multiplet basis can be obtained
by using the BF-action (3), along with the composite definitions (1). Imposing the
gauge fixing conditions (7), along with the following choice to break the SU(2)R
symmetry to U(1)R
                                         1
                                  Li j = √ δi j L ,                            (25)
                                          2
leads to the gauged off-shell Poincaré supergravity
                                                              
              −1               1     ab          ab    ′i j ′a
             e L = L R − Gab G + 4HabH + 2Va Vi j
                               2
                                                     √
                      +L ∂a L∂ a L − 2L−1 E a Ea − 2 2E aVa − 2L−1 N 2
                         −1

                                                   1
                      −4gE aCa − 2gLN − 4gN − g2 L3 + 2g2L2 ,                       (26)
                                                   2
                      ij                          ′i j
where we have split Va into its traceless part Va and trace part Va . Specically,
                                               1
                               Vai j = Va′i j + δ i jVa .                           (27)
                                               2

From this Lagrangian, the auxiliary fields N ,Va′i j can be eliminated by their equa-
tions of motion
                               1
                        N = − gL(2 + L) ,           Va′i j = 0 .                 (28)
                               2
We can, furthermore, dualize the two-form gauge field Bµν to a vector field C̃µ by
adding a Lagrange multiplier term [24]. The resulting model can be further truncated
to a minimal model by setting
```

</details>

### W: cached source equations

Source PDF: 2013-Proeyen-Weyl multiplets of N = 2 conformal supergravity in five dimensions.pdf. SHA-256: `ec863fb0ec5f88b74743f65055c74cbfb01af3383b514c75de19e7b4fac967a0`.

<a id="src-w-p015"></a>

<details>
<summary>W-p015 — PDF page 15: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p015: PDF page 15](https://arxiv.org/pdf/hep-th/0104113v4#page=15) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
   The transformations are generated by operators according to
      δ = ξ a Pa + λab Mab + ΛD D + ΛaK K a + Λij Uij + i ǭQ + i η̄S .                  (3.1)
The i factors in the last two terms appear due to the reality properties, as
explained in appendix A.
   We can read off the transformation rules for the gauge fields from the
algebra (B.1) using the general rules for gauge theories. We find
    δeµ a = Dµ ξ a − λab eµb − ΛD eµ a + 12 ǭγ a ψµ ,
                                            [a
   δωµ ab = Dµ λab − 4ξ [a fµ b] − 4ΛK eµ b] + 12 i ǭγ ab φµ − 21 i η̄γ ab ψµ ,
     δbµ = ∂µ ΛD − 2ξ a fµa + 2ΛaK eµa + 21 i ǭφµ + 12 i η̄ψµ ,
    δfµ a = Dµ ΛaK − λab fµb + ΛD fµ a + 12 η̄γ a φµ ,
    δVµij = ∂µ Λij − 2Λ(i ℓ Vµj)ℓ − 23 i ǭ(i φj)  3     (i j)
                                               µ + 2 i η̄ ψµ ,

     δψµi = Dµ ǫi + i ξ a γa φiµ − 14 λab γab ψµi − 21 ΛD ψµi − Λi j ψµj − i eaµ γa η i , (3.2)
     δφiµ = Dµ η i − 14 λab γab φiµ + 21 ΛD φiµ − Λi j φjµ − i ΛaK γa ψµi + i fµa γa ǫi ,
where Dµ is the covariant derivative with respect to dilatations, Lorentz
rotations and SU(2) transformations:
                   Dµ ξ a   =    ∂µ ξ a + bµ ξ a + ωµ ab ξb ,
                  Dµ λab    =    ∂µ λab + 2ωµc [a λb]c ,
                  Dµ ΛaK    =    ∂µ ΛaK − bµ ΛaK + ωµ ab ΛKb ,
                   Dµ ǫi    =    ∂µ ǫi + 21 bµ ǫi + 14 ωµab γab ǫi − Vµij ǫj ,
                    Dµ η i = ∂µ η i − 21 bµ η i + 41 ωµab γab η i − Vµij ηj .            (3.3)
Using the commutator expressions (B.1) we obtain the following expressions
for the curvatures (terms proportional to vielbeins are underlined for later
use):
  Rµν a (P ) = 2∂[µ eν] a + 2ω[µ ab eν]b + 2b[µ eν] a − 12 ψ̄[µ γ a ψν] ,
 Rµν ab (M) = 2∂[µ ων] ab + 2ω[µ ac ων]c b + 8f[µ [a eν] b] + i φ̄[µ γ ab ψν] ,
   Rµν (D) = 2∂[µ bν] − 4f[µ a eν]a − i φ̄[µ ψν] ,
  Rµν a (K) = 2∂[µ fν] a + 2ω[µ ab fν]b − 2b[µ fν] a − 12 φ̄[µ γ a φν] ,
                                                          (i   j)
  Rµν ij (V ) = 2∂[µ Vν] ij − 2V[µk(i Vν] k j) −3 i φ̄[µ ψν] ,                           (3.4)
   Rµν i (Q) = 2∂[µ ψν]
                     i
                        + 21 ω[µ ab γab ψν]
                                         i         i
                                            + b[µ ψν] − 2V[µ ij ψν] j + 2 i γa φi[µ eν] a ,
   Rµν i (S) = 2∂[µ φiν] + 12 ω[µ ab γab φiν] − b[µ φiν] − 2V[µ ij φν] j − 2 i γa ψ[µ
                                                                                   i
                                                                                      fν] a .

                                              14
```

</details>

<a id="src-w-p016"></a>

<details>
<summary>W-p016 — PDF page 16: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p016: PDF page 16](https://arxiv.org/pdf/hep-th/0104113v4#page=16) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    Since the transformation laws given above satisfy the F 2 (4) superalgebra,
we have a gauge theory of F 2 (4), but we do not have a gauge theory of
diffeomorphisms of spacetime. This can only be realized if we take the spin
connection as a composite field that depends on the vielbein. So far, we have
it as an independent field.4
    Furthermore, we see that the number of bosonic and fermionic degrees
of freedom do not match. The gauge fields together have 96 + 64 degrees of
freedom. Therefore, we can not have a supersymmetric theory with invertible
general coordinate transformations generated by the square of supersymme-
try operations.

3.2     Constraints and their solutions
The solution to the problems described above is well known. In order to
convert the P -gauge transformations into general coordinate transformations
and to obtain irreducibility we need to impose curvature constraints and we
have to introduce extra matter fields in the multiplet.
    The constraints will define some gauge fields as dependent fields. The
extra matter fields will also change the transformations of the gauge fields.
In fact, we will have for the transformation (apart from the general coordinate
transformations) of a general gauge field hIµ :
                     δJ (ǫJ )hIµ = ∂µ ǫI + ǫJ hµ A fAJ I + ǫJ MµJ I ,              (3.5)
where we use the index I to denote all gauge transformations apart from
general coordinate transformations, and an index A includes the translations.
    The last term depends on the matter fields, and its explicit form has
to be determined below. But also the second term has contributions from
matter fields. This is due to the fact that the structure ‘functions’ of the
final algebra fIJ K are modified from those of the F 2 (4) algebra which was
used for (3.2). These extra terms lead also to modified curvatures
                  b I = 2∂ h I + h B h A f I − 2h J M I .
                  R                                                                (3.6)
                   µν     [µ ν]   ν   µ   AB     [µ  ν]J

   The commutator of two supersymmetry-transformations will also change.
In particular we will find transformations with field-dependent parameters.
   4
    One might think that the field equations can determine the spin connection as a
dependent gauge field. This can indeed be done for the spin connection, but it is not
known how to generalize this for the gauge fields of special (super)conformal symmetries,
which we also want to be dependent gauge fields.

                                           15
```

</details>

<a id="src-w-p017"></a>

<details>
<summary>W-p017 — PDF page 17: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p017: PDF page 17](https://arxiv.org/pdf/hep-th/0104113v4#page=17) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
They can be conveniently written as so-called covariant general coordinate
transformations which are defined as

                              δcgct(ξ) = δgct (ξ) − δI (ξ µ hµ I ) ,       (3.7)

namely a combination of general coordinate transformations and all the other
transformations whose parameter ǫI is replaced by ξ µ hµ I . This takes a sim-
pler form on fields of various types:

                δcgct (ξ)eµ a = (∂µ + bµ )ξ a + ωµ ab ξb ,
                                     b I − ξ ν hJ M I − ξ ν hJ ea f I ,
                 δcgct (ξ)hIµ = −ξ ν Rµν         µ    νJ     µ ν aJ
                                 µ
                  δcgct (ξ)Φ = ξ Dµ Φ .                                    (3.8)

The last terms for Bµν are similar to the M-term for usual gauge fields in
the second line. The last line holds for all covariant matter fields, including
their covariant derivatives Da , or covariant curvature tensors after changing
the indices to local Lorentz indices.
    We will consider the fünfbein as an invertible field. Then some of the cur-
vatures in (3.4) are linear in some gauge fields. This is shown by the under-
lined terms in (3.4). Therefore, we can impose constraints on these curvatures
that are solvable for these gauge fields. Such constraints are called conven-
tional constraints, and imposing them reduces the Weyl multiplet, such that
we get closer to an irreducible multiplet. The conventional constraints are5

                                      Rµν a (P ) = 0 (50) ,
                                     b ab (M) = 0 (25) ,
                                eν b Rµν
                                     µb i
                                   γ Rµν (Q) = 0 (40) .                    (3.9)

    In brackets we denoted the number of restrictions each constraint im-
poses. These constraints are similar to those for other Weyl multiplets in 4
dimensions with N = 1 [19, 21], N = 2 [31] or N = 4 [28], or in 6 dimensions
for the (1, 0) [22] or (2, 0) [29] Weyl multiplets.
    In general one can add extra terms to the constraints (3.9), which just
amount to redefinitions of the composite fields. By choosing suitable terms
simplifications were obtained in 4 and 6 dimensions. In this case one could
e.g. add a term Tµa T ab to the second constraint rendering all the constraints
  5                                                    bρσ] i (Q) = 0.
      Note that the third constraint implies that γµν R

                                               16
```

</details>

<a id="src-w-p018"></a>

<details>
<summary>W-p018 — PDF page 18: Full Weyl geometry, constraints, transformations and soft algebra</summary>

!W-p018: PDF page 18 (W, p. 18) ([source locator)

Layout text for searching; the image controls mathematical transcription.

```text
invariant under S-supersymmetry, but in 5 dimensions this turns out to be
impossible. Therefore we keep the constraints as written above.
   Due to these constraints the fields ωµ ab , fµ a and φiµ are no longer inde-
pendent, but can be expressed in terms of the other fields. In order to write
down the explicit solutions of these constraints, it is useful to extract the
terms which have been underlined in (3.4). We define R     b ′ as the curvatures
without these terms. Formally,
                                b′ I = R
                                R      b I + 2hJ ea f I ,                                  (3.10)
                                 µν     µν     [µ ν] aJ

where faJ I are the structure constants in the F 2 (4) algebra that define com-
mutators of translations with other gauge transformations. Then the solu-
tions to the constraints are
                         b]
  ωµab = 2eν[a ∂[µ eν] − eν[a eb]σ eµc ∂ν eσc + 2eµ [a bb] − 12 ψ̄ [b γ a] ψµ − 14 ψ̄ b γµ ψ a ,
  φiµ =      1
               i γaRb ′ i (Q) − 1 i γ γ ab R
                                           b ′ i (Q) ,                                     (3.11)
             3        µa        24   µ       ab

   fµa =     1    a      1
               R − 48 eµ R ,a
                                      Rµν ≡ R    b ′ ab (M)e ρ e ,             R ≡ Rµ µ .
             6 µ                                   µρ       a νb

The constraints imply through Bianchi identities further relations between
the curvatures. The Bianchi identities for R(P ) imply

      Rµν = Rνµ ,                   b (D) = R
                              e[µ a R       b      a                b (D) = 0 .
                                     νρ]      [µνρ] (M) ,           Rµν                    (3.12)

3.3     Adding matter fields
After imposing the constraints we are left with 21 bosonic and 24 fermionic
degrees of freedom. The independent fields are those in the left upper part
of table 3. These have to be completed with matter fields to obtain the full
Weyl multiplet. We have already seen that there are two possibilities for a
D = 5 Weyl multiplet with each 32 + 32 degrees of freedom.
    These are obtained by adding either the left lower corner or right lower
corner of table 3. To obtain all the extra transformations we imposed the
superconformal algebra, but at the same time allowing modifications of the
algebra by field-dependent quantities. The techniques are the same as already
used in 4 and 6 dimensions in [31, 28], and were described in detail in [22].
    For the fields in the upper left corner, we now have to specify the extra
parts M in (3.5). This will in fact only apply to Q-supersymmetry. The other
transformations are as in (3.2). The extra terms we can read already from the

                                               17
```

</details>

<a id="src-w-p019"></a>

<details>
<summary>W-p019 — PDF page 19: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p019: PDF page 19](https://arxiv.org/pdf/hep-th/0104113v4#page=19) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
linearized rules in (2.11) and (2.14). The full supersymmetry transformations
of these fields are

               δQ eµ a = 12 ǭγ a ψµ ,
                δQ ψµi = Dµ ǫi + i γ · T γµ ǫi ,
              δQ Vµ ij = − 23 i ǭ(i φj)      (i      j)     (i   j)
                                      µ + i ǭ γ · T ψµ + 4ǭ γµ χ ,
                δQ bµ = 12 i ǭφµ − 2ǭγµ χ ,                                        (3.13)

where Dµ ǫ is given in (3.3). The fields Tab and χi , and a further field D that
appears in their transformation laws (see below) are independent fields in
the Standard Weyl multiplet, but not in the Dilaton Weyl multiplet. There,
they are given by expressions that are the non-linear extensions of (2.13):
                                                                        
            Tab =    1 −2
                     8
                       σ          σ Fb    1        cedc + 1 i ψ̄γ ψ
                                     ab − 6 εabcde H      4      ab           ,

            χi =     1
                     8
                              Dψ i + 16
                       i σ −1 /          1
                                                   Dσψ i − 32
                                            i σ −2 /                σ γ · Fb ψ i +
                                                                 1 −2

                     + 41 σ −1 γ · T ψ i + 32 1
                                                 i σ −3 ψj ψ̄ i ψ j ,
                                                                      1 −2 b 2
             D =       σ ✷ σ + 18 σ −2 (Da σ)(D a σ) − 16
                     1 −1 c
                     4
                                                                       σ F −
                        1 −2 /             1 −4 i j
                     − 8 σ ψ̄ Dψ − 64 σ ψ̄ ψ ψ̄i ψj − 4 i σ −1 ψ̄χ +
                                                                        
                     + − 26 T + 2σ −1 Fbab + 41 i σ −2 ψ̄γab ψ T ab ,
                          3 ab
                                                                                     (3.14)

where the conformal d’alembertian is defined by
                                                  
   ✷c σ ≡ D a Da σ =            ∂ a − 2ba + ωb ba Da σ − 12 i ψ̄a D a ψ − 2σ ψ̄a γ a χ +
                            + 12 ψ̄a γ a γ · T ψ + 12 φ̄a γ a ψ + 2fa a σ ,          (3.15)

and where the underlining indicates that these terms are dependent fields.
We have not substituted these terms in the expression for D for reasons of
brevity.
    The modification M in (3.5) is the last term of the transformations of ψµi ,
Vµij and bµ . The second term in the transformation of Vµij on the other hand is
due to the fact that the structure constants have become structure functions,
and in particular there appears a new T -dependent SU(2) transformation in
the anti-commutator of two supersymmetries. We will give the full new
algebra in section 4.

                                              18
```

</details>

<a id="src-w-p020"></a>

<details>
<summary>W-p020 — PDF page 20: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p020: PDF page 20](https://arxiv.org/pdf/hep-th/0104113v4#page=20) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
    The transformation rules for the matter fields6 of the Weyl multiplets are
as follows. For the Standard Weyl multiplet we have (Q and S supersymme-
try)

       δTab =      1
                     i ǭγab χ − 323
                                     i ǭRb (Q) ,
                   2                       ab

        δχi =      1 i         1
                     ǫ D − 64 γ · R  b (V )ǫ + 1 i γ ab DT
                                        ij                    / ab ǫi − 18 i γ a D b Tab ǫi −
                   4                           j     8
                  − 14 γ abcd Tab Tcd ǫi + 61 T 2 ǫi + 41 γ · T η i ,
        δD =         / − 35 i ǭγ · T χ − i η̄χ .
                  ǭDχ                                                                        (3.16)

There are no explicit gauge fields here, as should be the case for ‘matter’,
i.e. non-gauge fields. These are all hidden in the covariant derivatives and
covariant curvatures. The covariant derivatives are for any matter field given
by the rule                                     
                        Da Φ = eµa ∂µ − δI (hIµ ) Φ .                   (3.17)
The last term represents thus a sum over all transformations except general
coordinate transformations, with parameters replaced by the corresponding
gauge fields. In practice, the Lorentz transformations and SU(2) transforma-
tions follow directly from the index structure and lead to additions similar
to those in (3.3). For the Weyl transformations there is a term −w bµ Φ,
where w is the Weyl weight of the field that can be found in table 3, and
then there remain the terms for Q and S supersymmetry. There are no K
transformations for any matter field in this paper.
    The covariant curvatures are given by the general rule (3.6), e.g.
               b i (Q) = R i (Q) + 2 i γ · T γ ψ i ,
               Rµν        µν                  [µ ν]
                                                    (i
              b ij (V ) = R ij (V ) − 8ψ̄ γ χj) − i ψ̄ γ · T ψ ,     (i         j)
              Rµν          µν            [µ ν]        [µ      ν]                            (3.18)

                                                                        b )
where Rµν i (Q) and Rµν ij (V ) are those given in (3.4). Note that for R(V
there are corrections from modified structure functions as well as from M-
dependent terms. Having all the matter field dependence, we can obtain
further consequences of the curvature constraints. E.g. the Bianchi identity
   6
     As we have already seen, two of the extra fields in the Dilaton Weyl multiplet are
actually gauge fields, rather than matter fields. However, we use uniformly ‘matter fields’
for them in this context to indicate that they are not gauging a symmetry of the super-
conformal algebra.

                                              19
```

</details>

<a id="src-w-p021"></a>

<details>
<summary>W-p021 — PDF page 21: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p021: PDF page 21](https://arxiv.org/pdf/hep-th/0104113v4#page=21) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
   b
on R(Q) gives:7
            b
        γ · R(S)            b
                 = − 83 T · R(Q) ,
                           b (Q) + 4 γ T · R(Q)
         b (S) = − 1 i D µ R
       γµR                                 b               b (Q) ,
                                                + 2γb T bµ R
          µν       2        µν     3 ν                      µν
         b (S) = − i D
         R           /Rb (Q) − i γ D ρ R               b
                                       b (Q) − 8 γ T · R(Q)                           (3.19)
          µν            µν        [µ    ν]ρ    3 µν
                                     b (Q) − 3γ · T R
                      +12γb T ρb γ[µ R              b (Q) − 8T ρ Rb
                                      ν]ρ            µν         [µ ν]ρ (Q) .

    Given these transformation rules, we can calculate the transformations
of the dependent fields. Their transformation rules are now determined by
their definition due to the constraints. An equivalent way of expressing this
is that their transformation rules are modified w.r.t. (3.2), due to the non-
invariance of the constraints under these transformations. We have chosen
the constraints to be invariant under all bosonic symmetries without mod-
ifications. Therefore, only the Q- and S-supersymmetries of the dependent
fields are modified to get invariant constraints. The new transformation of
the spin connection is
                         1
             δωµ ab =    2
                           i ǭγ ab φµ − 21 i η̄γ ab ψµ −
                         − i ǭγ [a γ · T γ b] ψµ −
                                     b b] (Q) − 1 ǭγ R
                         − 21 ǭγ [a R                  b ab (Q) − 4e [a ǭγ b] χ .   (3.20)
                                      µ           4   µ              µ

The first line is the transformation as implied from the F 2 (4) algebra, see (3.2).
The second line is due to the modification of the anti-commutator of two su-
persymmetries by a T -dependent Lorentz rotation. Finally, the last line
contains the terms that go into the M of (3.5). We give here for φiµ just the
latter type of terms
                                  n                     o
                            1
            δφiµ = . . . − 12                        b i (V )ǫj +
                              i γ ab γµ − 12 γµ γ ab Rab j
                          h                                            i
                      + 13 /
                           Dγ · T γµ − Dµ γ · T + γµ γ c D a Tac ǫi +
                          h                                                 i
                      + i −γµabcd T ab T cd + 8γρ T ρσ Tµσ − 2γµ T 2 ǫi +
                                                  
                      + 31 i 8γ b Tµb − γµ γ · T η i .                                (3.21)

We will not need the transformations for the field fµ a , except the transforma-
tion of fa a under S, since this term appears in the conformal d’alembertian.
   7
     We thank F. Coomans for drawing our attention to mistakes in versions v1 and v2 of
this paper.

                                            20
```

</details>

<a id="src-w-p022"></a>

<details>
<summary>W-p022 — PDF page 22: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p022: PDF page 22](https://arxiv.org/pdf/hep-th/0104113v4#page=22) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
We only give its M-dependent S-transformation

                                       δS fa a = −5 i η̄χ .                                (3.22)

We also used the transformation of the following curvatures:
                                                     
   b i (Q) =
  δR               1                                   b i (V )ǫj + 1 R
                       γab cd − γ cd γab − 21 γab γ cd R              b cd (M)γ ǫi +
    ab             6                                    cd j        4 ab       cd
                           
                   +2 i D[a γ · T γb] − 31 D[a γb] γ · T −
                                                                     
                               − 31 γ[a /
                                       Dγ · T γb] − 13 γab Dc γd T cd ǫi
                   −8Tab η i + 16 T c γ η i + 43 γabcd T cd η i ,
                                3 [a b]c
                                                                                           (3.23)
                         b j) (S) − 8ǭ(i γ D χj) + i ǭi γ · T R
  b ij (V ) = − 3 i ǭ(i R
 δR                                                             b j) (Q) +
   ab           2         ab               [a b]                 ab
                                                            b j) (Q) + 8 i η̄ (i γ χj) .
                   +8 i ǭ(i γ[a γ · T γb] χj) + 32 i η̄ (i Rab                   ab

   The Q- and S-supersymmetry variations of the matter fields in the Dila-
ton Weyl multiplet are

        δAµ = − 21 i σǭψµ + 12 ǭγµ ψ ,
       δBµν = 21 σ 2 ǭγ[µ ψν] + 12 i σǭγµν ψ + A[µ δ(ǫ)Aν] ,
        δψ i = − 41 γ · Fb ǫi − 12 i /
                                    Dσǫi + σγ · T ǫi − 14 i σ −1 ǫj ψ̄ i ψ j + ση i ,
         δσ = 12 i ǭψ .                                                              (3.24)

The gauge fields Aµ and Bµν have the additional symmetries

                                 δAµ = ∂µ Λ ,
                                δBµν = 2∂[µ Λν] − 12 ΛFµν .                                (3.25)

Note that the dependence of the transformation rules for Aµ and Bµν on ψµ
and Aµ signal new terms in the algebra of supersymmetries and U(1) trans-
formations8 . This algebra will be written in section 4. On the other hand,
the F -term in δBµν should be interpreted as an M term according to (3.5),
and modifies the field strength accordingly. This leads to the following field
strengths of these gauge fields

          Fbµν = 2∂[µ Aν] + 12 i σ ψ̄[µ ψν] − ψ̄[µ γν] ψ ,
         c                   3 2               3                   3
         H µνρ = 3∂[µ Bνρ] − 4 σ ψ̄[µ γν ψρ] − 2 i σ ψ̄[µ γνρ] ψ + 2 A[µ Fνρ] . (3.26)

   8
   The A[µ ψν] term in δBµν is an extension of (3.5) that occurs for antisymmetric tensor
gauge fields.

                                                21
```

</details>

<a id="src-w-p023"></a>

<details>
<summary>W-p023 — PDF page 23: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p023: PDF page 23](https://arxiv.org/pdf/hep-th/0104113v4#page=23) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
For the convenience of the reader we give their transformation rules:
        δ Fbab = − 12 i σǭR
                           b (Q) − ǭγ D ψ + i ǭγ γ · T γ ψ + i η̄γ ψ ,
                            ab        [a b]       [a      b]        ab
       c         3 2       b          3                  3
      δH abc = − 4 σ ǭγ[a Rbc] (Q) + 2 i ǭγ[ab Dc] ψ + 2 i D[a σǭγbc] ψ −

                  − 32 σǭγ[a γ · T γbc] ψ − 23 ǭγ[a Fbbc] ψ − 32 ση̄γabc ψ .                (3.27)
Finally, we give the Bianchi identities for these two curvatures
                             D[a Fbbc] =       1
                                               2
                                                       b (Q) ,
                                                 ψ̄γ[a R bc]
                               c
                           D[a H               3 b     b
                                 bcd] =          F F .
                                               4 [ab cd]
                                                                                              (3.28)
   This finishes our discussion of the Standard and Dilaton Weyl multiplets.
The final results for these multiplets have been collected in section 4. In the
next section we will explain the connection between the two multiplets.

4     Results for the two Weyl multiplets
For the convenience of the reader we collect in this section the essential
results of the previous sections, and give the supersymmetry algebra, which
is modified by field-dependent terms. The transformation under dilatation
is for each field δD Φ = wΛD Φ, where the Weyl weight w can be found in
table (3). The Lorentz, and SU(2) transformations are evident from the
index structure, and our normalizations can be found in (3.2).

4.1     The Standard Weyl multiplet
The Q- and S-supersymmetry and K-transformation rules for the indepen-
dent fields of the Standard Weyl multiplet are
      δeµ a = 12 ǭγ a ψµ ,
      δψµi = Dµ ǫi + i γ · T γµ ǫi − i γµ η i ,
      δVµ ij = − 32 i ǭ(i φj)     (i   j)     (i      j)  3     (i j)
                            µ + 4ǭ γµ χ + i ǭ γ · T ψµ + 2 i η̄ ψµ ,

      δTab =      1
                    i ǭγab χ − 323
                                    i ǭRb (Q) ,
                  2                       ab

       δχi =      1 i               b
                    ǫ D − 64 γ · R (V )ǫj + 81 i γ ab /
                              1        ij
                                                            DTab ǫi − 18 i γ a D b Tab ǫi −
                  4
                 − 14 γ abcd Tab Tcd ǫi + 61 T 2 ǫi + 14 γ · T η i ,
       δD =        Dχ − 53 i ǭγ · T χ − i η̄χ ,
                 ǭ /
                  1
       δbµ =      2
                    i ǭφµ − 2ǭγµ χ + 21 i η̄ψµ + 2ΛKµ .                                      (4.1)

                                             22
```

</details>

<a id="src-w-p024"></a>

<details>
<summary>W-p024 — PDF page 24: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p024: PDF page 24](https://arxiv.org/pdf/hep-th/0104113v4#page=24) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
The covariant derivative Dµ ǫ is given in (3.3). For other covariant derivatives,
see the general rule (3.17), with more explanation below that equation. The
                       b
covariant curvatures R(Q)           b ) are given explicitly in (3.18). The
                              and R(V
expressions for the dependent fields are given in (3.11), where the prime
indicates the omission of the underlined terms in (3.4).

4.2      The Dilaton Weyl multiplet
The Dilaton Weyl multiplet contains two extra gauge transformations: the
gauge transformations of Aµ with parameter Λ and those of Bµν with param-
eter Λµ . The transformation of the fields are given by:
      δeµ a = 21 ǭγ a ψµ ,
      δψµi = Dµ ǫi + i γ · T γµ ǫi − i γµ η i ,
      δVµ ij = − 32 i ǭ(i φj)     (i    j)     (i       j)  3   (i j)
                            µ + 4ǭ γµ χ + i ǭ γ · T ψµ + 2 i η̄ ψµ ,
       δAµ = − 12 i σǭψµ + 21 ǭγµ ψ + ∂µ Λ ,
      δBµν = 21 σ 2 ǭγ[µ ψν] + 12 i σǭγµν ψ + A[µ δ(ǫ)Aν] + 2∂[µ Λν] − 21 ΛFµν ,
       δψ i = − 14 γ · Fb ǫi − 12 i /
                                   Dσǫi + σγ · T ǫi − 14 i σ −1 ǫj ψ̄ i ψ j + ση i ,
        δσ = 12 i ǭψ ,
       δbµ = 21 i ǭφµ − 2ǭγµ χ + 12 i η̄ψµ + 2ΛKµ .                                  (4.2)
The covariant curvature of Aµ and Bµν can be found in (3.26). The trans-
formation of the dependent fields and the curvatures have been given in the
previous section. We have underlined the fields Tab and χi to indicate that
they are not independent fields but merely short-hand notations. The explicit
expression for these fields in terms of fields of the Dilaton Weyl multiplet are
given in (3.14).

4.3      Modified superconformal algebra
Finally, we present the ‘soft’ algebra that these Weyl multiplets realize. This
is the algebra that all matter multiplets will have to satisfy, apart from possi-
bly additional transformations under which the fields of the Weyl multiplets
do not transform, and possibly field equations if these matter multiplets are
on-shell.
    The full commutator of two supersymmetry transformations is
          [δQ (ǫ1 ), δQ (ǫ2 )] = δcgct (ξ3µ ) + δM (λab                    ij
                                                     3 ) + δS (η3 ) + δU (λ3 ) +

                                             23
```

</details>

<a id="src-w-p025"></a>

<details>
<summary>W-p025 — PDF page 25: Full Weyl geometry, constraints, transformations and soft algebra</summary>

[W-p025: PDF page 25](https://arxiv.org/pdf/hep-th/0104113v4#page=25) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                    +δK (ΛaK3) + δU (1) (Λ3 ) + δB (Λ3µ ) .                (4.3)
The covariant general coordinate transformations have been defined in (3.7).
The last two terms appear obviously only in the Dilaton Weyl multiplet
formulation. The parameters appearing in (4.3) are
                 ξ3µ =     1
                             ǭ γ ǫ ,
                           2 2 µ 1
               λab
                3  =       − i ǭ2 γ [a γ · T γ b] ǫ1 ,
                               (i          j)
                λij
                  3  =     i ǭ2 γ · T ǫ1 ,
                   i
                 η3 =      − 49 i ǭ2 ǫ1 χi + 74 i ǭ2 γc ǫ1 γ c χi +
                                                                       
                                     (i       j)                b cd (Q) ,
                           + 41 i ǭ2 γcdǫ1 γ cd χj + 41 R          j
                                                   1 i abc j b
              ΛaK3 =       − 21 ǭ2 γ a ǫ1 D + 96   ǭ2 γ ǫ1 Rbcij (V ) +
                                                                       
                             1
                           + 12 i ǭ2 −5γ abcd Db Tcd + 9Db T ba ǫ1 +
                                                                            
                           +ǭ2 γ abcde Tbc Tde − 4γ c Tcd T ad + 32 γ a T 2 ǫ1 ,
                Λ3 = − 21 i σǭ2 ǫ1 ,
               Λ3µ = − 12 σ 2 ξ3µ − 21 Aµ Λ3 .                                             (4.4)
For the Q, S commutators we find the following algebra:
   [δS (η), δQ (ǫ)] = δD ( 12 i ǭη) + δM ( 21 i ǭγ ab η) + δU (− 32 i ǭ(i η j) ) + δK (Λa3K ) ,
 [δS (η1 ), δS (η2 )] = δK ( 12 η̄2 γ a η1 ) .                                               (4.5)
with                                                             
                           Λa3K = 61 ǭ γ · T γa − 12 γa γ · T η .                         (4.6)
The commutator of Q and U(1) transformations is given by
                                                                   
                            [δ(ǫ), δ(Λ)] = δB − 21 Λδ(ǫ)Aµ .                               (4.7)
    This concludes our description of the Standard and Dilaton Weyl multi-
plets.

5      Connection between the Weyl multiplets
In the previous section we have shown that the Standard and Dilaton Weyl
multiplets can be related to each other by expressing the fields of the Stan-
dard Weyl multiplet in terms of those of the Dilaton Weyl multiplet (see (3.14)).

                                                24
```

</details>

<a id="src-w-p028"></a>

<details>
<summary>W-p028 — PDF page 28: Improved-vector constraints5.10–5.14 and their descendants</summary>

[W-p028: PDF page 28](https://arxiv.org/pdf/hep-th/0104113v4#page=28) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
curved background extension of the flat spacetime action defined by (5.3)
and next derive the equations of motion from this action. However, for our
present purposes, it is sufficient to find the equations of motion only.
    We want to identify the spinor ψ i of the vector multiplet with the spinor
  i
ψ of the Dilaton Weyl multiplet. This is why we have given these two
spinors the same name in the first place (see the footnote in subsection 2.3).
Comparing the SU(2) triplet term in the supersymmetry transformations of
the two spinors, see (3.24) and (5.6), we deduce that the constraint S ij does
not get any corrections and we must have

                              S ij = 2σY ij − 12 i ψ̄ i ψ j .                       (5.10)

There are now two ways to proceed. One way is to make the transition to an
on-shell vector multiplet by using (5.10) to eliminate the auxiliary field Y ij
from the transformation rules (5.6). The commutator of two supersymmetry
transformations would then only close modulo the equations of motion.
    A more elegant way is to note that the equations of motion must transform
into each other. By varying (5.10) under (5.6) we find

                                δS ij = i ǭ(i Γj) ,                                (5.11)

where the supercovariant extension of Γi is now given by

                                 Dσψ i − 14 γ · Fb ψ i + Y ij ψj +
                      Dψ i + 12 i /
              Γi = i σ /
                   +2σγ · T ψ i − 8σ 2 χi .                                         (5.12)

Varying this expression under (5.6) and using (5.8) leads to the other equa-
tions of motion. We find:

             δΓi = − 12 i /
                         DS ij ǫj − 21 i γ · Hǫi + 21 Cǫi − γ · T S ij ǫj ,         (5.13)

where the supercovariant generalizations of (5.4) are given by

      C = − 14 Fbab Fb ab − 12 ψ̄ Dψ
                                  / + σ✷c σ + 21 D a σDa σ + Y ij Yij +
              + i ψ̄γ · T ψ − 16 i σ ψ̄χ − 104
                                            3
                                               σ 2 Tab T ab + 8σ Fbab T ab − 4σ 2 D ,
                                                                       
    Ha = − 18 εabcde Fb bc Fb de − D b 8σ 2 Tba − σ Fbba − 41 i ψ̄γba ψ .           (5.14)

The supercovariant equations of motion and Bianchi identity are then given
by
                     0 = S ij = Γi = C = Ha = Gabc .                (5.15)

                                            27
```

</details>

<a id="src-w-p029"></a>

<details>
<summary>W-p029 — PDF page 29: Improved-vector constraints5.10–5.14 and their descendants</summary>

[W-p029: PDF page 29](https://arxiv.org/pdf/hep-th/0104113v4#page=29) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
5.3    Solving the equations of motion
In 6 dimensions, the equations of motion for an on-shell tensor multiplet
coupled to the Standard Weyl multiplet can be used to eliminate the matter
fields of the latter in terms of the matter fields of the Dilaton Weyl multiplet.
Precisely the same happens here. First of all the equations of motion for Y ij
can be used to eliminate this auxiliary field. Next, the equations of motion
for ψ i and σ can be used to solve for the fields χi and D, respectively. The
expressions for these fields exactly coincide with the ones we found in (3.14).
    The solution for the matter field Tab in terms of the fields of the Dila-
ton Weyl multiplet is more subtle. It requires that we first reinterpret the
equation of motion for the vector field as the Bianchi identity for a two-form
antisymmetric tensor gauge field Bµν . To be precise, we rewrite Ha = 0
from (5.14) as a Bianchi identity
                                    c
                                D[a H        3 b    b
                                      bcd] = 4 F[ab Fcd] ,                          (5.16)

                               c is defined by
where the three-form curvature H abc

                              cedc = 8σ 2 T − σ Fb − 1 i ψ̄γ ψ .
                  − 61 εabcde H                                                     (5.17)
                                           ab     ab 4      ab

Note that the latter equation is just a rewriting of the relation (3.14) we
found in section 3.
   The Bianchi identity (5.16) can be solved in terms of an antisymmetric
two-form gauge field Bµν . The superconformal algebra (5.9) imposes that
such a field transforms under supersymmetry as follows:

               δQ Bµν = 21 σ 2 ǭγ[µ ψν] + 21 i σǭγµν ψ + A[µ δ(ǫ)Aν] .            (5.18)

In addition one finds that the field Bµν transforms under a U(1) and a vector
gauge transformation as follows

                             δBµν = 2∂[µ Λν] − 12 ΛFµν .                            (5.19)

Furthermore, the commutator of two Q-transformations picks up a vector
gauge transformation δB for the field Bµν :

                [δ(ǫ1 ), δ(ǫ2 )] = . . . + δU (1) (Λ3 ) + δB (Λ3µ ) ,
                Λ3 = − 12 i σǭ2 ǫ1 ,       Λ3µ = − 41 σ 2 ǭ2 γµ ǫ1 − 12 Aµ Λ3 .   (5.20)

                                            28
```

</details>

<a id="src-w-p032"></a>

<details>
<summary>W-p032 — PDF page 32: AppendixA: all 5D Clifford, symplectic-Majorana, SU(2), Fierz and duality conventions</summary>

[W-p032: PDF page 32](https://arxiv.org/pdf/hep-th/0104113v4#page=32) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
mission RTN programme HPRN-CT-2000-00131, in which E.B., R.H. and
T.de W. are associated to the university of Utrecht. R.H. was in part sup-
ported by a Marie Curie fellowship of the European Community programme
“Improving Human Research Potential and the Socio-Economic Knowledge
Base”, contract number HPMT-CT-2000-00165. We were also supported
by the programme Supergravity, Superstrings and M-Theory of the Centre
Émile Borel of the Institut Henri Poincaré Paris (UMS 839-CNRS/UPMC),
and thank this center and the Spinoza institute in Utrecht for hospitality.
A.V.P. thanks the Caltech-USC Center for hospitality while the paper was
finalized.

A     Notations and Conventions
The metric is (− + + + +), and we use the following indices (spinor indices
are always omitted)

                        µ 0, . . . , 4 local spacetime ,
                        a 0, . . . , 4 tangent spacetime ,
                        i    1, 2      SU(2) .                           (A.1)

   The generators Uij of the R-symmetry group SU(2) are defined to be
anti-hermitian and symmetric, i.e.

                         (Ui j )∗ = −Uj i ,      Uij = Uji .             (A.2)

A symmetric traceless Ui j corresponds to a symmetric U ij since we lower or
raise SU(2) indices using the ε-symbol, in NW–SE convention:

       X i = εij Xj ,     Xi = X j εji ,        ε12 = −ε21 = ε12 = 1 .   (A.3)

The actual value of ε is here given as an example. It is in fact arbitrary as
long as it is antisymmetric, εij = (εij )∗ and εjk εik = δj i .
    The charge conjugation matrix C and Cγa are antisymmetric. The matrix
C is unitary and γa is hermitian apart from the timelike one, which is anti-
hermitian. The bar is the Majorana bar:

                                   λ̄i = (λi )T C .                      (A.4)

                                           31
```

</details>

<a id="src-w-p033"></a>

<details>
<summary>W-p033 — PDF page 33: AppendixA: all 5D Clifford, symplectic-Majorana, SU(2), Fierz and duality conventions</summary>

[W-p033: PDF page 33](https://arxiv.org/pdf/hep-th/0104113v4#page=33) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
We define the charge conjugation operation on spinors as
                                                                                     ∗
      (λi )C ≡ α−1 B −1 εij (λj )∗ ,               λ̄iC ≡ (λi )C = α−1 λ̄k                 Bεki ,    (A.5)
where B = Cγ0 , and α = ±1 when one uses the convention that complex
conjugation does not interchange the order of spinors, or α = ± i when it
does. Symplectic Majorana spinors satisfy λ = λC . Charge conjugation acts
on gamma matrices as (γa )C = −γa , does not change the order of matrices,
and works on matrices in SU(2) space as M C = σ2 M ∗ σ2 . Complex conju-
gation can then be replaced by charge conjugation, if for every bispinor one
inserts a factor −1. Then, e.g. the expressions
                                        λ̄i γµ λj ,         i λ̄i χi                                 (A.6)
are real for symplectic Majorana spinors. For more details, see e.g. [24].
   When the SU(2) indices on spinors are omitted, northwest-southeast con-
traction is understood, e.g.
                                        λ̄γ (n) ψ = λ̄i γ (n) ψi ,                                   (A.7)
where we have used the following notation
                              γ (n) = γ a1 ···an = γ [a1 γ a2 · · · γ an ] .                         (A.8)
   The anti-symmetrizations are always with unit strength. Changing the
order of spinors in a bilinear leads to the following signs
                                                            (
         (1)        (2)          (2)         (1)                tn = −1 for n = 2, 3
       ψ̄ γ(n) χ          = tn χ̄ γ(n) ψ           ,                                                 (A.9)
                                                                tn = +1 for n = 0, 1
where the labels (1) and (2) denote any SU(2) representation.
   We frequently use the following Fierz rearrangement formulae
 ψj λ̄i = − 14 λ̄i ψj − 41 λ̄i γ a ψj γa + 81 λ̄i γ ab ψj γab ,         ψ̄ [i λj] = − 12 ψ̄λεij . (A.10)
   When one multiplies three spinor doublets, one should be able to write the
result in terms of (8 ×7 ×6)/3! = 56 independent structures. From analyzing
the representations, one can obtain that these are in the (4, 2)+(4, 4)+(16, 2)
representations of SO(5) × SU(2). They are
                               ξj ξ¯j ξ i = γ a ξj ξ¯j γa ξ i = 18 γ ab ξ i ¯
                                                                           ξγab ξ ,
                               ξ (k ξ¯i ξ j) ,
                               ξj ξ¯j γa ξ i .                                                      (A.11)

                                                       32
```

</details>

<a id="src-w-p034"></a>

<details>
<summary>W-p034 — PDF page 34: AppendixA: all 5D Clifford, symplectic-Majorana, SU(2), Fierz and duality conventions</summary>

[W-p034: PDF page 34](https://arxiv.org/pdf/hep-th/0104113v4#page=34) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
       The Levi–Cività tensor is real and satisfies
                                                  [c         c ]
  εa1 ...an b1 ...bp εa1 ...an c1 ...cp = −n!p!δ[b11 . . . δbpp] ,     εµνρστ = eeµa eνb · · · eτe εabcde .
                                                                                                     (A.12)
We introduce the dual of a tensor as

                              Ãa1 ...a5−n = n!1 i εa1 ...a5−n b1 ...bn Abn ...b1 ,               (A.13)

with the properties

          ˜ = A,            1 a1 ...an            1           1
          Ã                   A       Ba1 ...an = A · B =          Ã · B̃ ,                     (A.14)
                            n!                    n!       (n − 5)!

where we have introduced the notation A · B that we use throughout the
paper.
   The product of all gamma matrices is proportional to the unit matrix in
odd dimensions. We use
                           γ abcde = i εabcde .                    (A.15)
This implies that the dual of a (5 − n)-antisymmetric gamma matrix is the
n-antisymmetric gamma matrix given by
                                          1
                            γa1 ...an = (5−n)! i εa1 ...an b1 ...b5−n γ b5−n ...b1 .              (A.16)

       For convenience we will give a rule for calculating gamma-contractions
like
                                       γ (m) γ(n) γ(m) = cn,m γ(n) ,                              (A.17)
where the constants cn,m are given for the most frequently used cases in
table 7.

                                        d=5            m=1 m=2
                                        n=0              5  −20
                                        n=1             −3   −4
                                        n=2              1    4
                                        n=3              1    4

                          Table 7: The coefficients cn,m in (A.17).

                                                        33
```

</details>

### OP: cached source equations

Source PDF: 2013-Ozkan-Supersymmetric Completion of GB.pdf. SHA-256: `4cc005cc0dbd96246e709ef267cf6956d08e64fa8b5910b20cf0549e50e29d20`.

<a id="src-op-p004"></a>

<details>
<summary>OP-p004 — PDF page 4: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p004: PDF page 4](https://arxiv.org/pdf/1301.6622v4#page=4) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
invariants allow us to combine different invariants to obtain more general theories.
      The crucial observation in our construction of supersymmetric Gauss-Bonnet combina-
tion is that although three independent curvature squared terms enter the expression of
Gauss-Bonnet combination, such an off-shell construction might be possible with only two
independent curvature squared super-invariants. This observation is based on the fact that
the Riemann squared invariant obtained in [28] using the Dilaton Weyl multiplet contains an
ordinary kinetic term for the auxiliary vector field Vµij . Thus the Riemann square extended
Poincaré supergravity contains a dynamical massive auxiliary vector in its spectrum which
forms the same multiplet with the massive graviton generated by the Riemann squared
term. By counting degrees of freedom, we notice that it might always be the case (except
for the pure Ricci scalar squared invariant) that when formulated in terms of Dilaton Weyl
multiplet, the curvature squared super-invariant includes an ordinary kinetic term for the
auxiliary vector field Vµij . Therefore, if there exist two independent curvature squared super-
invariants, a particular combination of them can be formed in which the kinetic term for
the auxiliary vector vanishes. This implies that there is no massive graviton since the mas-
sive vector and massive graviton fall into the same multiplet, suggesting that the curvature
squared terms comprise Gauss-Bonnet combination.
      Based on the above observation, we start looking for another curvature squared invari-
ant constructed in terms of the Dilaton Weyl multiplet besides the known Riemann tensor
squared invariant. An obvious candidate is Cb µνρσ C
                                                   bµνρσ , which is the superconformal ex-
tension of the Weyl tensor squared term whose supersymmetric completion was obtained
previously in [24]1 using the Standard Weyl multiplet coupled to the vector multiplet. Utiliz-
ing superconformal tensor calculus, we supersymmetrize the square of super-covariant Weyl
tensor. We find that in addition to the Weyl tensor squared term, the bosonic action acquires
a Ricci scalar squared term arising from the square of D, which is a fundamental scalar
field in the Standard Weyl multiplet but a composite field in the Dilaton Weyl multiplet.
Equivalently, the curvature squared terms in the action take the form of C µνρσ Cµνρσ + 16 R2 .
Since
                         C µνρσ Cµνρσ + 61 R2 = Rµνρσ Rµνρσ − 34 Rµν Rµν + 13 R2          (1.3)

the ratio of coefficients in front of the Rµν Rµν and R2 terms is -4, which is the required
value to obtain the supersymmetric completion of Gauss-Bonnet invariant by combining a
Riemann squared invariant with an appropriate coefficient.
      This paper is organized as follows. In section 2, we briefly review the superconformal
  1
      The on-shell theory of this model is derived in [25].

                                                        4
```

</details>

<a id="src-op-p005"></a>

<details>
<summary>OP-p005 — PDF page 5: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p005: PDF page 5](https://arxiv.org/pdf/1301.6622v4#page=5) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
multiplets of five-dimensional supergravity constructed in [23, 26, 29]. In section 3, we
review the construction of the superconformal linear multiplet action [27] and obtain a su-
perconformal action for the Yang-Mills multiplet coupled to the Dilaton Weyl multiplet.
In section 4, we fix the superconformal symmetries to obtain an off-shell Poincaré super-
gravity and an off-shell Yang-Mills theory coupled to the Dilaton Weyl multiplet. Using
a map between the Yang-Mills multiplet and the Dilaton Weyl multiplet [28], we recon-
struct the off-shell supersymmetric Riemann squared action. In section 5, we present the
supersymmetric completion of C µνρσ Cµνρσ + 61 R2 and combine it with a supersymmetric
Riemann squared invariant to obtain the supersymmetric Gauss-Bonnet combination. In
section 6, we derive the D = 5 on-shell minimal Einstein Hilbert supergravity and on-shell
Gauss-Bonnet extended Einstein-Maxwell supergravity. In section 7, we discuss the vac-
uum solutions with AdS3 × S 2 and AdS2 × S 3 structures. The bosonic spectrum around
a maximally supersymmetric Minkowski5 vacuum is also analyzed. In section 8 we give
conclusion and discussions.

2     Superconformal Multiplets

In this section, we introduce the basic elements of five dimensional superconformal tensor
calculus with eight supercharges [23, 26]. In section 2.1, we present the Dilaton Weyl
multiplet adopted in our construction. In the subsequent two subsections, we briefly review
two superconformal matter multiplets of D = 5, N = 2 theory: the Yang-Mills multiplet
and the linear multiplet, which are used as compensator multiplets in the construction of
superconformal actions.

2.1    Dilaton Weyl Multiplet

In [26], it was established that there exist two different Weyl multiplets for N = 2 confor-
mal supergravity in five dimensions: the Standard Weyl multiplet and the Dilaton Weyl
multiplet. These two multiplets have the same contents of gauge fields but different matter
fields. However, the matter fields of the Standard multiplet can be built from the funda-
mental fields in the Dilation Weyl multiplet as composite fields. The gauge sector of the
Dilaton Weyl multiplet consists of a fünfbein eµ a , a gravitino, ψµ i , the dilatation gauge field
bµ , and the SU(2) gauge field Vµij . Since these gauge fields account for 21(bosonic) +24
(fermionic) degrees of freedom, they cannot form a super-multiplet. Therefore, matter fields
are needed to comprise a superconformal Weyl multiplet. For the Dilaton Weyl multiplet,

                                                 5
```

</details>

<a id="src-op-p006"></a>

<details>
<summary>OP-p006 — PDF page 6: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p006: PDF page 6](https://arxiv.org/pdf/1301.6622v4#page=6) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
the matter sector consists of a physical vector Cµ , an antisymmetric two-form gauge field
Bµν , a dilaton field σ and a dilatino ψ i . The Q, S and K transformation rules for the
Dilaton Weyl Multipet are given by [26]

                                1 a
                  δeµ a =       2 ǭγ ψµ ,

                   δψµi = (∂µ + 12 bµ + 14 ωµ ab γab )ǫi − Vµij ǫj + iγ · T γµ ǫi − iγµ η i ,

                 δVµ ij    = − 23 iǭ(i φj)     (i   j)    (i      j)  3 (i j)
                                         µ + 4ǭ γµ χ + iǭ γ · T ψµ + 2 iη̄ ψµ ,

                   δCµ = − 21 iσǭψµ + 21 ǭγµ ψ,
                                1 2             1
                 δBµν      =    2 σ ǭγ[µ ψν] + 2 iσǭγµν ψ + C[µ δ(ǫ)Cν] ,

                   δψ i = − 41 γ · b
                                   Gǫi − 12 i /
                                             Dσǫi + σγ · T ǫi − 41 iσ −1 ǫj ψ̄ i ψ j + ση i ,
                                1
                     δσ =       2 iǭψ ,
                                1                   1
                    δbµ =       2 iǭφµ − 2ǭγµ χ + 2 iη̄ψµ + 2ΛKµ ,                                            (2.1)

where

                      Dµ σ = (∂µ − bµ )σ − 21 iψ̄µ ψ ,
                                                                                  b µi
                      Dµ ψ i = (∂µ − 32 bµ + 41 ωµ ab γab )ψ i − Vµij ψj + 14 γ · Gψ
                                           / µi + 41 iσ −1 ψµj ψ̄ i ψ j − σγ · T ψµi − σφiµ ,
                                     + 21 iDσψ                                                                  (2.2)

and the supercovariant curvatures are defined according to

                               bµν
                               G       = Gµν − ψ̄[µ γν] ψ + 21 iσ ψ̄[µ ψν] ,
                             b µνρ = Hµνρ − 3 σ 2 ψ̄[µ γν ψρ] − 3 iσ ψ̄[µ γνρ] ψ,
                             H                                                                                  (2.3)
                                            4                   2

                                                                                    bµν and
In above expressions, Gµν = 2∂[µ Cν] and Hµνρ = 3∂[µ Bνρ] + 23 C[µ Gνρ] . Note that G
Hb µνρ are invariant under following gauge transformations

                               δCµ = ∂µ Λ ,           δBµν = 2∂[µ Λν] − 12 ΛGµν .                               (2.4)

The definitions of spin connection ωµ ab and the S-supersymmetry gauge field φiµ are given
in [26]

          ωµ ab = 2eν[a ∂[µ eν] b] − eν[a eb]σ eµc ∂ν eσ c + 2eµ [a bb] + 12 ψ̄ [a γ b] ψµ + 14 ψ̄ a γµ ψ b ,
                       1 a b′ i        1      ab b ′ i
            φiµ =      3 iγ Rµa (Q) − 24 iγµ γ Rab (Q),                                                         (2.5)

      bi (Q), the supercovariant curvature of gravitino is defines as [26]
where R µν

            Rbµν
               i         b′ µν i (Q) − 2iγ[µ φi ,
                   (Q) = R                    ν]

           b′ µν i (Q) = 2∂[µ ψ i + 1 ω[µ ab γab ψ i + b[µ ψ i − 2V ij ψν]j + 2iγ · T γ[µ ψ i .
           R                                                                                                    (2.6)
                                 ν]               ν]        ν]     [µ                      ν]
                                     2

                                                           6
```

</details>

<a id="src-op-p007"></a>

<details>
<summary>OP-p007 — PDF page 7: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p007: PDF page 7](https://arxiv.org/pdf/1301.6622v4#page=7) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
For future reference, we also give the supercovariant curvature of ωµ ab and Vµij [26]

   bµν ab (M ) = 2∂[µ ων] ab + 2ω[µ ac ων]cb + 8f[µ [a eν] b] + iψ̄[µ γ ab ψν] + iψ̄[µ γ [a γ · T γ b] ψν]
   R
                                                          bab (Q) − 8ψ̄[µ eν] [a γ b] χ + iφ̄[µ γ ab ψν] ,
                                  bν] b] (Q) + 1 ψ̄[µ γν] R
                       +ψ̄[µ γ [a R            2
    bµν ij (V ) = 2∂[µ Vν] ij − 2V[µ k(i Vν] k j) −3iφ̄(i ψ j) − 8ψ̄ (i γν] χj) − iψ̄ (i γ · T ψ j) .
    R                                                                                                         (2.7)
                                                       [µ ν]        [µ               [µ         ν]

                                                     bµν and H
The Q- and S- transformations of the field strengths G       b abc are presented in [26]

                bµν
               δG                  bµν (Q) − ǭγ[µ Dν] ψ + iǭγ[µ γ · T γν] ψ + iη̄γµν ψ ,
                        = − 12 iσǭR
                babc = − 3 σ 2 ǭγ[a R
               δH                    bbc] (Q) + 3 iǭγ[ab Dc] ψ + 3 iǭγ[ab ψDc] σ
                         4                      2                 2
                                                                    bbc] ψ − 3 σ η̄γabc ψ .
                                − 23 σǭγ[a γ · T γbc] ψ − 23 ǭγ[a G                                         (2.8)
                                                                             2

The expressions for the composite fields Tab , χi and D are given as follows [26]
                                                                       
              Tab =       1 −2         bab + 1 ǫabcde H
                                      σG              b cde + 1 iψ̄γab ψ ,
                          8σ                 6                4

               χi =       1 −1 / i   1   −2 / i 1 −2     b i 1 −1         i
                          8 iσ Dψ + 16 iσ Dσψ − 32 σ γ · Gψ + 4 σ γ · T ψ
                            1
                          + 32 iσ −3 ψj ψ̄ i ψ j ,
                          1 −1 c    1 −2        a      1 −2 b  bµν
                D =       4 σ ✷ σ + 8 σ (Da σ)(D σ) − 16 σ Gµν G
                                              1 −4 i j
                          − 81 σ −2 ψ̄ /
                                      Dψ − 64   σ ψ̄ ψ ψ̄i ψj − 4iσ −1 ψχ
                                                                       
                                                −1 b      1 −2
                          + − 26   3  T ab + 2σ   G  ab + 4 iσ ψ̄γ ab ψ   T ab ,                              (2.9)

where the superconformal d’Alambertian for σ is given by

                  ✷c σ = (∂ a − 2ba + ωb ba )Da σ − 12 iψ̄a D a ψ − 2σ ψ̄a γ a χ

                       + 12 ψ̄a γ a γ · T ψ + 12 φ̄a γ a ψ + 2fa a σ,
                  f a = − 1 Rµ a + 1 eµ a R, Rµν ≡ R           b′ ab (M )eb ρ eνa ,       R ≡ Rµ µ .         (2.10)
                   µ        6            48                        µρ

             b′ (M ) indicates that we have omitted the fµ a term in b
The notation R                                                       R(M ). It was es-
tablished in [26] that one can also construct another Weyl multiplet, the Standard Weyl
multiplet if considering Tab , D and χi as fundamental fields instead as a matter sector in
addition to the gauge sector of the Weyl multiplet. Therefore, the composite expressions
of these fields establish a map from the Dilaton Weyl multiplet to the Standard Weyl mul-
tiplet. We refer to [26, 27] for readers interested in the derivation of this map and the
five-dimensional Weyl multiplets in superconformal theory. For later convenience, we also
present the Q- and S- transformations of the composite fields [26]

                                1             3    b
                δTab =          2 iǭγab χ − 32 iǭRab (Q) ,

                                                          7
```

</details>

<a id="src-op-p008"></a>

<details>
<summary>OP-p008 — PDF page 8: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p008: PDF page 8](https://arxiv.org/pdf/1301.6622v4#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                    δχi =       1 i      1     bij        1 ab /     i  1 a b        i
                                4 ǫ D − 64 γ · R (V )ǫj + 8 iγ DTab ǫ − 8 iγ D Tab ǫ

                                − 14 γ abcd Tab Tcd ǫi + 16 T 2 ǫi + 14 γ · T η i ,
                           / − 53 iǭγ · T χ − iη̄χ ,
                    δD = ǭDχ                                                                                   (2.11)

where the supercovariant derivatives of the composite fields are

       Dµ χi = (∂µ − 27 bµ + 14 ωµ ab γab )χi − Vµij χj − 41 ψµi D + 64
                                                                      1   bij (V )ψµj
                                                                        γ·R

                              DTab ψµi + 81 iγ a D b Tab ψµi + 14 γ abcd Tab Tcd ψµi − 61 T 2 ψµi − 14 γ · T φiµ ,
                    − 18 iγ ab /

      Dµ Tab = ∂µ Tab − bµ Tab − 2ωµ c [a Tb]c − 21 iψ̄µ γab χ + 32
                                                                  3      bab (Q) .
                                                                    iψ̄µ R                                      (2.12)

2.2     Yang-Mills Multiplet

The off-shell non-abelian D = 5, N = 2 vector multiplet consists of 8n (bosonic) + 8n (
fermionic) degrees of freedom (where n is the dimension of the gauge group). Denoting the
Yang-Mills index by I (I = 1, · · · , n), the bosonic sector consists of vector fields AIµ , scalar
fields ρI and SU(2)-triplet auxiliary fields Y ij I = Y (ij) I . SU(2)-doublet fields λiI constitute
the fermionic sector.
   In the background of the Dilaton Weyl multiplet, the Q- and S-transformations of the
fields in the vector multiplet are given by [29]

       δAIµ = − 21 iρI ǭψµ + 12 ǭγµ λI ,

   δY ij I    = − 21 ǭ(i /
                         Dλj)I + 21 iǭ(i γ · T λj)I − 4iρI ǭ(i χj) + 12 iη̄ (i λj)I − 21 igǭ(i fJK I ρJ λj)K ,

       δλiI   = − 41 γ · FbI ǫi − 12 i /
                                      DρI ǫi + ρI γ · T ǫi − Y ij I ǫj + ρI η i ,
                   1     I
       δρI    =    2 iǭλ .                                                                                     (2.13)

The superconformally covariant derivatives used here are

                                                              1
               Dµ ρI     = (∂µ − bµ )ρI + gfJK I AJµ ρK −       iψ̄µ λI ,                                       (2.14)
                                                              2
              Dµ λiI     = (∂µ − 32 bµ + 41 ωµ ab γab )λiI − Vµij λIj + gfJK I AJµ λiK
                             1
                           + γ · FbI ψµi + 21 i b/
                                               DρI ψµi + Y ijI ψµ j − ρI γ · T ψµi − ρI φiµ ,                   (2.15)
                             4

where the supercovariant Yang-Mills curvature is given as

                                                                      1 I
                       Fbµν
                         I
                            = 2∂[µ AIν] + gfJK I AJµ AK             I
                                                      ν − ψ̄[µ γν] λ + iρ ψ̄[µ ψν] .                            (2.16)
                                                                      2

                                                            8
```

</details>

<a id="src-op-p009"></a>

<details>
<summary>OP-p009 — PDF page 9: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p009: PDF page 9](https://arxiv.org/pdf/1301.6622v4#page=9) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2.3    Linear Multiplet

The off-shell D = 5, N = 2 linear multiplet contains 8 (bosonic)+8 (fermionic) degrees of
freedom carried by the following fields

                                              (Lij , E a , N, ϕi ).                              (2.17)

The bosonic fields are an SU(2) triplet Lij = L(ij) , a constrained vector Ea and a scalar N .
The fermionic fields are given by an SU(2) doublet ϕi . In the background of the Standard
Weyl multiplet, the Q- and S- transformations of the fields in the linear multiplet are given
by [27]

                  δLij   = iǭ(i ϕj) ,

                  δϕi = − 12 i /
                              DLij ǫj − 12 iγ a Ea ǫi + 12 N ǫi − γ · T Lij ǫj + 3Lij ηj ,

                  δEa = − 21 iǭγab D b ϕ − 2ǭγ b ϕTba − 2η̄γa ϕ ,
                             1 /      3                  i j      3
                   δN    =   2 ǭDϕ + 2 iǭγ · T ϕ + 4iǭ χ Lij + 2 iη̄ϕ ,                       (2.18)

where the super-covariant derivatives are defined as

            Dµ Lij = (∂µ − 3bµ )Lij + 2Vµ (i k Lj)k − iψ̄µ(i ϕj) ,

            Dµ ϕi = (∂µ − 72 bµ + 41 ωµ ab γab )ϕi − Vµij ϕj + 12 i /
                                                                   DLij ψµ j + 21 iγ a Ea ψµi

                         − 21 N ψµi + γ · T Lij ψµ j − 3Lij φµ j ,

            Dµ Ea = (∂µ − 4bµ )Ea + ωµab E b + 21 iψ̄µ γab D b ϕ + 2ψ̄µ γ b ϕTba + 2φ̄µ γa ϕ .   (2.19)

The closure of the superconformal algebra requires that the following constraint must be
satisfied
                                                 D a Ea = 0 .                                    (2.20)

Thus Ea can be solved in terms of a 3-form Eµνρ as

                                             1 µνρσλ
                                     E µ = − 12 ǫ    Dν Eρσλ ,                                   (2.21)

where Eµνρ is invariant under the following gauge transformation

                                         δΛ Eµνρ = 3∂[µ Λνρ] .                                   (2.22)

We can also express E µ and Eµνρ in terms of a 2-form potential according to [27]

                                            E µ = Dν E µν ,

                                          Eµνρ = ǫµνρσλ E σλ .                                   (2.23)

                                                       9
```

</details>

<a id="src-op-p010"></a>

<details>
<summary>OP-p010 — PDF page 10: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p010: PDF page 10](https://arxiv.org/pdf/1301.6622v4#page=10) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
The supersymmetry transformations of the 2-form gauge field Eµν and 3-form gauge field
Eµνρ are given in [27]

                         δE µν    = − 12 iǭγ µν ϕ − 12 ψ̄ρi γ µνρ ǫj Lij − ∂ρ Λ̃µνρ ,
                                               i
                        δEµνρ = −ǭγµνρ ϕ + iψ̄[µ γνρ] ǫj Lij .                          (2.24)

3     Superconformal Actions

In this section, we review the derivation of the superconformal action for the linear multiplet
[27], and construct a superconformal action for the Yang-Mills multiplet. We begin with
the following super-invariant density formula [23]

                                                                    1 µνρσλ
                 e−1 LV L = Y ij Lij + iλ̄ϕ − 12 ψ̄ai γ a λj Lij − 12 ǫ     Aµ ∂ν Eρσλ

                                 +ρ(N + 12 ψ̄a γ a ϕ + 14 iψ̄ai γ ab ψbj Lij ) .          (3.1)

By integration by parts, LV L can be reexpressed as

                      e−1 LV L = Y ij Lij + iλ̄ϕ − 21 ψ̄ai γ a ψ j Lij + 21 Fµν E µν

                                       +ρ(N + 12 ψ̄a γ a ϕ + 41 iψ̄ai γ ab ψbj Lij ) .    (3.2)

3.1   Linear Multiplet Action

In this section, we construct the vector multiplet in terms of fundamental fields of the linear
multiplet and the Dilation Weyl multiplet, and obtain an action for the linear multiplet by
using vetor-linear Lagrangian (3.2). Firstly, the scalar ρ in the vector multiplet can be
constructed from the elements of linear multiplet as follows [27]

                           ρ = 2L−1 N + iϕ̄i ϕj Lij L−3 ,            L2 = Lij Lij .       (3.3)

Using this expression and applying a sequence of supersymmetry transformations, we obtain
the full expressions for the components of vector multiplets in terms of elements in the linear
multiplet [27]

                  ρ = 2L−1 N + iL−3 ϕ̄i ϕj Lij ,

                         Dϕi L−1 + (16Lij χj + 4γ · T ϕi )L−1 − 2N Lij ϕj L−3
                 λi = −2i /
                              / ij Ljk ϕk − EL
                          +2i(DL            / ij ϕj )L−3 + 2iϕj ϕ̄i ϕj L−3

                          −6iϕj ϕ̄k ϕl Lkl Lij L−5 ,

                                                       10
```

</details>

<a id="src-op-p011"></a>

<details>
<summary>OP-p011 — PDF page 11: Multiplets, derivatives, curvatures, forms, full composites and density</summary>

[OP-p011: PDF page 11](https://arxiv.org/pdf/1301.6622v4#page=11) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
         Yij = L−1 ✷C Lij − Da Lk(i D a Lj)m Lkm L−3 − N 2 Lij L−3 − Eµ E µ Lij L−3

                      + 83 L−1 T 2 Lij + 4L−1 DLij + 2Eµ Lk(i D µ Lj) k L−3 − 21 iN L−3 ϕ̄(i ϕj)

                      − 34 L−5 N Lk(i Lj)m ϕ̄k ϕm − 32 L−3 ϕ̄(i Eϕ
                                                                / j) − 13 L−5 Lk(i Lj)m ϕ̄k Eϕ
                                                                                            / m

                      −8iL−1 χ̄(i ϕj) + 16iL−3 Lk(i Lj)m χ̄k ϕm + 2L−3 Lk(i ϕ̄k /
                                                                               Dϕj)

                      +2iL−3 Lij ϕ̄γ · T ϕ − 32 L−3 ϕ̄(i DL                           / j)k ϕn
                                                         / j)k ϕk − L−5 Lmn Lk (i ϕ̄m DL

                      − 16 L−5 Lkm ϕ̄i γ a ϕj ϕ̄k γa ϕm + 12
                                                           1 −7
                                                             L Lij Lkm Lpq ϕ̄k γa ϕm ϕ̄p γ a ϕq ,

        Fbµν                             bµν ij (V )Lij − 2L−3 Ll D[µ Lkp Dν] Llp
                = 4D[µ (L−1 Eν] ) + 2L−1 R                      k

                                                           bµν (Q) .
                      −2D[µ (L−3 ϕ̄i γν] ϕj Lij ) − iL−1 ϕ̄R                                                (3.4)

Substituting above composite expressions into the vector-linear Lagrangian (3.2), one ob-
tains the superconformal action for the linear multiplet [27]

               e−1 LL = L−1 Lij ✷c Lij − Lij Dµ Lk(i D µ Lj)m Lkm L−3 + N 2 L−1

                              −Eµ E µ L−1 + 38 LT 2 + 4DL − 12 L−3 E µν Llk ∂µ Lkp ∂ν Lpl

                              +2E µν ∂µ (L−1 Eν + Vνij Lij L−1 ) + fermions,                                (3.5)

where the complete expression for the superconformal d’Alembertian is defined as

         Lij ✷c Lij     = Lij (∂ a − 4ba + ωb ba )Da Lij + 2Lij Va i k D a Ljk + 6L2 fa a

                            −iLij ψ̄ ai Da ϕj − 6L2 ψ̄ a γa χ − Lij ϕ̄i γ · T γ a ψaj + Lij ϕ̄i γ a φja .   (3.6)

Fermionic contribution to above action can be straightforwardly read from the formulae
given in (3.4).

3.2   Yang-Mills Multiplet Action

This subsection is devoted to construct a superconformal action describing a vector multiplet
coupled to a Dilaton Weyl multiplet. Such an action was previously obtained in [23] using
the Standard Weyl multiplet and applied in [24] to derive an off-shell Poincaré theory.
Another use of the vector multiplet action was established in [26, 27], where the vector
multiplet action in the Standard Weyl multiplet background was used to derive the map
between the Standard Weyl multiplet and the Dilaton Weyl multiplet.
   Similar to the construction of a linear multiplet action, we can use the density formula
(3.1) to obtain an action for an abelian vector multiplet coupled to a Dilaton Weyl multiplet.
Based on the action for an abelian vector multiplet, we derive the action for a Yang-Mills
multiplet coupled to the Dilaton Weyl Multiplet.

                                                       11
```

</details>

<a id="src-op-p013"></a>

<details>
<summary>OP-p013 — PDF page 13: Gauge4.1, retained fields4.2 and truncated compensating transformations4.3</summary>

[OP-p013: PDF page 13](https://arxiv.org/pdf/1301.6622v4#page=13) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
4        Gauge Fixing and Off-Shell Actions

In the previous section, we have obtained superconformal actions for a linear multiplet and
Yang-Mills multiplet. In this section, we fix the redundant superconformal symmetries to
obtain off-shell supersymmetric theories including a Poincaré supergravity and Yang-Mills
coupled to the Dilaton Weyl multiplet.
        As discussed in [30] for the four-dimensional case and in [24] for the five-dimensional case,
the construction of a consistent Poincaré supergravity requires more than one compensator
multiplet if the Standard Weyl multiplet is adopted. However, if the Dilaton Weyl multiplet
is utilized, a single compensator multiplet is sufficient to construct a consistent Poincaré
supergravity. As we will present shortly, a consistent Poincaré supergravity is obtained via
gauge fixing the superconformal linear multiplet action [27] instead of the vector multiplet
action. The latter cannot give rise to a supergravity theory due to the lacking of Einstein-
Hilbert term in the action.
        In section 4.1 we present our gauge choices and the corresponding decomposition rules.
Imposing these gauge choices in the superconformal action, we obtain an off-shell Poincaré
supergravity in section 4.2. In section 4.3, we first present an off-shell action describing
Yang-Mills coupled to a Dilaton Weyl multiplet. Then, using a map between Yang-Mills
multiplet and Dilaton Weyl multiplet [28], we obtain an off-shell Riemann tensor squared
invariant. Different from [28] where the five-dimensional Riemann squared invariant is
obtained via circle reduction of the six-dimensional Riemann squared invariant, our con-
struction of the Yang-Mills action is purely based on the superconformal tensor calculus.

4.1        Gauge Fixing and Decomposition Rules

In this section, we introduce our gauge choices to fix the redundant superconformal sym-
metries in order to obtain off-shell supersymmetric theories. If we do not insist on the
canonical Einstein-Hilbert term in the action, there exists a set of gauge choices facilitating
the derivation of curvature squared invariant. These gauge choices are2
                           1
                   Lij = √ δij L,    σ = 1,    ψ i = 0,  bµ = 0.              (4.1)
                            2
The first gauge choice breaks the SU(2)R down to U(1)R whereas the second one fixes
dilatations, the third one fixes special supersymmetry transformations and the last one
fixes conformal boosts. After fixing the gauge, the remaining fields are
                                                                                          ′
         eµ a (10), ψµi (32), Cµ (4), Bµν (6), ϕi (8), L(1), Eµνρ (4), N (1), Vµ (4), Vµij (10).          (4.2)
    2
        The canonical Einstein-Hilbert term can be obtained by using another set of gauge choices [27].

                                                       13
```

</details>

<a id="src-op-p014"></a>

<details>
<summary>OP-p014 — PDF page 14: Gauge4.1, retained fields4.2 and truncated compensating transformations4.3</summary>

[OP-p014: PDF page 14](https://arxiv.org/pdf/1301.6622v4#page=14) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
      To maintain the gauge (4.1), the compensating transformations are required including a
compensating SU(2), a compensating special supersymmetry and a compensating conformal
boost with parameters (up to cubic fermion terms)
                         1  k(i j)l                    1
                λij = − √     S δ ǫkl , S ij = ǭ(i ϕj) − δij ǭk ϕl δkl ,
                        2L                             2
                 i              1
                η = − γ · T + 4γ · G  b ǫ , ΛKµ = − iǭφµ − 1 iη̄ψµ + ǭγµ χ.
                                         i           1
                                                                                                                  (4.3)
                                                     4       4

4.2      Off-Shell Poincaré Theory

Imposing the gauge fixing conditions (4.1) in the linear multiplet action (3.5), one can
obtain a consistent Poincaré supergravity whose action is given by3

           e−1 LLR =         1      1 −1     µ    1
                             2 LR + 2 L ∂µ L∂ L − 4 LGµν G
                                                          µν
                                                             − 16 LHµνρ H µνρ − L−1 N 2
                                                                                                      ′
                                                                    Vµ ∂ν Eρσλ + LVµij Vijµ
                                                                                                 ′
                                                            1 µνρσλ
                            + 16 L−1 ∂[µ Eνρσ] ∂ µ E νρσ + 6√ 2
                                                                ǫ

                            +fermions.                                                                            (4.4)

Notice that we have decomposed the field Vµij into its trace and traceless part as
                                            ′                        ′
                                  Vµij = Vµij + 12 δij Vµ ,       Vµij δij = 0.                                   (4.5)

The Poincaré supergravity presented above is invariant under the following supersymmetry
transformation rules (up to cubic fermion terms)

                     1 a
         δeµ a =     2 ǭγ ψµ ,
                                 bµν γ ν ǫi ,
         δψµi = Dµ (ω− )ǫi − 21 iG
                     1 (i ν bj)   1 (i     b j) 1 (i       b j)      ij  (i j)k
        δVµ ij =     2 ǭ γ ψµν − 6 ǭ γ · Hψµ − 4 iǭ γ · Gψµ + ∂µ λ + λ k Vµ ,

         δCµ = − 12 iǭψµ ,
                     1
        δBµν    =    2 ǭγ[µ ψν] + C[µ δ(ǫ)Cν] ,

           δL =      √1 iǭi ϕj δij ,
                       2
                   1 /
          δϕi = − 2√ 2
                       i∂ Lδij ǫj − √12 iVµ′ (i k δj)k Lǫj − 12 i /
                                                                 Eǫi + 21 N ǫi + 4√
                                                                                  1
                                                                                    2
                                                                                      Lγ · b
                                                                                           Gδij ǫj
                        1
                     − 6√         b ij ǫj ,
                            iLγ · Hδ
                          2

       δEµνρ = −ǭγµνρ ϕ + √12 iLψ̄[µ i
                                        γνρ] ǫj δij ,
                                       
         δN = 12 ǭγ µ ∂µ + 14 ωµ bc γbc ϕ + 12 ǭi γ a Va ij ϕj − 4√
                                                                    1
                                                                      2
                                                                        iǭi γ a ∂/Lψaj δij
                        1
                     + 4√ 2
                            iǭi γ a γ b Vb(i
                                           ′ k
                                               δj)k ψaj + 41 iǭγ a /                     1
                                                                   Eψa − 14 N ǭγ a ψa + 8√ 2
                                                                                              Lǭi γ a γ · b
                                                                                                           Gψaj δij
                      √
                     − 2Lǭi γ a φja δij + 81 iǭγ · Hϕ, b                                                          (4.6)
  3
      The action directly coming from (3.5) by imposing (4.1) is equal to−e−1 LLR .

                                                          14
```

</details>

<a id="src-op-p028"></a>

<details>
<summary>OP-p028 — PDF page 28: Appendices: gamma/spinor and notation conventions</summary>

[OP-p028: PDF page 28](https://arxiv.org/pdf/1301.6622v4#page=28) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
that these solutions are not modified by the inclusion of the higher-derivative interactions
proportional to α and β for arbitrary values. The spectrum of this theory around the
maximally supersymmetric Minkowski5 is determined. We show that the spectrum has a
ghostly massive spin two multiplet in addition to a massless supergravity and a Maxwell
vector multiplet. However, when β = 3α corresponding to the Gauss-Bonnet combination,
the massive spin-2 multiplet decouples.
    Our off-shell model is ungauged and therefore does not admit AdS5 as a supersymmetric
vacuum solution. The gauging of our model should be interesting. A further question
is the matter couplings of this theory. Since neither “very special geometry” [35, 36],
nor “quaternionic Kähler geometry” [29] arise naturally in our model via the gauge fixing
condition (4.1), it would be interesting to investigate how the scalars in the vector multiplet
and hypermultipet are constrained and what kind of geometries arise. Finally, we hope
to generalize our construction to D = 6, N = (1, 0) off-shell supergravity to derive the
supersymmetric completion of the Gauss-Bonnet combination in six dimensions.

Acknowledgements

We thank Frederik Coomans, Chris Pope for useful discussions and Ergin Sezgin for his
careful reading and useful remarks which help us improve this paper. Y.P. is supported in
part by DOE grant DE-FG03-95ER40917.

A     Notations and Conventions

In this paper, we use the conventions of [26]. The signature of the metric is diag(−, +, +, +, +).
The SU(2) indices are lowered or raised according to NW-SE convention

                                 Ai = εij Aj ,           Ai = Aj εji ,                    (A.1)

where ε12 = −ε21 = ε12 = 1. When SU(2) indices on spinors are suppressed, NW-SE
contraction is understood.
                                  ψ̄γ a1 ... an χ = ψ̄ i γ a1 ... an χi ,                 (A.2)

where γ a1 ...an is defined as
                                    γ a1 ·an = γ [a1 γ a2 ... γ an ] .                    (A.3)

Changing the order of spinors in a bilinear leads to the following signs

                                    ψ̄ i γ(n) χj = tn χ̄j γ(n) ψ i ,                      (A.4)

                                                   28
```

</details>

<a id="src-op-p029"></a>

<details>
<summary>OP-p029 — PDF page 29: Appendices: gamma/spinor and notation conventions</summary>

[OP-p029: PDF page 29](https://arxiv.org/pdf/1301.6622v4#page=29) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
where t0 = t1 = −t2 = −t3 = 1. We also used the following Fierz identity

                         ψj χ̄i = − 14 χ̄i ψj − 14 χ̄i γ a ψj γa + 18 χ̄i γ ab ψj γab .          (A.5)

The Levi-Civitá tensor is real and satisfies
                                                                          [r ... r ]
                          ǫp1 ...pn q1 ...qm ǫp1 ...pn r1 ...rm = −n!m!δ[q11... δqm
                                                                                  m
                                                                                    ].           (A.6)

Finally, the product of all gamma matrices is proportional to the unit matrix, and we use

                                             γ abcde = iǫabcde .                                 (A.7)

B     Multiplets of Five Dimensional Superconformal Gravity

In this appdendix, we give the SU(2) representations and Weyl weights of the fields appear-
ing in this paper.

                        Multiplet                 Field      SU(2) reps.        Weyl weight
                Dilaton Weyl Multiplet             eµ a             1                     -1
                                                    ψµi             2                     − 12
                                                    bµ              1                      0
                                                   Vµij             3                      0
                                                    Cµ              1                      0
                                                   Bµν              1                      0
                                                     σ              1                      1
                                                                                           3
                                                    ψi              2                      2

                     Vector Multiplet              Aµ               1                      0
                                                                                           3
                                                    λi              2                      2
                                                     ρ              1                      1
                                                   Y ij             3                      2
                     Linear Multiplet              Lij              3                      3
                                                                                           7
                                                    ϕi              2                      2
                                                    Ea              1                      4
                                                    N               1                      4

References

 [1] P. Candelas, G. T. Horowitz, A. Strominger and E. Witten, Vacuum Configurations
    for Superstrings, Nucl. Phys. B 258, 46 (1985).

                                                      29
```

</details>

### CO: cached source equations

Source PDF: 2013-Coomans-Ozkan-Internally-Gauged-D5-N2-Supergravity.pdf. SHA-256: `c65ea0f165ff73a9562a3acdde69c29b7af36206085ef1fa488a0d014c9f367d`.

<a id="src-co-p004"></a>

<details>
<summary>CO-p004 — PDF page 4: Weyl, vector and linear multiplet transformations and covariant structures</summary>

[CO-p004: PDF page 4](https://arxiv.org/pdf/1210.4704v3#page=4) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
an off-shell Lagrangian for 5D minimal supergravity in the background of a Dilaton Weyl
Multiplet in which the U (1) R-symmetry is gauged dynamically by the internal vector C,
i.e. the vector field C has a kinetic term in the Lagrangian. This forms a basis for a future
study of the Weyl squared invariant in a Dilaton Weyl background with the external vector
A replaced by the internal one C. A similar discussion in 4D can be found in [14].
    The paper is built up as follows. In section 2 we summarize the 5D superconformal cal-
culus and introduce the Standard Weyl Multiplet as well as two types of matter multiplets:
the Linear Multiplet and the Vector Multiplet. In section 3 we construct invariant actions
for the Linear and Vector Multiplet. In section 4 we construct 5D pure off-shell supergravity
by coupling the Standard Weyl Multiplet to a Linear compensator. This procedure is very
similar to the one used in 6D in [15]. We then add a superconformal abelian Vector Mul-
tiplet action to the Linear Multiplet action and compute the field equations for the Vector
Multiplet components. These equations allow us to solve for the matter fields of the Stan-
dard Weyl Multiplet (D, Tab χi ) in terms of the fields of the Vector Multiplet1 (σ, Cµ , ψ i )
plus an additional 2-form (Bµν ). Using these expressions in the Lagrangian we obtain the
action for the Linear Multiplet in the background of the Dilaton Weyl Multiplet. Gauge
fixing the redundant conformal symmetries leads to off-shell Poincaré supergravity which
has apart from the graviton and the gravitino, a vector field, a 2-form gauge field, a dilaton,
a symplectic Majorana spinor and a number of auxiliary fields.
    In section 5 we develop an off-shell method to gauge the theory. We start with an off-
shell action consisting of the Linear Multiplet action, the Vector Multiplet action and a
coupling between the Vector and Linear Multiplet, all in the background of the Standard
Weyl Multiplet. Then we compute, as in the ungauged case, the field equations for the
Vector Multiplet components to obtain expressions for the Standard Weyl matter fields.
We notice that these expressions get deformed by the Vector-Linear coupling. After using
these expressions in the Lagrangian and gauge fixing the conformal symmetries we obtain
an off-shell expression for U (1)-gauged supergravity. After eliminating the auxiliary fields
and dualizing the 2-form Bµν to a vector C̃µ , we show that the resulting theory is Einstein-
Maxwell supergravity gauged by a linear combination of Cµ and C̃µ . This theory agrees
completely with the one constructed in [3] via the Noether procedure. Finally, we show that
we can consistently eliminate σ, ψ and C̃µ . The resulting on-shell theory is minimal gauged
5D supergravity [3] consisting of the graviton, the graviphoton and the gravitino.

2       Superconformal Multiplets
In this section, we will recall the elements of N = 2, D = 5 superconformal tensor calculus
constructed in [8, 9]. In the first subsection 2.1 we introduce the gauge multiplet of the N =
2, D = 5 superconformal group: the Standard Weyl Multiplet. In the last two subsections,
2.2 and 2.3, we introduce two types of matter multiplets, the Vector Multiplet and the Linear
Multiplet.
    1
    We suggestively denote the fields of the Vector Multiplet with σ, Cµ and ψ i . The Vector Multiplet also
has an auxiliary Y ij , but we solve for this auxiliary and use its value in the expressions for D, Tab and χi .

                                                       4
```

</details>

<a id="src-co-p005"></a>

<details>
<summary>CO-p005 — PDF page 5: Weyl, vector and linear multiplet transformations and covariant structures</summary>

[CO-p005: PDF page 5](https://arxiv.org/pdf/1210.4704v3#page=5) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
2.1      The Standard Weyl Multiplet
The N = 2, D = 5 superconformal tensor calculus is based on the superconformal algebra2
F 2 (4) with the generators
                             Pa ,   Mab ,     D,     Ka ,       Uij ,     Qαi ,     Sαi ,                     (2.1)
where a, b, . . . are Lorentz indices3 , α is a spinor index and i = 1, 2 is an SU (2) index.
Here Mab and Pa are the usual Poincaré generators, D is the generator for dilatations, Ka
generates special conformal boosts, Uij is the SU (2) generator and Qαi and Sαi are the
supersymmetry and conformal supersymmetry generators respectively.
For each of the generators above we now introduce the following gauge fields
                       hµ A ≡ {eµ a ,     ωµ ab ,   bµ ,    fµ a ,      Vµij ,    ψµi ,   φiµ } ,             (2.2)
where µ, ν, . . . are world vector indices. Using the structure constants fAB C of the supercon-
formal algebra (given e.g. in appendix B of [8]) and the basic rules
                                        δhA       A   C B    A
                                          µ = ∂µ  +  hµ fBC ,
                                      Rµν A = 2∂[µ hA     C B     A
                                                    ν] + hν hµ fBC ,                                          (2.3)
one can easily write down the linear transformation rules and the linear curvatures Rµν A
of the superconformal gauge fields given in (2.2). The linear transformations given in [8]
satisfy the F 2 (4) superalgebra, thus resulting in a gauge theory of F 2 (4) since we have not
related the generators Pa , Mab to the diffeomorphisms of spacetime. This problem can be
solved by imposing the so-called curvature constraints [8]. These constraints determine the
gauge fields ωµ ab , φiµ and fµ a in terms of the independent gauge fields eµ a , ψµi , bµ , Vµij and,
in addition, achieve maximal irreducibility of the superconformal gauge field configuration.
    A simple counting argument shows that the superconformal gauge fields, after imposing
the conventional constraints, represent 21 + 24 off-shell degrees of freedom and therefore
cannot represent a supersymmetric theory. Additional matter fields Tµν (10), D(1) and χi (8)
must be added to the gauge fields in order to obtain an off-shell closed multiplet [8, 9]. This
multiplet is known as the Standard Weyl Multiplet.
    Starting from the linear transformation rules of the superconformal fields, the linear
curvatures Rµν A and the matter fields Tµν , D, and χi we can construct the full nonlinear
N = 2, D = 5 Weyl Multiplet by applying an iterative procedure (described in detail for 6
dimensions in [16]). The results are [8] (we only give Q, S and K transformations):
                   δeµ a =      1
                                2
                                  ¯γ a ψµ ,
                    δψµi =      (∂µ + 21 bµ + 41 ωµ ab γab )i − Vµij j + iγ · T γµ i − iγµ η i ,
                  δVµ ij =      − 32 i¯(i φj)   (i γµ χj) + i¯(i γ · T ψµj) + 32 iη̄ (i ψµj) ,
                                            µ + 4¯
                                1            3
                   δTab =       2
                                  i¯γab χ − 32 i¯R
                                                   bab (Q) ,
   2
      The notation F p (4) refers to a compact form of F (4) with bosonic subalgebra SO(7 − p, p).
   3
      We use the conventions of [8, 20]. In particular, the spacetime signature is (−, +, +, +, +) and ψ̄ i γ(n) χj =
tn χ̄ γ(n) ψ i with t0 = t1 = −t2 = −t3 = 1. When SU (2) indices on spinors are omitted, northwest-southeast
     j

contraction is understood.

                                                            5
```

</details>

<a id="src-co-p006"></a>

<details>
<summary>CO-p006 — PDF page 6: Weyl, vector and linear multiplet transformations and covariant structures</summary>

[CO-p006: PDF page 6](https://arxiv.org/pdf/1210.4704v3#page=6) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                    δχi =       1 i
                                4
                                   D − 64 1
                                             γ·R  bij (V )j + 1 iγ ab DT
                                                                  8
                                                                         / ab i − 18 iγ a Db Tab i
                               − 14 γ abcd Tab Tcd i + 61 T 2 i + 14 γ · T η i ,
                    δD =          / − 35 i¯γ · T χ − iη̄χ ,
                               ¯Dχ
                                1
                    δbµ =       2
                                  i¯φµ − 2¯γµ χ + 21 iη̄ψµ + 2ΛKµ ,                                           (2.4)

where

        Dµ χi = (∂µ − 72 bµ + 14 ωµ ab γab )χi − Vµij χj − 14 ψµi D + 64   1
                                                                             γ·R bij (V )ψµj
                − 18 iγ ab /
                          DTab ψµi + 18 iγ a Db Tab ψµi + 14 γ abcd Tab Tcd ψµi − 16 T 2 ψµi − 41 γ · T φiµ ,
     Dµ Tab = ∂µ Tab − bµ Tab − 2ωµ c [a Tb]c − 12 iψ̄µ γab χ + 32
                                                                3
                                                                   iψ̄µ R
                                                                        bab (Q) .                               (2.5)

The relevant modified curvatures are
    bµν ab (M ) = 2∂[µ ων] ab + 2ω[µ ac ων]c b + 8f[µ [a eν] b] + iψ̄[µ γ ab ψν] + iψ̄[µ γ [a γ · T γ b] ψν]
    R
                  +ψ̄[µ γ [a R
                             bν] b] (Q) + 1 ψ̄[µ γν] R
                                                 2
                                                     bab (Q) − 8ψ̄[µ eν] [a γ b] χ + iφ̄[µ γ ab ψν] ,
     bµν ij (V ) = 2∂[µ Vν] ij − 2V[µ k(i Vν] k j) −3iφ̄(i ψ j) − 8ψ̄ (i γν] χj) − iψ̄ (i γ · T ψ j) ,
     R                                                  [µ ν]        [µ               [µ         ν]
                                1
       bi (Q) = 2∂[µ ψ i + ω[µ ab γab ψ i + b[µ ψ i − 2V ij ψν]j − 2iγ[µ φi + 2iγ · T γ[µ ψ i .(2.6)
      R µν               ν]                   ν]          ν]      [µ                   ν]              ν]
                                2
As mentioned before, the dependent fields, which relate the generators Pa , Mab to the diffeo-
morphisms of spacetime, are completely determined by the following curvature constraints

                                                   Rµν a (P ) = 0 ,
                                             eν b R
                                                  bµν ab (M ) = 0 ,
                                                γ µR
                                                   bµν i (Q) = 0 .                                              (2.7)

Notice that our choices for the above constraints are not unique, i.e. one can impose different
constraints by adding further terms to (2.7). However such additional terms only amount
to redefinitions of the dependent fields defined below. Using the curvature constraints we
identify ωµ ab , φiµ and fµ a in terms of the other gauge fields and matter fields
                                   b]
           ωµ ab = 2eν[a ∂[µ eν] − eν[a eb]σ eµc ∂ν eσc + 2eµ [a bb] − 12 ψ̄ [b γ a] ψµ − 14 ψ̄ b γµ ψ a ,
                             0 i                     0 i
             φiµ = 13 iγ a R
                           bµa          1
                                 (Q) − 24 iγµ γ ab R
                                                   bab   (Q) ,                                                  (2.8)
               a       1     a     1  a
             fµ = − 6 Rµ + 48 eµ R ,

                0 ab                                          b0 (M ) and R
                                                                          b0 (Q) indicates that
where Rµν ≡ R bµρ    (M )eb ρ eνa and R ≡ Rµ µ . The notation R
we have omitted the fµ a dependent term in R(M b ) and the φi dependent term in R(Q).
                                                              µ
                                                                                    b      The
constraints imply through Bianchi identities further relations between the curvatures. The
Bianchi identities for R(P ) imply [8]

                Rµν = Rνµ ,             e[µ a R          b[µνρ] a (M ) ,
                                              bνρ] (D) = R                       R
                                                                                 bµν (D) = 0 .                  (2.9)

                                                          6
```

</details>

<a id="src-co-p007"></a>

<details>
<summary>CO-p007 — PDF page 7: Weyl, vector and linear multiplet transformations and covariant structures</summary>

[CO-p007: PDF page 7](https://arxiv.org/pdf/1210.4704v3#page=7) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
The full commutator of two supersymmetry transformations is
              [δQ (1 ), δQ (2 )] = δcgct (ξ3µ ) + δM (λab                    ij         a
                                                         3 ) + δS (η3 ) + δU (λ3 ) + δK (ΛK3 ) ,              (2.10)
where δcgct represents a covariant general coordinate transformation4 . The parameters ap-
pearing in (2.10) are
                            ξ3µ =     1
                                      2 2
                                         ¯ γ µ 1 ,
                           λab
                            3  =      −i¯2 γ [a γ · T γ b] 1 ,
                                          (i         j)
                           λij
                             3  =     i¯2 γ · T 1 ,
                              i
                            η3 =      − 49 i ¯2 1 χi + 74 i ¯2 γc 1 γ c χi
                                                                                    
                                               (i       j)
                                      + 41 i ¯2 γcd 1 γ cd χj + 41 R      bcd j (Q) ,
                                                     1 i abc j b
                         ΛaK3 = − 21 ¯2 γ a 1 D + 96 ¯2 γ 1 Rbcij (V )
                                + 12 i¯2 −5γ Db Tcd + 9Db T ba 1
                                   1              abcd
                                                                         

                                      +¯2 γ abcde Tbc Tde − 4γ c Tcd T ad + 23 γ a T 2 1 .
                                                                                       
                                                                                                              (2.11)
       For the Q, S commutators we find the following algebra
               [δS (η), δQ ()] = δD ( 12 i¯η) + δM ( 12 i¯γ ab η) + δU (− 32 i¯(i η j) ) + δK (Λa3K ) ,
             [δS (η1 ), δS (η2 )] = δK ( 12 η̄2 γ a η1 ) ,                                                    (2.12)
with
                                      Λa3K = 16 ¯ γ · T γ a − 12 γ a γ · T η .
                                                                           
                                                                                                              (2.13)
This concludes our review of the Standard Weyl Multiplet.

2.2       The Vector Multiplet
The off-shell abelian D = 5, N = 2 Vector Multiplet contains 8 + 8 degrees of freedom and
consists of the fields
                                    {Cµ , σ, Y ij , ψ i } ,                         (2.14)
with Weyl weights (0,1,2,3/2) respectively. The bosonic field content consists of a vector
field Cµ , a scalar field σ and an auxiliary field Y ij = Y (ij) , that is an SU(2) triplet. The
fermion field is given by an SU(2) doublet ψ i .
    The Q- and S-transformations of the Vector Multiplet, in the background of the Standard
Weyl Multiplet, are given by [7]
                     δCµ = − 12 iσ¯ψµ + 21 ¯γµ ψ ,
                     δY ij = − 21 ¯(i Dψ
                                       / j) + 12 i¯(i γ · T ψ j) − 4iσ¯(i χj) + 21 iη̄ (i ψ j) ,
                      δψ i = − 1 γ · G
                                      4
                                        b i − 1 iDσ
                                                 / i + σγ · T i − Y ij j + ση i ,
                                                    2
                                   1
                        δσ =       2
                                     i¯
                                       ψ.                                                                    (2.15)
   4
    The covariant general coordinate transformations are defined as δcgct (ξ) = δgct (ξ) − δI (ξ µ hIµ ), where the
index I runs over all transformations except the general coordinate transformations and the hIµ represent
the corresponding gauge fields.

                                                            7
```

</details>

<a id="src-co-p008"></a>

<details>
<summary>CO-p008 — PDF page 8: Weyl, vector and linear multiplet transformations and covariant structures</summary>

[CO-p008: PDF page 8](https://arxiv.org/pdf/1210.4704v3#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
We have used here the superconformally covariant derivatives
                 Dµ σ = (∂µ − bµ )σ − 12 iψ̄µ ψ ,
                Dµ ψ i = (∂µ − 23 bµ + 14 ωµ ab γab )ψ i − Vµij ψj
                               Gψµi + 1 i /
                         +1γ · b
                               4
                                           Dσψµi + Y ij ψµ j − σγ · T ψµi − σφi ,
                                             2                                          µ     (2.16)
and the supercovariant Yang-Mills curvature
                                bµν = Gµν − ψ̄[µ γν] ψ + 1 iσ ψ̄[µ ψν] ,
                                G                                                             (2.17)
                                                         2

where Gµν = 2∂[µ Cν] . The supersymmetry transformation rule for G
                                                                 bµν is given by

                bµν = − 1 iσ¯R
               δG             bµν (Q) − ¯γ[µ Dν] ψ + i¯γ[µ γ · T γν] ψ + iη̄γµν ψ .         (2.18)
                        2

This concludes our discussion on the Vector Multiplet.

2.3    The Linear Multiplet
The off-shell D = 5, N = 2 Linear Multiplet contains 8 + 8 degrees of freedom and consists
of the fields
                                   {Lij , E a , N, ϕi } ,                           (2.19)
with Weyl weights (3,4,4,7/2) respectively. The bosonic fields consist of an SU(2) triplet
Lij = L(ij) , a constrained vector Ea and a scalar N . The fermion field is given by an SU(2)
doublet ϕi . The Q and S supersymmetry transformations of the Linear Multiplet in the
background of the Standard Weyl Multiplet are given by
               δLij = i¯(i ϕj) ,
                             / ij j − 21 iγ a Ea i + 12 N i − γ · T Lij j + 3Lij ηj ,
                δϕi = − 21 iDL
               δEa = − 12 i¯γab Db ϕ − 2¯γ b ϕTba − 2η̄γa ϕ ,
                          / + 32 i¯γ · T ϕ + 4i¯i χj Lij + 32 iη̄ϕ ,
                δN = 21 ¯Dϕ                                                                  (2.20)
where we used the following superconformally covariant derivatives
         Dµ Lij = (∂µ − 3bµ )Lij + 2Vµ (i k Lj)k − iψ̄µ(i ϕj) ,
          Dµ ϕi = (∂µ − 27 bµ + 14 ωµ ab γab )ϕi − Vµij ϕj + 21 i /
                                                                 DLij ψµ j + 12 iγ a Ea ψµi
                      − 12 N ψµi + γ · T Lij ψµ j − 3Lij φµ j ,
          Dµ Ea = (∂µ − 4bµ )Ea + ωµab E b + 12 iψ̄µ γab Db ϕ + 2ψ̄µ γ b ϕTba + 2φ̄µ γa ϕ .   (2.21)
Finally, we note that the superconformal algebra closes if the following constraint is satisfied
                                           Da Ea = 0 .                                        (2.22)
The solution for Ea in terms of a 3-form Eµνρ is
                                E a = − 12
                                        1
                                           eµ a e−1 εµνρσλ Dν Eρσλ                            (2.23)

                                                   8
```

</details>

<a id="src-co-p016"></a>

<details>
<summary>CO-p016 — PDF page 16: Gauged map5.2–5.8 and explicit higher-fermion omission statement</summary>

[CO-p016: PDF page 16](https://arxiv.org/pdf/1210.4704v3#page=16) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
vector field of the Dilaton Weyl Multiplet Cµ . The fermions in the theory transform under
U (1)V , thus their covariant derivatives contain Vµ . This gauging by Vµ , however, is unde-
sirable since Vµ has no kinetic term. To obtain a dynamical gauging, one may choose to
eliminate Vµ and to promote, in the resulting on-shell theory, the vector field of the Dilaton
Weyl multiplet Cµ to a gauge field by replacing the covariant derivatives of the fermionic
fields with U (1)C covariant derivatives. Such a covariantization in the Lagrangian breaks
supersymmetry and hence g-dependent gauge invariant terms must be added to the La-
grangian in order to restore supersymmetry [3]. The necessary g-dependent gauge invariant
terms can be found by the Noether procedure. However, when considering more complicated
scenarios, such as the inclusion of R2 terms, the step-by-step Noether procedure is tedious
and cumbersome. Therefore, we devote this section to an easier procedure to construct the
internally gauged theory.
    In subsection 5.1 we add to the ungauged off-shell Lagrangian L0 (4.1) a vector-linear
coupling gLV L (3.1), where g is a coupling constant. We show that the expressions for the
Standard Weyl matter fields, obtained via the field equations of the Vector Multiplet com-
ponents, get deformed by g-dependent terms. In subsection 5.2 we discuss the elimination of
the auxiliaries Vµ , V 0ij
                        µ , N, Pµ and dualize the 2-form Bµν to a vector C̃µ . We show that the
resulting theory describes Einstein-Maxwell supergravity [3] in which a linear combination of
Cµ and C̃µ plays the role of the gauge field. Finally, in subsection 5.3, we show that we can
consistently truncate the matter content that is coupled to supergravity, thereby breaking
the gauge group down to a single U (1)R , gauged by Cµ , and obtain the minimal on-shell
gauged supergravity discussed [3].

5.1    The Off-shell Internally Gauged Supergravity
Our starting point for the construction of the internally gauged supergravity is the following
Lagrangian
                                        Lg ≡ L0 − 3gLV L
                                           = LL − 3LV − 3gLV L ,                                     (5.1)
where LL , LV and LV L are given in (3.7), (3.9) and (3.1). The field equations for Y ij , σ, ψ i
and Cµ give rise to the following map between the Standard Weyl Multiplet and the Dilaton
Weyl Multiplet
                       1 −1 i j
            Ygij =     4
                         iσ ψ̄ ψ − 21 gσ −1 Lij ,                                                    (5.2)
                       1 −1 / i
             χig   =   8
                         iσ Dψ + 161
                                      iσ −2 Dσψ   1 −2
                                            / i − 32 σ γ · Gψ i
                                                             1
                     + 41 σ −1 γ · T ψ i + 18 σ −2 Y ij ψj + gσ −2 ϕi ,                              (5.3)
                                                             8
            Dg     = 14 σ −1 2c σ + 18 σ −2 (Da σ)(Da σ) − 16  1 −2
                                                                σ Gµν Gµν
                     − 18 σ −2 ψ̄ Dψ
                                  / + 41 σ −2 Y ij Yij − 4iσ −1 ψ̄χ + 18 σ −2 ψ̄µ γν ψGµν
                                                                                           
                     − 161
                           iσ −1 ψ̄µ ψµ Gµν + − 26        T
                                                        3 ab
                                                             + 2σ −1 b
                                                                    G  ab + 1 −2
                                                                            4
                                                                              iσ    ψ̄γab ψ   T ab
                       + 14 gσ −2 N ,                                                                (5.4)

                                                     16
```

</details>

<a id="src-co-p017"></a>

<details>
<summary>CO-p017 — PDF page 17: Gauged map5.2–5.8 and explicit higher-fermion omission statement</summary>

[CO-p017: PDF page 17](https://arxiv.org/pdf/1210.4704v3#page=17) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
                                                3 b  b + 1 gD[a Ebcd] ,
                              D[a H
                                  bbcd] =        G G
                                                4 [ab cd] 2
                                                                                                              (5.5)
where
                                       b edc = 8σ 2 Tab − σ G
                           − 61 εabcde H                    bab − 1 iψ̄γab ψ .                                (5.6)
                                                                  4
The subscript g in the equations (5.2), (5.3) and (5.4) indicates that the expressions for
Y ij , χi and D now pick up g dependent terms. Note that the expressions for χig and Dg are
given up to 3- and 4-fermion terms respectively. Comparing the above map with the one
in the ungauged case, (4.4) to (4.6), it is clear that the map gets deformed by the gauging.
The Bianchi identity (5.5) implies that
            bµνρ = 3∂[µ Bνρ] + 3 C[µ Gνρ] + 1 gEµνρ − 3 σ 2 ψ̄[µ γν ψρ] − 3 iσ ψ̄[µ γνρ] ψ .
            H                                                                                                 (5.7)
                               2            2         4                   2

The above equation for H bµνρ is clearly not gauge invariant since Eµνρ has the gauge invariance
δΛ Eµνρ = 3∂[µ Λνρ] . In order to balance that out, Bµν needs to have the additional gauge
invariance
                            δΛ Bµν = 2∂[µ Λν] − 21 ΛGµν − 12 gΛµν .                                           (5.8)
   Using the above expressions for Y ij , D, Tab and χi in the Lagrangian (5.1) and imposing
the gauge fixing conditions (4.13) we obtain the following off-shell Poincaré Lagrangian
e−1 Lg,DW |L=−1 =     1
                      2
                        R − 41 σ −2 Gµν Gµν − 2gCµ P µ − 61 σ −4 Hµνρ Hµνρ − N 2 − gN (σ −2 + 2σ)
                                                               √
                      −g 2 ( 41 σ −4 − σ −1 ) + P µ Pµ + 2P µ Vµ − Vµ0 ij Vµij          0
                                                                                            − 23 σ −2 ∂µ σ∂ µ σ
                      − 12 ψ̄µ γ µνρ Dν ψρ − 23 σ −2 ψ̄ D / 0 ψ − 32 iσ −2 ψ̄γ µ γ ρ ψµ ∂ρ σ
                      − 81 iσ −1 ψ̄µ γ µνρσ ψν Gρσ − 41 iσ −1 ψ̄µ ψν Gµν − 14 σ −2 ψ̄µ γ µνρ ψGνρ
                      + 21 σ −2 ψ̄µ γν ψGµν − 18 iσ −3 ψ̄γ · Gψ + 2√1 2 ψ̄µi γ µνρ ψνj Pρ δij
                          1 −2
                      − 24  σ ψ̄µ γ µνρσλ ψν Hρσλ + 14 σ −2 ψ̄µ γν ψρ Hµνρ
                      − 16 iσ −3 ψ̄µ γ µνρσ ψHνρσ + 12 iσ −3 ψ̄µ γνρ ψHµνρ − 24           5 −4
                                                                                            σ ψ̄γ · Hψ
                                   −2
                      + 4√2 igσ ψ̄µ γ ψν δij + 2√2 igσ ψ̄µ γ ψν δij − √2 g ψ̄µi γ µ ψ j δij
                           1            i  µν    j         1         i   µν    j          1

                      + √12 gσ −3 ψ̄µi γ µ ψ j δij − 4√1 2 igσ −1 ψ̄ i ψ j δij − 4√5 2 igσ −4 ψ̄ i ψ j δij ,    (5.9)
where Hµνρ is defined as
                            Hµνρ = Bµνρ + 32 C[µ Gνρ] + 12 gEµνρ .                                           (5.10)
This Lagrangian is invariant under the transformation rules given in (4.20), where the un-
derlined fields are now to be evaluated using the deformed expressions, (5.2) to (5.6).
    This theory has a U (1)V × U (1)C gauge group parametrized by λ and η respectively. The
fermion covariant derivatives are defined in (4.18) and contain Vµ . The gauge transformations
of the relevant fields are given by
                           δλ Vµ = ∂µ λ ,     δη Cµ = ∂µ η ,
                               i       ij
                                   1
                           δλ ψµ = 2 λδ ψµj ,      δλ ψ i = 12 λδ ij ψj .                                    (5.11)

                                                     17
```

</details>

### OPall: cached source equations

Source PDF: 2013-Ozkan-AllOfShellR2.pdf. SHA-256: `6d52227f31e9f047b09dc51ff01dea1891a3ab4c7aaa35301100ac0c7039b91c`.

<a id="src-opall-p008"></a>

<details>
<summary>OPall-p008 — PDF page 8: 3.1–3.2: operational E_a density and P/E completion</summary>

[OPall-p008: PDF page 8](https://arxiv.org/pdf/1306.1540v3#page=8) (source locator)

Layout text for searching; the image controls mathematical transcription.

```text
Therefore Ea can be solved in terms of a 3-form Eµνρ as
                                   E a = − 12
                                           1
                                              eµ a e−1 εµνρσλ Dν Eρσλ .                                       (2.17)
Similar to the vector multiplet, if the dilaton Weyl multiplet is adopted, the supersymmetry trans-
formation rules for the linear multiplet can be obtained by using the map (2.9).

3     Superconformal Actions
In this section, we review the superconformal actions for the matter multiplets coupled to the
standard Weyl multiplet and the dilaton Weyl multiplet, which give rise to different formulations
of off-shell Poincaré supergravities. These actions include a linear multiplet action [19, 23] and
three vector multiplet actions. The first vector multiplet action describing n number of vector
multiplets coupled to the standard Weyl is treated as the master action from which we derive the
other two actions for n number of vector multiplets coupled to the dilaton Weyl multiplet.
    The starting point for the constructions of the linear and vector multiplet actions is the super-
conformal density formula [17]
                                                      1
                        e−1 LV L = Y ij Lij + iλ̄ϕ − ψ̄ai γ a λi Lij + Aa P a
                                                      2
                                              1           1               
                                      +ρ N + ψ̄a γ a ϕ + iψ̄ai γ ab ψbj Lij ,                                  (3.1)
                                               2           4
where Pa is the bosonic part of the supercovariant field strength Ea
                                           1             1
                                P a = E a + iψ̄b γ ba ϕ + ψ̄bi γ abc ψcj Lij .                                 (3.2)
                                           2             4

3.1   The Linear Multiplet Action
The procedure of constructing an action for the linear multiplet is based on superconformal tensor
calculus, where the fields of vector multiplets are composed in terms of the fields in linear multiplet
and a Weyl multiplet. The construction of a linear multiplet action is explored in detail by [19, 23].
Here we only present the results which contribute to the purely bosonic action. Using the linear
multiplet and the standard Weyl multiplet, the elements of vector multiplet can be composed as
given in (A.2). Inserting the composite expressions into the vector-linear action (3.1), one can
obtain an action for the linear multiplet,
                 e−1 LSL = L−1 Lij 2c Lij − Lij Dµ Lk(i Dµ Lj)m Lkm L−3 + N 2 L−1
                               −Eµ E µ L−1 + 83 LT 2 + 4DL − 12 L−3 E µν Llk ∂µ Lkp ∂ν Lpl
                               +2E µν ∂µ (L−1 Eν + Vνij Lij L−1 ) ,                                            (3.3)
where we have defined L2 = Lij Lij and the superscript S indicates that this action utilizes the
standard Weyl multiplet. The superconformal d’Alembertian of Lij is given by
             Lij 2c Lij   = Lij (∂ a − 4ba + ωb ba )Da Lij + 2Lij Va i k Da Ljk + 6L2 fa a
                              −iLij ψ̄ ai Da ϕj − 6L2 ψ̄ a γa χ − Lij ϕ̄i γ · T γ a ψaj + Lij ϕ̄i γ a φja .    (3.4)
   The linear multiplet action (3.3) can be transferred to an action describing the linear multiplet
coupled to the dilaton Weyl multiplet by replacing the Tab , D and χi by their composite expressions
according to (2.9) in the action (3.3).

                                                          8
```

</details>
