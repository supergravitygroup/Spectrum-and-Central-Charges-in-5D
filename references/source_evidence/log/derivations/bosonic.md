# LOG bosonic certification

The equations and reported residuals below belong to the cited construction. Finite component tests and formal symbolic identities retain their distinct scopes; the former do not establish an unrestricted symbolic identity.


## Problem and Target

The actual calculated triplet, scalar and vector give the corrected project LOG action, including every flux, derivative and independent-compensator-vector term. The equality is local after adding the explicit total divergence in (B-13). It requires no field equation, auxiliary-field elimination, dualization or background ansatz.

The [equation companion](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md) displays the complete calculated bosonic triplet/scalar, the full vector potential, the two intermediate boundary currents, their collected sum, the complete target action, and all weighted pointwise relations used in the final vector/density certificates. This compares the calculated polynomials; it does not copy a source-action reduction or appeal to a superspace existence theorem.

## Convention Ledger

Use `GAUGED-LOG-CONVENTIONS-v1`, five-dimensional mostly-plus metric, $`\epsilon^{01234}=+1`$, weighted antisymmetrization, project Riemann/Ricci contractions, and the established source/component bridge. Fourier, quantum-state and renormalization conventions do not enter this classical calculation. Keep the LOG-CORR05 action normalization, $`g`$, and higher-derivative coupling convention of LOG-G03.

1. Set all fermions to zero for this audit. Their hidden contributions vanish here; no two-fermion coefficient is certified by this test.
2. Evaluate the full covariant derivatives before imposing $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$. In particular retain the bosonic special-conformal terms in $`\mathcal D_a\mathcal D_b\sigma`$ and higher derivatives.
3. Preserve the independent linear compensator $`L_c^{ij},N_c,E_c^a`$. Its orientation gauge is compatible with the covariant expressions; a constant aligned triplet can have nonzero $`SU(2)`$ covariant derivative.
4. In this internal comparison only, $`\nabla_a`$ denotes the ordinary torsion-free Lorentz/$`SU(2)`$ derivative after the superconformal connections have been evaluated. This does **not** redefine $`\mathcal D_a`$ or $`\Box^c`$ in the active full-component documents.
5. Retain the boundary currents. Integrated actions agree if their displayed boundary integral vanishes; the local equality with the current retained requires no boundary assumption.

The bosonic dependent-connection constraint gives

```math
f_{ab}=-\frac16R_{ab}+\frac1{48}\eta_{ab}R,\qquad f^a{}_a=-\frac1{16}R,\qquad R_{ab}=-6f_{ab}-2\eta_{ab}f^c{}_c.\tag{B-01}
```

Thus $`f_{ab}`$ is symmetric **on this zero-fermion body only**. This does not restore the incorrect full-fermionic symmetry rule. The bosonic Lorentz-curvature trace/decomposition are

```math
R(M)_{ab}{}^{cb}=0,\qquad R_{abcd}=R(M)_{abcd}-2\left(f_{ac}\eta_{bd}-f_{bc}\eta_{ad}-f_{ad}\eta_{bc}+f_{bd}\eta_{ac}\right).\tag{B-02}
```

The bosonic $`R(Q)`$ constraint is identically satisfied because all fermions vanish. Sources: branch conventions R03–R04, C24 (2.23), and the established Step 1/Step 6 bridge.

## Definitions and Required Identities

| Located source | Use |
| --- | --- |
| S23 (3.24)–(3.26), already calculated outputs | Original full-covariant LOG component polynomials |
| S23 (3.2), (3.27); locked component BF density | $`\ell_{\rm BF}^{(0)}=N_{\log}^{(0)}-gL_c^{ij}L_{\log\,ij}^{(0)}/2+C_aE_{\log}^{a(0)}`$ |
| C24 (4.8d), PDF36; (4.9); (4.10b–c), PDF37 | Independently transcribed complete bosonic vector potential and its degauging completion |
| C24 Appendix A (A.4c), cached PDF83 | Traceless Lorentz-curvature bridge |
| C24 (4.11), PDF37; project R03 | Ordinary derivative commutators and Bianchi reductions |
| [Original standard ledger](../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex), `eq:L-standard-ledger` | Full independent Standard-Weyl target, including corrected $`R_{abcd}w^{ab}w^{cd}`$ coefficient $`3/8`$ |
| [Branch conventions](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/CONVENTIONS.md), LOG-CORR01–LOG-CORR05 | Gauged $`H`$ Bianchi identity, independent $`E_c`$ terms and full corrected gauged action |

