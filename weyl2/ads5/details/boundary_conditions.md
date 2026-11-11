# Boundary falloffs

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="14-generic-boundary-falloffs-compatible-with-susy"></a>

## Generic boundary falloffs compatible with SUSY

<a id="141-energymass-relations-and-selected-responses"></a>

### Energy–mass relations and selected responses

Denote the response weight in orthonormal components by $`\Delta`$.
Use $`M^2\ell^2=\Delta(\Delta-4)`$ for scalars and spin 2, $`M^2\ell^2=(\Delta-1)(\Delta-3)`$ for vectors, and $`M^2\ell^2=(\Delta-2)^2`$
for two-forms. A first-order fermion equation determines both $`\Delta`$
and the boundary chirality.

The SUSY-compatible response chain in the additional multiplet is selected as

```math
1+\rho,\quad \frac32+\rho,\quad 2+\rho,\quad
\frac52+\rho,\quad 3+\rho
```

For example,

```math
M_{Z_-}^2\ell^2=\rho^2-2\rho
\Longrightarrow
\Delta=1+\rho\ \ \text{or}\ \ 3-\rho.
```

The multiplet primary requires $`1+\rho`$.
The lower fermions also have energy $`3/2+\rho`$.

| Region | Falloff required for the full long multiplet |
|---|---|
| $`\alpha g^2<0`$ | Fast falloff for all additional modes |
| $`\alpha g^2>8`$ | Slow falloff for $`Z_-`$ |
| $`6<\alpha g^2<8`$ | Slow falloff for $`Z_-`$, $`\Psi_-`$, and $`X_-`$ |
| $`\alpha g^2=8`$ | Of the lower fermion's two chiralities with the same exponent, the one continuous along the SUSY chain |

Thus the earlier independent choice of fast falloff for every field does not preserve this full multiplet chain for $`\alpha g^2>6`$.

<a id="142-convergence-and-source-condition"></a>

### Convergence and source condition

For a vector coordinate component $`A_i\sim z^{\Delta-1}`$, the radial norm power is $`z^{2\Delta-3}`$; for an orthonormal fermion component it is $`z^{2\Delta-4}`$. Thus, for the lower branches,

```math
\|Z_-\|_\partial^2\sim\int_0dz\,z^{-1+2\rho},\qquad
\|X_-\|_\partial^2,\|\Psi_-\|_\partial^2
\sim\int_0dz\,z^{-1+2\rho}.
```

These integrals converge for $`\rho>0`$.
At $`\rho=0`$, this simple-pole criterion cannot replace the critical coupled action.

The entire source supermultiplet is set to zero.
The primary source-chain weight is $`1-\rho`$; source/response pairing reverses
multiplet levels. Normalizable responses of the massless graviton and
vector multiplets are retained. For the BF scalar, the source coefficient
of $`z^2\log z`$ vanishes.

For global AdS₅, central regularity and the universal cover are retained.
At the time of this record, an explicit basis of all global harmonics
and all critical global norms had not been constructed; boundary exponents
do not replace that calculation.

<a id="143-obstruction-to-a-local-reflecting-condition-in-the-bf-violating-region"></a>

### Obstruction to a local reflecting condition in the BF-violating region

For $`0<\alpha g^2<6`$, there is an exceptional family satisfying

```math
\rho=is,\quad s=\sqrt{\frac6{\alpha g^2}-1}>0,\qquad
d=z^2(Az^{is}+Bz^{-is})+\cdots .
```

Up to positive constant factors and orientation, the scalar radial flux is

```math
\omega_\partial\ \propto\
2is\,\mathcal N_d
(\delta A^\dagger\wedge\delta A
-\delta B^\dagger\wedge\delta B)
```

A local reflecting condition requires a phase relation such as $`B=e^{i\theta}A`$.
Under a dilation,

```math
z\mapsto\lambda z
\quad\Longrightarrow\quad
\frac BA\mapsto\lambda^{-2is}\frac BA,\qquad
\theta\mapsto\theta-2s\log\lambda.
```

A fixed phase is incompatible with all dilations. This establishes only
the following obstruction: for real fields with all modes retained,
a **local reflecting boundary condition with zero flux** cannot preserve
full AdS symmetry. It is not a theorem about all unexamined nonlocal
boundary theories.

<a id="bolum-15"></a>

