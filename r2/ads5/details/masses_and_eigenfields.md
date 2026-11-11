# Masses and reconstructed eigenfields

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="10-all-physical-masses-roots-and-field-combinations"></a>

## All physical masses, roots, and field combinations

For $`\lambda\neq0`$, define
```math
\nu^2=\frac2{\lambda g^2L}-2=\frac{4-L}{2(L-1)},\quad
U=X-\frac ALs,\quad Z=n+2gLs
```
Here $`\nu`$ is a scalar-spectrum parameter distinct from the internal triplet direction $`\nu_{ij}`$.

```math
\sigma_0=\frac LB\left(X-\frac92\lambda g^2Ls-3\lambda gn\right),
\qquad
\sigma_\pm=Z+\frac{2\pm\nu}{gA\ell^2}U.
```
The inverse transformation is
```math
\begin{aligned}
U&=\frac{gA\ell^2}{2\nu}(\sigma_+-\sigma_-),\\
Z&=\frac12(\sigma_++\sigma_-)-\frac1\nu(\sigma_+-\sigma_-),\\
s&=\sigma_0-\frac LB U+\frac{3\lambda gL}{B}Z,\quad
n=Z-2gLs,\quad X=U+As/L
\end{aligned}
```
and is nonsingular when $`\lambda AB\nu\ne0`$. In particular it applies on both sides of $`A=0`$, but not at $`A=0`$ or $`B=0`$ themselves.

With $`x=\ell^2\Box`$, the scalar determinant factorizes as
```math
\det(\mathsf Kx/\ell^2+\mathsf M)
=\frac{\det\mathsf K}{\ell^6}(x+4)
\left[(x+3-\nu^2)^2-4\nu^2\right]
```
Therefore
```math
\boxed{
M_0^2\ell^2=-4,\quad
M_\pm^2\ell^2=(\nu\pm1)^2-4,\quad
M_\Pi^2\ell^2=\nu^2-4,\quad M_V^2\ell^2=\nu^2-1.
}
```
Each scalar satisfies $`(\Box-M^2)\sigma=0`$. The $`\Pi`$ root gives the same mass for two real internal components.

For fermions, let $`y`$ be the eigenvalue of $`\mathbb J\mathord{\not{\nabla}}`$. The heavy-block polynomial is
```math
\begin{aligned}
\lambda(y+5m)(y-3m)-A
&=\lambda\left[(y+m)^2-16m^2-\frac A\lambda\right]\\
&=\lambda\left[(y+m)^2-\frac{\nu^2}{\ell^2}\right]
\end{aligned}
```
so
```math
\mu_0=m,\qquad\mu_\pm=-m\pm\frac\nu\ell,
\quad
\chi_\pm=\frac{\mathbb J\mathord{\not{\nabla}}-\mu_\mp}{\mu_\pm-\mu_\mp}\zeta_1.
```
```math
(\mathord{\not{\nabla}}-\mu_\pm\mathbb J)\chi_\pm=0,
\qquad(\mathord{\not{\nabla}}-m\mathbb J)\zeta_0=0.
```
The two eigenvalues of $`\mathbb J`$ do not justify double-counting the symplectic–Majorana field.

| Physical sector | Field/representation | Local polarizations |
|---|---|---:|
| Massless spin 2 | $`h^{\mathrm{TT}}`$ | 5 B |
| Massless vectors | $`\widehat c=c^{(0)}+\sqrt2v/(3gL),\ v`$ | 3+3 B |
| Proca | $`\mathsf E`$, $`M_V^2=B/\lambda`$ | 4 B |
| Neutral scalars | $`\sigma_0,\sigma_+,\sigma_-`$ | 1+1+1 B |
| Internally charged scalars | $`\Pi^{ij}`$ | 2 B |
| Massless AdS gravitino | $`\psi^{3/2}`$ | 8 F |
| Light spinor | $`\zeta_0`$ | 4 F |
| Two additional spinors | $`\chi_+,\chi_-`$ | 4+4 F |

```math
\boxed{N_B=N_F=20\quad(0<\lambda g^2<1/3,\ \lambda g^2\ne1/4).}
```
For $`\lambda=0`$, the original equations give $`n=-2gs`$, $`w=0`$, $`\mathsf E=0`$, and $`\zeta_1=0`$, with
```math
N_B=N_F=12.
```
The additional $`8+8`$ modes at finite $`\lambda`$ were not eliminated merely because they become heavy at small coupling.

