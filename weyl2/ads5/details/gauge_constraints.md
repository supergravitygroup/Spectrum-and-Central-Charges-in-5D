# Gauge directions and physical constraints

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="9-gauge-directions-constraints-and-local-physical-content"></a>

## Gauge directions, constraints, and local physical content

The following block gives the coupled local analysis of [the physical-content derivation](../../action/details/physical_content.md). Its off-shell gauge count $`40+40`$ differs from its local propagating-mode count $`44+44`$. These are local counts; [kinetic norms](kinetic_norms.md) and [critical-branch boundary conditions](critical_branches.md) state the separate physical restrictions.

<a id="1-gauge-directions-and-noether-identities"></a>

### Gauge directions and Noether identities

For the quadratic action, gauge directions are the inhomogeneous parts
of the transformations evaluated on the background:

```math
\begin{aligned}
\delta k_{\mu\nu}&=\nabla_\mu\xi_\nu+\theta_{\mu\nu},
&\theta_{\mu\nu}&=-\theta_{\nu\mu},\\
\delta h_{\mu\nu}&=2\nabla_{(\mu}\xi_{\nu)},\\
\delta c&=d\Lambda,
&\delta v&=d\beta,\\
\delta b&=d\Lambda_1-\frac g2\Lambda_2,
&\delta a_3&=d\Lambda_2,\\
\delta\Psi_\mu&=\mathcal K_\mu\epsilon,
&\mathcal K_\mu&=\nabla_\mu+\frac{ig}{2\sqrt2}\gamma_\mu J,\\
\delta\zeta&=0,
&\delta\lambda=\delta n=\delta v'&=0.
\end{aligned}
\tag{1}
```

Here $`\delta\zeta=0`$ follows because, on the selected background,

```math
\left(\frac{\bar N}{2}+\frac{3g\bar L^2}{4}\right)\epsilon
=\left(-\frac{3g}{4}+\frac{3g}{4}\right)\epsilon=0
\tag{2}
```

Thus $`\zeta`$ is not a Goldstino that can be set to zero by local SUSY.

The current compensator gauge leaves a $`U(1)`$ subgroup of $`SU(2)`$.
The two internal components of $`v'_\mu{}^{ij}`$ transform homogeneously under
this $`U(1)`$; there are no two additional vector gauge parameters for them.

The form parameters

```math
\Omega_2:=\Lambda_2-\frac2g\,d\Lambda_1
```

Writing this as

```math
\delta b=-\frac g2\Omega_2,\qquad
\delta a_3=d\Omega_2,\qquad
\delta\left(a_3+\frac2g\,db\right)=0.
\tag{3}
```

The form sector therefore has **ten independent gauge directions**.
$`b_2`$ and $`a_3`$ cannot be counted as separate massless form systems.

| Gauge symmetry | Independent local parameter |
|---|---:|
| Diffeomorphism | $`5`$ |
| Local Lorentz | $`10`$ |
| $`C`$ gauge symmetry | $`1`$ |
| Residual internal $`U(1)`$ | $`1`$ |
| Combined $`B_2,E_3`$ form gauge symmetry | $`10`$ |
| Local SUSY | $`8`$ real Grassmann-odd components |

There are $`67`$ bosonic field components and $`48`$ fermionic ones.
Subtracting gauge directions gives

```math
67-(5+10+1+1+10)=40,\qquad 48-8=40.
\tag{4}
```

This $`40+40`$ is an off-shell gauge count, not the number of propagating
modes of the higher-derivative theory.

Without an additional $`1/p!`$ for form indices in the Euler derivatives,
the relevant linearized Noether identities are

```math
\begin{gathered}
\nabla^\mu\mathcal E_{\mu\nu}\equiv0,\qquad
\mathcal E_{[ab]}\equiv0,\\
\nabla_\mu\mathcal E_c^\mu\equiv0,\qquad
\nabla_\mu\mathcal E_v^\mu\equiv0,\\
3\nabla_\rho\mathcal E_a^{\rho\mu\nu}
+\frac g2\mathcal E_b^{\mu\nu}\equiv0,\\
\left(\nabla_a+\frac{ig}{2\sqrt2}\gamma_aJ\right)
\mathcal F_\Psi^a\equiv0
\end{gathered}
\tag{5}
```

