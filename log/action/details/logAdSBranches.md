# AdS₅ background branches of the total two-derivative + LOG theory

<a id="1-action-normalization-and-scope"></a>

## Action, normalization, and scope

The only higher-derivative coupling is $`\alpha`$ in the fixed total action:

```math
\boxed{
S=S_{2\partial}+\alpha S_{\log}
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2\partial}+\alpha\ell_{\log}\bigr),
\qquad \alpha\ne0,\quad g\ne0.
}
\tag{AD1}
```

The LOG coupling in this derivation is $`\alpha`$. In the expanded bosonic density, the pure $`R^2`$ term has coefficient $`\alpha/24`$; the total LOG invariant is multiplied by $`\alpha`$.

The action input is action.md, the independent-field inventory is [indep_fields.md](independent_fields.md), and the convention authority is [CONVENTIONS.md](../../../common/details/source_conventions.md). General bosonic Euler equations appear in [eom.md](field_equations.md), E16, E18, E27, E31, and E38. This report rechecks their coefficients on the selected background by variation and solves the coupled algebraic system.

Couplings and bosonic backgrounds are real. The input action has domain $`L\ne0`$; no additional $`L>0`$ condition is imposed. No $`\alpha`$ expansion is performed. Auxiliary fields are not eliminated in the general theory; only field values in the specified background class are determined by the total theory's equations.

<a id="2-selected-local-ads₅-class"></a>

## Selected local AdS₅ class

The superscript $`(0)`$ denotes a background value. The curvature convention and AdS radius $`\ell_{\mathrm{AdS}}>0`$ are:

```math
\begin{gathered}
R_{\mu\nu\rho\sigma}^{(0)}
=k\bigl(g_{\mu\rho}^{(0)}g_{\nu\sigma}^{(0)}
-g_{\mu\sigma}^{(0)}g_{\nu\rho}^{(0)}\bigr),
\qquad k=-\ell_{\mathrm{AdS}}^{-2}<0,\\
R_{\mu\nu}^{(0)}=4k\,g_{\mu\nu}^{(0)},\qquad
R^{(0)}=20k,\qquad
R_{\mu\nu}^{(0)}R^{(0)\mu\nu}=80k^2.
\end{gathered}
\tag{AD2}
```

The contracted Bianchi identity gives

```math
4\partial_\nu k
=\nabla^{(0)\mu}R_{\mu\nu}^{(0)}
=\frac12\partial_\nu R^{(0)}
=10\partial_\nu k
\quad\Longrightarrow\quad \partial_\nu k=0
\tag{AD3}
```

The other background conditions are:

```math
\begin{gathered}
L^{(0)}=L_0\ne0,\qquad N^{(0)}=N_0,\qquad
\partial_\mu L_0=\partial_\mu N_0=0,\qquad
L_0^{ij}=\frac{L_0}{\sqrt2}\delta^{ij},\\
G^{(0)}=0,\qquad H_3^{(0)}=0,\qquad
P^{(0)\mu}=0,\qquad \mathcal F_{\mu\nu}^{(0)ij}=0,\qquad
V_\mu^{\prime(0)ij}=0,\\
\psi_\mu^{(0)i}=0,\qquad \varphi^{(0)i}=0.
\end{gathered}
\tag{AD4}
```

Here $`\mathcal F^{ij}`$ is the bosonic curvature of the $`V^{ij}=V'^{ij}+\delta^{ij}V/2`$ connection. The form definitions and allowed potential profiles are:

```math
\begin{aligned}
G&=dC,\qquad
H_3=dB_2+\frac12C\wedge G+\frac g2E_3,\\
P^\mu&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda},\\
dC^{(0)}&=0,\qquad dV^{(0)}=0,\qquad
dB_2^{(0)}+\frac g2E_3^{(0)}=0,\\
E_3^{(0)}&=-\frac2g\,dB_2^{(0)}
\quad\Longrightarrow\quad dE_3^{(0)}=0
\quad\Longrightarrow\quad P^{(0)\mu}=0.
\end{aligned}
\tag{AD5}
```

No additional gauge condition is imposed on the potentials themselves. This local class fixes neither global topology nor flat-connection holonomies. Preserved supersymmetry is not assumed.

<a id="3-evaluation-of-all-independent-field-equations"></a>

## Evaluation of all independent field equations

<a id="31-variation-order-and-fermion-equations"></a>

### Variation order and fermion equations

Let $`\Phi_B`$ and $`\Phi_F`$ denote all independent bosons and physical fermions, respectively. For $`S=S_0+S_2+O(\Phi_F^4)`$, decomposed by physical fermion degree,

