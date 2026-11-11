#!/usr/bin/env python3
"""Exact checks of the definition-derived W^-3 sector.

The raw side is the projected product rule and the displayed descendant
reductions. The comparison side is S23 (3.25) with its gradient-X sign
explicitly corrected. The published disagreement is tested, never hidden.
Independent six-derivative flat checks of that sign are in the companion file.
"""
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'verify_log_step2_projected.py'));globals().update({k:v for k,v in ns.items() if not k.startswith('__')})
# All odd source components retained independently.
y=[[{1<<(48+2*a+i):1} for i in range(2)] for a in range(4)]
yu=[[add(*[scale(U[a,b],y[b][i]) for b in range(4)]) for i in range(2)] for a in range(4)]
w3={}
for n,ids in enumerate(it.combinations_with_replacement(range(4),3)):
 for perm in set(it.permutations(ids)):
  for i in range(2):w3[(*perm,i)]={1<<(56+2*n+i):1}
zero=lambda:np.zeros((5,5))
def inputs():
 return dict(F=zero(),X=np.zeros((2,2)),v=np.zeros(5),W=zero(),dx=np.zeros((5,2,2)),df=np.zeros((5,5,5)),h=zero(),der=False,wy=False,ww=False)
def pol(x):return x if isinstance(x,dict) else ({0:x} if x else {})
def rawparts(F,X,v,W,dx,df,h,der=False,wy=False,ww=False,detail=False):
 Wsp=sum(W[a,b]*SD[a,b]/2 for a,b in it.product(range(5),repeat=2));Wm=-Wsp@U
 Fsp=sum(F[a,b]*SD[a,b]/2 for a,b in it.product(range(5),repeat=2));vsp=sum(v[a]*GD[a] for a in range(5));Q=-2*Fsp-C*X[0,1]-vsp
 yy=[[y[a][i] if wy else {} for i in range(2)] for a in range(4)]
 yu0=[[yu[a][i] if wy else {} for i in range(2)] for a in range(4)]
 www={key:value if ww else {} for key,value in w3.items()}
 R=Rplus(Wsp,der)
 RW={(c,d,r):add(scale(-1.5*C[c,d],yy[r][0]),scale(-.5*C[c,r],yy[d][0]),scale(.5*C[d,r],yy[c][0])) for c,d,r in it.product(range(4),repeat=3)}
 # D+ nabla_beta{}^rho lambda_rho^- at explicit scalar W^0.
 d2x={};TP={};DDpieces={}
 for a,b in it.product(range(4),repeat=2):
  ordinary=[]
  for m,r in it.product(range(5),range(4)):
   dQ=add(*[scale(-SD[c,d,a,r],pol(df[m,c,d])) for c,d in it.product(range(5),repeat=2)],{0:-C[a,r]*dx[m,0,1]},*[scale(-GD[n,a,r],pol(h[m,n])) for n in range(5)])
   ordinary.append(scale(G[m,b,r],dQ))
   ordinary.append({0:-2*G[m,b,r]*Wsp[a,r]*v[m]})
  tc=sum(G[m,b,r]*((3*eta[m]*G[m]@Wm-Wm@(eta[m]*G[m]))/4@Q)[a,r] for m,r in it.product(range(5),range(4)))
  mc=add(*[scale(.5,prod(www[a,b,t,0],lu[t][1])) for t in range(4)],*[scale(.5*C[a,b],prod(yu0[t][0],ll[t][1])) for t in range(4)],scale(-.25,prod(yy[a][0],ll[b][1])),scale(.5,prod(yy[b][0],ll[a][1])),scale(.75,prod(yy[a][1],ll[b][0])),*[scale(-1.5*C[a,b],prod(yu0[t][1],ll[t][0])) for t in range(4)],scale(-1.5,prod(yy[b][1],ll[a][0])))
  dwl=add(*[prod(add(www[b,r,a,0],scale(.5*C[a,b],yy[r][0]),scale(.5*C[a,r],yy[b][0])),lu[r][1]) for r in range(4)])
  DDpieces[a,b]=[scale(2j,add(*ordinary)),{0:2j*tc},scale(2j,mc),scale(-1j,dwl),{0:-1j*sum(Wsp[b,r]*U[r,s]*Q[a,s] for r,s in it.product(range(4),repeat=2))},scale(1.5j,prod(yy[b][1],ll[a][0]))]
  d2x[a,b]=add(*DDpieces[a,b])
  TP[a,b]=add({0:4j*sum(GD[m,a,b]*dx[m,0,0] for m in range(5))-8j*Wsp[a,b]*X[0,0]},*[scale(-8j,prod(www[a,b,t,0],lu[t][0])) for t in range(4)],*[scale(1j*C[a,b],prod(yu0[t][0],ll[t][0])) for t in range(4)],scale(2j,prod(yy[a][0],ll[b][0])),scale(-2j,prod(yy[b][0],ll[a][0])))
 parts=[{0:-.25*X[0,0]**2*X[1,1]}]
 parts.append(add(*[scale(.5j*X[0,0],prod(lu[r][0],add(*([scale(G[m,r,t],dl[m][t][1]) for m,t in it.product(range(5),range(4))] if der else []),*[scale(-.5*Wsp[r,t],lu[t][1]) for t in range(4)]))) for r in range(4)]))
 parts.append(add(*[scale(-eps4(a,b,c,d)/16,prod(ll[a][0],ll[b][0],d2x[c,d])) for a,b,c,d in it.product(range(4),repeat=4)]))
 parts.append(add(*[scale(-9j/16,prod(bil(0,0),lu[a][0],yy[a][1])) for a in range(4)]))
 parts.append(add(*[scale(.75j*X[0,0]*Wsp[a,b],prod(lu[a][0],lu[b][1])) for a,b in it.product(range(4),repeat=2)]))
 p6=[];p7=[];p8=[];p9=[]
 for a,b,c,d in it.product(range(4),repeat=4):
  e=eps4(a,b,c,d)
  if not e:continue
  dd0=add(*[scale(-2,prod(R[c,d,r],lu[r][1])) for r in range(4)],{0:-2*sum(Q[d,r]*U[r,s]*Q[c,s] for r,s in it.product(range(4),repeat=2))})
  dd1=add(*[scale(-2,prod(RW[c,d,r],lu[r][1])) for r in range(4)],{0:4*sum(Wsp[d,r]*U[r,s]*Q[c,s]+Q[d,r]*U[r,s]*Wsp[c,s] for r,s in it.product(range(4),repeat=2))})
  p6.append(scale(-X[0,0]*e*C[a,b]/64,dd0))
  p7.append(scale(-3j*e/64,prod(ll[a][0],ll[b][0],dd1)))
  p9.extend([scale(e*U[r,s]*Q[d,s]/16,prod(ll[a][0],R[b,c,r])) for r,s in it.product(range(4),repeat=2)])
 for a,r in it.product(range(4),repeat=2):p8.append(scale(-1/16,prod(lu[a][0],TP[a,r],lu[r][1])))
 parts.extend([add(*p6),add(*p7),add(*p8),add(*p9)])
 if detail:return [add(*[scale(-eps4(a,b,c,d)/16,prod(ll[a][0],ll[b][0],DDpieces[c,d][n])) for a,b,c,d in it.product(range(4),repeat=4)]) for n in range(6)]
 return parts

