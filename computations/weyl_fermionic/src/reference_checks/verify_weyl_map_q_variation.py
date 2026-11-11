#!/usr/bin/env python3
"""Independent finite-basis checks of notebook Part II; no EOM or truncation.

The imported S checker supplies Clifford matrices and a surjective projector.
It also runs its existing S-regression assertions. All arithmetic below is
integer-scaled Gaussian-integer arithmetic, represented exactly in binary64.
No tolerance or fitted coefficient is used. This does not rederive the input
curvature transformation laws from the elementary gauge fields.
"""
import itertools as it
import json
from pathlib import Path
from functools import lru_cache
import verify_weyl_map_s_invariance as s

I, Z, C, Ci, eta = s.I, s.Z, s.C, s.Ci, s.eta
add, scale, mul, trans = s.add, s.scale, s.mul, s.trans
mv, vsum, vscale = s.mv, s.vsum, s.vscale
ga = lru_cache(None)(s.ga)
pairs = s.pairs
ordered = list(it.product(range(5), repeat=2))
zero = [0j]*4
checks = {}
max_integer = 0

def same(a, b):
    global max_integer
    assert a == b, (a, b)
    vals = a+b
    if vals and isinstance(vals[0], list):
        vals = [z for row in vals for z in row]
    for z in vals:
        z = complex(z)
        assert z.real.is_integer() and z.imag.is_integer()
        max_integer = max(max_integer, abs(z.real), abs(z.imag))

def tilde(m):
    return mul(mul(Ci, trans(m)), C)

def raised(r):
    return [[vscale(eta[a]*eta[b],r[a][b]) for b in range(5)] for a in range(5)]

rup = [raised(r) for r in s.rbasis]

# Q13: both terms of a scalar bilinear produce the same ordered odd monomial.
for n in range(5):
    for ids in it.combinations(range(5),n):
        m=ga(ids)
        same(mul(trans(m),C),scale(-1,trans(mul(C,m))))
checks['odd_product_rule']='PASS: ranks0-4; A^T C=-(C A)^T, with parameter moved left'

# Q49-Q51: epsilon duality and the six-term four-form constraint.
def epsilon(ids):
    if len(set(ids))<5:
        return 0
    return (-1)**sum(ids[a]>ids[b] for a in range(5) for b in range(a+1,5))
for e,c,d in it.product(range(5),repeat=3):
    same(add(*[scale(epsilon((e,a,b,c,d)),ga((a,b),True)) for a,b in ordered]),
         scale(2j,ga((e,c,d))))
for r in s.rbasis:
    for a,b,c,d in it.combinations(range(5),4):
        same(vsum([mv(ga((a,b),True),r[c][d]),mv(ga((c,d),True),r[a][b]),
                   vscale(-1,mv(ga((a,c),True),r[b][d])),vscale(-1,mv(ga((b,d),True),r[a][c])),
                   mv(ga((a,d),True),r[b][c]),mv(ga((b,c),True),r[a][d])]),zero)
checks['four_form_constraint']='PASS: all125 epsilon-gamma identities and200 projected-curvature/four-form components'

# Q20: the transposed V-curvature operator, multiplied by6.
for vpair in pairs:
    v=s.t_basis(vpair)
    h=[]
    for a,b in ordered:
        h.append(add(*[scale(v[c][d],add(
            scale(eta[a]*eta[b],ga((a,b,c,d))),
            scale(-1,mul(ga((a,b),True),ga((c,d)))),
            scale(-0.5,mul(ga((c,d)),ga((a,b),True)))))
            for c,d in ordered]))
    # Factor1/2 multiplies two antisymmetric gamma products; entries remain integers.
    for r,ru in zip(s.rbasis,rup):
        lhs=vsum(mv(h[k],ru[a][b]) for k,(a,b) in enumerate(ordered))
        rhs=vscale(6,vsum(vscale(v[a][b]*eta[a]*eta[b],r[a][b]) for a,b in ordered))
        same(lhs,rhs)
checks['V_R_gamma_reduction']='PASS: 400 V/projected-R basis pairs, transposed source operator'

