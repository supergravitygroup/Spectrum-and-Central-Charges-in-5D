# Norms, stability and boundary dependence

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="12-norms-stability-degrees-of-freedom-and-boundary-dependence"></a>

## Norms, stability, degrees of freedom, and boundary dependence

The norm discussion gives algebraic residues and the paper's relative physical kinetic signs. The latter use the symplectic-Majorana reality convention and positive two-derivative reference through the [Weyl norm pullback](../../../weyl2/ads5/details/kinetic_norms.md#paper-reality-and-x-pullback) and the LOG quadratic-action correspondence. Global BF/log boundary conditions are a separate choice.

Throughout this chapter retain

```math
L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
\ell^{-2}=\frac{g^2L_0^2}{2},\qquad
\alpha g^2L_0^2=8(L_0-1)
\tag{N-1}
```

and define

```math
B_0:=4-3L_0,\qquad
\Delta:=\sqrt{\frac{2(4-L_0)}{L_0-1}}
\tag{N-2}
```

In the positive-coupling region,

```math
0<\alpha g^2\le2
\quad\Longleftrightarrow\quad
1<L_0\le2,\qquad \Delta\ge2.
```

For a physical channel with

```math
S^{(2)}=\frac12\langle X,K(\mathcal O)X\rangle,\qquad
K(\lambda)v_\lambda=0
```

the simple-pole kinetic coefficient and residue are

```math
\boxed{
Z_\lambda=v_\lambda^\dagger K'(\lambda)v_\lambda,\qquad
\mathcal R_\lambda=
\frac{v_\lambda v_\lambda^\dagger}{Z_\lambda}
}
\tag{N-3}
```

The fermionic algebra below uses the formal Majorana adjoint. Physical kinetic signs use the paper's reality convention through the norm pullback cited above. Tables omit the common prefactor $`1/(2\kappa_5^2)`$.

## Bosonic residues

The TT metric operator is

```math
K_2(x)=-\frac{\alpha}{12}x(x-\mu),
\qquad
\mu=\frac{6B_0}{\alpha}
```

so

```math
K_2'(0)=\frac{B_0}{2},\qquad
K_2'(\mu)=-\frac{B_0}{2}.
```

and consequently

```math
\boxed{
Z_{h_0}=\frac{4-3L_0}{2},\qquad
Z_{h_M}=-\frac{4-3L_0}{2}
}
\tag{N-4}
```

with residues

```math
K_2(x)^{-1}
=\frac{2}{4-3L_0}
\left(\frac1x-\frac1{x-\mu}\right).
\tag{N-5}
```

The two simple spin-two poles have opposite residues.

Scalar norms cannot be read from the explicit $`l`$ kinetic term alone. In the conformal metric representative $`h_{\mu\nu}=\bar g_{\mu\nu}f`$, the eigenvectors are

```math
v_0=
\begin{pmatrix}
4/(3L_0^2)\\-2/L_0\\4g
\end{pmatrix},
\qquad
v_M=
\begin{pmatrix}
-1/L_0^2\\2/L_0\\-3g
\end{pmatrix},
\qquad
\begin{pmatrix}f\\l\\n\end{pmatrix}
=v_0\phi_0+v_M\phi_M
\tag{N-6}
```

as displayed.

```math
A=1-\frac{\alpha g^2L_0}{6},\qquad
b=\frac{\alpha g}{6},\qquad
Z_L=\frac1{L_0}-\frac{\alpha g^2}{4}
```

With the stated definitions, contraction with the derivative of the full scalar Hessian gives

```math
v^TK_S'(x)v=
\left(-\frac{2\alpha x}{3}-6B_0-\frac{\alpha k}{3}\right)f^2
-8Afl-8bfn-2Z_Ll^2
\tag{N-7}
```

Evaluating at $`v_0,x=4k`$ and $`v_M,x=\mu`$ yields

```math
\boxed{
Z_{\phi_0}=\frac{8(2-L_0)}{3L_0^4},\qquad
Z_{\phi_M}=-\frac{2(2-L_0)}{L_0^4}.
}
\tag{N-8}
```

For $`L_0<2`$, $`\phi_0`$ has positive and $`\phi_M`$ negative kinetic coefficient. The zero diagonal $`n^2`$ coefficient at $`L_0=2/5`$ does not alter this result.

For the Maxwell channels use the basis

