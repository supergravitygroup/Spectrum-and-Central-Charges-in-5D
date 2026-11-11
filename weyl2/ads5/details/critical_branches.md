# Critical branches and boundary conditions

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="15-critical-and-special-parameter-conditions"></a>

## Critical and special parameter conditions

<a id="151-complete-symbolic-separation-of-coincidence-conditions"></a>

### Complete symbolic separation of coincidence conditions

With $`O_0=\Box+g^2`$ and $`t=\Box+2g^2`$:

```math
P_2(x)=x(x+\kappa),\qquad
P_{\rm scal}(s)=(s+2g^2)(s+\kappa),
```

```math
P_V(t)=t^2[(t-\nu^2)^2-2g^2\nu^2],
```

```math
P_{RS}(z)=(z+3m)[(z-m)^2-\nu^2],\qquad
P_{1/2}(z)=(z+m)[(z+m)^2-\nu^2].
```

Directly from root differences:

```math
\begin{aligned}
\mathop{\mathrm{Disc}}\nolimits P_2&=\kappa^2,\\
\mathop{\mathrm{Disc}}\nolimits P_{\rm scal}&=(2g^2-\kappa)^2=\nu^4,\\
\mathop{\mathrm{Disc}}\nolimits[(t-\nu^2)^2-2g^2\nu^2]&=8g^2\nu^2,\\
\mathop{\mathrm{Disc}}\nolimits P_{RS}
&=(2\nu)^2(4m+\nu)^2(4m-\nu)^2
=4\nu^2(16m^2-\nu^2)^2
=4\nu^2\kappa^2,\\
\mathop{\mathrm{Disc}}\nolimits P_{1/2}&=(2\nu)^2\nu^2\nu^2=4\nu^6 .
\end{aligned}
```

The principal physical coincidences are therefore

```math
\boxed{
\kappa=0\Longleftrightarrow\alpha g^2=-2,\qquad
\nu^2=0\Longleftrightarrow\alpha g^2=6
}
```

Zeros in the generic norm table also reduce to these finite conditions.
$`\alpha=0`$ and $`g=0`$ are excluded in the present problem.

Other special conditions:

| Equation | The result is | Status |
|---|---|---|
| $`2\alpha g^2-3=0`$ | $`\alpha g^2=3/2`$ | The algebraic solution coefficient of $`N`$ vanishes; the scalar system remains |
| $`1-2\rho=0`$ | $`\alpha g^2=8`$ | The Dirac root of one fermion branch vanishes; no new gravitino gauge symmetry |
| $`-\kappa=5g^2/2`$ | $`\alpha g^2=-3/4`$ | Singularities of some trace projections; no new double root in the full physical operator |
| $`M_{H_1}^2+3g^2/2=0`$ | $`-3/\alpha=0`$ | Does not occur at finite $`\alpha`$; no separate finite partially massless spin-2 branch |

At $`\alpha g^2=8`$, the masses of $`Z_-`$ and $`v'`$ also coincide at $`-3g^2/8`$.
Their $`R`$ charges are $`0`$ and $`\pm2`$, respectively, so mass equality
alone does not indicate a Jordan block. For the $`\mu=0`$ gravitino branch,
$`\mu^2-9g^2/8\neq0`$, so the massless-gravitino gauge condition is not satisfied.

At $`\alpha g^2=-3/4`$, $`\rho=3`$, and physical norm coefficients are nonzero.
Use the full coupled equations instead of dividing by factors such as
$`2\Box-5g^2`$ or $`\mathord{\not{\nabla}}-5m`$ in trace/gamma-trace projections.

<a id="152-alpha-g2-2-merger-with-the-massless-root"></a>

### $`\alpha g^2=-2`$: merger with the massless root

```math
\nu^2=2g^2=16m^2,\quad\kappa=0,\quad\rho=2.
```

