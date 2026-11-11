# Fermionic quadratic collection: full descendants and explicit coefficient sums

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, action_lock=GB-FERMION-ACTION-0+2-v1, fermion_bar=linear_Majorana, variation=left -->

This calculation uses only GB-FINAL-DENSITY. The [two-derivative and Weyl calculation](../code/derivations/support/gb-splus-fermionic-expansion-EXPLAIN.md), equations F1–F29, displays every two-derivative insertion and the surviving Weyl terms. The [descendant calculation](../code/derivations/support/part2_fermion_descendant_check.md), SF1–SF19, expands the required Q/S/K contributions. Both are parts of the present calculation, not separately sourced actions.

## F.1 Fields and evaluated descendants

Define $`m=gx/(2\sqrt2)`$, $`u=3x/\sqrt2`$, and $`J(\zeta^1,\zeta^2)=(-\zeta^2,\zeta^1)`$, so $`J^2=-1`$ and $`k=-4m^2`$. A contracted pairing means $`\bar A^iB_i`$; a pairing carrying $`\delta_{ij}`$ is written explicitly. In particular $`\delta_{ij}\bar A^iB^j=-\bar A J B`$. From $`\gamma_a^T\mathsf C=\mathsf C\gamma_a`$ and $`J^T=-J`$, $`\overline{\gamma_aJ\zeta}\,B=-\bar\zeta\gamma_aJ B`$ in contracted-doublet notation. This sign is used in the Majorana field shift.

The temporary letters below abbreviate evaluated linear polynomials, not independent variables or unexpanded full derivatives:

```math
\begin{aligned}
R'_{ab}&=\nabla_a\Psi_b-\nabla_b\Psi_a,\qquad \phi_a=\frac i3\gamma^bR'_{ab}-\frac i{24}\gamma_a\gamma^{bc}R'_{bc},\qquad R_{ab}=R'_{ab}-i\gamma_a\phi_b+i\gamma_b\phi_a,\\
d_a&=-mJ\Psi_a-\frac i3\gamma^b(\nabla_a\Psi_b-\nabla_b\Psi_a)+\frac i{24}\gamma_a\gamma^{bc}(\nabla_b\Psi_c-\nabla_c\Psi_b),\qquad \chi=\frac i8\gamma^ad_a+\frac g8\zeta,\\
q_a&=\nabla_a\zeta+uJd_a,\qquad d_{ab}=\nabla_a d_b+im\gamma_bJd_a,\qquad q_{ab}=\nabla_aq_b-ium\gamma_bd_a+7m^2\eta_{ab}\zeta-m^2\gamma_{ba}\zeta.
\end{aligned}
\tag{FC1}
```

Here $`R`$ without a spacetime scalar index in this appendix is the linear $`Q`$ curvature, and obeys $`\gamma^aR_{ab}=0`$ by its defining projection. Every $`\nabla`$ acts on all its displayed tangent and spinor indices. For example $`d_{ab}`$ equals the original full $`\mathcal D_a\mathcal D_b\psi|_1`$, not $`\nabla_a\nabla_b`$ acting on a vanished dilatino. The source identities and their substitution are

```math
\begin{aligned}
\mathcal D_a\mathcal D_b\psi\big|_1&=\nabla_ad_b-\frac{ik}{4}\gamma_b\Psi_a-im\gamma_bJ\phi_a=\nabla_ad_b+im^2\gamma_b\Psi_a+im\gamma_bJd_a+im^2\gamma_bJ^2\Psi_a=d_{ab},\\
\mathcal D_a\varphi\big|_1&=\nabla_a\zeta-\frac{N_0}{2}\Psi_a-uJ\phi_a=\nabla_a\zeta+\frac34gx^2\Psi_a+uJd_a+umJ^2\Psi_a=q_a.
\end{aligned}
\tag{FC2}
```

The $`\Psi_a`$ terms cancel since $`um=3gx^2/4`$. Equation SF5 derives $`q_{ab}`$, including its weight-$`7/2`$ K term; its trace is $`q^a{}_a=\nabla^aq_a-ium\gamma^ad_a-35k\zeta/4`$. The full first derivatives of $`R`$ and $`\chi`$ equal $`\nabla R`$ and $`\nabla\chi`$ at this order, since each additional Q/S connection multiplies $`\bar D,\bar T,\bar C,\overline{R(V)}`$ or $`\overline{\mathcal DT}`$, all zero.

