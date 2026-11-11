"""Symbolic BPS branch and dimension-preserving amplitude changes for item 24."""
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
L, k, D, S, g, w = s.symbols('L k D S g w')
M2 = s.Symbol('M2')
P1, P2, P3 = 2-k*L, 4-k*L, 2*L+4-k*L**2
P4, P5 = 8-4*k-4*k*L+k**2*L**2, 8+4*k-8*k*L+k**2*L**2
v = 2*g**2*L*(2*L-8+3*k*L-k*L**2)/P4
ell_s = s.sqrt(2)*P2/(g*P3)

def branch(chi=1):
    if chi not in (1, -1):
        raise ValueError('chi is a discrete chirality, +1 or -1')
    return dict(N=-g*L*P3/P2, p=g*L/s.sqrt(2),
                h=g*(L-2)/(s.sqrt(2)*P2), r=v,
                l=chi*ell_s, lam=k/g**2)

def raw_name(n, charged=False, fs=False):
    return f"{'fs' if fs else 'raw'}_n{n}{'Z' if charged else ''}.json"

def load_raw(n, charged=False, fs=False):
    record=json.loads((HERE/'outputs'/raw_name(n,charged,fs)).read_text())
    loc={name:s.Symbol(name) for name in 'L k D S g w N p h r l lam'.split()}
    K=s.Matrix([[s.sympify(e,locals=loc) for e in row] for row in record['K']])
    return K, record

def amplitude_scale(name, torus=False):
    field,comp=name.split('_')[1:]
    parity=(comp.count('3')+comp.count('4'))%2
    # V,Z,N have dimension one; all other independent frame amplitudes
    # have dimension zero. No value is assigned to g, k or L.
    unit=g/s.sqrt(2)
    scale=unit if field in ('V','Z','N') else s.Integer(1)
    if field in ('E','N'):
        scale*=s.sqrt(2)
    if not torus:
        scale*=(w/unit)**parity
    return scale

def on_branch(K, record, chi=1, torus=False, momentum=False):
    """Khat=2*Sb*K*Sa/g**2, over QQ(L,k)[D,S]; g stays symbolic throughout.

    w/(g/sqrt(2)) is real on H2. Sphere continuation retains its basis metric;
    the inverse congruence is required when reading physical residues.
    """
    sub={s.Symbol(key):value for key,value in branch(chi).items()}
    if torus:
        sub[s.Symbol('r')]=0
        sub[w]=0
    av,bv=record['avars'],record['bvars']
    def entry(i,j):
        base=K[i,j]
        if torus:
            base=base.subs(s.Symbol('r'),0)
            if momentum:
                # Flat Fourier chart: hold w*S=(g/sqrt(2))*S_flat fixed.
                # S_flat=3*i*M on the physical torus; M2=-S_flat**2/9.
                base=s.expand(base.subs(S,S*g/(s.sqrt(2)*w)))
            base=base.subs(w,0)
        expr=2*base*amplitude_scale(av[j],torus)*amplitude_scale(bv[i],torus)/g**2
        expr=s.expand(expr.subs(sub, simultaneous=True))
        expr=s.cancel(expr.subs(w**2,-v))
        if torus:
            expr=s.cancel(expr.subs(k,2*(L-4)/(L*(L-3))))
        if expr.has(w,g,s.sqrt(2)):
            raise AssertionError(('unremoved dimensional/basis factor',i,j,expr))
        return s.factor(expr)
    return s.Matrix(K.rows,K.cols,entry)

def encode_matrix(K,record,**metadata):
    return dict(metadata,avars=record['avars'],bvars=record['bvars'],
                K=[[str(e) for e in row] for row in K.tolist()])

def read_matrix(path):
    record=json.loads(Path(path).read_text())
    loc={name:s.Symbol(name) for name in 'L k D S g w N p h r l lam'.split()}
    return s.Matrix([[s.sympify(e,locals=loc) for e in row] for row in record['K']]),record
