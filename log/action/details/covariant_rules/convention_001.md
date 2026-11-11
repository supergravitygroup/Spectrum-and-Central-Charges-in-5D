# Conventions and source equations: full fermionic gauged LOG invariant — LOG-P01 – C24-Table6

<a id="conventions-and-source-equations-full-fermionic-gauged-log-invariant--conventions-and-source-equations-full-fermionic-gauged-log-invariant"></a>

[Component index](../covariant_rules.md).

## Conventions and source equations: full fermionic gauged LOG invariant

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Supercovariant derivative convention.** Use the full supercovariant $`\mathcal D_a`$ and the conformal box $`\Box^c=\mathcal D^a\mathcal D_a`$, exactly as in the [fermionic gauged Weyl-squared calculation](../../../../weyl2/action/details/construction.md), GC14–GC24. Its Q/S/K and implicit fermionic contributions stay inside the operators. Gauge evaluation follows each ordered differentiation; derivatives of the fixed dilaton/dilatino are not silently set to zero. The [active LOG endpoint](../construction.md) uses this policy. Gold superspace source formulas retain $`\nabla_A`$ until the complete bridge is applied.

**Reference lock:** `GAUGED-LOG-CONVENTIONS-v1` · **2026-09-22**.
**Procedure lock:** `GAUGED-LOG-G25-S23-PROCEDURE-v1`.

This is the reusable calculation reference for the locked procedure. It contains
equations, not only citations: transcribed working relations first, followed by
the complete cached source equations needed for the long component expressions.
The searchable source transcriptions below retain equation and page locators.
For exact index placement, consult the corresponding published source in the [bibliography](../../../../references/bibliography.md).

The lock establishes notation, provenance, source equations and permitted
conversions. The checked identities and their fermion orders are specified
in the associated construction records. Printed formulas and project-derived
repairs remain explicitly distinguished.

The separate [LOG working conventions and step 1 derivation](../component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md)
record the checked covariant four-slot Q/S map, six nonform BF terms, bosonic
normalization and explicit chi-curvature reconciliation. The [full superform derivation](../../../../references/source_evidence/log/derivations/form-interface.md)
now resolves the generic current/potential/BF interface for a genuine linear
multiplet, with explicit repairs of the incompatible printed formulas. This main
file preserves literal source formulas; the working ledger distinguishes those
from derived repairs and from verification of the particular LOG polynomials. The source's convention-check script is not supplied as a runnable module here.

**Retained-order construction.** The current construction through two physical fermions is certified in [CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md](../component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The full primary, retained descendants, projection, canonicalization, reality, current/BF interface and complete bosonic comparison pass. Higher-fermion action terms and independent all-order gauge-algebra closure remain outside that certificate. The certificate specifies which component expressions and checks support this scope.

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
| LOG-S1-01–LOG-S1-24 in [LOG_CONVENTIONS.md](../component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md) | Derived step 1 bridge, density comparison, curvature reconciliation and current/potential diagnostics |
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
6. L04 is a recorded source conflict, not an adopted pair of potential laws.
   For density insertion the operational constrained-vector route A02 is
   available. A full SUSY variation of the gauged H potential still requires
   the linear-potential interface derived by the full-superform calculation.
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

<a id="2-geometry-and-the-meaning-of-a-derivative"></a>

## Geometry and the meaning of a derivative

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
The source constraint consequences include $`\widehat R(D)=0`$ and the full Lorentz-curvature Bianchi identity. They do **not** justify symmetrizing the locked full primed Ricci $`\mathcal R_{\mu\nu}`$ in R03 or its dependent $`f_{ab}`$ at fermionic order. The earlier local statement doing so was corrected by the [ordered-connection audit](../component_construction/results/gauged_full_fermionic_log/sources/step7/supercovariant/equivalence/README.md); only the bosonic specialization used there is symmetric. Keep the primed Ricci and $`f`$ indices ordered.
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

<a id="3-weyl-transformations-and-component-derivatives"></a>

## Weyl transformations and component derivatives

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

<a id="4-connections-curvatures-and-their-variations"></a>

## Connections, curvatures and their variations

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

<a id="5-gauge-forms-and-full-ungauged-dw-composites"></a>

## Gauge forms and full ungauged DW composites

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

<a id="6-linear-and-defining-vector-multiplets"></a>

## Linear and defining-vector multiplets

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

### X11 — R05 index ordering and S-invariance

W(3.23), printed p.21/PDF p.22, fixes the R05 ordering as
$`+\frac{16}{3}T_{[a}{}^c\gamma_{b]c}\eta^i`$.
The alternative ordering
$`+\frac{16}{3}T^c{}_{[a}\gamma_{b]c}\eta^i`$
has the opposite sign because
$`T_a{}^c=\eta^{cd}T_{ad}=-\eta^{cd}T_{da}=-T^c{}_a`$.
The adopted ordering preserves $`\gamma^a\delta_S\widehat R_{ab}(Q)=0`$
and the cancellation in $`\delta_S L^{ij}`$. The [fermionic-map derivation](../../../../computations/weyl_fermionic/derivations/fermionic-map.md)
and [S-invariance checker](../../../../computations/weyl_fermionic/src/reference_checks/verify_weyl_map_s_invariance.py) give the algebra and the opposite-sign control.

## Gauged realization of the shared component covariants

Use these instead of the ungauged realization when g is nonzero. The project-derived full restoration is shown in GC01–GC24 below; its use in the Gold LOG multiplet is through the explicit source-frame bridge.

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

<a id="31-primary-source-inputs-and-their-exact-scope"></a>

### Primary source inputs and their exact scope

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

<a id="32-the-density-bridge-and-gauged-defining-vector"></a>

### The density, bridge and gauged defining vector

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

<a id="4-detailed-derivation"></a>

## Detailed Derivation

<a id="41-solve-the-lowest-gauged-constraint-and-vary-it"></a>

### Solve the lowest gauged constraint and vary it

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

<a id="42-solve-the-spinor-constraint-including-its-cubic-term"></a>

### Solve the spinor constraint, including its cubic term

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

<a id="43-solve-the-scalar-constraint-and-expand-every-y-product"></a>

### Solve the scalar constraint and expand every Y product

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

<a id="44-solve-the-tensor-relation-and-check-the-form-gauge-symmetry"></a>

### Solve the tensor relation and check the form gauge symmetry

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

<a id="45-propagate-the-gauging-through-derivatives-and-connections"></a>

### Propagate the gauging through derivatives and connections

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
| S23 | [Gold et al., superspace paper](../component_construction/EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8) | arXiv:2302.14295v2. `PDF n` means the one-based page in this local file; printed page is usually `n-1`. |
| C24 | [Gold et al., component paper and supplement](../component_construction/EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4) | Local combined PDF contains arXiv:2311.00679v1, subsequently published in JHEP 07 (2024) 221. Main printed page is `PDF-1`; supplement printed page is `PDF-99`. |

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

This is a project-derived correction, not a claim of a published erratum. The independent exact test exhausts 122,880 coefficient equations in the linear Weyl-descendant sector: the corrected coefficients pass and the printed coefficients fail. See [source-local Jacobi checks](../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/curved/jacobi-SDD-checks.json). It affects S acting on vector descendants, even when their elementary parent is K-primary. The scalar/vector reconstruction uses this corrected relation; it does not import the different frame-dependent $`WS`$ coefficient from the older source.

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

[Component index](../covariant_rules.md) · [Next component](derivation_002.md)