In particular,

```math
\mathcal E_b^{\mu\nu}
=-\frac6g\nabla_\rho\mathcal E_a^{\rho\mu\nu}.
\tag{6}
```

It is therefore incorrect to count the $`B_2`$ equation as a second
independent constraint system alongside the $`E_3`$ equation.

<a id="2-constraints-and-dynamical-modes-in-the-scalar-and-metric-sector"></a>

### Constraints and dynamical modes in the scalar and metric sector

```math
r:=\delta R,\qquad
d:=\delta D=-\frac r{32}+\frac g4n+\frac{g^2}{8}\lambda
\tag{7}
```

Use these definitions. The scalar $`d`$ here is distinguished by context
from the exterior derivative $`d`$ in the form expressions.

The independent $`N,L`$ equations and the trace of the metric equation are:

```math
\begin{aligned}
0&=-4n-8g\lambda+\frac{32\alpha g}{3}d,\\
0&=r-2\Box\lambda-8g^2\lambda-8gn
+\frac{16\alpha g^2}{3}d,\\
0&=-\frac32r+(4\Box-10g^2)
\left(\lambda-\frac{4\alpha}{3}d\right).
\end{aligned}
\tag{8}
```

The first equation and (7), without dividing by a parameter-dependent
coefficient, give

```math
n=-2g\lambda+\frac{8\alpha g}{3}d,\qquad
r=-12g^2\lambda+
\left(\frac{64\alpha g^2}{3}-32\right)d
\tag{9}
```

Substituting these into the remaining two equations gives

```math
\begin{aligned}
0&=-2(\Box+2g^2)\lambda
+\frac{16}{3}(\alpha g^2-6)d,\\
0&=-\frac{16\alpha}{3}
\left(\Box+\frac{3g^2}{2}+\frac3\alpha\right)d .
\end{aligned}
\tag{10}
```

Now

```math
\lambda_{\mathrm s}:=\lambda-\frac{16\alpha}{3}d
```

Define these quantities, since

```math
(\Box+2g^2)d
=\left(\frac{g^2}{2}-\frac3\alpha\right)d,
```

```math
\begin{aligned}
(\Box+2g^2)\lambda_{\mathrm s}
&=\frac83(\alpha g^2-6)d
-\frac{16\alpha}{3}
\left(\frac{g^2}{2}-\frac3\alpha\right)d\\
&=0.
\end{aligned}
```

Result:

```math
\boxed{
(\Box+2g^2)\left(\lambda-\frac{16\alpha}{3}d\right)=0,\qquad
\left(\Box+\frac{3g^2}{2}+\frac3\alpha\right)d=0.}
\tag{11}
```

**There are two scalar modes.** $`d`$ is not a new independent off-shell
field; it is a dynamical combination of the metric, $`N`$, and $`L`$.

The auxiliary character of $`N`$ must be distinguished separately.
Substituting (7) into the first equation gives

```math
4(2\alpha g^2-3)n
+4g(\alpha g^2-6)\lambda-\alpha g\,r=0.
\tag{12}
```

Therefore:

- When $`2\alpha g^2-3\neq0`$, $`n`$ can be determined algebraically in the total
  quadratic system.
- When $`2\alpha g^2-3=0`$, the same equation becomes

```math
r+12g^2\lambda=0
\tag{13}
```

a constraint; $`n`$ acts as a multiplier in the quadratic action.

Equations (9)–(11) remain valid in the second case.
**Vanishing of this algebraic coefficient does not reduce the number
of scalar modes from two to one.**

To isolate the spin-2 part, write the metric equation as