```math
\begin{aligned}
P_2&=O_0^2,\\
P_{RS}&=(\mathord{\not{\nabla}}+3m)^2(\mathord{\not{\nabla}}-5m),\\
P_V&=t^3(t-4g^2).
\end{aligned}
```

At the repeated root,

```math
O_0H_0=0,\qquad O_0H_{\log}=H_0,
```

```math
(\mathord{\not{\nabla}}+3m)\Psi_0=0,\qquad
(\mathord{\not{\nabla}}+3m)\Psi_{\log}=\Psi_0
```

generalized partners are required. A vanishing simple-pole norm does not make the entire critical block zero:

```math
\mathcal G_{\rm Jordan}
=\begin{pmatrix}0&c\\c&b\end{pmatrix},
\qquad
\det\mathcal G_{\rm Jordan}=-c^2 .
```

The second-order block has one positive and one negative direction as long as $`c\neq0`$. This does not claim that the numerical normalization of the full global norm matrix has been calculated.

In the vector block, regular combinations replace the singular eigenvector
basis. With $`\mathcal Z:=A-c`$ and

```math
C_M=(t-\nu^2)\mathcal Z+g^2c,\qquad
V_M=\frac\alpha3v-\frac{\sqrt2a_0}{g}A+\frac{\sqrt2}{g}c,
\qquad
W_M=C_M+\frac{3\sqrt2g}{\alpha}V_M
```

write $`tC_M=tV_M=0`$ and, at the critical point,

```math
t(t-4g^2)\mathcal Z=2g^2W_M,\qquad tW_M=0.
```

```math
\mathcal Z_4=\frac{t^2}{16g^4}\mathcal Z,\qquad
\mathcal Z_J=\mathcal Z-\mathcal Z_4
```

Then

```math
(t-4g^2)\mathcal Z_4=0,\qquad
t\mathcal Z_J=-\frac12W_M,\qquad tW_M=0
```

This explicitly retains the generalized partner of the coincident Maxwell branch.

<a id="153-shortening-content-at-alpha-g2-2"></a>

### Shortening content at $`\alpha g^2=-2`$

Here $`E_0=3`$. Using standard names at the unitarity bound and Dynkin labels
$`[2j_L;2j_R]`$ in square brackets,

```math
\mathfrak L[1;1]^{(0)}_3
\rightsquigarrow
A_1\bar A_1[1;1]^{(0)}_3
\oplus A_2\bar L[0;1]^{(-1)}_{7/2}
\oplus L\bar A_2[1;0]^{(+1)}_{7/2}.
```

This is an equality of characters/composition factors, not a direct-sum decomposition of the critical action into independent blocks.

```math
(32+32)=(8+8)+(12+12)+(12+12).
```

The first short graviton multiplet coincides with the theory's existing massless graviton multiplet. The total critical content therefore has two graviton composition factors, their logarithmic link, two conjugate semishort multiplets, and a massless vector multiplet.

Longitudinal states do not disappear under shortening:

```math
D(\Delta;1,1)\xrightarrow{\Delta\to4}
D_{\rm massless}(4;1,1)\oplus D(5;\tfrac12,\tfrac12),
```

```math
D(\Delta;\tfrac12,\tfrac12)\xrightarrow{\Delta\to3}
D_{\rm massless}(3;\tfrac12,\tfrac12)\oplus D(4;0,0).
```

For this longitudinal vector and scalar,

```math
M_{\rm vec}^2\ell^2=(5-1)(5-3)=8,\qquad
M_{\rm scal}^2\ell^2=4(4-4)=0.
```

Since the spinor in gravitino shortening has $`\Delta=9/2`$,
$`|\mu|\ell=5/2`$.
These are solution branches of the original fields, not new independent fields.

Counting check:

```math
\begin{aligned}
\text{spin-2 critical block:}&\quad 5+5+4=14,\\
\text{merged vector block:}&\quad3+3+1=7,\\
\text{merged gravitino block:}&\quad8+8+4=20.
\end{aligned}
```

