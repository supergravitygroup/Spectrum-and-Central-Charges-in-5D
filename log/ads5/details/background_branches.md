# LOG: AdS5 backgrounds and selected branch

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="6-exact-ads_5-background-branches-of-the-total-theory"></a>

## Exact AdS$`_5`$ background branches of the total theory

## Action and domain

The unique higher-derivative coupling is $`\alpha`$ in

```math
\boxed{
S=S_{2\partial}+\alpha S_{\log}
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2\partial}+\alpha\ell_{\log}\bigr),
\qquad \alpha\ne0,\quad g\ne0.
}
\tag{AD1}
```

The earlier name $`\lambda_{R^2}`$ is corrected to $`\alpha`$. It had already been identified with this coupling, so the solutions and normalization are unchanged. The coefficient of the isolated $`R^2`$ monomial is $`\alpha/24`$; the coefficient of the complete LOG invariant is $`\alpha`$.

The bosonic Euler equations E16, E18, E27, E31, and E38 are now evaluated on the selected background class. Their surviving coefficients are checked by variation before solving the coupled algebraic system.

Couplings and bosonic backgrounds are real. The action requires $`L\ne0`$; no extra positivity condition is imposed on all branches. No expansion in $`\alpha`$ or general auxiliary-field elimination is used. Only background values are solved from the total equations.

## Local AdS$`_5`$ class

A superscript $`(0)`$ denotes a background value. With $`\ell_{\mathrm{AdS}}>0`$, the curvature convention is

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

The other background conditions are

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

Here $`\mathcal F^{ij}`$ is the bosonic curvature of $`V^{ij}=V'^{ij}+\delta^{ij}V/2`$. The permitted potentials obey

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

No additional potential gauge is imposed. This local class leaves topology and flat holonomies unspecified and does not assume preserved SUSY.

## Evaluation of all independent equations

### Variation order and fermion equations

Let $`\Phi_B,\Phi_F`$ denote all independent bosons and physical fermions. For $`S=S_0+S_2+O(\Phi_F^4)`$,

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

The background is imposed after variation. This degree argument includes implicit fermions in supercovariant objects and dependent connections. Vanishing background fermion equations do not amount to computing their linear operators.

### Vectors and forms

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

The symbol $`\simeq_\partial`$ denotes an explicit divergence that preserves local Euler equations, not a physical boundary prescription. The general equations are

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

On AD4 all strengths, their derivatives, and internal curvatures vanish. Every response contains one such factor except the potential terms in $`W_\mu`$. Thus

```math
\Pi^{(0)\mu\nu}=Q^{(0)\mu\nu\rho}
=J_C^{(0)\mu}=M^{(0)\mu\nu}_{ij}=0,\qquad
W_\mu^{(0)}=-2\sqrt2V_\mu^{(0)}-4gC_\mu^{(0)}.
\tag{AD9}
```

Only $`\nabla_{[\nu}W_{\mu]}`$ survives the epsilon contraction:

```math
dW^{(0)}=-2\sqrt2\,dV^{(0)}-4g\,dC^{(0)}=0.
\tag{AD10}
```

Combining AD8–AD10 gives

```math
\left.\mathcal E_C^\mu\right|_0
=\left.\mathcal E_B^{\mu\nu}\right|_0
=\left.\mathcal E_E^{\mu\nu\rho}\right|_0=0
\tag{AD11}
```

In particular, $`W_\mu^{(0)}=0`$ is not required.

For the internal connection, let $`\nabla^{(V)}`$ contain only bosonic Levi–Civita and internal connections. The response is

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

AD4/AD9 make $`\mathcal V^{(0)\nu}_{ij}=0`$, separately satisfying trace and traceless equations without dividing by $`4L-\alpha g^2L^2`$.

### Scalar and vielbein variations

The density terms whose first variations survive have coefficients

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

The signed potential contribution $`\mathcal V(L,N)`$ is distinct from the indexed connection response $`\mathcal V^\nu_{ij}`$. The relevant density is

```math
\ell_0\supset
\mathcal A R+\alpha\left(-\frac16R_{\mu\nu}R^{\mu\nu}
+\frac1{24}R^2\right)+\mathcal V.
\tag{AD14}
```

This does not turn the restricted density into an independent theory: omitted terms have vanishing background Euler contributions by the already evaluated equations. Curvature is varied on a general metric first.

Differentiate the scalars while holding $`R`$ independent:

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

Then substitute $`R=20k`$ and abbreviate $`L=L_0,N=N_0`$:

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

For the metric test variation $`h^{\mu\nu}=\delta g^{\mu\nu}`$,

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

The dependent Levi–Civita term $`Z^{\mu\nu}\delta R_{\mu\nu}`$ contributes, after two integrations by parts,

```math
\frac12\Box Z_{\mu\nu}
+\frac12g_{\mu\nu}\nabla_\rho\nabla_\sigma Z^{\rho\sigma}
-\nabla_\rho\nabla_{(\mu}Z_{\nu)}{}^\rho
\tag{AD20}
```

which vanishes on AD19. The connection contribution has been evaluated before being set to zero.

The algebraic curvature-square contributions are

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

Consequently,

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

AD16, AD17, and AD23 must be solved together. The two-derivative vacuum was not inserted beforehand.

## Lossless algebraic reduction

For this solution only, define

```math
q:=\alpha g^2,\qquad t:=qL,\qquad w:=L^{-1},\qquad
n:=\frac{N}{gL^2},\qquad h:=\frac{k}{g^2L^2},\qquad
u:=n+\frac32.
\tag{AD24}
```

The scalar $`h`$ here is distinct from the indexed metric test variation. In the action domain,

```math
q\ne0,\qquad t\ne0,\qquad w\ne0,\qquad q=tw.
\tag{AD25}
```

