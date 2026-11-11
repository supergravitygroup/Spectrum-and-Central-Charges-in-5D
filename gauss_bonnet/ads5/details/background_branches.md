<a id="step-5--all-local-maximally-symmetric-branches"></a>

# All local maximally symmetric branches

The calculation starts from the first-order expansions in [Step 3](../code/derivations/background/STEP_03_FIRST_ORDER_INGREDIENTS.md), not from a reduced-field-equation ansatz. The background density $`F`$ is (4.6) in [Step 4](../code/derivations/background/STEP_04_ZEROTH_ORDER_ACTION.md). $`L,N,k`$ below denote still-independent background constants until a branch is imposed. All solutions are local, real, in the accepted $`L\ne0`$ field patch. This algebraic classification does not impose Killing-spinor conditions; the [selected branch for Gauss–Bonnet on AdS₅](../background.md), which continuously approaches the two-derivative AdS₅ vacuum as the Gauss–Bonnet coupling tends to zero, is discussed with its separate local Killing-spinor analysis.

<a id="51-first-order-terms-before-integrations-by-parts"></a>

## First-order terms before integrations by parts

The two-derivative terms in (3.18) give, by the product rule,

```math
\begin{aligned}
\ell_{2,1}={}&-2\left(\bar\Box\ell-\frac{15}{2}k\ell-\frac38Lr\right)-8\left[\ell D_0+L\left(-\frac r{32}+\frac g4n+\frac{g^2L}{8}\ell\right)\right]\\
&-\frac{4N}{L}n+\frac{2N^2}{L^2}\ell-4gn+4g^2L\ell .
\end{aligned}\tag{5.1}
```

Collect the curvature, scalar and derivative coefficients separately:

```math
\begin{aligned}
[r]:&\quad\frac34L+\frac14L=L,\qquad [n]:\quad-2gL-\frac{4N}{L}-4g,\qquad [\bar\Box\ell]:\quad-2,\\
[\ell]:&\quad15k-8\left(-\frac58k+\frac g4N+\frac{g^2L^2}{16}\right)-g^2L^2+\frac{2N^2}{L^2}+4g^2L\\
&\quad=20k-2gN+\frac{2N^2}{L^2}+4g^2L-\frac32g^2L^2.
\end{aligned}\tag{5.2}
```

For the twelve higher-derivative entries, the complete first-order evaluations are as follows. $`D_0`$ is (3.15); the exterior $`\lambda`$ is suppressed in this table.

| Locator | First-order coefficient from the actual product |
|---|---|
| W2 | $`-\frac{256}{3}D_0(-r/32+gn/4+g^2L\ell/8)`$ |
| L46 | $`-\frac{20}{3}(-5k/2)(-r/8)=-25kr/12`$ |
| L47 | $`-\frac{26}{3}g^2[2L\ell(-5k/2)-L^2r/8]=\frac{130}{3}g^2Lk\ell+\frac{13}{12}g^2L^2r`$ |
| L48 | $`-\frac{32}{3}g[(-5k/2)n-Nr/8]=\frac{80}{3}gkn+\frac43gNr`$ |
| L49 | $`-\frac7{12}g^4(4L^3\ell)=-\frac73g^4L^3\ell`$ |
| L50 | $`-\frac83g^3(L^2n+2NL\ell)`$ |
| L51 | $`\frac23g^2(2Nn)=\frac43g^2Nn`$ |
| L71 | $`2g^2[\ell(-15kL/2)+L(\bar\Box\ell-15k\ell/2-3Lr/8)]=2g^2L\bar\Box\ell-30g^2Lk\ell-\frac34g^2L^2r`$ |
| L74 | $`6(kr/8)=3kr/4`$ |
| L75 | $`3g^2[(\mathcal DL)_0(\mathcal DL)_1+(\mathcal DL)_1(\mathcal DL)_0]=0`$ |
| L76 | $`4g(\bar\Box n-10kn-Nr/2)=4g\bar\Box n-40gkn-2gNr`$ |
| L80 | $`-\frac14g^4(4L^3\ell)=-g^4L^3\ell`$ |

The W2 coefficients, obtained by multiplying its three factors against $`D_0`$, are

```math
\begin{aligned}
[r]_{W2}&=\frac83D_0=-\frac53k+\frac23gN+\frac16g^2L^2,\qquad
[n]_{W2}=-\frac{64}{3}gD_0=\frac{40}{3}gk-\frac{16}{3}g^2N-\frac43g^3L^2,\\
[\ell]_{W2}&=-\frac{32}{3}g^2LD_0=\frac{20}{3}g^2Lk-\frac83g^3LN-\frac23g^4L^3.
\end{aligned}\tag{5.3}
```