def target(F,X,v,W,dx,df,h,der=False,wy=False,ww=False,published=False):
 P=scale(X[0,0]*(sum(eta[a]*eta[b]*F[a,b]**2 for a,b in it.product(range(5),repeat=2))-sum(X[a,b]*(E.T@X@E)[a,b] for a,b in it.product(range(2),repeat=2))-2*sum(eta[a]*v[a]**2 for a in range(5)))/8,{0:1})
 terms=[P]
 if der:
  for a,b,al,be in it.product(range(5),range(5),range(4),range(4)):
   terms.append(scale(-.25j*GU[a,al,be]*F[a,b]*eta[b],prod(ll[al][0],dl[b][be][0])))
   terms.append(scale(-.5j*SU[a,b,al,be]*v[a],prod(ll[al][0],dl[b][be][0])))
  for a,al,be,k in it.product(range(5),range(4),range(4),range(2)):
   terms.append(scale(.25j*GU[a,al,be]*X[0,0],prod(ll[al][k],dld[a][be][k])))
   terms.append(scale(.25j*GU[a,al,be]*X[k,0],prod(ll[al][0],dld[a][be][k])))
  for a,al in it.product(range(5),range(4)):terms.append(scale(.75j*eta[a]*v[a],prod(lu[al][0],dl[a][al][0])))
  for a,b,c,d,e in it.permutations(range(5)):
   for al,be in it.product(range(4),repeat=2):terms.append(scale(1j/8*cc['eps']((a,b,c,d,e))*eta[a]*eta[b]*SU[a,b,al,be]*F[d,e],prod(ll[al][0],dl[c][be][0])))
 for a,al,be,k in it.product(range(5),range(4),range(4),range(2)):
  terms.append(scale((-.25j if published else .25j)*GU[a,al,be]*dx[a,0,k],prod(ll[al][0],ld[be][k])))
 for a,c,al,be in it.product(range(5),range(5),range(4),range(4)):
  terms.append(scale(-.25j*GU[a,al,be]*eta[c],prod(ll[al][0],ll[be][0],pol(df[c,a,c]))))
 for a in range(5):terms.append(scale(.25j*eta[a],prod(bil(0,0),pol(h[a,a]))))
 for a,b,al,be in it.product(range(5),range(5),range(4),range(4)):
  terms.append(scale(-3j/16*GU[a,al,be]*W[a,b]*eta[b]*v[b],prod(ll[al][0],ll[be][0])))
  for k in range(2):terms.append(scale(-3j/32*SU[a,b,al,be]*X[0,0]*W[a,b],prod(ll[al][k],ld[be][k])))
 terms.append(scale(3j/32*sum(eta[a]*eta[b]*W[a,b]*F[a,b] for a,b in it.product(range(5),repeat=2)),bil(0,0)))
 for a,b,c,d,e in it.permutations(range(5)):
  for al,be in it.product(range(4),repeat=2):terms.append(scale(-9j/64*cc['eps']((a,b,c,d,e))*eta[a]*GU[a,al,be]*W[b,c]*F[d,e],prod(ll[al][0],ll[be][0])))
 if wy:
  for a,b,k in it.product(range(4),range(4),range(2)):
   terms.append(scale(-3j/8,prod(yu[a][k],ll[a][0],lu[b][0],ld[b][k])))
   terms.append(scale(-3j/8,prod(yu[a][k],lu[b][0],ll[b][0],ld[a][k])))
 return add(*terms)