The divisors $`gL,g^2L^2,g^2L^3`$ are nonzero, so the three equations may be rewritten as

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

Adding the first two gives

```math
\begin{aligned}
0=F_N+F_L
&=20h+2n^2-6n-\frac72+t\left(n+\frac32\right)\\
&=20h+2u^2+(t-12)u+10.
\end{aligned}
\tag{AD27}
```

With $`\mathscr H(t,u)=2u^2+(t-12)u+10`$,

```math
\begin{aligned}
h&=-\frac{\mathscr H(t,u)}{20},\\
4w&=-4n-2+\frac t3(10h-n+2)\\
&=4-4u+\frac t3\left(-\frac{\mathscr H}{2}-u+\frac72\right),\\
w&=-\frac{t^2u+2tu^2-10tu+3t+24u-24}{24}.
\end{aligned}
\tag{AD28}
```

The polynomial $`\mathscr H`$ is not the physical three-form. Write $`q=tw`$ without denominators:

```math
\begin{aligned}
0=A_q(t,u)&:=-24(tw-q)\\
&=2t^2u^2+t(t-4)(t-6)u+3t^2-24t+24q.
\end{aligned}
\tag{AD29}
```

The same substitution factorizes the metric equation as

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

Substituting AD28 into AD26 also gives $`F_N=F_L=0`$. The equivalent full system is

```math
\boxed{
A_q(t,u)=0,\qquad uB(t,u)=0,\qquad
t\ne0,\quad q\ne0,\quad \mathscr H(t,u)>0.
}
\tag{AD31}
```

The final inequality follows from

```math
k=-\frac{g^2L^2}{20}\mathscr H(t,u)<0
\quad\Longleftrightarrow\quad \mathscr H(t,u)>0
\tag{AD32}
```

No division by $`u`$ or the potentially zero coefficient $`12+qL`$ has occurred.

## Branch I: $`u=0`$

Equations AD28–AD29 reduce to

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

In the original variables, the two roots and curvature scale are

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

Their real domains and merger are

| Parameter region | Branch-I solutions |
|---|---|
| $`\alpha g^2<0`$ | Two real AdS solutions; $`L_0`$ one positive and one negative value |
| $`0<\alpha g^2<2`$ | Two distinct positive values of $`L_0`$, both AdS |
| $`\alpha g^2=2`$ | The roots merge: $`L_0=2`$, $`N_0=-6g`$, $`\ell_{\mathrm{AdS}}^{-2}=2g^2`$ |
| $`\alpha g^2>2`$ | No real branch-I solution |

The value $`\alpha g^2=2`$ follows from the vanishing discriminant, rather than an arbitrary parameter choice. The value $`\alpha g^2=0`$ lies outside the initial domain. No additional sign condition on $`L_0`$ is imposed.

For substitution back into the original equations, put $`\mathscr R=qL^2-8L+8`$. At $`N=-3gL^2/2,k=-g^2L^2/2`$,

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

Hence $`\mathscr R=0`$ satisfies all three equations simultaneously.

## Branch II: $`u\ne0`$ and $`B(t,u)=0`$

### Generic denominator

Define the polynomials

```math
\begin{aligned}
\mathscr D_q(t)&:=t(16q+34t^2+112t-192),\\
\mathscr C_q(t)&:=21t^4-102t^3-72t^2+192t
+8q(t^2+26t-24)
\end{aligned}
\tag{AD36}
```

The symbol $`\mathscr D_q`$ is distinct from the composite scalar $`D`$. Polynomial division gives the denominator-free identity

```math
\boxed{
t^2B(t,u)
=(2tu+t^2+26t-24)A_q(t,u)
-3\bigl(\mathscr D_q(t)u+\mathscr C_q(t)\bigr).
}
\tag{AD37}
```

Where $`\mathscr D_q(t)\ne0`$, the equations $`A_q=B=0`$ imply

```math
u=-\frac{\mathscr C_q(t)}{\mathscr D_q(t)}
\tag{AD38}
```

Clearing the denominator in AD29 gives

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

The resultant supplies the additional elimination check

```math
\mathop{\mathrm{Res}}\nolimits_u(A_q,B)=144t^2P_q(t)
\tag{AD41}
```

Sufficiency follows from AD37/AD39, rather than from the resultant alone.

For symbolic nonzero $`q=\alpha g^2`$, retain every real algebraic root of $`P_q(t)`$. Determine $`u`$ by AD38 and impose exactly

```math
\boxed{
\mathscr D_q(t)\ne0,\qquad
u\ne0,\qquad
\mathscr H(t,u)=2u^2+(t-12)u+10>0.
}
\tag{AD42}
```

Since $`P_q(0)=1536q^3\ne0`$, none of these roots is zero. Simplicity of a root is not assumed.

The original field values are

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

Here $`t`$ is the exact algebraic root defined by AD40, and $`u`$ its AD38 rational function. The real-root and AdS inequalities AD40/AD42 specify the domain without numerical roots or an extra sign assumption on $`\alpha`$.

The substitution check is

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

This excludes spurious roots in the generic elimination branch.

### Exceptional denominator $`\mathscr D_q(t)=0`$

The zero-denominator branch is retained. Since $`t\ne0`$,

```math
\mathscr D_q(t)=0
\quad\Longleftrightarrow\quad
q=12-7t-\frac{17}{8}t^2.
\tag{AD45}
```

Equation AD37 additionally requires $`\mathscr C_q=0`$:

```math
\left.\mathscr C_q(t)\right|_{q=12-7t-17t^2/8}
=4\left(t^4-150t^3-256t^2+1008t-576\right).
\tag{AD46}
```

Thus the exceptional branch obeys

```math
\boxed{
t^4-150t^3-256t^2+1008t-576=0,\qquad
q=12-7t-\frac{17}{8}t^2\ne0.
}
\tag{AD47}
```

