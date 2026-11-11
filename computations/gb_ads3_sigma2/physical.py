"""Certified physical divisors and gauge-invariant propagators.

If K=C M R, every maximal minor is det(C_I) det(M) det(R_J).
The gcd G of explicitly exhibited minors is the full determinantal divisor
when G is coprime, as a polynomial in D, to every denominator of C and R.
This is the stopping certificate, not a count of unchanged random minors.
All operations are over QQ(L,k,S)[D]; couplings are never sampled.
"""
import json
from itertools import combinations
import sympy as s
from polynomial_matrix import (Fraction,ONE,ZERO,poly,expr,extract,rational,
    polynomial_rows,rational_chart,rational_inverse,primitive_in_D)

def matmul(A,B):
    return [[sum((x*y for x,y in zip(row,col)),Fraction(0))
             for col in zip(*B)] for row in A]

def fractions(A):return [[Fraction(e) for e in row] for row in A]

def small_det(A):
    if not A:return Fraction(1)
    if len(A)==1:return A[0][0]
    return sum(((-1)**j*A[0][j]*small_det([row[:j]+row[j+1:] for row in A[1:]])
                for j in range(len(A)) if A[0][j]),Fraction(0))

def plucker_denominator(T):
    """For [I;T], gcd of all maximal minors is 1/lcm(reduced denominators).

    Its minors are, up to sign, every square minor of T, including 1.
    Enumerating these is an exact fallback when a chart crosses a physical root.
    """
    den=ONE;count=1
    if not T:return den,count
    for size in range(1,min(len(T),len(T[0]))+1):
        for rows in combinations(range(len(T)),size):
            for cols in combinations(range(len(T[0])),size):
                d=small_det([[T[i][j] for j in cols] for i in rows]).den
                den=den*(d/den.gcd(d));count+=1
    return den,count

def pack_polynomial(p):
    unit,factors=p.factor()
    return {'coefficient':str(unit),'factors':[[str(f),m] for f,m in factors]}

def pack_fraction(f):
    return {'numerator':pack_polynomial(f.num),'denominator':pack_polynomial(f.den)}

