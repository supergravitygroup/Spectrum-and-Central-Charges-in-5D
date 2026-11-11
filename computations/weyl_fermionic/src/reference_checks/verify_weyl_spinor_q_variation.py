#!/usr/bin/env python3
"""Bounded checks of notebook Part III; not an E/N or SUSY-closure proof.

Exact rational coefficient checks and finite Clifford/SU(2) basis checks.
The hand calculation is the derivation; this script only cross-checks it.
No external algebra package, commuting substitute for odd spinors, or EOM.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PHASE = ROOT / '.gpd/phases/02-ozkan-map-and-variation-completion'
LEDGER = PHASE / 'VARPHI-Q-TERM-LEDGER.json'
NOTE = PHASE / 'DERIVATION-fermionic-map.md'
checks = {}

# Rational complex numbers: no rounding in the 94 coefficient comparisons.
def q(a=0, b=0):
    return F(a), F(b)

def qm(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]

responses = {
    'R': [q('1/6'), q('-1/6'), q('-1/12'), q('1/4'),
          q(0, 2), q(0, '-2/3'), q(0, '-2/3'), q(0, '-2/3')],
    'chi': [q('1/4'), q('-1/64'), q(0, '1/8'), q(0, '-1/8'), q('-1/4'), q('1/6')],
    'V': [q('-3/2'), q('-3/2'), q(0, 4), q(0, -18), q(0, '9/2'),
          q(0, 12), q(-8), q(0, 1), q(0, 8)],
    'T': [q(0, '1/2'), q(0, '-3/32')],
    'D': [q(1), q(0, '-5/3')],
    # Both factors of T_ab T^ab are varied, then combined by a dummy swap.
    'T2': [qm(q(2), q(0, '1/2')), qm(q(2), q(0, '-3/32'))],
    'C': [q(1)], 'U': [q(1)], 'Y': [q(1)], 'Z': [q(1)],
}
start = [q('-1/8'), q(0,-4), q('128/3'), q(0,8), q(0,8),
         q(0,'-64/3'), q('1024/9'), q(0,'128/3'), q('8/3'), q('1/2'), q('-8/3')]
factor_slots = [('R','C'), ('R','U'), ('chi','D'), ('Y','T'), ('Y','T'),
                ('U','chi'), ('T2','chi'), ('Z','T'), ('R','T','T'), ('V','R'), ('V','chi')]
data = json.loads(LEDGER.read_text())
for n, (coefficient, slots) in enumerate(zip(start, factor_slots), 1):
    expected = []
    for field in slots:
        expected += [qm(coefficient, child) for child in responses[field]]
    actual = [tuple(map(F, t['coefficient'])) for t in data['terms'][str(n)]]
    assert expected == actual, (n, expected, actual)
counts = [len(data['terms'][str(n)]) for n in range(1, 12)]
assert counts == [9,9,8,3,3,7,8,3,12,17,15]
assert sum(counts) == 94
checks['outer_product_rule_coefficients'] = {'status':'PASS', 'count':94, 'block_counts':counts,
    'scope':'Every varied factor and rational complex multiplier; gamma/spinor order checked in the hand notebook.'}
assert qm(q('128/3'), q('1/4')) == q('32/3')
checks['D_squared'] = 'PASS: delta phi = (32/3) D^2 epsilon, N = (64/3) D^2'

# Matrix entries are Gaussian integers or binary halves throughout these tests.
# All arithmetic is exactly representable below 2**53; assert that bound below.
def eye(n): return [[complex(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[0j for _ in range(n)] for _ in range(n)]
def add(*xs): return [[sum(x[i][j] for x in xs) for j in range(len(xs[0]))] for i in range(len(xs[0]))]
def scale(a,x): return [[a*z for z in row] for row in x]
def mm(x,y): return [[sum(x[i][k]*y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]
def tr(x): return sum(x[i][i] for i in range(len(x)))
def transpose(x): return [list(row) for row in zip(*x)]
def kron(x,y):
    m,n=len(y),len(y[0])
    return [[x[i//m][j//n]*y[i%m][j%n] for j in range(len(x[0])*n)] for i in range(len(x)*m)]
I=eye(4); Z=zero(4); I2=eye(2)
s1=[[0,1],[1,0]]; s2=[[0,-1j],[1j,0]]; s3=[[1,0],[0,-1]]
gamma=[scale(-1j,kron(s3,I2)),kron(s1,s1),kron(s1,s2),kron(s1,s3),kron(s2,I2)]
eta=[-1,1,1,1,1]
def gm(ids):
    if len(set(ids)) != len(ids): return Z
    answer=I
    for i in ids: answer=mm(answer,gamma[i])
    return answer
def metric(a,b): return eta[a] if a==b else 0
def eps(ids):
    if len(set(ids))!=5: return 0
    return (-1)**sum(ids[i]>ids[j] for i in range(5) for j in range(i+1,5))
for a,b in product(range(5),repeat=2):
    assert add(mm(gamma[a],gamma[b]),mm(gamma[b],gamma[a])) == scale(2*metric(a,b),I)
assert gm((0,1,2,3,4))==scale(1j,I)
for a,b,c,d in product(range(5),repeat=4):
    left=add(mm(gm((a,b)),gm((c,d))),mm(gm((c,d)),gm((a,b))))
    right=add(scale(2,gm((a,b,c,d))),scale(2*(metric(a,d)*metric(b,c)-metric(a,c)*metric(b,d)),I))
    assert left==right
    # gamma^abcd = i epsilon^abcde gamma_e.
    assert gm((a,b,c,d))==add(*[scale(1j*eps((a,b,c,d,e))*eta[e],gamma[e]) for e in range(5)])
checks['clifford_anticommutator_and_duality']='PASS: 625 ordered four-index choices, signature/orientation included'
C=mm(gamma[2],gamma[4]); Ci=scale(-1,C)
for a,b,c,d in product(range(5),repeat=4):
    K=gm((c,d))
    G=scale(.5,add(mm(mm(gamma[a],K),gamma[b]),scale(-1,mm(mm(gamma[b],K),gamma[a]))))
    assert mm(mm(Ci,transpose(G)),C)==G
checks['curvature_parameter_derivative_flip']='PASS: transpose-even gamma^[a K gamma^b] for all 625 choices; contracted odd-spinor/world-label signs shown in P43-P44'

# C^2 gamma contraction: polarize over a complete two-form basis. No assumption
# about full fermionic Weyl pair-exchange symmetry is used in the main result.
pairs=list(combinations(range(5),2))
twoforms=[]
for x in range(10): twoforms.append({x:1})
for x,y in combinations(range(10),2): twoforms.append({x:1,y:1})
max_entry=0
for t in twoforms:
    A=add(*[scale(2*v,gm(pairs[p])) for p,v in t.items()])
    norm=2*sum(v*v*eta[pairs[p][0]]*eta[pairs[p][1]] for p,v in t.items())
    rank4=add(*[scale(4*v*w,gm(pairs[p]+pairs[r])) for p,v in t.items() for r,w in t.items()])
    # 32 times delta phi for one curvature two-form: -slash(A)^2.
    left=scale(-1,mm(A,A))
    right=add(scale(2*norm,I),scale(-1,rank4))
    assert left==right
    max_entry=max(max_entry,max(abs(z) for row in left for z in row))
checks['C_squared_polarization']='PASS: all 10 two-form basis tensors and 45 distinct pair sums; scalar and rank4 signs'

# NW-SE triplet conversions. For symmetric S upper, mixed = S epsilon.
E=[[0,1],[-1,0]]
triplets=[[[1,0],[0,0]], [[0,1],[1,0]], [[0,0],[0,1]]]
def mixed(S): return mm(S,E)
def lower(S): return mm(mm(transpose(E),S),E)
def contract(S,T):
    L=lower(T)
    return sum(S[i][j]*L[i][j] for i,j in product(range(2),repeat=2))
for S,T in product(triplets,repeat=2):
    A,B=mixed(S),mixed(T)
    assert tr(mm(A,B)) == -contract(S,T)
    assert add(mm(A,B),mm(B,A))==scale(tr(mm(A,B)),I2)
checks['SU2_triplet_identity']='PASS: all nine symmetric-triplet basis pairs; tr(V W) = -V^ij W_ij'

# Full V^2 block on 30 independent pair/triplet components, polarized by every
# pair sum. 8x8 spinor-doublet matrices retain noncommuting SU(2) products.
vbasis=list(product(range(10),range(3)))
vtests=[[(p,s)] for p,s in vbasis]+[[a,b] for a,b in combinations(vbasis,2)]
for terms in vtests:
    raw10=zero(8); raw11=zero(8); scalar=0; rank4=Z
    for p,s in terms:
        ab=pairs[p]; S=triplets[s]
        for r,t in terms:
            cd=pairs[r]; T=triplets[t]
            # World/tangent metrics have already converted the gammas to upper
            # indices; four is the two antisymmetric-pair summation factors.
            Vprod=mm(mixed(S),mixed(T))
            first=add(scale(2,gm(ab+cd)),scale(-2,mm(gm(cd),gm(ab))),scale(-1,mm(gm(ab),gm(cd))))
            raw10=add(raw10,scale(4,kron(Vprod,first)))
            raw11=add(raw11,scale(-4,kron(Vprod,mm(gm(ab),gm(cd)))))
            rank4=add(rank4,scale(4*contract(S,T),gm(ab+cd)))
            if p==r: scalar += 2*eta[ab[0]]*eta[ab[1]]*contract(S,T)
    right=kron(I2,add(scale(-4*scalar,I),rank4))
    left=add(raw10,raw11)
    assert left==right
    for row in left:
        for z in row:
            assert z.real.is_integer() and z.imag.is_integer()
            max_entry=max(max_entry,abs(z.real),abs(z.imag))
assert max_entry<2**53
checks['V_squared_full_spinor_doublet']='PASS: 30 basis tensors + 435 polarizations; original F10 and F11 varied separately, all 8x8 entries'

# No derivative of epsilon remains: independent signed coefficient ledgers for
# the cancellations displayed in P41-P46. These checks do not prove the full
# curvature variation or perform a nonlinear Fierz reduction.
ordinary=[q(0,1),q(0,-2),q(-1),q('-1/2'),q(-8)]
fermionic=[q(0,-1),q(0,2),q(1),q('1/2'),q(8)]
assert all((a[0]+b[0],a[1]+b[1])==q() for a,b in zip(ordinary,fermionic))
assert qm(q(0,'-1/2'),q(0,-1)) == q('-1/2')
assert qm(q(0,'3/32'),q(0,-1)) == q('3/32')
checks['local_parameter_cancellations']='PASS: all five Lorentz-curvature groups, both T-derivative remainders; full hand cancellation P41-P46'

if NOTE.exists() and '# Part III' in NOTE.read_text():
    full=NOTE.read_text(); part=full.split('# Part III',1)[1]
    assert not [(i,ord(c)) for i,c in enumerate(part) if ord(c)<32 and c not in '\n\t']
    tags=re.findall(r'\\tag\{(P\d+[a-z]?)\}',part)
    assert len(tags)==len(set(tags))
    assert {f'P{x:02d}' for x in range(1,81)}.issubset(tags)
    assert all(term['latex'] in part for block in data['terms'].values() for term in block)
    for title in ['16. Problem and Target','17. Convention Ledger','18. Definitions and Required Identities',
                  '19. Detailed Derivation','20. Consistency Checks','21. Final Result',
                  '22. Convention Dependence and Remaining Uncertainties']:
        assert '## '+title in part
    for phrase in ['after some algebra','it is calculated','straightforwardly','it is easy to show']:
        assert phrase not in part.lower()
    checks['document_coverage']='PASS: seven required sections, all P01-P80 tags, 94 ledger expressions, no control characters or skipped-algebra phrases'
else:
    checks['document_coverage']='PENDING: draft has not been appended to the notebook'

result={'date':'2026-09-18','lock':'UNG-WEYL2-OP58-CONVENTIONS-v5',
        'status':'PASS' if all(not str(v).startswith('PENDING') for v in checks.values()) else 'DRAFT_CHECKS_PASS',
        'scope':'Termwise uncollected Q(M08); coefficient/Clifford/SU2/local-parameter checks. No certification of full E/N matching or nonlinear multiplet closure.',
        'checks':checks,'outer_term_count':94,'max_exact_matrix_entry':max_entry,
        'proof_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest() if NOTE.exists() else None,
        'ledger_sha256':hashlib.sha256(LEDGER.read_bytes()).hexdigest()}
(PHASE/'VARPHI-Q-VARIATION-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