def check_mixed_lorentz_action():
    """C24 A.3d curvature acting on lambda: all symmetric W3 and X components."""
    count=0
    for kind in ['W3','X']:
        choices=list(it.combinations_with_replacement(range(4),3)) if kind=='W3' else [(k,) for k in range(4)]
        for ids in choices:
            w=np.zeros((4,4,4));x=np.zeros(4)
            if kind=='W3':
                for perm in set(it.permutations(ids)):w[perm]=1
            else:x[ids[0]]=1
            wab=np.einsum('abrs,rsq->abq',SU,w)
            original=np.zeros((4,4,4),complex)
            for b,al,c,d in it.product(range(5),range(4),range(5),range(5)):
                r=-sum(eta[b]*G[b,al,t]*wab[c,d,t] for t in range(4))
                r+=sum(eta[b]*cc['eps']((b,c,d,e,f))*eta[e]*eta[f]*wab[e,f,al]/4 for e,f in it.product(range(5),repeat=2) if len({b,c,d,e,f})==5)
                r+=sum((int(b==c)*G[d,al,t]-int(b==d)*G[c,al,t])*x[t]/4 for t in range(4))
                original[al]+=r*eta[c]*eta[d]*(G[b]@S[c,d])/2
            reduced=.5*np.einsum('art,ts->ars',w,U)-np.einsum('ar,t->art',C,U@x)+.5*np.einsum('a,rt->art',x,np.eye(4))-np.einsum('r,at->art',x,np.eye(4))
            assert np.array_equal(original,reduced),'C24 A.3d mixed Lorentz generator'
            count+=1
    return count

