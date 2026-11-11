#!/usr/bin/env python3
"""Restricted independent six-spinor calculation; not a full curved proof.

Run with the bundled Python (numpy required). Field coefficients are Gaussian
integers until the final projector normalization; comparison is performed after
clearing that denominator. Eight exterior generators retain anticommutativity.
C here is epsilon_down, NOT the C=epsilon_up label of Butter et al. Appendix A.
"""
import itertools as it, runpy, contextlib, io, json, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
from collections import defaultdict
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    cc=runpy.run_path(str(BASE/'scripts/common_conventions_check_frozen.py'))
C=np.array(cc['C']); U=-C; E=np.array([[0,1],[-1,0]])
eta=np.array([-1,1,1,1,1]); G=np.array([1j*np.array(x) for x in cc['g']])
S=np.array([[-(G[a]@G[b]-G[b]@G[a])/4 for b in range(5)] for a in range(5)])
GD=np.array([-x@C for x in G]); GU=np.array([U@x@U.T for x in GD])
SD=np.array([[-S[a,b]@C for b in range(5)] for a in range(5)])
SU=np.array([[U@SD[a,b]@U.T for b in range(5)] for a in range(5)])
def add(*xs):
    d=defaultdict(complex)
    for x in xs:
        for m,c in x.items():d[m]+=c
    return {m:c for m,c in d.items() if abs(c)>1e-9}
def scale(c,x):return {m:c*v for m,v in x.items() if abs(c*v)>1e-9}
def prod(*xs):
    d={0:1}
    for x in xs:
        o=defaultdict(complex)
        for m,c in d.items():
            for n,b in x.items():
                if m&n:continue
                sign=(-1)**sum((n&((1<<j)-1)).bit_count() for j in range(8) if m&(1<<j))
                o[m|n]+=sign*c*b
        d={m:c for m,c in o.items() if abs(c)>1e-9}
    return d
ll=[[{1<<(2*a+i):1} for i in range(2)] for a in range(4)]
lu=[[add(*[scale(U[a,b],ll[b][i]) for b in range(4)]) for i in range(2)] for a in range(4)]
ld=[[add(*[scale(E[j,i],ll[a][j]) for j in range(2)]) for i in range(2)] for a in range(4)]
lud=[[add(*[scale(E[j,i],lu[a][j]) for j in range(2)]) for i in range(2)] for a in range(4)]
def bil(i,j):return add(*[prod(lu[a][i],ll[a][j]) for a in range(4)])
def deriv(A,pol,Q):
    out=defaultdict(complex)
    for (n,m),c in pol.items():
        if not m&(1<<A):
            sign=(-1)**(m&((1<<A)-1)).bit_count()
            out[n+1,m|(1<<A)]+=-n*1j*c*sign
        ids=[j for j in range(8) if m&(1<<j)]
        for p,B in enumerate(ids):out[n,m^(1<<B)]+=(-1)**p*c*Q[A,B]
    return {k:v for k,v in out.items() if abs(v)>1e-9}
def raw(F,X,v):
    Fb=sum(F[a,b]*SD[a,b]/2 for a in range(5) for b in range(5))
    vb=sum(v[a]*GD[a] for a in range(5))
    Q=np.zeros((8,8),complex)
    for a,i,b,j in it.product(range(4),range(2),range(4),range(2)):
        Q[2*a+i,2*b+j]=-2*E[i,j]*Fb[a,b]-C[a,b]*X[i,j]-E[i,j]*vb[a,b]
    result={}
    pairs=[(a,b,U[a,b]) for a,b in it.product(range(4),repeat=2) if U[a,b]]
    for i,j in [(0,0),(0,1),(1,1)]:
        out=defaultdict(complex)
        for k,l,p,q in it.product(range(2),repeat=4):
            if not E[p,k]*E[q,l]:continue
            syms=list(it.permutations((i,j,k,l)))
            for s in syms:
                pref=E[p,k]*E[q,l]
                for (a,b,uv),(c,d,uw),(e,f,ux) in it.product(pairs,repeat=3):
                    word=(2*b+s[0],2*a+s[1],2*d+s[2],2*c+s[3],2*f+p,2*e+q)
                    pol={(1,1<<word[-1]):1j}
                    for A in word[-2::-1]:pol=deriv(A,pol,Q)
                    for key,val in pol.items():out[key]+=pref*uv*uw*ux*val
        result[i,j]={key:3j*val for key,val in out.items() if abs(val)>1e-7}
    return result
