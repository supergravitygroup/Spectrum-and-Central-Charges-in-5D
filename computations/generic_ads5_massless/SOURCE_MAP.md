# Source projection for citation-map item 23

The inputs are the current [generic bosonic action](../../generic_combination/action.md),
equations G-2D, G-W, G-LOG and G-R2, with their definitions G-D1--G-D15.
They use the [common action normalization](../../common/generic_action.md).
The component-action coefficient c2 is one, and its lambda is zeta here; see the
[normalization dictionary](../../generic_combination/action_inputs.md).
All integrations by parts below are bulk equalities modulo the displayed
total divergences' integrals, for compactly supported variations or compatible
boundary flux conditions. They do not specify a global boundary problem.

## Background and retained fields

Write L for L0 in this derivation and set

```math
\begin{aligned}
r&=\ell^{-2}=g^2L^2/2,& k&=-r,&N_0&=-3gL^2/2,\\
Q&=(\beta+6\zeta)g^2L^2-8L+8=0,& L&>0,&g&\ne0.
\end{aligned}
```

These are the paper's supersymmetric AdS5 relations. The
[constant-curvature density and tadpoles](../../generic_combination/background_equations.md)
retain the background projection used below.
The metric, L and N are fixed to their background values only when selecting
the singlet vector quadratic sector. In the background and TT calculations,
curvature coefficients and tadpoles are extracted before imposing these
relations. There is no use of the two-derivative auxiliary equations in the
four-derivative action.

In the singlet sector let c and v denote the fluctuations of C and V. The
traceless internal connection is zero in this sector. Its absence is justified
by the residual internal charge decomposition; G-D5 has no singlet V term in
the covariant derivative of the background compensator triplet.

For the local spin-one calculation decompose the dual two-form H into an
exact part dh and a co-closed part. Here h is a vector potential for that exact
part, not the metric fluctuation. The co-closed part has zero divergence and
is orthogonal to dc, dv and dE under integration by parts. Constant-curvature
derivative operators preserve this decomposition. Parity-odd field-strength
terms start at cubic order on the zero-form background. Thus the two parts
decouple in the singlet vector quadratic block. This is a sector projection,
not an assertion that the full H is globally exact.

For transverse vector amplitudes define

```math
\begin{aligned}
\mathcal O a_b&=\bar\nabla^a(da)_{ab}=x a_b,&
\bar\nabla^b(da)_{ab}&=-x a_a,\\
\langle da,db\rangle&=-2x\langle a,b\rangle,&
\langle\bar\nabla da,\bar\nabla db\rangle
&=(2x^2-12rx)\langle a,b\rangle.
\end{aligned}
```

Angle brackets include the AdS volume integral and Lorentzian contraction.
The second line follows from integration by parts and the two-form
Weitzenbock identity in five dimensions. The curvature contribution is
6r times the first two-form pairing. In the code these two pairings are
`pair` and `derivative_pair`. Their signs are fixed by the first line, rather
than by choosing a numerical mode.

The linearized G-D1 Bianchi identity is

```math
\bar\nabla^b H_{ab}=gE_a/2,
\qquad E+2xh/g=0.
```

The g-dependent term must remain. One route substitutes this constraint only
after constructing the quadratic density. The second varies a multiplier
term mu(E+2xh/g) in the unreduced five-field density. In particular, H=dh is
not substituted into an isolated H-squared term after imposing a Maxwell
equation: the E--C and E--V terms and the constraint are retained. This keeps
the first-order dualization contribution and its kinetic sign.

## Curvature inputs for a and c

`curvature_blocks()` transcribes the constant-scalar, zero-form projection of
G-2D, G-W, G-LOG and G-R2. The three curvature invariants remain independent.
For Weyl, retain

```math
\mathsf C^2=R_{abcd}^2-\frac43R_{ab}^2+\frac16R^2,
\qquad D=-\frac R{32}+\frac{gN}{4}+\frac{g^2L^2}{16}.
```

