# Critical branches

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="13-critical-points-of-the-selected-branch"></a>

## Critical points of the selected branch

The selected Einstein-connected branch has two distinct critical points: $`A=0`$ at $`\lambda_{R^2}g^2=1/4`$, and $`B=0`$ at its endpoint $`\lambda_{R^2}g^2=1/3`$. The latter is also the merger with $`L_+`$. A separate spectrum along $`L_+`$ is not included. Here $`\tau=6\lambda_{R^2}g^2`$.

<a id="131-absence-of-further-root-mergers"></a>

### Absence of further root mergers

```math
\begin{aligned}
(M_+^2-M_-^2)\ell^2&=4\nu,&
(M_\pm^2-M_0^2)\ell^2&=(\nu\pm1)^2,\\
(M_\Pi^2-M_-^2)\ell^2&=2\nu-1,&
(M_\Pi^2-M_+^2)\ell^2&=-2\nu-1,\\
(\mu_+-\mu_-)\ell&=2\nu,&
(\mu_\pm-\mu_0)\ell&=-s_g\pm\nu.
\end{aligned}
```
For $`\nu>1`$ or $`\nu=i\kappa`$, with $`\kappa^2>2`$, these differences are nonzero. The regular eigenfield formulas also exclude $`A=0`$, even though these root differences do not vanish there. Equal masses of the two internal components of $`\Pi`$ and the two zero Maxwell roots occur throughout the regular branch; they are not new critical points. Equal energies of different spins do not imply a Jordan block in the same physical operator. The merger at $`\nu=1`$ is analyzed separately below.

<a id="132-lambda_r20"></a>

### $`\lambda_{R^2}=0`$

This value is the zero of the higher-derivative coefficient. The background equation determines
```math
-4L_0+4=0\quad\Longrightarrow\quad L_0=1
```
while $`g`$ remains free. The original scalar equations give
```math
n=-2gs,\quad\frac32r_1-4\Box s+10g^2s=0,
\quad r_1-2\Box s+8g^2s=0
```
and
```math
(\Box+2g^2)s=0,\qquad M_s^2\ell^2=-4
```
Together with $`w=0`$, $`\mathsf E=0`$, and $`\zeta_1=0`$, $`12+12`$ polarizations remain. At $`\lambda\to0^+`$, the long-multiplet energy diverges; the change at exactly $`\lambda=0`$ is a drop in derivative order, not multiplet shortening.

<a id="133-lambda_r2g219121"></a>

### $`\lambda_{R^2}g^2=19/121`$

The zero scalar-mass condition is
```math
M_-^2=0\quad\Longrightarrow\quad(\nu-1)^2=4.
```
On the selected positive branch, $`\nu>2`$, so $`\nu=3`$ and
```math
\frac{4-L}{2(L-1)}=9
\quad\Longrightarrow\quad L=\frac{22}{19},\qquad
\lambda g^2=\frac{4(L-1)}{3L^2}=\frac{19}{121}.
```
The background Jacobian determinant
```math
\det J_{\mathrm{bg}}
=-\frac{8g^2}{15L^2}(L-2)(3L-4)(19L-22)
```
vanishes at this point. However, its $`(N,L)`$ minor is $`320g^2/121\neq0`$, so the background rank is two. The kernel direction is checked by
```math
J_{\mathrm{bg}}\begin{pmatrix}-22g/19\\1\\-88g^2/19\end{pmatrix}=0
```
For the kinetic matrix, $`\det\mathsf K=-8A\lambda/L^4\neq0`$ remains. Thus there is no new gauge direction or reduction in propagation count. The normalizable energy of the massless scalar is $`E=4`$; the constant source mode is not treated as a physical vacuum modulus.

<a id="134-lambda_r2g214-original-critical-action"></a>

<a id="tau-three-halves"></a>

### $`\lambda_{R^2}g^2=1/4`$: original critical action

```math
A=4-3L=0\quad\Longrightarrow\quad L_c=\frac43.
```
Substitution into the total background equation gives
```math
3\lambda_cg^2\frac{16}{9}-\frac{16}{3}+4=0
\quad\Longrightarrow\quad\lambda_c=\frac1{4g^2}
```
Also,
```math
B_c=\frac23,\quad\ell_c^{-2}=\frac{8g^2}{9},\quad
m_c=\frac{2g}{3\sqrt2},\quad\nu_c=2.
```
The regular-branch transformations involving $`A^{-1}`$ are not used here.

