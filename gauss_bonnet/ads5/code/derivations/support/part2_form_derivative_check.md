# Independent check of the quadratic form derivatives for Gauss–Bonnet on AdS₅

The bosonic form block below includes the conformal-Hessian sign correction. Sections 1–7 establish a derivative subtotal; Sections 8–12 extend the calculation to the remaining form currents, compensator connections, raw form equations and local physical vectors. The check concerns these quadratic form terms. Fermions and the graviton/scalar blocks are outside this report.

The sole action input is [the full fermionic GB action](../../../../action/gb_splus_action.md), `GB-FINAL-DENSITY`. Term identifiers below refer to its [coefficient ledger](../../outputs/action_coefficients.json). The derivative definitions are the accepted [component conventions](../../references/COMPONENT_CONVENTIONS.md), G01, G02, W01, R04a, X09 and SC7-01–SC7-10. No other action or spectrum is used.

## 1. Background and quantities being checked

The calculation is quadratic in bosonic form fluctuations, on the already selected background

```math
L=x,\qquad N=-\frac32gx^2,\qquad k=-\frac12g^2x^2,\qquad f_{ab}=-\frac{k}{4}\eta_{ab},\qquad \overline D=\overline T=\overline C_{abcd}=0.
```

The metric signature is $`(-,+,+,+,+)`$, the curvature is $`R_{abcd}=k(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc})`$, and $`\epsilon^{01234}=1`$. The two-form $`H_{ab}`$ means the accepted dual $`H^{ab}=-\epsilon^{abcde}H_{cde}/12`$; it does not mean a closed two-form. At this order,

```math
G=dC,\qquad H_3=dB+\frac g2E_3,\qquad T_{ab}=\frac18(G_{ab}-2H_{ab}),\qquad j_{Xb}:=\nabla^aX_{ab},\qquad j_{Hb}=-\frac g2P_b.
```

Indeed, the $`E_3`$ contribution to $`H^{ab}`$ is $`gE^{ab}/2`$. Hence $`\nabla_bH^{ba}=(g/2)\nabla_bE^{ba}=-(g/2)P^a`$, using `GB14`. Define the contracted quantities

```math
A_{XY}:=(\nabla_aX_{bc})(\nabla^aY^{bc}),\qquad J_{XY}:=j_X\!\cdot j_Y,\qquad XY:=X_{ab}Y^{ab}.
```

An equality denoted $`\doteq`$ is an equality of integrated bulk quadratic densities up to an explicitly used integration by parts. Compactly supported variations suffice; no AdS boundary condition has been selected. The engineering dimensions are $`[G]=[H]=1`$, $`[\nabla]=1`$ and $`[k]=2`$, so every $`A`$, $`J`$ and $`kXY`$ below has dimension four before multiplication by $`\lambda_{\rm GB}`$.

## 2. The Lorentz contribution to the conformal Hessian has a minus sign

Let $`X_{cd}`$ be a K-primary antisymmetric tensor of Weyl weight $`w`$. Accepted G01/X09 give the bosonic first derivative, and W01/R04a give the relevant K variations:

```math
\mathcal D_bX_{cd}=\partial_bX_{cd}+\omega_{bc}{}^eX_{ed}+\omega_{bd}{}^eX_{ce}-wb_bX_{cd},\qquad \delta_Kb_b=2\Lambda_b,\qquad \delta_K\omega_b{}^{cd}=-2(\Lambda^c\delta_b^d-\Lambda^d\delta_b^c).
```

Lower the first Lorentz index of the connection before inserting its variation:

```math
\delta_K\omega_{bc}{}^e=2\eta_{bc}\Lambda^e-2\Lambda_c\delta_b^e.
```

Therefore, with the same generator convention as the tentative calculation,

```math
(M_{be}X)_{cd}:=\eta_{bc}X_{ed}-\eta_{ec}X_{bd}+\eta_{bd}X_{ce}-\eta_{ed}X_{cb},\qquad \delta_K(\mathcal D_bX_{cd})=-2w\Lambda_bX_{cd}+2\Lambda^e(M_{be}X)_{cd}.
```

The outer derivative subtracts this K variation, as required by G01. Consequently,

```math
\boxed{\mathcal D_a\mathcal D_bX_{cd}=\nabla_a\nabla_bX_{cd}+2wf_{ab}X_{cd}-2f_a{}^e(M_{be}X)_{cd}=\nabla_a\nabla_bX_{cd}-\frac{wk}{2}\eta_{ab}X_{cd}+\frac{k}{2}(M_{ba}X)_{cd}.}
\tag{FD1}
```