Now the actual coefficient sums are

```math
\begin{aligned}
[kr]:&\ -\frac53-\frac{25}{12}+\frac34=-3,\qquad [gNr]:\ \frac23+\frac43-2=0,\qquad [g^2L^2r]:\ \frac16+\frac{13}{12}-\frac34=\frac12,\\
[g^2Lk\ell]:&\ \frac{20}{3}+\frac{130}{3}-30=20,\qquad [g^3LN\ell]:\ -\frac83-\frac{16}{3}=-8,\qquad [g^4L^3\ell]:\ -\frac23-\frac73-1=-4,\\
[gkn]:&\ \frac{40}{3}+\frac{80}{3}-40=0,\qquad [g^2Nn]:\ -\frac{16}{3}+\frac43=-4,\qquad[g^3L^2n]:\ -\frac43-\frac83=-4.
\end{aligned}\tag{5.4}
```

The derivative terms left over are $`2g^2L\bar\Box\ell+4g\bar\Box n`$. Thus the complete measure-inclusive first variation is

```math
\frac{[e\ell_{\rm tot}]_1}{\bar e}=\frac12Fh+Ar+E_L\ell+E_Nn+(-2+2\lambda g^2L)\bar\Box\ell+4\lambda g\bar\Box n,\qquad A=L+\lambda\left(-3k+\frac12g^2L^2\right), \tag{5.5}
```

where the explicitly evaluated scalar coefficients are

```math
\boxed{\begin{aligned}
E_L&=20k+\frac{2N^2}{L^2}-2gN+4g^2L-\frac32g^2L^2+\lambda(20g^2Lk-8g^3NL-4g^4L^3),\\
E_N&=-\frac{4N}{L}-2gL-4g+\lambda(-4g^2N-4g^3L^2).
\end{aligned}}\tag{5.6}
```

<a id="52-integrations-by-parts-and-every-tadpole"></a>

## Integrations by parts and every tadpole

Insert $`r=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}-\bar\Box h-4kh`$ into (5.5). All background coefficients are constants, so, for example, $`\bar e A\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}=\partial_\mu(\bar e A\bar\nabla_\nu h^{\mu\nu})`$. The other three derivative terms give the following total current:

```math
J^\mu=A(\bar\nabla_\nu h^{\mu\nu}-\bar\nabla^\mu h)+(-2+2\lambda g^2L)\bar\nabla^\mu\ell+4\lambda g\bar\nabla^\mu n. \tag{5.7}
```

The first-order action is consequently

```math
\boxed{S^{(1)}=\frac1{2\kappa_5^2}\left\{\int d^5x\,\bar e\,[M\bar g^{\mu\nu}h_{\mu\nu}+E_L\ell+E_Nn]+\int d^5x\,\partial_\mu(\bar eJ^\mu)\right\},\qquad M=\frac12F-4kA.} \tag{5.8}
```

Expanding $`M`$ itself gives the third independent equation:

```math
\boxed{M=6Lk-\frac{N^2}{L}-gLN-2gN+g^2L^2-\frac14g^2L^3+\lambda(-3k^2+3g^2L^2k-g^2N^2-2g^3NL^2-\tfrac12g^4L^4)=0.} \tag{5.9}
```

| Independent variation | Bulk coefficient before any equation is solved | Reason |
|---|---|---|
| $`h_{\mu\nu}`$ | $`M\bar g^{\mu\nu}`$ | (5.5)–(5.9); the traceless coefficient is zero |
| $`\theta_{ab}`$ | $`0`$ | Lorentz rotation of a contracted scalar; $`\theta^a{}_a=0`$, connection rotation cancels the frame rotations |
| $`\ell,n`$ | $`E_L,E_N`$ | (5.1)–(5.6) |
| $`c_\mu`$ | $`0`$ | All strength/potential contributions have at least two zero factors, except the explicit zero contraction (3.16) |
| $`b_{\mu\nu}`$ | $`0`$ | Its first strength enters the same products and (3.16) |
| $`u_{\mu\nu\rho}`$ | $`0`$ | Both its $`g u_3/2`$ contribution to $`H_3`$ and its constrained-current contribution (3.8) multiply a zero factor; no unconstrained-current equation was substituted |
| $`v_\mu,v'_\mu{}^{ij}`$ | $`0`$ | Strength products start at $`t^2`$; the only possible scalar-projected divergence is zero by (3.9) |
| $`\zeta_\mu^i,\xi^i`$ | $`0`$ | Every odd field occurs in an even pair, explicitly expanded in (1.4) |

