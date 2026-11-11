# Physical operators and eigenfields

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="10-physical-operator-decomposition"></a>

## Physical operator decomposition

On the selected branch,

```math
L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
N_0=-\frac32gL_0^2,\qquad
k=-\frac12g^2L_0^2,
```

```math
\alpha g^2L_0^2=8(L_0-1),\qquad
0<L_0\le2,\qquad L_0\ne1.
\tag{O-1}
```

The decomposition is performed on the coupled Euler system of the quadratic action; the off-shell action retains all fields.

Define the differential operators

```math
\mathfrak T_2:=\bar\Box-2k,\qquad
\mathfrak M_p:=d\,\mathrm{div}+\mathrm{div}\,d
              =\bar\Box-p(5-p)k
\tag{O-2}
```

where the second acts on $`p`$-forms. In particular,

```math
\mathrm{div}\,A=0
\ \Longrightarrow\
(\mathfrak M_1A)_\mu=\bar\nabla^\nu(dA)_{\nu\mu},
```

```math
dH_c=0
\ \Longrightarrow\
\mathfrak M_3H_c=d\,\mathrm{div}\,H_c.
\tag{O-3}
```

For fermions use temporarily

```math
D:=\gamma^a\bar\nabla_a,\qquad
M^2=-\frac{L_0^2}{2},\qquad
t:=igM,\qquad
t^2=-k=\frac{g^2L_0^2}{2},\qquad
J:=t^{-1}D
\tag{O-4}
```

The inverse $`t^{-1}=2t/(g^2L_0^2)`$ is an algebraic internal matrix, not an inverse differential operator.

## Metric and scalar mixing

Initially retain

```math
r:=\delta R,\qquad l:=\delta L,\qquad n:=\delta N
```

The scalar system from the quadratic action is

```math
\begin{pmatrix}
\frac{\alpha}{12}\bar\Box+\frac32B_0-\frac{\alpha k}{3}
&-4A(\bar\Box+5k)&-4b(\bar\Box+5k)\\
A&-2Z\bar\Box+C&D_s\\
b&D_s&-F
\end{pmatrix}
\begin{pmatrix}r\\l\\n\end{pmatrix}=0,
\tag{O-5}
```

```math
\begin{aligned}
B_0&=L_0-\frac{\alpha g^2L_0^2}{2}=4-3L_0,
&
A&=1-\frac{\alpha g^2L_0}{6},
&
b&=\frac{\alpha g}{6},\\
Z&=\frac1{L_0}-\frac{\alpha g^2}{4},
&
C&=4g^2-12g^2L_0+\frac{13\alpha g^4L_0^2}{6},\\
D_s&=-8g+\frac{4\alpha g^3L_0}{3},
&
F&=\frac4{L_0}+\frac{\alpha g^2}{3}.
\end{aligned}
\tag{O-6}
```

Define the two combinations

```math
\phi_0:=\frac ng+\frac32L_0l,\qquad
\phi_M:=\frac ng+2L_0l.
\tag{O-7}
```

with inverse

```math
l=\frac2{L_0}(\phi_M-\phi_0),\qquad
n=g(4\phi_0-3\phi_M)
\tag{O-8}
```

Substitution in the $`n`$ equation and use of the branch relation give

```math
r=g^2\left[
24\phi_0-\frac{19L_0-22}{L_0-1}\phi_M
\right]
\tag{O-9}
```

No division by $`F`$ occurs; the point $`F=0,L_0=2/5`$ is retained.

Temporarily set

```math
\mu:=\frac{6(4-3L_0)}{\alpha},\qquad
X_0:=(\bar\Box-4k)\phi_0,\qquad
X_M:=(\bar\Box-\mu)\phi_M
\tag{O-10}
```

Direct substitution into the coupled equations yields

```math
E_{\rm tr}=\frac{L_0-2}{L_0^2}(-8X_0+6X_M),\qquad
E_l=\frac{4(L_0-2)}{L_0^3}(-X_0+X_M),\qquad E_n=0.
\tag{O-11}
```

