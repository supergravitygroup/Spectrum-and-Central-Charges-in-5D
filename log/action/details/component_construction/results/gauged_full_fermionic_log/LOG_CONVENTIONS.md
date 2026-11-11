# LOG working conventions and step 1 derivation

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Supercovariant derivative convention.** Use the full supercovariant $`\mathcal D_a`$ and the conformal box $`\Box^c=\mathcal D^a\mathcal D_a`$, exactly as in the [fermionic gauged Weyl-squared calculation](../../../../../../weyl2/action/details/construction.md), GC14–GC24. Its Q/S/K and implicit fermionic contributions stay inside the operators. Gauge evaluation follows each ordered differentiation; derivatives of the fixed dilaton/dilatino are not silently set to zero. The [active LOG endpoint](../../../construction.md) uses this policy. Gold superspace source formulas retain $`\nabla_A`$ until the complete bridge is applied.

**Step 2 continuation:** [STEP_02_LOG_PRIMARY.md](STEP_02_LOG_PRIMARY.md) now derives **all 58 terms**, from $`W^0`$ through $`W^{-6}`$. Equations (S2-173)–(S2-192) complete the two $`W^0`$ terms, and (S2-193) collects the full definition-derived primary. Fifty-seven terms agree with S23 (3.25); (S2-79)–(S2-81) establish the **gradient-$`X`$ coefficient $`+i/4`$**, opposite to the printed $`-i/4`$. The literal source remains unchanged. Full-primary defining-projector equality and curved S/K/linearity now pass. Project-frame projection, canonicalization, reality, current conservation and BF construction are certified through the retained order in [the current certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The conservation and supersymmetry conclusions use verified multiplet premises and the complete superform proof; a separate brute-force variation of all expanded terms is not claimed. The continuation imports the main reference and this ledger; it does not change a step-1 convention. The generic current/form gate is resolved separately by [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md).

**Step 3 continuation:** [STEP_03_LOG_SPINOR.md](STEP_03_LOG_SPINOR.md) differentiates our 58-term primary by S23 (3.26a), retaining the H3.9 correction. It displays every graded product and its evaluated covariant geometric expansion, with the collected result (S3-200) at the end. Standard torsion and curvature tensors remain explicit; no spinor derivative or generator action remains in the endpoint. Independent flat seventh-derivative checks, weights and index checks pass. Step 6 and the current certificate supply the retained-order component projection, canonicalization and reality; full-primary S/K is independently verified. This continuation changes no step-1 formula.

**Step 4 continuation:** [STEP_04_LOG_SCALAR.md](STEP_04_LOG_SCALAR.md) takes the scalar trace of the calculated spinor and preserves all 58 primary inputs. The endpoint is an **unprojected Gold-frame superfield**, at the same stage as $`H^{ij}`$ and the LOG spinor. It retains $`W_{ab}`$, $`X_\alpha^i`$, $`X_{\alpha\beta}^{ij}`$, $`Y`$, the superspace geometric tensors and full covariant vector derivatives; all spinor derivatives and generator actions are evaluated. This endpoint deliberately remains in the source frame; its component projection and conversion are carried out in Step 6 and certified at the retained order. Independent original eight-derivative flat checks pass; the checked algebraic sector remains $`69W^{ab}W_{ab}Y/1024+3Y^2/2048`$. The complete earlier [once-projected result](STEP_04_LOG_SCALAR_PROJECTED_REFERENCE.md) is retained separately for comparison, without project-convention conversion; its coefficient audit remains in [note 05](notes/05_two_bosonic_corrections_source_audit.md). Retained-order component projection/canonicalization/reality and full-primary S/K are now certified; equality to every literal all-fermion C24 term is not asserted. No step-1 formula is changed.

**Step 5 continuation:** [STEP_05_LOG_VECTOR.md](STEP_05_LOG_VECTOR.md) takes the gamma trace of our calculated spinor, using $`\mathcal H^a=i(\Gamma^a)^{\alpha\beta}\nabla_{\alpha i}\varphi_\beta^i/4`$. This descendant displays explicit fermion degrees zero and two, with $`+\text{high fermi term}`$ for degree four and higher. Cubic spinor and quartic primary contributions are retained during differentiation. The endpoint remains in Gold superspace with full vector derivatives and the defined geometric tensors; common component projection and project conversion are supplied by Step 6. The original eight-derivative flat checks, flat divergence, full-index spinor/scalar/vector trace check, and both $`3/32`$ Weyl–$`Y`$ derivative sectors pass. The result is a nonminimal tensor expansion. The later certificate establishes full-primary S/K/linearity, retained reality and the component constraint/transformation theorem. FORM-01 is resolved for a genuine linear multiplet by [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md). This scoped truncation changes no step-1 equation or full-invariant lock.

**Step 6 continuation:** [STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md](STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md) applies the common bar projection and full field/curvature bridge to all four calculated slots. The endpoint retains zero/two explicit fermions in the even slots and one in the spinor, with the specified higher remainder. C24 (A.4) eliminates the higher Weyl tensors in favor of project R(Q), R(M), R(V), T, chi and D; the indexed matrix placement remains step 2 (S2-02), distinguished from note 07's bilinear kernel. Full covariant vector derivatives and odd-factor order are preserved. The BF expression stays compact, and the entire bosonic triplet is degauged explicitly. The later independent bosonic reduction starts from the calculated components and reproduces the complete LOG-CORR05 action plus an explicit boundary current. The generic FORM-01 closure is proved in [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md). No unrestricted invariant or nonlinear-SUSY lock is issued. Evidence: `sources/step6/`.

Date: 2026-09-22. Working record: `GAUGED-LOG-STEP1-v1`.

**Status (FORM update 2026-09-25):** the covariant four-slot Q/S map, all seven BF slots, bosonic overall normalization and explicit curvature chi sector are checked. [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md) derives the full ordinary current, potential law and closed-five-form BF action. FORM-01 is resolved conditional on a genuine linear multiplet. The printed Gold current/form formulas still require the explicitly identified repairs; the actual expanded LOG multiplet and retained gauged realization have their own completed certificate.

This ledger records the LOG component conventions. The [branch conventions](CONVENTIONS.md) specify the source formulas and their conversion to the component conventions used here.

<!-- ASSERT_CONVENTION: regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->
<!-- LOG_STEP1_CONVENTIONS: parent=GAUGED-LOG-CONVENTIONS-v1; procedure=GAUGED-LOG-G25-S23-PROCEDURE-v1; metric_signature=(-,+,+,+,+); scope=classical off-shell generic multiplet bridge; fermions=all degrees retained; gauge=unfixed -->

## 1. Problem and Target

The convention and normalization bridge is step 1 of the [construction sequence](notes/06_complete_construction_sequence.md), preceding the LOG primary, its descendants, the BF density, the gauged-field substitution and the target gauge.

The assumptions used throughout are:

1. **A1:** classical local superconformal fields in five dimensions, off shell; no target-action equations of motion or auxiliary elimination.
2. **A2:** every fermion degree is retained; boundary terms are kept except where an equality is explicitly marked modulo a divergence.
3. **A3:** the defining scalar has the local patch $`W>0`$, corresponding to $`\rho>0`$. The independent linear compensator is distinct from the composite LOG multiplet.
4. **A4:** the gauge in the bosonic normalization probe is a diagnostic specialization, not a gauge imposed on the construction. The form-potential comparison is local; no global cohomological equivalence is assumed.

| Source input | Exact equations | Saved evidence |
|---|---|---|
| Gold component paper, C24 | Appendix C, Tables 4–6 and preceding paragraph | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF90](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF91](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF92](https://arxiv.org/abs/2311.00679) |
| Gold generic linear multiplet | C24 (2.50)–(2.54) | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF22](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF23](https://arxiv.org/abs/2311.00679) |
| Full superform input | Butter et al., arXiv:1410.8682v2 (8.3)–(8.9), (8.19)–(8.30), C24 ref. 30 | [exact equation cache](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/form/source_equations.json), [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md) |
| Gold full BF | S23 (3.2b), (3.27b); C24 (3.2b–c) | [S23 PDF14](https://arxiv.org/abs/2302.14295), [C24 PDF24](https://arxiv.org/abs/2311.00679) |
| Component linear laws | OP (2.18)–(2.24) | [Supersymmetric Completion of Gauss-Bonnet Combination in Five Dimensions — PDF9](https://arxiv.org/abs/1301.6622), [Supersymmetric Completion of Gauss-Bonnet Combination in Five Dimensions — PDF10](https://arxiv.org/abs/1301.6622) |
| Component density and current | OP (3.1)–(3.2); OPall (3.1)–(3.2) | [OP PDF10](https://arxiv.org/abs/1301.6622), [OPall PDF8](https://arxiv.org/abs/1306.1540) |
| Curvature comparison | C24 (2.18c), Table 4; W (3.20); OP (2.7) | [C24 PDF13](https://arxiv.org/abs/2311.00679); master R03, X01 |
| Bosonic normalization | C24 (5.20); G25 (1), (11) | [C24 PDF45](https://arxiv.org/abs/2311.00679); master LOG-B01, LOG-B03 |

The source keys and exact local versions are defined in the main convention file. C24 means the local Gold component paper with supplement, not a newly retrieved edition. The source PDFs are unchanged.

## 2. Convention Ledger

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

## 3. Definitions and Required Identities

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

## 4. Detailed Derivation

### 4.1 Four covariant linear slots

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

Every intermediate scalar/vector coefficient and the rank-three reduction are given in the [independent audit](notes/07_step1_linear_bridge_independent_check.md), sections 4.2–4.3. Thus all four **covariant Q/S laws** match. These homogeneous laws leave $`a`$ free. Choose $`a=-1/2`$ so that the six nonform density terms have unit component normalization:

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

### 4.2 Explicit chi curvature: index order resolves the apparent sign

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

### 4.3 Seven BF terms and the form residual

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

### 4.4 Ordinary form representative and a local supersymmetry diagnostic

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

The explicit superfour-form pullback proves the required relation $`\mathcal H_G^a=h_G^a-Q_1^a-Q_2^a`$. Literal source minus required is **$`2Q_1^a`$ only**. The earlier plus-$`Q_2`$ conversion in this ledger and note 07 came from lowering the second spinor index on the wrong side: the tensor is $`M\mathsf C^T=-M\mathsf C`$, yielding the bilinear kernel $`-\mathsf C M`$. The corrected (LB42)–(LB44) and [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md), (FI03)–(FI18), give all intermediate steps. Original-PDF glyph positions confirm the source doublet placement; a guessed reversal is not a correction. Evidence is saved in [the glyph audit](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step1/glyph_evidence.json).

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

The component current (LOG-S1-06), density (LOG-S1-16), and potential law with $`(\alpha,\beta)=(1,-3)`$ are now derived by [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md), (FI09)–(FI31). The graded superfour-form pullback supplies the full potential law; the closed superfive-form supplies generic BF invariance. The original arXiv:1410.8682v2 (8.28)–(8.29) explicitly uses the ordinary dual $`h_G`$ in the vector coupling, resolving the C24/S23 (3.2b) symbol mismatch. These are **derived repairs**, kept separate from literal source displays. This closes FORM-01 for a genuine linear multiplet without promoting the principal test above to a complete proof of the expanded LOG polynomials.

### 4.5 Bosonic overall normalization without borrowing another invariant

Use only a normalization probe: set $`W=1`$, fermions, gauge strengths, T and g to zero. The nonzero scalar auxiliary is still fixed by the defining dilaton-Weyl map: $`D=-R_B/32=R_G/32`$. The relevant C24 (5.20) terms are

```math
-\tfrac16R_{Gab}R_G^{ab}
+\tfrac{23}{384}R_G^2-\tfrac12R_GD-\tfrac83D^2.
\tag{LOG-S1-22}
```

Their scalar-curvature coefficient is

```math
\frac{23}{384}-\frac1{64}-\frac1{384}=\frac1{24}.
\tag{LOG-S1-23}
```

Since the Ricci square is unchanged by $`R_G=-R_B`$, this gives exactly $`-R_{Bab}R_B^{ab}/6+R_B^2/24`$, the curvature-only G25 (11) normalization. The multiplier is one in this bosonic sector. This calculation does not rely on either of the two disputed bosonic $`w`$ coefficients, because $`w=0`$ in the probe. It also cannot certify fermionic form terms that vanish in the probe.

The target coupling remains

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,
\left(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\rm LOG}\right),
\qquad [\kappa_5^2]=-3,\quad [\lambda_{\rm LOG}]=-2.
\tag{LOG-S1-24}
```

## 5. Consistency Checks

The generic superconformal Weyl weights are $`w(L,\varphi,N,E)=(3,7/2,4,4)`$, $`w(\rho,\lambda,Y,A_a)=(1,3/2,2,1)`$, and $`w(\psi_a)=1/2`$. Every BF term and both current-completion terms have respectively weights five and four. The normalization $`a`$ is dimensionless. These conformal weights are distinct from the gauge-fixed engineering assignments used for the target action, where both terms in its parentheses have mass dimension two after including $`\lambda_{\rm LOG}`$.

Checks and their scope are saved in [step1/checks.json](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step1/checks.json): explicit Clifford/duality matrices, doublet lowering, exact slot and BF coefficients, antisymmetrized curvature order, a Grassmann-polynomial test of local-parameter cancellation, the curvature normalization probe and dependency hashes. The tests deliberately include the failing printed potential coefficients, so a PASS means the discrepancy was detected, not that the printed formula became valid.

The bosonic limit makes $`Q_1=Q_2=0`$, removes the residual (LOG-S1-15) and reproduces the earlier bosonic map. No g appears in this generic Standard-Weyl bridge; gauging is a later substitution. Boundary equivalence is used only in (LOG-S1-18). The independent audit is linked above. Markdown math is checked with the installed VS Code KaTeX renderer; no PDF is generated.

## 6. Final Result

For subsequent LOG algebra use (LOG-S1-02)–(LOG-S1-04) with the covariant-slot map (LOG-S1-12). The operational component BF formula is (LOG-S1-16), with P explicitly defined by (LOG-S1-06). Its six nonform terms match the raw Gold BF terms with unit normalization, and its bosonic curvature sector matches G25 without an additional multiplier. The explicit chi-curvature repair agrees with C24 once index order is aligned.

This file records the generic bridge and the source-grounded FORM-01 repair. The ordinary current and compact BF density are certified by the superform argument for genuine vector and linear multiplets. The current certificate independently verifies that the particular LOG descendants and retained gauged substitutions satisfy those hypotheses; no literal incompatible source formula is silently relabeled as verified.

## 7. Convention Dependence and Remaining Uncertainties

1. **FORM-01 — resolved at the generic interface:** [the superform certification](../../../../../../references/source_evidence/log/derivations/form-interface.md) derives the full four-form current/potential and the closed-five-form action. C24 (2.50) needs the one-gravitino sign repair; C24/S23 (3.2b) needs the ordinary dual in its vector coupling. The actual LOG primary and its retained gauged transport are now verified in the current certificate.
2. **FORM-02:** retain literal OP (2.24) as a quarantined source record. The operational $`(1,-3)`$ coefficients now follow from the full superform contraction; label this derived repair when comparing to the literal OP law.
3. **BRIDGE-01:** the chi sector and four covariant Q/S laws are checked. The complete primitive projection and derivative/connection bridge are now checked in the separate projection certificate.
4. **LATER-STEPS:** retained descendants, gauged substitution and BF construction are now certified; separately expanded all-order gauge-algebra closure and omitted higher-fermion action terms remain outside scope. The old scalar-descendant and $`Rww`$ audits retain their qualified status in master LOG-CORR01–05 and note 05; no new unqualified erratum is asserted here.

Relation identifiers connect the geometric conventions, component maps and LOG-specific descendants.

<!-- LOG_SOURCE_ALGEBRA_REPAIR_20260925 -->

## Source-algebra repair used in the scalar and vector descents

The master [CONVENTIONS.md](CONVENTIONS.md), (G-C24-A1l-repair), preserves literal C24 (A.1l) and separately states the Jacobi-required coefficients $`+i/8,-i/4`$ for its two K-generator terms. The exact source-local proof is [the curved certification report](../../../../../../references/source_evidence/log/derivations/curved.md), (CC-03)–(CC-11). No other generator or frame coefficient is changed. All cached source pages remain immutable. The calculation rebuilds the scalar and vector from the repaired algebra; projection and Clifford reduction are applied afterward. See [propagation evidence](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md).
