# Complete construction sequence: full fermionic gauged LOG invariant

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

The sequence below organizes the defining equations, component descent and retained-order action.

The construction forms the complete LOG linear multiplet and its Standard-Weyl BF action, substitutes the full gauged dilaton-Weyl realization, and then imposes the target Poincaré gauge. This is the order prescribed immediately after G25 (10), PDF p.9. All formulas below are used with [CONVENTIONS.md](../CONVENTIONS.md), lock `GAUGED-LOG-CONVENTIONS-v1`; the [existing equation map](02_equation_reference_map.md) supplies further cached locators.

The construction is classical, off shell and un-dualized. Intermediate expressions retain the fermion degrees needed for the displayed two-fermion action. The construction uses off-shell fields and exact dependence on the LOG coupling. The defining improved-vector constraints in step 7 specify the chosen Weyl-multiplet realization. The final normalization is

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2\partial}+\lambda_{\rm LOG}\ell_{\rm LOG}\bigr),
\qquad [\lambda_{\rm LOG}]=-2.
```

This declares the target convention; the conversion of the raw S23 BF coefficient into this normalization is established by the current slot and full-superform certificates.

## Sources and field roles

Page numbers below count PDF pages from one. The C24 supplement restarts its printed page numbering.

| Key | Local source |
|---|---|
| S23 | [Gold et al., *On curvature-squared invariants from superspace*](../../../EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8), arXiv:2302.14295v2 |
| C24 | [Gold et al., *Components of curvature-squared invariants* and supplement](../../../EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4), local arXiv:2311.00679v1 |
| G25 | [Gold et al., *On five-dimensional curvature squared supergravity and holography*](../../../EXTERNAL_REFERENCES.md#ref-f480139fecd5), arXiv:2504.10856v1 |
| W | [Bergshoeff et al., *Weyl multiplets of N = 2 conformal supergravity in five dimensions*](../../../EXTERNAL_REFERENCES.md#ref-2cf4df97c0da), hep-th/0104113v4 |
| CO | [Coomans–Özkan, internally gauged supergravity](../../../EXTERNAL_REFERENCES.md#ref-91993860706d), arXiv:1210.4704v3 |
| OP | [Özkan–Pang, Gauss–Bonnet completion](../../../EXTERNAL_REFERENCES.md#ref-16b843794969), arXiv:1301.6622v4 |

S23's five-dimensional $`\mathcal N=1`$ and the project's $`\mathcal N=2`$ denote the same eight real supercharges. Until the bridge is applied, keep Gold symbols and spinor contractions unchanged:

- $`(W,v_\mu,\lambda^i,X^{ij})`$ is the defining vector multiplet; $`W_{ab}`$ is instead the super-Weyl tensor.
- $`(H_{\log}^{ij},\varphi_{\log}^i,F_{\log},\mathcal H_{\log}^a)`$ is the **composite LOG linear multiplet**.
- $`(L_c^{ij},\varphi_c^i,N_c,E_c^a)`$ is the **independent compensator** in component notation; $`E_{c\,\mu\nu\rho}`$ is its form potential.
- The component dilatino $`\psi^i`$ differs from the gravitino $`\psi_\mu^i`$. The LOG vector $`\mathcal H_{\log}^a`$ differs from the dilaton-Weyl three-form $`\widehat H_{abc}`$ and its dual two-form $`H_{ab}`$.

The thirteen calculation steps refine, without changing, the seven locked stages:

| Locked stage | Calculation steps |
|---|---|
| 1. Convention and normalization bridge | 1 |
| 2. Complete LOG multiplet | 2–5 |
| 3. Standard-Weyl BF invariant | 6 |
| 4. Full gauged realization | 7–8 |
| 5. Target gauge | 9 |
| 6. Component collection | 10 |
| 7. Component and action checks | 11–13 |

## 1. Establish the complete convention and normalization bridge

Component derivation: [LOG_CONVENTIONS.md](../LOG_CONVENTIONS.md), 2026-09-22.
The covariant Q/S slots, six nonform BF terms, bosonic normalization and explicit
chi-curvature interface are checked. The printed current/form conflict is
isolated with a necessary local-SUSY test; the later full-superform derivation resolves the generic current and potential interface.

The bridge uses C24 Appendix C, Tables 4–6 (PDF pp.91–92), including the field-dependent Q/S/K parameter shifts; supplement (1.1)–(1.2) (PDF p.103); and W (A.4), (A.9)–(A.10), (A.15)–(A.17). It specifies metric/Riemann signs, gamma and epsilon conventions, Majorana bars, SU(2) raising, Grassmann order and dependent connections.

The conversion of **all four LOG slots**, the defining vector, and the full density uses S23 (3.2), (3.27), C24 (3.2), (5.9b), and OP (3.1)–(3.2). The conversion includes the constrained-vector/form representative and scalar couplings. G25 (9), (11) provide bosonic normalization comparisons, not substitutes for the fermionic matching.

**Component result:** the convention bridge specifies the conversion table and common density normalization, including all BF slots, generators, connections and the project $`R(M)`$ correction. The local patch is $`W>0`$, $`\sigma>0`$ and $`L\ne0`$.

## 2. Construct the complete LOG primary

S23 (3.24), PDF p.20, defines the primary:

```math
H_{\log W}^{ij}
=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W
=\frac{3i}{1280}\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
```

The component sources are S23 (3.25), PDF pp.21–22, and C24 (4.7), (4.8a), PDF pp.32–34. The cached primary has 58 source summands, including quartic and sextic fermions. G25 (10) is truncated and cannot replace it.

**Component result:** the primary has weight three. Its primarity and $`\nabla_\alpha^{(i}H_{\log}^{jk)}=0`$ are checked using the defining algebra; the certificate distinguishes those checks from the source summand count.

## 3. Calculate the spinor descendant

S23 (3.26a), PDF p.22, defines the spinor descendant:

```math
\varphi_{\log W}^{\alpha i}
=\frac13\nabla_j^\alpha H_{\log W}^{ij}.
```

The derivative algebra evaluates this descendant. C24 supplement §2.2.1, PDF pp.106–112 / printed pp.7–13, gives its source component expression. C24 (2.16) specifies component projection, and (2.41)–(2.42) give the descendant identities.

**Component result:** the spinor descendant has weight $`7/2`$, with the stated covariant dependencies and spinor order. Its defining relation and component projection are recorded in the descent and projection derivations.

## 4. Calculate the scalar descendant and resolve its projection

S23 (3.26b) defines the scalar descendant:

```math
F_{\log W}=\frac i{12}\nabla_i^\alpha\nabla_{\alpha j}H_{\log W}^{ij}.
```

The **full** source expression is in C24 supplement §2.2.2, PDF pp.113–121 / printed pp.14–22, including fermions. The raw Weyl descendants are projected with supplement (1.2), exactly once. Here $`w_{ab}=W_{ab}|`$ is the Standard-Weyl two-form and $`D`$ its auxiliary scalar. In particular,

```math
D=-\frac3{128}Y\big|,
\qquad \frac{69}{1024}w^{ab}w_{ab}Y\big|
=-\frac{23}{8}w^{ab}w_{ab}D.
```

C24 (4.8b) prints a discrepant number; C24 (5.20) **already** has the consistent $`+23w^2D/8`$ action term after the BF sign. The [source audit](05_two_bosonic_corrections_source_audit.md) establishes that distinction. A repeated conversion is only a possible explanation of the printed number.

**Component result:** the scalar descendant, its weight-four check and projection ledger are given in the component derivation. The bosonic certificate compares the primary-derived sector with the corrected action.

## 5. Calculate the constrained vector and verify the multiplet

S23 (3.26c) defines the vector descendant:

```math
\mathcal H_{\log W}^a
=\frac i{12}(\Gamma^a)^{\alpha\beta}
\nabla_{\alpha i}\nabla_{\beta j}H_{\log W}^{ij}.
```

C24 supplement §2.2.3, PDF pp.121–149 / printed pp.22–50, gives the source expression; C24 (2.50)–(2.54) specifies the component/form bridge. Superspace conservation $`\nabla_a\mathcal H_{\log}^a=0`$ must be converted to the full component constraint; it is not permission to discard gravitino contributions.

**Component result:** the vector slot and its form representative obey the stated multiplet constraint. The full superform pullback supplies the potential/current relation and resolves the `X10` interface; the source transcription and derived repair remain distinguished.

## 6. Assemble the seven-term Standard-Weyl BF invariant

Insertion of the multiplet into S23 (3.2) gives S23 (3.27b), supported by C24 (5.9b), PDF p.41:

```math
\begin{aligned}
S_{\log W}=-\int d^5x\,e\Big[&
v_a\mathcal H_{\log W}^a+WF_{\log W}
+X_{ij}H_{\log W}^{ij}+2\lambda^k\varphi_{k\log W}\\
&-\psi_{ai}\Gamma^a\varphi_{\log W}^iW
-i\psi_{ai}\Gamma^a\lambda_jH_{\log W}^{ij}
+i\psi_{ai}\Sigma^{ab}\psi_{bj}WH_{\log W}^{ij}\Big].
\end{aligned}
```

These are Gold spinor contractions; their explicit indices are fixed by S23 (3.2b), reproduced in the convention file. The density retains the overall minus sign and all three explicit gravitino terms.

**Component result:** the Standard-Weyl density retains each BF slot and its gravitino contributions. The component checks specify weight, reality, normalization and boundary currents at the retained fermion order.

## 7. Derive and substitute the complete gauged composite map

The gauged substitution G25 (1), (4) follows BF assembly, as specified after (10). The full improved-vector constraints W (5.10)–(5.14), PDF p.28, and CO (5.2)–(5.8), PDF pp.16–17, supply the supporting fermionic definitions.

The constraint chain begins with $`S^{ij}+gL_c^{ij}=0`$ and yields the spinor, scalar and vector shifts. The audited project candidates are `GC01`–`GC05`, `GA03`, `GC08`, `GC11`, `GC12` in [the shared gauged calculation](../../../../../../../weyl2/action/details/construction.md), displayed in the conventions ledger. These are project relations, not published LOG equations.

**Component input:** the complete $`Y^{ij},\chi^i,D,T_{ab}`$ and defining-vector substitutions are specified by the supporting constraints and project covariants. CO (5.3)–(5.4) display a cubic/quartic truncation. This realization is distinct from the LOG multiplet in steps 2–5.

## 8. Resolve dependent connections, covariants and the gauged three-form

The dependent connections $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$, curvatures and covariant derivatives use C24 (2.16), (2.24), (2.27), (2.37)–(2.39), (2.53), its supplement §§5.1–5.3, and project `GC14`–`GC24`. The presentation in [Step 7](../../../../construction.md) retains full $`\mathcal D_a`$ and $`\Box^c`$, including the Q/S/K terms and implicit fermions. Gauge evaluation follows ordered differentiation. The certificate identifies the ordered-connection defect in earlier connection-expanded expressions.

CO (5.5)–(5.8) specifies the full supercovariant three-form. Its **bosonic restriction**, with the locked form normalization, is

```math
H_3=dB+\frac12C\wedge G+\frac g2E_c,
\qquad dH_3=\frac12G\wedge G+\frac g2dE_c,
\qquad G=dC.
```

The resulting project identity `LOG-CORR01` is

```math
\nabla_bH^{ab}=-\frac1{16}\epsilon^{abcde}G_{bc}G_{de}
+\frac g2E_c^a.
```

**Component result:** the covariant definitions retain their fermion content and the gauged Bianchi/form-gauge identities, including the compensator contribution to the divergence.

## 9. Impose the target gauge and derive its preserving transformations

The gauge is G25 (7), (25), (27), and OP (4.1)–(4.2):

```math
\begin{gathered}
\sigma=1,\qquad b_\mu=0,\qquad\psi^i=0,\qquad
L_c^{ij}=\frac{\delta^{ij}}{\sqrt2}L,\\
V_a^{ij}=V_a'{}^{ij}+\frac12\delta^{ij}V_a,
\qquad\delta_{ij}V_a'{}^{ij}=0.
\end{gathered}
```

The retained fields include $`\psi_\mu^i`$ and $`\varphi_c^i`$, together with $`L,N_c,E_c,V,V'`$. A vanishing dilatino does not make its supercovariant derivative vanish. Gauge preservation is specified by CO (2.15), (2.20), OP (2.1), the C24 Table 5 parameter bridge, and project `LOG-G02`.

