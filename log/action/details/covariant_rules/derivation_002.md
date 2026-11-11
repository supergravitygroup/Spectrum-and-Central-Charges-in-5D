# Conventions and source equations: full fermionic gauged LOG invariant — LOG-G01 – LOG-CHECK01

<a id="conventions-and-source-equations-full-fermionic-gauged-log-invariant--deliberate-boundaries-and-pending-matching-checks"></a>

[Component index](../covariant_rules.md). Definitions and source conventions are in [the opening section](convention_001.md).

## Source frames and conversion scope

- The full S23 primary is transcribed above. The compact descendant definitions are exact. The long descendants and higher component derivatives are available in the local source cache; the component derivations evaluate them in the stated source frame.
- S23 (3.27) and C24 (5.9b) are Standard-Weyl BF constructions. Their published local supersymmetry does not by itself prove a new, explicitly expanded, project-corrected gauged action.
- C24 Tables4–6 establish the published Gold/Bergshoeff bridge. They do not contain a full Gold linear-multiplet-to-project `L,varphi,E,N` normalization table. The branch derives that covariant normalization in LOG_CONVENTIONS.md. The [full superform interface](../../../../references/source_evidence/log/derivations/form-interface.md) completes the generic current/potential/BF comparison, preserving explicit derived repairs of the incompatible printed formulas. Checking the actual expanded LOG multiplet remains distinct from this generic conversion.
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
remains free. These equations specify gauge preservation and its kinematic
solutions in the declared component frame.

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
[weyl_log_from_definitions.tex](../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex):
`eq:Bianchi-expanded`, `eq:L-Yraw`, `eq:L-YD`, L1–L13,
`eq:L-final-expanded` (Eq. (52) in the accompanying report), and the boundary
currents `eq:Log-mixed-current`, `eq:twoform-boundary-id`, `eq:Log-D-boundary`.
Its checks are in [verify_weyl_log_definition_map.py](../../../../references/source_evidence/log/scripts/verify_weyl_log_definition_map.py).
The earlier [missing-terms literature audit](../component_construction/EXTERNAL_REFERENCES.md#ref-7145e536cd95)
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
conditional on the raw supplement. The [complete calculated bosonic certificate](../../../../references/source_evidence/log/derivations/bosonic.md)
now additionally reproduces the entire corrected ledger from the newly calculated
LOG scalar/vector/BF components, including this sector. Full details and original page
anchors are in [the direct source audit](../component_construction/results/gauged_full_fermionic_log/notes/05_two_bosonic_corrections_source_audit.md),
with [the independent checker](../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_two_bosonic_corrections.py).
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
The [complete calculated bosonic certificate](../../../../references/source_evidence/log/derivations/bosonic.md) now reproduces this entire density
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
  derivation](../../../../references/source_evidence/log/derivations/form-interface.md) resolves FORM-01
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
- LOG-G02 gives exact gauge-preservation equations and their kinematic
  solutions in the declared component frame.
- G25 (11) is preserved as a literal source record. LOG-CORR01–LOG-CORR05
  carry the existing definition-derived bosonic corrections and corrected
  comparison density. The [complete calculated bosonic certificate](../../../../references/source_evidence/log/derivations/bosonic.md) now reproduces its full
  bosonic body from the calculated multiplet with explicit boundary currents.
  This closes that bosonic comparison; unrestricted fermionic checks remain
  separate, and matching the uncorrected printed action is insufficient.
- Neither raw source text nor a hash check proves a 44-page descendant
  polynomial. The cited source equations determine its coefficients and indices;
  each algebraic validation states what was actually checked.

The [bibliography](../../../../references/bibliography.md) provides the original publications for source comparisons; the displayed equation and page locators specify the relations used here.

## Subsequent retained-order certification — 2026-09-25

The reference-task limits above describe what its own integrity checker establishes. The later [complete branch certificate](../component_construction/results/gauged_full_fermionic_log/CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) independently closes defining-projector, full curved-primary, retained projection/canonicalization/reality, generic current/BF and complete bosonic gates. Its supersymmetry conclusion uses the verified multiplet and closed BF superform. Its action-level statement is restricted to the retained physical fermion order. Source transcriptions and project-derived repairs remain distinct.

## Source-equation appendix: exact saved equations and searchable text

This appendix contains searchable source transcriptions with stable page identifiers. The [bibliography](../../../../references/bibliography.md) links the published sources for checking exact upper/lower positions, underlines and bracket glyphs. Plain-text order is not a Grassmann or index-order rule. The page identifiers below locate source text, rather than bundled page images or PDF caches.

The full C24 LOG descendants span PDF106–149. The scalar/vector transition occurs on PDF121; the vector/bosonic-action transition occurs on PDF149. Nothing is truncated at those boundaries. Supplement §3.1 on PDF149 is bosonic only. Full higher-derivative expansions occupy PDF300–327.