```math
\begin{aligned}
\left.\frac{\delta S}{\delta\Phi_B}\right|_{\Phi_F=0}
&=\frac{\delta S_0}{\delta\Phi_B},\\
\frac{\delta S_2}{\delta\Phi_F}&=O(\Phi_F),\qquad
\frac{\delta O(\Phi_F^4)}{\delta\Phi_F}=O(\Phi_F^3),\\
\left.\mathcal E_{\psi_\mu^i}\right|_0
&=\left.\mathcal E_{\varphi^i}\right|_0=0.
\end{aligned}
\tag{AD6}
```

The background condition is imposed after variation. This fermion-degree result also holds for supercovariant objects and dependent connections containing implicit fermions. Satisfaction of the zero-fermion background equations does not mean that all fermionic linear operators have been computed.

<a id="32-vectors-two-form-and-three-form"></a>

### Vectors, two-form, and three-form

Define the variation responses by

```math
\delta\ell_0\simeq_\partial
\frac12\Pi^{\mu\nu}\delta G_{\mu\nu}
+\frac16Q^{\mu\nu\rho}\delta H_{\mu\nu\rho}
+W_\mu\delta P^\mu+J_C^\mu\delta C_\mu
+\frac12M^{\mu\nu}_{ij}\delta\mathcal F_{\mu\nu}^{ij}
+\cdots
\tag{AD7}
```

Here $`\simeq_\partial`$ denotes the specified exact-divergence difference, which leaves local Euler equations unchanged; it is not a physical boundary condition. The general equations are:

```math
\begin{aligned}
\mathcal E_B^{\nu\rho}
&=-\nabla_\mu Q^{\mu\nu\rho},\\
\mathcal E_C^\nu
&=J_C^\nu-\nabla_\mu\Pi^{\mu\nu}
+\frac12Q^{\nu\mu\rho}G_{\mu\rho}
-\frac12C_\mu\mathcal E_B^{\mu\nu},\\
\mathcal E_E^{\rho\sigma\lambda}
&=\frac g2Q^{\rho\sigma\lambda}
+\frac12\varepsilon^{\mu\nu\rho\sigma\lambda}\nabla_\nu W_\mu.
\end{aligned}
\tag{AD8}
```

In AD4, field strengths, their derivatives, and internal curvature vanish. Every term of the general responses contains at least one of these objects, except the potential terms in $`W_\mu`$. Thus

```math
\Pi^{(0)\mu\nu}=Q^{(0)\mu\nu\rho}
=J_C^{(0)\mu}=M^{(0)\mu\nu}_{ij}=0,\qquad
W_\mu^{(0)}=-2\sqrt2V_\mu^{(0)}-4gC_\mu^{(0)}.
\tag{AD9}
```

The epsilon contraction selects only $`\nabla_{[\nu}W_{\mu]}`$:

```math
dW^{(0)}=-2\sqrt2\,dV^{(0)}-4g\,dC^{(0)}=0.
\tag{AD10}
```

AD8–AD10 together give

```math
\left.\mathcal E_C^\mu\right|_0
=\left.\mathcal E_B^{\mu\nu}\right|_0
=\left.\mathcal E_E^{\mu\nu\rho}\right|_0=0
\tag{AD11}
```

In particular, no condition $`W_\mu^{(0)}=0`$ follows.

For the internal connection, let $`\nabla_\mu^{(V)}`$ denote only the bosonic Levi–Civita and internal-connection derivative. The general response is

```math
\begin{aligned}
\mathcal V^\nu_{ij}
&=-\nabla_\mu^{(V)}M^{\mu\nu}_{ij}
+(4L-\alpha g^2L^2)V'{}^\nu_{ij}
-2\sqrt2P^\nu\delta_{ij},\\
\mathcal E_V^\nu&=\frac12\delta^{ij}\mathcal V^\nu_{ij},\\
\mathcal E_{V'}^\nu{}_{ij}
&=\left(\delta_{(i}^k\delta_{j)}^l
-\frac12\delta_{ij}\delta^{kl}\right)\mathcal V^\nu_{kl}.
\end{aligned}
\tag{AD12}
```

AD4 and AD9 imply $`\mathcal V^{(0)\nu}_{ij}=0`$; the trace and traceless connection equations hold separately. No division by the coefficient $`(4L-\alpha g^2L^2)`$ has been performed.

<a id="33-variation-of-the-remaining-scalar-and-vielbein-equations"></a>

### Variation of the remaining scalar and vielbein equations

For density terms whose first variations survive on the AD4 class, define