```math
\mathcal A_0:=c_0+\frac{\sqrt2}{3gL_0}v_0,\qquad
\mathcal B_0:=v_0
\tag{N-9}
```

to obtain

```math
\ell_{0,V}^{(2)}
=-\frac14Z_{\mathcal A_0}(d\mathcal A_0)^2
-\frac14Z_{\mathcal B_0}(d\mathcal B_0)^2,
```

```math
\boxed{
Z_{\mathcal A_0}=6(2-L_0),\qquad
Z_{\mathcal B_0}=
\frac{2(4-3L_0)}{3g^2L_0^2}.
}
\tag{N-10}
```

Normalize a massive-vector eigenvector as

```math
v_\lambda=
\begin{pmatrix}
C_\lambda/A_\lambda\\ V_\lambda/A_\lambda\\1
\end{pmatrix},
\qquad
C_\lambda=4(4-L_0)+2\alpha\lambda,\quad
A_\lambda=2(5L_0-8)+\alpha\lambda
```

with last component $`a_\lambda`$. The action Hessian is $`-4xK_V(x)`$, so

```math
\begin{aligned}
Z_{a_\lambda}
&=-4\lambda\,v_\lambda^TK_V'(\lambda)v_\lambda\\
&=-4\lambda\left[
\frac{\alpha}{12}\left(\frac{C_\lambda}{A_\lambda}\right)^2
-\frac{\alpha}{3}\frac{C_\lambda}{A_\lambda}
-\frac2{g^2}\left(-\frac2{L_0}+\frac{\alpha g^2}{3}\right)
\right].
\end{aligned}
\tag{N-11}
```

Substituting the roots and branch relation gives

```math
\boxed{
\begin{aligned}
Z_{a_+}&=-\frac{4(4-L_0)}3(\Delta-2)(\Delta+4),\\
Z_{a_-}&=-\frac{4(4-L_0)}3(\Delta+2)(\Delta-4).
\end{aligned}}
\tag{N-12}
```

In the previous $`p_\pm`$ normalization,

```math
a_\pm=-\frac{g}{2\lambda_\pm}p_\pm
\quad\Longrightarrow\quad
Z_{p_\pm}=\frac{g^2}{4\lambda_\pm^2}Z_{a_\pm}.
\tag{N-13}
```

For real nonzero roots the transformation preserves the sign.

For the traceless internal vectors, the kinetic term is

```math
\frac{\alpha}{6}(dw^{ij})^2
=-\frac14\left(-\frac{2\alpha}{3}\right)(dw^{ij})^2
```

with coefficient

```math
\boxed{Z_w=-\frac{2\alpha}{3}}
\tag{N-14}
```

multiplying the stated internal contraction.

For the closed-form sector,

```math
\ell_{H_c}^{(2)}
=a_HH_c^2-\frac{\alpha}{6}(\mathrm{div}\,H_c)^2,\qquad
a_H=\frac{L_0-4}{9}.
```

introduce $`q=\mathrm{div}\,H_c`$ in the equivalent first-order quadratic form

```math
\ell_1=a_HH_c^2+\frac{\alpha}{6}q^2
-\frac{\alpha}{3}q\cdot\mathrm{div}\,H_c
```

Integration by parts and completion of the square give

```math
\ell_1\simeq_\partial
a_H\left(H_c+\frac{\alpha}{18a_H}dq\right)^2
-\frac{\alpha^2}{324a_H}(dq)^2+\frac{\alpha}{6}q^2
\tag{N-15}
```

Thus the physical form channel has

```math
H_c=\frac1{m_H^2}dq,\qquad
m_H^2=\frac{2(4-L_0)}{\alpha},\qquad \mathrm{div}\,q=0
```

and

```math
\ell_q^{(2)}
=-\frac{Z_q}{12}(dq)^2-\frac{Z_qm_H^2}{4}q^2,
\qquad
\boxed{Z_q=-\frac{\alpha^2}{3(4-L_0)}<0.}
\tag{N-16}
```

This is a quadratic rewriting for the norm calculation, not elimination of independent fields from the full off-shell action.

## Polarization signs and bosonic inertia

For the two generic positive-coupling intervals, the coefficient signs are listed below.