# Q23-Q25: 6 P_ab contains all four derivative structures before transposition.
# U[c][a][b]=D_c T_ab, all50 independent jets.
for c0 in range(5):
    for pair in pairs:
        u=[[[0]*5 for _ in range(5)] for _ in range(5)]
        u[c0]=s.t_basis(pair)
        dk=[add(*[scale(u[c][a][b],ga((a,b))) for a,b in ordered]) for c in range(5)]
        slash=add(*[mul(s.g[c],dk[c]) for c in range(5)])
        div=add(*[scale(eta[c]*eta[d]*u[c][c][d],s.gl[d]) for c,d in ordered])
        p6=[]
        for a,b in ordered:
            p6.append(add(scale(3,mul(dk[a],s.gl[b])),scale(-3,mul(dk[b],s.gl[a])),
                scale(-1,mul(s.gl[b],dk[a])),mul(s.gl[a],dk[b]),
                scale(-1,mul(mul(s.gl[a],slash),s.gl[b])),mul(mul(s.gl[b],slash),s.gl[a]),
                scale(-2,mul(ga((a,b),True),div))))
        for r,ru in zip(s.rbasis,rup):
            lhs=vsum(mv(tilde(p6[k]),ru[a][b]) for k,(a,b) in enumerate(ordered))
            rhs=vsum(vscale(-24*eta[a]*eta[b]*u[a][b][c],mv(s.g[c],r[a][b]))
                for a,b in ordered for c in range(5))
            same(lhs,rhs)
        # Q32: transpose of both D T terms of delta chi.
        left=add(*[scale(u[c][a][b],mul(s.g[c],ga((a,b)))) for a,b in ordered for c in range(5)],
                 *[scale(eta[b]*u[b][a][b],s.g[a]) for a,b in ordered])
        right=add(*[scale(u[a][b][c],mul(ga((a,b)),s.g[c])) for a,b in ordered for c in range(5)])
        same(left,right)
checks['DT_R']='PASS: all50 derivative jets x40 projected-R basis images; all four P terms retained'
checks['DT_chi']='PASS: all50 derivative jets, all matrix entries'

# Q38: SU(2) Schouten identity as an ordered epsilon-spinor coefficient identity.
# epsilon_{12}=1; V^i_k=V^{il}epsilon_lk; B=Vij bar(eps)^k z^l epsilon_lk.
eps=[[0,1],[-1,0]]
vtrip=[[[1,0],[0,0]],[[0,1],[1,0]],[[0,0],[0,1]]]
for v in vtrip:
    mixed=[[sum(v[i][l]*eps[l][k] for l in range(2)) for k in range(2)] for i in range(2)]
    for i,j,k,l in it.product(range(2),repeat=4):
        A2=mixed[i][k]*int(j==l)+mixed[j][k]*int(i==l)
        B2=2*v[i][j]*eps[l][k]
        C2=int(i==k)*mixed[j][l]+int(j==k)*mixed[i][l]
        assert A2-B2==C2
checks['SU2_recoupling']='PASS: all48 triplet/parameter/spinor coefficient choices, A-B=C'

# Quadratic polynomial basis: squares and pairwise sums determine every cross term.
tensors=[s.t_basis(pair) for pair in pairs]
tensors += [[[s.t_basis(p)[a][b]+s.t_basis(q)[a][b] for b in range(5)] for a in range(5)]
            for p,q in it.combinations(pairs,2)]