The tentative expression had $`+2f_a{}^eM_{be}`$ instead of $`-2f_a{}^eM_{be}`$. The scalar Hessian does not detect this error because a scalar has no Lorentz-generator term.

There is an independent curvature check. G02 implies $`[\nabla_a,\nabla_b]X_{cd}=k(M_{ab}X)_{cd}`$. Antisymmetrizing the last two terms of (FD1) gives $`-k(M_{ab}X)_{cd}`$. Thus $`[\mathcal D_a,\mathcal D_b]X_{cd}=0`$ on this conformally flat bosonic background. The tentative sign instead adds the two curvature contributions.

## 3. Ordered contractions and integrations by parts

Contract (FD1), retaining the order of its derivatives. The elementary contractions are $`\eta^{ce}(M_{ea}X)_{bc}=-3X_{ab}`$ and $`\eta^{ce}(M_{ae}X)_{bc}=3X_{ab}`$ in five dimensions. This gives

```math
\Box^cX_{ab}=\nabla^2X_{ab}-\frac{5wk}{2}X_{ab},\qquad \mathcal D_a\mathcal D^cX_{bc}=-\nabla_a j_{Xb}+\frac{w-3}{2}kX_{ab},\qquad \mathcal D^c\mathcal D_aX_{bc}=\nabla^c\nabla_aX_{bc}+\frac{w+3}{2}kX_{ab}.
\tag{FD2}
```

For the reversed contraction, the curvature commutator is

```math
[\nabla^c,\nabla_a]X_{bc}=-3kX_{ab},\qquad \nabla^c\nabla_aX_{bc}=-\nabla_a j_{Xb}-3kX_{ab}.
```

It follows that the two ordered contractions in (FD2) agree after their curvature terms are combined. Their common integrated contraction with a second two-form is

```math
Y^{ab}\mathcal D_a\mathcal D^cX_{bc}\doteq J_{XY}+\frac{w-3}{2}kXY,\qquad Y^{ab}\mathcal D^c\mathcal D_aX_{bc}\doteq J_{XY}+\frac{w-3}{2}kXY.
\tag{FD3}
```

In particular, $`w(G)=2`$ supplies $`-kYG/2`$; $`w(H)=3`$ supplies zero. A contraction with the inner indices of $`H`$ in the opposite order has the opposite sign: $`G_{ac}\mathcal D^a\mathcal D^bH_b{}^c\doteq-J_{GH}`$ and $`G_{bc}\mathcal D^a\mathcal D^bH_a{}^c\doteq-J_{GH}`$.

The first-derivative crossed contraction has its own, unchanged curvature identity:

```math
(\nabla^aX^{bc})(\nabla_bY_{ac})\doteq-X^{bc}\nabla^a\nabla_bY_{ac}=-X^{bc}\nabla_bj_{Yc}-3kXY\doteq J_{XY}-3kXY.
\tag{FD4}
```

The Bianchi identity for $`G`$ is $`\nabla_aG_{bc}+\nabla_bG_{ca}+\nabla_cG_{ab}=0`$. Contracting it with $`\nabla^aY^{bc}`$ and using (FD4) gives

```math
A_{GY}=2(\nabla^aY^{bc})(\nabla_bG_{ac})\doteq2J_{GY}-6kGY.
\tag{FD5}
```

Only the $`G`$ factor needs to be closed in (FD5); the substitution is valid for $`Y=H`$ without imposing $`dH=0`$.

## 4. Weyl and LOG derivative sums

The three Weyl derivative terms are `Weyl_sigma_N` 6–8. Apply (FD3) with $`w(T)=1`$ and (FD4):

```math
\frac{128}{3}(\nabla T)^2-\frac{128}{3}(\nabla_bT_{ac})(\nabla^aT^{bc})+\frac{256}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\doteq\frac{128}{3}A_{TT}-128J_{TT}+\frac{640}{3}kT^2.
```

Substitute $`T=(G-2H)/8`$ only after evaluating its weight-one second derivative:

```math
\ell^{(2)}_{\mathrm{W,der}}\doteq\frac23A_{GG}-\frac83A_{GH}+\frac83A_{HH}-2J_{GG}+8J_{GH}-8J_{HH}+\frac{10}{3}kG^2-\frac{40}{3}kGH+\frac{40}{3}kH^2.
\tag{FD6}
```

For clarity, the coefficient-free reductions of the LOG derivative monomials are listed before multiplying by their source coefficients.