| Channel | $`0<\alpha g^2<3/2`$, $`\Delta>4`$ | $`3/2<\alpha g^2<2`$, $`2<\Delta<4`$ |
|---|---:|---:|
| $`h_0`$ | $`+`$ | $`-`$ |
| $`h_M`$, highest-spin component | $`-`$ | $`+`$ |
| $`\phi_0`$ | $`+`$ | $`+`$ |
| $`\phi_M`$ | $`-`$ | $`-`$ |
| $`\mathcal A_0`$ | $`+`$ | $`+`$ |
| $`\mathcal B_0`$ | $`+`$ | $`-`$ |
| $`a_+`$ | $`-`$ | $`-`$ |
| $`a_-`$, transverse components | $`-`$ | $`+`$ |
| $`w^{ij}`$ | $`-`$ | $`-`$ |
| $`H_c`$, $`q`$ representative | $`-`$ | $`-`$ |

Positive highest-spin coefficients for $`h_M,a_-`$ in the second interval do not imply positive norms for every polarization.

Substitute $`A_\mu=B_\mu+\nabla_\mu\pi`$ in the Proca action:

```math
-\frac Z4F^2-\frac{Zm^2}{2}A^2
\supset-\frac{Zm^2}{2}(\nabla\pi)^2
\tag{N-17}
```

The longitudinal sign is $`Zm^2`$. Here

```math
-1<m_{a_-}^2\ell^2
=\frac{\Delta^2}{4}-\Delta<0
```

so $`a_-`$ has three positive transverse polarizations and one negative longitudinal polarization.

For Fierz–Pauli spin two write

```math
h_{\mu\nu}=\widetilde h_{\mu\nu}
+\nabla_\mu\nabla_\nu\pi+f\,g_{\mu\nu}
```

The scalar derivative terms are

```math
-6Zf\Box f+4Zm^2f\Box\pi-2Zm^2k\,\pi\Box\pi
```

The shift $`f=F+m^2\pi/3`$ gives

```math
\ell_{\pi,\mathrm{kin}}
=\frac{2Z}{3}m^2(m^2-3k)\,\pi\Box\pi
\tag{N-18}
```

The vector Stückelberg sign is $`Zm^2`$. Hence in

```math
3k<m_{h_M}^2<0
```

three vector and one scalar polarizations are negative despite a positive highest-spin coefficient.

For real fast-falling modes the bosonic inertia in both generic positive-coupling intervals is

```math
\boxed{(N_B^+,N_B^-)=(12,32)}
\tag{N-19}
```

Negative-norm modes remain included in the count.

## Formal fermionic residues

Define

```math
D=\gamma^a\bar\nabla_a,\qquad t=igM,\qquad
t^2=\ell^{-2},\qquad z=t^{-1}D
```

The spin-three-halves Euler polynomial is

```math
P_{3/2}(D)=
(D+3t/2)\left[\frac{\alpha}{3}(D^2-tD)+L_0-3\right]
\tag{N-20}
```

and its formal kinetic coefficients are

```math
\boxed{
\begin{aligned}
N_{\Psi_0}&=-2(4-3L_0),\\
N_{\Psi_+}&=\frac{2(L_0-1)}3\Delta(\Delta+4),\\
N_{\Psi_-}&=\frac{2(L_0-1)}3\Delta(\Delta-4).
\end{aligned}}
\tag{N-21}
```

The projected algebraic residue at each simple pole is $`1/N_\Psi`$.

For the mixed spin-half sector use

```math
u=\rho-\chi,\qquad
\zeta=\frac tg(4\rho-3\chi),\qquad
P(z)=4(L_0-1)(z^2+z)+3L_0-9
```

The Hessian with the supplied formal Majorana adjoint is

```math
\mathbb K_{\chi\rho}
=\frac t3
\begin{pmatrix}
-(2z+1)\bigl[8(L_0-1)z^2+7L_0-16\bigr]
&2(2z+1)P(z)\\
2(2z+1)P(z)&-2(2z+3)P(z)
\end{pmatrix}.
\tag{N-22}
```

Differentiate first and evaluate at the root afterward:

```math
\boxed{
\begin{aligned}
N_\chi&=6(2-L_0),\\
N_{\rho_+}&=-\frac{8(L_0-1)}3\Delta(\Delta+2),\\
N_{\rho_-}&=-\frac{8(L_0-1)}3\Delta(\Delta-2).
\end{aligned}}
\tag{N-23}
```

These inverse residues retain all gravitino–spinor mixing.

These formal inverse residues do not alone define Hermitian conjugation: $`\sharp`$ is not identified with $`\dagger`$. The paper's relative physical kinetic signs follow after applying its symplectic-Majorana reality convention and the positive two-derivative reference, as in the [mixed-action norm pullback](../../../weyl2/ads5/details/kinetic_norms.md#paper-reality-and-x-pullback).