The source/project bosonic dictionary is applied once:

```math
w_{ab}=\frac{16}{3}T_{ab},\qquad F_{G\,ab}=-G_{ab},\qquad \Phi_{G\,ab}^{ij}=-V_{ab}^{ij},\qquad X_G^{ij}=-gL_c^{ij},\qquad R_G(M)=-R(M),\qquad \epsilon_G=-\epsilon.\tag{B-03}
```

In particular $`R_G=16f^a{}_a`$ and $`(R_G)_{ab}=6f_{ab}+2\eta_{ab}f^c{}_c`$. The latter trace term is retained in the source potential completion.

For an ordinary bosonic covariant Lorentz tensor, the commutator sign is

```math
[\nabla_a,\nabla_b]U_{c_1\ldots c_p}=\sum_{r=1}^{p}R_{ab c_r}{}^dU_{c_1\ldots c_{r-1}d c_{r+1}\ldots c_p}.\tag{B-04}
```

When commuting through $`\nabla_cU`$, the derivative index $`c`$ receives its own covector curvature action. Upper slots are raised with $`\eta`$. The generator checks that every encountered derivative interchange on an $`SU(2)`$-indexed field is a contracted zero commutator; no nontrivial $`SU(2)`$ commutator is used with its curvature omitted.

```math
\nabla_aG_{bc}+\nabla_bG_{ca}+\nabla_cG_{ab}=0,\qquad \nabla_eR_{abcd}+\nabla_aR_{becd}+\nabla_bR_{eacd}=0,\qquad \nabla^af_{ab}=\nabla_bf^a{}_a.\tag{B-05}
```

The algebraic curvature identity is $`R(M)_{abcd}+R(M)_{acdb}+R(M)_{adbc}=0`$. Schouten relations come from antisymmetrizing six Lorentz indices in five dimensions, preserving all index positions. The needed triplet identity is

```math
L_c^{ij}L_{c\,i}{}^kL_{c\,j}{}^lL_{c\,kl}=\frac12\left(L_c^{ij}L_{c\,ij}\right)^2.\tag{B-06}
```

An independent symbolic calculation takes $`L_c^{ij}=\begin{pmatrix}a&b\\b&c\end{pmatrix}`$ and obtains $`L_c^2=2ac-2b^2`$, while the quartic chain is $`2a^2c^2-4ab^2c+2b^4`$.

The only gauged three-form identity used is

```math
\nabla_bH^{ab}=-\frac1{16}\epsilon^{abcde}G_{bc}G_{de}+\frac g2E_c^a.\tag{B-07}
```

This is LOG-CORR01's Bianchi identity, not an equation of motion for $`H`$ or $`E_c`$.

## Detailed Derivation

### 1. Rebuild the actual calculated slots

The inputs are the canonical triplet, scalar and vector slots displayed in the [component construction](../../../../log/action/details/construction.md). The full-$`\mathcal D`$ representation has its separate origin-equivalence check. The bosonic comparison reconstructs their zero-fermion gauge values: inverse-map each factor to the source superfield, recursively evaluate its Q/S/K covariant derivatives, apply its component bridge once, then impose the bosonic conventional constraints. Terms with a written fermion cannot contribute at zero-fermion degree and are removed before the recursion.

