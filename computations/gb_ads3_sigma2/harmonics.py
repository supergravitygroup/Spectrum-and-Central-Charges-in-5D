"""Restricted harmonic spaces; no generic-level M=0 shortcut."""
import sympy as s
from model import S

def change_trace(K,record):
    av,bv=list(record['avars']),list(record['bvars'])
    A=s.eye(len(av)); B=s.eye(len(bv))
    if 'a_h_33' in av:
        for names,T,prefix in ((av,A,'a'),(bv,B,'b')):
            i,j=names.index(prefix+'_h_33'),names.index(prefix+'_h_44')
            T[i,i]=T[j,i]=T[i,j]=1; T[j,j]=-1
            names[i],names[j]=prefix+'_h_t',prefix+'_h_u'
    return B.T*K*A,dict(avars=av,bvars=bv)

def kind(name):
    _,field,comp=name.split('_')
    if field=='h' and comp in ('u','34'):return 'tensor'
    return 'vector' if (comp.count('3')+comp.count('4'))==1 else 'scalar'

def restrict(K,record,level):
    """Return restricted matrix and the equations in discarded row types.

    h1f/hqd consistency is checked exactly. For j1 the tensor harmonic itself
    is absent, so its putative equations are not equations of this level.
    """
    definitions={'h1f':(1,{'vector','tensor'}),
                 'hqd':(2,{'tensor'}),'j1':(-1,{'scalar','vector'})}
    sigma,keep=definitions[level]
    K,rec=change_trace(K.subs(S,sigma),record)
    rows=[i for i,x in enumerate(rec['bvars']) if kind(x) in keep]
    cols=[j for j,x in enumerate(rec['avars']) if kind(x) in keep]
    dropped=[i for i in range(K.rows) if i not in rows]
    residual=K.extract(dropped,cols).applyfunc(s.cancel)
    return K.extract(rows,cols),dict(avars=[rec['avars'][j] for j in cols],
        bvars=[rec['bvars'][i] for i in rows]),residual
