"""Regenerate only this package's numerical spectrum records."""
import argparse
from concurrent.futures import ProcessPoolExecutor,as_completed
import hashlib
import json
import time
import tempfile
import inspect
from pathlib import Path
import numpy as np
import sympy as sp
from backend import HERE,ROOT,ACTION_DIR,SAMPLES,SECTORS,total,pack,unpack,mode,prediction,gauge_at,lr_polynomial,basis_record
from polynomial import fit,extract,value,scaled_error,distance_multiset,action_rank_certificate
from matching import match,negative_controls

OUT=HERE/"outputs"
EXTRA=[
    ("k0_H2_3_s13","3","0","1/3"),
    ("k0_H2_3_s14","3","0","1/4"),
    ("k0_H2_7o2","7/2","0","1/2"),
    ("k0_S2_5_j2","5","0","3"),
    ("k0_S2_5_j3","5","0","4"),
    ("k0_T2_constant","4","0","0"),
]
ALL_SAMPLES=SAMPLES+EXTRA

def sector_filename(label,n,q):
    sign="p" if n>0 else "m"
    return f"{label}_n{sign}{abs(int(2*n))}_q{q:+d}.json"

def flatten(records):
    return [complex(*r["root"]) for r in records for _ in range(r["multiplicity"])]

def compute_sector(spec):
    label,L,k,S,n,q=spec
    start=time.monotonic();g="1"
    evaluator=lambda z:total(L,k,g,n,q,z,S)
    # Explicit generation may cache its costly action interpolation in the
    # system temporary directory. The key includes all action source bytes,
    # the adapter, interpolation implementation, versions and input tuple.
    fingerprint=hashlib.sha256()
    for path in sorted(ACTION_DIR.glob("*.py")):
        fingerprint.update(path.read_bytes())
    action_sources=json.loads((ACTION_DIR/"source_manifest.json").read_text())
    for name in sorted(action_sources["repository_inputs"]):
        fingerprint.update(name.encode())
        fingerprint.update((ROOT/name).read_bytes())
    fingerprint.update((HERE/"backend.py").read_bytes())
    fingerprint.update(inspect.getsource(fit).encode())
    fingerprint.update(repr((spec,np.__version__,sp.__version__)).encode())
    cache=Path(tempfile.gettempdir())/"gb_item25_interpolations"
    cache.mkdir(exist_ok=True)
    cache_file=cache/(fingerprint.hexdigest()+".json")
    Ccheck=None
    if cache_file.exists():
        cached=json.loads(cache_file.read_text())
        C=np.asarray([unpack(x) for x in cached["coefficients"]])
        interp=cached["interpolation"]
        if cached.get("alternate_coefficients"):
            Ccheck=np.asarray([unpack(x) for x in cached["alternate_coefficients"]])
    else:
        C,interp=fit(evaluator)
    if label in (SAMPLES[0][0],"H2_3_1o1000") and n>0 and q==1 and Ccheck is None:
        Ccheck,other=fit(evaluator,count=7,phase=.41,radius=2.1)
        if Ccheck.shape!=C.shape or scaled_error(Ccheck,C)>2e-9:
            raise AssertionError(("two interpolation resolutions",label,n,q))
        interp["independent_grid"]=dict(coefficient_error=scaled_error(Ccheck,C),**other)
    cache_file.write_text(json.dumps(dict(coefficients=[pack(x) for x in C],interpolation=interp,
                                         alternate_coefficients=[pack(x) for x in Ccheck] if Ccheck is not None else None)))
    scale=max(1.,min(2000.,1/max(abs(float(sp.Rational(k))),1e-3))) if sp.Rational(k)!=0 else 1.
    roots,info=extract(C,seed=25,projections=4,scale=scale)
    expected_rank=C.shape[1]-(2 if abs(n)==sp.Rational(1,2) else 0)
    if info["generic_rank"]!=expected_rank or any(r!=expected_rank for r in info["probe_ranks"]):
        raise AssertionError(("unexpected generic rank",label,n,q,info))
    alternate,altinfo=extract(C,seed=109,projections=4,scale=max(1.,scale/2))
    discrepancy=distance_multiset(flatten(roots),flatten(alternate))
    if discrepancy>1e-6:
        raise AssertionError(("independent projections/scale",label,n,q,discrepancy))
    if Ccheck is not None:
        gridroots,_=extract(Ccheck,seed=71,projections=4,scale=scale)
        griddifference=distance_multiset(flatten(roots),flatten(gridroots))
        if griddifference>1e-6:
            raise AssertionError(("root energies vary across interpolation grids",griddifference))
        interp["independent_grid"]["maximum_root_difference"]=griddifference
    direct=[]
    for root in roots:
        z=complex(*root["root"]);K=evaluator(z)
        sv=np.linalg.svd(K,compute_uv=False)
        r=info["generic_rank"]
        disagreement=float(np.linalg.norm(K-value(C,z),2))
        direct.append(action_rank_certificate(C,z,r,root["multiplicity"],sv,disagreement))
    gauge=[]
    if abs(n)==sp.Rational(1,2):
        matrices=[]
        for z in [.37+.11j,-1.2+.8j]:
            G,projection=gauge_at(L,k,g,n,q,z,S);K=evaluator(z)
            sg=np.linalg.svd(G,compute_uv=False)
            residual=float(np.linalg.norm(K@G)/(np.linalg.norm(K)*np.linalg.norm(G)))
            if residual>2e-10 or max(projection)>2e-10 or sg[-1]/sg[0]<1e-8:
                raise AssertionError(("SUSY kernel",label,n,q,residual,projection))
            matrices.append(K)
            gauge.append(dict(D=[z.real,z.imag],columns=pack(G),residual=residual,
                              basis_residual=max(projection),column_singular_values=sg.tolist()))
        stacked=np.linalg.svd(np.vstack(matrices),compute_uv=False)
        info["kernel_intersection_at_two_D"]=int((stacked<1e-10*stacked[0]).sum())
    _,_,a,b,_=lr_polynomial(L,k,g,str(n),q,S)
    return dict(sample=label,L=L,k=k,g=g,S=S,n=str(n),q_R=q,
                method="complex128 action evaluation; D-polynomial and numerical determinantal roots",
                coefficients=[pack(c) for c in C],degree=len(C)-1,
                basis_a=basis_record(a),basis_b=basis_record(b),
                interpolation=interp,rank_and_projections=info,roots=roots,
                direct_root_checks=direct,gauge_checks=gauge,
                independent_seed_and_scale=dict(maximum_root_difference=discrepancy,**altinfo),
                elapsed_seconds=time.monotonic()-start)

