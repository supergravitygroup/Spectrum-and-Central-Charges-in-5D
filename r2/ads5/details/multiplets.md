# AdS5 supermultiplets

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="14-multiplets-of-the-preserved-ads₅-superalgebra"></a>

## Multiplets of the preserved AdS₅ superalgebra

Eight real Killing supersymmetries give the $`\mathfrak{su}(2,2|1)`$ superalgebra. Let $`(j_L,j_R)`$ be half-integer spin labels. The overall R-charge sign is named so that
```math
Q:(\tfrac12,0)_{-1},\qquad\bar Q:(0,\tfrac12)_{+1},\qquad
[E,Q]=Q/2
```
The two internally charged scalars have charges $`\pm2`$, the fermions $`\pm1`$, and the other bosons zero. Changing the sign of $`g`$ exchanges the low/high-energy labels of the heavy spinors. Representation names follow [Córdova–Dumitrescu–Intriligator](https://arxiv.org/pdf/1612.00809), §§2.2.1 and 5.5.1; the mass matching below follows from the independent operator calculation.

<a id="141-long-vector-multiplet"></a>

### Long vector multiplet

Let the neutral scalar primary $`|\Omega\rangle`$ have energy $`\Delta`$. The exterior powers of the four raising supercharges,
```math
\bigwedge\nolimits^\bullet[(\tfrac12,0)_{-1}\oplus(0,\tfrac12)_{+1}]
```
give the content

| Level | Energy | Representation | Field |
|---|---|---|---|
| 0 | $`\Delta`$ | $`(0,0)_0`$ | $`\sigma_-`$ |
| 1 | $`\Delta+1/2`$ | $`(1/2,0)_{-1}\oplus(0,1/2)_{+1}`$ | $`\chi_{s_g}`$ |
| 2 | $`\Delta+1`$ | $`(0,0)_{-2}\oplus(1/2,1/2)_0\oplus(0,0)_{+2}`$ | $`\Pi^{ij},\mathsf E`$ |
| 3 | $`\Delta+3/2`$ | $`(1/2,0)_{+1}\oplus(0,1/2)_{-1}`$ | $`\chi_{-s_g}`$ |
| 4 | $`\Delta+2`$ | $`(0,0)_0`$ | $`\sigma_+`$ |

With $`\bigwedge^2(2\oplus2)=1\oplus4\oplus1`$,
```math
N_B=1+(1+4+1)+1=8,\qquad N_F=4+4=8.
```
The mass–energy check gives
```math
\begin{aligned}
M_-^2\ell^2&=(\nu+1)(\nu-3),&
M_\Pi^2\ell^2&=(\nu+2)(\nu-2),\\
M_V^2\ell^2&=(\nu+1)(\nu-1),&
M_+^2\ell^2&=(\nu+3)(\nu-1)
\end{aligned}
```
and, with $`|\mu_{s_g}|\ell=\nu-1/2`$ and $`|\mu_{-s_g}|\ell=\nu+1/2`$,
```math
\boxed{\Delta_{\mathrm{long}}=\nu+1}
```

For a neutral scalar primary, the shortening threshold is checked directly from the supercharge norm. With normalization
```math
\{S^\alpha,Q_\beta\}=2\delta^\alpha{}_{\beta}(E+3R/2)+4M_\beta{}^\alpha
```
we have
```math
S^1Q_1Q_2|\Omega\rangle
=[2(\Delta+1/2)-3-2]Q_2|\Omega\rangle
=2(\Delta-2)Q_2|\Omega\rangle,
```
```math
\|Q_1Q_2|\Omega\rangle\|^2
=4\Delta(\Delta-2)\|\Omega\|^2.
```
Shortening occurs at $`\Delta=2`$. On the healthy positive interval, $`\Delta>3`$; at $`19/121`$, $`\Delta=4`$, and at the formal $`A=0`$ limit, $`\Delta=3`$. The long multiplet undergoes no BPS shortening at either point. On the upper interval $`1/4<\lambda g^2<1/3`$, $`2<\Delta<3`$: the representation is unitary, but this action assigns negative norm to it and to the graviton multiplet. At $`\lambda g^2=1/3`$, $`\Delta=2`$ and the local vector/spinor operators have the [Jordan structure](critical_branches.md#tau-2-endpoint) described separately; singular generic eigenfields cannot be continued through this point.

<a id="142-graviton-and-massless-vector-multiplets"></a>

### Graviton and massless vector multiplets

```math
\mathcal G:
v[E=3]\oplus\psi^{3/2}[E=7/2]\oplus h^{\mathrm{TT}}[E=4],
```
```math
\mathcal V_0:
\sigma_0[E=2]\oplus\zeta_0[E=5/2]\oplus\widehat c[E=3].
```
For the graviton multiplet, conservation/gauge conditions give
```math
N_B=(4-1)+(9-4)=8,\qquad N_F=2(6-2)=8.
```
For the massless vector multiplet,
```math
N_B=1+(4-1)=4,\qquad N_F=2+2=4.
```
Thus, in the regular positive-coupling region $`0<\lambda g^2<1/3`$, excluding $`\lambda g^2=1/4`$,
```math
\boxed{\mathcal H_{\mathrm{phys}}
=\mathcal G_{8+8}\oplus\mathcal V_{0,4+4}
\oplus\mathcal V_{\mathrm{long},8+8}(\nu+1,0).}
```

At $`\lambda_{R^2}=0`$, the propagation system of the long multiplet disappears, leaving $`\mathcal G\oplus\mathcal V_0`$. At negative coupling, the same mass polynomials match $`\Delta=1+i\kappa`$ algebraically on the complexified solution space; this is not a unitary global-multiplet interpretation with positive norms and real energies.

<a id="143-multiplet-at-the-critical-point"></a>

### Multiplet at the critical point

```math
E_{\rho_1}=2,\qquad E_\Lambda=2+|m_c|\ell_c=5/2,
\qquad E_{\mathcal W}=3
```
With equal positive norm coefficients,
```math
\boxed{(\rho_1,\Lambda,\mathcal W)\in\mathcal V_0,
\qquad N_B=N_F=4.}
```
This expression applies only to the quotient with nonzero quadratic norm:
```math
\frac{\text{critical linear solution space}}
{\text{kernel of the quadratic symplectic form}}
=\mathcal V_0.
```
The zero-source boundary behaviors are $`\rho_1=z^2\rho_{\mathrm{reg}}+\cdots`$, $`\mathcal W_\alpha=z^2\mathcal W_{\alpha(2)}+\cdots`$, and $`\Lambda\sim z^{5/2}`$. The BF logarithmic source vanishes. The nonlinear fate of the zero-norm directions and any new interacting gauge algebra were not determined in this report.

