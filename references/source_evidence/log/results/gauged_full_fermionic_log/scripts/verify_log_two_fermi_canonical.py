"""Independent component-array and exterior-algebra checks for the new file."""
import sys,runpy,io,contextlib,pickle,json,itertools,random,time,gzip
from pathlib import Path
import numpy as np
import canonicalize_log_two_fermi as q

with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(q.BASE/'scripts/common_conventions_check_frozen.py'),run_name='read_only_matrix_input')
C=np.array(m['C'],complex);U=-C;E=np.array([[0,1],[-1,0]],complex)
eta=np.array([-1,1,1,1,1]);gamma=np.array(m['g'],complex)
g2=np.array([[np.array(m['gam']((a,b)),complex) for b in range(5)] for a in range(5)])
rng=np.random.default_rng(240926); cache={}

def arr(f):
    nd=len(f.ds);ix=f.ds+f.ix
    if f.name=='pow':return np.array(1.3**f.power)
    if f.name=='eps':
        return (E if f.ix[0][0]=='+' else -E) if f.ix[0][1]=='u' else (U if f.ix[0][0]=='+' else C)
    if f.name=='suB':return E
    if f.name=='eta':return np.diag(eta) if f.ix[0][0]==f.ix[1][0] else np.eye(5)
    if f.name=='del':return np.eye({'s':4,'l':5,'u':2}[f.ix[0][1]])
    if f.name=='volB':
        z=np.zeros((5,)*5,complex)
        for ids in itertools.permutations(range(5)):z[ids]=(-1)**sum(a>b for j,a in enumerate(ids) for b in ids[j+1:])
        for k,x in enumerate(f.ix):
            if x[0]=='-':z*=eta.reshape([5 if i==k else 1 for i in range(5)])
        return z
    if f.name=='g1':z=np.einsum('aij,jk->aik',-gamma,C)*eta[:,None,None]
    elif f.name=='g2':z=np.einsum('abij,jk->abik',-g2,C)*eta[:,None,None,None]*eta[None,:,None,None]
    else:
        key=f.name,nd
        if key not in cache:
            shape=tuple({'s':4,'l':5,'u':2}[x[1]] for x in ix)+((2,) if f.parity else ())
            z=rng.integers(-2,3,shape).astype(complex)
            if f.name in ('hatF','ten','RQ','RV','RMB'):z=z-z.swapaxes(nd,nd+1)
            if f.name=='RMB':z=z-z.swapaxes(nd+2,nd+3)
            if f.name=='RV':z=z+z.swapaxes(nd+2,nd+3)
            if f.name=='aux':z=z+z.swapaxes(nd,nd+1)
            cache[key]=z
        z=cache[key].copy()
    for k,x in enumerate(ix):
        want='+' if x[1]=='u' else '-'
        if x[0]==want:continue
        if x[1]=='l':z*=eta.reshape([5 if i==k else 1 for i in range(z.ndim)])
        else:z=np.moveaxis(np.tensordot(-E if x[1]=='u' else U,z,axes=(1,k)),0,k)
    return z

def evaluate(c,fs,slot):
    mapping={};args=[];odd=[]
    for f in fs:
        ix=[]
        for x in q.b.allix(f):
            mapping.setdefault(x[1:],len(mapping));ix.append(mapping[x[1:]])
        if f.parity:
            k='odd'+str(len(odd));mapping[k]=len(mapping);odd.append(mapping[k]);ix.append(mapping[k])
        args.extend([arr(f),ix])
    free=[mapping[x] for x in q.p.FREE[slot]]
    z=np.einsum(*args,free+odd,optimize='greedy') if args else np.array(1)
    if len(odd)==2:z=z[...,0,1]-z[...,1,0]
    return complex(c.r,c.i)*z

