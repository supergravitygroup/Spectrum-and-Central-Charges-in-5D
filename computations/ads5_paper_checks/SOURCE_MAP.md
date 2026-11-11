# Formula inputs and manuscript correspondence

The source is the final paper `draft_v109.pdf` and its matching TeX file.
The manifest records their SHA-256 hashes; equation labels below refer to
that text.

| Citation item | Final-paper locator | Local mathematical input |
|---|---|---|
| 11 | Weyl quadratic-action paragraph, Wquad, WDT | [Quadratic action](../../weyl2/ads5/quadratic_action.md), (8), (13), (21), (23) |
| 12–13 | WV, WVmassless, Wmpm and the full-form-equation warning | [Coupled form equations](../../weyl2/ads5/details/gauge_constraints.md), (20)–(27); [operators](../../weyl2/ads5/details/physical_operators.md), $`M(t),Y_\sigma`$; [norms](../../weyl2/ads5/details/kinetic_norms.md) |
| 14–16 | $`\mathcal Q,\mathcal X`$, Wgravitino, WX and norm paragraph | [Quadratic fermions](../../weyl2/ads5/quadratic_action.md), (10), (18), (23); [mixed equations](../../weyl2/ads5/details/gauge_constraints.md), (35)–(46); [action pullback](../../weyl2/ads5/details/kinetic_norms.md#paper-reality-and-x-pullback) |
| 17 | Highest-helicity and longitudinal norm paragraph | [Norm factors and counts](../../weyl2/ads5/details/kinetic_norms.md); the replay supplies the underlying simple-pole coefficients, not a new global polarization calculation |
| 18–19 | Weyl special points $`\alpha g^2=6,-2`$ | [Critical operators and coupled equations](../../weyl2/ads5/details/critical_branches.md), §§15.2, 15.4 |
| 21–22 | LOGresult, LOGmap, LOGnu and direct-fermion paragraph | [LOG quadratic action](../../log/ads5/quadratic_action.md); [LOG coupled operators](../../log/ads5/details/physical_operators.md), (O-43)–(O-52); [root table](../../log/ads5/fermionic_spectrum.md), (M-16)–(M-19) |
| Convention bridge | Jdef; Appendix A, Majorana and symplectic-Majorana equations | The paper supplements the component formal component-bar rules; the explicit matrix check is a realization of those supplied identities |

The Weyl internal matrix $`J_{\rm s}`$ and paper matrix $`\mathbb J`$ satisfy
$`J_{\rm s}=i\mathbb J`$ and $`m=-\bar m\mathbb J`$.
For LOG, source-local $`\alpha`$ is paper $`\beta`$,
$`t=igM=-\ell^{-1}\mathbb J`$ and the local operator variable is
$`J=t^{-1}D`$. Thus $`\Delta_{\rm source}=2\nu_{\rm paper}`$; the
spinor root sign labels in the source table are interchanged when needed
to match the paper's $`\chi_\pm`$ labels. Both signed roots are retained.

The sources are read and hashed; the check formulas are newly written in
this package's own organization. A passing source lock checks provenance,
while a passing algebra residual checks only its stated identity.
