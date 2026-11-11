# Gauss–Bonnet bosons on supersymmetric AdS3 × Sigma2

This package supplies the bosonic quadratic actions, physical polynomials and
primary-norm calculations for paper Sections 4.2–4.5 and Appendix C
(repository citation 24). The [scientific chapter](../../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md)
states the conventions, branch exclusions and interpretation.

The action is LR + lambda(W + 2 LOG), with k = lambda g². No numerical value
is assigned to g, L or k when constructing or reducing the matrices. The
old product-background convention is lambda = -2 lambda_GB. Fermionic Hessians
and their comparison with multiplets are documented separately under repository citations 25–26 and are outside
this package.

## Reproduce

Use Python 3 with the pinned packages in [requirements.txt](requirements.txt).
The commands below are run from the repository root. Installing dependencies
in an external environment keeps the repository unchanged.

```bash
python3 -m venv /tmp/gb-item23-env
/tmp/gb-item23-env/bin/python -m pip install -r computations/gb_ads3_sigma2/requirements.txt
source /tmp/gb-item23-env/bin/activate
/tmp/gb-item23-env/bin/python -B computations/gb_ads3_sigma2/checks.py --norms
python3 -B tools/validate_repository.py --details
```

The scientific check is read-only. It reconstructs the off-shell Hessians,
compares the two source representatives, restores the symbolic BPS branch,
recomputes maximal-minor certificates and checks the stored invariant
propagators. `--norms` also repeats the explicitly labelled finite samples.
It includes the four formal alternative-branch norm relations and checks
the stored standalone product matrices, their root ranks and complete
multiplet matchings. To reconstruct all 39 numerical source matrices
(36 standalone sectors and three E-deletion sectors) independently:

```bash
python3 -B computations/gb_ads3_sigma2/product_checks.py --verify --fresh
```

The repository validator checks structure and hashes; it does not verify
physics. To regenerate only this package's output files:

```bash
python3 -B computations/gb_ads3_sigma2/derive.py --stage all
python3 -B computations/gb_ads3_sigma2/norms.py
python3 -B computations/gb_ads3_sigma2/product_checks.py --workers 3 --write
python3 -B computations/gb_ads3_sigma2/product_checks.py --verify --fresh --write-log
python3 -B computations/gb_ads3_sigma2/checks.py --norms --write-log
```

These commands require the dependencies on the chosen Python's import path.
`derive.py --stage` also accepts `raw`, `branches`, `generic`, `chirality`,
`special`, `torus_momentum` and `constant`. Each command evaluates its named calculation.

## Calculation and data layout

| File or output family | Content |
|---|---|
| [algebra.py](algebra.py), [action.py](action.py), [sectors.py](sectors.py) | Exact second-order metric/form algebra and all six boost/charge matrices |
| [source_weyl.py](source_weyl.py) | Independent current G-W representative, including conformal dependent connections |
| [model.py](model.py) | BPS substitutions and invertible dimension-preserving amplitude changes |
| [closed_forms.py](closed_forms.py) | v109 check targets; these do not construct the Hessian |
| [physical.py](physical.py), [polynomial_matrix.py](polynomial_matrix.py) | Exact rank factorizations, certified determinantal divisors, invariant probes |
| [harmonics.py](harmonics.py), [constant.py](constant.py) | Restricted harmonic spaces and independent fixed-flux constant-level reduction |
| `outputs/raw_*.json`, `fs_*.json` | Off-shell quadratic matrices, amplitude order, linear terms, background parameters |
| `outputs/branch_*.json`, `minus_*.json`, `torus_*.json` | Symbolic on-branch matrices, both chiralities and the constant torus level |
| `outputs/torus_momentum_*.json` | Independent nonzero-momentum torus matrices; S is the flat Fourier exponent and M²=-S²/9 |
| `outputs/physical_*.json` | Rank, charts, gauge spaces, divisor certificates and invariant propagators; special levels retain their restricted matrices |
| [constant.json](outputs/constant.json) | Four-field scalar pencil, N elimination, vector curl pencil and current CS matrix |
| [norms.py](norms.py), [norm_samples.json](outputs/norm_samples.json) | Analytic pole residues and 22 levels of paper Table 11 (`tab:GBbos`), upper block, at 80/140 digits |
| [product_checks.py](product_checks.py), [r2_density.py](r2_density.py) | The explicit E-term deletion spectrum and six standalone W/LOG/R² comparisons after paper equation (4.9) (`eq:Kform`) |
| [product verification](outputs/product_checks/verification.json), [log](outputs/product_checks/verification.log) | Fresh numerical action reconstruction, high-precision rank checks, complete matchings and failing mutation controls |
| [accumulation_norm_samples.json](outputs/accumulation_norm_samples.json) | 45 finite-level checks of the towers approaching the flat weights, lower block of that table |
| [verification.log](outputs/verification.log) | Fresh scientific-check results, distinct from repository structural validation |
| [source_manifest.json](source_manifest.json) | Current input fingerprints and external-source provenance; no external runtime files |

JSON polynomial factors use `^` for exponentiation; matrix expressions use
Python/SymPy `**`. `rank` refers to generic rank over the stated rational
function field. A constant nonzero factor in D is a unit for the physical
divisor, but its sign is **not** discarded from the propagator used for norms.
No pickle files are used. The generic symbolic GB divisors use exact
certificates, without numerical reconstruction or random-minor stopping
rules. The separate six-point comparison uses numerical root candidates
and direct high-precision rank checks, as detailed below. At a singular
parameter or a colliding root, return to the unreduced
matrix instead of substituting into a generic inverse.

## Scope of the additional paper checks

The standalone models are evaluated at g=1 and (L,c,S)=(1,1/10,3) and
(5/4,-1/10,1/2+13i/10), each on its own numerically solved H² background.
The S=3 point is an algebraic continuation, not a physical principal-series
mode. The first variations are solved at 125 digits and retained at 115
digits; all background equations are checked. The stored files
`outputs/product_checks/{W,LOG,R2}_{a,b}.json` contain the polynomial
coefficients, amplitude bases, rank diagnostics and complete root matchings.

The existing prediction-independent polynomial-pencil module supplies
candidate roots with two seeds and four projections per seed. Two further
independent projections refine each root at high precision. The unreduced
matrix must lose the stated rank there and recover it nearby. Background
precision and retained/gauge singular-value gaps are checked before roots
are counted. The verification rejects a synthetic 42-digit gauge-breaking
direction, missing roots, wrong energies and wrong charges. This is finite
numerical evidence for the paper's six examples, not an all-parameter proof.

`--case W_a` (and the other five names, or `E_deletion`) limits generation
to one example. Verification is read-only unless `--write-log` is supplied;
that flag also requires `--fresh`. `--write` writes only the requested data
under this package's `outputs/product_checks/`. The original source notes are
provenance references only: no external file is needed at runtime.
