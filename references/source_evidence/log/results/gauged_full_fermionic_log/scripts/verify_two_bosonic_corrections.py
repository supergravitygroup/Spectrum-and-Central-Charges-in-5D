#!/usr/bin/env python3
"""Independent tensor/index check of the two scoped C24 discrepancies.

Uses C24 (2.21): [D_i,D_j] w_ab=-R_ij a^e w_eb-R_ij b^e w_ae.
Unlike the earlier coefficient ledger, does not assume P-Q=K-J/2.
It builds covariant second jets with this commutator and checks the exact
raw-minus-canonical density against the explicit boundary divergence.
This checks the printed-source comparison, not the superspace construction.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import random

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
N = 5
IX = range(N)


def one_case(seed, eta):
    rng = random.Random(seed)
    tuples = lambda n: product(IX, repeat=n)
    def sym():
        a = [[0]*N for _ in IX]
        for i in IX:
            for j in range(i,N):
                a[i][j] = a[j][i] = rng.randrange(-3,4)
        return a
    # Sums of Kulkarni-Nomizu products give nonconstant algebraic curvature.
    pairs = [(sym(),sym()) for _ in range(3)]
    R = {(a,b,c,d): sum(S[a][c]*T[b][d]+S[b][d]*T[a][c]
                       -S[a][d]*T[b][c]-S[b][c]*T[a][d]
                       for S,T in pairs) for a,b,c,d in tuples(4)}
    for a,b,c,d in tuples(4):
        assert R[a,b,c,d] == -R[b,a,c,d] == -R[a,b,d,c] == R[c,d,a,b]
        assert R[a,b,c,d]+R[a,c,d,b]+R[a,d,b,c] == 0
    def anti():
        a = [[0]*N for _ in IX]
        for i in IX:
            for j in range(i+1,N):
                a[i][j] = rng.randrange(-4,5); a[j][i] = -a[i][j]
        return a
    w = anti(); u = [anti() for _ in IX]
    second_sym = {}
    for i in IX:
        for j in range(i,N):
            second_sym[i,j] = second_sym[j,i] = anti()
    q = {}
    for i,j,a,b in tuples(4):
        comm = -sum(eta[e]*(R[i,j,a,e]*w[e][b]+R[i,j,b,e]*w[a][e]) for e in IX)
        q[i,j,a,b] = F(second_sym[i,j][a][b]) + F(comm,2)
    for i,j,a,b in tuples(4):
        assert q[i,j,a,b] == -q[i,j,b,a]
        assert q[i,j,a,b]-q[j,i,a,b] == -sum(eta[e]*(R[i,j,a,e]*w[e][b]+R[i,j,b,e]*w[a][e]) for e in IX)
    ric = {(a,b):sum(eta[c]*R[a,c,b,c] for c in IX) for a,b in tuples(2)}
    scalar = sum(eta[a]*ric[a,a] for a in IX)
    w2 = sum(eta[a]*eta[b]*w[a][b]**2 for a,b in tuples(2))
    J = sum(eta[a]*eta[b]*eta[c]*eta[d]*R[a,b,c,d]*w[a][b]*w[c][d] for a,b,c,d in tuples(4))
    Jcross = sum(eta[a]*eta[b]*eta[c]*eta[d]*R[a,b,c,d]*w[a][c]*w[b][d] for a,b,c,d in tuples(4))
    K = sum(eta[a]*eta[b]*eta[c]*ric[a,b]*w[a][c]*w[b][c] for a,b,c in tuples(3))
    kin = sum(eta[c]*eta[a]*eta[b]*u[c][a][b]**2 for c,a,b in tuples(3))
    P = sum(eta[a]*eta[b]*eta[c]*u[c][a][b]*u[b][a][c] for a,b,c in tuples(3))
    Q = sum(eta[a]*eta[b]*eta[c]*u[b][a][b]*u[c][a][c] for a,b,c in tuples(3))
    box = sum(eta[a]*eta[b]*eta[c]*w[a][b]*q[c,c,a,b] for a,b,c in tuples(3))
    second_A = sum(eta[a]*eta[b]*eta[c]*q[b,c,a,b]*w[a][c] for a,b,c in tuples(3))
    second_B = sum(eta[a]*eta[b]*eta[c]*q[c,b,a,b]*w[a][c] for a,b,c in tuples(3))
    assert 2*Jcross == J
    # -w^a_b[D^c,D^b]w_ac, obtained directly from the tensor representation.
    assert second_B-second_A == K-F(1,2)*J
    raw = F(1,3)*J+F(1,3)*Jcross-K-F(27,256)*scalar*w2
    raw += -F(39,16)*box+F(1,2)*second_A-2*second_B-F(33,16)*kin-F(9,4)*Q+F(3,4)*P
    canonical = F(3,8)*J-F(3,4)*K-F(27,256)*scalar*w2-F(3,8)*box
    # Divergence of -33/16 w^ab D^m w_ab +3/4 w_ac D^c w^am
    #               -9/4 w_a^m D_b w^ab; all product-rule terms retained.
    boundary = -F(33,16)*(kin+box)+F(3,4)*(P+second_A)-F(9,4)*(Q+second_B)
    assert raw-canonical-boundary == 0
    printed = canonical-F(1,8)*J
    assert raw-printed-boundary == F(1,8)*J
    return {'J':str(J),'printed_residual':str(F(1,8)*J),'corrected_residual':'0'}


def main():
    assert F(69,1024)*F(-128,3) == F(-23,8)
    assert F(3,2048)*F(-128,3)**2 == F(8,3)
    assert F(-3,32)*F(-128,3) == 4
    assert F(-23,8)*F(-128,3) == F(368,3)
    assert F(1,8)*F(2,3)**2*(-1) == F(-1,18)
    cases = {}
    for name,eta in [('lorentz',[-1,1,1,1,1]),('euclidean',[1]*5)]:
        cases[name] = [one_case(20260922+i,eta) for i in range(12)]
        assert any(c['J'] != '0' for c in cases[name])
    sha = lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    paths = [ROOT/'Sources/2024-Gold-Components-of-curvature-squared-invariants.pdf']
    paths += [BASE/'sources/equations'/f'C24-p{x:03d}.png' for x in [14,34,103,113]]
    paths += [BASE/'sources/correction_audit'/f'C24-p{x:03d}.png' for x in [45,150]]
    result = {'status':'PASS','date':'2026-09-22',
       'scope':'Source-level bosonic discrepancy audit; raw descendant assumed as input; no independent all-fermion/SUSY proof',
       'projection':'69/1024 * (-128/3) = -23/8; 3/2048 * (-128/3)^2 = 8/3; (-3/32) * (-128/3) = 4',
       'qualifier':'C24 (5.20) already has +23/8 w^2 D; 368/3 mismatch is in (4.8b)',
       'curvature':'24 tensor-jet cases, two signatures; raw=canonical_3/8+divJ; raw-canonical_1/4-divJ=Rww/8',
       'sources':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in paths],
       'cases':cases}
    dest=BASE/'sources/correction_audit/checks.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['sources','cases']},indent=2))


if __name__=='__main__': main()