| `LOG_seed` | Source coefficient | Monomial reduced under the integral |
|---|---:|---|
| 33 | $`-8/9`$ | $`J_{GG}-kG^2/2`$ |
| 35 | $`-112/9`$ | $`-J_{GH}`$ |
| 37 | $`-32/9`$ | $`J_{GH}-kGH/2`$ |
| 39 | $`-128/9`$ | $`J_{HH}`$ |
| 40 | $`-4/3`$ | $`-A_{GG}-5kG^2`$ |
| 41 | $`-16/3`$ | $`-A_{GH}-5kGH`$ |
| 42 | $`-4/9`$ | $`J_{GG}-kG^2/2`$ |
| 43 | $`-8/9`$ | $`-J_{GH}`$ |
| 44 | $`-16/9`$ | $`J_{GH}-kGH/2`$ |
| 45 | $`32/9`$ | $`J_{HH}`$ |
| 52 | $`-10/3`$ | $`J_{GG}-3kG^2`$ |
| 53 | $`28/3`$ | $`J_{GH}-3kGH`$ |
| 54 | $`-16/3`$ | $`J_{HH}-3kH^2`$ |
| 55 | $`4/3`$ | $`A_{GG}`$ |
| 56 | $`-22/3`$ | $`A_{GH}`$ |
| 57 | $`-8/3`$ | $`A_{HH}`$ |
| 58 | $`8`$ | $`-J_{GH}`$ |
| 59 | $`-16`$ | $`-J_{HH}`$ |

Adding these rows to (FD6) gives

```math
\ell^{(2)}_{\mathrm{der}}\doteq\frac{10}{3}A_{GG}-\frac{14}{3}A_{GH}-\frac{20}{3}J_{GG}+\frac{52}{3}J_{GH}-8J_{HH}+\frac{62}{3}kG^2-12kGH+\frac{88}{3}kH^2.
```

Now use (FD5). The $`J_{GG}`$ coefficient is $`-20/3+2(10/3)=0`$, and the $`J_{GH}`$ coefficient is $`52/3+2(-14/3)=8`$. The curvature coefficients become $`62/3-6(10/3)=2/3`$ and $`-12-6(-14/3)=16`$. Therefore

```math
\ell^{(2)}_{\mathrm{der}}\doteq8J_{GH}-8J_{HH}+\frac23kG^2+16kGH+\frac{88}{3}kH^2.
\tag{FD7}
```

The algebraic form contributions from `LOG_seed` 19–25, 32, 34, 36 and 38 use $`g^2x^2=-2k`$, $`gN=3k`$, $`\Box^c\sigma=-5k/2`$ and $`\mathcal D_a\mathcal D_b\sigma=-k\eta_{ab}/2`$. Their coefficients are

```math
kG^2:\quad 3-6-\frac83=-\frac{17}{3},\qquad kGH:\quad-\frac{40}{3}-\frac83+16-\frac{56}{9}+\frac{56}{9}=0,\qquad kH^2:\quad-8-24-\frac{16}{3}=-\frac{112}{3}.
```

Thus the checked derivative-plus-algebraic subtotal is

```math
\ell^{(2)}_{\mathrm{subtotal}}\doteq8J_{GH}-8J_{HH}-5kG^2+16kGH-8kH^2.
\tag{FD8}
```

## 5. The ordered current in LOG term 287

The K transformation of the divergence follows directly by contracting the first-descendant variation in Section 2:

```math
\delta_Kj_{Xa}=2(3-w)\Lambda^bX_{ba}.
```

Consequently $`j_H`$ is K-primary because $`w(H)=3`$. Its weight is four. The bosonic conformal box acting on this vector has a vanishing Lorentz trace and a nonzero weight term:

```math
\Box^c j_{Ha}=\nabla^2j_{Ha}+8f_b{}^b j_{Ha}=(\nabla^2-10k)j_{Ha}.
```

Since $`\mathcal D^cH_{ac}=-j_{Ha}`$, term 287 becomes $`-8C^a(\nabla^2-10k)j_{Ha}`$. To integrate it by parts, use

```math
j_{Ga}=\nabla^b(\nabla_bC_a-\nabla_aC_b)=\nabla^2C_a-\nabla_a\nabla\!\cdot C-4kC_a,\qquad \nabla\!\cdot j_H=0.
```

The gradient of $`\nabla\!\cdot C`$ therefore drops from the integrated contraction. The result is

```math
8C^a\Box^c\mathcal D^cH_{ac}\doteq-8j_G\!\cdot j_H+48kC\!\cdot j_H.
\tag{FD9}
```

The remaining Hessian currents have the following coefficients of $`kC\cdot j_X`$ after inserting $`\mathcal D_a\mathcal D_b\sigma=-k\eta_{ab}/2`$:

```math
X=G:\quad(284,288,290,292)\longmapsto\left(-1,-1,-\frac52,+\frac12\right),\qquad X=H:\quad(286,289,291,293)\longmapsto(-10,+2,+5,-1).
```