The remaining quadratic and its discriminant are

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

Its two roots are

```math
\boxed{
u_\pm=
\frac{-(t-4)(t-6)\pm\sqrt{\Delta(t)}}{4t}
}
\tag{AD49}
```

Both signs are retained; a zero discriminant yields one background value. The acceptance conditions are

```math
t\in\mathbb R,\quad q=\alpha g^2\ne0,\quad
\Delta(t)\ge0,\quad u_\pm\ne0,\quad
2u_\pm^2+(t-12)u_\pm+10>0.
\tag{AD50}
```

AD43 gives the corresponding fields and radius. The nonzero constant term of the AD47 quartic already excludes $`t=0`$.

Since $`\mathscr C_q=\mathscr D_q=0`$,

```math
A_q=0
\overset{\mathrm{AD37}}{\Longrightarrow} t^2B=0
\Longrightarrow B=0.
\tag{AD51}
```

The last two lines of AD44 then verify all three original equations.

## Branch mergers and the vanishing $`N`$ coefficient

### Common limits of branches I and II

On the $`u=0`$ boundary of branch II,

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

These exact values solve the common-root equations; they are not samples of free parameters. At the first point,

```math
\alpha g^2=\frac32,\qquad
L_0=\frac43,\qquad N_0=-\frac83g,\qquad
\ell_{\mathrm{AdS}}^{-2}=\frac89g^2;
\tag{AD53}
```

and at the second,

```math
\alpha g^2=2,\qquad
L_0=2,\qquad N_0=-6g,\qquad
\ell_{\mathrm{AdS}}^{-2}=2g^2.
\tag{AD54}
```

These common backgrounds are counted in branch I because branch II is defined by $`u\ne0`$. Other repeated roots can satisfy

```math
P_q(t)=0,\qquad \partial_tP_q(t)=0
\tag{AD55}
```

The solution definition never divides by $`\partial_tP_q`$, so these roots remain included. A repeated algebraic root is not counted as multiple backgrounds unless it gives distinct field values.

### Branch lost by division of the $`N`$ equation

The coefficient of $`N`$ in AD16 vanishes when

```math
\frac4{L_0}+\frac{\alpha g^2}{3}
=\frac{12+t}{3L_0}=0
\quad\Longleftrightarrow\quad t=-12
\tag{AD56}
```

At this equation-determined value, AD29/AD30 become

```math
\begin{aligned}
A_q(-12,u)&=24(q+12u^2-144u+30),\\
B(-12,u)&=-48(u^3-4u^2-111u+280),\\
\mathscr H(-12,u)&=2(u^2-12u+5).
\end{aligned}
\tag{AD57}
```

There are therefore two possibilities:

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

In the second row $`u`$ is a real algebraic root, with nonzero $`q=\alpha g^2`$ and the AdS conditions

```math
u^2-12u+5>0
\tag{AD59}
```

Use $`t=-12`$ in AD43 for the fields. For the first row they are explicitly

```math
\alpha g^2=-30,\qquad
L_0=\frac25,\qquad N_0=-\frac6{25}g,\qquad
\ell_{\mathrm{AdS}}^{-2}=\frac2{25}g^2.
\tag{AD60}
```

This branch demonstrates why the original $`N`$ equation must not be divided by $`4/L+\alpha g^2/3`$ without a separate zero-case analysis.

## Remaining background fields and composites

For every admitted solution the independent fields have background values

| Independent field | Background value or condition |
|---|---|
| $`e_\mu{}^a`$ | $`R_{\mu\nu\rho\sigma}^{(0)}=-\ell_{\mathrm{AdS}}^{-2}(g_{\mu\rho}^{(0)}g_{\nu\sigma}^{(0)}-g_{\mu\sigma}^{(0)}g_{\nu\rho}^{(0)})`$ |
| $`L`$ | AD34 for branch I; AD43 for branch II |
| $`N`$ | AD34 for branch I; AD43 for branch II |
| $`C_\mu`$ | $`dC^{(0)}=0`$ |
| $`B_{\mu\nu}`$ | $`dB_2^{(0)}+gE_3^{(0)}/2=0`$ |
| $`E_{\mu\nu\rho}`$ | AD5, implying $`dE_3^{(0)}=0`$ |
| $`V_\mu`$ | $`dV^{(0)}=0`$ |
| $`V_\mu^{\prime ij}`$ | $`V_\mu^{\prime(0)ij}=0`$ |
| $`\psi_\mu^i`$ | $`\psi_\mu^{(0)i}=0`$ |
| $`\varphi^i`$ | $`\varphi^{(0)i}=0`$ |

No extra Euler equations are introduced for dependent connections or composites. Their defining expressions give

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

The last line is checked using AD24/AD28:

```math
\begin{aligned}
\frac{D^{(0)}}{g^2L_0^2}
&=\frac{\mathscr H}{32}+\frac14\left(u-\frac32\right)+\frac1{16}\\
&=\frac{\mathscr H+8u-10}{32}
=\frac{u(t+2u-4)}{32}.
\end{aligned}
\tag{AD62}
```

Restoring the original couplings,

```math
\boxed{
D^{(0)}=\frac{t^2}{32\alpha^2g^2}\,u(t+2u-4)
}
\tag{AD63}
```

and branch I has $`D^{(0)}=0`$ because $`u=0`$.

## Symbolic verification and solution set

The scalar variations, metric coefficient, algebraic reduction, elimination, exceptional denominator, and vanishing-coefficient branch were checked with exact arithmetic and polynomial identities. Every special numerical value follows from a branch equation; no free parameter was sampled.

The complete solution set within this local class is

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

