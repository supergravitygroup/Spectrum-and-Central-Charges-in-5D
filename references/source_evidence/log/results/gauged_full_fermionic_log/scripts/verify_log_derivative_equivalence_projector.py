"""Eliminate gamma-traceless R(Q) residuals using its exact algebraic projector."""
# ASSERT_CONVENTION: metric_signature=mostly-plus
import ast,json,pickle,sys,time
import verify_log_derivative_equivalence as e
from verify_log_derivative_equivalence_identities import run as identity_reduce
b,q,p,h=e.b,e.q,e.p,e.h
F,A,P,Q,I=e.F,e.A,e.P,e.Q,e.I
b.spec['RpQ']=('llsu',Q(3,2),1);b.symbols['RpQ']="R'(Q)"
old_sym=q.symmetry
q.symmetry=lambda name,nd,nix:old_sym('RQ' if name=='RpQ' else name,nd,nix)
q._tensor_canon.cache_clear()
source=open(q.__file__).read();tree=ast.parse(source)
src=ast.get_source_segment(source,next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='reduce_clifford'))
src=src.replace("slot=='phi'","any(x.startswith('s') for x in p.FREE[slot])").replace("('hatF','ten','RV','RQ','RMB')","('hatF','ten','RV','RQ','RMB','Hdual','RpQ')")
exec(src,q.__dict__)
T=F('RpQ','-lA','-lB','-sE','+uI')
T+=Q(1,3)*F('g1','-lA','-sE','+sX')*F('g1','+lC','-sX','+sY')*F('RpQ','-lB','-lC','-sY','+uI')
T-=Q(1,24)*F('g1','-lA','-sE','+sX')*F('g1','-lB','-sX','+sY')*F('g2','+lC','+lD','-sY','+sZ')*F('RpQ','-lC','-lD','-sZ','+uI')
T-=Q(1,3)*F('g1','-lB','-sE','+sX')*F('g1','+lC','-sX','+sY')*F('RpQ','-lA','-lC','-sY','+uI')
T+=Q(1,24)*F('g1','-lB','-sE','+sX')*F('g1','-lA','-sX','+sY')*F('g2','+lC','+lD','-sY','+sZ')*F('RpQ','-lC','-lD','-sZ','+uI')
FREE=('-lA','-lB','-sE','+uI')
def substitute(pol):
 out=P()
 for c,fs in pol.ts:
  term=P(c)
  for f in fs:
   if f.name!='RQ':term*=P(f);continue
   pre,ff=b.variance_lower(b.replace(f,ds=()))
   val=pre*h.alpha_copy(T,{old[1:]:new[1:] for old,new in zip(FREE,ff.ix)})
   for d in reversed(f.ds):val=b.vec(d,val)
   term*=val
  out+=term
 return out

def run(folder,slot):
 e.OUT=e.s.OUT/'equivalence'/folder;q.OUT=e.OUT
 path=e.OUT/(slot+'-identity-residual.pkl')
 if not path.exists():path=e.OUT/(slot+'-residual.pkl')
 pol=pickle.load(path.open('rb'));projected=e.canon(substitute(pol),slot)
 save=e.OUT/(slot+'-projector-residual.pkl');pickle.dump(projected,save.open('wb'))
 report={'slot':slot,'input_residual_terms':len(pol.ts),'after_exact_RQ_projector_terms':len(projected.ts),'projector_source':'R(Q)_ab=Rprime(Q)_ab-i gamma_a phi_b+i gamma_b phi_a, with phi=i gamma^c Rprime(Q)_ac/3-i gamma_a gamma^cd Rprime(Q)_cd/24; conventional gamma trace constraint'}
 (e.OUT/(slot+'-projector.json')).write_text(json.dumps(report,indent=2)+'\n');print(report,flush=True)
 if projected.ts:identity_reduce(slot,'-projector')
if __name__=='__main__':
 for slot in sys.argv[2:] or ['N','E']:run(sys.argv[1] if len(sys.argv)>1 else 'covariant',slot)
