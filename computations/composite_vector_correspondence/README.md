# Composite-vector correspondence checks

This package supplies bounded, executable checks for paper equations (B.1) and (B.3)–(B.7), corresponding to repository citations 30–31. The mathematical dictionary and action paths are in [the correspondence note](../../common/details/composite_vector_paper_correspondence.md). Existing component formulas remain the scientific inputs.

## Run

From the repository root, with NumPy and SymPy available:

```sh
python3 -B computations/composite_vector_correspondence/checks.py
```

The default run reads its manifest, checks SHA-256 fingerprints, performs the assertions and prints a summary. It writes no files. To deliberately regenerate this package's two verification outputs:

```sh
python3 -B computations/composite_vector_correspondence/checks.py --write-log
```

The recorded run used Python 3.14.1, SymPy 1.14.0 and NumPy 2.5.4. NumPy was available in `/tmp/item24_deps`, so its actual invocation was:

```sh
PYTHONPATH=/tmp/item24_deps python3 -B computations/composite_vector_correspondence/checks.py --write-log
```

That temporary directory is an environment detail, not a package dependency or input. [requirements.txt](requirements.txt) records the two tested library versions. No external manuscript or external source-folder path is opened by the checker.

## What is checked

- Independent symbolic entries of symmetric SU(2) tensors verify the norm/index identities, the vanishing contracted vector bilinear, the $`N`$ and $`\widehat E`$ coefficient dictionaries, the $`(-1,3)`$ derivative basis and its independent coefficient solution, and antisymmetry of the triplet-gradient contribution to $`\widehat F`$.
- Exact scalar differentiation checks the coefficients in the two compact covariant derivative products of equation (B.5) (`eq:compF`). The derivation assumes the inherited covariant product and Majorana-swap rules; it does not reconstruct supercovariant connections.
- Symbolic checks isolate the local $`\partial\epsilon`$ cancellation fixing $`+i/2`$ in $`\mathcal D\varphi`$, the $`E/P`$ bilinear current relation, conservation of a curl by symmetric/antisymmetric contraction, and physical fermion-order selection in the BF density. They do not prove the complete supercovariant constraint or action invariance.
- Exact Clifford checks establish $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, $`\eta=(-++++)`$, $`\gamma^{01234}=i`$, $`C^T=-C`$ and $`(C\gamma^a)^T=-C\gamma^a`$. The implemented bilinear is the linear Majorana expression $`\xi^TC\Gamma\zeta`$ on independent, complexified Grassmann components, with no numerical conjugation of odd generators.
- An original bitmask exterior algebra and even variation jets derive the scalar Clifford part of selected $`\delta\lambda`$ monomials. The eight components of $`\varphi`$ and eight of $`\epsilon`$ stay formal. Cubic-$`\lambda`$ terms are varied before selecting $`\epsilon\varphi^2`$. Bosonic SU(2) triplets are numerical positive matrices $`A\mathop{\mathrm{diag}}\nolimits(2,1)A^T`$ with determinant-one integer shears $`A`$, generated with seeds 7 and 4. Both have $`L=2`$. The 42 comparisons cover one $`N`$ block, five $`\widehat E`$ directions and fifteen $`\mathcal DL`$ directions/components for each seed.

The finite Grassmann comparisons concern the scalar Clifford block at $`\psi_\mu=0`$, with the other independent $`T`$, $`\chi`$ and $`\mathcal D\varphi`$ structures set to zero. They are not a proof for arbitrary bosonic fields, the full nonlinear transformation, non-scalar Clifford parts, gravitino-dependent terms or a quartic action. Neither equation (B.7) (`eq:boxc`) nor the full $`\widehat F`$ transformation is independently derived by this package.

## Failure detection and evidence

All positive comparisons have assertions. The formal exterior algebra discards only coefficients that are exactly zero in its numerical representation; it never uses a small-coefficient cleanup threshold. Numerical comparisons use

```math
\frac{\max|\text{derived}-\text{expected}|}
 {\max(1,\max|\text{derived}|,\max|\text{expected}|)}\le 2\times10^{-11}.
```

Five exact negative controls test the three literal-2013 coefficient blocks, the real $`1/2`$ derivative coefficient, and the omission of $`E^{[2]}`$. Six numerical negative controls, one for each block and seed, must exceed a scaled discrepancy of $`10^{-6}`$ for at least one of their independent directions. A changed source or implementation fingerprint also fails immediately.

[verification.json](outputs/verification.json) records every check, seed, numerical scale, residual and tested version; [verification.log](outputs/verification.log) is the console summary. Results document a fresh run of this implementation.

[source_manifest.json](source_manifest.json) fingerprints stable local scientific inputs and this package's implementation. External manuscript and source fingerprints are provenance records only. The original source notes suggested which coefficients deserve comparison and the use of a scalar Clifford projection; this package independently implements automatic variation jets, a fixed charge-conjugation representation, formal-generator arithmetic, symbolic bases and assertions. No external source file or program is copied or imported.