The density derivative identities $`F_L=E_L`$, $`F_N=E_N`$, $`F_k=20A`$ follow by differentiating (4.6). Hence (4.8) is $`5\epsilon\bar eM`$ and checks (5.9). This agreement is a check of the arbitrary-fluctuation result, not its replacement.

<a id="53-case-partition-before-division"></a>

## Case partition before division

The complete undivided scalar/metric system is $`E_N=E_L=M=0`$ with $`L\ne0`$. We first separate $`g=0`$ and $`g\ne0`$.

### A. Ungauged case: $`g=0`$

Equations (5.6)–(5.9) become

```math
E_N=-4N/L=0\ \Longrightarrow\ N=0,\qquad E_L=20k+2N^2/L^2=0\ \Longrightarrow\ k=0,\qquad M=6Lk-N^2/L-3\lambda k^2=0. \tag{5.10}
```

The last equation is $`0=0`$ after the first two. Thus **GB-U** is Minkowski$`_5`$ with $`N=0`$, arbitrary real $`\lambda`$ and arbitrary $`L\ne0`$. Its constant $`L`$ is an actual modulus in this fixed source gauge; it is not removed by a new compensator gauge choice. The Jacobian of $`(E_L,E_N,M)`$ with respect to $`(L,N,k)`$ is

```math
\left.\frac{\partial(E_L,E_N,M)}{\partial(L,N,k)}\right|_{\mathrm{GB-U}}=\begin{pmatrix}0&0&20\\0&-4/L&0\\0&0&6L\end{pmatrix},\qquad\mathop{\mathrm{rank}}\nolimits=2. \tag{5.11}
```

### B. Gauged case: $`g\ne0`$

Define dimensionless quantities only on this domain:

```math
x=L,\qquad y=N/g,\qquad z=k/g^2,\qquad a=\lambda g^2,\qquad f=F/g^2. \tag{5.12}
```

The three equations, divided only by nonzero $`g`$ or $`g^2`$, are

```math
\begin{aligned}
e_N&=-4y/x-2x-4-4ay-4ax^2=0,\\
e_L&=20z+2y^2/x^2-2y+4x-\tfrac32x^2+a(20xz-8yx-4x^3)=0,\\
m&=6xz-y^2/x-xy-2y+x^2-\tfrac14x^3+a(-3z^2+3x^2z-y^2-2yx^2-\tfrac12x^4)=0.
\end{aligned}\tag{5.13}
```

Here $`e_N=E_N/g`$, $`e_L=E_L/g^2`$, $`m=M/g^2`$. Multiplying the first equation by $`-x/2`$ gives

```math
2(1+ax)y+x(x+2+2ax^2)=0. \tag{5.14}
```

We must split $`1+ax=0`$ before solving this equation for $`y`$.

### B1. Exceptional denominator: $`1+ax=0`$

Set $`a=-1/x`$ directly in (5.14): $`x(x+2-2x)=x(2-x)=0`$. Since $`x\ne0`$, $`x=2`$ and $`a=-1/2`$. Substitution into the original remaining equations gives

```math
\left.e_L\right|_{x=2,a=-1/2}=\frac12(y+6)^2=0,\qquad \left.m\right|_{x=2,a=-1/2}=\frac32(z+2)^2=0. \tag{5.15}
```

Thus **GB-E** is the single point

```math
\boxed{a=-\tfrac12,\quad L=2,\quad N=-6g,\quad k=-2g^2,\qquad g\ne0.} \tag{5.16}
```

Both squares must vanish for real fields; there is no free $`y`$ or $`z`$ modulus. Every entry of the $`3\times3`$ background Jacobian vanishes at this point, but the nonlinear equations (5.14)–(5.15) still isolate it. A zero first Jacobian is not evidence for a family of nearby exact solutions.

### B2. Generic denominator: $`r_0:=1+ax\ne0`$

Introduce $`b_0=x+2+2ax^2`$ solely to show the elimination algebra. Equation (5.14) gives

```math
y=-\frac{xb_0}{2r_0}. \tag{5.17}
```

Insert this into $`e_L`$ and collect its $`z`$ coefficient:

```math
20r_0z=-\frac{b_0^2}{2r_0^2}-\frac{xb_0}{r_0}-4x+\frac32x^2-\frac{4ax^2b_0}{r_0}+4ax^3=-\frac{K}{2r_0^2}. \tag{5.18}
```

