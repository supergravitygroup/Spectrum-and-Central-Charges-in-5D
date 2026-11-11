# Anchored conventions for the full fermionic GB spectrum

**Lock:** `GB-FERMION-SPECTRUM-CONVENTIONS-v1`. **Date:** 2026-09-28.
**Scope:** shared geometry and fermion calculus, source gauge, GB normalization,
and spectrum conventions. The [action](../../../action/gb_splus_action.md) is now
assembled through two physical fermions from its adopted inputs; its separate
action lock retains their verification qualifications. No background is certified.

**Reference revision 2:** the full local [component convention reference](COMPONENT_CONVENTIONS.md)
now displays the fields, variations, curvatures and supercovariant derivatives
explicitly. Its [relation index](COMPONENT_INDEX.md) and
extraction manifest preserve the source locations
and exact equation bodies. The physical convention lock is unchanged.

## 1. Authority and detailed references

The detailed common authority is the current
[LOG master](LOG_MASTER.md),
`GAUGED-LOG-CONVENTIONS-v1`, including its 2026-09-25 corrections.
The [LOG working conventions](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md),
`GAUGED-LOG-STEP1-v1`, fix the once-only component bridge and BF current.
The [Weyl master](WEYL_MASTER.md),
`UNG-WEYL2-OP58-CONVENTIONS-v5`, is the common component-calculus donor;
its invariant-specific map retains its own qualifications.

The component inputs are identified in the
dated input snapshot. The manifest pins original
paths, snapshots and SHA-256 hashes. The concise formulas below are a
working guide to stable relation IDs, not a replacement for the masters'
full connections, transformations and cached source equations.

| Topic | Detailed relation/source anchor |
|---|---|
| Geometry, spinors, gamma algebra, Fierz, weights | LOG C01–C06; 5D Weyl paper Appendix A (A.1)–(A.17), Table 7 |
| Derivatives, curvature, conventional constraints | LOG G01–G04, W01–W04, R01–R07; OP (2.1)–(2.12), Weyl paper (3.9), (3.17), (3.20) |
| Forms, composites, linear/vector multiplets and density | LOG H01–H03, D01–D02, L01–L04, V01–V03, A01–A02, with X01–X11 repairs |
| Complete gauged realization | LOG GG01–GG05 and GC01–GC24; Weyl gauged calculation GC01–GC24; CO (5.2)–(5.8), W (5.10)–(5.14) |
| Gold/component conversion | LOG C24 Tables 4–6 and LOG-S1-02–12; C24 Appendix C, PDF pp.90–92 |
| Current and BF interface | LOG-S1-06, 16–21; current LOG certificate and superform derivation |
| Target source gauge | LOG-G01–G05; G25 (7), (25), (27); OP (4.1)–(4.2) |
| GB definition and bosonic normalization | G25 (22)–(23), PDF p.13; project `GB-WEYLOG-DEF-v1` |
| Fermionic variation and spectral bookkeeping | LOG spectrum file 04 §1, §§7–11, as a convention/method reference only |

`W` denotes the local 5D Weyl-multiplet paper; `OP` the corrected local
Özkan–Pang GB paper; `CO` Coomans–Özkan; `S23`, `C24`, `G25` the Gold
superspace, component and 2025 papers. Exact filenames are in SOURCE_LOCK.md.

## 2. Geometry, orientation and curvature