```math
\begin{aligned}
\mathcal A(L,N)&:=
L+\alpha\left(\frac{gN}{6}-\frac{g^2L^2}{12}\right),\\
\mathcal V(L,N)&:=
-\frac{2N^2}{L}-2gLN-4gN-\frac12g^2L^3+2g^2L^2\\
&\quad+\alpha\left(-\frac{g^2N^2}{6}
+\frac{2g^3NL^2}{3}+\frac{5g^4L^4}{24}\right).
\end{aligned}
\tag{AD13}
```

Here $`\mathcal V(L,N)`$ is the signed scalar-potential contribution to the density, distinct from the indexed connection Euler response $`\mathcal V^\nu_{ij}`$ in AD12. The relevant density is

```math
\ell_0\supset
\mathcal A R+\alpha\left(-\frac16R_{\mu\nu}R^{\mu\nu}
+\frac1{24}R^2\right)+\mathcal V.
\tag{AD14}
```

AD14 does not treat the background-reduced action as an independent theory. Background Euler contributions of the omitted terms vanish by AD8–AD12 and the constant-scalar conditions; curvature variation is taken for a general metric.

The scalar derivatives, with $`R`$ held independent, are:

```math
\begin{aligned}
\partial_N\mathcal A&=\frac{\alpha g}{6},\\
\partial_N\mathcal V
&=-\frac{4N}{L}-2gL-4g
+\alpha\left(-\frac{g^2N}{3}+\frac{2g^3L^2}{3}\right),\\
\partial_L\mathcal A&=1-\frac{\alpha g^2L}{6},\\
\partial_L\mathcal V
&=\frac{2N^2}{L^2}-2gN-\frac32g^2L^2+4g^2L
+\alpha\left(\frac{4g^3LN}{3}+\frac{5g^4L^3}{6}\right).
\end{aligned}
\tag{AD15}
```

Substituting $`R=20k`$ and using the abbreviation $`L=L_0,\ N=N_0`$ in this section,

```math
\boxed{
0=\mathcal E_N^{(0)}
=-\frac{4N}{L}-2gL-4g
+\alpha\left(\frac{10g}{3}k-\frac{g^2}{3}N+\frac{2g^3}{3}L^2\right).
}
\tag{AD16}
```

```math
\boxed{\begin{aligned}
0=\mathcal E_L^{(0)}
={}&20k+\frac{2N^2}{L^2}-2gN-\frac32g^2L^2+4g^2L\\
&+\alpha\left(-\frac{10g^2}{3}Lk
+\frac{4g^3}{3}LN+\frac{5g^4}{6}L^3\right).
\end{aligned}}
\tag{AD17}
```

In the metric variation, $`h^{\mu\nu}:=\delta g^{\mu\nu}`$ is only a test variation, and

```math
\delta e=-\frac12e\,g_{\mu\nu}h^{\mu\nu},\qquad
\delta R=R_{\mu\nu}h^{\mu\nu}+g^{\mu\nu}\delta R_{\mu\nu}.
\tag{AD18}
```

The Ricci response and its background value are

```math
\begin{aligned}
Z^{\mu\nu}
&:=\frac{\partial\ell_0}{\partial R_{\mu\nu}}
=\mathcal A g^{\mu\nu}
+\alpha\left(-\frac13R^{\mu\nu}+\frac1{12}Rg^{\mu\nu}\right),\\
Z^{(0)\mu\nu}
&=\left(\mathcal A+\frac{\alpha k}{3}\right)g^{(0)\mu\nu},
\qquad \nabla_\rho^{(0)}Z^{(0)\mu\nu}=0.
\end{aligned}
\tag{AD19}
```

After two integrations by parts, the response of the $`Z^{\mu\nu}\delta R_{\mu\nu}`$ term from the dependent Levi–Civita connection is

```math
\frac12\Box Z_{\mu\nu}
+\frac12g_{\mu\nu}\nabla_\rho\nabla_\sigma Z^{\rho\sigma}
-\nabla_\rho\nabla_{(\mu}Z_{\nu)}{}^\rho
\tag{AD20}
```

and vanishes on AD19. The connection was not held independent; its variation contribution vanishes only after evaluation.

The algebraic contributions of the curvature squares are:

```math
\begin{aligned}
-\frac16R_{\rho\sigma}R^{\rho\sigma}+\frac1{24}R^2
&=-\frac{80}{6}k^2+\frac{400}{24}k^2
=\frac{10}{3}k^2,\\
-\frac13R_{\mu\rho}R_\nu{}^\rho
+\frac1{12}RR_{\mu\nu}
-\frac12g_{\mu\nu}\left(-\frac16R_{\rho\sigma}R^{\rho\sigma}
+\frac1{24}R^2\right)
&=\left(-\frac{16}{3}+\frac{80}{12}-\frac53\right)
k^2g_{\mu\nu}^{(0)}
=-\frac13k^2g_{\mu\nu}^{(0)}.
\end{aligned}
\tag{AD21}
```

Thus

```math
\mathcal E_{\mu\nu}^{(0)}
=\mathfrak E\,g_{\mu\nu}^{(0)},\qquad
\mathfrak E:=-6\mathcal A k-\frac{\alpha}{3}k^2-\frac12\mathcal V,
\qquad
\mathcal E_e{}^\rho{}_a=-2e_{\nu a}\mathcal E^{\rho\nu}.
\tag{AD22}
```

Expanding AD13 gives the third independent equation:

```math
\boxed{\begin{aligned}
0=\mathfrak E={}&
-6Lk+\frac{N^2}{L}+gLN+2gN+\frac14g^2L^3-g^2L^2\\
&+\alpha\left(-\frac13k^2-gNk+\frac12g^2L^2k
+\frac1{12}g^2N^2-\frac13g^3NL^2-\frac5{48}g^4L^4\right).
\end{aligned}}
\tag{AD23}
```

AD16, AD17, and AD23 must be solved together. The two-derivative solution has not been substituted into these equations beforehand.

<a id="4-reduction-of-the-coupled-algebraic-system-without-losing-branches"></a>

## Reduction of the coupled algebraic system without losing branches

Temporary symbols used only for this solution are:

```math
q:=\alpha g^2,\qquad t:=qL,\qquad w:=L^{-1},\qquad
n:=\frac{N}{gL^2},\qquad h:=\frac{k}{g^2L^2},\qquad
u:=n+\frac32.
\tag{AD24}
```

The scalar $`h`$ here is not the indexed metric test variation of AD18. In the domain of definition,

```math
q\ne0,\qquad t\ne0,\qquad w\ne0,\qquad q=tw.
\tag{AD25}
```

Dividing AD16, AD17, and AD23 by $`gL,\ g^2L^2,\ g^2L^3`$, respectively, is valid; none of these factors vanishes in the domain:

```math
\begin{aligned}
F_N:=\frac{\mathcal E_N^{(0)}}{gL}
&=-4n-2-4w+\frac t3(10h-n+2),\\
F_L:=\frac{\mathcal E_L^{(0)}}{g^2L^2}
&=20h+2n^2-2n-\frac32+4w
+t\left(-\frac{10h}{3}+\frac{4n}{3}+\frac56\right),\\
F_e:=\frac{\mathfrak E}{g^2L^3}
&=-6h+n^2+n+\frac14+(2n-1)w\\
&\quad+t\left(-\frac{h^2}{3}-nh+\frac h2
+\frac{n^2}{12}-\frac n3-\frac5{48}\right).
\end{aligned}
\tag{AD26}
```

The sum of the first two equations is:

```math
\begin{aligned}
0=F_N+F_L
&=20h+2n^2-6n-\frac72+t\left(n+\frac32\right)\\
&=20h+2u^2+(t-12)u+10.
\end{aligned}
\tag{AD27}
```

Defining $`\mathscr H(t,u):=2u^2+(t-12)u+10`$,

```math
\begin{aligned}
h&=-\frac{\mathscr H(t,u)}{20},\\
4w&=-4n-2+\frac t3(10h-n+2)\\
&=4-4u+\frac t3\left(-\frac{\mathscr H}{2}-u+\frac72\right),\\
w&=-\frac{t^2u+2tu^2-10tu+3t+24u-24}{24}.
\end{aligned}
\tag{AD28}
```

The quantity $`\mathscr H`$ is an algebraic polynomial, not the physical three-form $`H_3`$. Write the condition $`q=tw`$ without denominators:

```math
\begin{aligned}
0=A_q(t,u)&:=-24(tw-q)\\
&=2t^2u^2+t(t-4)(t-6)u+3t^2-24t+24q.
\end{aligned}
\tag{AD29}
```

The same substitution in the metric equation explicitly factorizes as:

```math
\begin{aligned}
B(t,u):={}&4tu^3+(4t^2+32t)u^2\\
&+(t^3+16t^2-356t+480)u-60t^2+360t-480,\\
\left.F_e\right|_{\substack{n=u-3/2\\h,w\text{ AD28}}}
&=-\frac{u}{1200}
\left[4tu^3+(4t^2+32t)u^2
+(t^3+16t^2-356t+480)u
-60t^2+360t-480\right]\\
&=-\frac{u}{1200}B(t,u).
\end{aligned}
\tag{AD30}
```

