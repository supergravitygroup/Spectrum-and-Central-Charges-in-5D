# From action to spectrum: reading the calculation

This walkthrough follows the existing Gauss–Bonnet on AdS₅ calculation in physical order. Long covariant derivations remain in the linked notes, and Python functions follow the same sequence. It explains the provenance and role of the intermediate expressions. The [method record](../source_notes.md) states the scope of the component check.

## 1. Starting action

The accepted total density is

```math
\ell_{\mathrm{tot}}^{(0+2)}=
\left[\ell_{2\partial}+\lambda_{\mathrm{GB}}
(-2\ell_{W,OP}-4\ell_{\log})\right]_{\le2}.
```

Sources and normalization are in [GB01, GB16–GB20](../../action/gb_splus_action.md). `calculations/assemble_action.py` reads the three action inputs, applies exact Weyl/LOG coefficients, and preserves tensor bodies and fermion order. Its recorded output has 52 Weyl, 297 covariant LOG, and 835 explicit LOG terms. It separately records 17 Weyl terms vanishing in the source gauge and four of physical fermion degree at least four.

The outer physical degree projection includes implicit fermions in covariant derivatives and composites. Four-fermion interactions do not contribute to the fermionic Hessian on a bosonic background. The original assembly/readback commands are retained in the code; [action_readback](checks/action_readback.py) compares coefficients, phases, and tensor bodies through a separate parser.

## 2. Background and first order

The background has constant curvature and vanishing flux. This does not set form or spinor fluctuations to zero. The expansion is

```math
S=S^{(0)}+tS^{(1)}+t^2S^{(2)}+O(t^3)
```

`background.py` separately collects source background values and the coefficients of arbitrary scalar, curvature, and box terms. Tadpole conditions are read from the first variation. Derivatives of the background density give a separate reduced check. The vanishing of the other first variations is explained in [Step 3](derivations/background/STEP_03_FIRST_ORDER_INGREDIENTS.md) and the source ledger.

The selected catalogue branch is

```math
a=\lambda_{\rm GB}g^2,\quad ax^2+2x-2=0,\quad
x=\frac{2}{1+\sqrt{1+2a}},\qquad
(L_0,N_0,k)=\left(x,-\frac32gx^2,-\frac12g^2x^2\right).
```

Its background domain is $`g\ne0`$, $`a\ge-1/2`$, $`0<x\le2`$. Background and reduced coefficient expressions retain symbolic $`g,x`$. The separate component test in section 4 uses a fixed frame. The [catalogue](../background.md) preserves the other branches as source context; the spectrum runner follows the selected AdS₅ branch.

## 3. Raw bosonic quadratic action

The [source-term ledger](derivations/spectrum/SOURCE_TERM_LEDGER.md) precedes the reduction. `scalar_metric_restriction()` collects source coefficients in the intermediate expression

```math
F(L)R-\frac{\lambda}{4}\mathcal B+K(L)(\partial L)^2+V(L,N),
\qquad F=L+\frac{\lambda}{2}g^2L^2,\quad K=L^{-1}+\lambda g^2
```

and records the removed total-derivative current. This is the scalar/metric part of the complete action. Potential derivatives are taken before imposing the background branch.

For forms, `form_derivative_collection()` keeps derivative and current contributions separate. The Bianchi identity for $`G`$ is used; $`H`$ is not assumed closed. Ordered covariant derivatives are discussed in [FD1–FD17](derivations/support/part2_form_derivative_check.md).

With $`c=2-x`$, [equation (6.30)](../quadratic_action.md) records

```math
\begin{aligned}
\ell_B^{(2)}=c\bigg[&-\frac12h^{\mu\nu}\mathcal G^L_{\mu\nu}(h)
+\frac{\ell r}{x}+\frac{(\nabla\ell)^2}{x^2}
-4g^2\ell^2-\frac{8g}{x}\ell n-\frac{2n^2}{x^2}\\
&-\frac12G^2+4H^2-\frac{2p^2}{x^2}
-\frac{2\sqrt2}{x}p\cdot v-4gp\cdot A+2v'^2\bigg].
\end{aligned}
```

No fluctuation gauge fixing or auxiliary elimination has yet been made. The field strengths are derivatives of the potentials as defined in (6.19); the three-form variation remains constrained. The [recorded JSON](outputs/bosonic_quadratic.json) contains the twelve raw coefficients.

## 4. Raw fermionic quadratic action

The independent physical fermions are the gravitino and compensator spinor. Covariant derivatives of the gauge-fixed dilatino, the dependent S-connection, composite spinor, ordered Hessians, and implicit bilinears in bosonic-looking composites are retained in [FC1–FC15](../details/fermionic_reduction.md) and [SF1–SF19](derivations/support/part2_fermion_descendant_check.md).

