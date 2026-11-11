"""Rebuild LOG with full supercovariant derivatives, before gauge evaluation.

Never relabel the ordinary-connection Step-7 output. Substitute the complete
gauged composite identities into the frozen full-derivative canonical input,
differentiate, and only then apply elementary gauge values. Covariant jets of
the fixed scalar/dilatino survive. No connection expansion is used here.
"""
import ast, inspect, json, pickle, time
from collections import Counter
import log_step7_gauge as h
import log_step7_constraints as constraints

b,q,p=h.b,h.q,h.p
P,Q,I,A,F=b.P,b.Q,b.I,b.A,b.field
BASE=h.BASE
OUT=BASE/'sources/step7/supercovariant'
OUT.mkdir(exist_ok=True)
q.OUT=OUT
for name,spec,symbol in [
 ('Hdual',('ll',Q(3),0),r'\widehat H'),
 ('compPhi',('su',Q(7,2),1),r'\varphi_c'),
 ('compN',('',Q(4),0),'N_c')]:
    b.spec[name]=spec;b.symbols[name]=symbol
b.symbols.update(rho=r'\sigma',lam=r'\psi',hatF=r'\widehat G')
old_sym=q.symmetry
def symmetry(name,nd,nix):
    return old_sym('ten' if name=='Hdual' else name,nd,nix)
q.symmetry=symmetry
src=inspect.getsource(q.two_form_wedge).replace("('ten','hatF')","('ten','hatF','Hdual')")
exec(src,q.__dict__)
source=__import__('pathlib').Path(q.__file__).read_text()
src=ast.get_source_segment(source,next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='reduce_clifford'))
src=src.replace("slot=='phi'", "any(x.startswith('s') for x in p.FREE[slot])")
src=src.replace("('hatF','ten','RV','RQ','RMB')","('hatF','ten','RV','RQ','RMB','Hdual')")
exec(src,q.__dict__)

def vec(a,pol):
    # Kernel's power rule emits source W. Here W is the component sigma.
    raw=b.vec(a,pol)
    return P.terms([(c,tuple(b.replace(f,name='rho') if f.name=='W' else f for f in fs)) for c,fs in raw.ts])

def bil(left,right,blade=()):
    # Both spinors have lower spinor indices; kernel = C Gamma.
    kernel=F('g'+str(len(blade)),*blade,'+sX','+sY') if blade else F('eps','+sX','+sY')
    return -kernel*left*right

def templates():
    r=b.pw;g=F('gc')
    la=lambda s,i:F('lam',s,i)
    Y=I*Q(1,4)*r(-1)*bil(la('-sX','+uI'),la('-sY','+uJ'))-Q(1,2)*g*r(-1)*F('Lc','+uI','+uJ')
    T=Q(1,8)*r(-1)*F('hatF','-lA','-lB')-Q(1,4)*r(-2)*F('Hdual','-lA','-lB')
    T+=I*Q(1,32)*r(-2)*bil(la('-sX','+uI'),la('-sY','-uI'),('-lA','-lB'))
    chi=I*Q(1,8)*r(-1)*F('g1','+lA','-sE','+sX')*A('lam',('-sX','+uI'),('-lA',))
    chi+=I*Q(1,16)*r(-2)*F('g1','+lA','-sE','+sX')*A('rho',ds=('-lA',))*la('-sX','+uI')
    chi+=-Q(1,32)*r(-2)*F('hatF','-lA','-lB')*F('g2','+lA','+lB','-sE','+sX')*la('-sX','+uI')
    chi+=Q(1,4)*r(-1)*F('ten','-lA','-lB')*F('g2','+lA','+lB','-sE','+sX')*la('-sX','+uI')
    chi+=-Q(1,16)*g*r(-3)*F('Lc','+uI','+uJ')*la('-sE','-uJ')+Q(1,8)*g*r(-2)*F('compPhi','-sE','+uI')
    # Cubic chi and quartic D cannot reach the authorized total degree.
    D=Q(1,4)*r(-1)*A('rho',ds=('+lA','-lA'))+Q(1,8)*r(-2)*A('rho',ds=('-lA',))*A('rho',ds=('+lA',))
    D+=-Q(1,16)*r(-2)*F('hatF','-lA','-lB')*F('hatF','+lA','+lB')
    D+=-Q(1,8)*r(-2)*bil(la('-sX','+uI'),A('lam',('-sY','-uI'),('-lA',)),('+lA',))
    D+=Q(1,4)*r(-2)*F('aux','+uI','+uJ')*F('aux','-uI','-uJ')
    D+=I*Q(1,4)*r(-2)*F('ten','-lA','-lB')*bil(la('-sX','+uI'),la('-sY','-uI'),('+lA','+lB'))
    D+=-4*I*r(-1)*bil(la('-sX','+uI'),F('chi','-sY','-uI'))
    D+=-Q(26,3)*F('ten','-lA','-lB')*F('ten','+lA','+lB')+2*r(-1)*F('hatF','-lA','-lB')*F('ten','+lA','+lB')
    D+=Q(1,4)*g*r(-2)*F('compN')
    return {'aux':(Y,('+uI','+uJ')),'ten':(T,('-lA','-lB')),'chi':(chi,('-sE','+uI')),'auxD':(D,())}