sample=None
for t in tensors:
    active=[(a,b) for a,b in ordered if t[a][b]]
    K=add(*[scale(t[a][b],ga((a,b))) for a,b in active])
    t2=sum(eta[a]*eta[b]*t[a][b]**2 for a,b in active)
    G4=add(*[scale(t[a][b]*t[c][d],ga((a,b,c,d))) for a,b in active for c,d in active])
    F=add(*[scale(eta[a]*eta[b]*t[a][b],mul(mul(s.gl[a],K),s.gl[b])) for a,b in active])
    same(F,add(G4,scale(2*t2,I)))
    # 9 times phi_(T2 chi): raw chi variation plus raw V variation.
    same(add(scale(-384,G4),scale(256*t2,I),scale(384,F)),scale(1024*t2,I))
    for ri,(r,ru) in enumerate(zip(s.rbasis,rup)):
        X=vsum(vscale(t[a][b],ru[a][b]) for a,b in active)
        KX=mv(K,X)
        W=vsum(vscale(t[a][b]*eta[a]*eta[b]*t[c][a]*eta[c],r[b][c])
                for a,b in active for c in range(5))
        Zcross=vsum(vscale(t[a][b]*eta[a]*eta[b]*t[c][d]*eta[c]*eta[d],
                          mv(mul(s.gl[d],s.gl[a]),r[b][c])) for a,b in active for c,d in active)
        same(W,zero)
        same(vscale(2,Zcross),KX)
        # Contract the six source S-curvature terms: here its four algebraic terms.
        # 3 T.S_algebraic = -8 KX +36 Z -9 KX -24 W.
        TS3=vsum([vscale(-8,KX),vscale(36,Zcross),vscale(-9,KX),vscale(-24,W)])
        same(TS3,KX)
        # Three contributions to 3 phi: -24 TS +16 KX =8 KX.
        raw_phi3=vsum([vscale(-8,TS3),vscale(16,KX)])
        same(raw_phi3,vscale(8,KX))
        printed_phi3=vscale(16,KX)
        residual3=vsum([raw_phi3,vscale(-1,printed_phi3)])
        same(residual3,vscale(-8,KX))
        if sample is None and s.vmax(residual3):
            sample={'T_lower':[[a,b,t[a][b]] for a,b in pairs if t[a][b]],
                    'R_seed':{'pair':pairs[ri//4],'spinor_column':ri%4,'projection_scale':12},
                    'R_lower_nonzero':[[a,b,[str(z) for z in r[a][b]]] for a,b in pairs if s.vmax(r[a][b])],
                    'KX':[str(z) for z in KX], 'three_times_phi_Q_minus_phi_printed':[str(z) for z in residual3]}
checks['T2_chi']='PASS: all55 polarization tensors, entire4x4 matrix; coefficient1024/9'
checks['T2_R']='PASS: all55 polarization tensors x40 R images; W=0, 2Z=KX, 3T.S_alg=KX'
checks['printed_map_negative_control']='PASS: derived coefficient8/3; printed16/3 leaves residual -8KX/3'

# Lorentz curvature term: transposition gives minus gamma_cd without any C symmetry assumptions.
for pair in pairs:
    same(tilde(ga(pair,True)),scale(-1,ga(pair,True)))
checks['C_R']='PASS: all10 gamma_cd matrices; (1/2)(1/4)(-1)=-1/8'
# Derivative terms of T.S and T.Dchi require only weighted antisymmetry.
for tpair in pairs:
    t=s.t_basis(tpair)
    for a,b in ordered:
        assert t[a][b]-t[b][a]==2*t[a][b]
checks['antisymmetric_derivative_terms']='PASS: brackets contract with T with unit coefficient; no IBP or derivative reordering'
checks['S_regression']=s.result['status']
assert max_integer<2**53
result={'lock':'UNG-WEYL2-OP58-CONVENTIONS-v4','status':'PASS',
        'result':'delta_Q L^ij=i bar(epsilon)^(i phi_Q^j); phi_Q=phi_M02-(8/3)(gamma.T)(T.R(Q))',
        'printed_M02_matching_status':'FAIL: nonzero T^2 R(Q) residual',
        'checks':checks,'negative_control_sample':sample,
        'arithmetic':'Integer-scaled Gaussian integers, no tolerance or coefficient fitting',
        'maximum_checked_integer':max_integer,
        'scope':'Algebraic cross-check of source-law-based hand variation, including complete polynomial basis for nontrivial reductions',
        'not_checked':['Independent rederivation of Q-curvature laws','S/Q law of phi_Q','E/N completion','full invariant','spectrum']}
if __name__=='__main__':
    out=Path(__file__).resolve().parents[1]/'.gpd/phases/02-ozkan-map-and-variation-completion/Q-VARIATION-CHECKS.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