Here $`\mathfrak B_{\mathrm I}`$ consists of the real AD34 roots; $`\mathfrak B_{\mathrm{II},\mathscr D\ne0}`$ is defined by AD38/AD40/AD42/AD43; and $`\mathfrak B_{\mathrm{II},\mathscr D=0}`$ by AD43/AD47–AD50. AD6–AD12 verify the vector, form, internal-connection, and fermionic background equations for every accepted root. The dependence on $`\alpha,g`$ is exact.

This chapter classifies local maximally symmetric zero-fermion AdS$`_5`$ backgrounds only. Every bosonic and fermionic fluctuation remains available for the subsequent analysis.

<a id="7-verified-branches-selected-vacuum-and-global-boundary-prescription"></a>

## Verified branches, selected vacuum, and global boundary prescription

## Selection and scope

Retain the total action and domain

```math
S=S_{2\partial}+\alpha S_{\log},\qquad
\alpha\ne0,\qquad g\ne0,\qquad L\ne0
\tag{SB1}
```

with real couplings and bosonic backgrounds. For the spectrum select the branch-I root that remains finite in the two-derivative limit:

```math
\boxed{
L_*=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
N_*=-\frac32gL_*^2,\qquad
\ell_*^{-2}=\frac12g^2L_*^2.
}
\tag{SB2}
```

Its reality domain is

```math
\boxed{\alpha g^2\le2,\qquad \alpha\ne0,\qquad g\ne0.}
\tag{SB3}
```

No extra sign restriction on $`\alpha`$ is imposed. This selection does not invalidate the other branches. For $`\alpha g^2>2`$ this real branch-I background does not exist, but branch-II candidates retain their own acceptance criteria.

The local background equations and background Killing-spinor conditions were checked. The global prescription is the universal cover of global AdS$`_5`$, fixed sources, and a reflecting boundary with zero symplectic flux. Field-specific asymptotic conditions and renormalized boundary data are additional inputs to a global mode or norm problem; the local operators alone do not determine them.

The action, conventions, field inventory, general Euler equations, and exact branch classification are specified in the [component input](../../action/details/spectrum_input.md), [field inventory](../../action/details/independent_fields.md) and [Euler equations](../../action/details/field_equations.md). No expansion in $`\alpha`$, general auxiliary elimination, or fluctuation truncation is made.

## Substitution into every background equation

With $`k=-\ell_{\mathrm{AdS}}^{-2}<0`$, the class is

```math
\begin{gathered}
R_{\mu\nu\rho\sigma}^{(0)}
=k\bigl(g_{\mu\rho}^{(0)}g_{\nu\sigma}^{(0)}
-g_{\mu\sigma}^{(0)}g_{\nu\rho}^{(0)}\bigr),\\
R_{\mu\nu}^{(0)}=4k\,g_{\mu\nu}^{(0)},\qquad R^{(0)}=20k,\\
L^{(0)}=L_0\ne0,\qquad N^{(0)}=N_0,\qquad
\partial_\mu L_0=\partial_\mu N_0=0,\qquad
L_0^{ij}=\frac{L_0}{\sqrt2}\delta^{ij},\\
G^{(0)}=H_3^{(0)}=P^{(0)}=\mathcal F^{(0)ij}=0,\qquad
V_\mu^{\prime(0)ij}=0,\qquad
\psi_\mu^{(0)i}=\varphi^{(0)i}=0.
\end{gathered}
\tag{SB4}
```

Apply these conditions only after variation. Abbreviating $`L=L_0,N=N_0`$, the three independent scalar coefficients are

```math
\begin{aligned}
\mathcal E_N={}&-\frac{4N}{L}-2gL-4g
+\alpha\left(\frac{10gk}{3}-\frac{g^2N}{3}+\frac{2g^3L^2}{3}\right),\\
\mathcal E_L={}&20k+\frac{2N^2}{L^2}-2gN-\frac32g^2L^2+4g^2L\\
&+\alpha\left(-\frac{10g^2Lk}{3}+\frac{4g^3LN}{3}+\frac{5g^4L^3}{6}\right),\\
\mathfrak E={}&-6Lk+\frac{N^2}{L}+gLN+2gN+\frac14g^2L^3-g^2L^2\\
&+\alpha\left(-\frac{k^2}{3}-gNk+\frac{g^2L^2k}{2}
+\frac{g^2N^2}{12}-\frac{g^3NL^2}{3}-\frac{5g^4L^4}{48}\right).
\end{aligned}
\tag{SB5}
```

The metric and vielbein Euler expressions satisfy

```math
\mathcal E_{\mu\nu}=\mathfrak E g_{\mu\nu},\qquad
\mathcal E_e{}^\rho{}_a=-2e_{\nu a}\mathcal E^{\rho\nu}
\tag{SB6}
```

No additional independent Euler equation is assigned to a dependent connection.

### Common residual identity

Define temporary variables

```math
q:=\alpha g^2,\qquad t:=qL,\qquad
u:=\frac{N}{gL^2}+\frac32.
\tag{SB7}
```

and branch polynomials

```math
\begin{aligned}
\mathscr H(t,u)&:=2u^2+(t-12)u+10,\\
A_q(t,u)&:=
2t^2u^2+t(t-4)(t-6)u+3t^2-24t+24q,\\
B(t,u)&:=
4tu^3+(4t^2+32t)u^2\\
&\quad +(t^3+16t^2-356t+480)u-60t^2+360t-480.
\end{aligned}
\tag{SB8}
```

The polynomial $`\mathscr H`$ differs from the three-form. Each candidate has values

```math
L=\frac tq,\qquad
N=g\left(\frac tq\right)^2\left(u-\frac32\right),\qquad
k=-\frac{g^2}{20}\left(\frac tq\right)^2\mathscr H(t,u)
\tag{SB9}
```

whose direct substitution into SB5 gives the off-equation residuals