def expected(F,X,v):
    Xlow=E.T@X@E
    Fs=sum(eta[a]*eta[b]*F[a,b]**2 for a,b in it.product(range(5),repeat=2))
    Xs=sum(X[a,b]*Xlow[a,b] for a,b in it.product(range(2),repeat=2))
    vs=sum(eta[a]*v[a]**2 for a in range(5))
    out={}
    for i,j in [(0,0),(0,1),(1,1)]:
        ans={3:{0:X[i,j]*(Fs-Xs-2*vs)/8}}
        # P4: 8 terms with no field derivatives beyond dW.
        p4=scale(-3j/16*vs+3j/32*Fs-3j/32*Xs,bil(i,j))
        p4=add(p4,*[scale(-3j/16*X[i,j]*X[k,l],prod(lud[a][k],ld[a][l])) for a,k,l in it.product(range(4),range(2),range(2))])
        for ii,jj in [(i,j),(j,i)]:
            p4=add(p4,*[scale(-3j/16*GU[a,al,be]*v[a]*X[k,ii],prod(ll[al][jj],ld[be][k])) for a,al,be,k in it.product(range(5),range(4),range(4),range(2))])
        p4=add(p4,*[scale(3j/8*GU[a,al,be]*F[a,b]*eta[b]*v[b],prod(ll[al][i],ll[be][j])) for a,b,al,be in it.product(range(5),range(5),range(4),range(4))])
        p4=add(p4,*[scale(-3j/16*SU[a,b,al,be]*X[i,j]*F[a,b],prod(ll[al][k],ld[be][k])) for a,b,al,be,k in it.product(range(5),range(5),range(4),range(4),range(2))])
        for perm in it.permutations(range(5)):
            a,b,c,d,e=perm
            p4=add(p4,*[scale(-3j/64*cc['eps'](perm)*eta[a]*GU[a,al,be]*F[b,c]*F[d,e],prod(ll[al][i],ll[be][j])) for al,be in it.product(range(4),repeat=2)])
        ans[4]=p4
        p5={}
        for ii,jj in [(i,j),(j,i)]:
            p5=add(p5,*[scale(3/16*GU[a,al,be]*v[a],prod(ll[al][ii],lu[r][jj],ll[be][k],ld[r][k])) for a,al,be,r,k in it.product(range(5),range(4),range(4),range(4),range(2))])
        p5=add(p5,*[scale(3/8*SU[a,b,al,be]*F[a,b],prod(bil(i,j),ll[al][k],ld[be][k])) for a,b,al,be,k in it.product(range(5),range(5),range(4),range(4),range(2))])
        p5=add(p5,*[scale(3/8*X[k,l],prod(bil(i,j),lud[b][k],ld[b][l])) for k,l,b in it.product(range(2),range(2),range(4))])
        ans[5]=p5
        p6=add(*[scale(3j/32,prod(bil(i,j),bil(k,l),lud[c][k],ld[c][l])) for k,l,c in it.product(range(2),range(2),range(4))],*[scale(3j/16,prod(bil(i,k),bil(j,l),lud[c][k],ld[c][l])) for k,l,c in it.product(range(2),range(2),range(4))])
        ans[6]=p6
        out[i,j]={(n,m):z for n,p in ans.items() for m,z in p.items() if abs(z)>1e-8}
    return out