and hence

```math
\begin{aligned}
E_{\rm tr}-\frac32L_0E_l
   &=-\frac{2(L_0-2)}{L_0^2}X_0,\\
E_{\rm tr}-2L_0E_l
   &=-\frac{2(L_0-2)}{L_0^2}X_M.
\end{aligned}
```

For $`L_0\ne2`$, the two physical scalar operators are

```math
\boxed{
(\bar\Box+2g^2L_0^2)\phi_0=0,\qquad
\left[\bar\Box-\frac{6(4-3L_0)}{\alpha}\right]\phi_M=0.
}
\tag{O-12}
```

Their metric contributions must also remain. On solutions choose

```math
h_{\mu\nu}^{S}
=\frac{\bar g_{\mu\nu}}{L_0^2}
 \left(\frac43\phi_0-\phi_M\right)
\tag{O-13}
```

Indeed, for $`h_{\mu\nu}^{S}=\bar g_{\mu\nu}f`$,

```math
r[h^S]=-4(\bar\Box+5k)f
=g^2\left[
24\phi_0-\frac{19L_0-22}{L_0-1}\phi_M
\right].
```

The scalar part of the full metric equation is

```math
E^S_{h,\mu\nu}
=(\bar\nabla_\mu\bar\nabla_\nu
-\bar g_{\mu\nu}\bar\Box-4k\bar g_{\mu\nu})
\left[
\left(\frac{\alpha}{12}(\bar\Box-4k)+\frac32B_0\right)f+a_1
\right],
\tag{O-14}
```

```math
a_1=
\frac{2(3L_0-4)}{L_0^2}\phi_0+
\frac{2(10-7L_0)}{3L_0^2}\phi_M.
```

The two bracket coefficients separately become

```math
\frac{2B_0+2(3L_0-4)}{L_0^2}=0,
```

```math
-\frac{\alpha(\mu-4k)}{12L_0^2}
-\frac{3B_0}{2L_0^2}
+\frac{2(10-7L_0)}{3L_0^2}=0
\tag{O-15}
```

Thus the mixing is resolved using the full metric equation, not merely its trace.

The remaining metric representative is

```math
h_{\mu\nu}=h_{\mu\nu}^{TT}+h_{\mu\nu}^{S}
             +2\bar\nabla_{(\mu}\xi_{\nu)},\qquad
\bar\nabla^\mu h_{\mu\nu}^{TT}=0,\qquad h^{TT}=0
\tag{O-16}
```

The antisymmetric vielbein is a Lorentz gauge direction. The TT equation is

```math
\boxed{
-\frac{\alpha}{12}\,
\mathfrak T_2
\left[\mathfrak T_2-\frac{6(4-3L_0)}{\alpha}\right]
h_{\mu\nu}^{TT}=0.
}
\tag{O-17}
```

When $`\mu\ne0`$, define

```math
h_M=\frac{\mathfrak T_2}{\mu}h^{TT},\qquad
h_0=h^{TT}-h_M
```

which obey

```math
(\mathfrak T_2-\mu)h_M=0,\qquad \mathfrak T_2h_0=0.
\tag{O-18}
```

The scalar representative contains no inverse $`\bar\Box+5k`$, so it remains valid at $`L_0=22/19`$, where $`\mu=-5k`$. There $`r[\phi_M]=0`$ does not mean that $`\phi_M`$ disappears.

## Vector and form mixing

Retain the starting variables

```math
\mathcal G=dc,\qquad
\mathcal H=db+\frac12\bar C\wedge dc+\frac g2e_3,
```

```math
p^\mu=-\frac1{6g}\varepsilon^{\mu\nu\rho\sigma\lambda}
              \bar\nabla_\nu\mathcal H_{\rho\sigma\lambda},
\qquad \bar\nabla_\mu p^\mu=0
\tag{O-19}
```

including the term $`ge_3/2`$.

