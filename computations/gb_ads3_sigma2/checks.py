"""Read-only scientific verification of citation-map item 24.

--write-log writes only outputs/verification.log. --norms additionally repeats
the labelled finite-parameter norm checks; the symbolic checks do not sample.
"""
import argparse
import hashlib
import json
import time
import sympy as s
import symengine as se
from model import *
from closed_forms import *
from derive import (OUT,SECTORS,VECTOR_CHART,SCALAR_CHART,SCALAR_INDICES,
                   subrecord,certify_blocks,real_charged_basis)
from physical import certificate
from polynomial_matrix import rational,primitive_in_D,ONE
from norms import unpack_polynomial,unpack_fraction,parsed
from harmonics import restrict

MESSAGES=[]
def ok(text):MESSAGES.append('PASS '+text);print(MESSAGES[-1],flush=True)
def same(A,B):
    assert A.shape==B.shape
    assert all(s.cancel(x-y)==0 for x,y in zip(A,B))
def record(name):return json.loads((OUT/(name+'.json')).read_text())
def packed(p):
    from flint import fmpq
    from polynomial_matrix import CTX
    value=CTX.constant(fmpq(p['coefficient']))
    for text,power in p['factors']:value*=parsed(text)**power
    return value
def primitive(expr):return primitive_in_D(rational(expr).num)
def proof_matches(fresh,old):
    for key in ('rank','physical_divisor','gauge_right','gauge_left','probes','propagator'):
        if key in fresh:assert fresh[key]==old[key],key

def source_checks():
    from sectors import sector
    bg={name:se.Symbol(name) for name in 'L N p h r l w g lam'.split()}
    lam=bg['lam'];count=0
    for n,z in SECTORS:
        def calc(model='GB',fs=False,alpha=0,beta=0):
            return sector(bg,n,se.Symbol('D'),se.Symbol('S'),charged=z,model=model,fs=fs,alpha=alpha,beta=beta,verbose=False)
        raw=calc();K=s.Matrix(raw['K']);stored,rec=load_raw(n,z);same(K,stored)
        fs=calc(fs=True);KF=s.Matrix(fs['K']);saved,_=load_raw(n,z,True);same(KF,saved)
        W=calc('WLOG',alpha=lam);SW=calc('source_W',alpha=lam)
        Q=calc('WLOG',beta=2*lam);SQ=calc('source_LOG',beta=2*lam)
        combined=calc('WLOG',alpha=lam,beta=2*lam)
        for a,b in ((W,SW),(Q,SQ),(raw,combined)):
            assert all(se.expand(x-y)==0 for x,y in zip(sum(a['K'],[]),sum(b['K'],[])))
        # B = B' + C_bg wedge c / 2, in the same component order.
        def transform(names):
            T=s.eye(len(names))
            for i,name in enumerate(names):
                prefix,field,comp=name.split('_')
                if field!='B' or '3' not in comp:continue
                other=comp.replace('3','')
                target=prefix+'_C_'+other
                if target in names:T[i,names.index(target)]=(1 if comp=='34' else -1)*s.Symbol('p')/(2*w)
            return T
        same(KF,transform(rec['bvars']).T*K*transform(rec['avars']))
        count+=K.rows*K.cols
        ok(f'source W, source LOG, GB=W+2LOG, potential/field-strength congruence: n={n}, charged={z}')
    assert count==662
    ok('662 entries compared with free off-shell background parameters')

def branch_checks():
    B=branch()
    assert s.cancel(1/ell_s**2-4*(B['h']-g*L/(2*s.sqrt(2)))**2)==0
    assert s.cancel(B['N']+3*g*L**2/2-L*(B['p']+4*B['h'])/s.sqrt(2))==0
    for fs in (False,True):
        for n,z in SECTORS:
            K,r=load_raw(n,z,fs);stored,_=read_matrix(OUT/('branch_'+raw_name(n,z,fs)))
            same(on_branch(K,r),stored)
    for n,z in SECTORS:
        K,r=load_raw(n,z);stored,_=read_matrix(OUT/('minus_'+raw_name(n,z)))
        same(on_branch(K,r,chi=-1),stored)
    ok('BPS equations, g-preserving normalization and both chirality matrices')