The original component core uses explicit Clifford matrices and 48 independent fermion components. Weyl, LOG seed, explicit LOG bilinears, implicit sigma/L, and implicit N contributions are collected separately. The FC13 expression is built independently for comparison. The graded Euler operator with the AdS measure is

```math
K(s)=B(s)-B(4-s)^T
```

Here the radial variable denotes the eigenvalue of $`z\partial_z`$, and the linear Majorana bar leads to a transpose. Matrix entries have degree at most three. The original runner interpolates from four radial values and compares at a fifth in a fixed parameter frame. FC10–FC13 provide its homogeneity and covariance argument. The fixed-frame test does not by itself establish the operator identity for arbitrary branch parameters.

The [coefficient input](inputs/fermionic_coefficients.py) uses the ordered basis below.

| Python key | Bilinear |
|---|---|
| `gravitino_kinetic` | $`\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c`$ |
| `spinor_kinetic` | $`\bar\zeta\not\nabla\zeta`$ |
| `derivative_mixing_delta` | $`\delta_{ij}\bar\Psi_a^i\gamma^{ab}\nabla_b\zeta^j`$ |
| `gravitino_mass_delta` | $`\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j`$ |
| `algebraic_mixing` | $`\bar\Psi_a\gamma^a\zeta`$ |
| `spinor_mass_delta` | $`\delta_{ij}\bar\zeta^i\zeta^j`$ |

`fermionic_reduction.py` combines the two-derivative and GB contributions with the branch relation. The six FC15 coefficients are

```math
-c,\quad \frac{2c}{x^2},\quad-\frac{2\sqrt2ic}{x},\quad
-\frac{3igxc}{2\sqrt2},\quad-4gc,\quad\frac{7igc}{\sqrt2x}.
```

The gamma trace and divergence of the gravitino have not been set to zero at this stage.

## 5. Equations, constraints, and eigenfields

[Step 7](derivations/spectrum/STEP_07_LINEARIZED_EQUATIONS.md) varies the raw action. [Steps 9–10](derivations/spectrum/STEP_09_FIELD_STATUS_AND_CONSTRAINTS.md) classify fields and local gauge quotients. On $`0<x<2`$, the recorded transformations are

```math
n=-2gx\ell,\qquad
h_{\mu\nu}=H_{\mu\nu}-\frac{2}{3x}\bar g_{\mu\nu}\ell,\qquad
\Psi_a=\Upsilon_a+\frac{i\sqrt2}{3x}\gamma_aJ\zeta
```

They remove mixing and reconstruct the original equations. For the gravitino, a gamma-traceless representative is chosen by gauge, the divergence constraint follows from the equation, and residual gauge freedom is retained.

The form constraints give the local dual Maxwell description in [Step 11](../details/masses_and_eigenfields.md). Its kinetic sign follows from a first-order Legendre expression:

```math
4cY^2-8cYF_Q\quad\longrightarrow\quad-4cF_Q^2.
```

Substitution into the original unconstrained quadratic term alone is not the dualization prescription.

## 6. Spectrum and recorded checks

[spectrum.py](calculations/spectrum.py) reads masses and kinetic weights from the diagonal blocks. With $`m=gx/(2\sqrt2)`$ and $`k=-4m^2`$, the source table is:

| Mode | Local equation or mass | Kinetic weight | Real DoF |
|---|---|---|---:|
| Graviton | $`(\Box-2k)H=0`$, gauge massless | $`c`$ | 5 |
| Scalar | $`(\Box-4k)\ell=0`$, $`M^2\mathcal L^2=-4`$ | $`2c/(3x^2)`$ | 1 |
| Maxwell $`A`$ | Physical mass zero | $`2c`$ | 3 |
| Dual Maxwell $`Q`$ | Physical mass zero | $`16c`$ | 3 |
| Gravitino | $`(\not\nabla+3imJ)\Upsilon=0`$, gauge massless | $`c`$ | 8 |
| Spinor | $`(\not\nabla+imJ)\zeta=0`$ | $`2c/(3x^2)`$ | 4 |

The signed fermion parameters are $`\mu_{3/2,s}=3sm`$, $`\mu_{1/2,s}=sm`$. The two internal signs are paired by symplectic Majorana reality; they are not extra doublets. The scalar BF falloffs are two local boundary behaviors of one bulk scalar.

The source tests positivity with $`x=2t/(1+t),t>0`$ and records the two-derivative and flat limits. At $`x=2`$, all raw coefficients vanish; equations divided by $`c`$ cannot determine the endpoint spectrum.

The final local SUSY and representation stages compare the already obtained spectrum with short gravity and vector representations. Representation data are not mass inputs. See the [claims and calculation scope](CLAIMS.md).
