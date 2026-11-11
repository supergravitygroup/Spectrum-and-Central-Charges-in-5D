#!/usr/bin/env python3
"""Check the displayed projected derivation through W^-4, not the full primary.

Eight lambda and forty covariant derivative-lambda exterior generators are
independent. The W^-4 coefficient is evaluated from the projector product
rule and the derived second derivative of lambda, then compared to S23.
No lower-pole completeness claim is made.
"""
import runpy, json, hashlib
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
globals().update({k:v for k,v in runpy.run_path(str(BASE/'scripts/verify_log_step2.py')).items() if not k.startswith('__')})
def prod(*xs):
 d={0:1}
 for x in xs:
  o=defaultdict(complex)
  for m,c in d.items():
   for n,b in x.items():
    if m&n:continue
    sign=(-1)**sum((n&((1<<j)-1)).bit_count() for j in range(m.bit_length()) if m&(1<<j))
    o[m|n]+=sign*c*b
  d={m:c for m,c in o.items() if abs(c)>1e-9}
 return d
dl=[[[{1<<(8+8*a+2*b+i):1} for i in range(2)] for b in range(4)] for a in range(5)]
dlu=[[[add(*[scale(U[b,c],dl[a][c][i]) for c in range(4)]) for i in range(2)] for b in range(4)] for a in range(5)]
dld=[[[add(*[scale(E[j,i],dl[a][b][j]) for j in range(2)]) for i in range(2)] for b in range(4)] for a in range(5)]
def eps4(a,b,c,d):return U[a,b]*U[c,d]-U[a,c]*U[b,d]+U[a,d]*U[b,c]
def Rplus(W,derivative=True):
 R={}
 for c,d,r in it.product(range(4),repeat=3):
  terms=[]
  if derivative:
   terms += [scale(1j*(GD[a,c,d]*int(t==r)+GD[a,c,r]*int(t==d)+C[c,d]*G[a,r,t]+C[c,r]*G[a,d,t]-C[d,r]*G[a,c,t]-GD[a,d,r]*int(t==c)),dl[a][t][0]) for a in range(5) for t in range(4)]
  terms += [scale(1j*W[d,r],ll[c][0]),scale(-1j*W[c,r],ll[d][0])]
  terms += [scale(-3j*C[c,d]*W[r,t],lu[t][0]) for t in range(4)]
  R[c,d,r]=add(*terms)
 return R
def p4raw(F,X,v,W,derivative=True):
 Fspin=sum(F[a,b]*SD[a,b]/2 for a,b in it.product(range(5),repeat=2));vspin=sum(v[a]*GD[a] for a in range(5))
 Q=-2*Fspin-C*X[0,1]-vspin
 R=Rplus(W,derivative)
 ds=[add(*[scale(G[a,r,t],dl[a][t][1]) for a in range(5) for t in range(4)]) if derivative else {} for r in range(4)]
 db=[add(*[scale(-2*Q[r,t],lu[t][1]) for t in range(4)]) for r in range(4)]
 terms=[scale(-3j/8*X[0,0]*X[1,1],bil(0,0)),scale(-3j/16*X[0,0]**2,bil(1,1))]
 terms += [scale(-3/4,prod(bil(0,0),lu[r][0],ds[r])) for r in range(4)]
 terms += [scale(3/8*W[r,t],prod(bil(0,0),lu[r][0],lu[t][1])) for r,t in it.product(range(4),repeat=2)]
 terms += [scale(3j/16*X[0,0],prod(lu[r][0],db[r])) for r in range(4)]
 for a,b,c,d in it.product(range(4),repeat=4):
  if not eps4(a,b,c,d):continue
  dd=add(*[scale(-2,prod(R[c,d,r],lu[r][1])) for r in range(4)],{0:-2*sum(Q[d,r]*U[r,s]*Q[c,s] for r,s in it.product(range(4),repeat=2))})
  terms.append(scale(-3j/64*eps4(a,b,c,d),prod(ll[a][0],ll[b][0],dd)))
 terms += [scale(-3/2*W[r,t],prod(bil(0,0),lu[r][0],lu[t][1])) for r,t in it.product(range(4),repeat=2)]
 return add(*terms)
def expectedextra(Wab,derivative=True):
 terms=[]
 if derivative:
  for a,al,be,r,k in it.product(range(5),range(4),range(4),range(4),range(2)):
   g=GU[a,al,be]
   terms += [scale(-15/64*g,prod(ll[al][0],ll[be][0],lu[r][k],dld[a][r][k])),scale(-9/32*g,prod(ll[al][0],lu[r][0],ll[be][k],dld[a][r][k])),scale(-15/32*g,prod(ll[al][0],lu[r][0],ll[r][k],dld[a][be][k])),scale(-15/64*g,prod(lu[r][0],ll[r][0],ll[al][k],dld[a][be][k]))]
 for a,b,al,be,r,k in it.product(range(5),range(5),range(4),range(4),range(4),range(2)):
  g=SU[a,b,al,be]*Wab[a,b]
  terms += [scale(9/32*g,prod(ll[al][0],lu[r][0],ll[be][k],ld[r][k])),scale(9/64*g,prod(lu[r][0],ll[r][0],ll[al][k],ld[be][k]))]
 return add(*terms)