| Component | Original zero-fermion covariant monomials | Rebuilt ordinary-bosonic monomials | Difference from the bosonic component calculation |
| --- | ---: | ---: | ---: |
| $`L_{\log}^{ij}`$ | 10 | 8 | 0 |
| $`N_{\log}`$ | 127 | 75 | 0 |
| $`E_{\log}^{a}`$ | 332 | 177 | 0 |

The intermediate cache equality is supplementary. The complete rebuilt triplet/scalar expressions used in the comparison are (BC-01)–(BC-02) in the linked equation companion.

### 2. Establish the complete vector as a local divergence

Convert C24 (4.8d) with (B-03), retaining all defining-scalar Hessian/box contributions during bosonic gauge evaluation. Its ordinary first derivative vanishes only after that evaluation. The C24 (4.10c) completion, with $`U^{ab}=16T^{ab}/3-G^{ab}`$, becomes

```math
\widehat Q^{ab}=3f^c{}_cU^{ab}+6f^{c[a}U^{b]}{}_c.\tag{B-08}
```

The resulting potential $`Q^{ab}`$ is displayed as all 34 canonical monomials in (BC-04). Its antisymmetry is checked exactly. Apply the ordinary product rule and form

```math
\Delta E^a=E_{\log}^{a(0)}-\nabla_bQ^{ab}+\frac1{12}\epsilon^{abcde}V_{bc}^{ij}V_{de\,ij}.\tag{B-09}
```

The source divergence has 75 monomials. After tensor/trace normalization, $`\Delta E^a`$ has 157. The explicit identities generate 131 independent rows; the residual becomes exactly zero. Its certificate uses 116 nonzero weighted rows and replays to zero **without any IBP**. The actual weighted contractions appear in the companion's `VE-*` equations. Hence

```math
E_{\log}^{a(0)}=\nabla_bQ^{ab}-\frac1{12}\epsilon^{abcde}V_{bc}^{ij}V_{de\,ij}.\tag{B-10}
```

The bosonic vector constraint follows locally: $`\nabla_a\nabla_bQ^{ab}=\tfrac12[\nabla_a,\nabla_b]Q^{ab}=0`$ because the resulting symmetric Ricci tensors contract the antisymmetric $`Q`$. The $`\epsilon VV`$ divergence vanishes by $`\nabla_{[a}V_{bc]}=0`$. This does not assert the full fermionic conservation constraint.

### 3. Assemble the actual Standard-Weyl BF density

Antisymmetry fixes the BF boundary sign:

```math
\begin{aligned}
C_a\nabla_bQ^{ab}&=\nabla_b(C_aQ^{ab})-(\nabla_bC_a)Q^{ab}=\nabla_b(C_aQ^{ab})+\frac12G_{ab}Q^{ab},\\
\ell_{\mathrm{calc},0}&=N_{\log}^{(0)}-\frac g2L_c^{ij}L_{\log\,ij}^{(0)}+\frac12G_{ab}Q^{ab}.
\end{aligned}\tag{B-11}
```

This calculated non-CS density has 78 canonical monomials. The independently transcribed corrected Standard-Weyl target has 42. Ten preliminary product-rule IBPs leave 39 residual monomials. Each operation is $`(\nabla_aX)Y=\nabla_a(XY)-X\nabla_aY`$, preserving the ordered inner derivatives. The exact reduction uses 27 weighted rows, five of them further product-rule divergences, and leaves zero residual.

All boundary operations collect into the **11-term** $`J_{\mathrm{standard}}^a`$ in (BC-07). Independently subtract its divergence from the original local difference, disable all IBP generators, and reduce again: zero residual, with 22 pointwise rows.

The disputed algebraic scalar sector can be followed directly, with $`L_c^2=L_c^{ij}L_{c\,ij}`$:

