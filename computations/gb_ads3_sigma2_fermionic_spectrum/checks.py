"""Read-only item-26 verification; --write-log writes this package's reports."""
import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
import platform
import time
import numpy as np
import sympy as sp
import scipy
from scipy.optimize import linear_sum_assignment
from backend import HERE,ROOT,unpack,total,prediction,mode,lr_polynomial,gauge_at
from polynomial import value,scaled_error,extract,distance_multiset,action_rank_certificate
from matching import match,negative_controls
from test_polynomial import run as polynomial_regressions
from certificates import assert_certificate_close, validate_root_certificates

OUT=HERE/"outputs"

def read(path):
    return json.loads(path.read_text())

def roots_list(records):
    return [complex(*x["root"]) for x in records for _ in range(x["multiplicity"])]


def load_sector(path):
    d=read(path);C=np.asarray([unpack(x) for x in d["coefficients"]])
    validate_root_certificates(d, path.name, C.shape[1])
    return d,C


def fresh_sector(path):
    d,C=load_sector(path)
    k=float(sp.Rational(d["k"]))
    scale=max(1.,min(2000.,1/max(abs(k),1e-3))) if k else 1.
    fresh,info=extract(C,seed=2030,projections=4,scale=max(1.,scale*.73))
    error=distance_multiset(roots_list(fresh),roots_list(d["roots"]))
    if error>1e-6:
        raise AssertionError(("independent extraction changed roots",path.name,error))
    expected=C.shape[1]-(2 if abs(sp.Rational(d["n"]))==sp.Rational(1,2) else 0)
    if info["generic_rank"]!=expected or any(r!=expected for r in info["probe_ranks"]):
        raise AssertionError(("generic rank",path.name))
    # This point is absent from all interpolation grids, holdouts, rank probes
    # and saved item-25 samples. It calls the action, not a stored matrix.
    z=-.63+1.17j
    K=total(d["L"],d["k"],d["g"],sp.Rational(d["n"]),d["q_R"],z,d["S"])
    residual=scaled_error(K,value(C,z))
    if residual>2e-9:
        raise AssertionError(("fresh action holdout",path.name,residual))
    gauge_residual=None
    if abs(sp.Rational(d["n"]))==sp.Rational(1,2):
        G,projection=gauge_at(d["L"],d["k"],d["g"],sp.Rational(d["n"]),d["q_R"],z,d["S"])
        sg=np.linalg.svd(G,compute_uv=False)
        gauge_residual=float(np.linalg.norm(K@G)/(np.linalg.norm(K)*np.linalg.norm(G)))
        if gauge_residual>2e-10 or max(projection)>2e-10 or sg[-1]/sg[0]<1e-8:
            raise AssertionError(("fresh SUSY kernel",path.name,gauge_residual,projection))
    for root,check in zip(d["roots"],d["direct_root_checks"]):
        recalculated=action_rank_certificate(C,complex(*root["root"]),expected,root["multiplicity"],
                                            check["singular_values"],check["action_interpolant_disagreement"])
        assert_certificate_close(recalculated, check, f"{path.name}.root[{root['root']}]")
        check=recalculated
        if check["resolved_extra_nullity"]!=root["multiplicity"]:
            raise AssertionError(("direct action multiplicity",path.name))
        if check["coefficient_scaled_disagreement"]>2e-9:
            raise AssertionError(("direct action discrepancy",path.name))
        gap=check["retained_gap_over_error_budget"]
        if gap is not None and gap<20:
            raise AssertionError(("unresolved direct-action gap",path.name))
    return dict(sector_file=path.name,independent_root_difference=error,
                fresh_action_holdout_error=residual,fresh_SUSY_kernel_error=gauge_residual)

def sample_checks():
    records=[]
    for path in sorted(OUT.glob("*.json")):
        d=read(path)
        if not ("direct_modes" in d and "sector_files" in d):continue
        p=d["parameters"]
        predicted,metadata=prediction(p["L"],p["k"],p["S"])
        positive=[];negative=[]
        for name in d["sector_files"]:
            sec=read(OUT/name);destination=positive if sp.Rational(sec["n"])>0 else negative
            for root in sec["roots"]:
                destination.extend([mode(sp.Rational(sec["n"]),complex(*root["root"]),sec["q_R"])
                                    for _ in range(root["multiplicity"])])
        a=match(predicted,positive);b=match(predicted,negative)
        match(positive,d["direct_modes"])
        if metadata!=d["background"]:
            raise AssertionError(("background metadata",path.name))
        records.append(dict(sample=d["sample"],modes=len(positive),
                            positive_sector_matching=a["maximum_error"],
                            negative_sector_matching=b["maximum_error"]))
    if len(records)!=18:
        raise AssertionError(("expected eighteen completed sample records",len(records)))
    return records

