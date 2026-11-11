# Step 10 — Fluctuation gauges and sector maps

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

## 10.1 Diffeomorphisms and the metric–scalar map

Since $`x`$ and $`\bar N`$ are constant, the linearized diffeomorphisms are

```math
\delta_\xi h_{\mu\nu}=2\nabla_{(\mu}\xi_{\nu)},\qquad \delta_\xi\ell=0,\qquad\delta_\xi n=0.
\tag{10.1}
```

The invertible local change of variables used in Step 11 is

```math
H_{\mu\nu}=h_{\mu\nu}+\frac{2}{3x}\bar g_{\mu\nu}\ell,\qquad h_{\mu\nu}=H_{\mu\nu}-\frac{2}{3x}\bar g_{\mu\nu}\ell.
\tag{10.2}
```

It changes variables without quotienting any gauge orbit. Its determinant is nonzero for finite $`x>0`$ and it involves no inverse differential operator. Hence $`\delta H_{\mu\nu}=2\nabla_{(\mu}\xi_{\nu)}`$.

Choose de Donder gauge on $`H`$, $`F_\nu=\nabla^\mu H_{\mu\nu}-\nabla_\nu H/2=0`$. Varying it gives

```math
\delta_\xi F_\nu=\Box\xi_\nu+\nabla^\mu\nabla_\nu\xi_\mu-\nabla_\nu\nabla^\mu\xi_\mu=(\Box+4k)\xi_\nu.
\tag{10.3}
```

Thus residual gauge parameters solve $`(\Box+4k)\xi_\nu=0`$. For local radiative graviton modes, the trace can subsequently be removed using the corresponding residual solution. The final transverse-traceless representative has $`\nabla^\mu H_{\mu\nu}=0`$, $`H=0`$; global zero modes are not discarded by this local statement. At $`c=0`$ the absence of the metric equation prevents carrying over the generic constraint count.

## 10.2 Form gauge freedom at linear order

At zero background potentials, $`G_1=dA`$ and $`H_{3,1}=d b+g e_3/2`$. Their linear gauge transformations include

```math
\delta A=d\alpha,\qquad \delta e_3=d\Lambda_2,\qquad \delta b=d\Lambda_1-\frac g2\Lambda_2.
\tag{10.4}
```

Therefore $`\delta H_{3,1}=d^2\Lambda_1-gd\Lambda_2/2+gd\Lambda_2/2=0`$. This is a gauge identity, not an equation setting $`H_{3,1}`$ to zero. The redundancies of the parameters follow from $`d^2=0`$. No Lorenz gauge, form dualization or elimination has yet been used in the raw form block.

## 10.3 Fermionic gauge map

The accepted source gauge requires compensating S transformations. On the selected AdS₅ branch the kinematic background check in [the explanation](../support/gb-splus-spectrum-method-EXPLAIN.md) gives $`\delta\zeta=0`$ on the background and a Killing operator $`\nabla_\mu+igx\gamma_\mu J/(2\sqrt2)`$, with $`J(\epsilon^1,\epsilon^2)=(-\epsilon^2,\epsilon^1)`$ and $`J^2=-1`$. Its integrability yields (6.2).

The corresponding off-shell quadratic Noether identity and the gamma-trace/divergence reduction are established in §10.5. They use the independently derived fermionic Hessian.

## 10.4 Solving the local form gauges

For $`c>0`$ the equation $`p=0`$ makes $`e_3`$ closed. Locally choose $`\Lambda_2`$ with $`e_3=d\Lambda_2`$ and apply the transformation parameter $`-\Lambda_2`$ in (10.4). The resulting variables have $`e_3=0`$ and $`H_3=db`$, where the simultaneously shifted $`b`$ carries the same original $`H_3`$. Residual parameters obey $`d\Lambda_2=0`$, together with the ordinary $`b\mapsto b+d\Lambda_1`$ gauge and its gauge-for-gauge $`\Lambda_1\mapsto\Lambda_1+d\omega`$.

The local form equation $`dH=0`$ permits $`H=dQ`$ for a dual one-form $`Q`$. This introduces the redundancy $`Q\mapsto Q+d\beta`$. It is a map of solutions, not a substitution into the action for the purpose of computing norms. The curl equation then gives