def assert_poly_equal(a,b,label):
    # All arithmetic here is Gaussian integers and powers of two. This tests
    # exact equality in binary floating representation, not a tolerance fit.
    for m in set(a)|set(b):
        assert a.get(m,0)==b.get(m,0), (label,m,a.get(m,0),b.get(m,0))

def check_three_spinors():
    for a,b,c in it.product(range(4),repeat=3):
        rhs=scale(.5,prod(bil(0,0),add(scale(C[a,b],ll[c][0]),scale(-C[a,c],ll[b][0]),scale(C[b,c],ll[a][0]))))
        assert_poly_equal(prod(ll[a][0],ll[b][0],ll[c][0]),rhs,'S2-39')

def check_derivative_contractions():
    basis=[]
    for typ in range(4):
        terms=[]
        for a,al,be,r in it.product(range(5),range(4),range(4),range(4)):
            t=[prod(ll[al][0],ll[be][0],lu[r][1],dl[a][r][0]),prod(ll[al][0],lu[r][0],ll[be][1],dl[a][r][0]),prod(ll[al][0],lu[r][0],ll[r][1],dl[a][be][0]),prod(lu[r][0],ll[r][0],ll[al][1],dl[a][be][0])][typ]
            terms.append(scale(GU[a,al,be],t))
        basis.append(add(*terms))
    rows=[(2,0,0,0),(.5,1,1,-.5),(0,0,0,2),(-.5,1,1,.5),(-.5,1,1,.5),(.5,1,1,-.5)]
    for term,row in enumerate(rows):
        terms=[]
        for al,be,c,d,r,a,t in it.product(range(4),range(4),range(4),range(4),range(4),range(5),range(4)):
            z=eps4(al,be,c,d)
            if not z:continue
            g=[GD[a,c,d]*int(t==r),GD[a,c,r]*int(t==d),C[c,d]*G[a,r,t],C[c,r]*G[a,d,t],-C[d,r]*G[a,c,t],-GD[a,d,r]*int(t==c)][term]
            if g:terms.append(scale(z*g,prod(ll[al][0],ll[be][0],dl[a][t][0],lu[r][1])))
        assert_poly_equal(add(*terms),add(*[scale(z,p) for z,p in zip(row,basis)]),'S2-57 row '+str(term))
    assert_poly_equal(add(basis[0],scale(-2,basis[1]),scale(2,basis[2]),basis[3]),{},'S2-58')

def source_R(W,lam,dlam):
    """S2-45 before Clifford reduction; no benchmark coefficients used."""
    out=np.zeros((4,4,4),complex);Wm=-W@U;up=U@lam
    for c,d,r in it.product(range(4),repeat=3):
        out[c,d,r]=1j*sum(GD[a,c,d]*dlam[a,r]+GD[a,c,r]*dlam[a,d]+C[c,d]*sum(G[a,r,t]*dlam[a,t] for t in range(4))+C[c,r]*sum(G[a,d,t]*dlam[a,t] for t in range(4))-C[d,r]*sum(G[a,c,t]*dlam[a,t] for t in range(4))-GD[a,d,r]*dlam[a,c] for a in range(5))
        out[c,d,r]+=1j*(W[d,r]*lam[c]-(W[c,d]*lam[r]+W[c,r]*lam[d])/2+1.5*(C[c,d]*(Wm@lam)[r]+C[c,r]*(Wm@lam)[d])+.5*C[d,r]*(W@up)[c]-sum(GD[a,d,r]*eta[a]*((3*G[a]@Wm-Wm@G[a])@lam)[c]/4 for a in range(5)))
    return out

