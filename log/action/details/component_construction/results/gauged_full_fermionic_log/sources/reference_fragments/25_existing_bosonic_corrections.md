## Existing project result: corrected bosonic LOG invariant

**Bosonic comparison:** previously derived result used in this
construction. These are project-derived corrections, not a published erratum
and not a completed fermionic invariant. Gold's printed Eq. (11), retained as
LOG-B03, must not be used as an unquestioned target to which coefficients are fitted.

The detailed local derivation is
[weyl_log_from_definitions.tex](../../../../../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex):
`eq:Bianchi-expanded`, `eq:L-Yraw`, `eq:L-YD`, L1–L13,
`eq:L-final-expanded` (Eq. (52) in the accompanying report), and the boundary
currents `eq:Log-mixed-current`, `eq:twoform-boundary-id`, `eq:Log-D-boundary`.
Its checks are in [verify_weyl_log_definition_map.py](../../../../../../../../references/source_evidence/log/scripts/verify_weyl_log_definition_map.py).
The earlier [missing-terms literature audit](../../../../EXTERNAL_REFERENCES.md#ref-ab8a1d747de7)
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
conditional on the raw supplement. The [complete calculated bosonic certificate](../../../../../../../../references/source_evidence/log/derivations/bosonic.md)
now additionally reproduces the entire corrected ledger from the newly calculated
LOG scalar/vector/BF components, including this sector. Full details and original page
anchors are in [the direct source audit](../../notes/05_two_bosonic_corrections_source_audit.md),
with [the independent checker](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_two_bosonic_corrections.py).
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
The [complete calculated bosonic certificate](../../../../../../../../references/source_evidence/log/derivations/bosonic.md) now reproduces this entire density
from the actual calculated zero-fermion slots with explicit boundary currents.
The unrestricted fermionic component and nonlinear supersymmetry checks remain separate. No prior spectrum
conclusion is imported by recording this bosonic result.