Let
```math
\rho_1=\frac32n+3gs,\quad
X_c=\frac{r_1}{8g^2}-\frac{3\Box s}{16g^2}+\frac56s-\frac{\rho_1}{2g},
\quad\mathcal W=\sqrt2v+\frac32\mathsf E+4gc
```
be the critical composites. Substituting $`n=2\rho_1/3-2gs`$ puts the scalar density in the form
```math
\begin{aligned}
\mathcal L_{\mathrm{sc},c}={}&\frac1{16g^2}(r_1-3\Box s/2)^2
+(5s/6-\rho_1/(2g))r_1\\
&+\frac{25g^2}{9}s^2-\frac{10g}{3}s\rho_1+\frac{13}{9}\rho_1^2
+\frac54(\nabla s)^2-\frac3{4g}\nabla s\cdot\nabla\rho_1
-\frac1{8g^2}(\nabla\rho_1)^2
\end{aligned}
```
Square completion and integration by parts give
```math
\mathcal L_{\mathrm{sc},c}
=\frac{X_c^2}{\lambda_c}
+\frac{\lambda_c}{2}\rho_1(\Box+4/\ell_c^2)\rho_1
+\nabla_\mu J_{\mathrm{sc,new}}^\mu,
```
```math
J_{\mathrm{sc,new}}^\mu=(5s/4-3\rho_1/(4g))\nabla^\mu s
-\frac{\rho_1}{8g^2}\nabla^\mu\rho_1
```

The metric equation is
```math
\mathscr P_{\mu\nu}X_c=0
\quad\Longrightarrow\quad
\Box X_c=5X_c/\ell_c^2,
\quad\nabla_\mu\nabla_\nu X_c=\bar g_{\mu\nu}X_c/\ell_c^2
```
Its trace alone cannot be treated as an independent scalar wave equation. In the Poincaré patch, the general local solution is
```math
X_c=\frac{a+b_\alpha x^\alpha+c(x_\alpha x^\alpha+z^2)}z
```
so the zero-source condition implies $`a=b_\alpha=c=0`$, hence $`X_c=0`$.

The other two scalar variations leave one BF scalar through
```math
\lambda_c(\Box+4/\ell_c^2)\rho_1-\frac{X_c}{\lambda_cg}=0,
\qquad
\mathcal E_{s|\rho_1}=(20g^2/3-3\Box/2)X_c
=\frac38\bar g^{\mu\nu}\mathscr P_{\mu\nu}X_c
```
For the traceless connection,
```math
\mathcal L_{w,c}=2\lambda_c\Pi^{ij}\Pi_{ij},\quad
\nabla_\mu\Pi^{ij}=0
```
so the same boundary condition gives $`\Pi^{ij}=0`$. Two new massless propagating scalars cannot be inferred from the $`M_\Pi^2\to0`$ limit.

Direct substitution of the critical values in the vector sector gives
```math
\begin{aligned}
\mathcal L_{\mathrm{vf},c}={}&-\frac{\lambda_c}{4}(\mathsf F+4g\mathsf G)^2
-4\lambda_cg(\mathsf F+2g\mathsf G)\cdot Q\\
&-3\mathsf E^2-2\sqrt2v\cdot\mathsf E-4gc\cdot\mathsf E.
\end{aligned}
```
```math
-2(\sqrt2v+2gc)\cdot\mathsf E
\simeq(\sqrt2\,dv/g+2\mathsf G)\cdot Q,
\quad d\mathsf E\cdot Q\simeq-2g\mathsf E^2
```
and
```math
\mathcal L_{\mathrm{vf},c}
=-\frac{\lambda_c}{4}(d\mathcal W)^2+\nabla_\nu J_{\mathrm{vf,new}}^\nu,
```
```math
J_{\mathrm{vf,new}}^\nu=-\frac2g
(\sqrt2v_\mu+2gc_\mu+3\mathsf E_\mu/2)Q^{\nu\mu}.
```
Variation of $`c`$ gives $`4g\lambda_c\nabla_\nu(d\mathcal W)^{\nu\mu}=0`$, leaving one Maxwell equation; the other form equations are its derivatives/combinations.