Use natural units, five-dimensional Lorentzian spacetime and eight real
supercharges. The source labels N=1 (Gold) and N=2 (component literature)
refer to the same minimal supersymmetry here.

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\quad
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab},\quad
e=\det(e_\mu{}^a)>0.
\tag{GB-C01}
```

World indices are Greek, tangent indices Latin, both ranging from 0 to 4;
SU(2) indices are $`i,j=1,2`$. Brackets have unit weight:
$`X_{[ab]}=(X_{ab}-X_{ba})/2`$; higher brackets include $`1/p!`$.

```math
\epsilon^{01234}=+1,\quad \epsilon_{01234}=-1,\quad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
\epsilon^{abcdf}=e^{-1}[\mu\nu\rho\sigma\lambda].
\tag{GB-C02}
```

The square-bracket object is the alternating coordinate symbol,
$`[01234]=+1`$. Frame conversion of the tensor has no additional determinant.
This is the LOG C01 tensor/density convention.

```math
R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\qquad
R_{\mu\nu\rho\sigma}=R_{\mu\nu}{}^{ab}e_{\rho a}e_{\sigma b},
\tag{GB-C03}
```
```math
R_{\mu\nu}=R_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a},\qquad
R_{\mu\nu\rho\sigma}=k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})
\ \Longrightarrow\ R_{\mu\nu}=4kg_{\mu\nu},\quad R=20k.
\tag{GB-C04}
```

These are LOG G02. On a torsion-free bosonic background,
$`[\nabla_\mu,\nabla_\nu]\zeta=R_{\mu\nu}{}^{ab}\gamma_{ab}\zeta/4`$.
If AdS5 is selected, define its radius by $`k=-\ell^{-2}`$, hence
$`[\bar\nabla_a,\bar\nabla_b]\zeta=-\gamma_{ab}\zeta/(2\ell^2)`$.
This defines signs and units only; no $`\ell(g,\lambda_{\rm GB})`$ or vacuum
expectation value is assumed. Bosonic Riemann symmetries must not be imposed
on arbitrary fermionic hatted curvatures.

## 3. Spinors, gamma matrices and SU(2)

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\ldots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]},\qquad
\gamma^{01234}=i\mathbf1,\qquad
\gamma\!\cdot\!T=\gamma^{ab}T_{ab}.
\tag{GB-C05}
```

Dots are full ordered-index contractions with no extra $`1/p!`$.
Use $`\not{\mathcal D}=\gamma^a\mathcal D_a`$.
The matrices $`\gamma_0`$ and the spatial gammas are respectively
anti-Hermitian and Hermitian. Five dimensions has no chirality projection
to import from six dimensions.

```math
\bar\zeta^{\,i}=(\zeta^i)^T\mathsf C,\qquad
\mathsf C^T=-\mathsf C,\qquad
(\mathsf C\gamma_a)^T=-\mathsf C\gamma_a,\qquad
\mathsf C^\dagger\mathsf C=1.
\tag{GB-C06}
```

Use LOG C03's symplectic Majorana condition, with $`B=\mathsf C\gamma_0`$,
$`\alpha=1`$ and complex conjugation not reversing odd-factor order:
$`\zeta^i=B^{-1}\varepsilon^{ij}(\zeta^j)^*`$.
The operational bar is linear, $`\overline{i\zeta}=i\bar\zeta`$.
All physical spinors and SUSY parameters are Grassmann odd;
parameter-contracted SUSY variations and spacetime derivatives are even.

```math
X^i=\varepsilon^{ij}X_j,\qquad X_i=X^j\varepsilon_{ji},\qquad
\varepsilon_{12}=\varepsilon^{12}=1,\qquad
\bar u\Gamma v=\bar u^i\Gamma v_i.
\tag{GB-C07}
```

Lower each index separately, preserving order. In particular
$`\bar u_i\Gamma v^i=-\bar u^i\Gamma v_i`$.
For fixed upper doublet indices and then for contracted bilinears:

```math
\bar u^i\gamma_{(n)}v^j=t_n\bar v^j\gamma_{(n)}u^i,
\quad (t_0,t_1,t_2,t_3)=(1,1,-1,-1),\qquad
\bar u\gamma_{(n)}v=-t_n\bar v\gamma_{(n)}u.
\tag{GB-C08}
```

The extra contracted minus is essential. LOG C04–C05 supplies duality,
gamma products, full-index sandwich coefficients and the Fierz formula

```math
\psi_j\bar\lambda^i=-\frac14(\bar\lambda^i\psi_j)\mathbf1
-\frac14(\bar\lambda^i\gamma^a\psi_j)\gamma_a
+\frac18(\bar\lambda^i\gamma^{ab}\psi_j)\gamma_{ab}.
\tag{GB-C09}
```

Use these with the actual spinor order displayed at every application.

## 4. Fields, gauge and supercovariant differentiation

| Object | Role |
|---|---|
| $`e_\mu{}^a,\psi_\mu^i`$ | Vielbein and independent gravitino |
| $`\sigma,C_\mu,\psi^i,B_{\mu\nu}`$ | Dilaton-Weyl fields; $`\psi^i`$ is the dilatino |
| $`L_c^{ij},\varphi_c^i,N_c,E_{c\mu\nu\rho}`$ | Independent linear compensator and constrained-form potential |
| $`V_\mu,V_\mu'{}^{ij}`$ | Trace and traceless R-symmetry connections |
| $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$ | Dependent Lorentz, S and K connections |
| $`T_{ab},\chi^i,D,Y^{ij}`$ | Gauged Dilaton-Weyl composites, not additional independent fermions |
| $`L_W,\varphi_W,E_W,N_W`$ and $`L_{\log},\varphi_{\log},E_{\log},N_{\log}`$ | Distinct composite linear multiplets; neither is the compensator |