```math
\boxed{\begin{aligned}
\mathcal E_N&=-\frac{gL}{6t}A_q(t,u),\\
\mathcal E_L&=\frac{g^2L^2}{6t}A_q(t,u),\\
\mathfrak E&=g^2L^3
\left[\frac{u-2}{12t}A_q(t,u)-\frac{u}{1200}B(t,u)\right].
\end{aligned}}
\tag{SB10}
```

Thus $`A_q=0,uB=0`$ simultaneously solve all three original equations for every candidate, without sampling.

### Branch I

```math
u=0,\qquad
A_q(t,0)=3(t^2-8t+8q)=0
\quad\Longleftrightarrow\quad
qL^2-8L+8=0.
\tag{SB11}
```

Writing $`\mathscr R=\alpha g^2L^2-8L+8`$ in the original variables,

```math
\begin{aligned}
&\left.
(\mathcal E_N,\mathcal E_L,\mathfrak E)
\right|_{N=-3gL^2/2,\ k=-g^2L^2/2}\\
&\hspace{2em}=
\mathscr R\left(-\frac g2,\frac{g^2L}{2},-\frac{g^2L^2}{2}\right)
=(0,0,0)
\qquad(\mathscr R=0).
\end{aligned}
\tag{SB12}
```

This check applies to both real branch-I roots.

### Generic and exceptional parts of branch II

```math
\begin{aligned}
\mathscr D_q(t)&:=t(16q+34t^2+112t-192),\\
\mathscr C_q(t)&:=21t^4-102t^3-72t^2+192t
+8q(t^2+26t-24),\\
P_q(t)&:=
42t^8-78t^7+(1959+16q)t^6\\
&\quad+(-32424+3488q)t^5+(80640-9400q)t^4\\
&\quad+(-53760+59776q+1152q^2)t^3\\
&\quad+(-215040q+35136q^2)t^2
+(184320q-47616q^2)t+1536q^3.
\end{aligned}
\tag{SB13}
```

The verification identities are

```math
\begin{aligned}
t^2B(t,u)
&=(2tu+t^2+26t-24)A_q(t,u)
-3\bigl(\mathscr D_q(t)u+\mathscr C_q(t)\bigr),\\
\mathscr D_q(t)^2
A_q\left(t,-\frac{\mathscr C_q(t)}{\mathscr D_q(t)}\right)
&=4t^2P_q(t).
\end{aligned}
\tag{SB14}
```

On $`\mathscr D_q\ne0`$,

```math
P_q(t)=0,\qquad
u=-\frac{\mathscr C_q(t)}{\mathscr D_q(t)},\qquad u\ne0
\quad\Longrightarrow\quad A_q=B=0
\quad\Longrightarrow\quad\text{SB10}=0.
\tag{SB15}
```

On $`\mathscr D_q=0`$, using $`t\ne0`$,

```math
\begin{gathered}
q=12-7t-\frac{17}{8}t^2,\qquad
\mathscr C_q(t)=
4\bigl(t^4-150t^3-256t^2+1008t-576\bigr)=0,\\
\Delta(t):=t^4-20t^3+532t^2+1056t-1728,\\
u_\pm=\frac{-(t-4)(t-6)\pm\sqrt{\Delta(t)}}{4t}
\end{gathered}
\tag{SB16}
```

Both values solve $`A_q=0`$. Substituting $`\mathscr C_q=\mathscr D_q=A_q=0`$ in SB14 gives

```math
t^2B=0\quad\Longrightarrow\quad B=0
\quad\Longrightarrow\quad\text{SB10}=0.
\tag{SB17}
```

Both roots satisfying reality and AdS conditions are retained; a zero denominator is not a reason to discard a candidate.

### Vectors, forms, internal connections, and fermions

The general form equations are

```math
\begin{aligned}
\mathcal E_B^{\nu\rho}&=-\nabla_\mu Q^{\mu\nu\rho},\\
\mathcal E_C^\nu
&=J_C^\nu-\nabla_\mu\Pi^{\mu\nu}
+\frac12Q^{\nu\mu\rho}G_{\mu\rho}
-\frac12C_\mu\mathcal E_B^{\mu\nu},\\
\mathcal E_E^{\rho\sigma\lambda}
&=\frac g2Q^{\rho\sigma\lambda}
+\frac12\varepsilon^{\mu\nu\rho\sigma\lambda}\nabla_\nu W_\mu.
\end{aligned}
\tag{SB18}
```

The quantities $`\Pi,Q,W,J_C`$ are the action's form responses. On SB4,

```math
\Pi=Q=M=J_C=0,\qquad
W=-2\sqrt2V-4gC,\qquad
dW=-2\sqrt2\,dV-4g\,dC=0.
\tag{SB19}
```

The internal-curvature response $`M`$ yields the common trace/traceless Euler response

```math
\mathcal V^\nu_{ij}
=-\nabla_\mu^{(V)}M^{\mu\nu}_{ij}
+(4L-\alpha g^2L^2)V'{}^\nu_{ij}
-2\sqrt2P^\nu\delta_{ij}
=0
\tag{SB20}
```

where $`\nabla^{(V)}`$ is bosonic Levi–Civita plus internal connection. Hence

```math
\boxed{
\mathcal E_C=\mathcal E_{B_2}=\mathcal E_{E_3}
=\mathcal E_V=\mathcal E_{V'}=0.
}
\tag{SB21}
```

For the background-zero fermions $`\Phi_F=(\psi_\mu^i,\varphi^i)`$,

```math
S=S_0+S_2+O(\Phi_F^4),\qquad
\frac{\delta S_2}{\delta\Phi_F}=O(\Phi_F),\qquad
\frac{\delta O(\Phi_F^4)}{\delta\Phi_F}=O(\Phi_F^3).
\tag{SB22}
```