if __name__=='__main__':
    mixed_count=check_mixed_lorentz_action()
    # Entire exterior polynomials are compared, not commuting-spinor samples.
    eb=[]
    for a,b in it.combinations(range(5),2):
        p=inputs();p['F'][a,b]=1;p['F'][b,a]=-1;eb.append(p)
    for i,j in [(0,0),(0,1),(1,1)]:
        p=inputs();p['X'][i,j]=p['X'][j,i]=1;eb.append(p)
    for a in range(5):
        p=inputs();p['v'][a]=1;eb.append(p)
    bos_count=0
    for ids in it.combinations_with_replacement(range(18),3):
        F=sum(eb[k]['F'] for k in ids);X=sum(eb[k]['X'] for k in ids);v=sum(eb[k]['v'] for k in ids)
        fs=sum(F[a,b]*SD[a,b]/2 for a,b in it.product(range(5),repeat=2));Q=-2*fs-C*X[0,1]-sum(v[a]*GD[a] for a in range(5))
        direct=-X[0,0]**2*X[1,1]/4+sum(X[0,0]*eps4(a,b,c,d)*C[a,b]*Q[d,r]*U[r,s]*Q[c,s]/32 for a,b,c,d,r,s in it.product(range(4),repeat=6) if eps4(a,b,c,d)*C[a,b]*U[r,s])
        lowered=E.T@X@E
        comparison=X[0,0]*(sum(eta[a]*eta[b]*F[a,b]**2 for a,b in it.product(range(5),repeat=2))-sum(X[i,j]*lowered[i,j] for i,j in it.product(range(2),repeat=2))-2*sum(eta[a]*v[a]**2 for a in range(5)))/8
        assert direct==comparison,'all cubic even-jet coefficients'
        bos_count+=1
    checks={}
    for n,p in enumerate(eb):
        p=dict(p,der=True)
        assert_poly_equal(add(*rawparts(**p)),target(**p),'F/X/dW times derivative-gaugino '+str(n))
    checks['derivative_gaugino_even_basis_probes']=len(eb)
    count=0
    for a,b in it.combinations(range(5),2):
        for base in eb:
            p=dict(base);p['W']=zero();p['W'][a,b]=1;p['W'][b,a]=-1
            assert_poly_equal(add(*rawparts(**p)),target(**p),'Weyl two-form times F/X/dW')
            count+=1
    checks['weyl_two_form_mixed_probes']=count
    for m in range(5):
        for a,b in it.combinations(range(5),2):
            p=inputs();p['df'][m,a,b]=1;p['df'][m,b,a]=-1
            assert_poly_equal(add(*rawparts(**p)),target(**p),'all uncontracted dF components')
    checks['field_strength_derivative_probes']=50
    for a,b in it.product(range(5),repeat=2):
        p=inputs();p['h'][a,b]=1
        assert_poly_equal(add(*rawparts(**p)),target(**p),'ordered Hessian, no commuting assumption')
    checks['ordered_scalar_hessian_probes']=25
    printed_failures=0
    for a in range(5):
        for i,j in [(0,0),(0,1),(1,1)]:
            p=inputs();p['dx'][a,i,j]=p['dx'][a,j,i]=1
            actual=add(*rawparts(**p));assert_poly_equal(actual,target(**p),'all dX components')
            if add(actual,scale(-1,target(**p,published=True))):printed_failures+=1
    assert printed_failures==10
    checks['auxiliary_derivative_probes']=15
    for label,key in [('Weyl spinor','wy'),('Weyl three-spinor','ww')]:
        p=inputs();p[key]=True
        assert_poly_equal(add(*rawparts(**p)),target(**p),label+' complete exterior coefficient test')
    checks['weyl_spinor_independent_odd_generators']=8
    checks['weyl_three_spinor_independent_odd_generators']=40
    report={'status':'PASS: definition-derived W^-3; published gradient-X sign discrepancy', 'full_primary_verified':False, 'pole':3, 'written_terms':18, 'source_agreement':{'matching_terms':17,'gradient_X':'definition +i/4; S23(3.25) -i/4; original six-derivative check in companion report'}, 'commutator_source_basis_probes':mixed_count, 'cubic_even_jet_simplex_probes':bos_count, 'arithmetic':'Exact Gaussian dyadic coefficients, equality by ==; full exterior polynomials, no coefficient fitting', 'checks':checks, 'published_gradient_X_nonzero_failures':printed_failures, 'pending':'W^0, W^-1, W^-2, complete primary S/K/linearity/reality and component projection'}
    report['input_sha256']={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),BASE/'STEP_02_LOG_PRIMARY.md',HERE/'verify_log_step2_projected.py']}
    (BASE/'sources/step2/w3_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: all W^-3 channels; 17 printed terms agree, gradient-X sign is +i/4 from the definition. Full primary remains open.')
