"""Check full-covariant substitutions without expanding their connections."""
import itertools,json,pickle,random
import numpy as np
import log_step7_supercovariant as a
import verify_log_two_fermi_canonical as v
b,q,p=a.b,a.q,a.p
F,A,P,Q,I=a.F,a.A,a.P,a.Q,a.I
oldarr=v.arr;rng=np.random.default_rng(250926);eta=v.eta;gam=v.gamma;g2=v.g2;C=v.C;eps=v.E

def prepare(name,nd):
    if (name,nd) in v.cache:return
    shape=(5,)*nd+tuple({'l':5,'s':4,'u':2}[k] for k in b.spec[name][0])+((2,) if b.spec[name][2] else ())
    z=rng.integers(-2,3,shape).astype(complex)
    if name in ('Hdual','hatF','RQ','RV'):z=z-z.swapaxes(nd,nd+1)
    if name in ('RV',):z=z+z.swapaxes(nd+2,nd+3)
    if name in ('Lc',):z=z+z.swapaxes(nd,nd+1)
    if name=='Lc' and nd==0:z=np.eye(2)*1.7/np.sqrt(2)
    if name=='rho' and nd==0:z=np.array(1.)
    if (name=='rho' and nd==1) or (name=='lam' and nd==0):z*=0
    if name=='RQ':
        rp=z.copy();gl=gam*eta[:,None,None]
        vv=np.einsum('ast,...abtij->...bsij',gam,rp)
        aa=np.einsum('abst,...abtij->...sij',g2,rp)
        ph=-1j/3*vv-1j/24*np.einsum('ast,...tij->...asij',gl,aa)
        for k,l in itertools.product(range(5),repeat=2):
            z[...,k,l,:,:,:]+=-1j*np.einsum('st,...tij->...sij',gl[k],ph[...,l,:,:,:])+1j*np.einsum('st,...tij->...sij',gl[l],ph[...,k,:,:,:])
    if name=='RMB':
        metric=np.diag(eta);mat=rng.integers(-2,3,(5,)*nd+(5,5)).astype(complex);mat=mat+mat.swapaxes(-1,-2)
        r=np.einsum('...ac,...bd->...abcd',mat,mat)-np.einsum('...ad,...bc->...abcd',mat,mat)
        ric=np.einsum('...acbc,c->...ab',r,eta);sc=np.einsum('...aa,a->...',ric,eta)
        z=r-(np.einsum('...ac,bd->...abcd',ric,metric)-np.einsum('...bc,ad->...abcd',ric,metric)-np.einsum('...ad,bc->...abcd',ric,metric)+np.einsum('...bd,ac->...abcd',ric,metric))/3
        z+=np.einsum('...,abcd->...abcd',sc,(np.einsum('ac,bd->abcd',metric,metric)-np.einsum('ad,bc->abcd',metric,metric))/12)
    v.cache[name,nd]=z

def arr(f):
    if f.name=='gc':return np.array(.41)
    if f.name=='pow':return np.array(1.)
    if f.name not in ('eps','suB','eta','del','volB','g1','g2'):prepare(f.name,len(f.ds))
    return oldarr(f)
v.arr=arr
def evaluate(pol,slot):return sum((v.evaluate(c,fs,slot) for c,fs in pol.ts),0)

def template_checks():
    for name,nd in [('rho',2),('lam',1),('hatF',0),('Hdual',0),('Lc',0),('compPhi',0),('compN',0)]:prepare(name,nd)
    G=v.cache['hatF',0];H=v.cache['Hdual',0];lc=v.cache['Lc',0];nc=v.cache['compN',0];phic=v.cache['compPhi',0];g=.41
    slash=np.einsum('ast,atij->sij',gam,v.cache['lam',1])
    dot=lambda x,y:np.einsum('ab,ab,a,b->',x,y,eta,eta)
    box=np.einsum('aa,a->',v.cache['rho',2],eta)
    expected={'aux':-g*lc/2,'ten':(G-2*H)/8,'chi':1j*slash/8+g*phic/8,
      'auxD':box/4+5*dot(G,G)/96+dot(G,H)/24-13*dot(H,H)/24+g*nc/4+g*g*np.sum(lc*((-eps)@lc@(-eps).T))/16}
    result={}
    for name,target in expected.items():
        free=a.TEMPLATES[name][1];slot='test-'+name;p.FREE[slot]={x[1:]:x[0] for x in free}
        pol=a.gauge_values(a.substitute(P(A(name,free)),2))
        delta=float(np.max(abs(evaluate(pol,slot)-target)))
        assert delta<1e-10,(name,delta)
        result[name]=delta
    return result

