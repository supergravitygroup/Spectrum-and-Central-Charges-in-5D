"""Exact common full-covariant basis comparison, with no connection expansion.

Undo pre-gauge composites, differentiate before evaluating gauges, then compare
with frozen original canonical slots subjected only to elementary gauge values.
Neither side contains f_ab or primed Ricci; their old symmetry bug cannot enter.
"""
# ASSERT_CONVENTION: metric_signature=mostly-plus
import json,pickle,sys,time,hashlib
import verify_log_derivative_equivalence as e
from verify_log_derivative_equivalence_identities import run as identity_reduce
b,q,p,h=e.b,e.q,e.p,e.h
BASEOUT=e.OUT;OUT=BASEOUT/'covariant';OUT.mkdir(exist_ok=True);e.OUT=OUT;q.OUT=OUT

def run(slot):
 start=time.time();limit=1 if slot=='phi' else 2
 currentpath=e.s.OUT/(slot+'-canonical.pkl');current=pickle.load(currentpath.open('rb'))
 mapped=e.s.gauge_values(e.undo(current,limit))
 sourcepath=h.SOURCE_OUT/(slot+'-clifford.pkl');source=pickle.load(sourcepath.open('rb'))
 original=e.s.gauge_values(source)
 assert not any(f.name in ('fcon','RpRic','scon','grav','ginv') for pol in (mapped,original) for c,fs in pol.ts for f in fs)
 pickle.dump(mapped,(OUT/(slot+'-common-current.pkl')).open('wb'))
 pickle.dump(original,(OUT/(slot+'-common-source.pkl')).open('wb'))
 delta=e.canon(mapped-original,slot)
 pickle.dump(delta,(OUT/(slot+'-residual.pkl')).open('wb'))
 report={'slot':slot,'mapped_terms':len(mapped.ts),'original_gauge_terms':len(original.ts),'exact_tensor_clifford_residual_terms':len(delta.ts),'source_sha256':hashlib.sha256(sourcepath.read_bytes()).hexdigest(),'current_sha256':hashlib.sha256(currentpath.read_bytes()).hexdigest(),'seconds':time.time()-start,'scope':'exact full-covariant standard-Weyl comparison; no connection expansion and no f/Ricci symmetry assumption'}
 (OUT/(slot+'-report.json')).write_text(json.dumps(report,indent=2)+'\n');print(report,flush=True)
 if delta.ts:identity_reduce(slot)
if __name__=='__main__':
 for slot in sys.argv[1:] or ['L','phi','N','E']:run(slot)
