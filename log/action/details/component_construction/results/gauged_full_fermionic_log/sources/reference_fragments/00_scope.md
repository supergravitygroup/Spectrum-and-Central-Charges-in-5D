# Conventions and source equations: full fermionic gauged LOG invariant

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Supercovariant derivative convention.** Use the full supercovariant $`\mathcal D_a`$ and the conformal box $`\Box^c=\mathcal D^a\mathcal D_a`$, exactly as in the [fermionic gauged Weyl-squared calculation](../../../../../../../../weyl2/action/details/construction.md), GC14–GC24. Its Q/S/K and implicit fermionic contributions stay inside the operators. Gauge evaluation follows each ordered differentiation; derivatives of the fixed dilaton/dilatino are not silently set to zero. The [active LOG endpoint](../../../../../construction.md) uses this policy. Gold superspace source formulas retain $`\nabla_A`$ until the complete bridge is applied.

**Reference lock:** `GAUGED-LOG-CONVENTIONS-v1` · **2026-09-22**.
**Procedure lock:** `GAUGED-LOG-G25-S23-PROCEDURE-v1`.

This is the reusable calculation reference for the locked procedure. It contains
equations, not only citations: transcribed working relations first, followed by
the complete cached source equations needed for the long component expressions.
The searchable source transcriptions below retain equation and page locators.
For exact index placement, consult the corresponding published source in the [bibliography](../../../../../../../../references/bibliography.md).

The lock establishes notation, provenance, source equations and permitted
conversions. The checked identities and their fermion orders are specified
in the associated construction records. Printed formulas and project-derived
repairs remain explicitly distinguished.

The separate [LOG working conventions and step 1 derivation](../../LOG_CONVENTIONS.md)
record the checked covariant four-slot Q/S map, six nonform BF terms, bosonic
normalization and explicit chi-curvature reconciliation. The [full superform derivation](../../../../../../../../references/source_evidence/log/derivations/form-interface.md)
now resolves the generic current/potential/BF interface for a genuine linear
multiplet, with explicit repairs of the incompatible printed formulas. This main
file preserves literal source formulas; the working ledger distinguishes those
from derived repairs and from verification of the particular LOG polynomials. The source's convention-check script is not supplied as a runnable module here.

**Retained-order construction.** The current construction through two physical fermions is certified in [CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md](../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The full primary, retained descendants, projection, canonicalization, reality, current/BF interface and complete bosonic comparison pass. Higher-fermion action terms and independent all-order gauge-algebra closure remain outside that certificate. The certificate specifies which component expressions and checks support this scope.

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
| LOG-S1-01–LOG-S1-24 in [LOG_CONVENTIONS.md](../../LOG_CONVENTIONS.md) | Derived step 1 bridge, density comparison, curvature reconciliation and current/potential diagnostics |
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

The numbered sources and their versions are listed in the [bibliography](../../../../../../../../references/bibliography.md).
The [current evidence manifest](../../../../../../../../references/source_evidence/manifest.json) identifies the retained repository evidence; source-page numbers below refer to the cited publications.
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