Then G-W is $`\mathsf C^2/8+64D^2/3`$ in this projection. For $`R^2`$,
G-D13 gives $`\boldsymbol Y^{ij}\boldsymbol Y_{ij}=(-R/2-N^2/L^2)^2`$,
while the explicit $`g^2`$ bracket in G-R2 is retained separately. The resulting
coefficients of $`R`$, $`R^2`$, $`R_{ab}R^{ab}`$ and $`R_{abcd}R^{abcd}`$ are

```math
\begin{aligned}
b_1={}&L+\alpha\left(-\frac{gN}{3}-\frac{g^2L^2}{12}\right)
+\beta\left(\frac{gN}{6}-\frac{g^2L^2}{12}\right)
+\zeta\left(\frac{N^2}{L^2}-\frac{g^2L^2}{4}\right),\\
b_2={}&\frac{\alpha+\beta}{24}+\frac\zeta4,\qquad
b_3=-\frac{\alpha+\beta}{6},\qquad b_4=\frac\alpha8.
\end{aligned}
```

Substitution $`R=20k`$, $`R_{ab}R^{ab}=80k^2`$, $`R_{abcd}R^{abcd}=40k^2`$
reproduces each block of the existing
[constant-curvature blocks](background_blocks.py).
`checks.py` verifies all four equalities before any coupling specialization.
It also differentiates the unrestricted density and verifies

```math
\mathcal E_N=-gQ/2,\qquad
\mathcal E_L=g^2LQ/2,\qquad
\mathcal E_g=g^2L^2Q/2
```

after the supersymmetric-background substitution.

## Vector term ledger

Every group below is encoded separately by `vector_groups()` in
[action_inputs.py](action_inputs.py). $`G,H,\mathcal V`$ denote $`dc,dh,dv`$;
$`J_T`$ denotes the second-index divergence of $`T`$. Terms absent from the
ledger either contain no vector, belong to a charged sector, or have field
degree at least three about the specified zero-form background.

| Code group | Current source | Quadratic contribution or reduction |
| --- | --- | --- |
| 2D-strengths | G-2D | $`-LG^2/2+4LH^2`$ |
| 2D-constrained-current | G-2D | $`-2E^2/L-2\sqrt2 E\cdot V-4gE\cdot C`$ |
| W-internal-strength | G-W internal curvature term | $`-\mathcal V^2/6`$ |
| W-T-derivatives | G-W three T derivative terms | $`-64(\nabla T)^2/3+64J_T^2`$ |
| W-T-curvature | G-W commutator and f correction | $`320rT^2/3`$ |
| W-gauging | G-W final term | $`-gL\mathcal V\cdot(G-2H)/(3\sqrt2)`$ |
| LOG-internal-strength | G-LOG first line | $`\mathcal V^2/12`$ |
| LOG-strength-mixing | G-LOG first line | $`gL\mathcal V\cdot(G+4H)/(6\sqrt2)`$ |
| LOG-curvature | G-LOG Ricci and scalar-curvature couplings | $`-2rG^2/3-4rGH/3+20rH^2/3`$ |
| LOG-N | G-LOG gN bracket | $`gN(-G^2/3-2GH/3+2H^2)`$ |
| LOG-L | G-LOG g-squared L-squared bracket | $`g^2L^2(G^2/24-GH/6-H^2)`$ |
| LOG-G-derivative | G-LOG divergence product | $`-(\mathop{\mathrm{div}}\nolimits G)^2/6`$ |
| LOG-current | G-LOG last line | $`gE\cdot\mathop{\mathrm{div}}\nolimits G/3+g^2E^2/3`$ |
| R2-Y-square | G-D13, G-R2 first term | $`2Y_0(G^2/4-2H^2-E^2/L^2)`$ |
| R2-composite-strength | G-D12, G-R2 | $`-\mathcal F^2/4`$, where $`\mathcal F=d(2E/L+\sqrt2v)`$ |
| R2-mixed-strength | G-R2 | $`(N/L)\mathcal F\cdot(G-4H)`$ |
| R2-N-square | G-R2 | $`-(N^2/L^2)(G^2-4HG)`$ |
| R2-gauging | G-R2 g-squared bracket | $`g^2L^2(G^2/8-H^2)-g^2E^2/2`$ |