The numerator is explicitly

```math
\begin{aligned}
K&=b_0^2+2xb_0r_0(1+4ax)+(8x-3x^2-8ax^3)r_0^2\\
&=8a^3x^5+13a^2x^4+24a^2x^3+4ax^3+44ax^2+16x+4,
\qquad z=-\frac{K}{40r_0^3}.
\end{aligned}\tag{5.19}
```

For transparency, complete the square in the $`y`$-dependent part of $`f`$:

```math
-\frac{2r_0}{x}y^2-2b_0y=-\frac{2r_0}{x}\left(y+\frac{xb_0}{2r_0}\right)^2+\frac{xb_0^2}{2r_0}. \tag{5.20}
```

At (5.17) its value, including the remaining potential, is $`V_0=xb_0^2/(2r_0)+2x^2-x^3/2-ax^4=x(2a^2x^4+ax^3+12ax^2+8x+4)/(2r_0)`$. Thus $`m=3x(2+ax)z-3az^2+V_0/2`$. On putting in (5.19), multiplying by the nonzero denominator gives the polynomial identity

```math
\begin{aligned}
1600r_0^6m&=-120x(2+ax)Kr_0^3-3aK^2+400x(2a^2x^4+ax^3+12ax^2+8x+4)r_0^5\\
&=-(ax^2+2x-2)Q(a,x).
\end{aligned}\tag{5.21}
```

The complete degree-eight factor is

```math
\begin{aligned}
Q(a,x)={}&352a^6x^8+1880a^5x^7+(3859a^4-64a^5)x^6+(3754a^3+352a^4)x^5\\
&+(1700a^2+2030a^3)x^4+(280a+3032a^2-288a^3)x^3+(1720a-540a^2)x^2+(320-216a)x-24a.
\end{aligned}\tag{5.22}
```

The coefficient multiplications in (5.19) and (5.21), and the exact polynomial-division calculations used below, are displayed in [POLYNOMIAL_CALCULATIONS.md](../code/derivations/background/POLYNOMIAL_CALCULATIONS.md). Equations (5.17)–(5.22) are reversible on $`x r_0\ne0`$. Consequently every real allowed root of either factor gives a solution, and every generic solution is among those roots.

<a id="54-simple-family-and-degree-eight-family"></a>

## Simple family and degree-eight family

### GB-S: the simple factor

For $`ax^2+2x-2=0`$, substitution $`a=2(1-x)/x^2`$ into (5.17) and (5.19) yields $`y=-3x^2/2`$ and $`z=-x^2/2`$. One can check the cancellation directly in (5.13):

```math
\begin{aligned}
e_N&=6x-2x-4+6ax^2-4ax^2=2(ax^2+2x-2),\\
e_L&=(-10+\tfrac92+3-\tfrac32)x^2+4x+(-10+12-4)ax^3=-2x(ax^2+2x-2),\\
m&=\left(-3-\tfrac94+\tfrac32-\tfrac14\right)x^3+(3+1)x^2+\left(-\tfrac34-\tfrac32-\tfrac94+3-\tfrac12\right)ax^4=-2x^2(ax^2+2x-2).
\end{aligned}\tag{5.23}
```

Both generic simple roots are therefore

```math
\boxed{x_\pm=\frac{-1\pm\sqrt{1+2a}}a,\qquad N=-\frac32g x_\pm^2,\qquad k=-\frac12g^2x_\pm^2.} \tag{5.24}
```

For the regular root use $`x_+=2/(1+\sqrt{1+2a})`$, which also defines $`x_+(0)=1`$. Existence: $`a\ge-1/2`$; at $`a=-1/2`$ both roots give GB-E and are counted once. For $`-1/2<a<0`$ both are positive. For $`a>0`$, $`x_+>0`$ and $`x_-<0`$. At $`a=0`$, only $`x=1`$ is finite. Each allowed root has $`k<0`$ because $`g\ne0,x\ne0`$.

### GB-Q: every real root of the degree-eight factor

For every real $`x`$ satisfying

```math
\boxed{Q(a,x)=0,\quad x\ne0,\quad 1+ax\ne0,\qquad L=x,\quad N=-g\frac{x(x+2+2ax^2)}{2(1+ax)},\quad k=-g^2\frac{K(a,x)}{40(1+ax)^3},} \tag{5.25}
```