<a id="154-alpha-g26-a-different-critical-structure"></a>

### $`\alpha g^2=6`$: a different critical structure

```math
\nu^2=0,\quad\kappa=2g^2,\quad\rho=0.
```

Scalars

```math
(\Box+2g^2)\lambda_{\rm s}=0,\qquad
(\Box+2g^2)d=0
```

with kinetic matrices

```math
\mathop{\mathrm{diag}}\nolimits\left(\frac23,-\frac{512}{g^4}\right)
```

Counting two separate BF scalars as one Jordan block is incorrect.

For fermions,

```math
(\mathord{\not{\nabla}}+m)\zeta_{\rm s}=0,\qquad
(\mathord{\not{\nabla}}+m)^2X=0,
```

```math
(\mathord{\not{\nabla}}+3m)(\mathord{\not{\nabla}}-m)^2\widehat\Psi^{TT}=0.
```

The spin-$`1/2`$ field has a simple block and a double block, not a single
triple Jordan block. Vanishing of a simple-pole coefficient alone does
not justify removal of the double block.

In the form sector, with $`w=v+gc/\sqrt2`$, the regular critical action is

```math
\boxed{
\mathcal L_{\rm form,crit}
=-\frac{2}{3g^2}(dF)^2
+\frac4{g^2}j_Fj_G
-\frac2{g^2}j_G^2-G^2-\frac1{g^2}(dw)^2 .
}
```

The full independent coupled equations are

```math
2\mathop{\mathrm{div}}\nolimits dF=d(tc),\qquad
t^2c=0,\qquad
t(j_F+g^2c)=0,\qquad tw=0
```

Since $`j_Fj_G`$ mixing remains, $`F\mapsto F+d\Lambda`$ is not a new gauge symmetry.
In the generic higher-derivative matrix,

```math
\det\begin{pmatrix}
\alpha/3-2/g^2&2/g^2\\
2/g^2&-2/g^2
\end{pmatrix}
=-\frac{2\alpha}{3g^2}
```

is nonzero. Vanishing of one subblock coefficient does not by itself determine the rank of the whole coupled system.

For the two-form operator
$`\mathscr L_2=\mathop{\mathrm{div}}\nolimits d+d\,\mathop{\mathrm{div}}\nolimits`$,

```math
\mathscr L_2F=dj_F+\frac12d(tc),\qquad
\mathscr L_2^2F=-g^2d(tc),\qquad
\mathscr L_2^3F=0.
```

The final cubic equation is a necessary consequence; it cannot alone replace the coupled system in the first line.

<a id="bolum-16"></a>

<a id="16-result-of-the-critical-boundary-analysis-at-this-stage"></a>

## Scope of the critical boundary analysis

<a id="161-retaining-logarithmic-responses-for-alpha-g2-2"></a>

### Retaining logarithmic responses for $`\alpha g^2=-2`$

For coincident fast responses,

```math
\Phi_{\log}
=\lim_{\lambda_1\to\lambda_0}
\frac{\Phi_{\lambda_1}-\Phi_{\lambda_0}}{\lambda_1-\lambda_0}
```

this root-merger calculation produces a generalized partner. Here $`\lambda_1,\lambda_0`$ are operator eigenvalues, not arbitrary numerical assignments to free couplings.

Critical source and logarithmic-source coefficients vanish; ordinary and logarithmic responses are retained:

```math
\boxed{\text{source}=0,\quad\text{log source}=0,\quad
\text{the response and logarithmic response are retained}.}
```

Finite logarithmic powers multiplying fast falloff do not spoil norm
convergence on these branches. Also removing logarithmic responses
truncates the full local branch content. These results concern local roots
and falloffs; a global normalization and supermultiplet interpretation depend
on the common boundary domain and the transformations preserving it.

<a id="162-critical-form-boundary-data-for-alpha-g26"></a>

### Critical form boundary data for $`\alpha g^2=6`$