## F.2 Surviving source terms and implicit bilinears

Of the 52 Weyl outer terms, precisely Weyl_sigma_N:12,15 and Weyl_Y:4,5 survive in the fermionic quadratic block. They give

```math
\ell^{(2)}_{W,F}=-\frac32\bar R_{ab}\gamma^c\nabla_cR^{ab}+\frac{512}{3}\bar\chi\gamma^a\nabla_a\chi+\frac{igx}{4\sqrt2}\delta_{ij}\bar R_{ab}^{,i}R^{abj}+\frac{256igx}{3\sqrt2}\delta_{ij}\bar\chi^i\chi^j.
\tag{FC3}
```

Among LOG_seed terms, only 46–48,71,74,76 have implicit quadratic fermions on this background. The coefficient of $`[\Box^c\sigma]_2`$ before the Hessian square is

```math
-\frac{20}{3}\left(-\frac52k\right)-\frac{26}{3}(-2k)-\frac{32}{3}(3k)=2k.
\tag{FC4}
```

The variation of $`6(\mathcal D_a\mathcal D_b\sigma)^2`$ supplies $`12(-k\eta^{ab}/2)[\mathcal D_a\mathcal D_b\sigma]_2=-6k[\Box^c\sigma]_2`$. Thus the complete implicit contribution is $`-4k[\Box^c\sigma]_2+2g^2L_{ij}[\Box^c L^{ij}]_2+4g[\Box^cN]_2`$.

The ordered primed curvature must be traced before using any symmetry. Its $`R(Q)`$ terms have zero scalar trace, the contorsion trace is a divergence, and its last term is $`2(1-5-5+1)\bar\Psi_a\gamma^a\chi=-16\bar\Psi_a\gamma^a\chi`$. Therefore

```math
[\mathcal R]_2\doteq i\bar\phi_a\gamma^{ab}\Psi_b-16\bar\Psi_a\gamma^a\chi,\qquad [f_a{}^a]_2\doteq-\frac i{16}\bar\phi_a\gamma^{ab}\Psi_b+\bar\Psi_a\gamma^a\chi.
\tag{FC5}
```

Using this trace, SF15–SF16 give the fully evaluated boxes needed here:

```math
\begin{aligned}
[\Box^c\sigma]_2&\doteq-\frac i8\bar\phi_a\gamma^{ab}\Psi_b-\frac i2\bar\Psi^ad_a,\\
L_{ij}[\Box^cL^{ij}]_2&\doteq-\frac{3ix^2}{8}\bar\phi_a\gamma^{ab}\Psi_b-\frac{ix}{\sqrt2}\delta_{ij}\bar\Psi^{ai}q_a^j+\frac{x}{\sqrt2}\delta_{ij}\bar\zeta^i\gamma^a\phi_a^j,\\
[\Box^cN]_2&\doteq-\frac{iN_0}{2}\bar\phi_a\gamma^{ab}\Psi_b-\frac12\bar\Psi^a\gamma^bq_{ab}-\frac{4ix}{\sqrt2}\delta_{ij}\bar\Psi^{ai}\nabla_a\chi^j-\frac{3i}{2}\bar\phi^aq_a-\frac i2\bar\phi^a\gamma_a\gamma^bq_b+\frac{4x}{\sqrt2}\delta_{ij}\bar\phi^{ai}\gamma_a\chi^j.
\end{aligned}
\tag{FC6}
```

Their divergences are explicitly retained before integration in SF7, SF12–SF15. At the constant coefficients in this quadratic block they contribute only local boundary currents. None of (FC5)–(FC6) symmetrizes the fermionic $`f_{ab}`$.