so, after variation,

```math
\boxed{
\left.\mathcal E_{\psi_\mu^i}\right|_{\Phi_F=0}
=\left.\mathcal E_{\varphi^i}\right|_{\Phi_F=0}=0.
}
\tag{SB23}
```

This argument includes all implicit fermions in supercovariants and dependent connections. Fermionic fluctuations are not set to zero.

## Reality, regularity, and exceptional loci

Every branch must satisfy

```math
\boxed{
q\in\mathbb R\setminus\{0\},\qquad
t,u\in\mathbb R,\qquad t\ne0,\qquad
\mathscr H(t,u)>0.
}
\tag{SB24}
```

The exceptional denominator branch also requires $`\Delta(t)\ge0`$. In the generic branch,

```math
P_q(0)=1536q^3\ne0
\tag{SB25}
```

which excludes $`t=0`$. The exceptional quartic likewise has nonzero constant term.

At finite admitted couplings and roots, $`L=t/q\ne0`$, $`N`$, and $`k`$ are finite. The geometric invariants are

```math
R=20k,\qquad
R_{\mu\nu}R^{\mu\nu}=80k^2,\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=40k^2.
\tag{SB26}
```

A repeated root or $`\mathscr D_q=0`$ does not itself imply a geometric singularity. Negative-$`L`$ candidates are not excluded merely by their sign.

### Regularity of the selected root

Put $`s=\sqrt{1-\alpha g^2/2}\ge0`$. Then

```math
L_*=\frac2{1+s}>0,\qquad
N_*=-\frac{6g}{(1+s)^2},\qquad
\ell_*^{-2}=\frac{2g^2}{(1+s)^2}.
\tag{SB27}
```

The denominator $`1+s`$ is strictly positive at finite admitted couplings. The selected root is obtained from the original pair as

```math
\begin{aligned}
L_{0,-}
&=\frac4{\alpha g^2}\left(1-\sqrt{1-\alpha g^2/2}\right)\\
&=\frac4{\alpha g^2}
\frac{1-(1-\alpha g^2/2)}{1+\sqrt{1-\alpha g^2/2}}
=\frac2{1+\sqrt{1-\alpha g^2/2}}
=L_*
\end{aligned}
\tag{SB28}
```

Its selection criterion is

```math
\lim_{\alpha\to0}L_*=1
\tag{SB29}
```

This limit labels a root after solving the full equations; it is not a perturbative construction from the two-derivative vacuum. Positivity of the selected $`L_*`$ is a consequence, not an assumption imposed on all candidates.

### Algebraic Jacobian

Define $`Y=N/g`$, $`Z=k/g^2`$, and the equation vector

```math
\mathbf F:=
\left(\mathcal E_N/g,\ \mathcal E_L/g^2,\ \mathfrak E/g^2\right)
\tag{SB30}
```

Differentiate at fixed $`q=\alpha g^2`$, then rewrite $`t=qL`$. On branch I,

```math
\left.\frac{\partial\mathbf F}{\partial(L,Y,Z)}\right|_{\mathrm I}
=
\begin{pmatrix}
\frac{4t}{3}-8&-\frac{12+t}{3L}&\frac{10t}{3L}\\
4-12L+\frac{13tL}{6}&\frac{4t}{3}-8&20-\frac{10t}{3}\\
-2L+\frac{tL^2}{12}&2-2L-\frac{tL}{12}&L(-6+\frac{7t}{3})
\end{pmatrix}.
\tag{SB31}
```

The branch equation gives

```math
(t-8)L+8=0\quad\Longrightarrow\quad L=\frac8{8-t}
\tag{SB32}
```

Finite $`L`$ excludes $`t=8`$. Substitution into SB31 yields

```math
\boxed{
\det\frac{\partial\mathbf F}{\partial(L,Y,Z)}
=-\frac{8(t-4)^2(t-2)}{t-8}.
}
\tag{SB33}
```

Using $`t=4(1-s)`$ and $`q=t(8-t)/8`$, the special points are

| $`\alpha g^2`$ | Feature on the selected branch |
|---|---|
| $`3/2`$ | $`t=2`$: merger with branch II; singular background Jacobian |
| $`2`$ | $`t=4`$: merger of the two branch-I roots; singular background Jacobian |
| $`-30`$ | $`t=-12`$: $`N`$ equation: $`4/L+\alpha g^2/3`$ coefficient vanishes |

The last condition follows directly from

```math
\frac4L+\frac{\alpha g^2}{3}
=\frac{12+t}{3L}=0
\quad\Longrightarrow\quad
t=-12,\qquad q=\frac{t(8-t)}8=-30
\tag{SB34}
```

These values are derived, not chosen samples.

All three backgrounds are finite. A singular background Jacobian alone proves neither a propagating zero mode nor kinetic degeneracy or stability. The fluctuation operators below decide those questions; the points remain in the solution domain.

## Preserved background supersymmetry

The transformation inputs are [01_shared_component_relations.md](../../action/details/component_construction/results/gauged_full_fermionic_log/sources/reference_fragments/01_shared_component_relations.md) in the LOG reference fragments, source compensation rules (4.12)–(4.14), and the [common conventions](../../../CONVENTIONS.md) and [gauge-compensation derivation](../../../common/details/gauge_compensations.md). The following applies those supplied rules in common conventions.

### Linear-multiplet fermion

On zero flux and constant scalars, the compensating $`S`$ parameter and fermion variation are

```math
\eta^i=-\frac g2L_0^{ij}\epsilon_j,\qquad
\delta\varphi^i=\frac12N_0\epsilon^i+3L_0^{ij}\eta_j.
\tag{SB35}
```

The NW–SE lowering rule is

