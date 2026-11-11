# Spectra and Central Charges of Gauged Curvature Squared Supergravities in Five Dimensions

**Authors:** Erol Aksoy, Cagatay Okyay, Mehmet Ozkan and Cemal Berfu Senisik

**Affiliation:** Department of Physics, İstanbul Technical University,
Maslak, 34469, İstanbul, Türkiye

Companion calculations for the paper: component actions, background equations,
quadratic fluctuation operators, local spectra and central charges of gauged
five-dimensional supergravity with eight real supercharges.
The action expressions retain bosons and terms up to quadratic order in the fermions, including
fermions implicit in supercovariant objects. The analytic reductions keep the couplings finite and symbolic.

[Paper calculations](#follow-the-paper) · [Run the checks](#reproduction) ·
[Conventions](CONVENTIONS.md) · [Scientific scope](#scientific-scope) ·
[Central-charge guide](references/central_charge_guide.md) ·
[All 31 paper citations](references/paper_citation_map.md) ·
[Saved results](references/paper_citation_map.md#calculations-and-saved-records)

## Follow the paper

Follow the topic table below through the model/background chapters. For a
specific equation or table, the [citation index](references/paper_citation_map.md)
enters the relevant step in those same chapters, with its derivation,
executable calculation and saved output.

| Paper topic | Start here | Continue to |
|---|---|---|
| Section 2: component theories | [Action family](common/action_family.md), [two-derivative action](common/two_derivative_action/README.md) | Individual invariant actions and their explicit two-fermion terms |
| Section 3.1: common vacuum and fluctuations | [Fields and derivatives](common/fields_and_derivatives.md), [fluctuation method](common/fluctuation_method.md) | Background, raw quadratic action and constraints in each sector |
| Sections 3.2–3.5: AdS₅ spectra | [R²](r2/ads5/README.md), [Weyl²](weyl2/ads5/README.md), [Gauss–Bonnet](gauss_bonnet/ads5/README.md), [LOG](log/ads5/README.md) | Masses, norms, multiplets and exceptional branches |
| Section 3.6: central charges | [Central charges and massless vectors](generic_combination/ads5/central_charges_and_massless_vectors.md) | [Extremization and universal twist](generic_combination/ads5/anomalies_and_extremization.md) |
| Section 4: BPS AdS₃ × Σ₂ | [Product-background chapter](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md) | [Bosonic matrices](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/quadratic_actions.md), [fermionic action](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md), [fermionic spectrum](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md) |
| Appendices A–B: conventions and corrected composites | [Common conventions](CONVENTIONS.md), [composite-vector correspondence](common/details/composite_vector_paper_correspondence.md) | [Component-to-Hessian correspondence](references/fermionic_input_correspondence.md) |
| Appendix C: product polynomials | [Generic harmonic levels](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/generic_levels.md) | [Special levels](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/special_levels.md) and [norms](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/norms_and_multiplets.md) |


## Reading the derivations

Within each background, follow the action input, background equations, raw
quadratic action, constraints, physical operators, masses, kinetic norms and
exceptional branches in that order. Long component expressions and supporting
algebra are linked as appendices.

- [Fields and derivatives](common/fields_and_derivatives.md) fix independent
  fields, composites and the inherited Poincaré representation.
- [Action family](common/action_family.md) and
  [coupling correspondence](#action-and-coupling-correspondence) distinguish the invariant basis
  from source-specific spectrum normalizations.
- [Physical fermion order](common/fermion_order.md) includes implicit
  supercovariant contributions.
- [Fluctuation method](common/fluctuation_method.md),
  [mass notation](common/spectrum_notation.md) and
  [kinetic norms](common/kinetic_terms_and_stability.md) fix the physical
  interpretation of the operators.

A determinant root must also satisfy the original constraints. Read the norm
and critical-branch conditions with each spectrum table; these conditions
are part of the result.

## Reproduction

From the repository root, create an external environment, install the pinned
requirements, and run the paper checks and Section 4 figures:

```bash
python3.14 -m venv /tmp/sugra-paper-env
source /tmp/sugra-paper-env/bin/activate
python -m pip install -r requirements.txt
python -B reproduce.py
```

The verified environment is Python **3.14.1**, SymPy **1.14.0**, SymEngine
**0.15.0**, python-flint **0.9.0**, mpmath **1.3.0**, NumPy **2.5.4** and
SciPy **1.18.1**. Matplotlib **3.11.2** is included for the figure scripts.
The runner uses the active interpreter, prints one PASS or FAIL line for each
package, and exits unsuccessfully if any package fails. It runs the bosonic
norms and the full fermionic spectrum checks, including fresh action evaluations.
The normal run includes the nine main packages, the exceptional-background,
tower-norm and first-order Gold checks, and Figures 2–3. It reads retained
scientific outputs and writes the figures outside the repository. Allow tens
of minutes; timings depend on the machine. Use `--verbose` to see all check
output, or an external `--output-dir` to keep individual logs and figures.

For the complete verification pass, including component suites, failure
controls, the adopted LOG replay and all three figures, run:

```bash
python -B reproduce.py --all --output-dir /tmp/sugra-reproduction
```

Figure 1 additionally needs Tectonic or pdflatex with standalone/amsmath/TikZ;
see the [figure build instructions](figures/README.md#figure-1-ads5-parameter-ranges).
An unavailable check is reported as NOT RUN and gives an unsuccessful exit
status. Failed checks never produce an overall successful exit. LOG replay
runs in a temporary package copy; its fresh summary can be retained in the
external output directory. `--all` also recomputes Figure 3's 150 entries.
These options use the same scientific chapters; they do not define separate
reader routes. Explicit full-regeneration commands below remain available
for rebuilding the stored matrix data, in a disposable checkout.

The independent repository integrity check is:

```bash
python -B tools/validate_repository.py
```

It checks local links and anchors, Markdown tables, Python syntax and hashes;
it does not verify physics. Individual scientific commands and their precise
scope are listed below.

<details>
<summary>Individual commands, evidence and component checks</summary>

### Structural checks and four auxiliary identities

Run the following commands from the repository root:

```bash
python3 -B tools/validate_repository.py
python3 -B tools/check_symbolic_identities.py
python3 -B tools/computation_inventory.py
```

The structural checker and source inventory use the Python standard library.
The algebraic checker requires SymPy; it has been evaluated with SymPy 1.14.0.
These three commands read the repository and print JSON to standard output.
They do not install dependencies or regenerate scientific outputs. The symbolic
command checks the four identities described below; the other two are structural.
The computational packages' `environment/requirements.txt` files describe
calculation dependencies; those full environments are unnecessary for
the three commands above.

| Command | Inputs | Output and scope |
|---|---|---|
| `tools/validate_repository.py` | Markdown, Python source and the current repository integrity manifest | Local links and embedded-image targets, pipe-table header/body column counts, Python syntax and file integrity; internal heading anchors are checked; external URLs and image decoding are not checked; no physics verification |
| `tools/check_symbolic_identities.py` | Four displayed identities encoded with exact rational coefficients and independent symbolic variables | Exact zero residuals for the identities below, together with their domains and exclusions |
| `tools/computation_inventory.py` | Python source text under `computations/` | Source counts and indicators of numerical evaluation; no source imports or execution |
| `tools/computation_inventory.py --details` | The same source text | Indicator paths and line numbers for manual inspection |

The symbolic checks use only definitions, algebraic identities and the
specified dimension. They do not assign values to any free coupling, scale,
field component or dimensionless parameter combination.

### Final-paper AdS5 reductions and central-charge checks

The [complete citation index](references/paper_citation_map.md) identifies
the final supplied PDF by hash and maps all 31 citations to their evidence.
The R² endpoint, regular norm ranges, Weyl/LOG reductions and
central-charge identities have these read-only commands:

```bash
python3 -B computations/r2_ads5_paper_checks/checks.py
python3 -B computations/ads5_paper_checks/checks.py
python3 -B computations/central_charge_extremization/checks.py
```

All three use the existing SymPy requirement. Their package guides list
the exact identities and saved results. R² uses finite original matrices
at tau=2; Weyl/LOG use the final quadratic actions; the central-charge
package checks the paper's trial a,
c-extremization, current normalization and universal-twist formulas.
Each explicit --write-log option refreshes only that package's records.

### General AdS5 central charges and massless vectors

The [generic AdS5 massless-sector package](computations/generic_ads5_massless/README.md)
provides a separate read-only check for equations (3.63)–(3.64):

```bash
python3 -B computations/generic_ads5_massless/checks.py
```

It retains all three couplings and g symbolically, compares the source
representatives, and verifies the vector reduction by constrained and
multiplier routes at symbolic spectral parameter. It also checks an undivided
kinetic congruence, named single-invariant limits, the source hashes and the
stored outputs. Those limits set absent invariants to zero by definition;
no numerical coupling samples or scale choices enter the general calculation.
This calculation covers the stated massless sector.
The package guide gives the two explicit commands that regenerate only its
results and verification log.

### GB product bosonic matrices and norms

The [GB AdS3 × Sigma2 bosonic package](computations/gb_ads3_sigma2/README.md)
provides the complete regular-family quadratic matrices, physical divisors
and primary-norm calculations cited in Section 4.2 of the paper:

```bash
python3 -B computations/gb_ads3_sigma2/checks.py --norms
```

The verified environment above includes SymPy, SymEngine, python-flint and mpmath. The symbolic checks retain g, L and k throughout,
compare 662 off-shell matrix entries between the source representatives,
recompute exact maximal-minor certificates and check all stated harmonic
restrictions. The optional `--norms` flag separately repeats the labelled
v109 numerical tables at 80/140 digits. These numerical samples do not replace
the symbolic proofs. The package guide gives explicit regeneration commands
confined to its own outputs. The fermionic action and spectrum use the separate commands below.

The accompanying E-term deletion and six separate-model comparisons in
the final paper have their own numerical records and command:

```bash
python3 -B computations/gb_ads3_sigma2/product_checks.py --verify --fresh
```

The [package guide](computations/gb_ads3_sigma2/README.md) specifies its
high-precision background and rank checks. The four alternative-quantization
norm pairs are checked with the correlated branches stated in the paper;
this does not assert general boundary admissibility.

### GB product fermionic action

The [GB AdS3 × Sigma2 fermionic package](computations/gb_ads3_sigma2_fermionic/README.md)
evaluates the complete two-fermion action with full supercovariant
derivatives, including the coupled gravitino and compensator blocks:

~~~bash
python3 -B computations/gb_ads3_sigma2_fermionic/checks.py
~~~

Use the verified environment above. This read-only
command reparses the current component density, checks its 1184-term
coverage and fingerprints, and recomputes 96 matrices at the twelve
manuscript background/level choices. The LR algebra and background
identities are exact; GB contractions are double-precision numerical
evaluations. Derivative identities, the independent compensator diagonal,
Majorana pairing, SUSY columns, four negative controls and a two-resolution
polynomial interpolation check have their own recorded residuals.
These samples do not certify symbolic identities over all couplings.
The guide gives explicit regeneration commands limited to this package.
Root extraction and multiplet matching use the spectrum command below.
The separate package below continues its action input; neither package
claims a symbolic generic kernel-dimension theorem over all couplings.

### GB product fermionic spectrum

The [GB product fermion spectrum package](computations/gb_ads3_sigma2_fermionic_spectrum/README.md)
uses the coupled-action evaluator and the independently specified
bosonic prediction. Its guide distinguishes the read-only
check from the explicit reconstruction command:

~~~bash
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/checks.py
python3 -B computations/gb_ads3_sigma2_fermionic_spectrum/derive.py --workers 2
~~~

Use the verified environment above.
The second command writes only that package's operator and spectrum
outputs and may take substantially longer. Polynomial coefficients,
generic ranks and direct-action root residuals are numerical, with
independent projection and interpolation checks. Matching preserves
spin, R-charge and multiplicity. The twelve v109 GB samples and the
separate two-derivative surface and constant-torus limits are labelled
explicitly. These checks do not prove a symbolic rank identity over
all couplings or compute fermion norms. See the package guide for its
full recomputation and verification-log commands.

### Vacuum, torsion and corrected-composite correspondence

These read-only commands test the convention and
composite-map correspondence:

~~~bash
python3 -B computations/paper_conventions/checks.py
python3 -B computations/composite_vector_correspondence/checks.py
~~~

The [paper-convention package](computations/paper_conventions/README.md)
imports the general-action projection. It differentiates before imposing
the supersymmetric configuration, preserving all couplings, and checks
the torsion identities with free bilinear symbols. The
[composite-vector package](computations/composite_vector_correspondence/README.md)
checks exact SU(2), derivative, current and fermion-order identities
and separately tests the stated corrected blocks using a Grassmann
implementation with numerical bosonic coefficients and negative controls.
Each package's explicit --write-log option writes only its own reports.
The source-manifest inputs are checked before the algebra runs; the
external source folder is not a runtime dependency.

The [citation index](references/paper_citation_map.md) follows the 31 references
in the final manuscript. Each package's current log records its own checks.

### Mathematical scope of the symbolic checks

1. **Weyl-square vector determinant.** The determinant of the displayed
   $`3\times3`$ matrix in
   [physical operators](weyl2/ads5/details/physical_operators.md) equals
   ```math
   -\frac{2\alpha^2}{9g^2}
   \left[(t-\nu^2)^2-2g^2\nu^2\right],
   \qquad
   \nu^2=\frac{g^2}{2}-\frac3\alpha.

   ```
   The displayed form requires $`g\ne0`$ and $`\alpha\ne0`$.
   This check starts from the supplied matrix; it does not derive that matrix
   or the separate constraint factor $`t^2`$ from the action.
2. **NW–SE triplet lowering.** Independent symbolic symmetric triplets verify
   ```math
   \epsilon_{ki}\epsilon_{\ell j}
   \bigl(2V^{(k}{}_mL^{\ell)m}\bigr)
   =-2V_{(i}{}^kL_{j)k}.

   ```
   The entries of $`\epsilon`$ are its defining SU(2) convention, not sampled
   field values. This checks the connection sign in
   [equation (4.27a)](common/two_derivative_action/details/construction.md).
3. **Gauss–Bonnet curvature coefficients.** The
   [five-dimensional curvature decomposition](common/details/action_normalizations.md)
   gives
   ```math
   \ell_W+2\ell_{\log}\supset\frac18\mathrm{GB},
   \qquad
   -2\ell_W-4\ell_{\log}\supset-\frac14\mathrm{GB}.

   ```
   Consequently the corresponding curvature coefficients agree under
   $`\lambda=-2\lambda_{\rm GB}`$. This is coefficient matching, with
   curvature monomials retained as independent symbols; it is not a complete
   fermionic action equivalence.
4. **Gauss–Bonnet spinor coefficient products.** The displayed F25 reduction in
   the [fermionic expansion](gauss_bonnet/ads5/code/derivations/support/gb-splus-fermionic-expansion-EXPLAIN.md)
   contains
   ```math
   \frac{512}{3}\frac{g^2}{64}=\frac{8g^2}{3},\qquad
   \frac{256igx}{3\sqrt2}\frac{g^2}{64}
   =\frac{4ig^3x}{3\sqrt2}.

   ```
   Both coefficient identities hold for symbolic $`g,x`$. This check does not
   reconstruct the remaining quadratic-action entries.

### Component construction details

The commands below run the component checks using the environments specified
in their package guides; these are additional component checks, beyond the nine
paper packages. They leave repository inputs and scientific outputs unchanged.

| Construction | Command from the repository root | Successful completion |
|---|---|---|
| Two derivatives | `python3 -B computations/two_derivative_fermionic/src/kernels/audit_exact_checks.py` | `PASS current two-derivative map, gauging, fermion kernels and spectrum` |
| R² | `python3 -B computations/r2_fermionic/checks/run_component_checks.py` | `PASS current R² component checks; repository files unchanged` |
| Weyl | `python3 -B computations/weyl_fermionic/checks/reference_suite.py` | `PASS 13 Weyl component check programs; current inputs preserved.` |
| LOG interfaces | `(cd computations/log_fermionic && python3 -B -m checks.test_contract)` | Six tests and `OK` |
| GB AdS5 stored-output comparison | `(cd gauss_bonnet/ads5/code && python3 -B -m unittest checks.test_reproduction)` | Twelve tests and `OK` |

The R² and Weyl suites execute their component construction in temporary
directories. Their package guides give the precise mathematical scope. The LOG
interface tests and GB stored-output comparisons have narrower scopes than a
full component reconstruction. The [LOG guide](computations/log_fermionic/README.md)
and [GB AdS5 guide](gauss_bonnet/ads5/code/README.md) state the separate regeneration
commands and their write behavior.

The [calculation index](computations/README.md) connects each construction to its
component maps, coefficient ledgers and analytic derivation.

`python -B reproduce.py` runs the nine paper packages and the additional
checks and two Section 4 figure builds below. `--all` includes the component
suites, four auxiliary identities, separate-model checks and regression tests.

</details>

## Section 4 background checks and figures

The [exceptional-background and tower-norm checks](computations/paper_extra_checks/README.md)
cover the exceptional family in Section 4.1, the two isolated points in
Section 4.3 and the large-level spin-2 criterion in Section 4.5.
[Figures 2 and 3](figures/README.md) are generated from the existing formulas
and saved bosonic results. These commands are also included in the normal reproduction run:

```bash
python -B computations/paper_extra_checks/exceptional_points.py
python -B computations/paper_extra_checks/tower_norm_rule.py
python -B figures/make_l0_family.py --output-dir /tmp/sugra-figures
python -B figures/fig_towers.py --output-dir /tmp/sugra-figures
```

## Scientific scope

<details>
<summary>Results, parameter domains and limitations</summary>

All counts below concern local linearized propagation on the stated backgrounds.
The component densities are used through quadratic order in the fermions; on a
bosonic background, terms of degree four and higher do not enter the quadratic
fermionic Hessian. This does not identify a two-fermion action with an
all-orders fermionic completion.

| Analysis | Result represented | Domain and limitation |
|---|---|---|
| Two-derivative AdS₅ | 12 bosonic and 12 fermionic local polarizations; BF scalar | $`g\ne0`$, $`L_0=1`$ follows from its background equations; logarithmic scalar boundary data are separate |
| R² AdS₅ | Regular 20+20 spectrum; analytic fermion reduction, norm signs and critical actions | Positive-norm region $`0<\lambda_{R^2}g^2<1/4`$; the final paper's negative-norm interval and tau=2 Jordan endpoint are treated separately |
| Weyl² AdS₅ | Generic 44+44 spectrum of the displayed component Hessian | Exceptional masses and ranks are treated separately using the final component action |
| LOG AdS₅ | Generic 44+44 spectrum with signed fermion roots | Real background and real characteristic roots are distinct conditions; kinetic critical points have separate reductions |
| Gauss–Bonnet AdS₅ | Regular 12+12 local spectrum and positive source-relative kinetic weights | $`g\ne0`$, $`a=\lambda_{\rm GB}g^2>-1/2`$, $`0<x<2`$; raw quadratic action vanishes at the endpoint $`x=2`$ |
| Gauss–Bonnet BPS AdS₃ × Σ₂ bosons | [Bosonic Hessians, physical polynomials and primary norms](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md); generic and special harmonic levels | Symbolic $`g,L,k=\lambda g^2`$; regular $`P_1\cdots P_5\ne0`$ domain, explicit chirality and chart limits. The separate fermionic action and spectrum, boundary admissibility and global charged multiplicities are outside this package |
| General four-invariant combination | [AdS₅ central charges and massless vectors](generic_combination/ads5/central_charges_and_massless_vectors.md), [anomalies and extremization](generic_combination/ads5/anomalies_and_extremization.md) | Two-derivative coefficient one; all three higher-derivative couplings symbolic, with the stated supersymmetric-vacuum and regular-pole conditions |

### Interpreting the verification

The [fermion spectrum calculation](gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_spectrum.md)
extends the regular BPS product analysis with mode operators, physical roots
and fixed-charge multiplet comparisons at the stated numerical samples.
It checks the two SUSY kernel directions and generic rank within those
samples. This is not a symbolic maximal-minor certificate for arbitrary
couplings, a fermion-norm calculation or a global harmonic count.

The [complete final-paper citation map](references/paper_citation_map.md)
connects all 31 citations to their derivations, calculations and current results.

The [source map](references/source_map.md) identifies action-to-Hessian
derivations. The [verification record](references/verification_scope.md)
distinguishes these derivations from the subset of identities checked by the
root programs. The [reproduction guide](#reproduction) states exact inputs,
dependencies, commands, outputs and exclusions.

Established multiplet constructions are adopted with
[literature and equation references](references/bibliography.md).
Their adoption does not certify modified local coefficients; conversely,
absence of a fresh proof of an adopted construction is not by itself a gap in
the spectrum derivation.

### Conventions and boundaries

The [common conventions](CONVENTIONS.md) retain the authoritative index,
Clifford and density definitions. Explicit orientation or adjoint choices in a
source derivation are source-local data. A Majorana bilinear transpose is not
automatically a physical Hermitian adjoint.

Local masses, local polarization counts, boundary-admissible solutions and
global normal frequencies are different quantities. A vanishing quadratic
coefficient alone establishes neither an additional nonlinear gauge symmetry
nor the degree-of-freedom count of the full interacting theory.

</details>

## Action and coupling correspondence

<details>
<summary>Component basis and Gauss–Bonnet normalizations</summary>

The shared component basis is

```math
\ell_{\le2}
=\ell_{2,\le2}+\alpha\ell_{W,\le2}
+\beta\ell_{\log,\le2}+\zeta\ell_{R,\le2}.
```

The [assembled bosonic action](generic_combination/action.md) retains
$`c_2\ell_2`$ and names its R² coefficient $`\lambda`$. The paper calculations
use $`c_2=1`$ and $`\lambda=\zeta`$; the
[normalization dictionary](generic_combination/action_inputs.md) fixes this
correspondence.

| Calculation | Component source | Scientific role |
|---|---|---|
| Two-derivative reference | [2016-map construction](common/two_derivative_action/details/construction.md) | Common light-sector input; the literal 2013-map comparison is a distinct expression |
| R² | [Mixed composite construction](r2/action/details/construction.md) | Primed/unprimed roles and source-supercovariant derivatives remain distinct |
| Weyl² | [Weyl action](weyl2/action/README.md) | The spectrum uses the specified component version and its explicit Hessian |
| LOG | [Primary and descendant construction](log/action/details/construction.md) | Ordered derivatives, component bridge and terms up to quadratic order in the fermions are retained |
| Gauss–Bonnet | [GB spectrum action](gauss_bonnet/action/gb_splus_action.md) | Two-derivative, OP-normalized Weyl and converted LOG inputs are combined before the Hessian |
| General combination | [Action and AdS₅ calculations](generic_combination/README.md) | Central charges, massless-vector kinetic terms and extremization with all three higher-derivative couplings symbolic |

### Gauss–Bonnet coupling labels

The common-basis combination and its pure-curvature contribution are

```math
\ell_G=\ell_W+2\ell_{\log},\qquad
\ell_G\big|_{\mathrm{curv}^2}=\frac18
(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2).
```

The selected GB spectrum uses

```math
\ell_2+\lambda_{\rm GB}(-2\ell_{W,\mathrm{OP}}-4\ell_{\log}),
\qquad
\ell\big|_{\mathcal G}=-\frac{\lambda_{\rm GB}}4\mathcal G.
```

For identical component representatives the coefficient correspondence is
$`\lambda_{\rm common}=-2\lambda_{\rm GB}`$.
The [GB input record](gauss_bonnet/ads5/action_inputs.md) identifies the actual
versions. Pure-curvature coefficient matching alone is not a complete
fermionic equivalence proof.

</details>

## Abstract

We study the spectra and the central charges of off-shell gauged five-dimensional $`\mathcal N=2`$ supergravity extended by the Weyl squared, Ricci tensor squared and Ricci scalar squared invariants, and by their Gauss-Bonnet combination.
Working exactly in the couplings and keeping all auxiliary fields, we organize the spectra around the maximally supersymmetric AdS₅ vacuum into supermultiplets.
With the Ricci scalar squared invariant, the spectrum gains a long vector multiplet and is free of ghosts in a finite range of the coupling, while with the Weyl squared or Ricci tensor squared invariant, it gains a long spin-2 multiplet and always contains ghosts or instabilities.
The Gauss-Bonnet combination adds no new modes: around its supersymmetric vacuum, the quadratic action is a rescaled copy of that of the two-derivative theory, and this fixes the spectrum of the Ricci tensor squared extension.
We also compute the central charges $`a`$ and $`c`$ and the flavor central charge exactly in the couplings.
The vacuum equation is $`a`$-maximization, and the kinetic terms of the massless graviton and vector multiplets are proportional to $`c`$ and to the flavor central charge, so that the critical points, where the massive spin-2 multiplet becomes degenerate with the graviton multiplet, are zeros of $`c`$.
Finally, around supersymmetric AdS₃ × Σ₂ backgrounds of the Gauss-Bonnet extension, the two-dimensional central charges are reproduced by $`c`$-extremization, while the spectrum is generically not unitary and contains towers of states whose energies stay bounded at large Kaluza-Klein levels.
In part of the parameter space, the tower of spin-2 multiplets has positive norm, so that the spectrum has no finite density of states.


## Authorship and citation

The accompanying paper's Acknowledgments credit Claude Opus 5.5 and GPT-6 Astra
for assistance in constructing this repository. The component sources,
conventions, calculation methods and verification limits are documented in
[source correspondence](references/source_map.md) and
[verification scope](references/verification_scope.md); the executable checks
provide the reproducible evidence for the stated results.

Use [CITATION.cff](CITATION.cff) for the authors and repository citation.
Original code is licensed under MIT; original documents and data under
CC BY 4.0. See [LICENSE](LICENSE). Attributed third-party material retains
its original terms. Published sources are listed in the
[bibliography](references/bibliography.md) and [BibTeX file](references/bibliography.bib).
