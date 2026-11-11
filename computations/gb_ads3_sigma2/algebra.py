"""Zero-momentum bilinear-form engine for the 5d bosonic Lagrangian L_LR + lam L_GB on AdS3 x H2.

Background frame (anholonomic, constant structure constants):
  E_0=(z/l)d_t, E_1=(z/l)d_x, E_2=(z/l)d_z  (Poincare AdS3, radius l),  E_3=w y d_{y1}, E_4=w y d_{y2}  (H2, v=-w^2).
  [E_2,E_0]=E_0/l, [E_2,E_1]=E_1/l, [E_4,E_3]=w E_3.
Perturbations: phi-part ~ z^D y^S (amplitudes a_I), chi-part ~ z^(2-D) y^(1-S) (amplitudes b_I), both t,x,y1-independent.
The bilinear (a.b) part of sqrt(-g) L is scale invariant, so total derivatives vanish identically and
   [sqrt(-g) L]_{ab} = b^T K(D,S) a      (K = linearized field-equation operator on these modes).
Quantities are 'Pert' objects (bg, linear-a, linear-b, bilinear-ab); frame derivatives act by multiplication by the grade.
Conventions: paper's (mostly plus, eps^{01234}=+1, R^d_{cab}=E_a Gam^d_{bc}-..., R_{cb}=R^a_{cab})."""
import symengine as se, itertools
from functools import reduce

class P:
    __slots__=('z','a','b','ab')
    def __init__(s,z=0,a=0,b=0,ab=0): s.z,s.a,s.b,s.ab=se.sympify(z),se.sympify(a),se.sympify(b),se.sympify(ab)
    def __add__(s,o):
        o=o if isinstance(o,P) else P(o); return P(s.z+o.z,s.a+o.a,s.b+o.b,s.ab+o.ab)
    __radd__=__add__
    def __neg__(s): return P(-s.z,-s.a,-s.b,-s.ab)
    def __sub__(s,o): return s+(-(o if isinstance(o,P) else P(o)))
    def __rsub__(s,o): return (-s)+o
    def __mul__(s,o):
        if not isinstance(o,P):
            o=se.sympify(o); return P(s.z*o,se.expand(s.a*o),se.expand(s.b*o),se.expand(s.ab*o))
        z=s.z*o.z
        a=se.expand(s.z*o.a+s.a*o.z) if (s.a!=0 or o.a!=0) else se.Integer(0)
        b=se.expand(s.z*o.b+s.b*o.z) if (s.b!=0 or o.b!=0) else se.Integer(0)
        ab=0
        if s.z!=0 and o.ab!=0: ab+=s.z*o.ab
        if o.z!=0 and s.ab!=0: ab+=o.z*s.ab
        if s.a!=0 and o.b!=0: ab+=s.a*o.b
        if s.b!=0 and o.a!=0: ab+=s.b*o.a
        return P(z,a,b,se.expand(ab))
    __rmul__=__mul__
    def iszero(s): return s.z==0 and s.a==0 and s.b==0 and s.ab==0
ZERO=P()

def inv(X):
    z0=X.z; return P(1/z0,-X.a/z0**2,-X.b/z0**2,se.expand(-X.ab/z0**2+2*X.a*X.b/z0**3))
def sqrt1(X):  # sqrt of X with X.z>0
    s=se.sqrt(X.z); return P(s,X.a/(2*s),X.b/(2*s),se.expand(X.ab/(2*s)-X.a*X.b/(4*s**3)))

class Engine:
    def __init__(s,bg,D,S):
        """bg: dict with l,w,g,lam,L,N,p,h,r (exact numbers)."""
        s.bg=bg; l,w=bg['l'],bg['w']
        s.D,s.S=D,S
        # grade multipliers of frame derivatives
        s.ma={2:D/l,4:w*S}; s.mb={2:(2-D)/l,4:w*(1-S)}; s.mab={2:se.Integer(2)/l,4:w}
        C=[[[0]*5 for _ in range(5)] for _ in range(5)]   # C[c][a][b]: [E_a,E_b]=C^c_ab E_c
        C[0][2][0]=1/l; C[0][0][2]=-1/l; C[1][2][1]=1/l; C[1][1][2]=-1/l; C[3][4][3]=w; C[3][3][4]=-w
        s.Cs=C
        s.eta=[-1,1,1,1,1]
    def Ed(s,c,X):
        if c not in (2,4): return ZERO
        return P(0,se.expand(s.ma[c]*X.a),se.expand(s.mb[c]*X.b),se.expand(s.mab[c]*X.ab))

def perm_sign(p):
    s=1; p=list(p)
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: s=-s
    return s
EPS={p:perm_sign(p) for p in itertools.permutations(range(5))}