```math
\eta_j=-\frac g2L_0^{k\ell}\epsilon_\ell\epsilon_{kj},
\qquad
\epsilon_\ell=\epsilon^m\epsilon_{m\ell}.
\tag{SB36}
```

For $`L_0^{ij}=L_0\delta^{ij}/\sqrt2`$,

```math
L_0^{ij}L_0^{k\ell}\epsilon_{m\ell}\epsilon_{kj}
=\frac{L_0^2}{2}\delta^{ij}\delta^{k\ell}
\epsilon_{m\ell}\epsilon_{kj}
=-\frac{L_0^2}{2}\delta^i{}_m.
\tag{SB37}
```

and consequently

```math
\begin{aligned}
3L_0^{ij}\eta_j
&=-\frac{3g}{2}
L_0^{ij}L_0^{k\ell}\epsilon_{m\ell}\epsilon_{kj}\epsilon^m
=\frac{3gL_0^2}{4}\epsilon^i,\\
\boxed{\delta\varphi^i}
&\boxed{=
\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon^i
=\frac{gL_0^2u}{2}\epsilon^i.}
\end{aligned}
\tag{SB38}
```

Branch II has $`gL_0^2u\ne0`$, so $`\delta\varphi=0`$ requires $`\epsilon=0`$. Its coefficient is the spinor identity and admits no half-SUSY projector.

On branch I, $`u=0`$ makes this variation vanish for every $`\epsilon`$.

### Gravitino and integrability

Define the internal matrix

```math
\mathsf J^i{}_j:=\delta^{ik}\epsilon_{jk},
\qquad
\mathsf J^2=-\mathbf1
\tag{SB39}
```

On $`T=b_\mu=0`$, the gravitino variation is

```math
\begin{aligned}
0=\delta\psi_\mu^i
&=\nabla_\mu\epsilon^i
-\frac12V_\mu\delta^{ij}\epsilon_j-i\gamma_\mu\eta^i,\\
0=\mathscr D_\mu\epsilon,\qquad
\mathscr D_\mu
&:=\nabla_\mu-\frac12V_\mu\mathsf J
+\frac{igL_0}{2\sqrt2}\gamma_\mu\mathsf J.
\end{aligned}
\tag{SB40}
```

Using $`dV=0`$, constant $`L_0`$, $`\nabla_\mu\gamma_\nu=0`$, and $`\mathsf J^2=-\mathbf1`$,

```math
\begin{aligned}
[\mathscr D_\mu,\mathscr D_\nu]\epsilon
&=\left[
\frac14R_{\mu\nu}{}^{ab}\gamma_{ab}
+\left(\frac{igL_0}{2\sqrt2}\right)^2
\mathsf J^2[\gamma_\mu,\gamma_\nu]
\right]\epsilon\\
&=\left[
\frac k2+\left(-\frac{g^2L_0^2}{8}\right)(-1)\,2
\right]\gamma_{\mu\nu}\epsilon\\
&=\left(\frac k2+\frac{g^2L_0^2}{4}\right)
\gamma_{\mu\nu}\epsilon.
\end{aligned}
\tag{SB41}
```

Branch I obeys $`k=-g^2L_0^2/2`$, so the Killing-spinor connection is flat. There is no algebraic projection on its eight real symplectic-Majorana initial components:

```math
\boxed{\text{Branch I locally preserves eight real supersymmetries.}}
\tag{SB42}
```

Bosonic SUSY variations contain a dynamical fermion and vanish on the background. Traceless internal and $`K`$ compensations also vanish there. Dependent composites add no independent Killing-spinor equations.

The chosen universal cover has no flat-holonomy obstruction, so these solutions extend to global background Killing spinors. This neither proves closure of the full fluctuation boundary conditions under SUSY nor supplies a complete nonlinear invariance check.

## Preserved gauge symmetries

Distinguish local gauge redundancies from the stabilizer of a fixed potential representative.

The form transformations are

```math
\delta C=d\Lambda,\qquad
\delta B_2=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2,\qquad
\delta E_3=d\Lambda_2
\tag{SB43}
```

and on $`G=0`$, with residual $`\delta V=d\beta`$,

```math
\delta C=d\Lambda,\qquad
\delta V=d\beta,\qquad
\delta B_2=d\Lambda_1-\frac g2\Lambda_2,\qquad
\delta E_3=d\Lambda_2.
\tag{SB44}
```

They preserve the vanishing covariant strengths. Parameters preserving a fixed potential representative additionally obey

```math
d\Lambda=d\beta=0,\qquad
d\Lambda_2=0,\qquad
d\Lambda_1=\frac g2\Lambda_2
\tag{SB45}
```

The nonzero triplet orientation leaves residual internal $`U(1)`$:

```math
\lambda^{ij}=\frac{\beta}{2}\delta^{ij}
\quad\Longrightarrow\quad
\delta_U L_0^{ij}
=-2\lambda^{(i}{}_kL_0^{j)k}=0.
\tag{SB46}
```

The gauge parameter $`\lambda^{ij}`$ has no relation to the action coupling $`\alpha`$.

Local Lorentz and diffeomorphism redundancies remain. The geometric stabilizer solves

```math
\nabla_{(\mu}\xi_{\nu)}=0
\tag{SB47}
```

and has fifteen AdS Killing vectors. The Abelian $`C`$ symmetry and form hierarchy remain. This symmetry count alone does not identify the massless vector combinations.

## Global AdS$`_5`$ and the selected boundary prescription

The boundary prescription fixes sources and imposes a reflecting boundary on global AdS$`_5`$.

### Global geometry

The metric on the universal cover is

```math
\boxed{
ds^2=\frac1{\cos^2\rho}
\left[-dt^2+\ell_*^2
\left(d\rho^2+\sin^2\rho\,d\Omega_3^2\right)\right],
\quad
t\in\mathbb R,\quad 0\le\rho<\frac\pi2.
}
\tag{SB48}
```