```math
G=dA,\qquad H=dQ,\qquad v=\sqrt2gx(2Q-A)+du,\qquad e_3=0,\qquad v'=0.
\tag{10.5}
```

The gradient $`du`$ belongs to the residual trace-connection gauge. The scalar $`u`$ has no propagating equation or norm. In terms of two-form variables, $`db=2*dQ`$ because $`H=-*H_3/2`$ and $`*^2=-1`$ on two- and three-forms in signature $`-++++`$.

One can choose $`\nabla\cdot A=\nabla\cdot Q=0`$ locally. Their residual parameters solve $`\Box\alpha=\Box\beta=0`$. Gauge zero modes and global harmonic potentials remain outside the local radiative quotient; no inverse $`\Box`$ is used to erase them.

## 10.5 Fermionic Noether identity, constraints and residual gauge

Use the algebraic field map of Step 11, $`\Psi_a=\Upsilon_a+\beta\gamma_aJ\zeta`$, with $`\beta=i\sqrt2/(3x)`$. Since the background transformation of $`\zeta`$ vanishes, the local transformations and the unconstrained gravitino equation are

```math
\delta\Upsilon_a=\widehat\nabla_a\epsilon=(\nabla_a+im\gamma_aJ)\epsilon,\qquad\delta\zeta=0,\qquad E_\Upsilon^a=\gamma^{abc}\nabla_b\Upsilon_c-3im\gamma^{ab}J\Upsilon_b.
\tag{10.6}
```

Write $`\theta_\Upsilon=\gamma^a\Upsilon_a`$, $`\sigma_\Upsilon=\nabla^a\Upsilon_a`$. The identities $`\gamma_a\gamma^{abc}=3\gamma^{bc}`$ and $`\gamma_a\gamma^{ab}=4\gamma^b`$ give

```math
\gamma_aE_\Upsilon^a=3(\not\nabla\theta_\Upsilon-\sigma_\Upsilon)-12imJ\theta_\Upsilon.
\tag{10.7}
```

For the divergence, the antisymmetry in $`a,b`$ replaces two derivatives by a commutator. Its vector-curvature part vanishes after contraction with $`\gamma^{abc}`$, while the spin-curvature part is $`k\gamma^{abc}\gamma_{ab}\Upsilon_c/4=-3k\theta_\Upsilon`$. Consequently

```math
\nabla_aE_\Upsilon^a=-3k\theta_\Upsilon-3imJ(\not\nabla\theta_\Upsilon-\sigma_\Upsilon),\qquad \nabla_aE_\Upsilon^a+imJ\gamma_aE_\Upsilon^a=(-3k-12m^2)\theta_\Upsilon=0.
\tag{10.8--10.9}
```

This is the quadratic Noether identity on $`k=-4m^2`$, before imposing any equation. Direct substitution of $`\widehat\nabla\epsilon`$ into $`E_\Upsilon`$ gives the same zero: the derivative terms $`+3im\gamma^{ab}J\nabla_b\epsilon`$ and $`-3im\gamma^{ab}J\nabla_b\epsilon`$ cancel, and the remaining coefficient is $`-3k-12m^2`$.

The gamma trace transforms as $`\delta\theta_\Upsilon=(\not\nabla+5imJ)\epsilon`$. On a local patch solve this first-order gauge equation to set $`\theta_\Upsilon=0`$. Then (10.7) gives $`\sigma_\Upsilon=0`$ from the equation of motion. Thus the divergence is a constraint, not a second gauge condition. Residual parameters obey

```math
(\not\nabla+5imJ)\epsilon=0,\qquad \delta\sigma_\Upsilon=\Box\epsilon+imJ\not\nabla\epsilon=0.
\tag{10.10}
```

To check the second equality with the source curvature sign, $`\not\nabla^2=\Box+\gamma^{ab}R_{ab}{}^{cd}\gamma_{cd}/8=\Box-5k`$. The residual equation gives $`\not\nabla^2\epsilon=25m^2\epsilon`$, hence $`\Box\epsilon=(25m^2+5k)\epsilon=5m^2\epsilon`$; the remaining term is $`-5m^2\epsilon`$. Zero modes of the residual operator are retained as gauge transformations. A global obstruction to this gauge choice would belong to an additional boundary/topology problem.