if __name__=='__main__':
    # Check source matrix symmetries, Clifford algebra and two-form conversion.
    for a,b in it.product(range(5),repeat=2):
        assert np.array_equal(G[a]@G[b]+G[b]@G[a],-2*eta[a]*np.eye(4) if a==b else np.zeros((4,4)))
        assert np.array_equal(SD[a,b],SD[a,b].T)
    for a in range(5):
        assert np.array_equal(GD[a],-GD[a].T)
        assert np.sum(U*GD[a])==0
    for a,b in it.combinations(range(5),2):
        ff=np.zeros((5,5));ff[a,b]=1;ff[b,a]=-1
        spin=sum(ff[c,d]*SD[c,d]/2 for c,d in it.product(range(5),repeat=2))
        for c,d in it.product(range(5),repeat=2):
            assert eta[c]*eta[d]*np.sum(SU[c,d]*spin)==ff[c,d]
    for a in range(5):
        spin=GD[a]
        for b in range(5):assert -eta[b]*np.sum(GU[b]*spin)/4==int(a==b)
    # Generic integer examples, plus isolated sectors and mixed pairs.
    F=np.zeros((5,5));F[0,1]=2;F[1,0]=-2;F[2,3]=3;F[3,2]=-3
    X=np.array([[2,3],[3,5]]);v=np.array([1,2,3,4,5])
    cases=[('X_only',F*0,X,v*0),('F_only',F,X*0,v*0),('gradient_only',F*0,X*0,v),
           ('F_X',F,X,v*0),('F_gradient',F,X*0,v),('X_gradient',F*0,X,v),('all',F,X,v)]
    rng=np.random.default_rng(230214295)
    for z in range(6):
        a=rng.integers(-3,4,size=(5,5));ff=a-a.T
        a=rng.integers(-3,4,size=(2,2));xx=a+a.T
        cases.append((f'integer_probe_{z+1}',ff,xx,rng.integers(-3,4,size=5)))
    report={'scope':'Flat constant F_ab, X_ij, nabla_a W and gaugino probe only. Weyl multiplet zero. Not a full curved proof.',
            'matrix_conventions':'Gold Gamma=i gamma; source epsilon_down second-slot lowering; C_code=epsilon_down; Sigma=-[Gamma,Gamma]/4',
            'arithmetic':'Gaussian integer sums with denominator 1280*24 cleared before comparison; exterior algebra on 8 gaugino generators',
            'probes':[],'full_curved_reduction':'OPEN','full_primary_S_K_linearity_reality_checks':'OPEN'}
    for label,ff,xx,vv in cases:
        r=raw(ff,xx,vv);p=expected(ff,xx,vv);count=0
        for ij in r:
            for key in set(r[ij])|set(p[ij]):
                lhs=r[ij].get(key,0);rhs=30720*p[ij].get(key,0)
                assert lhs.real==round(lhs.real) and lhs.imag==round(lhs.imag)
                assert rhs.real==round(rhs.real) and rhs.imag==round(rhs.imag)
                assert lhs==rhs,(label,ij,key,lhs,rhs)
                count+=1
        report['probes'].append({'name':label,'status':'PASS','coefficients_checked':count})
    # W^-5 is linear in F, X and nabla W and depends only on two-spinor jets.
    # Test every independent coefficient of those 18 bosonic components.
    fifth=[]
    for a,b in it.combinations(range(5),2):
        ff=np.zeros((5,5));ff[a,b]=1;ff[b,a]=-1
        fifth.append((f'F_{a}{b}',ff,np.zeros((2,2)),np.zeros(5)))
    for i,j in [(0,0),(0,1),(1,1)]:
        xx=np.zeros((2,2));xx[i,j]=xx[j,i]=1
        fifth.append((f'X_{i+1}{j+1}',np.zeros((5,5)),xx,np.zeros(5)))
    for a in range(5):
        vv=np.zeros(5);vv[a]=1
        fifth.append((f'dW_{a}',np.zeros((5,5)),np.zeros((2,2)),vv))
    for label,ff,xx,vv in fifth:
        r=raw(ff,xx,vv);p=expected(ff,xx,vv)
        for ij in r:
            for key in set(r[ij])|set(p[ij]):
                if key[0]==5:
                    assert r[ij].get(key,0)==30720*p[ij].get(key,0),(label,ij,key)
    report['W_inverse_5_coefficients']='PASS: all 18 independent F/X/gradient components and every four-generator Grassmann monomial; valid for this general inverse-power sector, but not a hand Fierz derivation'
    ledger=json.loads((BASE/'sources/step2/primary_term_ledger.json').read_text())
    assert [len(g['terms']) for g in ledger['groups']]==[2,7,12,18,14,3,2]
    assert sum(len(g['terms']) for g in ledger['groups'])==58
    benchmark=(BASE/'STEP_02_LOG_PRIMARY.md').read_text().split(
        '<!-- FULL_PRIMARY_BENCHMARK_BEGIN -->',1)[1].split(
        '<!-- FULL_PRIMARY_BENCHMARK_END -->',1)[0]
    for g in ledger['groups']:
        for term in g['terms']:
            # A source fragment's terminal sentence period is typography.
            # The collected display closes its pole's braces at that position.
            # Preserve the literal ledger and compare the entire mathematical
            # summand, including its sign, only within the published benchmark.
            assert term['latex'].removesuffix('.') in benchmark,term['id']
    report['source_term_coverage']='PASS: 58 ordered summands in final display; benchmark only'
    # Weight ledger is the independently declared physical weight of each factor.
    Q=__import__('fractions').Fraction
    weights=dict(w=1,W=1,l=Q(3,2),x=Q(3,2),u=Q(3,2),X=2,F=2,Y=2,Z=2,dw=2,dW=2,dl=Q(5,2),dx=Q(5,2),dX=3,dF=3,boxw=3,boxX=4,boxl=Q(7,2))
    terms={0:['W Z','x x'],1:['X Y','F Z','boxX','X W W','W u l','x dl','l dx'],
    2:['X boxw','dw dX','F u l','l boxl','dl dl','W l dl','l l dW','Y l l','F x l','W W l l','W W l l','X x l'],
    3:['X F F','X X X','X dw dw','F l dl','F l dl','l l dF','X l dl','X l dl','l dX l','l l boxw','dw l dl','dw l dl','W l l dw','W F l l','W F l l','X W l l','x l l l','x l l l'],
    4:['l l dw dw','X l l dw','F l l dw','F F l l','F F l l','X F l l','X X l l','X X l l','l l l dl','l l l dl','l l l dl','l l l dl','W l l l l','W l l l l'],
    5:['l l l l dw','F l l l l','X l l l l'],6:['l l l l l l','l l l l l l']}
    for n,tt in terms.items():
        assert len(tt)==len(ledger['groups'][n]['terms'])
        for t in tt:assert sum(weights[x] for x in t.split())-n==3
    report['source_weights']='PASS: all 58 summands weight three'
    for path in ['CONVENTIONS.md','LOG_CONVENTIONS.md','PROCEDURE_LOCK.md','sources/reference_fragments/10_gold_source_equations_and_bridge.md']:
        report.setdefault('inputs_sha256',{})[path]=hashlib.sha256((BASE/path).read_bytes()).hexdigest()
    (BASE/'sources/step2/checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: 13 flat constant-field probes with exact cleared coefficients; 58 weights and source-term coverage. Full curved proof OPEN.')
