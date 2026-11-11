# Gauss–Bonnet on AdS₅: representation check

## Problem and Target

Check the independently derived local spectrum against the AdS₅ superalgebra, without changing any mass to fit a multiplet. The inputs are [Step 11](masses_and_eigenfields.md), (11.3), (11.8), (11.12)–(11.15), and [Step 14](../spectrum.md). This is an on-shell, linearized representation comparison of the action through two physical fermions.

**Verdict: the spectrum matches one massless gravity multiplet and one massless vector multiplet of $`SU(2,2|1)`$, throughout the nondegenerate interior of the selected AdS₅ branch.** This statement compares the standard positive-energy unitary modules compatible with the local operators; it does not select global boundary conditions or prove nonlinear supersymmetry closure.

## Convention Ledger

Retain `GB-FERMION-SPECTRUM-CONVENTIONS-v1`: five-dimensional signature $`-++++`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, unit antisymmetrization, $`\gamma^{01234}=i`$, linear Majorana bar and symplectic Majorana doublets. The accepted action is $`\ell_{2\partial}+\lambda_{\rm GB}(-2\ell_{W,OP}-4\ell_{\log})`$. Set

```math
a=\lambda_{\rm GB}g^2>-\frac12,\quad x=\frac2{1+\sqrt{1+2a}},\quad c=2-x>0,\quad k=-\frac{g^2x^2}{2}=-\frac1{\mathcal L^2},\quad m=\frac{gx}{2\sqrt2},\quad |m|\mathcal L=\frac12.
\tag{R1}
```

$`J^2=-1`$ is the doublet generator used in Step 11; $`iJ`$ has eigenvalues $`\pm1`$. The diagonal fields are $`H_{\mu\nu}=h_{\mu\nu}+2\bar g_{\mu\nu}\ell/(3x)`$ and $`\Upsilon_a=\Psi_a-i\sqrt2\gamma_aJ\zeta/(3x)`$. The form solution is $`G=dA`$, $`H_2=dQ`$, $`db=2*dQ`$, $`v=\sqrt2gx(2Q-A)`$ up to gauge. The symbol $`Q`$ for a dual vector potential is distinct from the supercharge $`\mathsf Q_\alpha`$ below.

Write $`D(E;j_L,j_R)_r`$ for an $`SO(4,2)`$ lowest-weight module with energy $`E`$, $`SO(4)`$ spins $`(j_L,j_R)`$ and R-charge $`r`$. Integer Dynkin labels are $`[j;\bar j]=[2j_L;2j_R]`$. Normalize R-charges so supercharges have magnitude one. Reversing the R-generator and interchanging left/right changes labels, not the conjugate-paired spectrum. The physical doublets carry $`r=\pm1`$ in this normalization; all propagating bosons are neutral.

## Definitions and Required Identities

