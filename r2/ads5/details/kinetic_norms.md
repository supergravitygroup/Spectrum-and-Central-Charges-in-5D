# Kinetic norms and propagator residues

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="11-kinetic-norms-and-propagator-residues"></a>

## Kinetic norms and propagator residues

Define the norm coefficients by
```math
\mathcal L_s=-\frac{k_s}{2}[(\nabla s)^2+M_s^2s^2],\quad
\mathcal L_v=-\frac{k_v}{4}F^2-\frac{k_vM_v^2}{2}v^2,
```
```math
\mathcal L_f=-\frac{k_f}{2}\bar f(\mathord{\not{\nabla}}-\mu\mathbb J)f
```
At a physical simple pole, the residue carries the coefficient $`1/k`$ with the corresponding standard physical projector. The massless-gravitino term induced by AdS curvature does not break SUSY gauge symmetry.

<a id="111-extracting-scalar-norms-from-the-coupled-system"></a>

### Extracting scalar norms from the coupled system

After separating metric mixing, the symmetric kinetic matrix of $`(X,s,n)`$ is
```math
K_s=\begin{pmatrix}
8/(3A)&-2/L&0\\-2/L&2/L+3\lambda g^2&6\lambda g/L\\0&6\lambda g/L&4\lambda/L^2
\end{pmatrix}
```
Completing the square in the kinetic density gives
```math
\boxed{
\mathcal L_{s,\mathrm{kin}}
=-\frac1{3A}(\nabla X)^2
-\frac A{L^2}\left(\nabla s-\frac LA\nabla X\right)^2
-\frac{2\lambda}{L^2}\left(\nabla n+\frac32gL\nabla s\right)^2.
}
```
For example, the coefficient of $`(\nabla s)^2`$ is
```math
-\frac A{L^2}-\frac92\lambda g^2
=-\frac1L-\frac32\lambda g^2=-\frac12(K_s)_{ss}
```
where $`A=L-3\lambda g^2L^2`$ was used. The determinant
```math
\det K_s=\frac{16\lambda}{3L^4}
```
is nonzero at $`\lambda\neq0`$.

For the Jacobian $`T=\partial(X,s,n)/\partial(\sigma_0,\sigma_+,\sigma_-)`$ of the [inverse eigenfield transformation](masses_and_eigenfields.md), direct multiplication gives
```math
T^TK_sT=\mathop{\mathrm{diag}}\nolimits\left(
\frac{2B}{3L^2},\frac{4A}{g^2L^4\nu(\nu+1)},
\frac{4A}{g^2L^4\nu(\nu-1)}\right)
```
The mass matrix also separates into the corresponding $`k_\sigma M_\sigma^2`$ values in the same basis.

For the internal connection, an equivalent first-order square completion uses
```math
2Aw^2+2\lambda(\nabla\cdot w)^2
\ \leftrightarrow\
2Aw^2+4\lambda\Pi\nabla\cdot w-2\lambda\Pi^2
```
Substituting $`w=\lambda\nabla\Pi/A`$ gives
```math
-\frac{2\lambda^2}{A}(\nabla\Pi)^2-2\lambda\Pi^2
\quad\Longrightarrow\quad k_\Pi=\frac{4\lambda^2}{A},\quad M_\Pi^2=\frac A\lambda.
```
This auxiliary calculation does not remove fields from the original off-shell action.

<a id="112-formvector-norms"></a>

### Form–vector norms

In an equivalent calculation retaining $`E=\nabla\cdot Q/g`$ with a multiplier, the algebraic two-form and multiplier equations give the physical vector kinetic terms
```math
\begin{aligned}
\mathcal L_{v,\mathrm{kin}}={}&-\frac A2(dc)^2
-\frac A{4g^2L^2}(\sqrt2\,dv+2gL\,dc)^2\\
&-\frac\lambda4(\sqrt2\,dv+2d\mathsf E/L+3gL\,dc)^2,
\qquad
\mathcal L_{v,\mathrm{mass}}=-\frac{2A}{L^2}\mathsf E^2.
\end{aligned}
```
Substituting $`c=\widehat c-\sqrt2v/(3gL)-g\lambda\mathsf E/B`$ cancels the kinetic cross terms:
```math
\mathcal L_v=-\frac{6B}{4}(d\widehat c)^2
-\frac14\frac{2A}{3g^2L^2}(dv)^2
-\frac14\frac{4A\lambda}{L^2B}(d\mathsf E)^2
-\frac12\frac{4A\lambda}{L^2B}\frac B\lambda\mathsf E^2.
```
The final term reproduces $`-2A\mathsf E^2/L^2`$ exactly. This result comes from the system retaining the $`g`$-dependent form mixing.

