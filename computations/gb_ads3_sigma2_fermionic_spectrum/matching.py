"""Fixed-label perfect matching; no choice of charge convention after a run."""
import numpy as np
from scipy.optimize import linear_sum_assignment

def match(predicted,observed,tolerance=1e-6):
    if len(predicted)!=len(observed):
        raise AssertionError(("mode count differs",len(predicted),len(observed)))
    if not predicted:return dict(pairs=[],maximum_error=0.)
    distance=np.full((len(predicted),len(observed)),np.inf)
    for i,p in enumerate(predicted):
        for j,o in enumerate(observed):
            if p['spin']==o['spin'] and p['q_R']==o['q_R']:
                distance[i,j]=abs(complex(*p['energy'])-complex(*o['energy']))
    allowed=distance<tolerance
    cost=np.where(allowed,distance,len(predicted)+1.)
    rows,cols=linear_sum_assignment(cost)
    if not all(allowed[i,j] for i,j in zip(rows,cols)):
        raise AssertionError("No spin/charge/multiplicity-preserving bijection")
    return dict(maximum_error=float(max(distance[rows,cols])),
                pairs=[dict(predicted=int(i),direct=int(j),energy_error=float(distance[i,j]))
                       for i,j in zip(rows,cols)])

def negative_controls():
    def m(s,d,q):return dict(spin=s,energy=[d,0.],q_R=q)
    base=[m(.5,2.3,1),m(.5,2.3,-1),m(1.5,3.2,1)]
    bad=[base[:-1],base+[base[0]], [base[0],base[0],base[2]],
         [m(.5,2.3,-1),base[1],base[2]], [m(1.5,2.3,1),base[1],base[2]],
         [m(.5,2.3001,1),base[1],base[2]]]
    for index,observed in enumerate(bad):
        try:match(base,observed)
        except AssertionError:continue
        raise AssertionError(("incorrect spectrum accepted",index))
    trap=[m(.5,2.,1),m(.5,2.+1.6e-6,1)]
    match(trap,[m(.5,2.+.9e-6,1),m(.5,2.-.5e-6,1)])
    match(base,base)
    return dict(rejected_incorrect_cases=len(bad),positive_controls=2)