Use the local representation decomposition

```math
\mathcal H^{abc}
=H_c^{abc}+\varepsilon^{deabc}(da)_{de},
\qquad dH_c=0
\tag{O-20}
```

The field $`a`$ represents the co-closed part of the three-form and is not a new independent field. Epsilon contraction gives

```math
p=-\frac2g\,\mathfrak M_1a,\qquad
q_{ab}:=\bar\nabla^c\mathcal H_{cab}
       =(\mathrm{div}\,H_c)_{ab}
\tag{O-21}
```

Keep harmonic intersections separately; the undifferentiated form equation below also constrains them.

The closed three-form part has action

```math
\ell[H_c]=\frac{L_0-4}{9}H_c^2
                 -\frac{\alpha}{6}(\mathrm{div}\,H_c)^2.
```

Variation and integration by parts give

```math
\delta\ell\simeq_\partial
\left[
\frac{2(L_0-4)}9H_c+\frac{\alpha}{9}
d\,\mathrm{div}\,H_c
\right]\cdot\delta H_c
```

and therefore

```math
\boxed{
dH_c=0,\qquad
\left[\mathfrak M_3-\frac{2(4-L_0)}{\alpha}\right]H_c=0.
}
\tag{O-22}
```

For the remaining $`(c,v,a)`$ mixing, let $`x`$ represent $`\mathfrak M_1`$ algebraically:

```math
K_V(x)=
\begin{pmatrix}
A_G+\alpha x/12&D_{cv}/2&(D_c-\alpha x/3)/2\\
D_{cv}/2&\alpha/12&D_v/2\\
(D_c-\alpha x/3)/2&D_v/2&A_U-2P_cx/g^2
\end{pmatrix},
\tag{O-23}
```

```math
\begin{aligned}
A_G&=-\frac{L_0}{2}+\frac{5\alpha g^2L_0^2}{24},
&
A_U&=4L_0-\frac{2\alpha g^2L_0^2}{3},\\
D_c&=\frac{\alpha g^2L_0^2}{6}-4,
&
D_v&=\frac{2\alpha gL_0}{3\sqrt2}-\frac{2\sqrt2}{g},\\
D_{cv}&=\frac{\alpha gL_0}{6\sqrt2},
&
P_c&=-\frac2{L_0}+\frac{\alpha g^2}{3}.
\end{aligned}
\tag{O-24}
```

On transverse representatives the physical system is

```math
\boxed{
\left.
\begin{pmatrix}x&0&0\\0&x&0\\0&0&1\end{pmatrix}
K_V(x)
\begin{pmatrix}c\\v\\a\end{pmatrix}
\right|_{x=\mathfrak M_1}=0.
}
\tag{O-25}
```

The final row is the undifferentiated three-form equation. Multiplying it by $`x`$ would introduce spurious Maxwell solutions; the physical operator is not read from $`\det[xK_V]`$.

Using the branch relation, the determinant factorizes as

```math
\det K_V(x)=-\frac{L_0-2}{9L_0^6g^6}P_V(x),
```

```math
\begin{aligned}
P_V(x)={}&16(L_0-1)^2x^2\\
&+8L_0^2g^2(L_0-1)(L_0-4)x\\
&+3L_0^4g^4(L_0-4)(3L_0-4)
\end{aligned}
\tag{O-26}
```

Its two roots are

```math
\boxed{
\lambda_\pm=\frac{g^2L_0^2}{2}
\left[
\frac{4-L_0}{2(L_0-1)}
\pm\sqrt{\frac{2(4-L_0)}{L_0-1}}
\right].
}
\tag{O-27}
```

The mixed eigenvectors are

```math
\begin{aligned}
C_\lambda&=4(4-L_0)+2\alpha\lambda,\\
A_\lambda&=2(5L_0-8)+\alpha\lambda,\\
V_\lambda&=-\frac{gL_0}{\sqrt2}C_\lambda
-\frac{gL_0(L_0-4)}{\sqrt2(L_0-1)}A_\lambda
\end{aligned}
\tag{O-28}
```