def run(samples=80):
    with gzip.open(q.OUT/'parsed.pkl.gz','rb') as stream:slots=pickle.load(stream)
    report={};selector=random.Random(92624)
    for slot,pol in slots.items():
        chosen=list(range(min(12,len(pol.ts))))+selector.sample(range(len(pol.ts)),min(samples,len(pol.ts)))
        worst=0
        for j in chosen:
            c,fs=pol.ts[j];old=evaluate(c,fs,slot)
            d,gs=q.metric_reduce(c,fs);d,gs=q.tensor_canon(d,gs,slot)
            new=evaluate(d,gs,slot) if d else old*0
            residual=float(np.max(abs(old-new)));scale=max(1.,float(np.max(abs(old))))
            assert residual<1e-8*scale,('tensor',slot,j,old,new,c,fs,d,gs)
            worst=max(worst,residual/scale)
            if d:
                result=q.reduce_clifford(d,gs,slot)
                final=sum((evaluate(e,hs,slot) for e,hs in result),np.zeros_like(new))
                residual=float(np.max(abs(new-final)));scale=max(1.,float(np.max(abs(new))))
                assert residual<1e-8*scale,('Clifford',slot,j,new,final,d,gs,result)
                worst=max(worst,residual/scale)
                reduced=[]
                for e,hs in result:
                    e,hs=q.metric_reduce(e,hs)
                    for ee,hh in q.epsilon_pairs(e,hs):
                        ee,hh=q.tensor_canon(ee,hh,slot)
                        if ee:reduced.append((ee,hh))
                final2=sum((evaluate(e,hs,slot) for e,hs in reduced),np.zeros_like(new))
                residual=float(np.max(abs(new-final2)))
                assert residual<1e-8*scale,('final reduction',slot,j,new,final2)
                worst=max(worst,residual/scale)
        report[slot]={'terms_checked':len(chosen),'max_relative_residual':worst}
        print('PASS array tests',slot,report[slot],flush=True)
    (q.OUT/'array_checks.json').write_text(json.dumps(report,indent=2)+'\n')

def exact_clifford():
    """Entries are Gaussian integers; all assertions use exact equality."""
    count=0
    for rank in range(6):
        for aa in itertools.combinations(range(5),rank):
            ga=np.array(m['gam'](aa),complex)
            for bb in range(5):
                rhs=np.array(m['gam'](aa+(bb,)),complex)
                for j,a in enumerate(aa):
                    if a==bb:rhs+=(-1)**(rank-1-j)*eta[a]*np.array(m['gam'](aa[:j]+aa[j+1:]),complex)
                assert np.array_equal(ga@gamma[bb],rhs),(aa,bb)
                count+=1
    dual=0
    for rank in (3,4,5):
        for aa in itertools.combinations(range(5),rank):
            rhs=np.zeros((4,4),complex)
            for bb in itertools.permutations([x for x in range(5) if x not in aa]):
                whole=aa+bb;sg=(-1)**sum(a>b for j,a in enumerate(whole) for b in whole[j+1:])
                rhs+=sg*np.prod([eta[x] for x in bb])*np.array(m['gam'](bb),complex)
            rhs*= {3:-0.5j,4:1j,5:1j}[rank]
            assert np.array_equal(np.array(m['gam'](aa),complex),rhs),(aa,rhs)
            dual+=1
    placements=0
    for rank in (1,2):
        for lor in itertools.product(range(5),repeat=rank):
            g=np.array(m['gam'](lor),complex)
            for signs in itertools.product('+-',repeat=2):
                atom=q.A('g'+str(rank),tuple('+l'+str(j) for j in range(rank))+tuple(s+'s'+str(j) for j,s in enumerate(signs)))
                actual=arr(atom)[lor]
                for rev in (False,True):
                    sg,left,blade,right=q.matrix_edge(atom,rev)
                    pred=sg*(C if left else np.eye(4))@g@(C if right else np.eye(4))
                    assert np.array_equal(pred,actual.T if rev else actual)
                    placements+=1
    pauli=0
    for rank in (0,1):
        for aa in itertools.combinations(range(5),rank):
            kernel=np.kron(C@np.array(m['gam'](aa),complex),E)
            assert np.array_equal(kernel,kernel.T);pauli+=1
    triplets=[np.array([[1,0],[0,0]]),np.array([[0,1],[1,0]]),np.array([[0,0],[0,1]])]
    for aa in itertools.combinations(range(5),2):
        for yy in triplets:
            kernel=np.kron(C@np.array(m['gam'](aa),complex),yy)
            assert np.array_equal(kernel,kernel.T);pauli+=1
    report={'right_vector_identities':count,'duality_identities':dual,'indexed_gamma_placement_checks':placements,'identical_fermion_zero_kernels':pauli,'exact_entry_residual':0}
    (q.OUT/'clifford_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS exact Clifford identities',report,flush=True)

