# Equation references for the seven construction steps

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

The source equations and full descendants are given in [CONVENTIONS.md](../CONVENTIONS.md). The retained-order calculation and its verification are specified in the component certificate.

This map follows the [construction sequence](06_complete_construction_sequence.md) and identifies its source equations. The [source registry](../SOURCE_LOCK.md) specifies the inputs and their convention bridge.

| Key | Local source or project note |
|---|---|
| S23 | [Gold et al., superspace construction](../../../EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8), arXiv:2302.14295v2; primary LOG definitions |
| C24 | [Gold et al., components paper and appended supplement](../../../EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4), arXiv:2311.00679v1; locally named 2024 |
| G25 | [Gold et al., gauged curvature-squared paper](../../../EXTERNAL_REFERENCES.md#ref-f480139fecd5), arXiv:2504.10856v1 |
| W | [Bergshoeff et al., 5D Weyl multiplets](../../../EXTERNAL_REFERENCES.md#ref-2cf4df97c0da), hep-th/0104113v4 |
| CO | [Coomans–Özkan, internally gauged supergravity](../../../EXTERNAL_REFERENCES.md#ref-91993860706d), arXiv:1210.4704v3 |
| OP | [Özkan–Pang, Gauss–Bonnet completion](../../../EXTERNAL_REFERENCES.md#ref-16b843794969), arXiv:1301.6622v4 |
| P | [Project gauged full-covariant Weyl calculation](../../../../../../../weyl2/action/details/construction.md); `GCxx`/`GAxx` are project relation IDs |
| B | [Existing corrected project bosonic LOG derivation](../../../../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex); `eq:...` are literal LaTeX labels |

Page cues below mean **PDF pages counted from one**, unless explicitly called printed pages. Main C24 (4.7)/(4.8a) is at PDF pp.32–34 (printed pp.31–33); its supplement restarts printed numbering. Formula locators are published unless marked **project**. Unnumbered supplement formulas are cited by subsection and page, without invented equation numbers.

The selected order follows G25 immediately after (10): **S23 LOG composite and standard-Weyl BF invariant → G25 maps (1), (4) → gauge (7), (25) and connection split (27)**. S23 is G25 reference 33; C24 is reference 34 and supplies expanded component support.

## 1. Convention bridge

| Reference | What it supplies |
|---|---|
| C24 Appendix C, Tables 4–5, PDF p.91 / printed p.90 | Weyl-field, curvature, gamma/epsilon and connection conversion; Q/S/K parameter shifts. These shifts must accompany field conversion |
| C24 Appendix C, Table 6, PDF p.92 / printed p.91 | Vector scalar, gaugino and auxiliary-triplet conversion |
| C24 supplement (1.1a,b), (1.2a,b), PDF p.103 / printed p.4 | Raw symmetric/antisymmetric index shorthand and the superspace `X/Y` to component `chi/D` projections |
| W (A.4), PDF p.32; (A.9)–(A.10), p.33; (A.15)–(A.17), p.34 | Majorana bar, spinor flips, Fierz and Clifford/duality identities in the 5D source conventions |
| S23 (3.2a,b), (3.27a,b); C24 (3.2b,c), (5.9b); G25 (3), (9), (11) | Density normalization and intended gauged bosonic representative to reconcile after converting fields |

The [LOG convention bridge](../LOG_CONVENTIONS.md) specifies the field conversions, Grassmann/SU(2) order and density normalization on the nonzero compensator patch. The fermionic `R(M)` chi-term sign repair is a project-derived correction, distinct from the printed source formulas.

## 2. LOG linear multiplet

| Reference | What it supplies |
|---|---|
| S23 (3.24), PDF p.20 / printed p.19; (3.25), PDF pp.21–22 / printed pp.20–21 | Defining LOG primary and full expanded superfield |
| S23 (3.26a–c), PDF p.22 / printed p.21 | Defining spinor, scalar and vector descendants; expanded expressions are deferred after (3.27) |
| S23 (2.20)–(2.24); (2.6), (2.8c), (2.13), (2.15) | Linear-multiplet constraints, derivative tower, descendants, vector conservation and S laws; algebraic inputs cited by the source for checking primarity |
| C24 (4.7), PDF p.32; complete component (4.8a), pp.32–34 | Component implementation and cross-check of the S23 primary |
| C24 (2.40), (2.41a–d), (2.42a–c), (2.43), (2.44) | Linearity/primarity conditions, descendant derivative identities and definitions, constrained-vector conservation and S laws |
| C24 supplement §2.2.1, PDF p.106 / printed p.7 onward | Full LOG spinor descendant; subsection rather than a numbered equation |
| C24 supplement §2.2.2, PDF p.113 / printed p.14 onward | Full LOG scalar descendant |
| C24 supplement §2.2.3, PDF pp.121–149 / printed pp.22–50 | Full LOG constrained-vector descendant |
| C24 (2.50)–(2.53), PDF pp.22–23 | Component/form bridge, vector constraint, complete component transformation rules and covariant derivatives |

The construction uses S23 (3.24)–(3.26), its linear-multiplet identities and the full C24 descendant support. G25 (10) displays a fermion truncation. The LOG composite is distinct from both the gauged realization in step 4 and the independent compensator. The [component certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) specifies the primary, descendant and constraint checks.

## 3. BF density

| Reference | What it supplies |
|---|---|
| S23 (3.2a,b), PDF p.14 / printed p.13 | General BF action principle |
| S23 (3.27a,b), PDF p.22 / printed p.21; G25 paragraph after (10) | Standard-Weyl LOG invariant obtained by inserting the composite into BF; the gauged map follows only afterward |
| C24 (3.2b,c) | Supporting general component BF density and its representatives, including explicit fermion/gravitino contributions |
| C24 (5.9a,b), PDF p.41 / printed p.40 | Supporting LOG-specific superspace/full component density, including all four LOG slots |
| C24 (2.50), (2.51), (2.54) | Covariant-vector/form-potential relation, constraint and form-potential transformation needed when comparing representatives |
| OP (3.1)–(3.2); **project** P `GA01`–`GA02` | Older vector–linear normalization and the `P/E` bridge to audit when converting to project notation |

The BF assembly retains the source slots and explicit gravitino terms with the stated boundary representative. C24 (5.10) and supplement §3.1 describe bosonic restrictions; C24 (5.9b) supplies the full fermionic density.

## 4. Gauged dilaton-Weyl realization

| Reference | What it supplies |
|---|---|
| G25 (1), (4), and paragraph after (10), PDF p.9 | Apply the standard-to-gauged-dilaton-Weyl map to the already-formed invariant; restore omitted fermions from full supporting inputs |
| W (5.10)–(5.14), PDF p.28 / printed p.27 | Full supercovariant improved-vector constraints and their transformation chain |
| CO (2.15)–(2.17), PDF pp.7–8; (2.20)–(2.23), p.8 | Vector and linear Q/S laws, covariant derivatives, defining field strength, and constrained-vector/form relations |
| CO (5.2), PDF p.16 | Gauged defining-vector auxiliary `Y`; starting point for the shifted constraint |
| CO (5.3)–(5.4), PDF p.16; warning on p.17 | Printed gauged `chi,D` expressions; **cubic/quartic fermions are omitted**, so these alone cannot supply the full map |
| CO (5.5)–(5.8), PDF p.17 | Gauged Bianchi identity, tensor relation, supercovariant three-form and form gauge transformations |
| **Project** P `GC01`–`GC02`, `GA03`, `GC04`–`GC05` | Recorded full constraint chain, `Y` solution and its gauged scalar/spinor/vector shifts |
| **Project** P `GC08`, `GC11`, `GC12`, `GC03` | Candidate full `chi`, `D`, `T` and supercovariant three-form used in the prior calculation |
| **Project** P `GC14`–`GC24`; source C24 (2.16), (2.24), (2.27), (2.37)–(2.39) | Gauged derivatives/connections to audit; component projection, dependent connections, Weyl/vector covariants in C |

The gauged dilaton-Weyl substitution follows the standard-Weyl BF assembly and retains the constrained three-form and its gauging. P relation IDs identify the project’s composite definitions; G25 (1), (4) give their abbreviated source presentation. This substitution is distinct from the LOG composite map S23 (3.24)–(3.26).

## 5. Target Poincaré gauge

| Reference | What it supplies |
|---|---|
| G25 (7), (25), (27); OP (4.1), PDF p.13 | Target dilaton/dilatino/K and linear-compensator gauge, with the R-connection split |
| OP (4.2), PDF p.13 | Retained field content: the gravitino and linear-compensator fermion survive the dilatino gauge |
| OP (4.3), PDF p.14 | Ungauged compensating parameters, explicitly only **up to cubic fermion terms**; comparison input, not the final gauged all-order law |
| CO (2.15), (2.20); OP (2.1) | Variations of the gauge-fixing fields, including the `b_mu` law, from which the required compensating S/K/R parameters must be derived |
| C24 Appendix C, Table 5 | Parameter conversion needed when transporting these transformations between conventions |

The gauge-preservation equations use the combined Q/S/K/R transformations. OP (4.3) has its stated fermion truncation. The condition `psi^i=0` fixes the dilatino, while P `GC14`–`GC16` retain its nonzero covariant derivatives.

## 6. Component action through two physical fermions

| Reference | What it supplies |
|---|---|
| S23 (3.25)–(3.27); C24 (4.8a), supplement §2.2 and (5.9b) | Defining full superfield/action and supporting expanded component lists whose coverage must be counted |
| C24 supplement (1.1)–(1.2), §§5.1–5.3 | Raw index/projection conventions and higher covariant-derivative expansions needed to expose hidden fermions |
| C24 (2.16), (2.24), (2.27), (2.37)–(2.39), (2.53) | Component projection, dependent connections, and the covariant derivatives/field strengths to expand or define exactly |
| W (A.9)–(A.10), (A.15)–(A.17); C24 Tables 1–2, PDF pp.18,23 | Spinor rearrangement identities and linear-multiplet weights for the term ledger |
| **Project** P `GC03`–`GC24`, `GA03`; [fermion-order ledger](../FERMION_ORDER_LEDGER.md) | Candidate gauged substitutions and the record of explicit versus hidden fermion degrees |

The collected action retains physical fermion degree zero and two. Fermion-order counting includes contributions inside covariants; the source definitions and component ledger specify these dependencies. The component certificate records coefficient, dimension, index and reality checks.

## 7. Component checks

| Reference/check | Mathematical content |
|---|---|
| S23 (2.20)–(2.24); C24 (2.40)–(2.44), (2.50)–(2.54); CO (2.15), (2.20); gauge-preservation equations from step 5 | Full linear-multiplet transformations, constrained-vector identity and local action supersymmetry modulo the stated boundary terms |
| G25 (11); C24 supplement §3.1 | Published bosonic comparisons after conversion; these cannot certify fermionic completeness |
| **Project** B `eq:L-final-expanded`, `eq:Bianchi-expanded` | Existing corrected bosonic LOG representative, now displayed as LOG-CORR05; gauged Bianchi/E-sector in LOG-CORR01–02 |
| **Project** B `eq:L-YD`, `eq:L-Riemann-correction-map`, `eq:Log-mixed-current`, `eq:Log-D-boundary` | Existing project-derived coefficient/projection corrections (LOG-CORR03–04) and boundary-current records; compared with the primary-derived expressions |
| CO (5.2)–(5.8) at `g=0`; OP (2.9), PDF p.7; S23 (3.27b), C24 (5.9b) | Ungauged composite and action comparison after matching full definitions and normalization |
| W (A.9)–(A.10), (A.15)–(A.17); C24 Tables 1–2 | Source identities/weights for independent symbolic Clifford/Fierz, coefficient and dimension checks |

The [component certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) links the primary, component projection, source repairs, BF identities, bosonic equality and ungauged-limit evidence. Each result has its stated fermion order and boundary scope.