def product_rule_checks():
    """Independent hand expressions, including terms lost by early gauge fixing."""
    ds=('-lC','-lD');rho=A('rho',ds=ds);g=F('gc')
    # Ordered second derivative of Y.
    y=-Q(1,2)*g*A('Lc',('+uI','+uJ'),ds)+Q(1,2)*g*F('Lc','+uI','+uJ')*rho
    y+=I*Q(1,4)*(a.bil(A('lam',('-sX','+uI'),('-lD',)),A('lam',('-sY','+uJ'),('-lC',)))+a.bil(A('lam',('-sX','+uI'),('-lC',)),A('lam',('-sY','+uJ'),('-lD',))))
    t=Q(1,8)*A('hatF',('-lA','-lB'),ds)-Q(1,4)*A('Hdual',('-lA','-lB'),ds)-Q(1,8)*rho*F('hatF','-lA','-lB')+Q(1,2)*rho*F('Hdual','-lA','-lB')
    t+=I*Q(1,32)*(a.bil(A('lam',('-sX','+uI'),('-lD',)),A('lam',('-sY','-uI'),('-lC',)),('-lA','-lB'))+a.bil(A('lam',('-sX','+uI'),('-lC',)),A('lam',('-sY','-uI'),('-lD',)),('-lA','-lB')))
    c=I*Q(1,8)*F('g1','+lA','-sE','+sX')*A('lam',('-sX','+uI'),('-lC','-lA'))
    c+=-Q(1,16)*F('Hdual','-lA','-lB')*F('g2','+lA','+lB','-sE','+sX')*A('lam',('-sX','+uI'),('-lC',))
    c+=-Q(1,16)*g*F('Lc','+uI','+uJ')*A('lam',('-sE','-uJ'),('-lC',))+Q(1,8)*g*A('compPhi',('-sE','+uI'),('-lC',))
    d=Q(1,4)*A('rho',ds=('-lC','+lA','-lA'))
    d+=Q(5,48)*F('hatF','+lA','+lB')*A('hatF',('-lA','-lB'),('-lC',))
    d+=Q(1,24)*(F('Hdual','+lA','+lB')*A('hatF',('-lA','-lB'),('-lC',))+F('hatF','+lA','+lB')*A('Hdual',('-lA','-lB'),('-lC',)))
    d+=-Q(13,12)*F('Hdual','+lA','+lB')*A('Hdual',('-lA','-lB'),('-lC',))+Q(1,4)*g*A('compN',ds=('-lC',))+Q(1,8)*g*g*F('Lc','-uI','-uJ')*A('Lc',('+uI','+uJ'),('-lC',))
    d+=Q(3,8)*a.bil(A('lam',('-sX','+uI'),('-lC',)),A('lam',('-sY','-uI'),('-lA',)),('+lA',))-I*Q(1,2)*g*a.bil(A('lam',('-sX','+uI'),('-lC',)),F('compPhi','-sY','-uI'))
    expected={'DDY':(A('aux',('+uI','+uJ'),ds),y),'DDT':(A('ten',('-lA','-lB'),ds),t),'Dchi':(A('chi',('-sE','+uI'),('-lC',)),c),'DDscalar':(A('auxD',ds=('-lC',)),d)}
    report={}
    for name,(atom,hand) in expected.items():
        slot='hand-'+name;p.FREE[slot]=a.h.free_indices(hand)
        got=a.gauge_values(a.substitute(P(atom),2))
        diff=a.canonical(got-hand,slot)[0]
        assert not diff.ts,(name,len(diff.ts))
        report[name]='exact zero coefficient residual'
    return report

def samples():
    report={};sel=random.Random(250926)
    for slot in ('L','phi','N','E'):
        raw=pickle.load((a.OUT/(slot+'-substituted.pkl')).open('rb'))
        ids=sorted(set(list(range(min(3,len(raw.ts))))+sel.sample(range(len(raw.ts)),min(24,len(raw.ts)))))
        worst=0
        for j in ids:
            c,fs=raw.ts[j];before=v.evaluate(c,fs,slot)
            final=a.canonical(P.terms([(c,fs)]),slot,'-sample')[0]
            delta=float(np.max(abs(before-evaluate(final,slot))))/max(1.,float(np.max(abs(before))))
            assert delta<1e-8,(slot,j,delta)
            worst=max(worst,delta)
        report[slot]={'sampled_terms':len(ids),'max_relative_residual':worst}
        print('PASS arrays',slot,report[slot],flush=True)
    pol=pickle.load((a.OUT/'L-canonical.pkl').open('rb'))
    def ix(x):return x[0]+{'uI':'uJ','uJ':'uI'}.get(x[1:],x[1:])
    swapped=P.terms([(c,tuple(b.replace(f,ix=tuple(ix(x) for x in f.ix),ds=tuple(ix(x) for x in f.ds)) for f in fs)) for c,fs in pol.ts])
    assert not q.collect_tensor(pol-swapped,'L')[0].ts
    return report

if __name__=='__main__':
    result={'composite_formula_array_residuals':template_checks(),'hand_product_rule_checks':product_rule_checks(),'sampled_canonical_algebra':samples(),'triplet_symmetry':'exact zero coefficient residual'}
    (a.OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
