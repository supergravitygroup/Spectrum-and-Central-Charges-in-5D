# Quadratic action checks

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="8-scope-of-the-independent-check"></a>

## Scope of the independent check

<a id="81-first-variation-and-background-equations"></a>

### First variation and background equations

The [quadratic expansion](../quadratic_action.md) gives

```math
\bar e^{-1}\mathcal L^{(1)}
=r_1-2g^2h-2\Box\lambda
=\nabla_\mu(\nabla_\nu h^{\mu\nu}-\nabla^\mu h-2\nabla^\mu\lambda)
```

The bulk first variation vanishes; the boundary integral requires specified boundary conditions.

<a id="82-comparison-of-scalar-equations-by-two-routes"></a>

### Comparison of scalar equations by two routes

Since $`D_0=0`$, linearizing the Weyl contribution gives

```math
\delta\left(\frac{128\alpha}{3}D\,\frac{\partial D}{\partial N}\right)_0
=\frac{32\alpha g}{3}d,\qquad
\delta\left(\frac{128\alpha}{3}D\,\frac{\partial D}{\partial L}\right)_0
=\frac{16\alpha g^2}{3}d
```

Together with direct derivatives of the two-derivative algebraic part and the scalar kinetic term,

```math
\begin{aligned}
\delta\mathcal E_N&=-4n-8g\lambda+\frac{32\alpha g}{3}d,\\
\delta\mathcal E_L&=r_1-2\Box\lambda-8g^2\lambda-8gn
+\frac{16\alpha g^2}{3}d .
\end{aligned}
```

Variation of $`-2n^2-8g\lambda n-4g^2\lambda^2 +(\nabla\lambda)^2+\lambda r_1+64\alpha d^2/3`$ in the quadratic action gives the same coefficients. Here $`\partial_nd=g/4`$ and $`\partial_\lambda d=g^2/8`$ are used.

This does not derive the scalar kinetic term from a function restricted to the constant background; $`-2\Box\lambda`$ comes from varying the full kinetic term.

<a id="83-correct-meaning-of-the-hessian-identity"></a>

### Correct meaning of the Hessian identity

```math
\frac{\delta S^{(2)}}{\delta\phi^I}
=\left.\frac{d}{d\varepsilon}
\mathcal E_I[\bar\Phi+\varepsilon\phi]\right|_{\varepsilon=0}.
```

This necessary identity does not make writing the same Hessian twice an independent check. Full verification requires an actual comparison of composite/connection variations from the full action with the quadratic-action coefficients.

The calculation checks the first variation, scalar/TT blocks, coupled form operators, fermionic trace equations, and linearized gauge identities through the displayed equations.

<a id="84-consequence-of-the-derivative-correction"></a>

### Consequence of the derivative correction

The correct Lorentz derivative of $`T`$ allows $`\nabla\gamma=0`$, integration by parts, and curvature commutators to be used consistently. The dependent $`f`$ contribution in $`\mathcal D\mathcal D T`$ is retained. The physical operators below use the corrected definition.

<a id="bolum-9"></a>