Substituting AD28 into AD26 also gives the identities $`F_N=F_L=0`$. Thus an equivalent form of the complete system is

```math
\boxed{
A_q(t,u)=0,\qquad uB(t,u)=0,\qquad
t\ne0,\quad q\ne0,\quad \mathscr H(t,u)>0.
}
\tag{AD31}
```

The final inequality is the equivalence

```math
k=-\frac{g^2L^2}{20}\mathscr H(t,u)<0
\quad\Longleftrightarrow\quad \mathscr H(t,u)>0
\tag{AD32}
```

No division by $`u`$ or by the potentially vanishing coefficient $`12+qL`$ has been performed.

<a id="5-branch-i-u0"></a>

## Branch I: $`u=0`$

AD28–AD29:

```math
\begin{aligned}
u=0&\quad\Longrightarrow\quad
n=-\frac32,\quad h=-\frac12,\quad w=1-\frac t8,\\
A_q(t,0)&=3(t^2-8t+8q)=0,\\
t=qL,\quad q\ne0
&\quad\Longrightarrow\quad qL^2-8L+8=0.
\end{aligned}
\tag{AD33}
```

In the original variables, the two roots and curvature scale are:

```math
\boxed{\begin{aligned}
L_{0,\pm}
&=\frac4{\alpha g^2}
\left(1\pm\sqrt{1-\frac{\alpha g^2}{2}}\right),\\
N_{0,\pm}&=-\frac32gL_{0,\pm}^2,\\
\ell_{\mathrm{AdS},\pm}^{-2}
&=\frac12g^2L_{0,\pm}^2,\qquad
R^{(0)}_\pm=-10g^2L_{0,\pm}^2.
\end{aligned}}
\tag{AD34}
```

Reality and merger regions:

| Parameter region | Branch I solutions |
|---|---|
| $`\alpha g^2<0`$ | Two real AdS solutions; one $`L_0`$ value positive, the other negative |
| $`0<\alpha g^2<2`$ | Two distinct positive $`L_0`$ values, both AdS |
| $`\alpha g^2=2`$ | The two roots merge: $`L_0=2`$, $`N_0=-6g`$, $`\ell_{\mathrm{AdS}}^{-2}=2g^2`$ |
| $`\alpha g^2>2`$ | No real solution on Branch I |

The special value $`\alpha g^2=2`$ follows from the vanishing discriminant in AD34. The value $`\alpha g^2=0`$ lies outside the initial domain. No additional restriction is imposed on the sign of $`L_0`$.

For direct back-substitution, define $`\mathscr R:=qL^2-8L+8`$. On the relations $`N=-3gL^2/2,\ k=-g^2L^2/2`$,

```math
\begin{aligned}
\mathcal E_N^{(0)}
&=-\frac g2\,\mathscr R,\\
\mathcal E_L^{(0)}
&=\frac{g^2L}{2}\,\mathscr R,\\
\mathfrak E&=-\frac{g^2L^2}{2}\,\mathscr R.
\end{aligned}
\tag{AD35}
```

Thus $`\mathscr R=0`$ satisfies all three original equations simultaneously.

<a id="6-branch-ii-une0-and-btu0"></a>

## Branch II: $`u\ne0`$ and $`B(t,u)=0`$

<a id="61-generic-part"></a>

### Generic part

Define temporary polynomials

```math
\begin{aligned}
\mathscr D_q(t)&:=t(16q+34t^2+112t-192),\\
\mathscr C_q(t)&:=21t^4-102t^3-72t^2+192t
+8q(t^2+26t-24)
\end{aligned}
\tag{AD36}
```

as follows. The quantity $`\mathscr D_q`$ is not the dependent scalar composite $`D`$. The denominator-free polynomial-division identity is:

```math
\boxed{
t^2B(t,u)
=(2tu+t^2+26t-24)A_q(t,u)
-3\bigl(\mathscr D_q(t)u+\mathscr C_q(t)\bigr).
}
\tag{AD37}
```

On the $`\mathscr D_q(t)\ne0`$ part, $`A_q=B=0`$ requires

```math
u=-\frac{\mathscr C_q(t)}{\mathscr D_q(t)}
\tag{AD38}
```

as stated. The denominator-cleared expansion of AD29 at this value is