Although the critical fermionic action is
```math
S_{F,c}^{(2)}=-\frac{\lambda_c}{2}\langle\Lambda,\mathcal H_c\Lambda\rangle,
\qquad\mathcal H_c=\mathord{\not{\nabla}}-m_c\mathbb J
```
$`\Lambda`$ is not varied independently. Defining $`Y=\mathcal H_c\Lambda`$, the original variations give
```math
\mathscr R^\mu(\gamma\mathbb IY)=0,\qquad
(\mathord{\not{\nabla}}+5m_c\mathbb J)Y=0
```
Clifford contraction
```math
\begin{aligned}
\mathscr R^\mu(\gamma Z)
&=\gamma^{\mu\nu\rho}\gamma_\rho\nabla_\nu Z
+3m_c\gamma^{\mu\nu}\gamma_\nu\mathbb JZ\\
&=3[\gamma^\mu(\mathord{\not{\nabla}}+4m_c\mathbb J)-\nabla^\mu]Z
\end{aligned}
```
implies $`\nabla_\mu Y=-m_c\gamma_\mu\mathbb JY`$. $`Y`$ is a Killing spinor with the opposite sign. Excluding these finite-dimensional solutions, which are incompatible with normalizable zero-source data, leaves
```math
\mathcal H_c\Lambda=0.
```

The resulting critical bulk action, with surface terms treated separately, is
```math
\boxed{
\begin{aligned}
S_c^{(2)}\simeq\int d^5x\,\bar e\bigg[
&\frac{X_c^2}{\lambda_c}
+\frac{\lambda_c}{2}\rho_1(\Box+4/\ell_c^2)\rho_1
+2\lambda_c\Pi^{ij}\Pi_{ij}\\
&-\frac{\lambda_c}{4}(d\mathcal W)^2
-\frac{\lambda_c}{2}\bar\Lambda(\mathord{\not{\nabla}}-m_c\mathbb J)\Lambda
\bigg].
\end{aligned}}
```

<a id="135-critical-norms-and-the-zero-norm-kernel"></a>

### Critical norms and the zero-norm kernel

The solutions with nonzero norm are one scalar, one Maxwell field, and one symplectic–Majorana spinor, with
```math
(\Box+4/\ell_c^2)\rho_1=0,\quad
\nabla_\nu(d\mathcal W)^{\nu\mu}=0,\quad
(\mathord{\not{\nabla}}-m_c\mathbb J)\Lambda=0,
```
```math
k_{\rho_1}=k_{\mathcal W}=k_\Lambda=\lambda_c=\frac1{4g^2}>0
```

To check the apparently singular norms of the regular-branch light coordinates, write
```math
\sigma_0|_c=2X_c-\rho_1/g=-\rho_1/g,\quad k_{\sigma_0}|_c=1/4
\quad\Longrightarrow\quad k_{\rho_1}=1/(4g^2)
```
For the light fermion solution,
```math
\widehat\zeta_0:=\frac AB\zeta_0=\zeta,
\quad\Lambda=-2g\mathbb I\widehat\zeta_0,
\quad k_{\widehat\zeta_0}=\frac{4B}{3L^2}\longrightarrow\frac12.
```
Using $`\widehat\zeta_0=\mathbb I\Lambda/g`$ and $`\mathbb I^\sharp\mathbb I=1/2`$ again gives $`k_\Lambda=1/(4g^2)`$. The zero of $`A^2`$ in the light fermion's $`\zeta_0`$ coordinate therefore does not remove the physical fermion.

In contrast,
```math
A(\Box+2/\ell^2)h^{\mathrm{TT}}=0,\qquad
A(\mathord{\not{\nabla}}_{3/2}-3m\mathbb J)\psi^{3/2}=0
```
ceases to be a propagation equation at the critical point. $`A(\Box+2/\ell^2)\to0`$ does not produce $`(\Box+2/\ell^2)^2`$; a logarithmic spin-2 partner cannot be derived from this limit.

Original field directions satisfying
```math
\delta X_c=\delta\rho_1=\delta\mathcal W
=\delta\Pi^{ij}=\delta\Lambda=0
```
lie in the kernel of the quadratic symplectic form. These directions remain in the action. This calculation neither establishes them as new gauge symmetries of the full nonlinear theory nor reduces the degrees of freedom of the complete interacting theory to $`4+4`$.

<a id="tau-2-endpoint"></a>

### $`\tau=2`$: local Jordan pairs and independent BF scalars