```math
\mathcal E_{\mu\nu}
=\mathcal A_{\mu\nu}
+\mathcal B_{\mu\nu}
 \left[\lambda-\frac{4\alpha}{3}d\right]
+\frac{\alpha}{2}\nabla^\sigma\nabla^\rho
 \mathsf C_{\mu\rho\nu\sigma}=0
\tag{14}
```

in the following form:

```math
\begin{aligned}
\mathcal A_{\mu\nu}
&=\delta R_{\mu\nu}+2g^2h_{\mu\nu}
-\frac12\bar g_{\mu\nu}r,\\
\mathcal B_{\mu\nu}[u]
&=(\bar g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu
-2g^2\bar g_{\mu\nu})u.
\end{aligned}
```

In the spin-2 projection of this equation, with $`k=-g^2/2`$ the background
sectional curvature,

```math
\begin{aligned}
\mathcal A_{\mu\nu}^{(2)}
&=-\frac12(\Box-2k)h_{\mu\nu}^{(2)},\\
\nabla^\sigma\nabla^\rho
\mathsf C_{\mu\rho\nu\sigma}^{(2)}
&=\frac23(\Box-5k)\mathcal A_{\mu\nu}^{(2)}.
\end{aligned}
```

Thus

```math
\boxed{
(\Box+g^2)
\left(\Box+\frac{5g^2}{2}+\frac3\alpha\right)
h_{\mu\nu}^{(2)}=0.}
\tag{15}
```

Here

```math
\nabla^\mu h_{\mu\nu}^{(2)}=0,\qquad
h^{(2)\mu}{}_\mu=0
```

This defines only the spin-2 component. The superscript $`(2)`$
in this section denotes the spin-2 projection. **The trace of the total
$`h_{\mu\nu}`$ has not been set to zero:** its scalar content remains in (9)–(11).

In the generic case, the spin-2 count is

```math
\underbrace{15-2(5)}_{\text{massless}}=5,\qquad
\underbrace{15-5-1}_{\text{massive}}=9
\tag{16}
```


<a id="3-coupled-analysis-of-the-formvector-sector"></a>

### Coupled analysis of the form–vector sector

Examine the form–vector sector using variables that retain
the $`g`$ mixing:

```math
U_{ab}:=\frac16\bar\varepsilon_{abcde}\mathsf H^{cde},
\qquad F_{ab}:=\mathsf G_{ab}+U_{ab}=8\tau_{ab},
\qquad j_X^b:=\nabla_aX^{ab}.
\tag{17}
```

These introduce no new independent fields. $`U`$ is a defined dual
combination used in this calculation; the convention for the fundamental
three-form $`\mathsf H`$ is unchanged. In particular,

```math
\begin{aligned}
j_U^\mu
&=-\frac16\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu\mathsf H_{\rho\sigma\lambda}\\
&=-\frac g{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\nabla_\nu a_{\rho\sigma\lambda}
=g\,p^\mu,
\end{aligned}
\tag{18}
```

and

```math
\mathsf H^2=-3U^2,\qquad
p^\mu=\frac1g(j_F^\mu-j_{\mathsf G}^\mu).
\tag{19}
```

The identities needed to organize derivatives in the quadratic Weyl block are:

```math
\begin{aligned}
\int\bar e\,\nabla_bF_{ac}\nabla^aF^{bc}
&=\int\bar e\left(j_F^2+\frac{3g^2}{2}F^2\right),\\
\int\bar e\,F_{ab}\nabla^b\nabla_cF^{ac}
&=-\int\bar e\,j_F^2,\\
(dF)^2&=3(\nabla F)^2
-6\nabla_bF_{ac}\nabla^aF^{bc}.
\end{aligned}
\tag{20}
```

These equalities hold modulo boundary terms from the indicated
integrations by parts.

The total form block then becomes