Both sums equal $`-4`$. Terms 294–295 contract an antisymmetric form with the symmetric background Hessian and vanish. The background $`\Box^c\mathcal D_a\sigma`$ vanishes, so terms 283 and 285 have no quadratic form contribution. Hence the checked current sum is

```math
\ell^{(2)}_{\mathrm{current}}\doteq-8J_{GH}-4kC\!\cdot j_G+44kC\!\cdot j_H\doteq-8J_{GH}+2kG^2-22kGH,
```

where $`C\cdot j_X\doteq-GX/2`$. Combining with (FD8) gives the scoped result

```math
\boxed{\ell^{(2)}_{\mathrm{checked\ form\ terms}}\doteq-8j_H^2-3kG^2-6kGH-8kH^2=-2g^2P^2-3kG^2-6kGH-8kH^2.}
\tag{FD10}
```

This is a subtotal of the higher-derivative density. The two-derivative density, the $`R(V)`$ terms and compensator connection terms still have to be added to form the complete vector/form Hessian. Equation (FD10) is not by itself a spectrum or a statement about the total rank of that Hessian.

## 6. Reproducible algebra checks

The following exact SymPy calculation checks the Lorentz contractions in the Lorentzian metric, the conformal-commutator cancellation, all numerical sums in (FD7)–(FD10), and the flat-curvature limit. Run it with the project Python having SymPy installed. It writes no files.

```python
import itertools
import sympy as s

q = s.Rational
eta = [-1, 1, 1, 1, 1]
w = s.symbols('w')
X = s.zeros(5)
for a in range(5):
    for b in range(a + 1, 5):
        X[a, b], X[b, a] = 7*a + 3*b + 1, -(7*a + 3*b + 1)
def metric(a, b):
    return eta[a] if a == b else 0
def M(a, b, c, d):
    return (metric(a,c)*X[b,d] - metric(b,c)*X[a,d]
            + metric(a,d)*X[c,b] - metric(b,d)*X[c,a])
def K(a, b, c, d):
    return -w*q(1,2)*metric(a,b)*X[c,d] + q(1,2)*M(b,a,c,d)
for a, b in itertools.product(range(5), repeat=2):
    assert s.expand(sum(eta[c]*K(a,c,b,c) for c in range(5))
                    - (w-3)*X[a,b]/2) == 0
    assert s.expand(sum(eta[c]*K(c,a,b,c) for c in range(5))
                    - (w+3)*X[a,b]/2) == 0
    assert s.expand(sum(eta[c]*K(c,c,a,b) for c in range(5))
                    + 5*w*X[a,b]/2) == 0
for a,b,c,d in itertools.product(range(5), repeat=4):
    assert s.expand(M(a,b,c,d)+K(a,b,c,d)-K(b,a,c,d)) == 0

AG, AM, AH, JG, JM, JH, KG, KM, KH = s.symbols('AG AM AH JG JM JH KG KM KH')
weyl = (q(2,3)*AG-q(8,3)*AM+q(8,3)*AH-2*JG+8*JM-8*JH
        +q(10,3)*KG-q(40,3)*KM+q(40,3)*KH)
rows = [(q(-8,9),JG-KG/2), (q(-112,9),-JM),
        (q(-32,9),JM-KM/2), (q(-128,9),JH),
        (q(-4,3),-AG-5*KG), (q(-16,3),-AM-5*KM),
        (q(-4,9),JG-KG/2), (q(-8,9),-JM),
        (q(-16,9),JM-KM/2), (q(32,9),JH),
        (q(-10,3),JG-3*KG), (q(28,3),JM-3*KM),
        (q(-16,3),JH-3*KH), (q(4,3),AG),
        (q(-22,3),AM), (q(-8,3),AH), (8,-JM), (-16,-JH)]
derivatives = s.expand(weyl + sum(c*t for c,t in rows))
closed = s.expand(derivatives.subs({AG:2*JG-6*KG, AM:2*JM-6*KM}))
assert s.expand(closed - (8*JM-8*JH+q(2,3)*KG+16*KM+q(88,3)*KH)) == 0
algebraic = (3-6-q(8,3))*KG + (-q(40,3)-q(8,3)+16-q(56,9)+q(56,9))*KM + (-8-24-q(16,3))*KH
subtotal = s.expand(closed + algebraic)
assert subtotal == 8*JM-8*JH-5*KG+16*KM-8*KH
current = -8*JM+2*KG-22*KM
answer = s.expand(subtotal + current)
assert answer == -8*JH-3*KG-6*KM-8*KH
assert answer.subs({KG:0, KM:0, KH:0}) == -8*JH
print('PASS: checked Lorentz contractions, ordered derivatives and scoped coefficient sums')
```

