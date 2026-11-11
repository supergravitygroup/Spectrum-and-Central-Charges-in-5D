"""Bounded numerical checks of the paragraph following paper eq:Kform.

Rebuilds the E-term deletion example and the six separate W/LOG/R2 examples
from action.py. Backgrounds and direct rank checks use mpmath precision;
the existing, prediction-independent polynomial pencil supplies candidates.
Only this package's outputs/product_checks/ is written with --write.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor,as_completed
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import time
import mpmath as mp
import numpy as np
import symengine as se
import sympy as sp
from scipy.optimize import linear_sum_assignment
from sectors import sector
from model import HERE

OUT=HERE/'outputs'/'product_checks'
ROOT=HERE.parents[1]
_spec=importlib.util.spec_from_file_location('product_pencil',HERE.parent/'gb_ads3_sigma2_fermionic_spectrum'/'polynomial.py')
pencil=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(pencil)
SECTORS=((2,False),(1,False),(0,False),(1,True),(0,True),(-1,True))
CASES=[(model,point) for model in ('W','LOG','R2') for point in ('a','b')]

def pack(z,digits=75):return [mp.nstr(mp.re(z),digits),mp.nstr(mp.im(z),digits)]
def unpack(z):return mp.mpc(*z)
def num(x,digits=115):
    a,b=sp.sympify(x).as_real_imag()
    return mp.mpc(str(a.evalf(digits)),str(b.evalf(digits)))
def write(name,data):
    OUT.mkdir(exist_ok=True)
    (OUT/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
def read(name):return json.loads((OUT/(name+'.json')).read_text())
def parameters(point):
    return ((sp.Integer(1),sp.Rational(1,10),sp.Integer(3)) if point=='a' else
            (sp.Rational(5,4),sp.Rational(-1,10),sp.Rational(1,2)+sp.I*sp.Rational(13,10)))

def background(model,point):
    """Solve first variations plus the Killing-spinor radius relation.

    The L variation is retained: L labels the solutions, it is not frozen
    before variation. Every independent tadpole is checked afterward.
    """
    L,c,S=parameters(point);h,w,l=se.symbols('h w l');D,T=se.symbols('D S')
    Ls=se.sympify(L);p=Ls/se.sqrt(2)
    bg=dict(L=Ls,p=p,h=h,w=w,l=l,r=-w*w,g=se.Integer(1),lam=se.Integer(0),
            N=-3*Ls*Ls/2+Ls*(p+4*h)/se.sqrt(2))
    couplings=dict(alpha=se.sympify(c if model=='W' else 0),
                   beta=se.sympify(c if model=='LOG' else 0),
                   zeta=se.sympify(c if model=='R2' else 0))
    result=sector(bg,0,D,T,verbose=False,model='WLOG',**couplings)
    linear=result['lin_a'].subs({D:2,T:1})
    equations=[sp.sympify(se.expand(se.diff(linear,a))) for a in result['avars']]
    equations=[x for x in equations if x!=0]
    hs,ws,ls=sp.symbols('h w l')
    radius=1/ls**2-4*(hs-L/(2*sp.sqrt(2)))**2
    guess=[x.evalf(30) for x in ((L-2)/(4*sp.sqrt(2)),sp.sqrt(L*(4-L)/2),2*sp.sqrt(2)/(L+2))]
    best=None
    for ij in itertools.combinations(range(len(equations)),2):
        try:
            sol=sp.nsolve([equations[i] for i in ij]+[radius],(hs,ws,ls),guess,
                          prec=125,tol=sp.Float('1e-115'),maxsteps=100)
        except (ValueError,ZeroDivisionError):continue
        subs=dict(zip((hs,ws,ls),sol))
        residual=max(abs(num(x.subs(subs))) for x in equations+[radius])
        if residual<mp.mpf('1e-105'):
            best=(sol,ij,residual);break
    if best is None:raise AssertionError(('no stationary BPS background',model,point))
    sol,ij,residual=best
    assert sol[1]>0 and sol[2]>0
    # Retain 115 decimal digits, rather than an under-resolved background
    # combined with an unjustifiably smaller rank threshold.
    exact={se.Symbol(str(x)):se.sympify(sp.Rational(str(y.evalf(115))))
           for x,y in zip((hs,ws,ls),sol)}
    frozen={name:se.expand(value.subs(exact)) for name,value in bg.items()}
    fixed={sp.Symbol(str(x)):sp.sympify(y) for x,y in exact.items()}
    checks=[abs(num(x.subs(fixed))) for x in equations+[radius]]
    assert max(checks)<mp.mpf('1e-105')
    meta=dict(model=model,point=point,L=str(L),coupling=str(c),S=str(S),
        digits_solve=125,digits_retained=115,equations=len(equations),
        selected_equations=list(ij),max_stationarity_residual=mp.nstr(max(checks),12),
        h=pack(num(fixed[hs])),w=pack(num(fixed[ws])),ell=pack(num(fixed[ls])),
        v=pack(-num(fixed[ws])**2),
        harmonic_scope='algebraic continuation S=3 on H2' if point=='a' else 'H2 principal series nu=13/10')
    return frozen,couplings,S,meta

def matrices(bg,couplings,S,n,charged,model='WLOG'):
    D=se.Symbol('D');result=sector(bg,n,D,se.sympify(S),charged=charged,
                                  model=model,verbose=False,**couplings)
    # Exact polynomial extraction, not interpolation. Coefficients of the
    # rational 115-digit background are evaluated at 115 decimal digits.
    polys=[[sp.Poly(sp.sympify(x),sp.Symbol('D')) for x in row] for row in result['K']]
    degree=max([p.degree() for row in polys for p in row if not p.is_zero],default=0)
    C=[mp.matrix([[num(p.nth(j)) for p in row] for row in polys]) for j in range(degree+1)]
    return C,dict(avars=list(map(str,result['avars'])),bvars=list(map(str,result['bvars'])),degree=int(degree))

def evaluate(C,z):
    value=mp.zeros(C[0].rows)
    for a in C[::-1]:value=value*z+a
    return value
def derivative(C,z):
    return sum((j*a*z**(j-1) for j,a in enumerate(C) if j),mp.zeros(C[0].rows))
def scale(C,z):return max(mp.mpf(1),sum(mp.norm(a)*max(1,abs(z))**j for j,a in enumerate(C)))
def singular(C,z):return list(mp.svd(evaluate(C,z),compute_uv=False))
def rank_at(C,z,tol=mp.mpf('1e-55')):
    sv=singular(C,z);norm=scale(C,z)
    return sum(x>norm*tol for x in sv),[x/norm for x in sv]

def high_precision_root(C,guess,rank,multiplicity,seed):
    """Refine an extracted candidate in an independent maximal projection."""
    rnd=random.Random(seed);m=C[0].rows
    if rank==m:A=B=mp.eye(m)
    else:
        while True:
            A=mp.matrix([[rnd.randrange(-4,5) for _ in range(m)] for _ in range(rank)])
            B=mp.matrix([[rnd.randrange(-4,5) for _ in range(rank)] for _ in range(m)])
            if abs(mp.det(A*evaluate(C,mp.mpc('.23','.71'))*B))>mp.mpf('1e-60'):break
    P=[A*c*B for c in C];z=mp.mpc(str(guess.real),str(guess.imag))
    for _ in range(80):
        K=evaluate(P,z);KP=derivative(P,z)
        try: inv=K**-1
        except ZeroDivisionError:break
        t=inv*KP;slope=sum(t[i,i] for i in range(rank))
        if not slope:raise AssertionError('zero Newton slope')
        step=multiplicity/slope;z-=step
        if abs(step)<mp.mpf('1e-85')*(1+abs(z)):break
    return z

def extraction(C,allow_empty=False):
    # The guard is applied at high precision before any double precision
    # pencil. A 42-digit background cannot pass the 1e-90 null-space guard.
    probes=[mp.mpc('.371','.113'),mp.mpc('-1.21','.83'),mp.mpc('1.91','-.73')]
    diagnostic=[rank_at(C,z) for z in probes];ranks=[r for r,_ in diagnostic]
    assert len(set(ranks))==1,('ambiguous generic rank',ranks)
    r=ranks[0];m=C[0].rows
    for _,sv in diagnostic:
        if r<m:assert max(sv[r:])<mp.mpf('1e-90'),('background precision insufficient',sv[r:])
        if r:assert sv[r-1]>mp.mpf('1e-20'),('unresolved retained rank',sv[r-1])
    Cdouble=np.asarray([[[complex(x) for x in row] for row in a.tolist()] for a in C])
    if r==m and all(mp.norm(c)==0 for c in C[1:]):
        return [],dict(generic_rank=r,dimension=m,generic_probe_ranks=ranks,root_count=0)
    runs=[]
    for seed in (41,137):
        try:found,info=pencil.extract(Cdouble,seed=seed,projections=4,scale=3.)
        except ArithmeticError as exc:
            if allow_empty and str(exc).startswith("('no common physical roots'"):
                found=[];info=dict(generic_rank=r,empty_candidate_set=True)
            else:raise
        assert info['generic_rank']==r
        runs.append((found,info))
    flat=lambda rs:[complex(*x['root']) for x in rs for _ in range(x['multiplicity'])]
    agreement=pencil.distance_multiset(flat(runs[0][0]),flat(runs[1][0]))
    assert agreement<1e-6
    records=[]
    for entry in runs[0][0]:
        mult=entry['multiplicity'];z0=complex(*entry['root'])
        z=high_precision_root(C,z0,r,mult,311)
        zz=high_precision_root(C,z0,r,mult,997)
        assert abs(z-zz)<mp.mpf('1e-65')*(1+abs(z)),('projection disagreement',z,zz)
        rr,sv=rank_at(C,z)
        assert rr==r-mult,('no direct high precision rank drop',z,r,rr,mult)
        assert max(sv[rr:])<mp.mpf('1e-65')
        if rr:assert sv[rr-1]>mp.mpf('1e-20')
        for delta in (mp.mpf('0.0001'),mp.mpc(0,'0.0001')):
            assert rank_at(C,z+delta)[0]==r,('nonlocal rank loss',z)
        records.append(dict(root=pack(z),multiplicity=mult,rank=rr,
            normalized_singular_values=[mp.nstr(x,12) for x in sv],
            independent_projection_difference=mp.nstr(abs(z-zz),12)))
    return records,dict(generic_rank=r,dimension=m,generic_probe_ranks=ranks,
        generic_probe_singular_values=[[mp.nstr(x,12) for x in sv] for _,sv in diagnostic],
        rank_threshold='1e-55',gauge_guard='1e-90',retained_gap_guard='1e-20',
        double_candidate_difference=agreement,candidate_runs=[x[1] for x in runs],
        root_count=sum(x['multiplicity'] for x in records),
        scope='numerical finite-point rank drops; no all-parameter symbolic divisor claim')

def modes(sectors):
    out=[]
    for item in sectors:
        n=item['n'];q=int(item['charged'])
        for e in item['roots']:
            for _ in range(e['multiplicity']):
                d=unpack(e['root']);out.append((n,d,q))
                if q:out.append((n,mp.conj(d),-q))
                elif n:out.append((-n,2-d,0))
    return out

def pair_modes(items,tolerance=mp.mpf('1e-50')):
    """A complete matching of roots, preserving spin and R-charge.

    R-charges here are 0,+2,-2 in supercharge units. Internal q=+/-1
    denotes one charged complex field; each fermion-primary pair differs
    by two physical R-charge units.
    """
    edges={i:[] for i in range(len(items))}
    for i,(n,d,q) in enumerate(items):
        for j,(nn,dd,qq) in enumerate(items[:i]):
            close=lambda x:abs(x)<tolerance*(1+abs(d)+abs(dd))
            if (n==nn and abs(q-qq)==1 and close(d-dd)) or (q==qq and abs(n-nn)==1 and close((d-dd)-(n-nn))):
                edges[i].append(j);edges[j].append(i)
    def search(remaining):
        if not remaining:return []
        i=min(remaining,key=lambda x:len(set(edges[x])&remaining))
        for j in edges[i]:
            if j not in remaining:continue
            rest=search(remaining-{i,j})
            if rest is not None:return [(i,j)]+rest
        return None
    pairs=search(set(range(len(items))))
    return pairs,edges

def run_case(model,point,save=False):
    mp.mp.dps=115;start=time.monotonic()
    bg,couplings,S,meta=background(model,point)
    print(model,point,'background',meta['max_stationarity_residual'],flush=True)
    records=[]
    for n,charged in SECTORS:
        C,basis=matrices(bg,couplings,S,n,charged)
        roots,diag=extraction(C,allow_empty=charged and n==0)
        item=dict(n=n,charged=charged,**basis,roots=roots,verification=diag,
                  coefficients=[[[pack(x,115) for x in row] for row in c.tolist()] for c in C])
        records.append(item)
        print(model,point,n,charged,'rank',diag['generic_rank'],'roots',diag['root_count'],flush=True)
    values=modes(records);pairs,edges=pair_modes(values)
    assert pairs is not None,('unpaired modes',model,point,[(i,pack(values[i][1])) for i,e in edges.items() if not e])
    output=dict(background=meta,sectors=records,raw_roots=len(values),pairs=[list(x) for x in pairs],
        boson_primary_pairs=sum(values[i][2]==values[j][2] for i,j in pairs),
        fermion_primary_pairs=sum(values[i][2]!=values[j][2] for i,j in pairs),
        status='PASS',elapsed_seconds=round(time.monotonic()-start,2))
    if save:write(model+'_'+point,output)
    return output

def deletion(save=False):
    from model import branch,L,k,g
    from closed_forms import cubic,F
    mp.mp.dps=115;sub={L:10,k:sp.Rational(1,10),g:1}
    bg={name:se.sympify(value.subs(sub)) for name,value in branch().items()}
    bg.update(L=se.Integer(10),g=se.Integer(1),w=se.sqrt(-bg['r']))
    results=[]
    for n in (2,1,0):
        C,basis=matrices(bg,{},sp.Integer(3),n,False,model='GBnoE')
        roots,diag=extraction(C)
        results.append(dict(n=n,charged=False,**basis,roots=roots,verification=diag,
                            coefficients=[[[pack(x,115) for x in row] for row in c.tolist()] for c in C]))
        print('E deletion',n,'rank',diag['generic_rank'],'roots',diag['root_count'],flush=True)
    vector=[unpack(e['root']) for e in results[1]['roots']]
    spin2=[unpack(e['root']) for e in results[0]['roots']]
    scalar=[unpack(e['root']) for e in results[2]['roots']]
    assert len(spin2)==3
    assert all(min(abs(x-1-y) for y in vector)>mp.mpf('0.01') for x in spin2)
    assert all(min(abs(x+1-y) for y in vector)>mp.mpf('0.001') for x in scalar)
    complex_pair=[z for z in vector if abs(abs(mp.im(z))-mp.mpf('1.866'))<mp.mpf('.001')]
    assert len(complex_pair)==2 and all(abs(mp.re(z)-mp.mpf('2.643'))<mp.mpf('.001') for z in complex_pair)
    target=[mp.mpf(x) for x in ('-2.108','3.550','10.061')]
    assert all(min(abs(x-y) for y in spin2)<mp.mpf('.001') for x in target)
    output=dict(L='10',k='1/10',S='3',sectors=results,status='PASS',
        complex_pair=[pack(z) for z in complex_pair],spin2_vector_partners_lost=3,
        scalar_root_partners_lost=len(scalar),physical_scalar_multiplets_lost=len(scalar)//2,
        scope='paper example, with all three explicit E_a-dependent GB terms removed')
    if save:write('E_deletion',output)
    return output

def decode_coefficients(record):
    return [mp.matrix([[unpack(x) for x in row] for row in a]) for a in record['coefficients']]

def verify_products(fresh=False,write_log=False):
    """Read-only by default; --write-log writes the two verification files.

    --fresh repeats all 36 standalone source Hessians and the three deleted
    GB Hessians. Direct high-precision ranks are always recomputed.
    """
    mp.mp.dps=115;start=time.monotonic();messages=[];max_source=mp.mpf(0)
    manifest=json.loads((HERE/'source_manifest.json').read_text())
    for name,digest in manifest['product_check_inputs'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    messages.append('PASS current local action and numerical-solver fingerprints')
    total_roots=0;max_null=mp.mpf(0);min_retained=mp.inf;case_rows=[]
    for model,point in CASES:
        saved=read(model+'_'+point)
        assert saved['status']=='PASS' and len(saved['sectors'])==6
        bg,couplings,S,meta=background(model,point) if fresh else (None,None,None,None)
        for rec in saved['sectors']:
            C=decode_coefficients(rec);rank=rec['verification']['generic_rank']
            assert rank_at(C,mp.mpc('.391','.217'))[0]==rank
            if fresh:
                current,_=matrices(bg,couplings,S,rec['n'],rec['charged'])
                assert len(current)==len(C)
                error=max(mp.norm(a-b)/max(1,mp.norm(a)) for a,b in zip(current,C))
                max_source=max(max_source,error)
                assert error<mp.mpf('1e-105'),('source coefficients changed',model,point,error)
            for root in rec['roots']:
                z=unpack(root['root']);rank_root,sv=rank_at(C,z)
                assert rank_root==rank-root['multiplicity']
                max_null=max(max_null,max(sv[rank_root:]))
                if rank_root:min_retained=min(min_retained,sv[rank_root-1])
                assert max(sv[rank_root:])<mp.mpf('1e-65')
                assert not rank_root or sv[rank_root-1]>mp.mpf('1e-20')
                assert rank_at(C,z+mp.mpc('.00013','.00017'))[0]==rank
        vals=modes(saved['sectors']);pairs,_=pair_modes(vals)
        assert pairs is not None and len(pairs)*2==saved['raw_roots']==len(vals)
        assert len({i for pair in pairs for i in pair})==len(vals)
        total_roots+=len(vals)
        case_rows.append(dict(model=model,point=point,raw_roots=len(vals),
            boson_primary_pairs=saved['boson_primary_pairs'],
            fermion_primary_pairs=saved['fermion_primary_pairs']))
        messages.append(f'PASS {model}_{point}: all six sectors, {len(vals)} raw roots, complete matching')
    deleted=read('E_deletion')
    for rec in deleted['sectors']:
        C=decode_coefficients(rec);r=rec['verification']['generic_rank']
        for e in rec['roots']:
            assert rank_at(C,unpack(e['root']))[0]==r-e['multiplicity']
    if fresh:
        newer=deletion(False)
        for a,b in zip(newer['sectors'],deleted['sectors']):
            A=decode_coefficients(a);B=decode_coefficients(b)
            assert max(mp.norm(x-y)/max(1,mp.norm(x)) for x,y in zip(A,B))<mp.mpf('1e-105')
    # Mutation controls: wrong energy/charge, omitted root, and numerical
    # gauge breaking at the precision that caused the historical failure.
    toy=[(0,mp.mpf(2),0),(1,mp.mpf(3),0)]
    assert pair_modes(toy)[0] is not None
    assert pair_modes(toy[:1])[0] is None
    assert pair_modes([toy[0],(1,mp.mpf('3.01'),0)])[0] is None
    assert pair_modes([toy[0],(1,mp.mpf(3),1)])[0] is None
    bad=[mp.diag([1,-2,mp.mpf('1e-42')]),mp.diag([0,1,0])]
    try:extraction(bad)
    except AssertionError as exc:
        assert 'unresolved retained rank' in str(exc)
    else:raise AssertionError('under-resolved gauge direction was counted as physical')
    good=[mp.diag([1,-2,0]),mp.diag([0,1,0])]
    found,_=extraction(good)
    assert len(found)==1 and abs(unpack(found[0]['root'])-2)<mp.mpf('1e-65')
    messages.append('PASS E deletion: quoted complex pair and all bosonic-primary partner losses')
    messages.append('PASS missing-root, wrong-energy, wrong-charge and 42-digit gauge-breaking controls')
    result=dict(status='PASS',fresh_source_matrices=fresh,standalone_sectors=36,
        deleted_sectors=3,standalone_raw_roots=total_roots,cases=case_rows,
        max_source_coefficient_error=mp.nstr(max_source,12) if fresh else None,
        maximum_discarded_singular_value=mp.nstr(max_null,12),
        minimum_retained_singular_value=mp.nstr(min_retained,12),
        precision_digits=115,root_rank_threshold='1e-55',root_residual_guard='1e-65',
        elapsed_seconds=round(time.monotonic()-start,2),messages=messages)
    for line in messages:print(line,flush=True)
    if write_log:
        assert fresh,'Only a fresh source verification may replace the recorded log'
        write('verification',result)
        (OUT/'verification.log').write_text('\n'.join(messages)+'\n')
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write',action='store_true');p.add_argument('--workers',type=int,default=1)
    p.add_argument('--verify',action='store_true');p.add_argument('--fresh',action='store_true')
    p.add_argument('--write-log',action='store_true')
    p.add_argument('--case',choices=[m+'_'+q for m,q in CASES]+['E_deletion'])
    args=p.parse_args()
    if args.verify:
        verify_products(args.fresh,args.write_log);return
    if args.fresh or args.write_log:p.error('--fresh and --write-log require --verify')
    if args.case=='E_deletion':deletion(args.write);return
    cases=[tuple(args.case.split('_'))] if args.case else CASES
    if args.workers==1:
        for model,point in cases:run_case(model,point,args.write)
    else:
        with ProcessPoolExecutor(args.workers) as pool:
            jobs={pool.submit(run_case,m,q,args.write):(m,q) for m,q in cases}
            for job in as_completed(jobs):job.result()
    if not args.case:deletion(args.write)

if __name__=='__main__':main()