The following calculation checks the **coupled bosonic form boundary form** in the stated local boundary coordinates.

In local conformal boundary coordinates, write

```math
ds^2=\frac{\ell^2}{z^2}(dz^2+\eta_{ij}dx^idx^j),\qquad
\ell^2=\frac2{g^2}
```

Here $`z`$ is the radial coordinate.
In a radial representative, a candidate response expansion without logarithms is:

```math
\begin{aligned}
c_i&=f_i+z^2c_{2i}+\cdots,\\
F_{zi}&=z^{-1}f_i+z f_{2i}+\cdots,\\
F_{ij}&=B_{ij}+z^2B_{2ij}+\cdots,\\
w_i&=z^2w_{2i}+\cdots.
\end{aligned}
```

In this section, $`B_{ij}`$ is a boundary coefficient of $`F_{ij}`$, not the independent two-form potential $`B_{\mu\nu}`$. Also,

```math
(Mf)_i=\partial^j(df)_{ji},\qquad
(\mathop{\mathrm{div}}\nolimits B)_i=\partial^jB_{ji}.
```

The divergence of a two-form in the AdS metric is

```math
(j_F)_i=\ell^{-2}\left[
z^2(\partial_zF_{zi}+\partial^jF_{ji})-zF_{zi}\right]
```

and hence

```math
(j_F+g^2c)_i
=\ell^{-2}z^2[(\mathop{\mathrm{div}}\nolimits B)_i+2c_{2i}]+\cdots,
```

```math
(j_F+g^2c)_z=-\ell^{-2}z\,\partial^if_i+\cdots.
```

Their radial component in the Maxwell equation gives

```math
\boxed{4\,\partial^ic_{2i}
+\Box_\partial\partial^if_i=0}
```

while $`tw=0`$ gives $`\partial^iw_{2i}=0`$.

In the other coupled equation,

```math
(dF)_{zij}
=-z^{-1}(df)_{ij}
+z(2B_2-df_2)_{ij}+\cdots,
\qquad
(tc)_i=\ell^{-2}z^2(Mf)_i+\cdots .
```

The $`ij`$ component of $`2\mathop{\mathrm{div}}\nolimits dF=d(tc)`$ is:

```math
8B_2-4df_2+2\mathop{\mathrm{div}}\nolimits dB=d(Mf),
```

```math
\boxed{
B_2=\frac12df_2-\frac14\mathop{\mathrm{div}}\nolimits dB+\frac18d(Mf).
}
```

The number of free boundary coefficients at this order is

```math
4\ (f)+6\ (B)+4\ (f_2)+3\ (c_2)+3\ (w_2)=20
```

This shows that the candidate critical expansion does not truncate the form-sector polarizations at the outset; it is not by itself a proof of global completeness or normalization.

<a id="163-logarithmic-term-and-boundary-variation-of-the-critical-form-block"></a>

### Logarithmic term and boundary variation of the critical form block

The leading possible logarithmic integral coefficient is

```math
-\frac{2\ell}{z}(df)^2-\frac{4\ell}{z}f\cdot Mf
```

because

```math
f\cdot Mf
=\partial_i[f_j(df)^{ij}]-\frac12(df)^2,
```

```math
-\frac{2\ell}{z}(df)^2-\frac{4\ell}{z}f\cdot Mf
=-\frac{4\ell}{z}\partial_i[f_j(df)^{ij}].
```

This term becomes a total derivative on the boundary. Corner contributions at time endpoints from total derivatives must be tracked in the physical symplectic form.

The radial boundary variation of the same expansion is

```math
\begin{aligned}
\ell^{-1}\Theta_\partial={}&
2(df)^{ij}\delta B_{ij}+2(Mf)^i\delta f_i
-8f^i\delta c_{2i}\\
&-\left[
4\mathop{\mathrm{div}}\nolimits B-4Mf
+2d(\partial\cdot f)+8c_2
\right]^i\delta f_i .
\end{aligned}
```

