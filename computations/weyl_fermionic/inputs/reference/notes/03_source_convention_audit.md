# Independent source-convention audit

<!-- ASSERT_CONVENTION: metric_signature=mostly-plus, natural_units=natural -->

This note establishes the convention inputs to the direct Özkan–Pang
Weyl-to-linear variation construction. The component calculations are given
in the [fermionic map derivation](../../../derivations/fermionic-map.md).
The working definitions are collected in the
[component conventions](../../../derivations/component_conventions.md).

## Sources and evidence

- **OP:** Özkan and Pang, *Supersymmetric Completion of Gauss–Bonnet
  Combination in Five Dimensions*, arXiv:1301.6622v4
  ([publication](../../../../../references/bibliography.md#OzkanPangGB2013)).
  Printed page numbers equal PDF page numbers.
- **W:** Bergshoeff et al., *Weyl multiplets of N=2 conformal supergravity in
  five dimensions*, arXiv:hep-th/0104113v4, JHEP 06 (2001) 051.
  Printed page n is PDF page n+1.
  ([publication](../../../../../references/bibliography.md#additional-references-cited-in-the-derivations)).

The audit consulted the existing branch convention lock and published source
text, and visually inspected OP PDF pages 7, 8, 10, 19, 20 and W PDF pages
23, 34. The field-variation and curvature reconstruction uses W (3.4),
(3.5)–(3.6), (3.11), (3.17), (3.20)–(3.23), (4.3)–(4.4), and Appendix A.
No published erratum has been established here. A corrected expression below
is identified as **source-derived working correction**, never silently
attributed to the literal PDF.

## Audit outcome and limits

The sources can be used together provided the explicit corrections and
notation distinctions below are carried into the working convention file.
The largest hidden danger is that W (3.21) is not the full dependent
S-connection variation. Its ellipsis cannot be filled by the bare gauge
variation alone without checking the modified algebra.

The independent checks do **not** establish nonlinear supersymmetry of OP
(5.8), the omitted E/N terms, the complete invariant, or the future spectrum.
They also do not resolve the separate higher-order disagreement in the
linear-to-vector map used for the future two-derivative action.

## A01 — A dot is an unnormalized full contraction

**Source:** W (A.14), printed p.33/PDF p.34, visually checked.

The equation actually reads

```math
\frac1{n!}A^{a_1\cdots a_n}B_{a_1\cdots a_n}
=\frac1{n!}A\cdot B.
```

Therefore

```math
A\cdot B=A^{a_1\cdots a_n}B_{a_1\cdots a_n},\qquad
\gamma\cdot T=\gamma^{ab}T_{ab},\qquad
T\cdot\widehat R(Q)=T^{ab}\widehat R_{ab}(Q).
```

There is **no** hidden factor 1/2 in either two-form dot. PDF text extraction
can lose the prefactor of the middle expression and suggest the opposite.
For a spatial two-form with A12=1, A21=−1, A·A=2; the normalized form inner
product (1/2!)A·A=1. These are different quantities.

The last denominator in the literal W (A.14) is `(n−5)!`; consistency with
the rank of the dual in (A.13) requires `(5−n)!`. This is a separate obvious
rank/factorial typo and does not alter the dot convention. Operational
identities can be stated directly in terms of the Levi-Civita contraction
and gamma duality, avoiding this misprinted denominator entirely.

**Status:** resolved by literal PDF reading; factorial repair is explicitly
source-derived.

## A02 — The dilatation connection in Dχ

**Sources:** OP (2.12), p.8; W Table 3, printed p.10/PDF p.11; W (3.17),
printed p.19/PDF p.20.

OP literally prints

```math
\mathcal D_\mu\chi^i=(\partial_\mu-\tfrac72 b_\mu+
\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\chi^i+\cdots.
```

But W Table 3 gives w(χ)=3/2, and W (3.17) fixes the coefficient to −w.
The required working expression is

```math
\boxed{\mathcal D_\mu\chi^i=(\partial_\mu-\tfrac32 b_\mu+
\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\chi^i+\cdots.}
```

This also follows directly from δT∼εχ: w(T)=1 and w(ε)=−1/2 imply
w(χ)=3/2. Under local dilatations, a trial coefficient −αb leaves
`(3/2−α)(∂μΛD)χ`. The printed α=7/2 gives −2, while α=3/2 gives zero.
The other terms in OP (2.12) are not changed by this weight correction.

**Status:** source-derived working correction; independent local-covariance
check passed.

## A03 — The naked gravitino term in the Lorentz curvature

**Sources:** OP (2.7), p.7, visually checked; W (3.4), (3.6), (3.20), and
(4.4), printed pp.14,15,20,24.

OP literally contains an isolated

```math
+i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}
```

in addition to the T-dependent gravitino term and the φψ term. It is not a
misread φ in the PDF. This isolated term has Weyl weight −1, while
`Rhatμν{}ab(M)` has weight zero. All the neighboring fermionic terms have
the appropriate compensating T, φ, χ, or curvature weight.

The W reconstruction starts with the bare curvature

```math
R_{\mu\nu}{}^{ab}(M)=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}.
```

The modified QQ→M structure function is T-dependent, as W (4.4) shows;
the M-dependent additions are the R(Q) and χ terms in W (3.20).
Neither mechanism generates the isolated, dimensionally incompatible term.
The working curvature omits it. This is a repair of the literal source,
not a bosonic truncation and not a field redefinition.

**Status:** source-derived working correction supported independently by
Weyl covariance and the explicit W gauge-curvature construction.

## A04 — The χ sign in the Lorentz curvature

**Sources:** OP (2.7), p.7; W (3.6), (3.20), printed pp.15,20.

The relevant M-dependent terms in the connection transformation have
coefficients

```math
M_\nu{}^{ab}\supset
-\tfrac12\gamma^{[a}\widehat R_\nu{}^{b]}(Q)
-\tfrac14\gamma_\nu\widehat R^{ab}(Q)
-4e_\nu{}^{[a}\gamma^{b]}\chi.
```

The common curvature rule `−2 barψ_[μ M_ν]` maps them to

```math
(-\tfrac12,-\tfrac14,-4)\ \longmapsto\ (+1,+\tfrac12,+8).
```

The first two coefficients agree with OP. Thus the third working coefficient
is +8, replacing OP's printed −8. In combination with A03, the complete
working curvature is

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^{ab}(M)={}&
2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}\\
&+i\bar\psi_{[\mu}\gamma^{[a}\gamma\cdot T\gamma^{b]}\psi_{\nu]}
+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\tfrac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)\\
&+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi.
\end{aligned}
```

The separate χ completion of `Rhat(V)` remains −8: δV contains +4 εγχ,
so the same curvature rule yields −8. Changing both signs would be wrong.

**Status:** source-derived working correction. No published erratum is
claimed. The coefficient test calibrates the common sign on the two
neighboring R(Q) structures.

## A05 — The Ricci sign is a contraction difference

**Sources:** OP (2.10), p.7; W (3.11), printed p.17/PDF p.18.

With the **same** primed Lorentz curvature,

```math
\mathcal R^{\rm OP}_{\mu\nu}
=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},\qquad
\mathcal R^{\rm W}_{\mu\nu}
=\widehat R'_{\mu\rho}{}^{ab}(M)e_a{}^\rho e_{\nu b}.
```

Antisymmetry in ab implies `R_OPμν=−R_Wμν` and `R_OP=−R_W`. Therefore

```math
-\tfrac16\mathcal R^{\rm OP}_\mu{}^a
+\tfrac1{48}e_\mu{}^a\mathcal R^{\rm OP}
=+\tfrac16\mathcal R^{\rm W}_\mu{}^a
-\tfrac1{48}e_\mu{}^a\mathcal R^{\rm W}.
```

Both sources define the same f. For the bosonic test curvature
`R'μν{}ab=k(eμa eνb−eνa eμb)`, OP gives Ricci=4kg and scalar=20k;
W gives −4kg and −20k. Both give `fμa=−k eμa/4`. For k=1 the coefficient
is −1/4 in both descriptions. This is not an independent curvature-sign
change and must not trigger an additional sign flip of f.

**Status:** exact source-to-source conversion established.

## A06 — A missing σ in the H variation

**Sources:** OP (2.8), p.7; W (3.27), printed p.22/PDF p.23; OP (2.1),
(2.3), p.6. Both printed short curvature-variation formulas omit σ in

```math
\tfrac{3i}{2}\bar\epsilon\gamma_{[ab}\mathcal D_{c]}\psi.
```

That term has weight 2; `Hhat_abc` has weight 3. Its required completion is

```math
\boxed{\tfrac{3i}{2}\sigma\bar\epsilon
\gamma_{[ab}\mathcal D_{c]}\psi.}
```

This is also fixed by direct variation, without guessing from weights.
At a point take a flat frame, constant ε, constant σ=s, C=B=T=ψμ=0 and
allow ∂ψ to be nonzero. The principal derivative term follows from

```math
\delta B_{\mu\nu}=\tfrac i2s\bar\epsilon\gamma_{\mu\nu}\psi,
\qquad
\delta\widehat H_{abc}\big|_{\partial\psi}
=\tfrac{3i}{2}s\bar\epsilon\gamma_{[ab}\partial_{c]}\psi.
```

The variation of the gravitino completions cannot supply a second
`∂ψ` term in this test. At s=2 the coefficient is 3i, whereas the literal
short formula gives 3i/2. This establishes the repair of this coefficient;
it is not a general proof of every term in the H variation.

**Status:** source-derived working correction; principal-derivative and
weight checks agree.

## A07 — Tangent and coordinate curvature variations differ

**Sources:** W (3.27) is explicitly δFhat_ab; OP (2.8) writes δGhat_μν with
the same short structure. The operational source should be the tangent
law, with the sigma repair in A06 for H.

For an ordinary transformation of the coordinate tensor,

```math
\delta\widehat G_{\mu\nu}
=e_\mu{}^ae_\nu{}^b\delta\widehat G_{ab}
+2\delta e_{[\mu}{}^ae_{\nu]}{}^b\widehat G_{ab}.
```

For H there are three analogous vielbein-variation terms. Conversely,
variation of a tangent tensor includes the inverse-vielbein variations.
Dropping these terms amounts to introducing a frame-compensated variation;
it is not the ordinary δ acting on the coordinate components.

A simple basis test suffices: at an identity frame let G12=1 and
δe1{}1=t, with δGab=0. Then δGworld12=t, not zero. This issue first appears
in the fermionic terms for Q transformations, since δe∼εψμ.

**Status:** operational frame rule fixed. The notation in the OP short
world-index law is not to be interpreted as permission to discard δe.

## A08 — The BF density's spinor in OP (3.2)

**Source:** OP (3.1) and (3.2), p.10, visually checked.

Equation (3.1) contains `−(1/2) barψ_ai γa λj Lij`. Equation (3.2), described
as differing only by integration by parts in the gauge-field term, prints
`−(1/2) barψ_ai γa ψj Lij`. The second spinor must remain the vector
multiplet λj. Integration by parts in A∂E cannot replace λ by the unrelated
dilatino ψ. With λ=0 and ψ nonzero the first density has no such term;
the literal second density spuriously generates one.

Use (3.1) as the primary density. If using its two-form form, retain λ in
this term and record that the source symbol has been corrected. The vector
and dilaton-Weyl spinors become identified only after the separate map
(5.16) is applied.

**Status:** source-derived working correction based on the preceding full
density and the stated integration by parts.

## A09 — Repeated vector variations in Section 5

**Sources:** OP (2.1), (2.13), (5.14), (5.15), pp.6,8,19,20; Section 5
pages visually checked.

The vector law in (5.14) literally has
`δAμ=−(1/2)σ barεψμ+(1/2)barεγμλ`. The correct primary law from (2.13) is

```math
\delta A_\mu=-\tfrac i2\rho\bar\epsilon\psi_\mu
+\tfrac12\bar\epsilon\gamma_\mu\lambda.
```

Section 5 prematurely substituted σ for ρ and omitted i in this line.
For ρ=2, σ=3, `barεψμ=1`, λ=0, the two printed expressions give −i and
−3/2, showing that they are not interchangeable before the map.

Likewise (5.15) omits i in δC. Use the full primary (2.1) law

```math
\delta C_\mu=-\tfrac i2\sigma\bar\epsilon\psi_\mu
+\tfrac12\bar\epsilon\gamma_\mu\psi.
```

For σ=2 and unit indicated bilinear, this term is −i, not −1. The map
`ρ→σ, A→C, λ→ψ` is consistent between the primary Section 2 laws; the
repeated Section 5 lines are not independent operational inputs.

**Status:** resolved by source's earlier complete transformation laws.

## A10 — Spinor exchange and the suppressed SU(2) index

**Sources:** OP (A.1)–(A.5), pp.28–29; W (A.3)–(A.10), printed pp.31–32.
For Grassmann-odd spinors with fixed, explicit SU(2) labels,

```math
\bar\psi^i\gamma_{(n)}\chi^j
=t_n\bar\chi^j\gamma_{(n)}\psi^i,
\quad (t_0,t_1,t_2,t_3)=(+1,+1,-1,-1).
```

Because `χ_i=χ^j ε_ji`, an additional minus arises when a **suppressed
NW–SE contraction** is exchanged:

```math
\boxed{\bar\psi\gamma_{(n)}\chi
=-t_n\bar\chi\gamma_{(n)}\psi.}
```

Thus scalar/vector contracted bilinears have exchange sign −, whereas
rank-2/rank-3 contracted bilinears have exchange sign +. This reconciles
the superficially different final contorsion terms in OP (2.5) and W
(3.11), since `barψ^b γμ ψ^a=−barψ^a γμ ψ^b`.

An explicit 4×4 matrix check used Pauli matrices and

```math
\Gamma_1=\sigma_1\otimes1,\quad
\Gamma_2=\sigma_2\otimes1,\quad
\Gamma_3=\sigma_3\otimes\sigma_1,\quad
\Gamma_4=\sigma_3\otimes\sigma_2,\quad
\Gamma_5=\sigma_3\otimes\sigma_3,
```

`γ^0=−iΓ5`, `(γ^1,…,γ^4)=(Γ1,…,Γ4)`, and `C=Γ2Γ4`.
The Clifford anticommutators, `γ^{01234}=i1`, `C^T=−C`, `C†C=1`, and
`(Cγ(n))^T=−t_n Cγ(n)` for every distinct index set through rank 3 all
had maximum numerical error zero. This checks the matrix signs; Grassmann
exchange and the epsilon contraction supply the two separate algebraic
minus signs described above.

**Status:** source conventions are consistent; concrete representation
checks passed. This check is not a nonlinear Fierz reduction of the map.

## A11 — An ellipsis in δφ is not a full law

**Sources:** W (3.5), (3.6), (3.20)–(3.22), (4.3)–(4.4), printed pp.15,
20–21,23–24.

W states that (3.21) displays only the M-dependent additions to δφ.
Equation (3.5) has both `εJ hA f_AJ^I` and `εJ M_J^I`. The structure
functions f are themselves modified; in particular (4.4) contains
χ/R(Q)-dependent QQ→S parameters. Consequently, adding only
`Dμη+i fμa γa ε` to the displayed M terms must not be called the extracted
full all-order δφ without reconstructing the modified-structure-function
terms as well.

A complete and safe operational alternative is to define the variation by
the dependent connection itself:

```math
\delta\phi_\mu^i
=\delta\left[\tfrac i3\gamma^a e_a{}^\nu
\widehat R'_{\mu\nu}{}^i(Q)
-\tfrac i{24}\gamma_\mu\gamma^{ab}
 e_a{}^\rho e_b{}^\sigma\widehat R'_{\rho\sigma}{}^i(Q)\right].
```

Here δ acts on every vielbein, world gamma, and factor in the explicit
primed Q curvature; tangent gamma matrices stay fixed. That curvature
contains no φ, so this prescription does not introduce an implicit δφ
on its own right-hand side. The required δω is the complete W (3.20)
with ordinary bosonic gauge terms as appropriate.

Similarly W (3.22), `δS f_a{}a=−5i barηχ`, is explicitly only the
M-dependent piece, not the full Q/S variation of f. Vary the full primed
Ricci definition of f instead.

**Status:** a potential falsely complete extraction has been prevented.
The exact chain-rule definition is complete; a simplified all-order
covariant δφ formula has not been derived in this audit.

## A12 — Levi-Civita tensors and densities

**Sources:** W (A.12), printed p.33/PDF p.34, visually checked; OP (2.21),
(2.23), (3.1), (A.6)–(A.7).

W (A.12) writes its upper world alternating object with an explicit factor
of e times five inverse vielbeins. Thus that particular source notation is
an alternating **density**, not the ordinary weight-zero tensor. Do not
import its displayed world-index formula into an OP scalar Lagrangian
while silently reusing the same epsilon name.

An unambiguous branch choice is `e=det(eμa)>0`, an alternating symbol
`[01234]=+1`, and

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e^{-1}[\mu\nu\rho\sigma\lambda],\qquad
\varepsilon_{\mu\nu\rho\sigma\lambda}
=-e[\mu\nu\rho\sigma\lambda],
```

with flat `ε01234` upper = +1, lower = −1 and `γabcde=i εabcde`.
Whenever reproducing the W world density, write it as
`mathfrak-epsilon=e epsilon_tensor`. At e=2 the two objects differ by a
factor 2. In particular, it is `e ε_tensor` that is constant as the
alternating coordinate symbol in integrations by parts.

**Status:** explicit notation distinction required; orientation choice is
compatible with the Clifford representation test in A10.

## A13 — SU(2) symmetry in a curvature variation

**Source:** W (3.23), printed p.21/PDF p.22.

In the γ·T R(Q) term in δRhat_ab{}ij(V), the printed expression closes a
symmetrization parenthesis on j but fails to open one on i. The entire
result transforms in the symmetric ij representation. The operational
term is therefore

```math
+i\bar\epsilon^{(i}\gamma\cdot T\widehat R_{ab}{}^{j)}(Q).
```

Keeping it unsymmetrized would produce an antisymmetric ij piece that
cannot be the variation of the symmetric connection curvature.

**Status:** missing bracket corrected explicitly by the source's field
representation and the surrounding symmetrized terms.

## Provides/consumes ledger

| Input transferred to the convention file | Check | Result |
|---|---|---|
| W dot → OP shorthand | Two-form A12=1 gives contraction 2 | No factorial |
| W weight χ → OP Dχ | Local dilatation residual | Printed −7/2 fails; −3/2 passes |
| W curvature construction → OP R(M) | Weyl weight and explicit f/M terms | Naked ψψ term excluded |
| W δω M terms → OP R(M) χ term | Common −2 map of three coefficients | +8 required |
| W Ricci/f → OP Ricci/f | k=1 constant-curvature test | Same f=−e/4 |
| OP δB → short δH | σ=2 principal ∂ψ test | Missing σ required |
| W tangent curvature laws → coordinate expressions | δe1{}1=t, G12=1 | Frame terms required |
| OP3.1 → OP3.2 density | Independent λ=0, ψ≠0 | Retain λ |
| OP2 vector laws → OP5 repeated rules | ρ=2, σ=3, unit bilinear | Use Section 2 factors/fields |
| Explicit SU(2) flip → suppressed flip | Clifford representation + ε antisymmetry | Extra minus required |
| Partial δφ/δf → full dependent variations | Modified algebra inspection | Use exact defining variations |
| W world epsilon → OP scalar density | e=2 test | Distinguish density from tensor |
| Symmetric curvature → W3.23 term | ij representation | Restore opening parenthesis |

No Fourier, quantization-state normalization, regularization, renormalization,
or thermal conventions enter these algebraic source-interface checks.
Their absence here is not a choice for a future spectrum computation.

## Follow-up review of the master convention file

The follow-up read-only review checked the first complete master reference,
especially G02–G03, R04–R07, H02, and the SU(2) interfaces. The G02
Ricci/commutator convention, R05 derivative ordering, exact defining
variations R04b/R04d, and R06 replacement rules were consistent. Two
additional source-interface problems were identified below. The parent
maintains the corresponding master-file corrections; this audit does not
edit that file.

## A14 — Lorentz covariantization of the two-form T

**Sources:** OP (2.12), p.8, rechecked with a 300-dpi crop; OP (2.19), p.9;
W (3.3), (3.17). The source prints the first contracted Lorentz index c
**upstairs** in

```math
-2\omega_\mu{}^c{}_{[a}T_{b]c}.
```

This has the opposite sign to the derivative induced on a two-form by the
locked covector derivative `D X_a=∂X_a+ω_{μa}{}^c X_c`. The Leibniz rule
requires

```math
\begin{aligned}
D_\mu T_{ab}\big|_{\rm Lorentz}
&=\omega_{\mu a}{}^cT_{cb}+\omega_{\mu b}{}^cT_{ac}\\
&=+2\omega_\mu{}^c{}_{[a}T_{b]c}
=-2\omega_{\mu[a}{}^cT_{b]c}.
\end{aligned}
```

The last two compact forms have different Lorentz index orders; their
coefficients cannot be copied interchangeably. For a spatial test with
`ω_{μ23}=w`, `T13=t` and the other independent entries zero, the derivative
of T12 obtained from its two covector indices is +wt. The literal
raised-c-first source expression gives −wt. Thus the master must use the
explicit two-index connection sum (or the corrected compact expression)
and record the source sign/index-order repair.

**Status:** source-derived working correction fixed by tensor-product
covariance. The same issue occurs in OP (5.11)'s bosonic notation and must
not be restored when taking a bosonic limit.

## A15 — The potential transformations are not compatible as printed

**Sources:** OP (2.18), (2.21)–(2.24), pp.9–10; OP Appendix A gamma duality;
Özkan–Pang *All Off-Shell R² Invariants in Five Dimensional N=2
Supergravity* (OP-all), [arXiv:1306.1540v3](../../../../../references/bibliography.md#OzkanPangR22013),
(2.17), (3.1)–(3.2), printed/PDF p.8. The latter page was visually checked.
Additional comparisons used Bergshoeff et al., *Superconformal N=2, D=5
matter with and without actions*, [arXiv:hep-th/0205230v6](https://arxiv.org/abs/hep-th/0205230v6),
(2.41), (2.48), and Özkan, *Off-Shell N=2 Linear Multiplets in Five Dimensions*,
[arXiv:1608.00349v2](../../../../../references/bibliography.md#Ozkan2016),
(3.11)–(3.13). Those additional passages are evidence for this audit;
they do not authorize unrecorded convention imports.

With the master's **tensor** epsilon and duality conventions,

```math
\epsilon^{\mu\nu\rho\sigma\lambda}\gamma_{\rho\sigma\lambda}
=6i\gamma^{\mu\nu},\qquad
E^{\mu\nu}=-\tfrac1{12}\epsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda}.
```

The latter inversion follows from OP's `E3=epsilon_lower E2`. Its ordinary
variation necessarily includes `−(δ ln e) E^{μν}`. The printed short
transformation of E2 has no such determinant term. Moreover, the printed
`δE3=−barεγ3ϕ+…` induces **+i/2** `barεγ2ϕ` in the dual E2 variation,
opposite the printed E2 coefficient **−i/2**. At flat principal-derivative
order it likewise induces +i/2 `barεγ^{μν}∂νϕ` in δEμ, opposite the
linear-multiplet law's −i/2. These formulas cannot all be ordinary
variations of the stated tensors simultaneously.

The local matter-coupling paper's (2.41),(2.48) uses
`δE3=+barεγ3ϕ` together with `E_a=−epsilon D E3/12`, which confirms the
necessary leading sign. In that passage E3 is a vector–tensor constraint,
not a full local-supergravity three-form potential, so it does not provide
the missing complete potential law. OP-all's gauge-fixed three-form law
repeats the minus sign and does not resolve the discrepancy.

### An operational density that uses E_a directly

OP-all (3.1)–(3.2), p.8, supplies the necessary source bridge:

```math
P^a=E^a+\tfrac i2\bar\psi_b\gamma^{ba}\varphi
+\tfrac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
```

The vector–linear density contains `+A_a P^a`, with the other terms as in
OP (3.1). In the potential representation,

```math
P^a=-\tfrac1{12}e_\mu{}^a
\epsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}.
```

Thus the direct Weyl-to-linear map can be inserted into the density without
using an unverified E3/E2 transformation. The added gravitino terms in P
must be retained; replacing P by the full supercovariant E drops fermions.
The future proof of the density must of course still use the complete
linear-multiplet transformation laws.

### What is fixed about a corrected potential law

A direct local-parameter check of the usual polynomial ansatz fixes

```math
\delta E_{\mu\nu\rho}\ \stackrel{\rm candidate}{=}
+\bar\epsilon\gamma_{\mu\nu\rho}\varphi
-3i\bar\psi_{[\mu}^{i}\gamma_{\nu\rho]}\epsilon^{j}L_{ij}.
```

The first sign is fixed by the flat principal derivative test above.
For the second coefficient write it as `α i barψ_[μγνρ]ε L`.
Using `δψ_b=∂bε+…`, the variation of
`−barψ_b^i γ^{abc}ψ_c^j Lij/4` in E^a contributes

```math
-\tfrac12(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
```

The potential contribution δP gives
`−α(∂b barε^i)γ^{abc}ψ_c^jLij/6`. Cancellation of derivatives of the local
Q parameter fixes α=−3. This repairs more than just the sign of the first
term. It is a **candidate constrained by these necessary tests**, not an
all-order verified replacement: nonderivative Q terms, S terms, frames,
and the supercovariant field-strength definition still need to be checked.

**Status:** quarantine the printed L04 potential formulas as source-literal
and inconsistent under the stated ordinary-tensor interpretation. Use E_a
and the P bridge for the selected construction. A complete potential-level
check is deferred explicitly, without setting the unknown terms to zero.

## A16 — R05 extraction error exposed by direct S-invariance (2026-09-17)

W(3.23), printed21/PDF22, actually contains T_[a^c gamma_b]c eta. The v3
master mistakenly raised the first index, T^c_[a, reversing the term's sign.
This is an extraction error, not a paper erratum. The original page image was
reinspected after the calculation failed. Master X11 and the
[fermionic-map derivation](../../../derivations/fermionic-map.md) (S02),(S44)–(S45) show the correction and its
consequence: the wrong extraction leaves (16i/3) bar_eta^(i T_ab R^j)ab.
The corrected rule gives zero and preserves the conventional gamma trace.
The [independent S-invariance checker](../../../src/reference_checks/verify_weyl_map_s_invariance.py) reproduces both outcomes.
Confidence: source-verified and independently algebraically checked.

## X12: Q-variation of the printed scalar triplet

The complete calculation is notebook Part II Q01–Q64, summarized in master
M07/X12. Exact locations visually rechecked: OP(5.8), PDF18; W(3.19), PDF21;
W(3.23), PDF22. The [bibliography](../../../../../references/bibliography.md) links the cited source editions. No source extraction error
was found on these lines. The locked laws give8/3 KX, while OP prints16/3 KX.
The explicit residual is -8i barepsilon^(i KX^j)/3; ten other terms match.

Q48–Q57 derive the entire algebraic S-curvature contraction rather than
setting it to zero. Q60–Q61 give a nonzero component example. The Q checker
covers all quadratic T coefficients by polarization and all constrained
spinor two-forms by a surjective gamma-trace projector. The algebra is
verified relative to the input laws. An erratum assignment to OP alone
is not certified: the next interface check is the spinor S-law and, if
needed, an independent curvature-law derivation. Literal M02 is retained.

## Working-spinor adoption — 2026-09-18