A necessary representation-theoretic positivity condition can still be checked. For the Rarita–Schwinger operator

```math
\mathscr R_a(\Psi)
=\gamma_{abc}\nabla^b\Psi^c+m_D\gamma_{ab}\Psi^b
```

one has

```math
\mathscr R_a\!\left[
\left(\nabla_b-\frac{m_D}{3}\gamma_b\right)\epsilon
\right]
=-\frac43\left(m_D^2+\frac94k\right)\gamma_a\epsilon.
\tag{N-24}
```

The derivative terms cancel by $`3(-m_D/3)+m_D=0`$; curvature contributes $`-3k\gamma_a\epsilon`$. Gauge masslessness occurs at $`m_D^2\ell^2=9/4`$.

For $`\Psi_-`$,

```math
|m_D|\ell=\frac{\Delta-1}{2}.
```

Thus $`2<\Delta<4`$ lies below the spin-three-halves unitary bound. An overall sign cannot repair relative lower-polarization signs. The gauge zero was directly checked above; related higher-spin gauge limits are discussed by [Deser–Waldron](https://arxiv.org/abs/hep-th/0103198).

## BF stability

The sign of a mass alone is insufficient. Near the boundary the reduced radial operator has form

```math
\mathcal A_\nu=-\partial_z^2+
\frac{\nu^2-\tfrac14}{z^2}+\text{regular terms}
\tag{N-25}
```

The BF condition is $`\nu^2\ge0`$. Substitution of the masses gives the table below.

| Channel | BF expression $`\nu^2`$ | Result for $`\alpha>0`$ |
|---|---:|---|
| $`\phi_0`$ | $`4+m^2\ell^2=0`$ | At the BF bound |
| $`\phi_M`$ | $`4+m^2\ell^2=\Delta^2/4`$ | Above the BF bound |
| $`h_M`$ | $`4+m^2\ell^2=\Delta^2/4`$ | Above the BF bound |
| $`w^{ij}`$ | $`1+m^2\ell^2=\Delta^2/4`$ | Above the BF bound |
| $`H_c`$, $`q`$ representative | $`m_H^2\ell^2=\Delta^2/4`$ | Above the BF bound |
| $`a_+`$ | $`1+m^2\ell^2=(\Delta+2)^2/4`$ | Above the BF bound |
| $`a_-`$ | $`1+m^2\ell^2=(\Delta-2)^2/4`$ | Above the BF bound; $`L_0=2`$gives equality |

At positive coupling, simple roots with standard fast falloff can therefore have real frequencies while negative norms remain.

At negative coupling,

```math
\alpha<0\Longrightarrow 0<L_0<1
\Longrightarrow \Delta^2<0.
```

and in particular

```math
\boxed{m_{\phi_M}^2\ell^2=\frac{\Delta^2}{4}-4<-4}
\tag{N-26}
```

violates the BF bound. This is not merely a norm-sign issue: the inverse-square radial potential lies below the critical coefficient in Hardy's inequality,

```math
\int|f'|^2\,dz\ge\frac14\int\frac{|f|^2}{z^2}\,dz
```

and localized test-function rescaling makes its negative spectrum unbounded below. Retaining the full $`\phi_M`$ sector precludes a positive-energy reflecting extension. The operator approach is described by [Ishibashi–Wald](https://arxiv.org/abs/hep-th/0402184).

## Critical norms and endpoint residues

At $`\alpha g^2=3/2,L_0=4/3`$, simple-pole formulas fail. For example,

```math
K_2(x)=-\frac{\alpha}{12}x^2,\qquad
K_2(x)^{-1}=-\frac{12}{\alpha x^2}.
\tag{N-27}
```

For a chain $`xX_1=X_0,xX_0=0`$, the conserved pairing has form

```math
G_{\rm chain}=
\begin{pmatrix}
0&b\\ b^*&c
\end{pmatrix},
\qquad
\det G_{\rm chain}=-|b|^2<0
\tag{N-28}
```

An ordinary solution with zero self-pairing is not gauge: it pairs nontrivially with its generalized partner.

Per unit second-order pairing the metric-chain coefficient is

```math
b_h=\frac12K_2''(0)=-\frac{\alpha}{12}\ne0.
\tag{N-29}
```

In the vector-chain normalization

```math
n_0=(-4,8\sqrt2g,1)^T,\qquad
n_1=(0,0,-27/(32g^2))^T
```

the coefficient is

```math
(n_0+xn_1)^T[-4xK_V(x)](n_0+xn_1)
=-\frac{24}{g^2}x^2+O(x^3),
```

```math
b_V=-\frac{24}{g^2}\ne0.
\tag{N-30}
```

Both bosonic chains are indefinite. The formal gravitino cross coefficient is

```math
b_{\Psi}=\frac12P_{3/2}''(-3t/2)
=-\frac{4\alpha t}{3}\ne0
\tag{N-31}
```

This pairing structure is also discussed by [Porrati–Roberts](https://arxiv.org/abs/1104.0674); the coefficients here belong to the present action.

Retaining a chain allows time dependence

```math
X_1(t)\sim e^{-i\omega t}\bigl(X_1(0)+t\,X_0(0)\bigr)
\tag{N-32}
```

so real $`\omega`$ does not imply bounded time evolution at the critical point.

At $`\alpha g^2=2,L_0=2`$, quotienting the additional gauge directions gives the bosonic coefficients below.

| Channel | Kinetic coefficient | Physical norm content |
|---|---:|---|
| Massless graviton | $`-1`$ | $`5`$ negative |
| Partially massless graviton | $`+1`$ | $`5`$ positive, $`3`$ negative |
| Two $`w^{ij}`$ Maxwell channels | $`-4/(3g^2)`$ | $`6`$ negative |
| Mixed Maxwell $`v_0`$ | $`-1/(3g^2)`$ | $`3`$ negative |
| $`p'`$, $`m^2=-2g^2`$ | $`+1/(3g^2)`$ | $`3`$ positive, $`1`$ negative |
| $`q=\mathrm{div}\,H'_c`$ | $`-2/(3g^4)`$ | $`6`$ negative |

Their inertia is

```math
\boxed{(N_B^+,N_B^-)=(8,24)\qquad(\alpha g^2=2).}
\tag{N-33}
```

The formal fermionic coefficients at the same endpoint are

```math
N_{\Psi_{-3/2}}=4,\qquad
N_{\Psi_{+3/2}}=8,\qquad
N_{\Psi_{-1/2}}=-\frac83,\qquad
N_\eta=\frac83
\tag{N-34}
```

The generic $`\chi,\rho_\pm`$ residues cannot be imported there as independent channels.

## Boundary admissibility

For $`z=\cos\rho\to0`$, use boundary-tangent orthonormal components:

```math
X=z^{2-\nu}a+z^{2+\nu}b+\cdots
\tag{N-35}
```

Up to the channel normalization, bosonic flux is

```math
\mathcal F_{\partial}
=2\nu Z\int_{\partial M}
(\delta_1a\,\delta_2b-\delta_2a\,\delta_1b)
\tag{N-36}
```

Different prescriptions include

```math
\delta a=0,
\qquad\text{or in the appropriate range}\qquad
b=\mathcal F a,\quad \mathcal F^\dagger=\mathcal F.
\tag{N-37}
```

Both can have zero flux. The Robin choice requires a separate stability test.

The fast branches at positive coupling are listed below.

| Channel | $`\nu`$ or $`\lvert m_D\rvert\ell`$ | Fast orthonormal falloff |
|---|---:|---|
| $`h_0`$ | $`2`$ | $`z^4`$ |
| Maxwell channels | $`1`$ | $`z^3`$ |
| $`h_M,\phi_M,w,H_c`$ | $`\Delta/2`$ | $`z^{2+\Delta/2}`$ |
| $`a_+`$ | $`(\Delta+2)/2`$ | $`z^{3+\Delta/2}`$ |
| $`a_-`$ | $`(\Delta-2)/2`$ | $`z^{1+\Delta/2}`$ |
| $`\chi`$ | $`1/2`$ | $`z^{5/2}`$ |
| $`\Psi_0`$ | $`3/2`$ | $`z^{7/2}`$ |
| $`\Psi_+,\rho_-`$ | $`(\Delta+1)/2`$ | $`z^{(5+\Delta)/2}`$ |
| $`\Psi_-,\rho_+`$ | $`(\Delta-1)/2`$ | $`z^{(3+\Delta)/2}`$ |

The form row uses the equivalent $`q`$ representative. First-order fermion equations additionally fix radial spinor projections.

The bosonic bulk norm behaves as

```math
\int_0 dz\,z^{-3}|X|^2
```

so the slow branch is additionally normalizable only for $`0\le\nu<1`$. In the generic positive-coupling region this occurs for

the BF-saturated $`\phi_0`$ and, for $`3/2<\alpha g^2<2`$, the vector $`a_-`$.

At the endpoint $`p'`$ also saturates the BF bound.

The fermionic bulk measure gives

```math
\int_0 dz\,z^{-4}|X|^2
```

Additional slow-branch admissibility requires $`|m_D|\ell<1/2`$. None of the present positive-coupling roots lies in this open window. See [Amsel–Marolf](https://arxiv.org/abs/0808.2184); no positive Hermitian completion is assumed here.

At the BF point the two branches merge as

```math
\phi_0=z^2(a_{\log}\log z+b)+\cdots
```

and their flux is

```math
\mathcal F_{\partial}
\propto Z_{\phi_0}
(\delta_1b\,\delta_2a_{\log}
-\delta_2b\,\delta_1a_{\log}).
\tag{N-38}
```

Thus “fixed sources” alone does not specify a BF mode until the source combination is identified.

The stability dependence is explicit. A center-regular BF solution with scalar harmonic index $`j`$ on $`S^3`$ is

```math
\phi=(\sin\rho)^j(\cos\rho)^2
\,{}_2F_1\!\left(
\frac{j+2-\omega\ell}{2},
\frac{j+2+\omega\ell}{2};
j+2;\sin^2\rho
\right)
\tag{N-39}
```

Its boundary expansion is

```math
\frac{b}{a_{\log}}
=\frac12\left[
\psi\!\left(\frac{j+2-\omega\ell}{2}\right)
+\psi\!\left(\frac{j+2+\omega\ell}{2}\right)
-2\psi(1)
\right].
\tag{N-40}
```

If $`a_{\log}=0`$, the frequencies obey

```math
  \omega\ell=j+2+2n,\qquad n=0,1,\ldots
```

and are real. For Robin data $`b=f a_{\log}`$, set $`j=0`$ and seek an imaginary frequency $`\omega\ell=i\gamma`$:

```math
  f=\mathop{\mathrm{Re}}\nolimits\psi(1+i\gamma/2)-\psi(1)
  =\sum_{n=1}^{\infty}
  \frac{(\gamma/2)^2}{n[n^2+(\gamma/2)^2]}.
  \tag{N-41}
```

For symbolic $`\gamma>0`$ the right-hand side is positive and unbounded. In this boundary basis, $`f>0`$ therefore admits a growing mode; this is a solved frequency condition, not a numerical parameter sample.

Reflectivity alone consequently does not fix stability.

At $`L_0=4/3`$ the fast logarithmic responses

```math
h_{\log}\sim z^4\log z,\qquad
A_{\log}\sim z^3\log z,\qquad
\Psi_{\log}\sim z^{7/2}\log z
\tag{N-42}
```

satisfy bulk normalizability. Fixing slow sources does not automatically remove them. An additional exclusion would shorten the chains, but was not selected in the supplied boundary data.

## Degrees of freedom and scope

Local degrees of freedom are counted independently of norm signs:

```math
n_{2,\mathrm{massless}}=\frac{5(5-3)}2=5,\qquad
n_{2,\mathrm{massive}}=15-5-1=9,
```

```math
n_{1,\mathrm{massless}}=3,\qquad
n_{1,\mathrm{massive}}=4,\qquad
n_{H_c}=\binom42=6,
```

```math
n_{3/2,\mathrm{massless}}=3\cdot4-4=8,\qquad
n_{3/2,\mathrm{massive}}=4\cdot4-4=12,\qquad
n_{1/2}=4.
\tag{N-43}
```

The totals are

```math
\boxed{
N_B=N_F=44\quad(L_0\ne2),\qquad
N_B=N_F=32\quad(L_0=2).
}
\tag{N-44}
```

At the critical merger the ordinary zero-self-norm solutions cannot be removed as gauge because of their nonzero cross-pairing. With chains retained the count is $`44+44`$.

The local theory contains negative kinetic channels; negative coupling also violates the BF bound. Positive-coupling fast simple-root modes satisfy BF conditions while ghost channels remain. The relative fermion kinetic signs use the reality convention specified in the paper. A global BF/log/Robin acceptance set requires boundary data beyond this local kinetic analysis.