**Gauge scope:** the density uses the specified gauge and exact covariant derivatives. The `LOG-G02` equations give gauge preservation; OP (4.3) is used within its ungauged, fermion-truncated domain.

## 10. Collect the complete component action

Lorentz and SU(2) contractions use W (A.9)–(A.10), (A.15)–(A.17), in the bridged conventions. The [fermion-order ledger](../FERMION_ORDER_LEDGER.md) organizes

```math
\ell_{\rm LOG}=\sum_{n,p}g^p\ell_{\rm LOG}^{(n,p)},
```

where $`n`$ is the actual fermion degree after substitutions, and $`p`$ the gauging power. The displayed action retains $`n=0,2`$, while differentiation retains the higher intermediate degrees required to obtain those components.

**Component result:** the ledger records the coefficient, BF slot, physical fermion degree, gauging power and boundary reduction for the retained terms. Compact covariants retain their explicit definitions.

## 11. Reproduce the bosonic limit and reconcile source discrepancies

The bosonic restriction is compared in the same frame and boundary representative with G25 (11), C24 supplement §3.1, and the [definition-derived project result](../../../../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex), label `eq:L-final-expanded`, denoted `LOG-CORR05`.

The comparison includes the gauged $`E_c`$ sector `LOG-CORR01`–`LOG-CORR02` and the scalar projection from step 4. For $`R^{\rm S}_{abcd}w^{ab}w^{cd}`$, the raw supplement reduces to $`3/8`$, whereas C24 (5.20) prints $`1/4`$, with the boundary current and C24 (2.21) commutator specified in [the audit](05_two_bosonic_corrections_source_audit.md). The source audit is conditional on the raw supplement; the separate bosonic certificate reconstructs this sector from the calculated primary and descendants.