| Input group | Cached PDF pages | Equation role |
|---|---|---|
| S23 | 7–14 | [Superconformal algebra, Weyl/vector/linear descendants and BF](derivation_002.md#src-s23-p007) |
| S23 | 20–22 | [LOG primary, complete expanded superfield, descendant definitions and action](derivation_002.md#src-s23-p020) |
| C24 | 8–24 | [Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF](derivation_002.md#src-c24-p008) |
| C24 | 32–37 | [Main4.2: LOG primary and descendants, including full4.8a](derivation_002.md#src-c24-p032) |
| C24 | 41–41 | [Main5.9: full component LOG BF density](derivation_002.md#src-c24-p041) |
| C24 | 81–83 | [AppendixA: conformal superspace derivative algebra](derivation_002.md#src-c24-p081) |
| C24 | 90–92 | [AppendixC: convention bridge and Tables4–6](derivation_002.md#src-c24-p090) |
| C24 | 103–103 | [Supplement1: raw index conventions and X/Y component projections](derivation_002.md#src-c24-p103) |
| C24 | 106–113 | [Supplement2.2.1: complete LOG spinor descendant; scalar starts on113](derivation_002.md#src-c24-p106) |
| C24 | 113–121 | [Supplement2.2.2: complete LOG scalar descendant; vector starts on121](derivation_002.md#src-c24-p113) |
| C24 | 121–149 | [Supplement2.2.3: complete LOG vector descendant; bosonic3.1 starts on149](derivation_003.md#src-c24-p121) |
| C24 | 300–308 | [Supplement5.1: full degauged higher Weyl derivatives](derivation_003.md#src-c24-p300) |
| C24 | 308–324 | [Supplement5.2: full degauged higher vector derivatives](derivation_003.md#src-c24-p308) |
| C24 | 324–327 | [Supplement5.3: full degauged higher linear derivatives](derivation_004.md#src-c24-p324) |
| G25 | 4–10 | [Maps1,4; derivative2; abbreviated BF3; gauge7; LOG9–11; relation13](derivation_004.md#src-g25-p004) |
| G25 | 13–14 | [Relations22–23; gauge25, reference26 and connection split27](derivation_004.md#src-g25-p013) |
| W | 15–25 | [Full Weyl geometry, constraints, transformations and soft algebra](derivation_004.md#src-w-p015) |
| W | 28–29 | [Improved-vector constraints5.10–5.14 and their descendants](derivation_004.md#src-w-p028) |
| W | 32–34 | [AppendixA: all 5D Clifford, symplectic-Majorana, SU(2), Fierz and duality conventions](derivation_004.md#src-w-p032) |
| OP | 4–11 | [Multiplets, derivatives, curvatures, forms, full composites and density](derivation_005.md#src-op-p004) |
| OP | 13–14 | [Gauge4.1, retained fields4.2 and truncated compensating transformations4.3](derivation_005.md#src-op-p013) |
| OP | 28–29 | [Appendices: gamma/spinor and notation conventions](derivation_005.md#src-op-p028) |
| CO | 4–8 | [Weyl, vector and linear multiplet transformations and covariant structures](derivation_005.md#src-co-p004) |
| CO | 16–17 | [Gauged map5.2–5.8 and explicit higher-fermion omission statement](derivation_005.md#src-co-p016) |
| OPall | 8–8 | [3.1–3.2: operational E_a density and P/E completion](derivation_005.md#src-opall-p008) |

### S23: cached source equations

Source PDF: [2023-Gold-On-curvature-squared-invariants-from-superspace.pdf](../component_construction/EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8). SHA-256: `7461b1548e04efb4836f2e0ea0f4f9e5d53566d52b112ab5c452332e36e3849a`.

<a id="src-s23-p007"></a>

<details>
<summary>S23-p007 — PDF page 7: Superconformal algebra, Weyl/vector/linear descendants and BF</summary>

[S23-p007: PDF page 7](https://arxiv.org/pdf/2302.14295v2#page=7)

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

[S23-p008: PDF page 8](https://arxiv.org/pdf/2302.14295v2#page=8)

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

[S23-p009: PDF page 9](https://arxiv.org/pdf/2302.14295v2#page=9)

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

[S23-p010: PDF page 10](https://arxiv.org/pdf/2302.14295v2#page=10)

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

[S23-p011: PDF page 11](https://arxiv.org/pdf/2302.14295v2#page=11)

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

[S23-p012: PDF page 12](https://arxiv.org/pdf/2302.14295v2#page=12)

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

[S23-p013: PDF page 13](https://arxiv.org/pdf/2302.14295v2#page=13)

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

[S23-p014: PDF page 14](https://arxiv.org/pdf/2302.14295v2#page=14)

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

[S23-p020: PDF page 20](https://arxiv.org/pdf/2302.14295v2#page=20)

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

[S23-p021: PDF page 21](https://arxiv.org/pdf/2302.14295v2#page=21)

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

[S23-p022: PDF page 22](https://arxiv.org/pdf/2302.14295v2#page=22)

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

Source PDF: [2024-Gold-Components-of-curvature-squared-invariants.pdf](../component_construction/EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4). SHA-256: `0e30ca2f64d6e7e8e08f653f08a85883a06c74377c2fb57f578dc01c00fedca2`.

<a id="src-c24-p008"></a>

<details>
<summary>C24-p008 — PDF page 8: Main section2: full superconformal multiplets, curvatures, connections, laws; section3 BF</summary>

[C24-p008: PDF page 8](https://arxiv.org/pdf/2311.00679v1#page=8)

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

[C24-p009: PDF page 9](https://arxiv.org/pdf/2311.00679v1#page=9)

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

[C24-p010: PDF page 10](https://arxiv.org/pdf/2311.00679v1#page=10)

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

[C24-p011: PDF page 11](https://arxiv.org/pdf/2311.00679v1#page=11)

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

[C24-p012: PDF page 12](https://arxiv.org/pdf/2311.00679v1#page=12)

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

[C24-p013: PDF page 13](https://arxiv.org/pdf/2311.00679v1#page=13)

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

[C24-p014: PDF page 14](https://arxiv.org/pdf/2311.00679v1#page=14)

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

[C24-p015: PDF page 15](https://arxiv.org/pdf/2311.00679v1#page=15)

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

[C24-p016: PDF page 16](https://arxiv.org/pdf/2311.00679v1#page=16)

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

[C24-p017: PDF page 17](https://arxiv.org/pdf/2311.00679v1#page=17)

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

[C24-p018: PDF page 18](https://arxiv.org/pdf/2311.00679v1#page=18)

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

[C24-p019: PDF page 19](https://arxiv.org/pdf/2311.00679v1#page=19)

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

[C24-p020: PDF page 20](https://arxiv.org/pdf/2311.00679v1#page=20)

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

[C24-p021: PDF page 21](https://arxiv.org/pdf/2311.00679v1#page=21)

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

[C24-p022: PDF page 22](https://arxiv.org/pdf/2311.00679v1#page=22)

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

[C24-p023: PDF page 23](https://arxiv.org/pdf/2311.00679v1#page=23)

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

[C24-p024: PDF page 24](https://arxiv.org/pdf/2311.00679v1#page=24)

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

[C24-p032: PDF page 32](https://arxiv.org/pdf/2311.00679v1#page=32)

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

[C24-p033: PDF page 33](https://arxiv.org/pdf/2311.00679v1#page=33)

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

[C24-p034: PDF page 34](https://arxiv.org/pdf/2311.00679v1#page=34)

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

[C24-p035: PDF page 35](https://arxiv.org/pdf/2311.00679v1#page=35)

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

[C24-p036: PDF page 36](https://arxiv.org/pdf/2311.00679v1#page=36)

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

[C24-p037: PDF page 37](https://arxiv.org/pdf/2311.00679v1#page=37)

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

[C24-p041: PDF page 41](https://arxiv.org/pdf/2311.00679v1#page=41)

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

[C24-p081: PDF page 81](https://arxiv.org/pdf/2311.00679v1#page=81)

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

[C24-p082: PDF page 82](https://arxiv.org/pdf/2311.00679v1#page=82)

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

[C24-p083: PDF page 83](https://arxiv.org/pdf/2311.00679v1#page=83)

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

[C24-p090: PDF page 90](https://arxiv.org/pdf/2311.00679v1#page=90)

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

[C24-p091: PDF page 91](https://arxiv.org/pdf/2311.00679v1#page=91)

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

[C24-p092: PDF page 92](https://arxiv.org/pdf/2311.00679v1#page=92)

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

[C24-p103: PDF page 103](https://arxiv.org/pdf/2311.00679v1#page=103)

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

[C24-p106: PDF page 106](https://arxiv.org/pdf/2311.00679v1#page=106)

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

[C24-p107: PDF page 107](https://arxiv.org/pdf/2311.00679v1#page=107)

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

[C24-p108: PDF page 108](https://arxiv.org/pdf/2311.00679v1#page=108)

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

[C24-p109: PDF page 109](https://arxiv.org/pdf/2311.00679v1#page=109)

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

[C24-p110: PDF page 110](https://arxiv.org/pdf/2311.00679v1#page=110)

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

[C24-p111: PDF page 111](https://arxiv.org/pdf/2311.00679v1#page=111)

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

[C24-p112: PDF page 112](https://arxiv.org/pdf/2311.00679v1#page=112)

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

[C24-p113: PDF page 113](https://arxiv.org/pdf/2311.00679v1#page=113)

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

[C24-p114: PDF page 114](https://arxiv.org/pdf/2311.00679v1#page=114)

Layout text for searching; the image controls mathematical transcription.


[Previous component](convention_001.md) · [Component index](../covariant_rules.md) · [Next component](derivation_003.md)