```math
\begin{aligned}
N_{\log}^{(0)}\big|_D&=-\frac83D^2-8Df^a{}_a+\frac{736}{9}DT^2+DG^2-3g^2DL_c^2,\\
-\frac g2L_c^{ij}L_{\log\,ij}^{(0)}\big|_D&=6g^2DL_c^2,\qquad \frac12G_{ab}Q^{ab}\big|_D=-\frac{32}{3}D\,G\!\cdot\!T-2DG^2,\\
\ell_{\mathrm{calc},0}\big|_D&=-\frac83D^2-8Df^a{}_a+\frac{736}{9}DT^2-DG^2-\frac{32}{3}D\,G\!\cdot\!T+3g^2DL_c^2.
\end{aligned}\tag{B-12}
```

The subscript selects algebraic terms containing $`D`$; the $`\nabla^2D`$ term belongs to the displayed boundary current. Since $`w=16T/3`$, the $`DT^2`$ coefficient is $`23Dw^2/8`$, matching the corrected ledger without a second application of a projection factor.

### 4. Apply every gauged substitution and compare the full target

Substitute $`T=(G-2H)/8`$ and the complete bosonic $`D`$ in (BC-08) into every Standard-Weyl term, including every derivative, with the ordinary product rule and no derivative reordering. The calculated ledger has 48 canonical terms. Independently transcribe all LOG-CORR05 terms, including its four explicit $`E_c`$ terms; the non-CS target has 43 canonical terms after epsilon-pair reduction.

Six preliminary product-rule IBPs leave 23 residual monomials. Exact reduction generates 37 independent rows: nine Schouten, six gauged-$`H`$ Bianchi, three algebraic-curvature Bianchi, eleven product-rule divergences, five $`dG=0`$, and three ordinary commutator rows. Eighteen weighted rows constitute the certificate, with exactly zero residual. There is no fit of action coefficients; exact rational arithmetic expresses the fixed calculated difference as a sum of verified identities.

The boundary operations collect into the **nine-term** $`J_{\mathrm{gauged}}^a`$ in (BC-09). Its direct pointwise recheck on the original difference also gives zero with IBP disabled, using 12 weighted rows.

The four reproduced independent-compensator-vector contributions are

```math
\frac g3E_{c\,a}\nabla_bG^{ab}-\frac g{24}E_{c\,a}\epsilon^{abcde}G_{bc}G_{de}-\frac{2g}{3}E_{c\,a}\epsilon^{abcde}H_{bc}H_{de}+\frac{g^2}{3}E_{c\,a}E_c^a.
```

An explicit check of the Bianchi conversion uses the temporary contractions $`u^a=\nabla_bH^{ab}`$, $`v^a=\nabla_bG^{ab}`$, $`A^a=\epsilon^{abcde}G_{bc}G_{de}`$ and $`B^a=\epsilon^{abcde}H_{bc}H_{de}`$. Insert $`u=-A/16+gE_c/2`$ into

```math
\frac43u^2+\frac23u\!\cdot\!v+\frac1{12}u\!\cdot\!A-\frac43u\!\cdot\!B+\frac1{24}A\!\cdot\!v-\frac1{12}A\!\cdot\!B.
```

The $`A^2`$ coefficients cancel as $`1/192-1/192`$; the $`A\cdot v`$ coefficients cancel as $`-1/24+1/24`$; and $`A\cdot B`$ cancels as $`1/12-1/12`$. The remainder is $`g^2E_c^2/3+gE_c\cdot v/3-gE_c\cdot A/24-2gE_c\cdot B/3`$, exactly the four terms above. No division by $`g`$ or a differential operator is used.

### 5. Check the final boundary relation directly

The **16-term** $`J^a=J_{\mathrm{standard}}^a|_{\mathrm{gauged}}+J_{\mathrm{gauged}}^a`$ is fully displayed in (BC-10). Subtract its divergence from the original newly calculated non-CS BF density minus LOG-CORR05. The remaining 61 canonical monomials reduce to zero using 33 weighted pointwise identities with **all IBP generators disabled**. These are the companion's `BF-*` equations. Therefore