```math
\begin{aligned}
\mathscr D_q^2 A_q\left(t,-\frac{\mathscr C_q}{\mathscr D_q}\right)
&=2t^2\mathscr C_q^2
-t(t-4)(t-6)\mathscr C_q\mathscr D_q
+(3t^2-24t+24q)\mathscr D_q^2\\
&=4t^2P_q(t)
\end{aligned}
\tag{AD39}
```

with the degree-eight polynomial

```math
\boxed{\begin{aligned}
P_q(t)={}&42t^8-78t^7+(1959+16q)t^6\\
&+(-32424+3488q)t^5+(80640-9400q)t^4\\
&+(-53760+59776q+1152q^2)t^3\\
&+(-215040q+35136q^2)t^2\\
&+(184320q-47616q^2)t+1536q^3
\end{aligned}}
\tag{AD40}
```

The resultant check of the same elimination is

```math
\mathop{\mathrm{Res}}\nolimits_u(A_q,B)=144t^2P_q(t)
\tag{AD41}
```

Sufficiency of the solutions follows from AD37 and AD39, rather than from the resultant alone.

For fixed but symbolic $`q=\alpha g^2\ne0`$, take each real algebraic root of $`P_q(t)`$. After determining $`u`$ with AD38, the complete admissibility conditions are

```math
\boxed{
\mathscr D_q(t)\ne0,\qquad
u\ne0,\qquad
\mathscr H(t,u)=2u^2+(t-12)u+10>0.
}
\tag{AD42}
```

Since $`P_q(0)=1536q^3\ne0`$, none of these roots is $`t=0`$. Roots are not assumed simple.

In the original field and coupling variables:

```math
\boxed{\begin{aligned}
L_0&=\frac{t}{\alpha g^2},\\
N_0&=\frac{t^2}{\alpha^2g^3}\left(u-\frac32\right),\\
\ell_{\mathrm{AdS}}^{-2}
&=\frac{t^2}{20\alpha^2g^2}
\left[2u^2+(t-12)u+10\right],\\
R^{(0)}
&=-\frac{t^2}{\alpha^2g^2}
\left[2u^2+(t-12)u+10\right],
\qquad q=\alpha g^2.
\end{aligned}}
\tag{AD43}
```

The quantity $`t`$ is an exactly defined algebraic root of AD40; $`u`$ is the rational root function in AD38. No approximate root or parameter sampling is used. This branch's parameter region is specified exactly by the real-root conditions and AdS inequalities in AD40 and AD42; no additional sign or magnitude assumption is made for $`\alpha`$.

Back-substitution:

```math
\begin{aligned}
P_q(t)=0,\quad t\ne0,\quad \mathscr D_q(t)\ne0
&\overset{\mathrm{AD39}}{\Longrightarrow} A_q(t,u)=0,\\
u=-\mathscr C_q/\mathscr D_q,\quad A_q=0
&\overset{\mathrm{AD37}}{\Longrightarrow} B(t,u)=0,\\
A_q=0&\Longrightarrow q=tw,\quad L=t/q=1/w,\\
h,w\text{ AD28},\quad uB=0
&\Longrightarrow F_N=F_L=F_e=0\\
&\Longrightarrow
\mathcal E_N^{(0)}=\mathcal E_L^{(0)}=\mathfrak E=0.
\end{aligned}
\tag{AD44}
```

This chain shows that the generic part of the elimination polynomial introduces no spurious solutions.

<a id="62-special-part-mathscr-d_qt0"></a>

### Special part $`\mathscr D_q(t)=0`$

The branch where the denominator of AD38 vanishes is retained. Since $`t\ne0`$,

```math
\mathscr D_q(t)=0
\quad\Longleftrightarrow\quad
q=12-7t-\frac{17}{8}t^2.
\tag{AD45}
```

In AD37, $`A_q=B=0`$ also requires $`\mathscr C_q=0`$:

```math
\left.\mathscr C_q(t)\right|_{q=12-7t-17t^2/8}
=4\left(t^4-150t^3-256t^2+1008t-576\right).
\tag{AD46}
```

Thus, on this special part,

```math
\boxed{
t^4-150t^3-256t^2+1008t-576=0,\qquad
q=12-7t-\frac{17}{8}t^2\ne0.
}
\tag{AD47}
```

The remaining quadratic equation and its discriminant are:

```math
\begin{aligned}
\left.A_q(t,u)\right|_{\mathrm{AD45}}
&=2t^2u^2+t(t-4)(t-6)u-48t^2-192t+288=0,\\
\mathop{\mathrm{disc}}\nolimits_u\left(A_q|_{\mathrm{AD45}}\right)
&=t^2\Delta(t),\\
\Delta(t)&:=t^4-20t^3+532t^2+1056t-1728.
\end{aligned}
\tag{AD48}
```