The CDI entry in the source map identifies the representation conventions. These are taken from Córdova–Dumitrescu–Intriligator, [§2.2.1, Tables 10–12, and §5.5.1, Eq. (5.89)](https://arxiv.org/pdf/1612.00809#page=124). Bulk five-dimensional $`N=2`$ corresponds here to four-dimensional $`N=1`$ superconformal notation. The needed representation data are

```math
\mathsf Q:[1;0]_{1/2}^{(-1)},\quad\overline{\mathsf Q}:[0;1]_{1/2}^{(+1)},\quad E_A=2+j-\frac32r,\quad \bar E_A=2+\bar j+\frac32r.
\tag{R2}
```

At either bound the shortening is $`A_1`$ for a nonzero corresponding Dynkin label and $`A_2`$ for zero. The null condition is the contracted first supercharge in $`A_1`$, and the same-chirality second supercharge in $`A_2`$. These are source inputs. The substitutions, mass comparisons and vector-field assignments below are new calculations using our GB results.

## Detailed Derivation

<a id="1-convert-the-computed-operators-to-energies"></a>

### Convert the computed operators to energies

The scalar equation is $`(\Box-4k)\ell=0`$. Its previously derived radial relation gives

```math
M_0^2\mathcal L^2=4k\mathcal L^2=-4,\qquad E(E-4)=-4\quad\Longrightarrow\quad(E-2)^2=0,\qquad E_0=2.
\tag{R3}
```

For either Maxwell field, in the Poincaré metric with radial gauge and zero boundary momentum, $`\sqrt{-g}\,g^{zz}g^{ij}=\mathcal L z^{-1}\eta^{ij}`$. Its radial equation is $`\partial_z(z^{-1}\partial_z A_i)=0`$. Substituting $`A_i=z^p a_i`$ gives $`p(p-2)z^{p-3}a_i=0`$. The tangent component has one extra power of $`z`$, hence the response weight is $`E=p+1`$. Therefore

```math
p=0,2\quad\Longrightarrow\quad E=1,3,\qquad (E-1)(E-3)=0,\qquad E_1=3
\tag{R4}
```

for the unitary massless-vector module. The $`E=1`$ root is not a second propagating vector multiplet.

For the TT graviton take $`h_{ij}=z^{E-2}t_{ij}`$ with boundary-transverse traceless constant $`t_{ij}`$ and vanishing radial components. The radial and boundary contractions of its two covariant derivatives give $`E^2h_{ij}/\mathcal L^2`$ and $`(-4E-2)h_{ij}/\mathcal L^2`$, respectively: $`\nabla_z h_{ij}=Eh_{ij}/z`$, while $`\nabla_m\nabla_nh_{ij}=-E\eta_{mn}h_{ij}/z^2-\eta_{mi}h_{nj}/z^2-\eta_{mj}h_{in}/z^2`$. Thus

```math
(\Box-2k)h_{ij}=\frac{E^2-4E-2+2}{\mathcal L^2}h_{ij}=\frac{E(E-4)}{\mathcal L^2}h_{ij},\qquad E=0,4,\qquad E_2=4.
\tag{R5}
```

For the physical spinor and transverse gamma-traceless gravitino, the tangential spinor connection gives $`\not\nabla=\mathcal L^{-1}[\gamma^z(z\partial_z-2)+z\gamma^i\partial_i]`$. For a tangent gravitino with zero radial component the additional vector-index connection in this indicial equation vanishes. Insert a radial gamma eigenvector with eigenvalue $`t=\pm1`$:

```math
(\not\nabla+\mu)z^E u_t=0\quad\Longrightarrow\quad t(E-2)+\mu\mathcal L=0,\qquad E_+=2+|\mu|\mathcal L.
\tag{R6}
```

Our independently computed signed parameters are $`\mu_{1/2,s}=sm`$ and $`\mu_{3/2,s}=3sm`$, $`s=\pm1`$. Hence

```math
E_{1/2}=2+\frac12=\frac52,\qquad E_{3/2}=2+\frac32=\frac72.
\tag{R7}
```

The conjugate charge sectors are related by symplectic Majorana reality. Their signed equations are retained; this energy conversion does not square away that distinction.

<a id="2-shortening-and-supercharge-levels"></a>

### Shortening and supercharge levels

For a neutral scalar primary insert $`(j,\bar j,r)=(0,0,0)`$ into (R2): $`E_A=\bar E_A=2`$. Both sides have zero Dynkin label, so its label is $`A_2\bar A_2[0;0]_2^{(0)}`$. Acting with one supercharge adds its spin, charge and energy. The surviving conformal primaries are

```math
[0;0]_2^{(0)}\ \longrightarrow\ [1;0]_{5/2}^{(-1)}\oplus[0;1]_{5/2}^{(+1)}\ \longrightarrow\ [1;1]_3^{(0)}.
\tag{R8}
```

The energies are $`2+1/2=5/2`$ and $`2+1=3`$; the mixed charge is $`-1+1=0`$. The $`A_2`$ null conditions remove $`\mathsf Q^2`$ and $`\overline{\mathsf Q}^{,2}`$ primaries. The anticommutator $`\{\mathsf Q_\alpha,\overline{\mathsf Q}_{\dot\alpha}\}=2P_{\alpha\dot\alpha}`$ separates the mixed primary from the derivative of the scalar. Three-supercharge terms reduce to derivatives, for example

```math
\mathsf Q_\alpha\mathsf Q_\beta\overline{\mathsf Q}_{\dot\alpha}|J\rangle=\overline{\mathsf Q}_{\dot\alpha}\mathsf Q_\alpha\mathsf Q_\beta|J\rangle+2P_{\beta\dot\alpha}\mathsf Q_\alpha|J\rangle-2P_{\alpha\dot\alpha}\mathsf Q_\beta|J\rangle=2P_{\beta\dot\alpha}\mathsf Q_\alpha|J\rangle-2P_{\alpha\dot\alpha}\mathsf Q_\beta|J\rangle.
\tag{R9}
```

The conjugate calculation gives $`2P_{\alpha\dot\beta}\overline{\mathsf Q}_{\dot\alpha}|J\rangle-2P_{\alpha\dot\alpha}\overline{\mathsf Q}_{\dot\beta}|J\rangle`$ for $`\overline{\mathsf Q}_{\dot\alpha}\overline{\mathsf Q}_{\dot\beta}\mathsf Q_\alpha|J\rangle`$. Four-supercharge terms are derivatives of these descendants. There is no additional conformal primary. Equation (R8) is precisely the scalar, spinor and second vector found in our action.

For the neutral vector primary insert $`(j,\bar j,r)=(1,1,0)`$: $`E_A=\bar E_A=3`$. Both labels are nonzero, so the multiplet is $`A_1\bar A_1[1;1]_3^{(0)}`$. The left tensor product is $`[1;0]\otimes[1;1]=[2;1]\oplus[0;1]`$; the $`A_1`$ contracted null removes $`[0;1]`$. The right product is $`[0;1]\otimes[1;1]=[1;2]\oplus[1;0]`$; the right null removes $`[1;0]`$. Therefore

```math
[1;1]_3^{(0)}\ \longrightarrow\ [2;1]_{7/2}^{(-1)}\oplus[1;2]_{7/2}^{(+1)}\ \longrightarrow\ [2;2]_4^{(0)}.
\tag{R10}
```

At the mixed level any undotted contraction obeys $`\mathsf Q^\alpha\overline{\mathsf Q}_{\dot\beta}J_{\alpha\dot\alpha}=2P^\alpha{}_{\dot\beta}J_{\alpha\dot\alpha}`$ because $`\mathsf Q^\alpha J_{\alpha\dot\alpha}=0`$; the dotted contraction is a derivative by the conjugate null condition. Removing derivative descendants leaves only the symmetrized $`[2;2]`$. Contracting both null conditions gives $`2P^{\alpha\dot\alpha}J_{\alpha\dot\alpha}=0`$, the vector conservation law. Applying a second same-chirality supercharge to the first-level contracted null gives $`\mathsf Q^2J_{\alpha\dot\alpha}=0`$ and its conjugate, so the higher levels contain derivatives, as in (R9). This is the vector–gravitino–graviton ladder in our spectrum. Its primary is the vector, not the graviton.

<a id="3-identify-the-two-vector-combinations-from-the-local-transformations"></a>

### Identify the two vector combinations from the local transformations

The accepted [component conventions](../code/references/COMPONENT_CONVENTIONS.md), W01, W02, L01 and the gauged defining-vector realization, give $`T_{ab}=G_{ab}/8-H_{ab}/4`$ and the source-gauge compensator $`\eta_{\rm flux}=\gamma\cdot(G/4-T)\epsilon`$. Use the previously derived form constraints $`p=v'=0`$. In the independent spinor variation the flux terms are

```math
\delta\zeta\big|_F=\frac{x}{\sqrt2}J\gamma\cdot[-T+3(G/4-T)]\epsilon=\frac{x}{\sqrt2}J\gamma\cdot[3G/4-4(G/8-H/4)]\epsilon=\frac{x}{4\sqrt2}J\gamma\cdot(G+4H)\epsilon.
\tag{R11}
```

Thus define $`A_{\rm M}=A+4Q`$. For the shifted gravitino, W01 and $`\beta=i\sqrt2/(3x)`$ give

```math
\begin{aligned}
\delta\Upsilon_a\big|_F&=i\{\gamma\cdot T,\gamma_a\}\epsilon-\frac i4\gamma_a\gamma\cdot G\epsilon-\beta\gamma_aJ\frac{x}{\sqrt2}J\gamma\cdot(G/4+H)\epsilon\\
&=\frac i4\gamma_a{}^{bc}(G-2H)_{bc}\epsilon-\frac i6\gamma_a\gamma^{bc}(G-2H)_{bc}\epsilon.
\end{aligned}
\tag{R12}
```

Here $`\gamma_a{}^{bc}`$ in the first term means the fully antisymmetric rank-three gamma. The Clifford product is $`\gamma_a\gamma^{bc}=\gamma_a{}^{bc}+2\delta_a^{[b}\gamma^{c]}`$, and its reversed product has the opposite contraction term; their sum gives the anticommutator $`2\gamma_a{}^{bc}`$. Also $`-\beta xJ^2/\sqrt2=+i/3`$, so the two coefficients of $`\gamma_a\gamma\cdot G`$ add as $`-i/4+i/12=-i/6`$, while the $`H`$ coefficient is $`i/3`$. These operations give (R12) without a multiplet assumption.

Define $`A_{\rm R}=A-2Q`$. Then $`v=-\sqrt2gxA_{\rm R}`$, so the connection term in the same variation is $`-v_aJ\epsilon/2=(gx/\sqrt2)A_{{\rm R},a}J\epsilon`$. The gravitino flux and connection both isolate $`A_{\rm R}`$, whereas the spinor flux isolates $`A_{\rm M}`$.

The change of variables and its kinetic check are

```math
A=\frac{A_{\rm M}+2A_{\rm R}}3,\quad Q=\frac{A_{\rm M}-A_{\rm R}}6,\qquad -\frac c2G^2-4cH^2=-\frac c{18}(F_{\rm M}+2F_{\rm R})^2-\frac c9(F_{\rm M}-F_{\rm R})^2=-\frac c6F_{\rm M}^2-\frac c3F_{\rm R}^2.
\tag{R13}
```

The cross coefficient is $`-4c/18+2c/9=0`$. The squared coefficients are $`-c/18-c/9=-c/6`$ and $`-4c/18-c/9=-c/3`$. Thus the two vector assignments are also kinetically orthogonal, with positive weights $`Z_{\rm M}=2c/3`$ and $`Z_{\rm R}=4c/3`$ relative to $`-ZF^2/4`$. The input $`-4cH^2`$ here is the Legendre-dualized vector representative derived in Step 12, not direct substitution into the original two-form density.

## Consistency Checks

The mass-to-energy substitutions are $`2(2-4)=-4`$, $`(3-1)(3-3)=0`$, $`4(4-4)=0`$, $`5/2-2=1/2`$ and $`7/2-2=3/2`$. Every supercharge step raises energy by $`1/2`$ and changes R-charge by $`\pm1`$. Both neutral primary bounds are saturated on both sides: $`(E,j,\bar j,r)=(2,0,0,0)`$ and $`(3,1,1,0)`$.

Subtract conservation null states when counting physical polarizations. The vector gives $`2\times2-1=3`$, the graviton $`3\times3-2\times2=5`$, and each chiral gravitino module $`3\times2-2\times1=4`$. Each spinor module gives $`2\times1=2`$; the scalar gives one. Therefore

```math
(N_B,N_F)_{\rm gravity}=(3+5,4+4)=(8,8),\qquad (N_B,N_F)_{\rm vector}=(1+3,2+2)=(4,4),\qquad (N_B,N_F)_{\rm total}=(12,12).
\tag{R14}
```

The conjugate fermion modules form one symplectic Majorana doublet at each spin. No additional doubling is allowed. The scalar BF logarithm is not a second scalar representation. All relative kinetic weights are positive for $`c>0`$; the matter scalar $`\ell/x`$ and spinor $`\zeta/x`$ have the same overall coefficient $`2c/3`$ as the matter vector's Maxwell normalization. At $`a=-1/2`$, $`c=0`$ and all these weights vanish, so this unitary particle interpretation is not extended to that point. In the fixed-$`\lambda`$, $`g\to0`$ contraction, $`k,m\to0`$ and both multiplets retain their $`8+8`$ and $`4+4`$ flat massless counts.

The accompanying [exact checker](../code/calculations/representations.py) reproduces the mass relations, shortening residuals, energy/charge ladder, null-state counts, vector kinetic transformation and both flux combinations. Its [report](../code/outputs/representations.json) is a representation check, not a new action certificate.

## Final Result

In half-integer spin notation, the independently computed spectrum has the following organization:

```math
\begin{aligned}
\mathcal G&=D(3;\tfrac12,\tfrac12)_0\oplus D(\tfrac72;1,\tfrac12)_{-1}\oplus D(\tfrac72;\tfrac12,1)_{+1}\oplus D(4;1,1)_0,\\
\mathcal V&=D(2;0,0)_0\oplus D(\tfrac52;\tfrac12,0)_{-1}\oplus D(\tfrac52;0,\tfrac12)_{+1}\oplus D(3;\tfrac12,\tfrac12)_0,\\
\boxed{\mathcal S_{\rm GB-S_+}=\mathcal G\oplus\mathcal V,\qquad \mathcal G:\ (H_{\mu\nu},\Upsilon_\mu,A-2Q),\quad \mathcal V:\ (\ell,\zeta,A+4Q).}
\end{aligned}
\tag{R15}
```

Equivalently the labels are $`A_1\bar A_1[1;1]_3^{(0)}`$ and $`A_2\bar A_2[0;0]_2^{(0)}`$. The latter is the bulk massless vector multiplet associated with a four-dimensional conserved-current multiplet; it is not a free boundary vector singleton.

## Convention Dependence and Scope

The charge/chirality orientation can be reversed together. The representation content, absolute energies, kinetic signs and counts are unchanged. Standard unitary positive-energy modules are used for this comparison; no global boundary Hilbert space or choice of BF logarithmic data has been imposed. Full transformation-law intertwining and closure on every eigenfield are stronger tests than this representation comparison. Equations (R11)–(R13) supply an explicit vector assignment and a partial linear-transformation check, not a substitute for that complete closure calculation. The critical endpoint remains outside a nondegenerate quadratic particle description.
