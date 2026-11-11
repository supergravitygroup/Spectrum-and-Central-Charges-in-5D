# Paper scope, provenance and the spin connection

This page connects citation-map items 27–29 to the repository's existing
action definitions and to the bounded checks in
[paper_conventions](../computations/paper_conventions/README.md).
The equation labels refer to the final supplied manuscript.

## Item 27: finite couplings and retained fields

The [generic action](../common/generic_action.md) is linear in independent,
finite coefficients alpha, beta and zeta. Its bosonic and two-fermion
parts retain their nonlinear bosonic dependence. Expanding in
fluctuation amplitude is distinct from expanding in these coefficients.
The [fluctuation prescription](../common/fluctuation_method.md) retains
the independent fields

```math
\begin{aligned}
\Phi_B&=\{e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},
             L,N,V_\mu,V_\mu^{\prime ij}\},\\
\Phi_F&=\{\psi_\mu^i,\varphi^i\}.
\end{aligned}
```

The quantities T, D and chi of the standard Weyl multiplet and the
connections omega, phi and f are defined composites or dependent
connections in this formulation. Substitution of their defining
expressions is not elimination of an independent auxiliary field by
its field equation. Later physical reductions must keep their
constraints and denominator conditions.

The completeness statement is attached to the specified actions and
backgrounds. The [source map](source_map.md) and
[fermionic input correspondence](fermionic_input_correspondence.md)
identify the AdS5 reductions. The
[bosonic BPS product chapter](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/README.md)
and [fermionic quadratic action](../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/fermionic_quadratic_action.md)
give their respective product-background inputs. The item-26 physical
root and multiplet comparison must be assessed from its own completed
calculation; these convention checks do not establish it.
No full three-coupling fluctuation spectrum, excluded-background
spectrum or universal boundary-unitarity theorem follows from item 27.

### Why the vacuum depends on tau

On the zero-flux, constant-scalar maximally symmetric ansatz let
R = 20k, with the supersymmetric configuration

```math
\begin{aligned}
N_0&=-\frac32gL_0^2,&
k&=-\frac12g^2L_0^2,&
\ell^{-2}&=\frac12g^2L_0^2,\\
\tau&=(\beta+6\zeta)g^2,&
Q&=\tau L_0^2-8L_0+8.
\end{aligned}
```

The [item-23 source projection](../computations/generic_ads5_massless/SOURCE_MAP.md)
keeps L, N and k independent until after differentiation.
Writing its scalar density as F, direct differentiation gives

```math
\begin{aligned}
\left.\partial_NF\right|_{\mathrm{SUSY}}&=-\frac g2Q,\\
\left.\partial_LF\right|_{\mathrm{SUSY}}&=\frac{g^2L_0}{2}Q,\\
\left.\left(\frac F2-\frac k5\partial_kF\right)\right|_{\mathrm{SUSY}}
 &=\frac{g^2L_0^2}{2}Q.
\end{aligned}
```

For g nonzero and $`L_0>0`$, all three equations reduce to Q = 0.
No coupling was assigned a sample value or treated perturbatively.
The Einstein-connected root selected in the paper is
$`L_0=2/(1+\sqrt{1-\tau/2})`$ on its real domain; the polynomial
identity itself does not select a branch.

On this ansatz the [Weyl invariant](../weyl2/action/bosonic.md) reduces to

```math
\begin{aligned}
\mathcal F_W&=\frac{64}{3}\overline D^{\,2},&
\overline D&=-\frac58k+\frac14gN+\frac1{16}g^2L^2,\\
\left.\overline D\right|_{\mathrm{SUSY}}&=0,&
\left.\partial_{(L,N,k)}\mathcal F_W\right|_{\mathrm{SUSY}}&=0.
\end{aligned}
```

The Weyl-tensor square and the remaining bosonic terms are at least
quadratic in quantities vanishing on this background. Thus the
vanishing is a statement about its value and first variation. It does
not remove its quadratic action: for example
$`\partial_N^2\mathcal F_W=8g^2/3\ne0`$.
The absence of alpha from the vacuum equation does not remove alpha
from the spectrum. The executable check imports the existing source
projection and repeats this differentiation; it does not constitute a
second derivation of every term in the full component action.

## Item 28: calculation support

The [complete citation index](paper_citation_map.md) and
[reproduction guide](../README.md#reproduction) identify the calculation details,
current checks and results accompanying the paper. The source attribution
in the paper's Acknowledgments remains in the manuscript.

The [central-charge package](../computations/central_charge_extremization/README.md)
contains trial a, the normalized flavor coefficient, c-extremization and
the universal-twist correction.

## Item 29: the connection retained in the component action

The paper's Lorentz derivative is the
[repository Lorentz derivative](../common/conventions.md#6-derivative-notation).
Its SU(2) contribution is separate:

```math
\begin{aligned}
\nabla_\mu^{\mathrm L}\zeta^i
 &=\left(\partial_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\zeta^i,\\
D_\mu^{\mathrm{connection}}\zeta^i
 &=\nabla_\mu^{\mathrm L}\zeta^i-V_\mu{}^{ij}\zeta_j
 \qquad(b_\mu=0).
\end{aligned}
```

This connection part is not the full field-dependent supercovariant
derivative. The [dependent connection](../common/details/source_conventions.md#7-connections-and-curvature-distinctions)
contains, in the Poincare gauge,

```math
\begin{aligned}
\omega_\mu{}^{ab}
 &=\omega_\mu{}^{ab}(e)+K_\mu{}^{ab},\\
K_\mu{}^{ab}
 &=\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
   +\frac14\bar\psi^a\gamma_\mu\psi^b .
\end{aligned}
```

With $`B_{acb}=\bar\psi_a\gamma_c\psi_b=-B_{bca}`$, the
contracted rank-one Majorana flip gives

```math
\begin{aligned}
K_{mab}&=\frac14(B_{abm}-B_{bam}+B_{amb}),\\
K_{mab}+K_{mba}&=0,&
K_{acb}-K_{bca}&=\frac12B_{acb}.
\end{aligned}
```

These are metric compatibility and the two-fermion coefficient of the
[conventional torsion constraint](../gauss_bonnet/ads5/code/references/COMPONENT_CONVENTIONS.md#geometry),
not independent field equations. The checker verifies all 125
components of each identity with free bilinear symbols. An incorrect
contracted flip fails antisymmetry; omitting the last contorsion term
fails the torsion constraint.

The [fermion grading](../common/fermion_order.md) and
[quadratic composites](../common/details/composite_fields.md#3-dependent-connections)
already retain this contribution. In a spinor kinetic bilinear,
K contributes at four-fermion order. In a bosonic-form curvature it
contributes at two-fermion order through
$`R^{(2)}=2\nabla^{(0)}_{[\mu}K_{\nu]}`$, so it cannot be discarded
from the whole action. The
[product-background implementation](../computations/gb_ads3_sigma2_fermionic/objects2.py)
retains this curvature contribution explicitly. The LR scalar
contraction's total-divergence simplification on its stated background
does not justify deleting torsion elsewhere.