def exact_epsilon():
    selector=random.Random(9262401);count=0
    def vol(atom,values):
        ids=[values[x[1:]] for x in atom.ix]
        if len(set(ids))!=5:return 0
        sg=(-1)**sum(a>b for j,a in enumerate(ids) for b in ids[j+1:])
        for x,a in zip(atom.ix,ids):
            if x[0]=='-':sg*=int(eta[a])
        return sg
    for shared in range(6):
        free=5-shared
        for sample in range(40):
            ai=[selector.choice('+-')+'la'+str(j) for j in range(free)]+['+lc'+str(j) for j in range(shared)]
            bi=[selector.choice('+-')+'lb'+str(j) for j in range(free)]+['-lc'+str(j) for j in range(shared)]
            selector.shuffle(ai);selector.shuffle(bi);aa=q.A('volB',tuple(ai));bb=q.A('volB',tuple(bi))
            values={x[1:]:selector.randrange(5) for x in ai+bi if x[2] in 'ab'}
            if sample%2==0:
                for j in range(free):values['la'+str(j)]=values['lb'+str(j)]=j
            lhs=0
            for cs in itertools.permutations(range(5),shared):
                values.update({'lc'+str(j):c for j,c in enumerate(cs)});lhs+=vol(aa,values)*vol(bb,values)
            rhs=0
            for c,fs in q.epsilon_pairs(q.b.coef(1),(aa,bb)):
                value=c.r;assert not c.i
                for f in fs:
                    assert f.name in ('eta','del')
                    x,y=f.ix;a,b=values[x[1:]],values[y[1:]]
                    value*=int(a==b)*(int(eta[a]) if f.name=='eta' and x[0]==y[0] else 1)
                rhs+=value
            assert lhs==rhs,(shared,aa,bb,lhs,rhs)
            count+=1
    report={'component_epsilon_pair_tests':count,'shared_index_counts':list(range(6)),'exact_residual':0}
    (q.OUT/'epsilon_checks.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS epsilon pairs',report,flush=True)

def final_checks():
    report={}
    for slot in q.p.WEIGHTS:
        file=q.OUT/(slot+'-clifford.pkl')
        if not file.exists():continue
        pol=pickle.load(open(file,'rb'));q.b.check(pol,q.p.WEIGHTS[slot],q.p.FREE[slot])
        repeated=q.collect_wedge(q.collect_epsilon(pol,slot),slot)
        assert {fs:c for c,fs in pol.ts}=={fs:c for c,fs in repeated.ts},('not idempotent',slot)
        assert all(sum(f.parity for f in fs)<=2 for c,fs in pol.ts)
        q.grouped(pol,slot)
        rewrites=0;worst=0
        for c,fs in pol.ts:
            # Input representation has already been collected; validate every
            # additional applicable two-form identity, if any remain.
            expanded=q.two_form_wedge(c,fs)
            if len(expanded)==1:continue
            old=evaluate(c,fs,slot);new=sum(evaluate(d,gs,slot) for d,gs in expanded)
            residual=float(np.max(abs(old-new)));scale=max(1.,float(np.max(abs(old))))
            assert residual<1e-9*scale;worst=max(worst,residual/scale);rewrites+=1
        report[slot]={'monomials':len(pol.ts),'idempotent_collection':True,'all_indices_and_weights':True,'max_explicit_fermion_degree':max(sum(f.parity for f in fs) for c,fs in pol.ts),'remaining_wedge_rewrites_tested':rewrites,'relative_residual':worst}
    (q.OUT/'final_structure_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    # Complete triplet symmetry, including every retained bilinear.
    pol=pickle.load(open(q.OUT/'L-clifford.pkl','rb'))
    def exchange(x):return x[:1]+{'uI':'uJ','uJ':'uI'}.get(x[1:],x[1:])
    swapped=q.b.P.terms([(c,tuple(q.b.replace(f,ix=tuple(map(exchange,f.ix))) for f in fs)) for c,fs in pol.ts])
    diff=q.collect_wedge(q.collect_epsilon(pol-swapped,'L'),'L');assert not diff.ts
    (q.OUT/'triplet_symmetry.json').write_text(json.dumps({'L_ij_equals_L_ji':True,'difference_terms':0},indent=2)+'\n')
    # Check CTF-10b with integer arithmetic on all 125 components of five
    # independent two-forms; multiply by four to avoid division.
    metric=eta.astype(int);volume=np.zeros((5,)*5,dtype=int)
    for ids in itertools.permutations(range(5)):volume[ids]=-(-1)**sum(a>b for j,a in enumerate(ids) for b in ids[j+1:])
    for seed in range(5):
        raw=np.random.default_rng(seed).integers(-3,4,(5,5));two=raw-raw.T;upper=two*metric[:,None]*metric[None,:]
        vv=np.einsum('abcde,bc,de->a',volume,upper,upper)
        lhs=4*np.einsum('cd,abdef,ef->abc',two*metric[None,:],volume,upper)
        rhs=np.einsum('bc,a->abc',np.diag(metric),vv)-np.einsum('ac,b->abc',np.diag(metric),vv)
        assert np.array_equal(lhs,rhs)
    (q.OUT/'wedge_identity_exact.json').write_text(json.dumps({'integer_component_entries_checked':625,'seeds':list(range(5)),'max_residual':0,'identity':'CTF-10b'},indent=2)+'\n')
    print('PASS final structure',report,flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--final':final_checks()
    else:exact_clifford();exact_epsilon();run(int(sys.argv[1]) if len(sys.argv)>1 else 80)