there is a branch entry. This is an exact implicit solution, not a numerical scan. Use the stable family ID **GB-Q** and identify an individual entry by its coupling cell below and its increasing real-root index $`j`$. For example, `GB-Q:I3:j4` is the fourth real root in cell I3. At cell boundaries the explicit merger maps below identify continuations; a repeated root counts once.

There is no simple/Q overlap in the generic domain. Polynomial division gives $`Q\bmod (ax^2+2x-2)=-640(2a+1)^3(x-1)/a`$ for $`a\ne0`$. Its vanishing at $`x=1`$ would require the simple equation $`a=0`$, outside that division; at $`a=-1/2`$ it leads back to the separately solved exceptional point. The resultant is $`409600a^6(2a+1)^6`$ and confirms the same partition.

At $`a=0`$, the original equations, without $`r_0`$ problems, give $`y=-x(x+2)/2`$ and $`z=-(4x+1)/10`$. Substitution into $`m`$ gives $`m=-2x(x-1)/5`$. Since $`x\ne0`$, the unique solution is the selected $`x_+`$ branch with $`(x,y,z)=(1,-3/2,-1/2)`$. The apparent Q root $`Q(0,x)=320x=0`$ is on the excluded patch boundary.

At $`a=-1/2`$, the generic Q factor is

```math
Q(-\tfrac12,x)=\frac1{16}(x-2)^6(88x^2+116x+3). \tag{5.26}
```

The root $`x=2`$ is handled by GB-E, not by (5.25). The two additional solutions have

```math
x=\frac{-29\pm5\sqrt{31}}{44}<0,\qquad y=-\frac{x(x+2-x^2)}{2-x},\qquad z=-\frac{K(-1/2,x)}{40(1-x/2)^3}. \tag{5.27}
```

The larger-magnitude negative root is dS and the other is AdS; approximate $`(x,z)`$ pairs are $`(-1.2917914,0.2767403)`$ and $`(-0.02639041,-0.08562456)`$. These Q entries survive at the exceptional coupling in addition to GB-E.

<a id="55-exact-real-root-domains-and-completeness"></a>

## Exact real-root domains and completeness

The Q discriminant is

```math
\mathop{\mathrm{Disc}}\nolimits_xQ=1391569403904000000\,a^{31}(2a+1)^{15}\Delta(a), \tag{5.28}
```

```math
\Delta(a)=6306398208a^5-350467498082304a^4+550975823398912a^3-437993097561120a^2+173650160891775a+12082788284000. \tag{5.29}
```

It has exactly three real simple roots, denoted $`d_1<d_2<d_3`$:

```math
d_1\simeq-0.0598427152415775,\qquad d_2\simeq0.844285034416643,\qquad d_3\simeq55571.7498309625. \tag{5.30}
```

Exact rational isolating intervals and polynomial divisions are in the polynomial companion. The other two roots are nonreal. The leading Q coefficient is $`352a^6`$, $`Q(a,0)=-24a`$, and $`Q(a,-1/a)=-3(2a+1)^3/a^2`$. Thus on each open cell below, a real root cannot escape to infinity, cross the patch boundary, cross the solving denominator or become multiple. The count is therefore constant on that cell.

The exact Sturm sign variations at one rational point of each cell give all real counts. A variation counts a sign change after zero entries are removed; crossing a simple polynomial root reduces the variation by one, while crossings of internal remainder roots leave it unchanged because the adjacent remainders have opposite signs. Thus the difference of endpoint variations counts roots. The fully evaluated sequences are in the companion, not inferred from floating-point scans.

| Cell | Coupling domain | Rational sample | $`V(-\infty),V(0),V(+\infty)`$ | Q roots $`L<0`$ | Q roots $`L>0`$ | Total distinct branches, including S |
|---|---|---|---|---:|---:|---:|
| I1 | $`a<-1/2`$ | $`-2`$ | $`5,3,3`$ | 2 | 0 | 2 |
| I2 | $`-1/2<a<d_1`$ | $`-1/4`$ | $`6,4,2`$ | 2 | 2 | 6 |
| I3 | $`d_1<a<0`$ | $`-1/20`$ | $`7,5,1`$ | 2 | 4 | 8 |
| I4 | $`0<a<d_2`$ | $`1/2`$ | $`6,3,2`$ | 3 | 1 | 6 |
| I5 | $`d_2<a<d_3`$ | $`1`$ | $`5,4,3`$ | 1 | 1 | 4 |
| I6 | $`a>d_3`$ | $`60000`$ | $`6,3,2`$ | 3 | 1 | 6 |

The boundary counts, with each double or merged root counted once, are