Here $`t`$ is global time, distinct from the earlier algebraic $`t=qL`$. The radius retains its exact coupling dependence.

In embedding coordinates with $`a=1,\ldots,4`$ and $`n^an^a=1`$,

```math
X^{-1}=\ell_*\sec\rho\cos(t/\ell_*),\qquad
X^0=\ell_*\sec\rho\sin(t/\ell_*),\qquad
X^a=\ell_*\tan\rho\,n^a
\tag{SB49}
```

the induced metric follows from

```math
\begin{aligned}
-(X^{-1})^2-(X^0)^2+X^aX^a
&=-\ell_*^2\sec^2\rho+\ell_*^2\tan^2\rho
=-\ell_*^2,\\
-(dX^{-1})^2-(dX^0)^2+dX^adX^a
&=-\sec^2\rho\,dt^2
+\ell_*^2\sec^2\rho\,d\rho^2
+\ell_*^2\tan^2\rho\,d\Omega_3^2.
\end{aligned}
\tag{SB50}
```

Time is unwrapped, with no periodic identification. Setting $`z=\cos\rho`$, the boundary conformal representative is

```math
\gamma^{(0)}
=\left.\lim_{z\to0}z^2g\right|_{\text{tangent to the boundary}}
=-dt^2+\ell_*^2d\Omega_3^2.
\tag{SB51}
```

No quotient or flat holonomy is added. The spin structure is the smooth one on the universal cover.

### Center and boundary conditions

Require smooth tensors and spinors in a regular local frame at $`\rho=0`$. Fix the boundary metric and source components of every independent radial canonical pair. Fermion sources vanish, but bulk fermions and responses remain. Require zero boundary flux for the finite symplectic structure of the total theory.

Let $`J^A`$ be sources and $`\Pi_A`$ their conjugate responses, including the overall action prefactor. The specified variational form is

```math
\left.\delta S_{\mathrm{ren}}\right|_{\mathrm{EOM}=0}
=\int_{\partial M}\Pi_A\,\delta J^A,
\qquad
\boxed{\delta J^A=0.}
\tag{SB52}
```

For fermions only the appropriate canonical polarization is fixed, not every spinor component simultaneously. Additional higher-derivative radial canonical pairs cannot be omitted. This background analysis does not derive the explicit $`J^A,\Pi_A`$ for every field.

For all fields $`\Phi`$, even test variations $`\delta_1,\delta_2`$, and renormalized boundary potential $`\Theta_{\mathrm{ren}}`$, define

```math
\omega_{\mathrm{ren}}
=\delta_1\Theta_{\mathrm{ren}}(\delta_2\Phi)
-\delta_2\Theta_{\mathrm{ren}}(\delta_1\Phi).
\tag{SB53}
```

On the background and linear equations,

```math
\begin{aligned}
d\omega_{\mathrm{ren}}&=0,\\
\Omega_{\Sigma_2}-\Omega_{\Sigma_1}
&=-\int_{\mathscr I_{12}}\omega_{\mathrm{ren}},\\
\left.\omega_{\mathrm{ren}}\right|_{\mathscr I}
&=\delta_1\Pi_A\,\delta_2J^A
-\delta_2\Pi_A\,\delta_1J^A=0
\qquad(\delta_1J^A=\delta_2J^A=0).
\end{aligned}
\tag{SB54}
```

Here $`\Omega_\Sigma=\int_\Sigma\omega_{\mathrm{ren}}`$ is the pairing on two variations, and $`\mathscr I_{12}`$ is the intervening conformal boundary. Finiteness is required; positivity is not assumed.

SB52–SB54 state the specified variational boundary prescription. They are not a completed derivation of this theory's counterterms, canonical sources, or finite symplectic coefficients.

The separation between bulk equations and admissible boundary conditions is discussed in [Ishibashi–Wald](https://arxiv.org/abs/hep-th/0402184). Counterterm contributions to symplectic structure are discussed in [Compère–Marolf](https://arxiv.org/abs/0805.1902). The LOG-specific boundary coefficients depend on its quadratic operators and the chosen boundary action.

## Scope of the background analysis

| Topic | Status |
|---|---|
| Substitution of every candidate into all independent bosonic background equations | Symbolic verification SB10–SB21 |
| Fermionic Euler equations at zero fermions | Satisfied by SB22–SB23 |
| Reality, $`L\ne0`$ field domain, and geometric regularity | SB24–SB29; exceptional branches retained |
| Known exceptional algebraic parameter loci | SB33–SB34; no branch lost through division |
| Preserved background SUSY | Branch I: eight real supersymmetries; branch II: none |
| Gauge redundancies and background stabilizer | Distinguished in SB43–SB47 |
| Spectrum branch | The exact SB2 root with $`\alpha,g`$ dependence is selected |
| Global geometry and boundary choice | Universal-cover global AdS$`_5`$; fixed sources and zero symplectic flux |
| Explicit source/response combinations and falloff exponents for every field | Outside the results derived in this background analysis |
| Closure of the full fluctuation boundary conditions under eight supersymmetries | Not demonstrated |

The [quadratic action](../quadratic_action.md), (Q31)–(Q40), (Q57), and [physical operators](physical_operators.md) provide the coupled AdS5 system with its stated check scope. These background-specific expressions do not establish all general-background fermion blocks or all canonical boundary pairs. Two-fermion action order remains sufficient throughout.

Repeated indicial roots do not justify automatically discarding logarithmic modes. Background zero-flux conditions are never imposed on fluctuations.

The selected spectrum background is SB2, with eight preserved background supersymmetries. The fixed-source boundary prescription does not by itself establish all field-specific boundary data or a complete global boundary problem.