The explicit result of running this code is the printed PASS line. It is a PASS only for the checks named in that line. It establishes neither global AdS boundary norms nor completion of the full Gauss–Bonnet on AdS₅ spectrum.

## 7. Findings and remaining scope

- **Corrected, central sign error:** the K-connection Lorentz term in the second derivative was reversed. Sections 2–3 derive its sign from the accepted component variations and check it by the vanishing conformal curvature.
- **Checked:** the Levi–Civita commutator and the closed-$`G`$ integration-by-parts identity used in the tentative script had the correct signs.
- **Checked:** the divergence of the weight-three dual form is K-primary and has weight four; term 287 contains the shift $`\nabla^2-10k`$.
- **Checked:** the displayed source-term subset sums to (FD10). In the limit $`k\to0`$ its surviving derivative term is $`-8j_H^2`$; on the ungauged fluxless limit $`g\to0`$, the identity $`j_H=-gP/2`$ makes that term vanish as well.
- **Scope of Sections 1–7:** the subtotal alone does not establish the complete form block. The specified extension below supplies its remaining currents, $`R(V)`$ and compensator terms and its local constrained spectrum. Fermions and the graviton/scalar block remain outside this report.

## 8. Remaining currents and the trace SU(2) connection

The six additional currents `LOG_seed` 246–251 have a nonzero background scalar coefficient. Their coefficients, with the derivative still written as $`C^a\nabla^bX_{ab}`$, sum to

```math
X=G:\quad \frac83\left(-\frac52k\right)+\frac83(-2k)+\frac{20}{3}(3k)=8k,\qquad X=H:\quad-\frac{40}{3}\left(-\frac52k\right)-\frac43(-2k)-\frac{16}{3}(3k)=20k.
```

Since $`\nabla^bX_{ab}=-j_{Xa}`$ and $`C\cdot j_X\doteq-GX/2`$, these contribute $`4kG^2+10kGH`$. Adding them to (FD10) gives

```math
\ell^{(2)}_{\mathrm{HD,forms\ before}\ V}\doteq-8j_H^2+kG^2+4kGH-8kH^2.
\tag{FD11}
```

Write $`V_a^{ij}=V_a'{}^{ij}+\delta^{ij}v_a/2`$, with $`\delta_{ij}V'{}^{ij}=0`$, and $`F(v)_{ab}=2\nabla_{[a}v_{b]}`$. The terms `Weyl_Y` 6 and `LOG_seed` 60, 81 reduce to

```math
\frac{16}{3}gL^{ij}R(V)_{abij}T^{ab}+\frac43gL^{ij}R(V)_{abij}G^{ab}-\frac83gL^{ij}R(V)_{abij}H^{ab}=2gL^{ij}R(V)_{abij}G^{ab}-4gL^{ij}R(V)_{abij}H^{ab}.
```

The other relevant term is `LOG_seed` 274. Its integration by parts fixes its relative sign:

```math
-4gC^aL^{ij}\nabla^bR(V)_{abij}\doteq4gL^{ij}(\nabla^bC^a)R(V)_{abij}=-2gL^{ij}G^{ab}R(V)_{abij}.
```

The $`GR(V)`$ terms cancel. At the background $`L^{ij}=x\delta^{ij}/\sqrt2`$, $`L^{ij}R(V)_{abij}=xF(v)_{ab}/\sqrt2`$ to first order. Thus the surviving term is

```math
-2\sqrt2gxH^{ab}F(v)_{ab}\doteq4\sqrt2gxv^aj_{Ha}=-2\sqrt2g^2xP\!\cdot v.
\tag{FD12}
```

The curvature-square terms themselves cancel between `Weyl_sigma_N` 5 and `LOG_seed` 1: $`(2/3-2/3)R(V)^2=0`$. There is consequently no independent $`F(v)^2`$ or $`F(V')^2`$ term in this bosonic Hessian.

## 9. Compensator connection terms and the complete raw form density