def generic_checks():
    level=s.cancel(v*ell_s**2)*S*(S-1)
    for prefix,chi in (('',1),('minus_',-1)):
        for n,ids,chart,name in ((1,None,VECTOR_CHART,'vector'),(0,SCALAR_INDICES,SCALAR_CHART,'scalar')):
            K,r=read_matrix(OUT/(('branch_' if chi==1 else 'minus_')+'raw_n'+str(n)+'.json'))
            if ids is not None:K=K.extract(ids,ids);r=subrecord(r,ids,ids)
            old=record('physical_'+prefix+'n'+str(n));fresh,div=certificate(K,r,chart)
            proof_matches(fresh,old)
            expected=generic_targets()[name].subs(M2,level)
            if chi==-1:expected=expected.subs(D,2-D)
            assert div==primitive(expected)
            ok(f'generic n={n}, chi={chi}: exact maximal-minor divisor and invariant propagators')
    K,r=read_matrix(OUT/'branch_raw_n0.json')
    other=[i for i in range(K.rows) if i not in SCALAR_INDICES]
    extra,div=certify_blocks(K.extract(other,other),subrecord(r,other,other),'constraints')
    assert div.degrees()[2]<=0 and extra['rank']==5
    for n,z in ((2,False),(1,True),(0,True),(-1,True)):
        K,r=read_matrix(OUT/('branch_'+raw_name(n,z)));K=real_charged_basis(K)
        fresh,div=certificate(K,r);proof_matches(fresh,record('physical_n'+str(n)+('Z' if z else '')))
        name='spin2' if not z else {1:'Z+',0:None,-1:'Z-'}[n]
        assert div==target_divisor(name) if name else div.degrees()[2]<=0
    K,_=read_matrix(OUT/'branch_raw_n2.json')
    assert not rational(K[0]+L*k*P3**3/(32*P2**3)*cubic.subs(M2,level))
    assert s.cancel(nuf-1-2*P1*P2/(k*P3))==0
    assert s.cancel(nuf+1-8*(P1+k)/(k*P3))==0
    ok('generic 3 spin-2 + 10 neutral vector + 5 scalar + 2 charged modes; TT prefactor; flat identities')

def special_checks():
    level=s.cancel(v*ell_s**2)*S*(S-1)
    targets={('hqd',0):D**2*(D-2)**2,
             ('h1f',0):D**4*(D-2)**4,
             ('h1f',1):(D-3)**2*(D+1)**2*(D-nuf)**2,
             ('j1',2):cubic.subs(M2,level.subs(S,-1)),
             ('j1',1):generic_targets()['vector'].subs(M2,level.subs(S,-1)),
             ('j1',0):generic_targets()['scalar'].subs(M2,level.subs(S,-1))/(D*(2-D))}
    for (levelname,n),target in targets.items():
        representation='raw' if levelname=='j1' else 'fs'
        K,r=read_matrix(OUT/(f'branch_{representation}_n{n}.json'))
        B,br,dropped=restrict(K,r,levelname)
        if levelname!='j1':assert dropped.is_zero_matrix
        fresh,div=certify_blocks(B,br,levelname)
        old=record(f'physical_{levelname}_n{n}')
        assert div==primitive(target) and fresh['physical_divisor']==old['physical_divisor']
        assert fresh['rank']==old['rank']
        ok(f'{levelname}, n={n}: restricted Hessian, rank and physical divisor')
    tt={2:D*(D-2)*(D-1-mul),
        1:(D-3)**2*(D-1)**2*(D+1)**2*(D-mul)*(D-nuf)**2*rr.subs(D,D-1),
        0:D**4*(D-2)**4*rr*rr.subs(D,2-D)}
    for n,z in SECTORS:
        K,r=load_raw(n,z,True);B=on_branch(K,r,torus=True)
        stored,_=read_matrix(OUT/('torus_n'+str(n)+('Z' if z else '')+'.json'));same(B,stored)
        fresh,div=certify_blocks(real_charged_basis(B) if z else B,r,'torus')
        old=record('physical_torus_n'+str(n)+('Z' if z else ''))
        assert fresh['physical_divisor']==old['physical_divisor']
        target=tt[n] if not z else ({1:D-nuf,0:s.Integer(1),-1:D-2+nuf}[n])
        assert div==primitive(target.subs(k,torus))
    from constant import derive
    assert derive()==record('constant')
    ok('constant fixed-flux reduction and T2: complete restricted matrices and divisors')

def torus_momentum_checks():
    for n,z in SECTORS:
        K,rec=load_raw(n,z,True);B=on_branch(K,rec,torus=True,momentum=True)
        rec['harmonic_chart']='flat Fourier'
        label='torus_momentum_n'+str(n)+('Z' if z else '')
        stored,_=read_matrix(OUT/(label+'.json'));same(B,stored)
        fresh,div=certify_blocks(real_charged_basis(B) if z else B,rec,label)
        old=record('physical_'+label)
        assert fresh['rank']==old['rank'] and fresh['physical_divisor']==old['physical_divisor']
        name={2:'spin2',1:'vector',0:'scalar'}[n] if not z else {1:'Z+',0:None,-1:'Z-'}[n]
        target=generic_targets()[name].subs(M2,-S**2/9).subs(k,torus) if name else s.Integer(1)
        assert div==primitive(target)
    ok('nonzero T2 Fourier momentum: six independent matrices and generic physical divisors')