On a local positive dilaton patch and nonzero compensator patch, inherit

```math
\sigma=1,\quad b_\mu=0,\quad\psi^i=0,\quad
L_c^{ij}=\frac{\delta^{ij}}{\sqrt2}L,\quad
V_a^{ij}=V_a'{}^{ij}+\frac12\delta^{ij}V_a,\quad
\delta_{ij}V_a'{}^{ij}=0.
\tag{GB-C10}
```

This does not set $`L=1`$, $`N_c=0`$, $`\varphi_c=0`$, or $`V'=0`$.
The independent fermions after this source gauge are $`\psi_\mu^i`$ and
$`\varphi_c^i`$. Later gamma-trace/transverse conditions are fluctuation
gauges or derived constraints and require a separate analysis.

Use the full definition, LOG G01,

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-
\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi-
\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi-
\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,
\quad \mathcal D_a=e_a{}^\mu\mathcal D_\mu,\quad
\Box^c=\mathcal D^a\mathcal D_a.
\tag{GB-C11}
```

On a doublet of weight $`w`$, the bosonic part is
$`D_\mu^{(0)}\zeta^i=(\partial_\mu-wb_\mu+\omega_\mu{}^{ab}\gamma_{ab}/4) \zeta^i-V_\mu{}^{ij}\zeta_j`$.
The full second derivative includes the S/K transformations of the first
derivative. Evaluate the source gauge after each ordered differentiation.
LOG-G02a explicitly gives

```math
\mathcal D_\mu\psi^i\big|_{\rm gauge}
=\frac14\gamma\!\cdot\!\widehat G\,\psi_\mu^i
-\frac g2 L_c^{ij}\psi_{\mu j}
-\gamma\!\cdot\!T\,\psi_\mu^i-\phi_\mu^i.
\tag{GB-C12}
```

The conventional constraints $`R(P)=0`$, $`\gamma^\mu\widehat R_{\mu\nu}(Q)=0`$,
and $`e_b{}^\nu\widehat R_{\mu\nu}{}^{ab}(M)=0`$ define the dependent
connections; they are not target-action auxiliary EOM. Preserve gravitino
contorsion and the order of primed Ricci/$`f_{ab}`$ indices.

<a id="lowered-linear-derivatives"></a>

### 4.1 Lower-index linear-multiplet derivatives

**Explicit lowering note, 2026-10-13.** The already established lowering
correction is recorded explicitly here. Its derivation is in
the two-derivative action, §3.3,
anchored there to source Eq. (2.19). This is a consequence of the existing
NW--SE convention, not a change of convention or a correction to the
upper-index source formula in component entry L02.

Here $`(L^{ij},\varphi^i,E_a,N)`$ denotes a generic linear multiplet; for the
independent compensator attach the subscript $`c`$. With
$`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$ and
$`\varepsilon_{12}=\varepsilon^{12}=1`$, symmetric $`L^{ij}`$ obeys

```math
L^{rj}\varepsilon_{ri}\Psi_j
=L_{i\ell}\varepsilon^{j\ell}\Psi_j
=-L_{i\ell}\varepsilon^{\ell j}\Psi_j
=-L_{ij}\Psi^j.
\tag{GB-C12a}
```

Since $`\mathcal D_\mu\varepsilon_{ij}=0`$, the same identity applies to
$`\mathcal D_\mu L^{ij}`$. The fully lowered derivatives are

```math
\mathcal D_\mu L_{ij}=(\partial_\mu-3b_\mu)L_{ij}
+2V_{\mu(i}{}^kL_{j)k}-i\bar\psi_{\mu(i}\varphi_{j)}.
\tag{GB-C12b}
```

```math
\begin{aligned}
\mathcal D_\mu\varphi_i={}&
\left(\partial_\mu-\frac72b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi_i-V_{\mu i}{}^j\varphi_j\\
&-\frac i2\not{\mathcal D}L_{ij}\psi_\mu{}^j+\frac i2\gamma^aE_a\psi_{\mu i}-\frac12N\psi_{\mu i}\\
&-\gamma\!\cdot\!T\,L_{ij}\psi_\mu{}^j+3L_{ij}\phi_\mu{}^j.
\end{aligned}
\tag{GB-C12c}
```