Integrating by parts on the boundary gives

```math
\int\Theta_\partial
=\ell\,\delta\!\int
\left[
-4f\cdot\mathop{\mathrm{div}}\nolimits B
-8f\cdot c_2+3f\cdot Mf
-f\cdot d(\partial\cdot f)
\right].
```

This establishes integrability of the bosonic form boundary form.
A global supersymmetric domain depends on the combined bosonic–fermionic
boundary flux and the boundary behavior of the SUSY charges.

<a id="164-critical-fermionic-coefficient-relations"></a>

### Critical fermionic coefficient relations

In the internal eigencomponent with $`m\ell=+1/2`$, for $`Q_X:=\mathord{\not{\nabla}}+m`$, write

```math
X_+=z^{3/2}a+\cdots,\qquad
X_-=z^{5/2}(b+b_{\log}\log z)+\cdots
```

The signs denote $`\gamma^z`$ chiralities.
The AdS Dirac operator is

```math
\ell\mathord{\not{\nabla}}
=\gamma^z(z\partial_z-2)+z\gamma^i\partial_i
```

with

```math
\ell Q_XX
=z^{5/2}(\mathord{\not{\partial}} a-b_{\log})+\cdots .
```

If the logarithmic coefficient vanishes, the required relation is

```math
\boxed{b_{\log}=0,\qquad
[\ell Q_XX]_{z^{5/2}}=\mathord{\not{\partial}} a}
```

This condition is not $`Q_XX=0`$; generalized double-operator solutions remain.

On the lower gravitino branch, with $`Q_{RS}:=\mathord{\not{\nabla}}-m`$ and $`\gamma^ia_i=0`$,
the divergence constraint is

```math
\widehat\Psi_z=\frac12z^{5/2}\partial^ia_i+\cdots
```

and hence

```math
[\ell Q_{RS}\widehat\Psi_i]_{z^{5/2}}
=(\mathscr D_{3/2}a)_i,\qquad
(\mathscr D_{3/2}a)_i
=\mathord{\not{\partial}} a_i-\frac12\gamma_i\partial^ja_j .
```

Gamma-trace check:

```math
\gamma^i\mathord{\not{\partial}} a_i
=2\partial^ia_i-\mathord{\not{\partial}}(\gamma^ia_i)
=2\partial^ia_i,
```

```math
\gamma^i(\mathscr D_{3/2}a)_i
=2\partial^ia_i-\frac12(4)\partial^ia_i=0.
```

Because critical residues vanish, norms of these slow falloffs cannot be decided from an ordinary single-Dirac action. The graded Green form of the total gravitino–spinor action must include finite boundary and corner contributions.

A local link showing that SUSY requires such solutions is the following:
for the spinor image $`d\epsilon`$ of a $`d`$ scalar branch,

```math
(\mathord{\not{\nabla}}+m)(d\epsilon)
=(\mathord{\not{\partial}} d-4md)\epsilon,
```

```math
(\mathord{\not{\nabla}}+m)^2(d\epsilon)
=(\Box+16m^2)d\,\epsilon
=(\Box+2g^2)d\,\epsilon=0.
```

The first line is generally nonzero. The SUSY image cannot be restricted to the ordinary Dirac kernel.

<a id="165-part-of-this-critical-analysis-left-open-at-the-time"></a>

### Local spectrum and global boundary domain

The $`44+44`$ count refers to local mode content. A global Hilbert-space interpretation depends on a common variational principle for the coupled fields, the boundary and corner terms, central regularity, the gauge quotient and the symplectic form. Supersymmetric boundary conditions must be preserved by the eight Killing supersymmetries together with their compensating gauge transformations.

The energy sequence $`1,3/2,2,5/2,3`$ at $`\alpha g^2=6`$ specifies local representation data. Its interpretation as a global critical supermultiplet also depends on the null and logarithmic component links and their compatibility with that common boundary domain.

<a id="bolum-17"></a>