and direct multiplication yields

```math
K_V(x)
\begin{pmatrix}C_x\\V_x\\A_x\end{pmatrix}
=
\begin{pmatrix}
0\\0\\
-\dfrac{2(L_0-2)}{L_0^4g^4(L_0-1)}P_V(x)
\end{pmatrix}
\tag{O-29}
```

so no vector–form mixing has been omitted.

For $`L_0\ne2,4/3`$, define

```math
p_\pm=
\frac{\mathfrak M_1-\lambda_\mp}{\lambda_\pm-\lambda_\mp}p,
\qquad
a_\pm=-\frac{g}{2\lambda_\pm}p_\pm,
```

```math
c_\pm=\frac{C_{\lambda_\pm}}{A_{\lambda_\pm}}a_\pm,
\qquad
v_\pm=\frac{V_{\lambda_\pm}}{A_{\lambda_\pm}}a_\pm.
\tag{O-30}
```

These satisfy

```math
(\mathfrak M_1-\lambda_\pm)p_\pm=0,\qquad
\mathrm{div}\,p_\pm=0
\tag{O-31}
```

the separated equations.

After subtracting the massive pieces, the residual $`c_0,v_0,a_0`$ obey

```math
\boxed{
\mathfrak M_1c_0=0,\qquad
\mathfrak M_1v_0=0,\qquad
a_0=\frac12c_0+\frac{v_0}{2\sqrt2\,gL_0}.
}
\tag{O-32}
```

There are two Maxwell and two massive-vector channels. The variable $`a_0`$ is not a third Maxwell channel.

The two traceless connection components obey

```math
-\frac{2\alpha}{3}\mathfrak M_1w^{ij}
+\left(4L_0-\alpha g^2L_0^2\right)w^{ij}=0.
```

and the branch relation gives

```math
\boxed{
\left[\mathfrak M_1-\frac{6(2-L_0)}{\alpha}\right]w^{ij}=0,
\qquad \mathrm{div}\,w^{ij}=0
}
\tag{O-33}
```

with the divergence constraint valid for $`L_0\ne2`$.

## Gravitino and spinor mixing

Neither $`\gamma\cdot\Psi=0`$ nor $`\zeta=0`$ is imposed before solving the mixing. Define

```math
U:=\gamma^a\Psi_a,\qquad
d_\Psi:=\bar\nabla^a\Psi_a,\qquad
R_F:=d_\Psi-(D-2t)U
\tag{O-34}
```

the trace variables as displayed.

The local SUSY direction is

```math
\delta_Q\Psi_a=\left(\bar\nabla_a+\frac t2\gamma_a\right)\epsilon,
\qquad \delta_Q\zeta=0
\tag{O-35}
```

under which

```math
\delta_QU=(D+5t/2)\epsilon,
```

```math
\delta_Qd_\Psi=(D-2t)(D+5t/2)\epsilon
\quad\Longrightarrow\quad
\delta_QR_F=0.
\tag{O-36}
```

The curvature contribution used here is

```math
D^2\epsilon=(\bar\Box-5k)\epsilon
```

so derivatives are not treated as commuting flat-space operators.

On the spin-half representative $`\Psi_a=\gamma_a u`$,

```math
U=5u,\qquad d_\Psi=Du,\qquad
R_F=-4(D-5t/2)u.
\tag{O-37}
```

the coupled equations are

```math
E_\Psi^a=
\bigl[\bar\nabla^a-\gamma^a(D-2t)\bigr](A_Fu+B_F\zeta),
\qquad
E_\zeta=C_Fu+H_F\zeta,
\tag{O-38}
```