In particular, lowering the free index of $`\mathcal D_\mu\varphi^i`$
changes the signs of its three triplet-contracted terms as follows:

```math
\begin{aligned}
+\frac i2\not{\mathcal D}L^{rj}\psi_{\mu j}\varepsilon_{ri}&=-\frac i2\not{\mathcal D}L_{ij}\psi_\mu{}^j,\\
+\gamma\!\cdot\!T\,L^{rj}\psi_{\mu j}\varepsilon_{ri}&=-\gamma\!\cdot\!T\,L_{ij}\psi_\mu{}^j,\\
-3L^{rj}\phi_{\mu j}\varepsilon_{ri}&=+3L_{ij}\phi_\mu{}^j.
\end{aligned}
\tag{GB-C12d}
```

Thus the remembered sign correction concerns, in particular, the
$`\not{\mathcal D}L`$ term inside $`\mathcal D_\mu\varphi_i`$; it does not
justify reversing the displayed connection term in
$`\mathcal D_\mu L_{ij}`$. The mixed-index connection is
$`V_{\mu i}{}^j=V_\mu{}^{rj}\varepsilon_{ri}`$, and
$`\phi_\mu{}^i`$ is the dependent S connection, distinct from $`\varphi^i`$.

## 5. Forms and the BF current

For the bosonic restriction only, LOG-G04 fixes

```math
G=dC,\qquad H_3=dB+\frac12C\wedge G+\frac g2E_{c3},\qquad
H^{ab}=-\frac1{12}\epsilon^{abcde}H_{cde},\qquad
H_{abc}=\epsilon_{abcde}H^{de}.
\tag{GB-C13}
```

Thus $`H_2=-\tfrac12\star H_3`$ in this convention. Potentials, constrained
field strengths, ordinary strengths and their supercovariant completions
must stay distinct. Use the full H/G definitions in the donor when retaining
fermions, rather than inserting this bosonic restriction prematurely.

For a generic linear multiplet the ordinary conserved current is

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},\qquad
P^a=-\frac1{12}e_\mu{}^a\epsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}.
\tag{GB-C14}
```

Use $`A_aP^a`$ in the ordinary-current BF density (LOG-S1-16), not $`A_aE^a`$.
The current and potential repairs are derived in the current LOG certificate;
the older source-literal potential formulas remain comparison records.

## 6. Source-frame bridge and corrections

Raw Gold gamma matrices are not the project matrices:
$`\Gamma_G^a=i\gamma^a`$, $`\Sigma_G^{ab}=\gamma^{ab}/2`$,
$`\epsilon_G^{abcde}=-\epsilon^{abcde}`$.
Use **all** C24 Tables 4–6 and LOG-S1-02–04, including the shifted S/K
connections and parameters, when converting. A name-only relabeling fails.

The generic linear-slot conversion is applied once:

```math
G_G^{ij}=-\frac12L^{ij},\qquad \varphi_G^i=\frac i2\varphi^i,
\qquad F_G=-N,\qquad \mathcal H_G^a=E^a.
\tag{GB-C15}
```

Already projected LOG components must not be multiplied by these factors
again. They do not determine a separate invariant's overall normalization.

Carry forward the explicit repair ledger: LOG X01's $`+8\bar\psi e\gamma\chi`$
term in the ordered primed Lorentz curvature, X02's $`w(\chi)=3/2`$,
X09's tensor-derivative sign, X11's corrected curvature variation,
the LOG gradient-X coefficient $`+i/4`$, the C24 (A.1l) K-generator repair,
and the current/form correction in the 2026-09-25 certificate. Source images
retain the printed formulas. These are labeled project-derived repairs.
The Weyl map's adopted $`8/3`$ coefficient is a separate Weyl-specific result;
it does not become a LOG-primary rule or a completed GB SUSY certificate.

## 7. Action normalization and dimensions

The intended total action is

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e
\left(\ell_{2\partial}+\lambda_{\rm GB}\ell_{\rm GB}\right),\qquad
\ell_{\rm GB}:=\ell_{\rm Weyl^2}-4\ell_{\rm LOG},\qquad
2\kappa_5^2=16\pi G_5.
\tag{GB-C16}
```