| Coupling | Q negative / positive roots | Additional simple or exceptional entries | Total | Total if $`L>0`$ only |
|---|---:|---|---:|---:|
| $`a=-1/2`$ | $`2/0`$ | GB-E | 3 | 1 |
| $`a=d_1`$ | $`2/3`$ | Two positive S roots | 7 | 5 |
| $`a=0`$ | $`0/0`$ | Gauss–Bonnet on AdS₅ | 1 | 1 |
| $`a=d_2`$ | $`2/1`$ | One positive and one negative S root | 5 | 2 |
| $`a=d_3`$ | $`2/1`$ | One positive and one negative S root | 5 | 2 |

The positive-patch totals in open cells I1–I6 are respectively $`0,4,6,2,2,2`$. This separate count makes the effect of imposing $`L>0`$ explicit.

<a id="56-background-critical-loci-and-geometry-changes"></a>

## Background critical loci and geometry changes

For generic solutions the first two equations have nonzero elimination derivatives $`\partial_y e_N=-4r_0/x`$ and $`\partial_z e_L=20r_0`$. Along their solution, row elimination of the background Jacobian gives

```math
\det\frac{\partial(e_L,e_N,m)}{\partial(x,y,z)}=\frac{80r_0^2}{x}\frac{d}{dx}\left[-\frac{(ax^2+2x-2)Q}{1600r_0^6}\right]. \tag{5.31}
```

On Q this is $`-(ax^2+2x-2)Q_x/(20xr_0^4)`$. On S it is $`32(x-2)^3/x^2`$. Therefore all generic simple roots have rank three. At each $`d_i`$ there is exactly one real Q double root and rank two; the two nonzero elimination derivatives ensure that the rank cannot be lower. The subresultant calculation in the companion confirms one common Q/Q$`_x`$ root and no higher multiplicity at each real $`d_i`$.

The branch maps are explicit:

- At $`d_1`$, two positive Q roots are born as $`a`$ increases: I3 roots $`j=3,4`$ meet; the old I2 roots $`j=1,2,3,4`$ continue into I3 roots $`j=1,2,5,6`$.
- At $`d_2`$, two negative Q roots, I4 $`j=2,3`$, meet and disappear. I4 $`j=1,4`$ continue into I5 $`j=1,2`$.
- At $`d_3`$, two negative Q roots are born: I6 $`j=1,2`$ meet. I5 $`j=1,2`$ continue into I6 $`j=3,4`$.
- At $`a=-1/2`$, the two S roots and the two positive Q roots from I2 approach GB-E. To see the Q approach without using singular (5.25) at the endpoint, set $`a=-1/2+\epsilon^2`$ and $`x=2+c\epsilon`$. The first nonzero Q coefficient is $`(587c^6-2760c^4+5184c^2-1536)\epsilon^6/16`$. Its two real roots are $`c\simeq\pm0.6000167707`$, and substitution in (5.17),(5.19) gives $`y\to-6,z\to-2`$. The S roots have $`x=2\pm\sqrt8\epsilon+O(\epsilon^2)`$ and the same endpoint. The Q negative roots continue smoothly across this coupling.

The exceptional point has Jacobian rank zero but remains isolated by (5.15). GB-U has rank two and a genuine modulus. These are background facts only: no kinetic rank or massless-mode statement follows.

The exact sign rule on Q is $`\mathop{\mathrm{sgn}}\nolimits k=-\mathop{\mathrm{sgn}}\nolimits[K(a,x)(1+ax)]`$. Its finite flat points are determined by

```math
B(a):=100352a^3+4800a^2-13035a-128=0,\qquad x=-\frac{11941888a^2+671552a-1590045}{40548},\qquad y=-\frac{x(x+2+2ax^2)}{2(1+ax)},\quad z=0. \tag{5.32}
```

These equations follow by eliminating $`x`$ between $`Q=0`$ and $`K=0`$: $`\mathop{\mathrm{Res}}\nolimits_x(Q,-K)=3276800000000a^{19}(2a+1)^9B(a)`$, and the final linear remainder reduces to the displayed $`x`$ formula modulo $`B`$. The excluded prefactors $`a=0,-1/2`$ were already solved and produce no additional flat gauged vacuum.

| Flat coupling | $`x=L`$ approximately | $`y=N/g`$ approximately | Root entry | Geometry as $`a`$ increases |
|---|---:|---:|---|---|
| $`b_1=-0.380443587489315`$ | $`2.88783042947`$ | $`-21.3336498569`$ | I2 $`j=4`$ | AdS to dS |
| $`b_2=-0.00979163814985713`$ | $`39.3478260730`$ | $`-352.947060773`$ | I3 $`j=4`$ | AdS to dS |
| $`b_3=0.342403592986111`$ | $`-0.985656502454`$ | $`1.24946063015`$ | I4 $`j=3`$ | dS to AdS |