def write(path,data):
    path.write_text(json.dumps(data,indent=2,allow_nan=False)+"\n")

def combine(spec):
    label,L,k,S=spec
    sectors=[json.loads((OUT/sector_filename(label,n,q)).read_text()) for n,q in SECTORS]
    observed=[]
    for sec in sectors:
        if sp.Rational(sec["n"])<0:continue
        for root in sec["roots"]:
            observed.extend([mode(sp.Rational(sec["n"]),complex(*root["root"]),sec["q_R"])
                             for _ in range(root["multiplicity"])])
    expected,meta=prediction(L,k,S)
    result=match(expected,observed)
    if len(expected)!=(14 if label=="k0_T2_constant" else 12 if k=="0" else 20):
        raise AssertionError(("unexpected prediction count",label,len(expected)))
    data=dict(sample=label,parameters=dict(L=L,k=k,g="1",S=S),background=meta,
              physical_level=label!="H2_5_1_algebraic",
              direct_modes=observed,predicted_modes=expected,matching=result,
              sector_files=[sector_filename(label,n,q) for n,q in SECTORS])
    write(OUT/(label+".json"),data)
    print(f"PASS {label}: {len(observed)} modes; matching error {result['maximum_error']:.3e}",flush=True)
    return data

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sample",choices=[s[0] for s in ALL_SAMPLES])
    ap.add_argument("--workers",type=int,default=2)
    ap.add_argument("--resume",action="store_true",help="reuse existing per-sector records; hashes checked separately")
    args=ap.parse_args();OUT.mkdir(exist_ok=True)
    from checks import source_checks
    source_checks()
    selected=[s for s in ALL_SAMPLES if args.sample in (None,s[0])]
    jobs=[(*s,n,q) for s in selected for n,q in SECTORS
          if not args.resume or not (OUT/sector_filename(s[0],n,q)).exists()]
    failures=[]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        pending={pool.submit(compute_sector,job):job for job in jobs}
        for future in as_completed(pending):
            job=pending[future]
            try:
                result=future.result()
            except Exception as error:
                failures.append((str(job),repr(error)))
                print("FAIL",job,repr(error),flush=True)
                continue
            write(OUT/sector_filename(job[0],job[-2],job[-1]),result)
            print(f"WROTE {job[0]} n={job[-2]} q={job[-1]} ({result['elapsed_seconds']:.1f}s)",flush=True)
    if failures:
        raise RuntimeError(failures)
    combined=[combine(s) for s in selected]
    if args.sample is None:
        write(OUT/"table.json",dict(samples=[dict(sample=r["sample"],**r["parameters"],**r["background"],
                    modes=len(r["direct_modes"]),maximum_matching_error=r["matching"]["maximum_error"]) for r in combined],
                    comparator_controls=negative_controls()))

if __name__=="__main__":main()
