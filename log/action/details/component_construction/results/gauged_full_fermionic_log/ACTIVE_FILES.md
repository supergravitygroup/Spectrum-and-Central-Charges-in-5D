# LOG component reading guide

Start with [the compact BF action and all four components](../../../construction.md), then [the certification report](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The active convention authority is [CONVENTIONS.md](CONVENTIONS.md), with the LOG-specific bridge in [LOG_CONVENTIONS.md](LOG_CONVENTIONS.md).

The current action retains two physical fermions; higher intermediate degrees are retained where required by differentiation. All project derivatives are full supercovariant derivatives. Step 5 uses the distinct source-only label D^(G,LUD) when displaying the Lorentz/SU(2)/dilatation part of a source derivative.

## Calculation sequence

| File | Role |
|---|---|
| [Step 2](STEP_02_LOG_PRIMARY.md) | Complete primary derivation; corrected explanatory S commutator |
| [Step 3](STEP_03_LOG_SPINOR.md) | Source-frame spinor descent |
| [Step 4](STEP_04_LOG_SCALAR.md) | Source-frame scalar descent |
| [Once-projected scalar reference](STEP_04_LOG_SCALAR_PROJECTED_REFERENCE.md) | Distinct Gold-component comparison; not the project-frame endpoint |
| [Step 5](STEP_05_LOG_VECTOR.md) | Source-frame vector descent; corrected current-interface explanation |
| [Step 6](STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md) | Once-only project component projection and BF assembly |
| [Canonical unfixed multiplet](LOG_MULTIPLET_CANONICAL_TWO_FERMI.md) | Input before gauged composite substitution |
| [Current Step 7](../../../construction.md) | Gauged canonical components, composite/constraint relations, derivative dictionary and BF density together |

## Reference and evidence

The source registry, fermion-order ledger and component notes supply definitions and component identities. The Markdown under `sources/reference_fragments/` and `sources/step4`–`step7` contains component reference sections. These sections support the named component documents.

## Execution scope

Executable LOG certification scripts are not included in this component documentation.