The ordering is $`-1/2<b_1<d_1<b_2<0<b_3<d_2<d_3`$. No simple S root is flat for $`g\ne0`$. The Q flat crossings are simple roots, so they change geometry without changing the number of backgrounds. Together with (5.28), the leading coefficient, patch and denominator tests exhaust finite background critical candidates.

<a id="57-limits-of-every-family"></a>

## Limits of every family

### Two-derivative limit: $`\lambda\to0`$ at fixed nonzero $`g`$

Here $`a\to0`$. On S$`_+`$, expand $`\sqrt{1+2a}=1+a-a^2/2+a^3/2+O(a^4)`$ in its rationalized expression:

```math
x_+=1-\frac a2+\frac{a^2}{2}+O(a^3),\qquad y_+=-\frac32+\frac32a-\frac{15}{8}a^2+O(a^3),\qquad z_+=-\frac12+\frac12a-\frac58a^2+O(a^3). \tag{5.33}
```

S$`_-`$ instead has $`x_-=-2/a-1+O(a)`$ and $`y_-=-3x_-^2/2,z_-=-x_-^2/2`$; it diverges and has no regular two-derivative limit.

Every real Q root is covered by the following small-$`a`$ balances. The polynomial companion displays the substitutions in (5.22).

| Q root type | Dominant balance and result | $`y,z`$ behavior | Endpoint |
|---|---|---|---|
| Small $`L`$ | $`x=ca`$: $`Q=a(320c-24)+O(a^2)`$, so $`x=3a/40+O(a^2)`$ | $`y=-x+O(a^2)`$, $`z=-1/10+O(a)`$ | $`L=0`$ excluded; finite curvature does not regularize the source action |
| Two square-root roots, only $`a<0`$ | $`a=-\epsilon^2`$, $`x=c/\epsilon`$: $`Q=\epsilon^{-1}(320c-280c^3)+O(1)`$, so $`c=\pm\sqrt{8/7}`$ | $`y\sim-x^2/2`$, $`z\sim-2x/7`$ | Divergent $`L,N,k`$ at fixed $`g`$ |
| Three inverse-$`a`$ roots | $`x=u/a`$: $`a^2Q\to u^3P_5(u)`$, where $`P_5=352u^5+1880u^4+3859u^3+3754u^2+1700u+280`$ | $`y\sim-\frac{u^2(2u+1)}{2(u+1)a^2}`$, $`z\sim-\frac{u^3(8u^2+13u+4)}{40(u+1)^3a^2}`$ | Divergent $`L,N,k`$ |

The three real $`P_5`$ roots are approximately $`-1.19313342500039,-0.752270721217875,-0.385325949381662`$; none is zero or $`-1`$, so all displayed denominators are nonzero. The other two roots are nonreal. For $`a<0`$ the count is $`1+2+3=6`$ real Q roots; for $`a>0`$ it is $`1+3=4`$, matching the exact cell counts. No additional finite nonzero-$`L`$ Q endpoint can exist because $`Q(0,x)=320x`$.

Thus only S$`_+`$ has a controlled small-$`|a|`$ background expansion with finite nonzero $`L`$. The exact catalogue still retains every other branch. In an EFT interpretation, divergent branches or branches approaching the singular compensator patch are not controlled continuations of the two-derivative vacuum.

### Ungauged limit: $`g\to0`$ at fixed finite $`\lambda`$

S$`_+`$ has $`L\to1,N\to0,k\to0`$, landing on the $`L=1`$ point of GB-U. S$`_-`$ and the three inverse-$`a`$ Q roots have $`L=O(g^{-2})`$, $`N=O(g^{-3})`$, $`k=O(g^{-2})`$ and are singular. The two square-root Q roots, possible only for $`\lambda<0`$, have $`L=O(|g|^{-1})`$, $`N=O(g^{-1})`$, $`k=O(|g|)`$: their curvature tends to zero but the fields diverge. The small-$`L`$ Q root has $`L=O(g^2)`$, $`N=O(g^3)`$, $`k\sim-g^2/10`$, approaching the excluded $`L=0`$ boundary. These cases exhaust all roots near $`a=0`$. GB-E requires $`\lambda=-1/(2g^2)`$, so it has no fixed-finite-$`\lambda`$ ungauged path.

