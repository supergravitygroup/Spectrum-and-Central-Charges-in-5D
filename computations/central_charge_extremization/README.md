# Anomalies and extremization in the final paper

This package supplies the central-charge checks referred to in the
paper's Sections 3.6 and 4.4 and its final repository statement (final-paper
citation 28). It continues the existing [central-charge and massless-vector calculation](../generic_ads5_massless/README.md).
The [derivation](../../generic_combination/ads5/anomalies_and_extremization.md)
identifies the source terms, normalizations and domains.

Run from the repository root with Python and the existing SymPy requirement:

```bash
python3 -B computations/central_charge_extremization/checks.py
```

The default command checks the input hashes, recomputes 33 exact identities
and compares with [verification.json](outputs/verification.json). It writes
nothing. To refresh only this package's result and [log](outputs/verification.log),
add `--write-log`.

| Paper statement | Calculation in checks.py |
|---|---|
| Equation (3.66) (`eq:LCS`), equation (3.67) (`eq:TrR`) | Source-grouped CS coefficients, symmetric cubic tensor, anomaly inflow |
| Equation (3.65) (`eq:atrial`), equation (3.4) (`eq:vacuum`), equation (3.63) (`eq:acgen`) | Trial function from anomalies and the existing scalar-curvature action; stationarity and values |
| Normalized flavor current | Existing massless-vector kinetic matrix; second derivative of the trial function |
| Equation (4.14) (`eq:cLcR`) | General-flux trial central charge and gravitational anomaly on the symbolic BPS family |
| The flat trial at k=2/3 | Evaluate the trial before dividing by its second derivative |
| c_L=3k_R | Compare the CS reduction with the existing constant-level current matrix |
| Equation (4.15) (`eq:UTc`), equation (4.16) (`eq:deltac`) | Universal-twist flux, flavor mixing and the first-order limit stated in the paper |

The couplings and g remain symbolic. These are checks of the stated
action projection and anomaly algebra; the adopted inflow normalization
is not rederived. The final paper is pinned in [source_manifest.json](source_manifest.json).
External files and the original source scripts are comparison records, not runtime
dependencies. The implementation is organized independently and imports
only current repository calculations. No scan of additional twist branches
or calculation from the historical draft notes is included.