```math
\boxed{\ell_{\mathrm{BF}}^{(0)}=\ell_{\mathrm{LOG-CORR05}}+\nabla_b\!\left(C_aQ^{ab}|_{\mathrm{gauged}}+J^b\right).}\tag{B-13}
```

The common Chern-Simons term is $`-\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij}/12`$. It was matched by the vector proof before comparing the non-CS polynomials, not omitted from the physical density.

## Consistency Checks

The full results are exact polynomial identities, not finite-background samples. Additional finite tests independently check the implemented conventions:

| Check | Result |
| --- | --- |
| Actual original-to-bosonic $`L,N,E`$ reconstruction | 8/75/177 terms; three cache differences exactly zero |
| Complete actual vector versus divergence potential | Exact zero; 116-row replay; no IBP |
| Actual BF versus corrected Standard-Weyl ledger | Exact zero; 27-row certificate; explicit 11-term current |
| Complete gauged density versus LOG-CORR05 | Exact zero; 18-row certificate; explicit nine-term current |
| Final difference after subtracting the displayed total current | Exact zero; 33-row pointwise replay; no IBP |
| Every monomial's post-gauge engineering dimension | $`[L_{\log}]=3`$, $`[N_{\log}]=[E_{\log}]=4`$, $`[Q]=[J]=3`$, $`[\ell]=4`$ |
| Arbitrary complex symmetric $`SU(2)`$ triplet quartic | Exact symbolic identity |
| Covariant rank-two commutator from explicit connection derivatives | 625 exact integer component checks |
| Differential Riemann Bianchi from symmetric third metric jets | 3125 exact component checks |
| Bosonic Weyl/Schouten and Ricci/scalar signs | 625 Weyl and 25 Ricci components; scalar/contracted-Bianchi checks |
| All six saved certificates replayed independently | Exactly zero residuals |

The finite geometric tests take $`g_{ab}=e^{2\phi}\eta_{ab}`$ with $`\phi=\partial\phi=0`$ at the point and integer symmetric second/third jets. Compute $`\partial_a\Gamma^r{}_{bd}`$ directly, then curvature and its action on a rank-two covariant tensor. This independently confirms the sign in (B-04), the decomposition (B-02), and the derivative-index curvature action. These finite tests supplement the complete formal proof.

The proof is polynomial in $`g`$ with no division by $`g`$, so it includes the ungauged limit. Directly, for $`g=G=H=V=0`$, one has $`D=f^a{}_a/2`$ and $`2\nabla^2f^a{}_a-4\nabla^2D=0`$. The density reduces to $`-6f_{ab}f^{ab}+10(f^a{}_a)^2/3`$. Since $`f_{ab}f^{ab}=R_{ab}R^{ab}/36-11R^2/2304`$ and $`(f^a{}_a)^2=R^2/256`$, this is $`-R_{ab}R^{ab}/6+R^2/24`$, matching LOG-CORR05.

The [complete equation companion](../../../../log/action/details/component_construction/results/gauged_full_fermionic_log/sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md) retains the explicit fields, boundary currents and weighted relations behind these recorded results. The original bosonic replay scripts and intermediate pickle caches are not distributed here; see the [component evidence guide](../../README.md) for the scope of retained source programs and records.

## Final Result

**BOSONIC-CALCULATED-BF-v1: PASS.** The complete actual bosonic LOG multiplet/BF density reproduces corrected LOG-CORR05 with the displayed boundary current. No new bosonic coefficient discrepancy was found. In particular the independent $`E_c`$ sector survives, the disputed scalar projection is consistent in the action, and the Standard-Weyl $`Rww`$ coefficient matches the corrected $`3/8`$ ledger.

## Convention Dependence and Remaining Uncertainties

This closes the full bosonic comparison and bosonic vector conservation. It does **not** certify full curved fermionic primary/descendant identities, fermionic $`R(M)`$ symmetry assumptions, nonlinear Q/S closure, or the FORM-01 potential/current interface. A correct complete bosonic body is a necessary check on the full invariant, not a substitute for the fermionic gates.
