# Source, procedure and convention locks

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

Source registry: `GAUGED-LOG-FULL-FERMI-INPUTS-v2`, 2026-09-22.
The reusable convention/source reference is `GAUGED-LOG-CONVENTIONS-v1` in
[CONVENTIONS.md](CONVENTIONS.md), with [machine-readable scope](../../../spectrum_input.md).
These are input and method locks, **not a completed-action or nonlinear-SUSY lock**.
The full linear-slot/action-normalization matching is now verified in the retained-order certificate.
PDF page cues count from the first PDF page.

## Primary construction chain

Follow Gold 2025's paragraph after (10): construct the **standard-Weyl LOG composite and BF action** using Gold 2023 (3.24)–(3.27), then apply the **gauged dilaton-Weyl maps** Gold 2025 (1), (4), then impose (7), supplemented by (25), (27). Compare the bosonic restriction with (11). The LOG composite map and the later gauged dilaton-Weyl map are distinct operations.

| Local source | Located input | Role and limit |
|---|---|---|
| [Gold superspace 2023, S23](../../EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8) | (3.24), PDF p.20 / printed p.19; (3.25), PDF pp.21–22 | Primary defining LOG superfield and its complete expanded superfield |
| Same S23 PDF | (3.26a–c), (3.27a–b), PDF p.22 / printed p.21; general BF (3.2a–b), PDF p.14 / printed p.13 | Descendant definitions and standard-Weyl LOG invariant. The paragraph after (3.27) defers explicit descendant expansions |
| Same S23 PDF | (2.20)–(2.24); (2.6), (2.8c), (2.13), (2.15) | Linear-multiplet constraints, descendants, vector conservation and S laws; primary-check inputs identified by the source |
| [Gold gauged 2025, G25](../../EXTERNAL_REFERENCES.md#ref-f480139fecd5) | Paragraph after (10), PDF p.9; (1), (3), (4), (7), (11), (25), (27) | Governs operation order, gauged map, target gauge and bosonic comparison. (1), (3) omit fermions and (10) suppresses higher fermions; use full supporting definitions |
| [Gold components, C24](../../EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4) | Main §4.2, (4.7), PDF p.32; complete component (4.8a), pp.32–34 | Component implementation and cross-check of the S23 primary |
| Same combined PDF | Appended supplement §2.2.1, PDF p.106; §2.2.2, p.113; §2.2.3, pp.121–149 | Full spinor, scalar and vector descendants; retain all displayed fermions |
| Same combined PDF | Main §2.3, (2.40)–(2.44), (2.52); §5.2, (5.9b), PDF p.41 | Linear-multiplet definitions/laws and full BF action with gravitino terms |
| Same combined PDF | Supplement §1, (1.1)–(1.2), PDF p.103 | Raw symmetrization/index notation and X/Y-to-chi/D projections |
| Same combined PDF | Supplement §3.1 | Bosonic gauge-fixed LOG action only |
| [Coomans–Özkan](../../EXTERNAL_REFERENCES.md#ref-91993860706d) | (2.15)–(2.21), (5.1)–(5.8), as indexed in the project reading guide | Gauging-deformation source in its stated conventions. (5.9) uses the alternate compensator-fermion gauge |

S23 is arXiv:2302.14295v2, G25 reference 33. C24 is G25 reference 34 (published JHEP07(2024)221); the local combined PDF contains arXiv:2311.00679v1 (2023). C24 supplement §2.2 supplies the expanded full-fermion descendants deferred by S23: it remains implementation support, not a competing construction route. No external source is currently needed for that gap. See manifest.

## Convention anchors and scoped prior work

The convention sources include the 5D Weyl paper, §§3–5 and Appendix A (A.1)–(A.17), for field content, curvatures, spinors and Fierz identities; Proeyen matter paper §4.1 (4.1)–(4.6); Lauria–Van Proeyen §§2.6.3, 4.7.1 and Appendix A; Tools §§2–3; and FVP opening conventions. The basic working relations and published Gold/Bergshoeff bridge are now recorded in CONVENTIONS.md. The four-slot and density matching are now certified at the scope of the current LOG certificate. Bergshoeff 2012 §§4–5 supplies workflow only.

| Prior artifact | Permitted reuse |
|---|---|
| [Gauged Weyl calculation](../../../../../../weyl2/action/details/construction.md), with its [README](../../EXTERNAL_REFERENCES.md#ref-6bc321587cb9) | Candidate full gauged composites and covariants; scoped insertion checks do not certify independent nonlinear invariance |
| [Existing corrected bosonic LOG derivation](../../../../../../gauss_bonnet/ads5/code/inputs/action_sources/10_weyl_log_from_definitions.tex) | Compare the bosonic restriction, including the exact gauged three-form Bianchi chain, `g E_3` sectors and boundary currents. Use CONVENTIONS.md LOG-CORR01–LOG-CORR05: the existing corrected result is a mandatory bosonic comparison, not a published erratum or a full-fermionic certificate |
| [Single-linear source anchor](../../EXTERNAL_REFERENCES.md#ref-1e90375d3355) and [map anchor](../../EXTERNAL_REFERENCES.md#ref-6e0705353bf2) | Scoped 2016 linear-to-vector map; not the LOG multiplet or full LOG action |
| [Defining-vector anchor](../../EXTERNAL_REFERENCES.md#ref-37d8ac9f8637) | Field and form definitions subject to the LOG conversion audit |
| [Two-derivative action](../../EXTERNAL_REFERENCES.md#ref-f28a0abdff2b) and [audit](../../EXTERNAL_REFERENCES.md#ref-4985118bd0c0) | Exact bosons and quadratic fermions only; higher-fermion omissions preclude using it as the complete LOG input |

Use corrected Özkan–Pang (3.1)–(3.2), (2.1)–(2.22), (3.6), (4.1)–(4.4) for the older density/covariant convention bridge, as required by the reading guide. The 2016 source remains restricted to its declared composite-map role.

## Verified interfaces and remaining scope

The master fixes the metric/Riemann, epsilon, Clifford, Majorana, SU(2), connection and source-to-project bridge. The current certificate verifies the primitive/linear-slot projection, complete density normalization, retained gauged substitutions, full-primary identities, canonical/reality checks and complete calculated bosonic LOG-CORR05 comparison with explicit boundary currents.

The displayed action retains terms through two physical fermions. Higher-fermion interactions and a separately expanded all-order gauge-preserving algebra lie outside the certificate. Literal source conflicts are distinguished from their derived corrections.
