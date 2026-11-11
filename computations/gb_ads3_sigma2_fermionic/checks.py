"""Read-only verification of item 25; --write-log writes only package reports.

Numerical checks use scaled max-entry residuals with tolerance 2e-10 unless
specified otherwise. They verify evaluated component identities and samples,
not universal parameter identities, a spectrum census, or nonlinear SUSY.
"""
import argparse
import hashlib
import importlib.util
import json
import platform
import time
import numpy as np
import sympy as sp
import symengine as se
from action import evaluate, gauge_columns, pack, unpack, lr_polynomial, SECTORS, exact
from background import background
from sources import HERE, ROOT, ACTION, census, terms
from derive import SAMPLES, DPOINT, OUT
from ferm2 import bl, ein, GUP, GL, DL, NW, ETAI, I, s2
import action2
import bderiv2
import eval2
from check_derivatives import run as derivative_checks

RECORDS = []
MESSAGES = []


def check(name, actual, expected=0, tol=2e-10):
    a, b = np.asarray(actual, complex), np.asarray(expected, complex)
    error = float(np.max(np.abs(a-b)))
    scale = max(1., float(np.max(np.abs(a))), float(np.max(np.abs(b))))
    record = dict(check=name, method='numerical', absolute_error=error,
                  scale=scale, scaled_error=error/scale, tolerance=tol)
    RECORDS.append(record)
    if not np.isfinite(error) or error/scale > tol:
        raise AssertionError(record)


def exact_check(name, condition):
    if not condition:
        raise AssertionError(name)
    RECORDS.append(dict(check=name, method='exact', passed=True))


def ok(message):
    MESSAGES.append('PASS '+message)
    print(MESSAGES[-1], flush=True)


def source_checks():
    manifest = json.loads((HERE/'source_manifest.json').read_text())
    for path, sha in manifest['repository_inputs'].items():
        exact_check('source hash '+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha)
    for path, sha in manifest['implementation_hashes'].items():
        exact_check('implementation hash '+path, hashlib.sha256((HERE/path).read_bytes()).hexdigest() == sha)
    current = census()
    exact_check('current source census vs stored record', current == json.loads((OUT/'source_terms.json').read_text()))
    from evalbg import expand_terms
    exact_check('1184 source terms', len(terms()) == 1184)
    exact_check('1190 distributed terms', len(expand_terms(terms())) == 1190)
    exact_check('1198 terms after Leibniz', sum(x['expanded_terms'] for x in current) == 1198)
    exact_check('871 explicit + 2 differentiated + 325 implicit terms',
                [sum(x[k] for x in current) for k in ('explicit_bilinears','differentiated_bilinears','implicit_bilinears')] == [871,2,325])
    ok('source fingerprints; complete 1184 -> 1190 -> 1198 term census')


def exact_checks():
    from clifford import _checks, J, SIGMA01, GU, CC
    _checks()
    exact_check('Clifford/Majorana identities and Jpaper=-i Jsource', (-sp.I*J)**2 == sp.eye(2))
    mult = SIGMA01.eigenvals()
    for n, charge in SECTORS:
        dim = sum(mult.get(n-w,0) for w in (1,-1,0,0,0))+mult.get(n,0)
        exact_check(f'sector dimension {n},{charge}', dim == (10 if abs(n)==sp.Rational(1,2) else 2))
    # Independent comparison with the already accepted item-24 formulas.
    path = ROOT/'computations/gb_ads3_sigma2/model.py'
    spec = importlib.util.spec_from_file_location('item23_background_check', path)
    model = importlib.util.module_from_spec(spec); spec.loader.exec_module(model)
    L,k,g = model.L, model.k, model.g
    for chi in (1,-1):
        got = background(L,k,g,chi)
        for name,want in model.branch(chi).items():
            exact_check(f'BPS background {name}, chi={chi}', sp.cancel(got[name]-want)==0)
    # Bilinear Grassmann derivative in an independent 2-generator exterior
    # algebra: coefficient of b a is X_B^T M Y_A - Y_B^T M^T X_A.
    from fengine import Sp, bil
    rng = np.random.default_rng(24)
    a,b,c,d = [rng.integers(-3,4,(2,4,1)).astype(object) for _ in range(4)]
    X,Y = Sp(a,b),Sp(c,d)
    P=sp.Matrix([[0,-1],[1,0]]); M=GU[0]*GU[3]
    direct=0
    for i in range(2):
        for j in range(2):
            for u in range(4):
                for v in range(4):
                    direct += P[i,j]*(CC*M)[u,v]*(b[i,u,0]*c[j,v,0]-a[i,u,0]*d[j,v,0])
    exact_check('independent two-generator Grassmann bilinear',sp.expand(sp.sympify(str(bil(X,M,Y,P)[0,0]))-direct)==0)
    ok('exact background, Clifford, sector bases and Grassmann signs')