**Component result:** the bosonic comparison gives explicit divergences and coefficient differences. These discrepancies are already incorporated in the corrected density and are project-derived findings.

## 12. Verify the normalized ungauged limit

The $`g\to0`$ restriction uses the matching field, density and boundary conventions of CO (5.2)–(5.8), OP (2.9), S23 (3.27b) and C24 (5.9b). The certificate records how the symbolic component identities pass to this limit.

**Limit:** the identities retain symbolic $`g`$ without division by $`g`$, so their $`g=0`$ restriction preserves the normalized ungauged BF construction at the retained fermion order.

## 13. Retained-order supersymmetry and component checks

The full linear laws S23 (2.20)–(2.24), C24 (2.40)–(2.44), (2.50)–(2.54), together with the verified primary and closed BF superform, supply the action-level supersymmetry argument. The local invariance condition is

```math
\delta_\epsilon(e\ell_{\rm LOG})=\partial_\mu J^\mu_\epsilon,
```

with off-shell fields. For the displayed action through two physical fermions, the certificate supports cancellation through one physical fermion, up to the stated boundary terms. Integrated invariance depends on the boundary integral.

**Verification scope:** the component certificate records the primary, projection, coefficient, reality, bosonic and ungauged checks. Its retained-order action argument uses the verified multiplet and closed BF superform, with the stated normalization, gauge and boundary representative.

The [component certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) links the results and evidence for this retained-order construction.