```math
\begin{aligned}
A_F={}&6L_0+
\alpha\left(\frac{D^2}{3}-tD-\frac{31g^2L_0^2}{24}\right),\\
B_F={}&-\frac{4t}{gL_0}
+\alpha g\left(\frac D3+\frac{5t}{6}\right),\\
C_F={}&10g(L_0+1)-\frac{16tD}{gL_0}
+\alpha g\left(\frac{4D^2}{3}-\frac{35g^2L_0^2}{12}\right),\\
H_F={}&\left(\frac4{L_0}+\frac{\alpha g^2}{3}\right)D
+t\left(-\frac{14}{L_0}+\frac{17\alpha g^2}{6}\right).
\end{aligned}
\tag{O-39}
```

The branch relation implies

```math
C_F=4B_F(D-5t/2).
\tag{O-40}
```

and hence the gauge-invariant trace equations are

```math
\gamma_aE_\Psi^a=A_FR_F-4(D-5t/2)B_F\zeta,
\qquad
E_\zeta=-B_FR_F+H_F\zeta
\tag{O-41}
```

In particular, replacing the full spinor equation by $`E_\zeta=H_F\zeta`$ would be incorrect.

The propagating block uses the constraint $`T=A_Fu+B_F\zeta=0`$. The remaining allowed kernel is

```math
\bar\nabla_aT=\frac t2\gamma_aT
\tag{O-42}
```

a Killing-spinor sector, retained separately for global considerations and not counted as local propagating modes.

Set $`y=gt^{-1}\zeta,z=J`$ and normalize the two equations by nonzero algebraic factors:

```math
\begin{pmatrix}
\mathcal A&\mathcal B\\
\mathcal C&\mathcal H
\end{pmatrix}
\begin{pmatrix}u\\y\end{pmatrix}=0,
\tag{O-43}
```

```math
\begin{aligned}
\mathcal A&=4(L_0-1)z^2-12(L_0-1)z+31-13L_0,\\
\mathcal B&=4(L_0-1)z+4L_0-10,\\
\mathcal C&=16(L_0-1)z^2-24L_0z+100-40L_0,\\
\mathcal H&=(10L_0-4)z+13L_0-34.
\end{aligned}
\tag{O-44}
```

The diagonalizing transformation is

```math
\chi:=y-4u,\qquad \rho:=y-3u,
\qquad u=\rho-\chi,\qquad y=4\rho-3\chi
\tag{O-45}
```

Writing the rows as $`E_1,E_2`$,

```math
E_2-4E_1=-3(L_0-2)(2z+1)\chi,
```

```math
E_1=P_{1/2}(z)\rho
-(L_0-1)(2z-1)(2z+1)\chi,
```

```math
P_{1/2}(z):=4(L_0-1)(z^2+z)+3L_0-9.
\tag{O-46}
```

for $`L_0\ne2`$ one obtains

```math
\boxed{
(D+t/2)\chi=0,\qquad
P_{1/2}(J)\rho=0.
}
\tag{O-47}
```

No inverse Dirac operator is needed. Indeed,

```math
P_{1/2}(-1/2)=2(L_0-4)
```

and the separated equations imply

```math
\chi=\frac{g}{6(4-L_0)}t^{-1}P_{1/2}(J)\zeta,
\qquad
\rho=\frac14\left(gt^{-1}\zeta+3\chi\right).
\tag{O-48}
```

For the remaining gravitino, the vanishing residual $`R_F`$ follows from the polynomial identity

```math
\mathcal A=
\left[z+\frac{11-8L_0}{2(L_0-1)}\right]\mathcal B
+\frac{3(L_0-4)(L_0-2)}{L_0-1}.
\tag{O-49}
```

The last term is nonzero on the selected generic branch. If both $`\mathcal A`$ and $`\mathcal B`$ annihilate $`R_F`$, then $`R_F=0`$.

The local gauge quotient therefore has representative

```math
\boxed{
\begin{aligned}
\Psi_a&=\Psi_a^{TT}+\gamma_a(\rho-\chi)
+\left(\bar\nabla_a+\frac t2\gamma_a\right)\epsilon,\\
\zeta&=\frac tg(4\rho-3\chi),\\
\gamma^a\Psi_a^{TT}&=0,\qquad
\bar\nabla^a\Psi_a^{TT}=0.
\end{aligned}}
\tag{O-50}
```