def small_k():
    reference=read(OUT/"k0_H2_3_s13.json")["direct_modes"]
    records=[]
    for label,k in [("H2_3_1o10",.1),("H2_3_1o100",.01),("H2_3_1o1000",.001)]:
        modes=read(OUT/(label+".json"))["direct_modes"]
        costs=np.full((len(reference),len(modes)),1e100)
        for i,a in enumerate(reference):
            for j,b in enumerate(modes):
                if a["spin"]==b["spin"] and a["q_R"]==b["q_R"]:
                    costs[i,j]=abs(complex(*a["energy"])-complex(*b["energy"]))
        rows,cols=linear_sum_assignment(costs)
        if len(rows)!=12 or np.max(costs[rows,cols])>1:
            raise AssertionError(("light-mode assignment",label))
        heavy=[m for j,m in enumerate(modes) if j not in set(cols)]
        if len(heavy)!=8:raise AssertionError(("heavy count",label))
        error=float(np.max(costs[rows,cols]))
        products=[k*complex(*m["energy"]).real for m in heavy]
        records.append(dict(k=k,light_modes=12,heavy_modes=8,
                            maximum_light_deviation=error,light_deviation_over_k=error/k,
                            heavy_k_ReDelta=products,maximum_heavy_limit_error=max(abs(x-1.6) for x in products)))
    if not all(records[i+1]["maximum_light_deviation"]<records[i]["maximum_light_deviation"]
               and records[i+1]["maximum_heavy_limit_error"]<records[i]["maximum_heavy_limit_error"] for i in (0,1)):
        raise AssertionError("Small-k deviations do not decrease")
    from backend import bosonic_forms as f,bosonic_model as m
    limit=sp.simplify(sp.limit(m.k*f.nuf,m.k,0))
    if sp.simplify(limit-8/(m.L+2))!=0:raise AssertionError("heavy scale formula")
    return dict(direct_fermion_samples=records,analytic_bosonic_prediction=str(limit),
                scope="three direct L=3 samples; finite-sample O(k) evidence, not a uniform all-level limit")

def exact_torus():
    D=sp.Symbol("D")
    out=[]
    for n in ("1/2","3/2"):
        _,K,_,_,_=lr_polynomial("4","0","1",n,1,"0")
        generic=K.rank()
        for root,want in [(sp.Rational(1,2),7),(sp.Rational(5,2),6)] if n=="1/2" else [(sp.Rational(3,2),1)]:
            actual=K.subs(D,root).rank()
            if actual!=want:raise AssertionError(("exact T2 rank",n,root,actual,want))
            out.append(dict(n=n,D=str(root),generic_rank=generic,root_rank=actual))
    return out

def source_checks():
    manifest=read(HERE/"source_manifest.json")
    for name,want in manifest["repository_inputs"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=want:
            raise AssertionError(("repository input changed",name))
    for name,want in manifest["implementation_hashes"].items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=want:
            raise AssertionError(("implementation changed",name))
    return dict(repository_inputs=len(manifest["repository_inputs"]),
                implementation_files=len(manifest["implementation_hashes"]))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers",type=int,default=2)
    ap.add_argument("--stored-only",action="store_true",help="skip fresh action/projection checks; scoped quick review")
    ap.add_argument("--write-log",action="store_true")
    args=ap.parse_args();start=time.monotonic()
    sources=source_checks();print("PASS source and implementation fingerprints",flush=True)
    controls=negative_controls();regressions=polynomial_regressions()
    print("PASS matching and polynomial extraction regressions",flush=True)
    samples=sample_checks();print("PASS all eighteen fixed-charge bijections, positive and negative boost sectors",flush=True)
    torus=exact_torus();limits=small_k()
    print("PASS exact constant-T2 rank/multiplicity checks and direct small-k comparison",flush=True)
    sector_paths=[p for p in sorted(OUT.glob("*.json")) if "coefficients" in read(p)]
    if len(sector_paths)!=144:raise AssertionError(("expected 144 sector records",len(sector_paths)))
    for path in sector_paths:
        load_sector(path)
    print("PASS complete per-root certificate evidence",flush=True)
    fresh=[]
    if not args.stored_only:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            for index,r in enumerate(pool.map(fresh_sector,sector_paths),1):
                fresh.append(r)
                if index%24==0:print(f"PASS {index}/144 independent source holdouts and new projection seed",flush=True)
    report=dict(scope="finite numerical item-26 spectra; no all-coupling symbolic completeness claim",
                mode="stored-only" if args.stored_only else "fresh-action-holdouts",
                versions=dict(python=platform.python_version(),numpy=np.__version__,sympy=sp.__version__,scipy=scipy.__version__),
                sources=sources,matching_controls=controls,polynomial_regressions=regressions,
                samples=samples,exact_torus_ranks=torus,small_k=limits,fresh_sector_checks=fresh,
                elapsed_seconds=time.monotonic()-start,status="PASS")
    print(f"PASS item 26: 144 sector polynomials, 18 samples, {len(fresh)} fresh action checks",flush=True)
    if args.write_log:
        if args.stored_only:raise ValueError("Canonical verification log requires fresh action checks")
        (OUT/"verification.json").write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
        (OUT/"small_k.json").write_text(json.dumps(limits,indent=2,allow_nan=False)+"\n")
        (OUT/"verification.log").write_text(
            "PASS source and implementation fingerprints\nPASS matching and polynomial negative/positive controls\n"
            "PASS 18 positive/negative sector mode bijections\nPASS exact T2 ranks and small-k checks\n"
            "PASS 144 fresh action holdouts and independently projected root sets\n"
            f"PASS item 26; elapsed {report['elapsed_seconds']:.1f}s\n")

if __name__=="__main__":main()