TEMPLATES=templates()

def substitute_atom(f,limit):
    if f.name not in TEMPLATES:return P(f)
    pre,ff=b.variance_lower(b.replace(f,ds=()))
    template,free=TEMPLATES[f.name]
    value=h.alpha_copy(template,{old[1:]:new[1:] for old,new in zip(free,ff.ix)})
    value=pre*substitute(value,limit)
    for derivative in reversed(f.ds):value=vec(derivative,value)
    return p.retained(value,limit)

def substitute(pol,limit):
    out=[]
    for c,fs in pol.ts:
        term=P(c)
        for f in fs:term=p.retained(term*substitute_atom(f,limit),limit)
        out.extend(term.ts)
    return P.terms(out)

def gauge_values(pol):
    terms=[]
    for c,fs in pol.ts:
        if any((f.name=='lam' and not f.ds) or (f.name=='rho' and len(f.ds)==1) for f in fs):continue
        terms.append((c,tuple(f for f in fs if not (f.name=='pow' or (f.name=='rho' and not f.ds)))))
    return P.terms(terms)

def canonical(pol,slot,suffix=''):
    tensor,zeros=q.collect_tensor(pol,slot)
    result,expanded,cliffzeros=q.collect_clifford(tensor,slot,checkpoint_suffix=suffix)
    reductions=[]
    for _ in range(6):
        result,stats=constraints.reduce(result,slot);reductions.append(stats)
        if not stats:break
    else:raise AssertionError('constraints did not stabilize')
    return q.collect_tensor(result,slot)[0],{'tensor_terms':len(tensor.ts),'tensor_zeros':zeros,'clifford_expansion_terms':expanded,'clifford_zeros':cliffzeros,'constraint_reductions':reductions}

def audit(pol,slot):
    assert h.free_indices(pol)==p.FREE[slot]
    degrees=Counter()
    dims={'rho':Q(0),'lam':Q(1,2),'gc':Q(1),'Lc':Q(0),'hatF':Q(1),'Hdual':Q(1),'compPhi':Q(1,2),'compN':Q(1)}
    for c,fs in pol.ts:
        assert not any(f.name in TEMPLATES or f.name in ('grav','scon','fcon','pow','W') for f in fs)
        assert not any(f.oddD for f in fs)
        assert not any((f.name=='lam' and not f.ds) or (f.name=='rho' and len(f.ds)<2) for f in fs)
        degree=sum(f.parity for f in fs);assert degree in ((1,) if slot=='phi' else (0,2))
        dimension=sum(dims.get(f.name,b.spec[f.name][1])+len(f.ds) for f in fs)
        assert dimension==p.WEIGHTS[slot],(slot,dimension,fs)
        degrees[degree]+=1
    return dict(degrees)

def main(slots):
    report_path=OUT/'canonicalization.json'
    report=json.loads(report_path.read_text()) if report_path.exists() else {}
    for slot in slots:
        start=time.time();source=pickle.load((h.SOURCE_OUT/(slot+'-clifford.pkl')).open('rb'))
        full=substitute(source,1 if slot=='phi' else 2)
        # Full conformal weights are tested before changing sigma's scale.
        b.check(full,p.WEIGHTS[slot],p.FREE[slot])
        raw=gauge_values(full)
        pickle.dump(raw,(OUT/(slot+'-substituted.pkl')).open('wb'))
        print(slot,'full-covariant',len(source.ts),'->',len(full.ts),'gauge',len(raw.ts),flush=True)
        result,stats=canonical(raw,slot)
        counts=audit(result,slot)
        pickle.dump(result,(OUT/(slot+'-canonical.pkl')).open('wb'))
        again,_=canonical(result,slot,'-check')
        diff=q.collect_tensor(result-again,slot)[0]
        assert not diff.ts,(slot,len(diff.ts))
        report[slot]={'input_terms':len(source.ts),'full_substituted_terms':len(full.ts),'gauge_terms':len(raw.ts),'canonical_terms':len(result.ts),'fermion_degrees':counts,'conformal_weights_before_gauge':'PASS','indices_dimensions_parity_after_gauge':'PASS','canonical_idempotence':'exact zero coefficient residual',**stats,'seconds':time.time()-start}
        report_path.write_text(json.dumps(report,indent=2)+'\n')
        print(slot,report[slot],flush=True)

if __name__=='__main__':
    import sys
    main(sys.argv[1:] or ['L','phi','N','E'])