The LOG input used at the next step is fixed by the
[component conventions](../code/references/LOG_MASTER.md#log-conventions),
[gauged composite derivation](../code/references/LOG_MASTER.md#gauged-composite-derivation)
and [descendant-to-density insertion](../code/references/LOG_MASTER.md#log-descendants-density).
These sections specify the inherited coefficients before the AdS reduction;
the calculation below evaluates them without changing their normalization.

## F.3 Explicit LOG terms: collection before eliminating the dependent spinors

The [source-order ledger](../code/derivations/spectrum/SOURCE_TERM_LEDGER.md) lists all 1184 outer entries and their sector routes. There are 53 potentially surviving explicit LOG bilinears. The gamma-trace and duality reductions used on them are

```math
\varepsilon_{abcde}\bar R^{ab}\gamma^{de}=0,\qquad \varepsilon_{abcde}\bar R^{bc}\gamma^d=-2i\bar R_{ae},\qquad \varepsilon_{abcde}\bar R^{ab}\gamma^eR^{cd}=2i\bar R_{ab}R^{ab},\qquad \varepsilon_{abcde}\gamma^{ab}=2i\gamma_{cde}.
\tag{FC7}
```

For the first identity, insert the rank-two/rank-three duality of C04c; the resulting $`\bar R_{ab}\gamma^{abc}`$ is zero because expanding $`\gamma^{abc}=\gamma^{ab}\gamma^c-2\eta^{c[b}\gamma^{a]}`$ contracts a gamma trace in each term. For the second, expand the rank-four product in the duality formula: terms containing $`\bar R_{bc}\gamma^b`$ or $`\bar R_{bc}\gamma^{bc}`$ vanish, leaving $`-2i\bar R_{ae}`$. The third is the second with the free pair interchanged and contracted with $`R^{cd}`$; the permutation contributes the additional minus. The Clifford matrices used below independently check these contractions in signature $`-++++`$.

Thus terms 31,52,59 vanish. Terms 60 and 61 cancel as $`(i/256)\,gL\bar RR-(1/512)(2i)\,gL\bar RR=0`$. Terms 29 and 30 add $`(81i/64+111i/64)\overline{\nabla^aR_{ab}}d^b=3i\overline{\nabla^aR_{ab}}d^b`$. Applying the same displayed duality to term 32 gives $`(i/3)(2i)\bar d_c\gamma^{cde}d_{de}=-2\bar d_c\gamma^{cde}d_{de}/3`$.

The remaining first group, in source order with these cancellations made, is

```math
\begin{aligned}
\ell_{29\text{--}62}={}&3i\overline{\nabla^aR_{ab}}d^b-\frac23\bar d_c\gamma^{cde}d_{de}-\frac{10}{3}\bar d_a\gamma^ad^b{}_b+\frac23\bar d^b\gamma^ad_{ab}+\frac{16}{3}\bar d^b\gamma^ad_{ba}\\
&-\frac{3igx}{\sqrt2}\delta_{ij}\bar d_a^i\gamma^{ab}d_b^j-\frac{12igx}{\sqrt2}\delta_{ij}\bar d^{ai}d_a^j-\frac{10ig}{3}\bar q^a\gamma_a{}^bd_b+\frac{26ig}{3}\bar q^ad_a-\frac{10ig}{3}\bar\zeta\gamma^{ab}d_{ab}+\frac{10ig}{3}\bar\zeta d^a{}_a\\
&-\frac{35g^2x}{3\sqrt2}\delta_{ij}\bar\zeta^i\gamma^ad_a^j-\frac{2g^2}{3}\bar\zeta\gamma^aq_a+\frac{17ig^3x}{3\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j.
\end{aligned}
\tag{FC8}
```

For the second group, 394 and 397/400 vanish by symmetric-Hessian contraction, 395/396 and 401/402 cancel pairwise. Terms 315/318/321 produce $`-5ik`$ for each of $`\bar\Psi_a\gamma^{ab}d_b`$ and $`\bar\Psi^ad_a`$. Terms 370/371 add $`-5ik/2`$ and 398/399 add $`+ik`$, giving $`-13ik/2`$. Terms 360/361 contribute $`-5ig^2x^2/4`$ after the two $`L`$ matrices are contracted, so $`-13ik/2-5ig^2x^2/4=2ig^2x^2`$. The scalar mixing from 317/320/323 is $`(-25/6+7/6-1)gk=-4gk=2g^3x^2`$. The mass coefficient from 822/824/826/827 is $`(-5/2-2+9-15/2)igxk/\sqrt2=-3igxk/\sqrt2`$. This gives

```math
\begin{aligned}
\ell_{315\text{--}827}={}&2ig^2x^2\bar\Psi_a\gamma^a\gamma^bd_b+2g^3x^2\bar\zeta\gamma^a\Psi_a+\frac{4ig^2x}{\sqrt2}\delta_{ij}\bar q^{ai}\gamma_a\gamma^b\Psi_b^j-\frac{4gx}{\sqrt2}\delta_{ij}\bar\Psi_c^i\gamma^{cde}d_{de}^j\\
&+\frac{4gx}{\sqrt2}\delta_{ij}\bar\Psi^{bi}\gamma^a(d_{ab}^j-d_{ba}^j)-\frac{2gx}{\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^ad^b{}_{b}{}^j-2g\overline{q^a{}_a}\gamma^b\Psi_b-\frac{3igxk}{\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j.
\end{aligned}
\tag{FC9}
```

The combination $`\gamma^{ab}+\eta^{ab}=\gamma^a\gamma^b`$ is responsible for the first and third terms. Equations (FC3), (FC6), (FC8), (FC9) display the entire fermionic higher-derivative quadratic action before eliminating dependent spinor expressions.

## F.4 Explicit component reduction and its domain

To keep the final Clifford collection reproducible, [the component-sum appendix](../code/derivations/spectrum/FERMION_COMPONENT_SUMS.md) gives every nonzero coefficient pattern of the graded Euler operator separately for (FC3), (FC8), (FC9), the sigma/L part of (FC6), and its N part. Each row adds these five polynomials and displays its collected result. Entries absent from the table vanish in all five contributions. This is a local component evaluation of (FC1), with all fields unconstrained; it imposes no gamma trace, divergence or physical eigenvalue.

The frame used to display that finite arithmetic is $`e^a=dx^a/z`$ with radial direction $`a=4`$, $`k=-1`$, $`g=1`$, $`x=\sqrt2`$. Then $`m=1/2,u=3,N_0=-3`$. Its nonzero connection entries are $`\omega_{a a}{}^4=-\eta_{aa}`$ and $`\omega_{a4}{}^a=1`$ for $`a=0,1,2,3`$, and the spinor connection is $`-\gamma_{a4}/2`$. For arbitrary radial exponent $`s`$,

```math
\nabla_a\zeta=\begin{cases}-\gamma_{a4}\zeta/2,&a<4,\\s\zeta,&a=4,\end{cases}\qquad \nabla_a\Psi_b=(\nabla_a|_{\rm spin})\Psi_b+\omega_{ab}{}^c\Psi_c,
\tag{FC10}
```

with a second tangent connection for $`R_{bc}`$. This explicitly generates each derivative in (FC1). $`s`$ is a test jet variable, not a spectrum or boundary exponent being selected. The radial integration-by-parts rule follows from $`\partial_z(z^{-4})=-4z^{-5}`$:

```math
\int dz\,z^{-5}A^T(z\partial_zB)=-\int dz\,z^{-5}[(z\partial_z-4)A]^TB+\left[z^{-4}A^TB\right]_{\partial},\qquad (z\partial_z)^*=4-z\partial_z.
\tag{FC11}
```

For a bilinear $`(L\Psi)^T\mathsf B(R\Psi)`$ the Euler coefficient is $`L(4-s)^T\mathsf B R(s)-[L(s)^T\mathsf B R(4-s)]^T`$. This minus is the exchange of two odd fields in a left variation. Use $`\mathsf B=J\otimes\mathsf C`$ for contracted doublets and $`\mathbf1\otimes\mathsf C`$ for explicit $`\delta_{ij}`$. The Clifford matrices are

```math
\gamma^0=-i\sigma_3\otimes\mathbf1,\quad \gamma^1=\sigma_1\otimes\sigma_1,\quad \gamma^2=\sigma_1\otimes\sigma_2,\quad \gamma^3=\sigma_1\otimes\sigma_3,\quad \gamma^4=\sigma_2\otimes\mathbf1,\quad \mathsf C=\gamma^2\gamma^4.
\tag{FC12}
```

They satisfy $`\gamma^{01234}=i`$, $`\mathsf C^T=-\mathsf C`$, and $`\gamma_a^T\mathsf C=\mathsf C\gamma_a`$. The table explicitly records the cancellation of every $`s^3`$ and $`s^2`$ coefficient. Each polynomial has degree at most three, so four exact values determine it; a fifth independently checks the interpolation. The [exact operator script](../code/calculations/fermion_operator.py) checks all $`48^2`$ entries for each value, with exact rational/Clifford arithmetic.

Restoring parameters is fixed before this evaluation by (FC1), (FC3), (FC6), (FC8), (FC9): put $`\zeta=x\zeta_*`$ and scale derivatives by $`gx`$. Every higher-derivative quadratic term is proportional to $`(gx)^3`$ times a dimensionless bilinear in $`\Psi,\zeta_*`$, with the same $`k/(gx)^2=-1/2`$. Thus no independent dimensionless coupling or compensator parameter is lost in the displayed frame. A Lorentz-covariant local operator identity is fixed by these unrestricted spinor/vector components and arbitrary non-null derivative direction; curvature commutators are included through the full connection. More explicitly, start with the difference of the source and collected operators. Its cubic principal symbol vanishes for all components and for a spacelike derivative direction. Lorentz covariance rotates this result to every spacelike direction; a polynomial that vanishes on that open set is identically zero. Subtract that vanishing symbol and repeat for the quadratic and linear symbols. The remaining algebraic curvature terms are then fixed by the constant coefficient. This descending-order argument is why the radial display suffices; it does not assume commutation of the covariant derivatives. No field equation or gauge quotient enters this test.

The collected higher-derivative representative is

```math
\boxed{\ell^{(2)}_{\rm GB,F}\doteq-g^2x^2\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c+2g^2\bar\zeta\not\nabla\zeta-2\sqrt2ig^2x\delta_{ij}\bar\Psi_a^i\gamma^{ab}\nabla_b\zeta^j-\frac{ig^3x^3}{\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j-3g^3x^2\bar\Psi_a\gamma^a\zeta+\frac{7ig^3x}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j.}
\tag{FC13}
```

As a direct check before any gravitino manipulation, set $`\Psi=0`$. Then $`d=\phi=R=0`$, $`\chi=g\zeta/8`$, $`q=\nabla\zeta`$. The surviving derivative coefficient is $`(512/3)(g^2/64)-2g^2/3=2g^2`$; the mass coefficient is $`(256/3)(g^2/64)igx/\sqrt2+(17/3)ig^3x/\sqrt2=7ig^3x/\sqrt2`$. This independently reproduces both last-field diagonal entries of (FC13).

## F.5 Add the directly expanded two-derivative action

Equation F22 of the companion gives

```math
\ell^{(2)}_{2\partial,F}\doteq-x\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c+\frac2x\bar\zeta\not\nabla\zeta-2\sqrt2i\delta_{ij}\bar\Psi_a^i\gamma^{ab}\nabla_b\zeta^j-\frac{igx(x+2)}{2\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j-2g(x+1)\bar\Psi_a\gamma^a\zeta+\frac{7ig}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j.
\tag{FC14}
```

Adding $`\lambda`$ times (FC13) produces the six independent coefficient sums

```math
\begin{aligned}
\bar\Psi\gamma^{abc}\nabla\Psi:&\ -x-ax^2=-c,\qquad \bar\zeta\not\nabla\zeta:\ \frac2x+2a=\frac{2c}{x^2},\qquad \delta\bar\Psi\gamma^{ab}\nabla\zeta:\ -2\sqrt2i(1+ax)=-\frac{2\sqrt2ic}{x},\\
\delta\bar\Psi\gamma^{ab}\Psi:&\ -\frac{igx}{2\sqrt2}(x+2+2ax^2)=-\frac{3igxc}{2\sqrt2},\qquad \bar\Psi\gamma\zeta:\ -2g(x+1)-3gax^2=-4gc,\qquad \delta\bar\zeta\zeta:\ \frac{7ig}{\sqrt2}(1+ax)=\frac{7igc}{\sqrt2x}.
\end{aligned}
\tag{FC15}
```

In each equality use $`ax^2=2-2x`$. All six terms have density dimension two after adding the exterior $`\lambda`$ as appropriate. The final raw action in Step 6 uses only the original independent $`\Psi,\zeta`$ and ordinary background derivatives.