The two root sets are given by

```math
\boxed{
u_\pm=
\frac{-(t-4)(t-6)\pm\sqrt{\Delta(t)}}{4t}
}
\tag{AD49}
```

Both roots of $`\pm`$ are retained; for $`\Delta=0`$, the shared root represents a single background value. The admissibility conditions are

```math
t\in\mathbb R,\quad q=\alpha g^2\ne0,\quad
\Delta(t)\ge0,\quad u_\pm\ne0,\quad
2u_\pm^2+(t-12)u_\pm+10>0.
\tag{AD50}
```

The $`L_0,N_0,\ell_{\mathrm{AdS}}`$ values of each admissible root are AD43. Since the quartic polynomial in AD47 has nonzero constant term, $`t=0`$ is already excluded.

Since $`\mathscr C_q=\mathscr D_q=0`$ on this part,

```math
A_q=0
\overset{\mathrm{AD37}}{\Longrightarrow} t^2B=0
\Longrightarrow B=0.
\tag{AD51}
```

The final two lines of AD44 then satisfy all three original equations.

<a id="7-branch-mergers-and-the-vanishing-n-coefficient-region"></a>

## Branch mergers and the vanishing-$`N`$-coefficient region

<a id="71-shared-boundary-points-of-branches-i-and-ii"></a>

### Shared boundary points of Branches I and II

At the $`u=0`$ boundary of Branch II:

```math
\begin{aligned}
A_q(t,0)&=3(t^2-8t+8q),\\
B(t,0)&=-60(t-2)(t-4),\\
A_q(t,0)=B(t,0)=0
&\quad\Longleftrightarrow\quad
(q,t)=\left(\frac32,2\right)
\ \text{or}\ (q,t)=(2,4).
\end{aligned}
\tag{AD52}
```

These numbers are exact solutions of the common-root equations, not free-parameter samples. At the first point,

```math
\alpha g^2=\frac32,\qquad
L_0=\frac43,\qquad N_0=-\frac83g,\qquad
\ell_{\mathrm{AdS}}^{-2}=\frac89g^2;
\tag{AD53}
```

at the second point

```math
\alpha g^2=2,\qquad
L_0=2,\qquad N_0=-6g,\qquad
\ell_{\mathrm{AdS}}^{-2}=2g^2.
\tag{AD54}
```

Since the separate definition of Branch II uses $`u\ne0`$, these shared backgrounds are counted on Branch I. At other multiple algebraic roots,

```math
P_q(t)=0,\qquad \partial_tP_q(t)=0
\tag{AD55}
```

may hold. Since the solution definition does not divide by $`\partial_tP_q`$, these remain included in AD40–AD50. A repeated root is not counted as an additional background unless it gives different field values.

<a id="72-special-branch-that-division-of-the-n-equation-could-discard"></a>

### Special branch that division of the $`N`$ equation could discard

The vanishing-coefficient condition for $`N`$ in AD16 is

```math
\frac4{L_0}+\frac{\alpha g^2}{3}
=\frac{12+t}{3L_0}=0
\quad\Longleftrightarrow\quad t=-12
\tag{AD56}
```

At the value derived from this equation, AD29 and AD30 become:

```math
\begin{aligned}
A_q(-12,u)&=24(q+12u^2-144u+30),\\
B(-12,u)&=-48(u^3-4u^2-111u+280),\\
\mathscr H(-12,u)&=2(u^2-12u+5).
\end{aligned}
\tag{AD57}
```

Thus there are two possibilities:

```math
\boxed{
\begin{cases}
u=0,\quad q=-30, &\text{Branch I},\\
u^3-4u^2-111u+280=0,\quad
q=-12u^2+144u-30, &\text{Branch II}.
\end{cases}
}
\tag{AD58}
```

In the second row, $`u`$ is a real algebraic root; $`q=\alpha g^2\ne0`$ and

```math
u^2-12u+5>0
\tag{AD59}
```

the AdS conditions are retained. Field values follow from AD43 using $`t=-12`$. The field values in the first row are

```math
\alpha g^2=-30,\qquad
L_0=\frac25,\qquad N_0=-\frac6{25}g,\qquad
\ell_{\mathrm{AdS}}^{-2}=\frac2{25}g^2.
\tag{AD60}
```

This branch demonstrates why the $`N`$ equation must not initially be divided by $`4/L+\alpha g^2/3`$.

<a id="8-other-background-values-and-dependent-objects"></a>

## Other background values and dependent objects

For every admissible solution, the backgrounds of all independent fields are:

| Independent field | Background value or condition |
|---|---|
| $`e_\mu{}^a`$ | $`R_{\mu\nu\rho\sigma}^{(0)}=-\ell_{\mathrm{AdS}}^{-2}(g_{\mu\rho}^{(0)}g_{\nu\sigma}^{(0)}-g_{\mu\sigma}^{(0)}g_{\nu\rho}^{(0)})`$ |
| $`L`$ | AD34 for Branch I; AD43 for Branch II |
| $`N`$ | AD34 for Branch I; AD43 for Branch II |
| $`C_\mu`$ | $`dC^{(0)}=0`$ |
| $`B_{\mu\nu}`$ | $`dB_2^{(0)}+gE_3^{(0)}/2=0`$ |
| $`E_{\mu\nu\rho}`$ | AD5; consequently $`dE_3^{(0)}=0`$ |
| $`V_\mu`$ | $`dV^{(0)}=0`$ |
| $`V_\mu^{\prime ij}`$ | $`V_\mu^{\prime(0)ij}=0`$ |
| $`\psi_\mu^i`$ | $`\psi_\mu^{(0)i}=0`$ |
| $`\varphi^i`$ | $`\varphi^{(0)i}=0`$ |

No separate Euler equation is added for dependent connections or composites. The background values of their common definitions are:

```math
\begin{aligned}
\omega_\mu^{(0)ab}&=\omega_\mu^{ab}(e^{(0)}),\qquad
\phi_\mu^{(0)i}=0,\\
f_\mu^{(0)a}
&=-\frac16R_\mu^{(0)a}+\frac1{48}e_\mu^{(0)a}R^{(0)}
=\left(-\frac{4k}{6}+\frac{20k}{48}\right)e_\mu^{(0)a}
=-\frac k4e_\mu^{(0)a}
=\frac1{4\ell_{\mathrm{AdS}}^2}e_\mu^{(0)a},\\
T_{ab}^{(0)}&=0,\qquad \chi^{(0)i}=0,\qquad
Y^{(0)ij}=-\frac g2L_0^{ij}
=-\frac{gL_0}{2\sqrt2}\delta^{ij},\\
D^{(0)}
&=-\frac{R^{(0)}}{32}+\frac g4N_0+\frac{g^2}{16}L_0^2
=-\frac58k+\frac g4N_0+\frac{g^2}{16}L_0^2.
\end{aligned}
\tag{AD61}
```

Check of the final line using AD24 and AD28:

```math
\begin{aligned}
\frac{D^{(0)}}{g^2L_0^2}
&=\frac{\mathscr H}{32}+\frac14\left(u-\frac32\right)+\frac1{16}\\
&=\frac{\mathscr H+8u-10}{32}
=\frac{u(t+2u-4)}{32}.
\end{aligned}
\tag{AD62}
```

In the original couplings,

```math
\boxed{
D^{(0)}=\frac{t^2}{32\alpha^2g^2}\,u(t+2u-4)
}
\tag{AD63}
```

On Branch I, $`u=0`$ implies $`D^{(0)}=0`$.

<a id="9-symbolic-verification-and-solution-set"></a>

## Symbolic verification and solution set

The scalar variations, metric coefficient, rewriting in AD26, reduction in AD28–AD30, elimination in AD37–AD41, special branch in AD45–AD49, and vanishing-coefficient branch in AD57 were checked by exact arithmetic and polynomial identities. No numerical sample value was assigned to free physical parameters or their combinations. Every special numerical value was derived from its branch equation.

The AdS solution set is

```math
\boxed{
\mathfrak B_{\mathrm{AdS}}
=\mathfrak B_{\mathrm I}
\ \cup\ 
\mathfrak B_{\mathrm{II},\,\mathscr D\ne0}
\ \cup\
\mathfrak B_{\mathrm{II},\,\mathscr D=0}
}
\tag{AD64}
```

Here $`\mathfrak B_{\mathrm I}`$ denotes the real roots of AD34; $`\mathfrak B_{\mathrm{II},\,\mathscr D\ne0}`$ denotes backgrounds defined by AD38, AD40, AD42, and AD43; and $`\mathfrak B_{\mathrm{II},\,\mathscr D=0}`$ those defined by AD43 and AD47–AD50. Independent vector, form, internal-connection, and fermion equations hold for each set by AD6–AD12. Dependence on $`\alpha,g`$ is exact.

This classifies only the selected local, maximally symmetric, fermion-free AdS₅ backgrounds. All bosonic and fermionic fluctuations are retained; no additional conclusion about preserved supersymmetry, linear spectra, stability, or unitarity is drawn.
