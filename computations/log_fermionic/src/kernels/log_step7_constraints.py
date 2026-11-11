"""Apply conventional curvature constraints to the new gauged polynomials.

No field equations, derivative commutations, or integrations by parts.
The rank-two identities are derived from gamma^a R(Q)_ab=0.
"""
import pickle,json
from collections import Counter
import log_step7_gauge as h
q=h.q;b=h.b;p=h.p;A=h.A;P=h.P

def reduce_term(c,fs,slot,stats):
    for f in fs:
        if f.name=='RMB' and any(x[1:]==y[1:] for x in f.ix[:2] for y in f.ix[2:4]):
            stats['R(M) trace']+=1;return []
    paths,removed=q.spin_paths(fs,slot)
    for kind,sg,blocks,left,right in paths:
        if kind!='open' or len(blocks)!=1:continue
        blade=blocks[0]
        for endpoint,isleft in [(left,True),(right,False)]:
            if endpoint is None:continue
            fi=endpoint[0];f=fs[fi]
            if f.name!='RQ':continue
            pairs=[(j,k) for j,x in enumerate(blade) for k,y in enumerate(f.ix[:2]) if x[1:]==y[1:]]
            if not pairs:continue
            if len(blade)==1 or len(pairs)==2:
                stats['R(Q) gamma trace']+=1;return []
            assert len(blade)==2 and len(pairs)==1
            j,k=pairs[0];other=blade[1-j]
            assert blade[j][0]!=f.ix[k][0]
            # Right: gamma^(a c) R_ab=R^c_b. Left: opposite sign.
            fac=(-1 if isleft else 1)*(1 if j==0 else -1)
            new=list(fs);ix=list(f.ix);ix[k]=other;new[fi]=b.replace(f,ix=tuple(ix))
            new=[f for n,f in enumerate(new) if n not in removed]
            new=[b.replace(f,ix=tuple('-'+x[1:] if x[1]=='s' else x for x in f.ix)) if f.parity else f for f in new]
            if left is None:
                new.append(A('del',('-sE','+'+right[2][1:])))
                cc=c*sg*fac
            else:
                new.append(A('eps',('+'+left[2][1:],'+'+right[2][1:])))
                cc=-c*sg*fac
            stats['R(Q) rank-two reduction']+=1
            return [(cc,tuple(new))]
    return [(c,fs)]

def reduce(pol,slot):
    stats=Counter();terms=[]
    for c,fs in pol.ts:terms+=reduce_term(c,fs,slot,stats)
    out=q.collect_tensor(P.terms(terms),slot)[0]
    return out,dict(stats)

def main(slots):
    report={}
    for slot in slots:
        src=h.OUT/(slot+'-gauged.pkl')
        pol=pickle.load(src.open('rb'));out,stats=reduce(pol,slot)
        again,ss=reduce(out,slot)
        assert not ss,(slot,ss)
        assert h.free_indices(out)==p.FREE[slot]
        pickle.dump(out,(h.OUT/(slot+'-constrained.pkl')).open('wb'))
        report[slot]={'before':len(pol.ts),'after':len(out.ts),'reductions':stats}
        print(slot,report[slot],flush=True)
    path=h.OUT/'constraints.json'
    old=json.loads(path.read_text()) if path.exists() else {}
    path.write_text(json.dumps({**old,**report},indent=2)+'\n')

if __name__=='__main__':
    import sys
    main(sys.argv[1:] or ['L','phi','N','E'])