At the endpoint,
```math
L=2,\qquad \lambda=\frac1{3g^2},\qquad A=-2,\qquad B=0,
\qquad \nu=1,\qquad \ell^{-2}=2g^2,\qquad m=\frac g{\sqrt2}.
```
The fields involving $`B^{-1}`$ in the regular diagonalization are not coordinates at this point. Instead, keep $`a=(c,v,\mathsf E)^T`$ in the finite dual vector action (the paper's equation (3.20) (`eq:R2vec2`)), with convention
```math
\mathcal L_{\rm vec}=-\frac14(da)^T K(da)-\frac12a^TMa.
```
Direct substitution gives
```math
K=\begin{pmatrix}
0&0&2/g\\
0&-1/(3g^2)&\sqrt2/(3g^2)\\
2/g&\sqrt2/(3g^2)&1/(3g^2)
\end{pmatrix},\qquad
M=\mathop{\mathrm{diag}}\nolimits(0,0,-2),\qquad
\det K=\frac4{3g^4}.
```
Thus, defining $`\mathcal O a_\nu=\bar\nabla^\mu(da)_{\mu\nu}`$,
```math
\begin{aligned}
N:=K^{-1}M&=\begin{pmatrix}0&0&-g\\0&0&0\\0&0&0\end{pmatrix},
&N^2&=0,&\mathop{\mathrm{rank}}\nolimits N&=1,\\
\mathcal O\mathsf E&=0,&\mathcal Oc&=-g\mathsf E,&\mathcal Ov&=0.
\end{aligned}
```
The zero eigenvalue has algebraic multiplicity three and kernel dimension two: one size-two Jordan block and one ordinary Maxwell block. The finite change $`C=c+\mathsf E/(4g)`$, $`V=v-\sqrt2\mathsf E`$ makes the pairing explicit,
```math
\mathcal L_{\rm vec}=-\frac1g(dC)\cdot(d\mathsf E)
+\frac1{12g^2}(dV)^2+\mathsf E^2.
```
This is the local Jordan pairing of the massless vector in $`\mathcal V`$ with the vector of $`\mathcal V_L(2)`$.

For the neutral scalars, use the original $`(X,s,n)`$ equations
$`(\mathsf K\Box+\mathsf M)(X,s,n)^T=0`$ in the
[constraint reduction](gauge_constraints.md#92-metricscalar-decomposition).
Their dimensionless mass matrix is finite:
```math
J_s:=-\ell^2\mathsf K^{-1}\mathsf M\big|_{L=2}
=\begin{pmatrix}5&-3&-3/g\\-3&-3&1/g\\18g&-6g&-10\end{pmatrix}.
```
It satisfies
```math
\det(x\mathbf1-J_s)=x(x+4)^2,\qquad
J_s(J_s+4\mathbf1)=0,\qquad
\dim\ker(J_s+4\mathbf1)=2.
```
Consequently, the two neutral scalars at $`M^2\ell^2=-4`$ are independent eigenmodes, rather than a Jordan pair. The remaining neutral scalar has $`M^2\ell^2=0`$.

The spinor conclusion follows from the original coupled Euler equations, before the $`B^{-1}`$ change to separate spinors. With
```math
\mathcal H=\mathord{\not{\nabla}}-m\mathbb J,\quad
\mathcal K_F=\mathord{\not{\nabla}}+5m\mathbb J,\quad
\mathcal P_F=\mathord{\not{\nabla}}-3m\mathbb J,\quad
\zeta_0=\zeta-\frac{i\lambda L}{2A}\mathcal K_F\Lambda,
```
the [undivided spinor equations](gauge_constraints.md#94-gravitinospinor-mixing) are
```math
\mathcal H\zeta_0=0,\qquad
(\lambda\mathcal K_F\mathcal P_F-A)\Lambda=2gA\mathbb I\zeta_0.
```
Here $`A=-2`$ is nonzero. The background identity
```math
\lambda\mathcal K_F\mathcal P_F-A
=\lambda\mathcal H(\mathord{\not{\nabla}}+3m\mathbb J)-B
```
then yields, for $`\chi=(\mathord{\not{\nabla}}+3m\mathbb J)\Lambda`$,
```math
\mathcal H\zeta_0=0,\qquad
\mathcal H\chi=-12g^3\mathbb I\zeta_0.
```
The nonzero off-diagonal coefficient gives a Jordan pair at the common light-spinor root; the other spinor root remains separate. In the paper's notation this pairs $`\varphi_0`$ and $`\chi_+`$ for $`g>0`$ (the extra-spinor labels interchange for $`g<0`$).

These are local quadratic statements. They establish the repeated vector and spinor operators that admit local logarithmic partners, without specifying which logarithmic modes belong to an admissible boundary domain. The final paper leaves that boundary problem open. The [exact paper checks](../../../computations/r2_ads5_paper_checks/README.md) replay the finite matrices, their Jordan structure and the two-dimensional BF eigenspace with symbolic $`g`$.
