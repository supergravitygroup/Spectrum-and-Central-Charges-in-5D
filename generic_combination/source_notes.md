# Sources, conventions and verification scope

The action source identifier is `GENERIC-COMBINATION-BOSONIC-v1`.
The [component action](action.md) identifies its four invariant blocks,
normalization maps and bulk representatives. Published superconformal
constructions are adopted as inputs; the assembly does not provide a new
nonlinear supersymmetry certification.

## Component sources

| Block | Source |
| --- | --- |
| Two derivative | [Gauged component construction](../common/two_derivative_action/details/construction.md) |
| Weyl | [Gauged Weyl construction](../weyl2/action/details/construction.md) |
| LOG | [Gauged LOG construction](../log/action/details/construction.md) |
| R² | [Canonical BF construction](../r2/action/details/construction.md) and [assembled component action](../r2/action/details/source_action.md) |
| Relative GB normalization | [Full-invariant normalization bridge](../gauss_bonnet/action/details/gb_splus_construction.md), GB16–GB20 |

The retained [assembly record](details/bosonic_assembly.json) concerns exact
expression transfer and normalization algebra. The [readback record](details/action_readback.json)
concerns the 43 displayed equations. These records do not certify new
invariants or a general spectrum.

## Conventions and scope

The repository uses the [common conventions](../common/conventions.md).
The [action](action.md) retains epsilon symbolically and uses
$`\nabla_\mu L_{ij}=\partial_\mu L_{ij}-2V_{\mu(i}{}^kL_{j)k}`$.
The [NW–SE derivation](../common/two_derivative_action/details/construction.md)
provides the lower-triplet sign. Source-specific spinor choices in bosonic
records do not extend the common fermion dictionary.

The compact densities retain their stated bulk representatives. Integrations
by parts require the displayed boundary transfers, compact support or
compatible boundary flux conditions; they do not specify counterterms or a
global boundary variational principle.

The [AdS5 calculation](ads5/central_charges_and_massless_vectors.md) supplies
the central charges and two massless-vector kinetic coefficients with all
three invariant couplings symbolic and $`c_2=1`$. Its
[source projection and checks](../computations/generic_ads5_massless/README.md)
include the constant-curvature density, tadpoles, vector–form quadratic block
and explicit regular-pole conditions. The [anomaly calculation](ads5/anomalies_and_extremization.md)
supplies the trial functions and their extremization.

The full generic quadratic action, remaining physical-mode reductions and
kinetic norms, mass spectrum and BPS count are not supplied. Global topology,
flat holonomies, boundary conditions and quotients are not fixed by these
local calculations. Individual invariant-family spectra retain their own domains.