A different double scaling can hold $`a`$ fixed while $`g\to0`$ and $`\lambda=a/g^2`$ diverges. Every fixed finite catalogue $`(x,y,z)`$ then has $`L=x,N=gy\to0,k=g^2z\to0`$. This is a shared geometric flat limit, not the same fixed theory limit as above. In particular GB-E reaches $`L=2`$ along such a path.

### Flat and zero-flux limits

Within the selected symmetry class fluxes vanish identically by (2.1), so the zero-flux limit is already included for every entry. Finite-coupling gauged flat limits are exactly the three Q crossings (5.32). Every ungauged entry is already flat. Vanishing curvature with divergent fields in the previous paragraph is a singular limit, not an additional regular flat branch.

### Large $`|a|`$ boundaries

For completeness, roots that move to the edge of the compensator patch at large coupling can be tracked by dominant balance. For $`a\to+\infty`$, S$`_\pm`$ have $`x\sim\pm\sqrt{2/a}`$, $`y\sim-3/a`$, $`z\sim-1/a`$. Q has two roots $`x\sim\pm\sqrt{2/(11a)}`$, $`y\sim-13/(11a)`$, $`z\sim-7/(11a)`$, from $`352a^6x^8-64a^5x^6=0`$ after excluding the smaller-root scaling. The other two Q roots have $`x\sim c a^{-2/3}`$ where $`c^3=(-9\pm5\sqrt3)/4`$, $`y\sim-1/a`$, $`z\sim-(6+c^{-3})/(10a)`$; the balance is $`8c^6+36c^3+3=0`$.

For $`a=-A\to-\infty`$, there are only the latter two real Q roots, with $`x\sim c A^{-2/3}`$, $`y\sim1/A`$, $`z\sim(6+c^{-3})/(10A)`$. The square-root balance would require $`x^2=-2/(11A)`$ and is nonreal. All these large-coupling limits approach $`L=0`$; no endpoint at finite allowed $`L`$ is omitted.

<a id="58-residual-catalogue-and-completion-statement"></a>

## Residual catalogue and completion statement

| Branch ID | Domain and geometry | Free data | $`(E_L,E_N,M)`$ after substitution | Other independent tadpoles |
|---|---|---|---|---|
| GB-U | $`g=0`$, all real finite $`\lambda`$, Minkowski | $`L\ne0`$ | $`(0,0,0)`$ by (5.10) | All zero by §5.2 |
| Gauss–Bonnet on AdS₅ | $`g\ne0`$, $`a\ge-1/2`$; AdS; rationalized root in (5.24) | Couplings only | $`(0,0,0)`$ by the three displayed factors (5.23) | All zero |
| GB-S$`_-`$ | $`g\ne0`$, $`a\ge-1/2`$, $`a\ne0`$; AdS | Couplings only | $`(0,0,0)`$ by (5.23) | All zero |
| GB-E | $`g\ne0`$, $`a=-1/2`$; AdS | Couplings on this locus | $`(0,0,0)`$ by (5.15); counts once for both S roots and positive Q endpoints | All zero |
| GB-Q:cell:$`j`$ | All real allowed roots in (5.25), with counts in §5.5; geometry by §5.6 | Couplings and discrete real-root choice | $`e_N=0`$, $`e_L=0`$, $`m=-(ax^2+2x-2)Q/(1600r_0^6)=0`$ | All zero |

The two generic negative Q roots at $`a=-1/2`$ are included via (5.27). At the three $`d_i`$, each merged root is one entry. No branch has been removed because it lacks a two-derivative limit or because its eventual kinetic sign is unknown.

**Case completeness:** $`g=0`$ is solved directly. For $`g\ne0`$, the disjoint cases $`r_0=0`$ and $`r_0\ne0`$ are exhausted. In the latter, elimination is reversible and the two polynomial factors include every real solution. Their leading coefficients, common roots, discriminants, zero-patch roots and forbidden-denominator roots have all been treated. The exact root counts and residual substitutions are reproducibly checked. The local maximally symmetric branch catalogue is complete on the declared signed $`L\ne0`$ domain; the positive-patch subcatalogue is also explicit.

The catalogue solves the accepted action’s background equations in the local maximally symmetric class with $`L\ne0`$. Global topology sectors, less symmetric flux backgrounds and the singular $`L=0`$ coordinate boundary lie outside that domain. The [selected AdS₅ analysis](../README.md) gives the Killing-spinor conditions and fluctuation spectrum on the chosen branch.