```math
\boxed{\begin{aligned}
\mathcal L_{\rm form}\simeq{}&
-\frac32\mathsf G^2
+\left(1-\frac{\alpha g^2}{6}\right)F^2
-\frac{\alpha}{9}(dF)^2+\frac{\alpha}{3}j_F^2\\
&-\frac2{g^2}(j_F-j_{\mathsf G})^2
-\frac{\alpha}{6}\mathsf v^2\\
&+\frac{\sqrt2}{g}
 \left(1-\frac{\alpha g^2}{6}\right)F_{ab}\mathsf v^{ab}
-\frac{\sqrt2}{g}\mathsf G_{ab}\mathsf v^{ab}
\end{aligned}}
\tag{21}
```

In particular, none of the conditions $`p=0`$, $`U=0`$, or $`v=-\sqrt2g\,c`$
has been imposed.

The divergence-free two-form component $`F^\perp`$ separates
from the vector components:

```math
j_{F^\perp}=0.
```

Equation

```math
\left(1-\frac{\alpha g^2}{6}\right)F^\perp_{ab}
+\frac{\alpha}{3}\nabla^c(dF^\perp)_{cab}=0.
```

```math
\nabla^c(dF^\perp)_{cab}=(\Box+3g^2)F^\perp_{ab}
```

using this relation,

```math
\boxed{
\left(\Box+\frac{5g^2}{2}+\frac3\alpha\right)
F^\perp_{ab}=0.}
\tag{22}
```

In the generic case, this sector has the polarization count

```math
\binom42=6
\tag{23}
```


In the vector part, use the representation $`F=dA`$.
$`A`$ is only the potential for this decomposition; it is not added
to the independent-field inventory. Denote the Maxwell operator
on transverse vectors by

```math
tA^\mu:=\nabla_\nu(dA)^{\nu\mu}
=(\Box+2g^2)A^\mu
\tag{24}
```

Here $`t`$ is a symbolic differential operator in the determinant below.

```math
a_0:=1-\frac{\alpha g^2}{6}
```

With this definition, the coupled matrix for $`(A,c,v)`$ is

```math
M(t)=
\begin{pmatrix}
-2a_0+\left(\frac\alpha3-\frac2{g^2}\right)t
&\frac{2t}{g^2}&-\frac{\sqrt2a_0}{g}\\
\frac{2t}{g^2}&3-\frac{2t}{g^2}&\frac{\sqrt2}{g}\\
-\frac{\sqrt2a_0}{g}&\frac{\sqrt2}{g}&\frac\alpha3
\end{pmatrix}
\tag{25}
```


The full $`F`$ equation gives the first row; the $`c,v`$ equations
give the second and third rows, respectively, with factors $`t`$.
Thus the characteristic factor is

```math
t^2\det M(t)
\tag{26}
```

After writing $`F=dA`$, one does not vary only $`A`$ and count
an extra $`t`$ root.

Determinant:

```math
\boxed{
\det M(t)=-
\frac{
4\alpha^2t^2+(24\alpha-4\alpha^2g^2)t
+36+12\alpha g^2-3\alpha^2g^4}
{18g^2}.}
\tag{27}
```

Thus the generic system has two Maxwell branches and two additional
vector branches:

```math
2(5-2)+2(5-1)=6+8=14.
\tag{28}
```

The total form–vector count is

```math
\boxed{6+14=20}
\tag{29}
```

bosonic degrees of freedom.

The derivative coefficients of the coupled higher-derivative vector part
also give

```math
\det
\begin{pmatrix}
\frac\alpha3-\frac2{g^2}&\frac2{g^2}\\
\frac2{g^2}&-\frac2{g^2}
\end{pmatrix}
=-\frac{2\alpha}{3g^2}\neq0
\tag{30}
```

Vanishing of one diagonal coefficient does not make the dynamical
rank of this coupled system vanish.

The equation for the traceless internal connection is

```math
4v'^{\mu ij}
+\frac{4\alpha}{3}\nabla_\nu\mathsf V'^{\nu\mu ij}=0.
```

Taking its divergence gives

```math
\nabla_\mu v'^{\mu ij}=0,
\tag{31}
```

followed by

```math
\boxed{
\left(\Box+2g^2+\frac3\alpha\right)v'_\mu{}^{ij}=0.}
\tag{32}
```

Each of the two internal components carries four polarizations:

```math
2\times4=8.
\tag{33}
```

Thus $`V'`$ is not an auxiliary connection in the total theory.

<a id="4-fermionic-constraints-and-dynamical-modes"></a>

### Fermionic constraints and dynamical modes

To display the fermionic constraints, temporarily write

```math
m:=\frac{ig}{2\sqrt2}J,\qquad m^2=\frac{g^2}{8},
\qquad
q:=\gamma^a\Psi_a,\qquad
A:=\gamma^{ab}\nabla_a\Psi_b
=\mathord{\not{\nabla}} q-\nabla^a\Psi_a
\tag{34}
```

Here $`m`$ is a defined internal matrix, not a freely selected mass
parameter. The $`A`$ of this section is a spinor and must be distinguished
from the vector potential $`A_\mu`$ in the [quadratic field definitions](../quadratic_action.md).

The dependent-spinor fluctuation is

```math
\mathcal X
=\frac1{32}(A-4mq+4g\zeta)
\tag{35}
```

Under local SUSY,

```math
\delta q=(\mathord{\not{\nabla}}+5m)\epsilon,\qquad
\delta A=4m(\mathord{\not{\nabla}}+5m)\epsilon,
```

and therefore

```math
\delta\mathcal X=0.
\tag{36}
```

Setting $`\mathcal X`$ to zero is not a gauge choice.

Retaining Grassmann signs, the gamma trace of the total fermion equation
and the $`\zeta`$ equation give

```math
\begin{aligned}
\gamma_a\mathcal F_\Psi^a
={}&\left[
\frac{32\alpha}{3}(\mathord{\not{\nabla}}-5m)
(\mathord{\not{\nabla}}-m)-96\right]\mathcal X\\
&+\frac{16m}{g}(\mathord{\not{\nabla}}+m)\zeta,\\
\mathcal F_\zeta
={}&2(\mathord{\not{\nabla}}+m)\zeta
-\left[\frac{128m}{g}
+\frac{32\alpha g}{3}(\mathord{\not{\nabla}}-m)\right]\mathcal X .
\end{aligned}
\tag{37}
```

Their combination is

```math
\begin{aligned}
\gamma_a\mathcal F_\Psi^a-\frac{8m}{g}\mathcal F_\zeta
&=32\left[
1+\frac\alpha3(\mathord{\not{\nabla}}+3m)
(\mathord{\not{\nabla}}-m)\right]\mathcal X .
\end{aligned}
```

Result:

```math
\boxed{
\left[
\left(\mathord{\not{\nabla}}+\frac{ig}{2\sqrt2}J\right)^2
-\frac{g^2}{2}+\frac3\alpha
\right]\mathcal X=0.}
\tag{38}
```

The other spin-$`\tfrac12`$ combination is

```math
\zeta_{\mathrm s}:=
\zeta+\frac{64\alpha m}{3g}\mathord{\not{\nabla}}\mathcal X
-\frac{8\alpha g}{3}\mathcal X
\tag{39}
```

Indeed,

```math
\begin{aligned}
(\mathord{\not{\nabla}}+m)\zeta_{\mathrm s}
={}&\frac12\mathcal F_\zeta\\
&+\frac{64\alpha m}{3g}
\left[(\mathord{\not{\nabla}}+m)^2-\frac{g^2}{2}
+\frac3\alpha\right]\mathcal X.
\end{aligned}
```

Thus

```math
\boxed{
\left(\mathord{\not{\nabla}}+\frac{ig}{2\sqrt2}J\right)
\zeta_{\mathrm s}=0.}
\tag{40}
```

Equation (38) gives two first-order spinor branches, and (40) gives one.
The eight real components of a symplectic–Majorana pair correspond
to four propagating polarizations under a first-order equation:

```math
\boxed{2\times4+4=12}
\tag{41}
```

spin-$`\tfrac12`$ degrees of freedom.

This result also determines how the gravitino constraints must be used:

```math
\boxed{
\nabla^a\Psi_a
=\left(\mathord{\not{\nabla}}-\sqrt2\,igJ\right)\gamma^a\Psi_a
+4g\zeta-32\mathcal X.}
\tag{42}
```

For example, in a representative with vanishing gamma trace,

```math
\nabla^a\Psi_a=4g\zeta-32\mathcal X.
\tag{43}
```

Also setting the divergence to zero adds the condition $`\mathcal X=g\zeta/8`$,
which is absent from the general solution, and removes physical
spinor modes.

For the pure spin-$`\tfrac32`$ component, use

```math
\gamma^a\Psi_a^{(3/2)}=0,\qquad
\nabla^a\Psi_a^{(3/2)}=0
\tag{44}
```

These conditions apply only to that spin component, not to the full
gravitino. For the gamma-traceless curvature projector $`P_Q`$,

```math
P_Q(\gamma_{[a}\rho_{b]})=0
```

and on this component,

```math
\begin{aligned}
P_Q\mathord{\not{\nabla}}\mathcal Q[\Psi^{(3/2)}]
&=\frac13\mathcal Q[\mathord{\not{\nabla}}\Psi^{(3/2)}],\\
\nabla_b\mathcal Q^{ba}
&=\frac23\left(\mathord{\not{\nabla}}^2-9m^2\right)
\Psi^{(3/2)a}.
\end{aligned}
\tag{45}
```

The right-hand side of the first identity in (45) is
$`\tfrac13\mathcal Q[\mathord{\not{\nabla}}\Psi^{(3/2)}]`$, not
$`\tfrac13\mathord{\not{\nabla}}\mathcal Q`$.
The distinction arises because $`\mathord{\not{\nabla}}\mathcal Q`$ itself need not be gamma-traceless.
The explicit check, with $`k=-g^2/2=-4m^2`$ and, in this paragraph, $`\Psi=\Psi^{(3/2)}`$, is

```math
\begin{aligned}
\mathcal Q_{ab}[\Psi]
&=2\nabla_{[a}\Psi_{b]}
-\frac23\gamma_{[a}\mathord{\not{\nabla}}\Psi_{b]},\\
\mathord{\not{\nabla}}\mathcal Q_{ab}[\Psi]
&=\frac23\nabla_{[a}\mathord{\not{\nabla}}\Psi_{b]}
+2\gamma_{[a}\left(k+\frac13\mathord{\not{\nabla}}^2\right)\Psi_{b]},\\
P_Q\mathord{\not{\nabla}}\mathcal Q[\Psi]
&=\frac13P_Q\!\left(2\nabla_{[a}\mathord{\not{\nabla}}\Psi_{b]}\right)
=\frac13\mathcal Q[\mathord{\not{\nabla}}\Psi].
\end{aligned}
```

The last line uses $`P_Q(\gamma_{[a}\rho_{b]})=0`$.
This projected identity supplies the factorization below.

The fermion equation therefore factorizes as

```math
\begin{aligned}
0
&=-(\mathord{\not{\nabla}}+3m)
\left[1+\frac\alpha3
(\mathord{\not{\nabla}}+m)(\mathord{\not{\nabla}}-3m)\right]
\Psi_a^{(3/2)}
\end{aligned}
```

with the following factorization:

```math
\boxed{
\left(\mathord{\not{\nabla}}+\frac{3ig}{2\sqrt2}J\right)
\left[
\left(\mathord{\not{\nabla}}-\frac{ig}{2\sqrt2}J\right)^2
-\frac{g^2}{2}+\frac3\alpha
\right]\Psi_a^{(3/2)}=0.}
\tag{46}
```

Generically, there is one massless and two massive gravitino branches.
Constraint count:

| Fermionic branch | Covariant component/constraint count | Propagating count |
|---|---|---:|
| Each massive spin-$`\tfrac32`$ field | $`40-8`$ gamma trace, $`-8`$ divergence; first-order equation | $`12`$ |
| Massless spin-$`\tfrac32`$ field | Same spin projection, plus residual local SUSY equivalence | $`8`$ |
| Each spin-$`\tfrac12`$ field | $`8`$ real components; first-order equation | $`4`$ |

