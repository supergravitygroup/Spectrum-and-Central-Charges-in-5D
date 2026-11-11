# Exact R² AdS5 checks for the final paper

This package reproduces the final paper's R² vector reduction, kinetic coefficients and local critical limits. The authoritative source is `draft_v110_source/draft_v109.pdf`, with its matching TeX. Their SHA-256 hashes and the repository inputs are recorded in [source_manifest.json](source_manifest.json).

The checks support equation (3.20) (`eq:R2vec2`), equation (3.21) (`eq:R2vec3`), equation (3.22) (`eq:R2MV`), the composite-spinor gauge-invariance statement, equation (3.24) (`eq:R2fermop`), the coefficients underlying Table 3 (`tab:R2`) and Table 4 (`tab:R2ranges`), and the critical-point paragraphs of Section 3.2.3 (`sec:R2mult`). They use the repository's documented quadratic action and coupled equations. This is a replay of the algebra following those inputs, not a new derivation of the complete component Hessian or a proof of nonlinear supersymmetry.

## Reproduction

From the repository root, with SymPy 1.14.0 installed:

```bash
python3 -B computations/r2_ads5_paper_checks/checks.py
```

The default command writes nothing. It checks the pinned input and implementation hashes, recalculates all 31 exact checks and compares their residuals and finite matrices with [outputs/verification.json](outputs/verification.json). To regenerate this package's two verification records after an intentional source update:

```bash
python3 -B computations/r2_ads5_paper_checks/checks.py --write-log
```

The optional command writes only `outputs/verification.json` and `outputs/verification.log` within this package. It does not refresh the repository hash manifest or any input. The stored run uses Python 3.14.1 and SymPy 1.14.0; the exact-result comparison does not require that particular Python patch version.

## Checked statements and scope

- The first-order vector constraint, algebraic elimination, and regular diagonalization reproduce the finite action and Proca mass. The scalar inverse eigenfields reproduce all nine entries of the kinetic congruence. The fermionic checks reproduce the background gauge-invariance coefficients, the characteristic factorization and the light/heavy norm pullbacks.
- The background relation is imposed exactly as $`\lambda=4(L-1)/(3g^2L^2)`$. The generic changes of variables require $`g\ne0`$, $`L>0`$ and $`\lambda AB\ne0`$. No coupling or energy is fitted from numerical samples. The identities in $`\nu`$ establish the signs for both $`0<\tau<3/2`$ and $`3/2<\tau<2`$: the massless vector multiplet is positive, while the graviton and long vector multiplets have the sign of $`A`$.
- At $`\tau=3/2`$, square completion in the original critical scalar and form action, together with the light-spinor norm, reproduces the algebraic steps used by the [existing zero-source analysis](../../r2/ads5/details/critical_branches.md#134-lambda_r2g214-original-critical-action). The boundary classification itself remains an analytic argument on that page.
- At $`\tau=2`$, the finite vector matrix has nonzero determinant and a rank-one nilpotent $`K^{-1}M`$. The original neutral-scalar equations have a two-dimensional BF eigenspace. The undivided spinor equations have a double light root with a one-dimensional eigenspace, giving the spinor Jordan pair. These identities keep $`g`$ symbolic and do not use the singular $`B^{-1}`$ eigenfields.

The endpoint result is local, as in the paper. It does not select a boundary domain for logarithmic partners or infer a complete interacting theory from the quadratic kernel.

The [readable verification log](outputs/verification.log) names each checked identity. The JSON additionally stores the exact endpoint matrices, individual zero residuals and the fresh-run environment.