def norm_identities():
    # Exact residues: no rational fitting or selected values of the couplings.
    assert not rational(F.subs(M2,0)-D*(D-2)*rr)
    assert not rational(kappa*(1-1/mul)-L*X/(2*P2*P4))
    assert not rational(kappa*(1+1/mul)-L*(2-3*k)*P2/P4)
    q=L**2*k-3*L*k-2*L+8
    targets={('h1f_n1','h_p3',s.Integer(3)):P2**2*P4/(4*L**2*(k*L-2)*P3**2*q),
             ('h1f_n1','h_p3',s.Integer(-1)):-P2**3*P4/(16*L**2*(k*(L-1)-2)*P3**2*q),
             ('hqd_n0','h_34',s.Integer(2)):P2**3/(L*P3**2*P4)}
    for (label,probe,root),target in targets.items():
        data=record('physical_'+label)
        block=next(b for b in data['blocks'] if probe in b.get('probes',{}))
        prop=unpack_fraction(block['probes'][probe])
        got=s.cancel((D-root)*prop).subs(D,root)
        assert s.cancel(got-target)==0
    from norms import symbolic_residue
    data=record('physical_n1');names=data['probe_names']
    flat=symbolic_residue(data['probes']['h_p3'],nuf)
    other=symbolic_residue(data['probes']['h_p4_transverse'],nuf)
    assert not (flat-other)
    assert not symbolic_residue(data['propagator'][names.index('h_p3')][names.index('h_p4_transverse')],nuf)
    charged=symbolic_residue(record('physical_n1Z')['probes']['Z_p'],nuf)
    level=s.cancel(v*ell_s**2)*S*(S-1)
    # This quotient is positive for a nonzero physical Laplacian eigenvalue.
    assert not (flat/rational(S*(1-S))/charged-rational(2*P2**4/(P3**4*level*(nuf**2-1))))
    for label,probe,root,target in (
            ('torus_n1','h_p3',3,-(L-3)/(18*L)),
            ('torus_n1','h_p3',-1,s.Rational(1,72)),
            ('torus_n0','h_34',2,(L-3)/(18*(L**2-6*L+12)))):
        block=next(b for b in record('physical_'+label)['blocks'] if probe in b.get('probes',{}))
        assert not (symbolic_residue(block['probes'][probe],s.Integer(root))-rational(target))
    block=next(b for b in record('physical_j1_n1')['blocks'] if 'h_p3' in b.get('probes',{}))
    jr=symbolic_residue(block['probes']['h_p3'],s.Integer(1))
    jt=-((L*k-4)*P4)/(3*L**3*(-P3)*(L**2*k**2-2*L**2*k+2*L*k+4*L-4*k-8))
    assert not (jr-rational(jt))
    # The signed-radius TT identity retains the prefactor needed for norms.
    K,_=read_matrix(OUT/'branch_raw_n2.json')
    target=P3**2/(8*P2**2)*kappa*D*(D-2)*(1-(D-1)/mul)
    assert not rational(K[0].subs(S,0)-target)
    # k=0 is a separate degree degeneration, never division by k followed by
    # dropping the diverging roots without checking the remaining polynomial.
    assert s.degree(s.cancel(k*cubic).subs(k,0),D)==2
    assert s.degree(s.cancel(k*F).subs(k,0),D)==4
    assert s.cancel((k*(D-nuf)).subs(k,0)).has(D) is False
    ok('exact flat, harmonic-vector/HQD, torus and j=1 current residues; TMG prefactor; k=0 degree degeneration')

def negative_control():
    from sectors import sector
    bg={name:se.Symbol(name) for name in 'L N p h r l w g lam'.split()}
    for n in (2,1):
        bad=sector(bg,n,se.Symbol('D'),se.Symbol('S'),model='GBnoE',verbose=False)
        K,_=load_raw(n);B=s.Matrix(bad['K'])
        eq=all(s.cancel(x-y)==0 for x,y in zip(K,B))
        assert eq if n==2 else not eq
    ok('negative control: deleting E terms changes the vector Hessian while leaving TT unchanged')

def source_hashes():
    data=json.loads((HERE/'source_manifest.json').read_text())
    root=HERE.parents[1]
    assert data['repository_inputs']
    for name,digest in data['repository_inputs'].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
    ok('current repository action-input fingerprints')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--norms',action='store_true');p.add_argument('--write-log',action='store_true')
    args=p.parse_args();start=time.monotonic()
    for fn in (source_hashes,source_checks,branch_checks,generic_checks,special_checks,torus_momentum_checks,norm_identities,negative_control):fn()
    if args.norms:
        from norms import verify_samples,accumulation_samples
        assert verify_samples()==record('norm_samples')
        assert accumulation_samples()==record('accumulation_norm_samples')
        ok('v109 upper-table norm samples: analytic residues, 80/140-digit agreement')
        ok('v109 lower-table accumulation norms: 45 finite levels, 80/140-digit agreement')
        from product_checks import verify_products
        verify_products()
        ok('formal alternative branches, E-deletion roots and six standalone product comparisons')
    ok('item 24 scientific checks complete; structural repository validation is separate')
    if args.write_log:(OUT/'verification.log').write_text('\n'.join(MESSAGES)+'\n')
    print('elapsed seconds',round(time.monotonic()-start,2))

if __name__=='__main__':main()