<a id="113-fermionic-norms"></a>

### Fermionic norms

The $`(\zeta,\Lambda,\xi)`$ matrix of the equivalent first-order kinetic system constructed with $`\xi=i\lambda\mathcal H\Lambda`$ is
```math
K_f=\begin{pmatrix}
4A/(3L^2)&0&-2/(3L)\\0&\lambda&0\\-2/(3L)&0&4/(3A)
\end{pmatrix},\qquad \det K_f=\frac{4\lambda}{3L^2}.
```
At a heavy root, $`\mathord{\not{\nabla}}\chi=\mu\mathbb J\chi`$,
```math
\zeta=a\,i\mathbb J\chi,\quad\Lambda=\chi,\quad\xi=b\,i\mathbb J\chi,
\quad a=\frac{\lambda L}{2A}(\mu+5m),\quad b=\lambda(\mu-m).
```
Using $`(i\mathbb J)^\sharp(i\mathbb J)=1`$,
```math
\begin{aligned}
k_\chi&=\frac{4A}{3L^2}a^2+\lambda-\frac4{3L}ab+\frac4{3A}b^2\\
&=\frac{2\lambda^2}{A}(\mu^2-m^2),
\qquad \lambda(\mu+5m)(\mu-3m)=A.
\end{aligned}
```
At the light root,
```math
\zeta=\frac AB\zeta_0,\quad
\Lambda=-\frac{2gA}{B}\mathbb I\zeta_0,\quad\xi=0
```
and hence
```math
k_{\zeta_0}=\frac{A^2}{B^2}\left(\frac{4A}{3L^2}+2\lambda g^2\right)
=\frac{4A^2}{3BL^2}.
```

<a id="114-combined-norm-table"></a>

### Combined norm table

With $`s_g=\mathop{\mathrm{sgn}}\nolimits g`$:

| Mode | Kinetic norm coefficient |
|---|---|
| $`h^{\mathrm{TT}}`$ | $`A/2`$ |
| $`\widehat c`$ | $`6B`$ |
| $`v`$ | $`2A/(3g^2L^2)`$ |
| $`\mathsf E`$ | $`4A\lambda/(L^2B)`$ |
| $`\sigma_0`$ | $`2B/(3L^2)`$ |
| $`\sigma_\pm`$ | $`4A/[g^2L^4\nu(\nu\pm1)]`$ |
| $`\Pi^{ij}`$ | $`4\lambda^2/A`$ |
| $`\psi^{3/2}`$ | $`2A`$ |
| $`\zeta_0`$ | $`4A^2/(3BL^2)`$ |
| $`\chi_\pm`$ | $`2\lambda^2\nu(\nu\mp s_g)/(A\ell^2)`$ |

The table is interpreted as physical norms in the regular real-mass region. At complex roots, the sign of the real norm is assessed from the real coupled kinetic system above, not from a complex eigenvector basis.

For the full interval $`0<\tau=6\lambda g^2<2`$, excluding $`\tau=3/2`$, one has $`B>0`$ and $`\nu>1`$. The three coefficients of the massless vector multiplet are positive. Every coefficient of the graviton and long vector multiplets has the sign of $`A`$. In particular,

```math
A=\frac{2(\nu^2-4)}{2\nu^2+1},\qquad
B=\frac{2(\nu^2-1)}{2\nu^2+1}.
```

Thus $`1<\nu<2`$, or $`3/2<\tau<2`$, gives negative norms for those two multiplets although the long representation has $`2<\Delta=1+\nu<3`$ and obeys its representation-theoretic unitarity bound. The signs of the action and the unitarity of a named representation are different conditions. At either $`A=0`$ or $`B=0`$, use the [critical action](critical_branches.md), rather than substituting into singular normal-mode coordinates.

The [paper checks](../../../computations/r2_ads5_paper_checks/README.md) reproduce the scalar congruence, fermionic norm pullbacks and vector diagonalization with symbolic parameters.