The spin-three-halves/spin-half separation follows from the mixed constraints, not from deleting the mixing.

TT projection annihilates $`\bar\nabla_a\zeta`$ and $`\gamma_a\zeta`$. With $`D^2=\bar\Box-6k`$ on TT vector-spinors, the operator becomes

```math
\begin{aligned}
P_{3/2}(D)
={}&\frac{\alpha}{3}D^3+\frac{\alpha t}{6}D^2
+\left(L_0-3-\frac{\alpha t^2}{2}\right)D
+\frac32(L_0-3)t\\
={}&(D+3t/2)
\left[\frac{\alpha}{3}(D^2-tD)+L_0-3\right].
\end{aligned}
\tag{O-51}
```

Define temporarily

```math
\Delta^2:=\frac{2(4-L_0)}{L_0-1}
```

The two factorizations are

```math
P_{3/2}(D)=\frac{\alpha}{3}
(D+3t/2)
\left[D-\frac{1+\Delta}{2}t\right]
\left[D-\frac{1-\Delta}{2}t\right],
```

```math
P_{1/2}(J)=4(L_0-1)
\left[J-\frac{-1+\Delta}{2}\right]
\left[J-\frac{-1-\Delta}{2}\right]
\tag{O-52}
```

For distinct roots the projectors are polynomials:

```math
\rho_\pm=
\frac{J-(-1\mp\Delta)/2}{\pm\Delta}\rho,
\qquad
\Psi_r=
\prod_{s\ne r}\frac{J-s}{r-s}\Psi^{TT},
\quad
r,s\in\left\{-\frac32,\frac{1+\Delta}{2},\frac{1-\Delta}{2}\right\}.
\tag{O-53}
```

Restoring the temporary symbols, the physical fermion operators are

```math
\boxed{
\begin{array}{c|l}
\text{Representation}&\text{First-order factors}\\ \hline
\frac32&
D+\frac32igM,\quad
D-\frac{igM}{2}
\left(1\pm\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)\\[2mm]
\frac12&
D+\frac12igM,\quad
D-\frac{igM}{2}
\left(-1\pm\sqrt{\frac{2(4-L_0)}{L_0-1}}\right)
\end{array}}
\tag{O-54}
```

For $`L_0<1`$ the square root is complex. This does not discard the $`\alpha<0`$ region: the real system contains the conjugate factors together.

## Exceptional operator loci

Points at which the generic derivation divided by a vanishing quantity require separate treatment.

```math
\mu=0
\ \Longleftrightarrow\
L_0=\frac43
\ \Longleftrightarrow\
\alpha g^2=\frac32.
\tag{O-55}
```

At the critical merger,

```math
\mathfrak T_2^2h^{TT}=0,\qquad
P_{3/2}(D)=\frac{\alpha}{3}
(D+3t/2)^2(D-5t/2).
\tag{O-56}
```

The double factors cannot be replaced by two independent simple-root equations. For example,

```math
\mathfrak T_2h_1=h_0,\qquad \mathfrak T_2h_0=0
\tag{O-57}
```

retains the generalized solutions.

The vector roots there are

```math
\lambda_-=0,\qquad \lambda_+=\frac{64g^2}{9}.
```

For $`M_V(x)=\mathop{\mathrm{diag}}\nolimits(x,x,1)K_V(x)`$,

```math
n_0=\begin{pmatrix}-4\\8\sqrt2g\\1\end{pmatrix},
\qquad
n_1=\begin{pmatrix}0\\0\\-27/(32g^2)\end{pmatrix}
```

and

```math
M_V(0)n_0=0,\qquad
M_V(0)n_1+M_V'(0)n_0=0.
\tag{O-58}
```

so the colliding channel is