Use the definition-derived bosonic reference
[GB-WEYLOG-DEF-v1](../inputs/action_sources/09_gauss_bonnet_from_weyl_log_action_lock.md).
Its curvature-only sector is
$`-\tfrac14(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2)`$.
Accordingly a coefficient $`\alpha`$ multiplying a bare positive GB curvature
density would be $`\alpha=-\lambda_{\rm GB}/4`$ in this sector only.
This does not replace the off-shell completion by bare Lovelock gravity.

**Normalization resolved, 2026-09-28:** Weyl GA24 is in the OP
$`\sigma\widehat C^2/8`$ normalization. Equations GB16–GB20 of
[the action derivation](../../../action/gb_splus_action.md) compare its complete
primary, including both fermion bilinears, and propagate the constant through
all descendants and BF/current slots. They give
$`\ell_{\rm Weyl^2}=-2\ell_{\rm W,OP}`$ for the inherited working map, hence
$`\ell_{\rm GB}=-2\ell_{\rm W,OP}-4\ell_{\log}`$.
The outstanding independent Weyl multiplet-law checks are unchanged.
This resolves the previously recorded gate without changing the target
physical convention.

After fixing the compensator scale,
$`[\kappa_5^2]=-3`$, $`[\lambda_{\rm GB}]=-2`$, $`[g]=[\nabla]=1`$,
$`[R]=2`$, $`[L]=0`$, and $`[N_c]=[E_{ca}]=[G_{ab}]=[H_{ab}]=[V_a]=1`$.
Then $`[\ell_{2\partial}]=2`$, $`[\ell_{\rm GB}]=4`$, so the action is
dimensionless. The source-frame fermions with the common gravitational
prefactor have dimension $`1/2`$ in a first-order kinetic density; canonical
rescaling must be stated before changing that assignment. Pre-gauge Weyl
weights are different: LOG C06 gives $`w(\chi)=3/2`$, $`w(\varphi_c)=7/2`$,
and $`w(L_c,N_c,E_c)=(3,4,4)`$. Do not mix these two gradings.

## 8. Variation, expansion and spectrum bookkeeping

Use independent Grassmann component coordinates with left variations:
$`\delta S=\int d^5x\,\delta\Psi^A(\delta^L S/\delta\Psi^A)`$ after
putting $`\delta\Psi^A`$ on the left. Bars are Majorana-dependent, not a
second set of independent physical fields. Derive the two contributions
from a diagonal quadratic Majorana bilinear; do not silently drop its
factor of two. This follows the convention in LOG spectrum file 04 §1.

Use an even bookkeeping parameter $`\varepsilon`$:

```math
S[\bar\Phi+\varepsilon\delta\Phi]
=S^{(0)}+\varepsilon S^{(1)}+\varepsilon^2S^{(2)}+\cdots,\qquad
S^{(n)}=\frac1{n!}\left.\frac{d^nS}{d\varepsilon^n}\right|_0.
\tag{GB-C17}
```

Physical fermion degree counts fermions inside hats, composites, connections
and derivatives. Around a bosonic background, keep all degree-two terms
for the fermionic Hessian. A degree-four intermediate can still feed a
degree-two descendant under spinor differentiation and cannot be discarded
before that operation. Fluctuation order and fermion degree are distinct.

Use exact equality, equality through a stated order, and equality modulo
a displayed divergence as separate statements. Derive local bulk EOM with
compactly supported variations. If AdS is selected, boundary conditions
and the conserved inner product require their own declaration; a bulk
kinetic sign is not a renormalized boundary norm.

For a first-order eigenfield define the signed mass by
$`(\not{\bar\nabla}+\mu)\Xi=0`$ after treating gauge and constraints.
Write $`\mu\ell`$ separately from any squared or curvature-shifted parameter.
Vector-spinor commutators act on both the spinor and vector indices.
Reality relates conjugate SU(2) charge branches; do not count them twice.
No Fourier convention is needed yet. Declare one before any flat momentum
calculation. Exact finite-action roots and formal EFT-heavy roots must be
reported separately.

## 9. Consistency checks and remaining scope

The component dictionary specifies the Clifford, Majorana, SU(2), curvature
and weight conventions used by the current action and Hessians.

The conventions are anchored. The common-normalized density through two
physical fermions and its full assembly ledger are now recorded in
`GB-FERMION-ACTION-0+2-v1`. Its inherited input-verification qualifications
remain explicit. The [GB AdS5 reduction](../../README.md) gives the background, quadratic operators,
eigenmodes, norms and critical branch in the GB normalization. The LOG-only
background and coupling labels are not substituted for that GB calculation.
