"""Rebuild the item-24 symbolic matrices and certified physical divisors.

All output is confined to this package's outputs/ directory.  No coupling is
assigned a numerical value.  Use --stage all for the complete derivation.
"""
import argparse
import json
import time
import sympy as s
import symengine as se
from model import HERE, D, S, load_raw, raw_name, on_branch, encode_matrix, read_matrix
from physical import certificate, pack_polynomial
from polynomial_matrix import ONE, primitive_in_D
from harmonics import restrict

SECTORS=((2,False),(1,False),(0,False),(1,True),(0,True),(-1,True))
VECTOR_CHART=([0,5,4,8,10,1,3],[5,0,4,10,8,3,1])
SCALAR_INDICES=[0,1,3,4,6,8,11,13,17,19,21,22]
SCALAR_CHART=([6,9,2,8,11,5,4,10,1],[10,1,7,11,0,6,8,4,3])
OUT=HERE/'outputs'

def save(name,data):
    OUT.mkdir(exist_ok=True)
    (OUT/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')

def raw():
    from sectors import sector
    bg={name:se.Symbol(name) for name in 'L N p h r l w g lam'.split()}
    for fs in (False,True):
        for n,z in SECTORS:
            result=sector(bg,n,se.Symbol('D'),se.Symbol('S'),charged=z,fs=fs,verbose=False)
            rec={key:list(map(str,result[key])) for key in ('avars','bvars')}
            save(raw_name(n,z,fs)[:-5],encode_matrix(s.Matrix(result['K']),rec,
                spin=n,charged=z,field_strength_variables=fs,
                parameters=list(bg)+['D','S'],
                linear_a=str(result['lin_a']),linear_b=str(result['lin_b'])))
            print('raw',n,z,fs,flush=True)

def branches():
    for fs in (False,True):
        for n,z in SECTORS:
            K,rec=load_raw(n,z,fs)
            B=on_branch(K,rec)
            save('branch_'+raw_name(n,z,fs)[:-5],encode_matrix(B,rec,chi=1,
                normalization='Khat = 2 Sb K Sa / g**2; k = lambda*g**2'))
            print('BPS matrix',n,z,fs,flush=True)

def subrecord(rec,rows,cols):
    return dict(avars=[rec['avars'][i] for i in cols],bvars=[rec['bvars'][i] for i in rows],
                **({'harmonic_chart':rec['harmonic_chart']} if 'harmonic_chart' in rec else {}))

def blocks(K):
    """Exact bipartite connected components, retaining zero row/column metadata."""
    remaining=set(range(K.rows+K.cols)); result=[]
    while remaining:
        frontier=[min(remaining)]; nodes=set()
        while frontier:
            node=frontier.pop()
            if node in nodes:continue
            nodes.add(node);remaining.discard(node)
            if node<K.rows:
                frontier.extend(K.rows+j for j in range(K.cols) if K[node,j]!=0 and K.rows+j not in nodes)
            else:
                frontier.extend(i for i in range(K.rows) if K[i,node-K.rows]!=0 and i not in nodes)
        rows=sorted(i for i in nodes if i<K.rows)
        cols=sorted(i-K.rows for i in nodes if i>=K.rows)
        result.append((rows,cols))
    return result

def certify_blocks(K,rec,label):
    records=[]; product=ONE; rank=0
    for rows,cols in blocks(K):
        if not rows or not cols:
            records.append(dict(original_rows=rows,original_cols=cols,rank=0));continue
        B=K.extract(rows,cols); br=subrecord(rec,rows,cols)
        proof,divisor=certificate(B,br)
        proof.update(original_rows=rows,original_cols=cols,**encode_matrix(B,br))
        records.append(proof);rank+=proof['rank']
        if divisor is not None:product*=divisor
    result=dict(label=label,rank=rank,shape=list(K.shape),blocks=records,
                physical_divisor=pack_polynomial(primitive_in_D(product)))
    return result,primitive_in_D(product)

def real_charged_basis(K):
    """Z4=i z4, barZ4=-i barz4: an invertible Hermitian congruence."""
    if not any(x.has(s.I) for x in K):return K
    assert K.shape==(3,3)
    result=s.diag(1,1,-s.I)*K*s.diag(1,1,s.I)
    assert not any(x.has(s.I) for x in result)
    return result

def generic():
    from closed_forms import target_divisor
    K,rec=read_matrix(OUT/'branch_raw_n1.json')
    proof,div=certificate(K,rec,VECTOR_CHART)
    assert div==target_divisor('vector')
    save('physical_n1',proof);print('certified generic vector',flush=True)
    K,rec=read_matrix(OUT/'branch_raw_n0.json')
    ids=SCALAR_INDICES; br=subrecord(rec,ids,ids)
    proof,div=certificate(K.extract(ids,ids),br,SCALAR_CHART)
    assert div==target_divisor('scalar')
    proof.update(original_indices=ids)
    save('physical_n0',proof);print('certified generic scalar',flush=True)
    other=[i for i in range(K.rows) if i not in ids]
    result,div=certify_blocks(K.extract(other,other),subrecord(rec,other,other),'generic scalar constraints')
    assert div.degrees()[2]<=0
    save('physical_n0_constraint',result)
    for n,z in ((2,False),(1,True),(0,True),(-1,True)):
        K,rec=read_matrix(OUT/('branch_'+raw_name(n,z) ))
        if z:K=real_charged_basis(K)
        proof,div=certificate(K,rec)
        name='spin2' if not z else {1:'Z+',-1:'Z-',0:None}[n]
        if name:assert div==target_divisor(name)
        else:assert div.degrees()[2]<=0
        save('physical_n'+str(n)+('Z' if z else ''),proof)

def special():
    for level,spins in (('hqd',(0,)),('h1f',(1,0)),('j1',(2,1,0))):
        for n in spins:
            representation='raw' if level=='j1' else 'fs'
            K,rec=read_matrix(OUT/('branch_'+representation+'_n'+str(n)+'.json'))
            B,br,residual=restrict(K,rec,level)
            if level!='j1':assert residual.is_zero_matrix
            result,div=certify_blocks(B,br,level)
            result.update(level=level,removed_equations_zero=(level!='j1'))
            save('physical_'+level+'_n'+str(n),result)
            print('certified',level,n,'rank',result['rank'],'degree',div.degrees()[2],flush=True)
    for n,z in SECTORS:
        K,rec=load_raw(n,z,True);B=on_branch(K,rec,torus=True)
        label='torus_n'+str(n)+('Z' if z else '')
        save(label,encode_matrix(B,rec,level='constant T2'))
        result,div=certify_blocks(real_charged_basis(B) if z else B,rec,label)
        save('physical_'+label,result)
        print('certified',label,'rank',result['rank'],'degree',div.degrees()[2],flush=True)

def chirality():
    from closed_forms import generic_targets
    from model import L,k,M2,P2,P3,P4
    from polynomial_matrix import rational
    for n,z in SECTORS:
        K,rec=load_raw(n,z);B=on_branch(K,rec,chi=-1)
        save('minus_'+raw_name(n,z)[:-5],encode_matrix(B,rec,chi=-1))
    level=4*L*(2*L-8+3*k*L-k*L**2)*P2**2*S*(S-1)/(P4*P3**2)
    for n,ids,chart,name in ((1,None,VECTOR_CHART,'vector'),(0,SCALAR_INDICES,SCALAR_CHART,'scalar')):
        K,rec=read_matrix(OUT/('minus_raw_n'+str(n)+'.json'))
        if ids is not None:K=K.extract(ids,ids);rec=subrecord(rec,ids,ids)
        proof,div=certificate(K,rec,chart)
        expected=rational(generic_targets()[name].subs(M2,level).subs(D,2-D))
        assert div==primitive_in_D(expected.num)
        save('physical_minus_n'+str(n),proof);print('chirality -1 certified',n,flush=True)

def torus_momentum():
    from closed_forms import generic_targets,torus
    from model import k,M2
    from polynomial_matrix import rational
    for n,z in SECTORS:
        K,rec=load_raw(n,z,True);B=on_branch(K,rec,torus=True,momentum=True)
        rec['harmonic_chart']='flat Fourier'
        label='torus_momentum_n'+str(n)+('Z' if z else '')
        save(label,encode_matrix(B,rec,harmonic_chart='flat Fourier',level='M2=-S**2/9'))
        proof,div=certify_blocks(real_charged_basis(B) if z else B,rec,label)
        name={2:'spin2',1:'vector',0:'scalar'}[n] if not z else {1:'Z+',0:None,-1:'Z-'}[n]
        if name:
            expected=rational(generic_targets()[name].subs(M2,-S**2/9).subs(k,torus))
            assert div==primitive_in_D(expected.num)
        else:assert div.degrees()[2]<=0
        save('physical_'+label,proof);print('flat Fourier',n,z,'certified',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--stage',choices=('raw','branches','generic','special','constant','chirality','torus_momentum','all'),required=True)
    args=p.parse_args();start=time.monotonic()
    for name,fn in (('raw',raw),('branches',branches),('generic',generic),('special',special),('chirality',chirality),('torus_momentum',torus_momentum)):
        if args.stage in (name,'all'):fn()
    if args.stage in ('constant','all'):
        from constant import derive
        save('constant',derive())
    print('seconds',round(time.monotonic()-start,2))