def check_R_and_clifford():
    zeroW=np.zeros((4,4),complex);zeroL=np.zeros(4);zeroDL=np.zeros((5,4))
    cases=[]
    for a,b in it.combinations_with_replacement(range(4),2):
        w=zeroW.copy();w[a,b]=w[b,a]=1
        for c in range(4):
            l=zeroL.copy();l[c]=1;cases.append((w,l,zeroDL))
    for a,c in it.product(range(5),range(4)):
        d=zeroDL.copy();d[a,c]=1;cases.append((zeroW,zeroL,d))
    for w,l,d in cases:
        original=source_R(w,l,d);reduced=np.zeros_like(original)
        for c,e,r in it.product(range(4),repeat=3):
            reduced[c,e,r]=1j*sum(GD[a,c,e]*d[a,r]+GD[a,c,r]*d[a,e]+C[c,e]*sum(G[a,r,t]*d[a,t] for t in range(4))+C[c,r]*sum(G[a,e,t]*d[a,t] for t in range(4))-C[e,r]*sum(G[a,c,t]*d[a,t] for t in range(4))-GD[a,e,r]*d[a,c] for a in range(5))
            reduced[c,e,r]+=1j*(w[e,r]*l[c]-w[c,r]*l[e]-3*C[c,e]*(w@U@l)[r])
        assert np.array_equal(original,reduced),'S2-45 to S2-49'
        assert np.array_equal(reduced+reduced.transpose(1,0,2),np.zeros_like(reduced)),'same-SU anticommutator'
    for a,b,c,d in it.product(range(4),repeat=4):
        assert sum(eta[x]*GD[x,a,b]*GD[x,c,d] for x in range(5))==C[a,b]*C[c,d]-2*C[a,c]*C[b,d]+2*C[a,d]*C[b,c]
    for k in range(4):
        x=np.eye(4)[k]
        for c,d,r in it.product(range(4),repeat=3):
            original=-C[c,d]*x[r]-C[c,r]*x[d]+.75*C[d,r]*x[c]+sum(GD[a,d,r]*eta[a]*(G[a]@x)[c]/4 for a in range(5))
            reduced=-1.5*C[c,d]*x[r]-.5*C[c,r]*x[d]+.5*C[d,r]*x[c]
            assert original==reduced, 'S2-47 Weyl-spinor coefficient'
    fb=[]
    for a,b in it.combinations(range(5),2):
        f=np.zeros((5,5));f[a,b]=1;f[b,a]=-1;fb.append(f)
    for f in fb+[a+b for a,b in it.combinations(fb,2)]:
        fm=sum(f[a,b]*S[a,b]/2 for a,b in it.product(range(5),repeat=2))
        f2=sum(eta[a]*eta[b]*f[a,b]**2 for a,b in it.product(range(5),repeat=2))
        rhs=(-f2*np.eye(4)/8).astype(complex)
        for ids in it.permutations(range(5)):
            a,b,c,d,e=ids
            rhs+=cc['eps'](ids)*f[a,b]*f[c,d]*eta[e]*G[e]/16
        assert np.array_equal(fm@fm,rhs),'S2-53 Clifford square'
    return len(cases)+4

if __name__=='__main__':
    check_three_spinors();check_derivative_contractions();r_count=check_R_and_clifford()
    zF=np.zeros((5,5));zX=np.zeros((2,2));zv=np.zeros(5);zW=np.zeros((4,4),complex)
    bosonic_basis=[]
    for a,b in it.combinations(range(5),2):
        f=zF.copy();f[a,b]=1;f[b,a]=-1;bosonic_basis.append((f,zX,zv))
    for a,b in [(0,0),(0,1),(1,1)]:
        x=zX.copy();x[a,b]=x[b,a]=1;bosonic_basis.append((zF,x,zv))
    for a in range(5):
        v=zv.copy();v[a]=1;bosonic_basis.append((zF,zX,v))
    # This coefficient is quadratic in the eighteen even jets. Diagonal basis
    # values and pairwise sums exhaust its polynomial coefficients.
    probes=list(bosonic_basis)
    probes += [tuple(x+y for x,y in zip(bosonic_basis[a],bosonic_basis[b])) for a,b in it.combinations(range(18),2)]
    for f,x,v in probes:
        target={m:z for (n,m),z in expected(f,x,v)[0,0].items() if n==4}
        assert_poly_equal(p4raw(f,x,v,zW,False),target,'all two-gaugino W^-4 coefficients')
    assert_poly_equal(p4raw(zF,zX,zv,zW,True),expectedextra(zF,True),'all forty derivative-gaugino generators')
    for a,b in it.combinations(range(5),2):
        w=zF.copy();w[a,b]=1;w[b,a]=-1
        wspin=sum(w[c,d]*SD[c,d]/2 for c,d in it.product(range(5),repeat=2))
        assert_poly_equal(p4raw(zF,zX,zv,wspin,False),expectedextra(w,False),'all Weyl two-form basis coefficients')
    report={
        'status':'PASS — stated sectors only; full curved primary OPEN',
        'scope':'Independent projected W^-4 derivation, eight lambda and forty derivative-lambda exterior generators; all coefficients checked by even-jet polarization.',
        'full_primary_verified':False,
        'three_spinor_identity_components':64,
        'derivative_contractions':6,
        'polarized_three_spinor_identity':'PASS',
        'unreduced_to_reduced_third_vector_derivative_probes':r_count,
        'clifford_completeness_components':256,
        'clifford_two_form_square_polarizations':55,
        'two_gaugino_coefficient_probes':len(probes),
        'derivative_gaugino_exterior_generators':40,
        'weyl_two_form_basis_probes':10,
        'arithmetic':'Exact Gaussian dyadic coefficients, tested with ==, no coefficient fitting.',
        'pending':'W^0, W^-1, W^-2 full curved reduction, full collected-polynomial verification and component projection; W^-3 checked separately in w3_checks.json.'}
    report['input_sha256']={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [BASE/'scripts/verify_log_step2.py',Path(__file__),BASE/'STEP_02_LOG_PRIMARY.md']}
    (BASE/'sources/step2/projected_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: full W^-4 coefficient; 171 even-jet polarization probes, 40 derivative-gaugino generators, 10 Weyl basis elements. Full primary remains OPEN.')
