# Stability and boundary conditions

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="12-stability-and-global-boundary-conditions"></a>

## Stability and global boundary conditions

<a id="121-positive-coupling-region"></a>

### Positive-coupling region

```math
0<\lambda_{R^2}g^2<\frac14
\quad\Longrightarrow\quad1<L<\frac43,\quad A>0,\quad B>0,\quad\nu>2.
```
All norm coefficients are positive. The scalar BF conditions are satisfied through
```math
4+M_0^2\ell^2=0,\qquad
4+M_\pm^2\ell^2=(\nu\pm1)^2>0,\qquad
4+M_\Pi^2\ell^2=\nu^2>0
```
$`M_V^2\ell^2=\nu^2-1>0`$; the fermionic first-order masses are real. With the stated standard boundary conditions, the quadratic physical system therefore has no ghost or linear BF instability. This is not a nonlinear stability theorem.

### Upper positive-coupling interval

For $`1/4<\lambda_{R^2}g^2<1/3`$, equivalently $`3/2<\tau<2`$, one has $`4/3<L<2`$, $`A<0`$, $`B>0`$, and $`1<\nu<2`$. All the scalar BF expressions displayed above remain nonnegative, the vector mass remains positive, and the fermion masses remain real. Nevertheless the graviton and long vector multiplets have negative norm, as follows from the [kinetic coefficients](kinetic_norms.md). The massless vector multiplet has positive norm. The singular endpoint $`\tau=2`$ is the separate local [Jordan-pair calculation](critical_branches.md#tau-2-endpoint); no logarithmic boundary domain is selected here.

<a id="122-negative-coupling-region"></a>

### Negative-coupling region

```math
\lambda_{R^2}<0\quad\Longrightarrow\quad0<L<1,\quad
\nu=i\kappa,\quad\kappa^2=\frac{4-L}{2(1-L)}>2.
```
The final square in the scalar kinetic square completion has the opposite sign; $`k_{\mathsf E}<0`$. The fermionic $`(\zeta,\xi)`$ kinetic block is positive for $`A>0`$, with determinant $`4/(3L^2)>0`$, while the separate $`\Lambda`$ direction has coefficient $`\lambda<0`$. The norm problem of the coupled system therefore cannot be diagnosed from the graviton coefficient alone.

```math
M_\Pi^2\ell^2=-4-\kappa^2<-4,\qquad
M_\pm^2\ell^2=-3-\kappa^2\pm2i\kappa.
```
There is BF violation and a pair of complex-conjugate roots. These were retained in the spectrum, with the observation that they do not define a healthy positive-norm global theory. For modes below the BF bound, the standard source/response distinction based on real exponents does not apply directly; no extra boundary phase or other extension was selected implicitly.

<a id="123-sources-responses-and-energies"></a>

### Sources, responses, and energies

Near the boundary, for $`z\to0`$, the scalar equation gives
```math
\Box q=\ell^{-2}(z^2q''-3zq')+\cdots,
\quad q\sim z^\Delta
\quad\Longrightarrow\quad\Delta(\Delta-4)=M_s^2\ell^2
```
With $`\eta_s=\sqrt{4+M_s^2\ell^2}`$,
```math
q=z^{2-\eta_s}a+z^{2+\eta_s}b+\cdots,
\quad\mathcal F_{\partial}\propto2\ell^3\eta_s(a_1b_2-a_2b_1).
```
The standard choice is $`a=0`$. At BF saturation,
```math
q=z^2(a_{\log}\log z+b)+\cdots,\qquad a_{\log}=0.
```
This logarithmic source must be distinguished from a repeated physical bulk-operator root.

For a spinor,
```math
[\gamma^{\hat z}(z\partial_z-2)-\mu\ell\mathbb J]\chi=0
```
determines the boundary data in the two projector sectors. For real mass, the normalizable energy is $`E_f=2+|\mu|\ell`$; the entire spinor field is not set to zero. For a vector,
```math
M_v^2\ell^2=(E_v-1)(E_v-3)
```
with the standard branch.

| Mode | Lowest normalizable AdS energy, $`0<\lambda g^2<1/3`$, $`\lambda g^2\ne1/4`$ |
|---|---:|
| $`h^{\mathrm{TT}}`$ | $`4`$ |
| $`\psi^{3/2}`$ | $`7/2`$ |
| $`v,\widehat c`$ | $`3`$ |
| $`\sigma_0`$ | $`2`$ |
| $`\zeta_0`$ | $`5/2`$ |
| $`\sigma_-`$ | $`\nu+1`$ |
| $`\chi_{s_g}`$ | $`\nu+3/2`$ |
| $`\Pi^{ij},\mathsf E`$ | $`\nu+2`$ |
| $`\chi_{-s_g}`$ | $`\nu+5/2`$ |
| $`\sigma_+`$ | $`\nu+3`$ |

This boundary choice applies to each independent operator root. Discarding heavy modes at finite $`\lambda`$ is not a boundary choice made in this calculation. General mixed boundary conditions, alternative quantizations, and classification of all finite boundary counterterms are outside its results. The general boundary-value framework agrees with [Ishibashi–Wald](https://arxiv.org/pdf/hep-th/0402184); masses and norms were not taken from that source.