def diagonal(result, label):
    c, ph = result['context'], result['engine'].o['varphi']
    lam = result['lambda_GB']
    coefficient = 2*(1/c.L+lam*c.g**2)
    P = (c.p-2*c.h)/c.L+2*lam*c.g**2*(c.p-3*c.h)
    M = s2*(2*c.g-c.N/c.L**2)+7*lam*c.g**3*c.L/s2
    predicted = coefficient*bl(ph,'',c.nab(ph),'a',G=GUP[1],gf='a')
    predicted += I*P*bl(ph,'',ph,'',G=GL[2][3,4])+I*M*bl(ph,'',ph,'',P=DL)
    ai=[i for i,x in enumerate(result['a']) if x[0]=='phi']
    bi=[i for i,x in enumerate(result['b']) if x[0]=='phi']
    if ai:
        check(label+' FQ.26 diagonal',result['K'][np.ix_(bi,ai)],predicted[np.ix_(bi,ai)])


def A1_check(r):
    c,o,e = r['context'],r['engine'].o,r['engine'].e
    psi,ph,chi,vphi,Dphi=o['psi'],o['phi_mu'],o['chi'],o['varphi'],o['Dvarphi']
    L,N,g=c.L,c.N,c.g
    up=lambda X:X.ap(lambda a:np.einsum('ab,b...->a...',ETAI,a))
    gX=8*c.gT
    A1=6*L*np.einsum('cdmn,cd->mn',e['f'],ETAI)
    A1+=-I/s2*bl(up(psi),'a',Dphi,'a',P=DL)-6*L*bl(psi,'a',chi,'',G=GUP[1],gf='a')
    A1+=-bl(vphi,'',psi,'a',G=np.einsum('st,atu->asu',gX,GUP[1]),gf='a',P=DL)/(8*s2)+bl(vphi,'',ph,'a',G=GUP[1],gf='a',P=DL)/s2
    Xup=np.einsum('ab,ax,by->xy',8*c.T,ETAI,ETAI)
    A1+=L/12*np.einsum('abmn,ab->mn',8*e['T'],Xup)+4*L*e['D']
    A1+=-I*s2*N/L**2*bl(vphi,'',vphi,'',P=DL)+I/(4*L)*bl(vphi,'',vphi,'',G=gX,P=NW)
    A1+=bl(vphi,'',Dphi,'a',G=GUP[1],gf='a',P=NW)/L
    check('LR A1: independent torsion-retaining construction',A1,r['lr_parts']['A1'])


def gauge_check(r, label):
    G, projection=gauge_columns(r)
    check(label+' SUSY basis projection',projection,0)
    denominator=max(np.linalg.norm(r['K'])*np.linalg.norm(G),1e-300)
    check(label+' K G_epsilon',r['K']@G/denominator,0)
    return G


def sample_checks():
    traced = False
    for label,L,k,S in SAMPLES:
        saved=json.loads((OUT/(label+'.json')).read_text())
        exact_check(label+' eight sectors',len(saved['sectors'])==8)
        for (n,q),old in zip(SECTORS,saved['sectors']):
            exact_check(label+' sector labels',old['n']==str(n) and old['q_R']==q)
            trace = label==SAMPLES[0][0] and n==sp.Rational(1,2) and q==1
            r=evaluate(L,k,'1',n,q,DPOINT,S,trace=trace)
            for key in ('LR','W','LOG','K'):
                check(f'{label}/{n}/{q}/{key} stored matrix',r[key],unpack(old['matrices'][key]))
            diagonal(r,f'{label}/{n}/{q}')
            if abs(n)==sp.Rational(1,2):
                G=gauge_check(r,f'{label}/{n}/{q}')
                check(label+' stored SUSY columns',G,unpack(old['gauge_columns']))
            if trace:
                traced = True
                record=json.loads((OUT/'term_contributions.json').read_text())
                exact_check('1184 source contribution records',len(record['terms'])==1184)
                exact_check('1184 evaluated source contributions',len(r['engine'].source_terms)==1184)
                total=np.zeros_like(r['K'])
                for fresh, oldterm in zip(r['engine'].source_terms,record['terms']):
                    previous=np.zeros_like(fresh)
                    for i,j,re,im in oldterm['entries']:previous[i,j]=re+1j*im
                    check(oldterm['id']+' stored contribution',fresh,previous)
                    total+=fresh
                check('all source contributions sum to W+LOG',total,r['W']+r['LOG'])
        ok(label+': all eight raw matrices, diagonal and SUSY residuals')
    exact_check('source contribution trace was verified',traced)


