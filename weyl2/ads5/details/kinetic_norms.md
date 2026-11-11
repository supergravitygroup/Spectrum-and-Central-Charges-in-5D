# Kinetic coefficients and stability

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="12-kinetic-coefficients-norm-signs-and-stability"></a>

## Kinetic coefficients, norm signs, and stability

<a id="121-normalization-and-scalar-check"></a>

### Normalization and scalar check

The $`\mathcal N`$ below are the physical second-/first-order kinetic coefficients of the specified field combinations; they carry the same sign information as propagator-pole residues. The numerical residue magnitude is the inverse coefficient and depends on propagator normalization. Fermion signs are compared with the healthy reference $`-\bar\Psi\mathord{\not{\nabla}}\Psi`$.

Check of the scalar derivative terms in physical variables:

```math
\begin{aligned}
(\nabla\lambda)^2
-\frac43\left[\nabla\left(\lambda-\frac{4\alpha}{3}d\right)\right]^2
&=\left[\nabla\left(\lambda_{\rm s}+\frac{16\alpha}{3}d\right)\right]^2
-\frac43[\nabla(\lambda_{\rm s}+4\alpha d)]^2\\
&=-\frac13(\nabla\lambda_{\rm s})^2
+\frac{64\alpha^2}{9}(\nabla d)^2 .
\end{aligned}
```

The cross-term coefficient is $`32\alpha/3-32\alpha/3=0`$.
Thus, in the $`-\mathcal N(\nabla\phi)^2/2`$ convention,

```math
\boxed{\mathcal N_{\lambda_{\rm s}}=\frac23,\qquad
\mathcal N_d=-\frac{128\alpha^2}{9}.}
```

This is the kinetic form of the physical coupled system; it does not define a new theory by making $`D`$ independent in the off-shell action.

<a id="122-bosonic-coefficients"></a>

### Bosonic coefficients

```math
\begin{array}{c|c}
\text{branch}&\mathcal N\\ \hline
H_0&1+\alpha g^2/2\\
H_1&-(1+\alpha g^2/2)\\
\lambda_{\rm s}&2/3\\
d&-128\alpha^2/9\\
u_0&6\\
v_0&(\alpha g^2+2)/(3g^2)\\
T&4\alpha/3\\
v'&4\alpha/3\\
Z_\sigma&-4\rho^2\,\dfrac{\rho+2\sigma}{\rho+\sigma}
\end{array}
```

For simple spin-2 poles,

```math
\frac1{O_0(O_0+\kappa)}
=\frac1\kappa\left(\frac1{O_0}-\frac1{O_0+\kappa}\right),
\qquad
\frac{\alpha\kappa}{3}=1+\frac{\alpha g^2}{2}.
```

At a vector root, the coefficient follows directly from the coupled matrix:

```math
\mathcal N_{Z_\sigma}
=2Y_\sigma^T
\left.\frac{d(tM)}{dt}\right|_{t=t_\sigma}Y_\sigma
=-4\rho^2\frac{\rho+2\sigma}{\rho+\sigma}.
```

Here $`Y_\sigma`$ is the vector direction from the [vector–form decomposition](physical_operators.md).
Since $`M(t_\sigma)Y_\sigma=0`$ at the root, the $`M`$ term in the derivative vanishes, while the $`tM'`$ contribution remains. The equality was checked symbolically for both signs.

<a id="123-fermionic-coefficients"></a>

### Fermionic coefficients

```math
\begin{array}{c|c}
\text{branch}&\mathcal N\\ \hline
\widehat\Psi_0&1+\alpha g^2/2\\
\widehat\Psi_\sigma&
\dfrac{\alpha g^2}{3}\rho(\rho+2\sigma)\\
\zeta_{\rm s}&2/3\\
X_\sigma&
-\dfrac{256\alpha^2g^2}{9}\rho(\rho+\sigma)
\end{array}
```

For example, for the spin-$`3/2`$ operator $`P_{3/2}`$, with reference sign $`\mathcal N=-P'(\mu)`$:

```math
\begin{aligned}
-P'(-3m)
&=\frac\alpha3(16m^2-\nu^2)
=\frac{\alpha\kappa}{3}=1+\frac{\alpha g^2}{2},\\
-P'((1+2\sigma\rho)m)
&=\frac\alpha3(4m+2\sigma\rho m)(4\sigma\rho m)\\
&=\frac{\alpha g^2}{3}\rho(\rho+2\sigma).
\end{aligned}
```

The norm of $`X`$ cannot be read from the $`[(\mathord{\not{\nabla}}+m)^2-\nu^2]X=0`$ equation alone; it requires the kinetic form of the $`\Psi`$–$`\zeta`$ action on the $`X`$ solution. The following calculation supplies that restriction in the displayed field normalization, with the final paper's reality convention made explicit.

<a id="paper-reality-and-x-pullback"></a>

### Paper reality convention and the $`X`$ coefficient

The final paper's Appendix A specifies

```math
\bar\zeta^i=(\zeta^i)^T\mathsf C,\qquad
\zeta^i=\mathsf B^{-1}\epsilon^{ij}(\zeta^j)^*,\qquad
\mathsf B=\mathsf C\gamma_0,
```

```math
\mathsf C^T=-\mathsf C,\quad
\gamma_a^T\mathsf C=\mathsf C\gamma_a,\quad
\mathsf C^\dagger\mathsf C=1,\quad
\mathsf B^*\mathsf B=-1.
```

The suppressed contraction is $`\bar X^iY_i`$, with NW–SE index lowering.
Majorana transpose in the component algebra does not complex-conjugate
$`i`$. The physical symplectic-Majorana condition is imposed on the paired
internal components; it is not an extra independent doubling of a mode.
The overall kinetic sign is fixed by the healthy two-derivative fermions,
as in the paper. These explicit reality data supplement the source-local
formal bar rules for this paper comparison.

Writing $`J_{\rm s}^i{}_j=\delta^{ik}\epsilon_{jk}`$ for this chapter's
real antisymmetric matrix, the paper's Hermitian internal matrix obeys

```math
J_{\rm s}=i\mathbb J_{\rm paper},\qquad
m=\frac{ig}{2\sqrt2}J_{\rm s}
=-\bar m\mathbb J_{\rm paper},\qquad
\bar m=\frac{g}{2\sqrt2}.
```

Consequently the signed masses are
$`\mu_\sigma\ell=-1/2-\sigma\rho`$ and
$`\mu'_\sigma\ell=1/2+\sigma\rho`$ for $`g>0`$.
The Majorana formal adjoint of a gamma matrix is itself, whereas that of
$`m`$ in the contracted internal bilinear is $`-m`$; integration by parts gives
$`\mathord{\not{\nabla}}^{\sharp}=-\mathord{\not{\nabla}}`$. These identities fix the
signs in the following action restriction. They do not substitute for a
global boundary-norm calculation at repeated poles.

Use the pure-$`X_\sigma`$ solution from the [physical operators](physical_operators.md):

```math
\zeta=A_\sigma X,\qquad \Psi_a=\gamma_aB_\sigma X,\qquad
A_\sigma=\frac{16\alpha g}{3}(1+\sigma\rho),\quad
B_\sigma=\frac{16\alpha m}{3}(1+\sigma\rho).
```

Hold this polarization fixed when differentiating with respect to the
Dirac eigenvalue $`z`$. The gamma-traceless curvature of $`\gamma_aX`$ is zero,
while the actual dependent spinor in the action is

```math
\mathcal X_{\rm calc}=h_\sigma(z)X,\qquad
h_\sigma(z)=\frac{B_\sigma(z-5m)+gA_\sigma}{8}.
```

Substitution into (18) and (23) of the [quadratic action](../quadratic_action.md)
gives the coefficient multiplying $`\bar XX`$:

```math
\begin{aligned}
L_{2,\sigma}(z)
={}&(12B_\sigma^2+2A_\sigma^2-32A_\sigma B_\sigma m/g)z\\
&-60B_\sigma^2m-14A_\sigma^2m+20gA_\sigma B_\sigma
=-\frac{A_\sigma^2}{2}(z+3m),\\
L_\sigma(z)
={}&-\frac{A_\sigma^2}{2}(z+3m)
-\frac{256\alpha}{3}h_\sigma(z)^2(z-m).
\end{aligned}
```