def certificate(K,record,chart=None,progress=None):
    A,scales=polynomial_rows(K)
    if chart is None:
        rank,rows,cols=rational_chart(A,progress)
    else:
        rows,cols=chart;rank=len(rows)
    if rank==0:
        assert all(not e for row in A for e in row)
        return {'rank':0,'physical_divisor':pack_polynomial(ONE),'probes':{}},None
    M=extract(A,rows,cols)
    inv,det=rational_inverse(M,progress,with_det=True)
    detpoly=det.num/det.den
    freea=[j for j in range(K.cols) if j not in cols]
    freeb=[i for i in range(K.rows) if i not in rows]
    C=[[Fraction(int(i==rows[h])) for h in range(rank)] for i in range(K.rows)]
    R=[[Fraction(int(j==cols[h])) for j in range(K.cols)] for h in range(rank)]
    for i in freeb:
        C[i]=matmul(fractions(extract(A,[i],cols)),inv)[0]
    for j in freea:
        column=matmul(inv,fractions(extract(A,rows,[j])))
        for h in range(rank):R[h][j]=column[h][0]
    for i in range(K.rows):
        for j in freea:
            value=sum((Fraction(A[i][cols[h]])*R[h][j] for h in range(rank)),Fraction(0))
            assert not (value-Fraction(A[i][j])),('right rank factorization',i,j)
    for i in freeb:
        for j in range(K.cols):
            value=sum((C[i][h]*Fraction(A[rows[h]][j]) for h in range(rank)),Fraction(0))
            assert not (value-Fraction(A[i][j])),('left rank factorization',i,j)
    denominator=ONE
    for T in (C,R):
        for row in T:
            for f in row:
                denominator=denominator*(f.den/denominator.gcd(f.den))
    divisor=primitive_in_D(detpoly)
    witnesses=[{'rows':rows,'cols':cols}]
    # One row and one column exchange, including the unchanged sets. Each
    # determinant is obtained from the verified rank factorization exactly.
    rchoices=[(Fraction(1),rows)]
    cchoices=[(Fraction(1),cols)]
    for i in range(K.rows):
        if i not in rows:
            for h in range(rank):
                if C[i][h]:rchoices.append((C[i][h],rows[:h]+[i]+rows[h+1:]))
    for j in range(K.cols):
        if j not in cols:
            for h in range(rank):
                if R[h][j]:cchoices.append((R[h][j],cols[:h]+[j]+cols[h+1:]))
    for a,ri in rchoices:
        for b,cj in cchoices:
            if primitive_in_D(divisor.gcd(denominator)).degrees()[2]<=0:break
            candidate=det*a*b
            p=candidate.num/candidate.den
            new=primitive_in_D(divisor.gcd(p))
            if new.degrees()[2]<divisor.degrees()[2]:
                divisor=new;witnesses.append({'rows':ri,'cols':cj})
        if primitive_in_D(divisor.gcd(denominator)).degrees()[2]<=0:break
    coprime=primitive_in_D(divisor.gcd(denominator)).degrees()[2]<=0
    extra={}
    if not coprime:
        left,nleft=plucker_denominator([C[i] for i in freeb])
        right,nright=plucker_denominator([[R[h][j] for h in range(rank)] for j in freea])
        full=det/Fraction(left*right)
        assert full.den.degrees()[2]<=0
        divisor=primitive_in_D(full.num)
        extra=dict(plucker_left_denominator=pack_polynomial(left),
                   plucker_right_denominator=pack_polynomial(right),
                   maximal_factor_minors_enumerated=[nleft,nright])
    # Every selected single-component probe must annihilate both gauge spaces.
    probes={}
    for ia,a in enumerate(record['avars']):
        partner='b_'+a[2:].translate(str.maketrans('pm','mp'))
        if partner not in record['bvars']:continue
        ib=record['bvars'].index(partner)
        if ia not in cols or ib not in rows:continue
        ja,jb=cols.index(ia),rows.index(ib)
        if any(R[ja][j] for j in freea) or any(C[i][jb] for i in freeb):continue
        num,den=s.fraction(scales[ib]);scale=Fraction(poly(num),poly(den))
        probes[a[2:]]=pack_fraction(inv[ja][jb]*scale)
    probe_names=list(probes)
    observables_a={p:{record['avars'].index('a_'+p):Fraction(1)} for p in probe_names}
    observables_b={p:{record['bvars'].index('b_'+p.translate(str.maketrans('pm','mp'))):Fraction(1)} for p in probe_names}
    # The second neutral flat mode is invisible to the component probes.
    # A magnetic three-form combination supplies a fourth independent probe.
    if record.get('harmonic_chart')!='flat Fourier' and K.has(s.Symbol('S')) and all('a_E_'+c in record['avars'] for c in ('p23','p34')):
        from model import L,k,D,S,P2,P3,P4
        q=L**2*k-3*L*k-2*L+8
        aa={record['avars'].index('a_E_p34'):Fraction(1),
            record['avars'].index('a_B_p3'):rational(4*L*(S-1)*q/P4)}
        bb={record['bvars'].index('b_E_m34'):Fraction(1),
            record['bvars'].index('b_B_m3'):rational(-4*L*S*q/P4)}
        right=[aa.get(j,Fraction(0))-sum((aa.get(cols[h],Fraction(0))*R[h][j] for h in range(rank)),Fraction(0)) for j in freea]
        left=[bb.get(i,Fraction(0))-sum((bb.get(rows[h],Fraction(0))*C[i][h]*rational(scales[rows[h]]/scales[i]) for h in range(rank)),Fraction(0)) for i in freeb]
        assert all(not x for x in right+left),'magnetic three-form probe is not gauge invariant'
        observables_a['H_p34']=aa;observables_b['H_p34']=bb;probe_names.append('H_p34')
        # Transverse projection of the other mixed metric vector. D=-1,3
        # are chart poles, so these points require another probe/chart.
        for radial_den in (D+1,3-D,D-3,-D-1):
            aa={record['avars'].index('a_h_p4'):Fraction(1),
                record['avars'].index('a_h_p2'):rational(S*P2/(radial_den*P3))}
            bb={record['bvars'].index('b_h_m4'):Fraction(1),
                record['bvars'].index('b_h_m2'):rational((1-S)*P2/(radial_den.subs(D,2-D)*P3))}
            right=[aa.get(j,Fraction(0))-sum((aa.get(cols[h],Fraction(0))*R[h][j] for h in range(rank)),Fraction(0)) for j in freea]
            left=[bb.get(i,Fraction(0))-sum((bb.get(rows[h],Fraction(0))*C[i][h]*rational(scales[rows[h]]/scales[i]) for h in range(rank)),Fraction(0)) for i in freeb]
            if all(not x for x in right+left):break
        else:raise AssertionError('transverse metric probe is not gauge invariant')
        observables_a['h_p4_transverse']=aa;observables_b['h_p4_transverse']=bb;probe_names.append('h_p4_transverse')
    propagator=[]
    for pa in probe_names:
        line=[]
        for pb in probe_names:
            value=Fraction(0)
            for ia,va in observables_a[pa].items():
                if ia not in cols:continue
                for ib,vb in observables_b[pb].items():
                    if ib not in rows:continue
                    value+=va*inv[cols.index(ia)][rows.index(ib)]*rational(scales[ib])*vb
            line.append(pack_fraction(value))
        propagator.append(line)
    for i,p in enumerate(probe_names):probes[p]=propagator[i][i]
    result={'rank':rank,'shape':list(K.shape),'rows':rows,'cols':cols,
        'row_scales':list(map(str,scales)),
        'physical_divisor':pack_polynomial(divisor),
        'chart_denominators':pack_polynomial(denominator),
        'minor_witnesses':witnesses,'rank_factorization_verified':True,
        'denominators_coprime_to_divisor_in_D':coprime,
        'proof_method':'coprime chart' if coprime else 'all factor Plucker minors',
        'gauge_right':[[pack_fraction(x) for x in row] for row in R],
        'gauge_left':[[pack_fraction(x) for x in row] for row in C],
        'probes':probes,'probe_names':probe_names,'propagator':propagator,
        'observables_a':{p:{str(i):pack_fraction(v) for i,v in c.items()} for p,c in observables_a.items()},
        'observables_b':{p:{str(i):pack_fraction(v) for i,v in c.items()} for p,c in observables_b.items()},**extra}
    return result,divisor