def consistency_checks():
    specs=[('3','2','1','29/100-7*I/100'),('5','-1','3/2','3'),('7/2','1','1','1/2+13*I/10')]
    for L,k,g,S in specs:
        r=evaluate(L,k,g,'1/2',1,DPOINT,S)
        derivative_checks(r,lambda name,a,b=0:check(f'{L},{k},{g}: {name}',a,b))
        A1_check(r);diagonal(r,'independent '+str((L,k,g)));gauge_check(r,'independent '+str((L,k,g)))
        dual=evaluate(L,k,g,'-1/2',-1,2-DPOINT,str(1-exact(S)))
        check('Majorana transpose / integration by parts '+L,dual['K'],-r['K'].T)
        ok(f'full derivative identities and Majorana pairing: L={L}, k={k}, g={g}')
    r=evaluate('3','2','1','1/2',1,DPOINT,'1/3')
    rg=evaluate('3','2','3/2','1/2',1,DPOINT,'1/3')
    for key,power in [('LR',1),('W',3),('LOG',3),('K',1)]:
        check('independent g rescaling '+key,rg[key],r[key]*(1.5**power))
    ok('dimensionful g variation: LR and total scale as g; raw GB as g^3')


def lr_checks():
    bg={x:sp.Symbol(x,nonzero=True) for x in 'l w g L N p h r'.split()}
    K,a,b,parts=action2.K2(bg,sp.Rational(1,2),1,sp.Symbol('D'),sp.Symbol('S'),parts=True)
    exact_check('full LR F block: symbolic free-background identity',all(se.expand(x)==0 for x in parts['A4'].flat))
    exact_check('ordinary-derivative F block negative control',any(se.expand(x)!=0 for x in (parts['A4']-parts['A4f']).flat))
    for L,S in [('3','1/3'),('5','3')]:
        r=evaluate(L,'0','1','1/2',1,DPOINT,S)
        gauge_check(r,'two-derivative k=0 '+L)
        check('k=0 total equals LR '+L,r['K'],r['LR'])
    for n in (sp.Rational(1,2),sp.Rational(3,2)):
        K,a,b,parts=action2.K2(background(4,0,1),n,1,sp.Symbol('D'),0,parts=True)
        exact_check('k=0 constant T2 F block '+str(n),all(se.expand(x)==0 for x in parts['A4'].flat))
    ok('exact free-background LR F block and k=0 checks (including constant T2 LR only)')


def negative_controls():
    args=('3','2','1','1/2',1,DPOINT,'29/100-7*I/100')
    good=evaluate(*args);G=gauge_check(good,'negative-control baseline')
    def fails(name,K):
        error=float(np.linalg.norm(K@G)/(np.linalg.norm(K)*np.linalg.norm(G)))
        RECORDS.append(dict(check=name,method='negative control',gauge_residual=error,required_minimum=1e-7))
        if not np.isfinite(error) or error<=1e-7:raise AssertionError((name,error))
    fails('fermionic GB rescaled by 1.05',good['LR']+1.05*good['lambda_GB']*(good['W']+good['LOG']))
    for name,module,attr,value in [('old H02 G sign',bderiv2,'H02_G_SIGN',-1.),
                                   ('omitted gauged H02 varphi',bderiv2,'H02_GAUGED_FACTOR',0.),
                                   ('ordinary derivative in source term 17',eval2,'LEGACY_NABLA',True)]:
        old=getattr(module,attr)
        try:
            setattr(module,attr,value);bad=evaluate(*args)
        finally:setattr(module,attr,old)
        fails(name,bad['K'])
    ok('four negative controls detect incorrect rules / relative normalization')


def interpolation_check():
    # Reproduce the manuscript's numerical polynomial method without solving
    # for roots. Two resolutions and independent off-grid points are compared.
    args=('3','2','1','1/2',1)
    coeff=[]
    for count in (6,10):
        grid=1+1.6*np.exp(2j*np.pi*(np.arange(count)+.3)/count)
        values=np.array([evaluate(*args,D,'1/3')['K'] for D in grid])
        C=np.linalg.solve(np.vander(grid,count,increasing=True),values.reshape(count,-1)).reshape(count,10,10)
        coeff.append(C)
    C6,C10=coeff
    check('D interpolation: 6 vs 10 nodes',C10,np.concatenate([C6,np.zeros((4,10,10),complex)]),tol=2e-8)
    for D in (1+.9*np.exp(.77j),1+2.3*np.exp(2.1j)):
        direct=evaluate(*args,D,'1/3')['K']
        check('D interpolation off-grid '+str(D),sum(C*D**j for j,C in enumerate(C10)),direct,tol=2e-8)
    ok('numerical D polynomial: two resolutions and two independent holdouts')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write-log',action='store_true')
    args=ap.parse_args();start=time.monotonic()
    source_checks();exact_checks();lr_checks();consistency_checks();negative_controls();interpolation_check();sample_checks()
    elapsed=time.monotonic()-start
    ok(f'item 25 complete: {len(RECORDS)} checks, {elapsed:.1f}s; item 26 not evaluated')
    if args.write_log:
        report=dict(scope='item 25 only; finite numerical GB evaluations, exact checks separately labelled',
                    versions=dict(python=platform.python_version(),numpy=np.__version__,sympy=sp.__version__,symengine=se.__version__),
                    elapsed_seconds=elapsed,checks=RECORDS,messages=MESSAGES)
        (OUT/'verification.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        (OUT/'verification.log').write_text('\n'.join(MESSAGES)+'\n')


if __name__=='__main__':main()