Therefore,

```math
\boxed{N_{3/2}=8+12+12=32,\qquad N_{1/2}=12.}
\tag{47}
```

The eight real SUSY Noether identities prevent the divergence of the
gravitino equation from being counted as eight additional independent
equations. In contrast, the gamma-trace equation in (37) contributes
to the dynamical equation of $`\mathcal X`$; it does not set it to zero algebraically.

<a id="5-special-parameter-conditions"></a>

### Special parameter conditions

Parameter-dependent special cases are determined from the operators
above; no parameter point is selected as an example.

```math
\begin{array}{c|c}
\text{Determining equation}&\text{Result}\\ \hline
2\alpha g^2-3=0&N\text{ equation has a vanishing algebraic solution coefficient}\\
-\frac{3g^2}{2}-\frac3\alpha=0&\alpha g^2=-2\\
\frac{g^2}{2}-\frac3\alpha=0&\alpha g^2=6
\end{array}
\tag{48}
```

Under the condition $`\alpha g^2=-2`$:

```math
\begin{aligned}
\text{spin-2:}\quad&(\Box+g^2)^2h^{(2)}=0,\\
\text{spin-}\tfrac32:\quad&
(\mathord{\not{\nabla}}+3m)^2(\mathord{\not{\nabla}}-5m)
\Psi^{(3/2)}=0,\\
\text{neutral vectors:}\quad&
t^2\det M(t)\ \propto\ t^3(t-4g^2).
\end{aligned}
\tag{49}
```

Under the condition $`\alpha g^2=6`$:

```math
\begin{aligned}
\text{two scalars:}\quad&
(\Box+2g^2)\lambda_{\mathrm s}=0,\qquad
(\Box+2g^2)d=0,\\
\text{spin-}\tfrac12:\quad&
(\mathord{\not{\nabla}}+m)^2\mathcal X=0,\\
\text{spin-}\tfrac32:\quad&
(\mathord{\not{\nabla}}+3m)(\mathord{\not{\nabla}}-m)^2
\Psi^{(3/2)}=0,\\
\text{neutral vectors:}\quad&
t^2\det M(t)\ \propto\ t^4.
\end{aligned}
\tag{50}
```

Under the same condition, (22) reduces to the massless two-form operator.
However, $`j_Fj_{\mathsf G}`$ mixing remains in the full coupled action of $`F`$;
no new independent $`F\to F+d\Lambda_1`$ gauge symmetry follows.

Retaining only ordinary eigenmodes of these repeated factors while
discarding generalized solutions changes the mode count.
**No such boundary condition or truncation has been imposed,
so the coincident branches are retained.**

<a id="6-total-local-physical-content-and-scope-of-the-classification"></a>

### Total local physical content and scope of the classification

The total local count of the generic branches is:

```math
\begin{array}{c|r}
\text{Bosonic sector}&N_B\\ \hline
\text{Massless and massive spin-2}&5+9\\
\text{Coupled metric--}L\text{--}N\text{ scalars}&2\\
(C,V,B_2,E_3)\text{ coupled sector}&20\\
V'^{ij}\text{ sector}&8\\ \hline
\text{Total}&44
\end{array}
\qquad
\begin{array}{c|r}
\text{Fermionic sector}&N_F\\ \hline
\text{Spin-}\tfrac32&8+12+12\\
\text{Spin-}\tfrac12&4+4+4\\ \hline
\text{Total}&44
\end{array}
\tag{51}
```

Thus an auxiliary-field classification inherited from the two-derivative
theory cannot be used for $`V,V',E_3,\varphi`$. The algebraic role of $`N`$ depends
on the condition in (12); $`T,D,\chi`$ and the dependent connections
are always calculated from their definitions.

Here $`44+44`$ counts **local propagating modes** after gauge equivalence;
it is neither a positive-norm count nor a global spectrum admitted
by selected AdS boundary conditions.

<a id="bolum-10"></a>