The connection contribution from the constant compensator cannot be set to zero. Its coefficient can be checked without a convention guess by a two-by-two matrix calculation. Let $`\varepsilon=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$, $`\mathsf V=\left(\begin{smallmatrix}p&q\\q&-p\end{smallmatrix}\right)`$ and $`\mathsf L=x\mathbf1/\sqrt2`$ for one world component. Right lowering of both indices is $`\mathsf X_{\rm lower}=\varepsilon^T\mathsf X\varepsilon`$. The full triplet derivative L02 gives

```math
\mathcal D\mathsf L=\mathsf V\varepsilon\mathsf L+\mathsf L(\mathsf V\varepsilon)^T=\sqrt2x\mathsf V\varepsilon,\qquad V'{}^{ij}V'_{ij}=-2(p^2+q^2),\qquad (\mathcal DL)^{ij}(\mathcal DL)_{ij}=2x^2V'{}^{ij}V'_{ij}.
```

Applying the connection once more and projecting onto the background direction gives

```math
\frac{\delta^{ij}}{\sqrt2}(\Box^cL_{ij})\big|_{V'^2}=-2xV'{}^{ij}V'_{ij}.
```

In the two-derivative part of `GB-FINAL-DENSITY`, the first box term therefore contributes $`+4xV'^2`$. The explicitly written derivative-product term contributes $`-2xV'^2`$; together they give $`+2xV'^2`$. The potentially linear $`E\cdot\mathcal DL`$ term vanishes under its trace because a symmetric triplet contracted with $`\varepsilon`$ has zero trace. The $`E^{ab}(\mathcal DL)(\mathcal DL)`$ term is cubic in fluctuations.

For `LOG_seed` 71 and 75, ordinary integration by parts of the triplet connection part gives

```math
2g^2L^{ij}\Box^cL_{ij}+3g^2(\mathcal DL)^{ij}(\mathcal DL)_{ij}\Big|_{V'^2}=(-2+3)g^2(\mathcal DL)^{ij}(\mathcal DL)_{ij}=2g^2x^2V'^2.
```

The conformal-curvature part of the box belongs to the scalar/graviton block and does not alter this connection coefficient. The two-derivative form coefficients are equally direct. The explicit flux square and the flux terms of $`D`$ give

```math
-\frac{x}{12}(G-2H)^2-8x\left(\frac5{96}G^2+\frac1{24}GH-\frac{13}{24}H^2\right)=-\frac x2G^2+4xH^2.
```

At quadratic bosonic order the independent linear-multiplet vector equals $`P`$. Its explicit algebraic term is $`+2P^2/x`$. The current-derivative term is $`-4E^{ab}\nabla_aP_b/x\doteq-4P^2/x`$, because $`\nabla_aE^{ab}=-P^b`$. Similarly,

```math
-\sqrt2E^{ab}F(v)_{ab}\doteq-2\sqrt2P\!\cdot v,\qquad -2gE^{ab}G_{ab}\doteq-4gP\!\cdot C.
```

Thus the two-derivative result and the higher-derivative result are

```math
\ell^{(2)}_{2\partial,\mathrm{forms}}\doteq-\frac x2G^2+4xH^2-\frac2xP^2-2\sqrt2P\!\cdot v-4gP\!\cdot C+2xV'^2,
```

```math
\ell^{(2)}_{\mathrm{HD,forms}}\doteq kG^2+4kGH-8kH^2-2g^2P^2-2\sqrt2g^2xP\!\cdot v+2g^2x^2V'^2.
\tag{FD13}
```

For the mixed term, $`GH\doteq-2C\cdot j_H=gC\cdot P`$. Define $`a=\lambda_{\rm GB}g^2`$ and $`c=2-x`$. The branch relation $`ax^2+2x-2=0`$ implies

```math
\lambda_{\rm GB}k=x-1,\qquad 1+ax=\frac cx,\qquad 1-\lambda_{\rm GB}k=c.
```

For example, the coefficients of $`G^2`$, $`H^2`$ and $`P^2`$ become $`-x/2+(x-1)=-c/2`$, $`4x-8(x-1)=4c`$ and $`-2/x-2a=-2c/x^2`$. The other three coefficients become $`-2\sqrt2(1+ax)=-2\sqrt2c/x`$, $`-4g+4\lambda_{\rm GB}kg=-4gc`$ and $`2x+2ax^2=2c`$. Hence the complete raw form/connection block is

```math
\boxed{\ell^{(2)}_{\mathrm{forms}}\doteq c\left[-\frac12G^2+4H^2-\frac2{x^2}P^2-\frac{2\sqrt2}{x}P\!\cdot v-4gP\!\cdot C+2V'{}^{ij}_aV'^a{}_{ij}\right].}
\tag{FD14}
```

This reduction uses neither a field equation nor a gauge condition on the fluctuations.

The possible curvature–form bilinears `LOG_seed` 26–31 vanish by the **bosonic algebraic** Weyl identity $`C_{a[bcd]}=0`$: each epsilon contracts either the last three indices of the Weyl tensor or all four. Its differentiated version vanishes too. Terms 72–73 vanish because their epsilon contracts the symmetric bosonic Hessian of $`\sigma`$. These statements do not symmetrize a fermionic $`f_{ab}`$. The remaining bosonic Weyl currents contain at least three fluctuations because $`\overline C_{abcd}=\overline T=\overline D=0`$. The unused LOG current terms contain either at least three fluctuations or a vanishing background first/third derivative of a scalar. Pure scalar/curvature terms have no form variation. Together with the explicit $`R(V)^2`$ cancellation, these exclusions close the bosonic form-block ledger for this check.

## 10. Vary the raw block before solving its constraints

Assume $`0<x<2`$, so $`c>0`$ and dividing by its common factor is allowed. Write $`\mathcal E^{ab}=E^{ab}`$ for the independent dual of $`E_3`$, so that $`P^a=\nabla_b\mathcal E^{ab}`$ and $`H=H_B+g\mathcal E/2`$, with $`H_B=-*dB/2`$. For variations of $`\mathcal E`$ at fixed metric,

```math
\delta P^a=\nabla_b\delta\mathcal E^{ab},\qquad \delta H_{ab}=\frac g2\delta\mathcal E_{ab}.
```

The individual terms in its Euler coefficient are

```math
\delta(4H^2)=4gH_{ab}\delta\mathcal E^{ab},\qquad \delta\left(-\frac2{x^2}P^2\right)\doteq-\frac2{x^2}F(P)_{ab}\delta\mathcal E^{ab},
```

```math
\delta\left(-\frac{2\sqrt2}{x}P\!\cdot v\right)\doteq-\frac{\sqrt2}{x}F(v)_{ab}\delta\mathcal E^{ab},\qquad \delta(-4gP\!\cdot C)\doteq-2gG_{ab}\delta\mathcal E^{ab}.
```

For the second identity, for instance, $`-4P_a\nabla_b\delta\mathcal E^{ab}/x^2\doteq4(\nabla_bP_a)\delta\mathcal E^{ab}/x^2=-2F(P)_{ab}\delta\mathcal E^{ab}/x^2`$. No unconstrained variation of $`P`$ has been substituted for variation of $`E_3`$.

The equations obtained from (FD14) are therefore

```math
P_a=0,\qquad 2j_{Ga}-4gP_a=0,\qquad 4gH_{ab}-\frac2{x^2}F(P)_{ab}-\frac{\sqrt2}{x}F(v)_{ab}-2gG_{ab}=0,\qquad dH=0,\qquad V'_a{}^{ij}=0.
\tag{FD15}
```

They follow, respectively, by varying $`v`$, $`C`$, $`\mathcal E`$, $`B`$ and $`V'`$. For $`B`$, the variation of $`4H^2`$ is $`8H\cdot(-*d\delta B/2)`$; integration by parts sets the three-form $`dH`$ to zero. In particular, the apparent $`P^2`$ derivative term does not by itself establish propagation of $`E_3`$: $`v`$ remains a multiplier and first imposes $`P=0`$.

Locally, $`P=0`$ is equivalent to $`dE_3=0`$. The gauge transformation $`\delta E_3=d\Sigma_2`$, $`\delta B=d\Lambda_1-g\Sigma_2/2`$ can therefore set $`E_3=0`$ on a contractible patch. This step retains the $`\mathcal E`$ equation as a relation fixing $`F(v)`$; it does not discard that equation. The remaining identities/equations are

```math
j_G=0,\qquad j_H=0,\qquad dH=0,\qquad F(v)=\sqrt2gx(2H-G).
```

The Poincaré lemma gives $`H=dQ`$ locally. The complete reconstruction of the trace connection is then

```math
v=\sqrt2gx(2Q-C)+du.
\tag{FD16}
```

The exact one-form $`du`$ is removed by the residual trace SU(2) gauge transformation. The local physical equations are the two Maxwell systems $`\nabla^aF(C)_{ab}=0`$ and $`\nabla^aF(Q)_{ab}=0`$, with independent potential gauges $`C\mapsto C+d\alpha`$ and $`Q\mapsto Q+d\chi`$. Lorenz gauge gives $`(\nabla^2-4k)C_a=0`$ and $`(\nabla^2-4k)Q_a=0`$ with residual $`\nabla^2\alpha=\nabla^2\chi=0`$. The curvature term is the Maxwell curvature coupling; the Proca masses are both zero.

## 11. Dualization and the kinetic signs

The positive-looking $`+4cH^2`$ has the correct sign for the original two-form kinetic term: $`H_{ab}H^{ab}=-H_{3abc}H_3^{abc}/12`$, so it equals $`-cH_3^2/3`$. A naive on-shell substitution $`H=dQ`$ into $`+4cH^2`$ would nevertheless give the wrong dual-action sign.

After the multiplier constraint and tensor gauge reduction, a first-order dualization treats $`H`$ as independent and imposes its kinematic divergence identity with $`Q`$:

```math
\ell^{(2)}_{\mathrm{first\ order}}=-\frac c2F(C)^2+4cH^2-8cH^{ab}F(Q)_{ab}.
```

The $`Q`$ variation gives $`\nabla_aH^{ab}=0`$, which locally reconstructs $`H=-*dB/2`$. The $`H`$ variation gives $`8c(H-F(Q))=0`$. Eliminating this algebraic variable is valid for $`c\ne0`$ and gives

```math
\boxed{\ell^{(2)}_{\mathrm{physical\ forms}}=-\frac c2F(C)^2-4cF(Q)^2=-\frac14\left[2cF(C)^2+16cF(Q)^2\right].}
\tag{FD17}
```

Thus the two local kinetic coefficients in the $`-ZF^2/4`$ convention are $`Z_C=2c`$ and $`Z_Q=16c`$. Both have the positive Maxwell sign for $`c>0`$, assuming the accepted positive $`\kappa_5^2`$. Canonically normalized potentials within the displayed density are $`C_{\rm can}=\sqrt{2c}\,C`$ and $`Q_{\rm can}=4\sqrt c\,Q`$. Each massless vector has $`5-2=3`$ local polarizations; this block contributes six local bosonic degrees of freedom. These kinetic signs do not select global AdS falloffs or assert normalizability under an unspecified boundary condition.

At the endpoint $`x=2`$, $`c=0`$, the entire raw block (FD14) vanishes. Equations (FD15) were obtained only for $`c\ne0`$ and must not be imposed there after division. Neither the algebraic elimination nor the canonical normalization is invertible at that point. The correct quadratic conclusion is loss of control over these form fluctuations; a zero local degree-of-freedom count or a new nonlinear gauge symmetry does not follow.

## 12. Reproducible extension checks

The following second independent code block checks the newly included rational sums, the SU(2) contractions, branch simplification and dual Legendre transform. It writes no files.

```python
import sympy as s
q = s.Rational
x, a, g, p, r = s.symbols('x a g p r', nonzero=True)
c = 2-x
assert q(8,3)*q(-5,2)+q(8,3)*(-2)+q(20,3)*3 == 8
assert q(-40,3)*q(-5,2)+q(-4,3)*(-2)+q(-16,3)*3 == 20
assert q(16,3)/8+q(4,3)-2 == 0
assert -2*q(16,3)/8-q(8,3) == -4
eps = s.Matrix([[0,1],[-1,0]])
V = s.Matrix([[p,r],[r,-p]])
L = x*s.eye(2)/s.sqrt(2)
low = lambda Z: eps.T*Z*eps
norm = lambda Z: s.expand(sum(Z[i,j]*low(Z)[i,j]
                              for i in range(2) for j in range(2)))
DL = V*eps*L+L*(V*eps).T
DDL = V*eps*DL+DL*(V*eps).T
assert s.simplify(norm(DL)-2*x**2*norm(V)) == 0
assert s.simplify(s.trace(DDL)/s.sqrt(2)+2*x*norm(V)) == 0
box_piece = -2*s.trace(DDL)/s.sqrt(2)
gradient_piece = s.trace(low(DL)**2)/x
assert s.simplify(box_piece+gradient_piece-2*x*norm(V)) == 0
a_branch = 2*(1-x)/x**2
coefficients = [-x/2+(x-1), 4*x-8*(x-1), -2/x-2*a,
                -2*s.sqrt(2)*(1+a*x), -4*g+4*g*(x-1),
                2*x+2*a*x**2]
targets = [-c/2, 4*c, -2*c/x**2, -2*s.sqrt(2)*c/x, -4*g*c, 2*c]
for left,right in zip(coefficients,targets):
    assert s.factor((left-right).subs(a,a_branch)) == 0
z, f, cc = s.symbols('z f cc', nonzero=True)
first_order = 4*cc*z**2-8*cc*z*f
assert s.factor(s.diff(first_order,z)) == 8*cc*(z-f)
assert s.expand(first_order.subs(z,f)) == -4*cc*f**2
assert all(s.simplify(t.subs(x,2)) == 0 for t in targets)
print('PASS: additional currents, SU(2) factors, complete form coefficients and dual kinetic sign')
```

Both code blocks have been executed successfully. The extended result establishes the bosonic form/connection block, its local constraint reduction, its two massless vector eigenfields, and their kinetic signs for $`c>0`$. This result is local and concerns the displayed bosonic form/connection sector.