```math
\begin{pmatrix}c\\v\\a\end{pmatrix}_{\rm chain}
=n_0W_1+n_1W_0,\qquad
\mathfrak M_1W_1=W_0,\qquad \mathfrak M_1W_0=0
\tag{O-59}
```

Here $`p=-2W_0/g`$ is invariant. Assigning an additional Maxwell gauge symmetry to $`W_0`$ would be incorrect. The other Maxwell and massive-vector channels are

```math
\begin{pmatrix}1\\0\\1/2\end{pmatrix}A_0,
\qquad
\begin{pmatrix}4\\8\sqrt2g/3\\1\end{pmatrix}A_M,
\qquad
\mathfrak M_1A_0=0,\quad
\left(\mathfrak M_1-\frac{64g^2}{9}\right)A_M=0
\tag{O-60}
```

as displayed.

The second exceptional point is

```math
L_0=2\qquad\Longleftrightarrow\qquad\alpha g^2=2
\tag{O-61}
```

Here the gauge rank changes. The scalar system has extra directions

```math
\delta l=\sigma,\qquad\delta n=-g\sigma,
```

```math
\delta h_{\mu\nu}=2\omega\bar g_{\mu\nu},\qquad
\delta l=0,\qquad
\delta n=-\frac1g(\bar\Box+5k)\omega
\tag{O-62}
```

so the two generic scalar channels must not be retained. The metric operator becomes

```math
\mathfrak T_2(\mathfrak T_2-3k)
\tag{O-63}
```

with a partially massless second factor. Both $`w^{ij}`$ vectors become Maxwell fields.

The vector–form symmetry is

```math
\delta c=2\xi,\qquad
\delta\mathcal H^{abc}
=\varepsilon^{deabc}(d\xi)_{de}
```

under which

```math
\mathcal H'^{abc}:=\mathcal H^{abc}
-\frac12\varepsilon^{deabc}\mathcal G_{de},
\qquad a':=a-\frac12c
\tag{O-64}
```

is invariant. The remaining coupled matrix is

```math
K_{\rm crit}(x)=
\begin{pmatrix}
1/(6g^2)&-\sqrt2/(3g)\\
-\sqrt2/(3g)&8/3+2x/(3g^2)
\end{pmatrix},
\qquad
\det K_{\rm crit}(x)=\frac{x+2g^2}{9g^4}.
\tag{O-65}
```

The physical system still has the undifferentiated form row:

```math
\mathop{\mathrm{diag}}\nolimits(x,1)K_{\rm crit}(x)
\begin{pmatrix}v\\a'\end{pmatrix}=0
```

Only the channels

```math
\mathfrak M_1v_0=0,\qquad
(\mathfrak M_1+2g^2)p'=0
\tag{O-66}
```

remain, with mixing map

```math
v=v_0+\frac{p'}{\sqrt2},\qquad
a'=\frac{v_0}{4\sqrt2g}+\frac{p'}{4g}
\tag{O-67}
```

The closed three-form obeys

```math
dH'_c=0,\qquad(\mathfrak M_3-2g^2)H'_c=0.
\tag{O-68}
```

The additional fermionic gauge direction is

```math
\delta\Psi_a=\gamma_a\theta,\qquad
\delta\zeta=-\frac1g(D-5t/2)\theta
\tag{O-69}
```

so the combination

```math
\eta:=\zeta+\frac1g(D-5t/2)u
```

is invariant, leaving one spin-half equation in place of three:

```math
\boxed{(D-igM/2)\eta=0}
\tag{O-70}
```

The spin-three-halves operator becomes

```math
\boxed{
P_{3/2}(D)=\frac{2}{3g^2}
(D+3igM/2)(D-3igM/2)(D+igM/2).
}
\tag{O-71}
```

The generic mixing is thus resolved while retaining Jordan chains at $`L_0=4/3`$ and the enlarged gauge quotient at $`L_0=2`$. These are local bulk operators; their global admissible kernels and generalized solutions remain subject to the boundary prescription.