For the Weyl reduction, the background $`\mathsf C`$ and $`D`$ vanish and
$`T=(G-2H)/8`$, $`f_{ab}=r\bar g_{ab}/4`$. In the pure vector sector $`D`$ begins
at degree two, so $`D^2`$ and $`DT^2`$ do not contribute. The relevant integrations by
parts are

```math
\begin{aligned}
\int(\nabla_bT_{ac})(\nabla^aT^{bc})
&=\int\left(J_T^2+3rT^2\right),\\
\int T_{ab}\nabla^b\nabla_cT^{ac}&=-\int J_T^2.
\end{aligned}
```

The first curvature term gives $`64rT^2`$; the explicit $`f`$ term gives
$`128rT^2/3`$. Their sum is $`320rT^2/3`$. This derives the two W-T
groups from G-W. In the [source building block](../../weyl2/action/bosonic.md),
these are terms b-012 and b-014, with the dependent-connection definitions
retained; b-013 and b-017 give the gauging and internal-strength groups.

For LOG the cyclic H-derivative term in G-LOG vanishes pointwise for H=dh.
Its explicit $`g^2E^2/3`$ must therefore be kept in this compact
representative. In the independently rewritten representative it is absorbed
by integration by parts, curvature commutators and the Bianchi identity.
With E not yet constrained, the difference of the two encoded LOG densities is

```math
\mathcal L_{\log,\mathrm{compact}}^{(2)}
-\mathcal L_{\log,\mathrm{rewritten}}^{(2)}
=\frac13(g^2E^2-4x^2h^2)
=\frac13(gE-2xh)(gE+2xh).
```

It vanishes on the Bianchi constraint. This identity is checked explicitly,
in addition to all four block comparisons. Dropping the compact E-squared
term before this conversion would change the calculation.

For R2, the background triplet is parallel to Lij and its coefficient is
$`Y_0=10r-N_0^2/L^2`$. Its quadratic shift is
$`G^2/4-2H^2-E^2/L^2`$. The singlet connection leaves
$`L^{ij}`$ covariantly constant, so G-D12 reduces to $`\mathcal F=d(2E/L+\sqrt2v)`$.
The charged part and scalar derivatives do not mix into this quadratic block.
These substitutions derive all five R2 groups directly from G-D12/D13 and G-R2.

## Independent matrix route and normalization

The compact route imposes the Bianchi constraint and writes the quadratic
density as $`x\,\mathbf w^TK(x)\mathbf w`$, where $`\mathbf w=(c,v,h)^T`$.
Thus $`K`$ is the Hessian of that density divided by $`2x`$. Its entries, including their full symbolic $`x`$
dependence, are saved in [results.json](outputs/results.json).

The rewritten route keeps (c,v,E,mu,h) and uses M = half the Hessian of the
density including mu(E+2xh/g). Eliminating the last three entries by a Schur
complement agrees with x times the compact route's h Schur complement for
symbolic x, not just at x=0. These are exact inversions of quadratic blocks;
no coupling expansion or original-action auxiliary truncation is made.

For the light block, $`M_{\rm light}=xZ/2+O(x^2)`$. Consequently the coefficient
of the pole in $`M_{\rm light}^{-1}`$ is $`2Z^{-1}`$. The inverse of the actual
Hessian $`2M`$ has pole coefficient $`Z^{-1}`$. `checks.py` verifies this factor
as well as the division-free congruence shown on the
[result page](../../generic_combination/ads5/central_charges_and_massless_vectors.md).

The low-x coefficient extracts a massless pole of the exact finite-coupling
operator. It is not a truncation in alpha, beta or zeta. Analytic inversions
require the stated nonzero pivots; the polynomial congruence is recorded
separately at their zeros.