Here $`m^2=g^2/8`$ was used. At
$`z_\sigma=-(1+2\sigma\rho)m`$, the relation
$`\alpha g^2(1-\rho^2)=6`$ gives

```math
h_\sigma(z_\sigma)=1,\qquad L_\sigma(z_\sigma)=0,\qquad
-L'_\sigma(z_\sigma)
=-\frac{256\alpha^2g^2}{9}\rho(\rho+\sigma).
```

Thus the relative physical kinetic sign quoted in the paper follows from
the mixed quadratic action, with its specified symplectic-Majorana reality
and positive two-derivative reference. The [exact paper replay](../../../computations/ads5_paper_checks/README.md)
checks both signs, the adjoint identities in an explicit Clifford
representation, and the associated gravitino/vector coefficients. At a
repeated root the original coupled action and Green form replace this
simple-pole prescription.

<a id="124-longitudinal-norms-and-counting-negative-directions"></a>

### Longitudinal norms and counting negative directions

The highest-spin kinetic coefficient of a higher-spin branch alone does not determine the signs of longitudinal modes. Relative sign factors:

| Field | Polarization decomposition | Sign factors |
|---|---|---|
| Massive vector | $`3+1`$ | $`\mathcal N`$, $`\mathcal N M^2`$ |
| Massive spin 2 | $`5+3+1`$ | $`\mathcal N`$, $`\mathcal N M^2`$, $`\mathcal N M^2(M^2+3g^2/2)`$ |
| Massive gravitino | $`8+4`$ | $`\mathcal N`$, $`\mathcal N(\mu^2-9g^2/8)`$ |

Positive normalization factors are suppressed only for the sign calculation; this is not the full numerical norm matrix.

Splitting the region $`\rho>1`$ into $`1<\rho<2`$ and $`\rho>2`$ gives:

```math
\begin{array}{c|cc}
\text{negative bosonic directions}&1<\rho<2&\rho>2\\ \hline
H_0&5&0\\
H_1&4&9\\
d&1&1\\
T&6&6\\
v'&8&8\\
v_0&3&0\\
Z_+&4&4\\
Z_-&1&4\\ \hline
\text{total}&32&32
\end{array}
```

Negative bosonic directions in the region $`0<\rho<1`$

```math
6\ (H_1)+1\ (d)+2\ (v')+4\ (Z_+)+3\ (Z_-)=16
```

The corresponding fermionic count is:

```math
\begin{array}{c|c|c}
\text{region}&\text{negative spin-}3/2&\text{negative spin-}1/2\\ \hline
\rho>1,\ \rho\neq2&24&8\\
0<\rho<1&12&4
\end{array}
```

Thus, for the **generic local kinetic form with real roots**,

```math
\begin{array}{c|c}
\alpha g^2<0,\ \alpha g^2\neq-2&32_B+32_F\text{ negative directions}\\
\alpha g^2>6&16_B+16_F\text{ negative directions}
\end{array}
```

These results do not claim completion of critical global Jordan norms. For $`0<\alpha g^2<6`$, inserting complex roots into this table as independent real poles is invalid.

<a id="125-bf-check-and-physical-interpretation"></a>

### BF check and physical interpretation

For the scalar $`d`$,

```math
M_d^2\ell^2
=\left(-\frac{3g^2}{2}-\frac3\alpha\right)\frac2{g^2}
=-3-\frac6{\alpha g^2}
=\rho^2-4.
```

The AdS₅ scalar BF condition $`M^2\ell^2\ge-4`$ is:

```math
\rho^2\ge0
\quad\Longleftrightarrow\quad
\alpha g^2<0\ \ \text{or}\ \ \alpha g^2\ge6.
```

$`\lambda_{\rm s}`$ always saturates the BF bound with $`M^2\ell^2=-4`$.
At $`\alpha g^2=6`$, $`d`$ also reaches the bound.

$`\rho^2\ge0`$ does not imply positivity of all norms:
$`\mathcal N_d=-128\alpha^2/9<0`$ remains for every finite $`\alpha\neq0`$.
This calculation found no ghost-free finite-$`\alpha`$ region while retaining the full mode set.

<a id="bolum-13"></a>

