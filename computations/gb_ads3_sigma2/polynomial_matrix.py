"""Exact polynomial matrices and rational functions over QQ[L,k,D,S], using FLINT.

No sampling or numerical rank tolerance. Division is checked to be exact.
"""
import sympy as s
from functools import lru_cache
from flint import fmpq, fmpq_mpoly_ctx
from model import L,k,D,S

VARIABLES=(L,k,D,S)
CTX=fmpq_mpoly_ctx.get([str(v) for v in VARIABLES])
ZERO=CTX.constant(0)
ONE=CTX.constant(1)

class Fraction:
    """Reduced rational function with cross-cancellation before products."""
    __slots__=('num','den')
    def __init__(self,num=ZERO,den=ONE,reduce=True):
        if isinstance(num,int): num=CTX.constant(num)
        if not den: raise ZeroDivisionError
        if reduce:
            d=num.gcd(den); num,den=num/d,den/d
        if not num:
            num,den=ZERO,ONE
        else:
            unit=den.leading_coefficient()
            num,den=num/unit,den/unit
        self.num,self.den=num,den
    def __bool__(self):return bool(self.num)
    def __neg__(self):return Fraction(-self.num,self.den,False)
    def __add__(self,other):
        if not isinstance(other,Fraction):other=Fraction(other)
        d=self.den.gcd(other.den); a=self.den/d; b=other.den/d
        n=self.num*b+other.num*a; t=n.gcd(d)
        return Fraction(n/t,a*(other.den/t),False)
    __radd__=__add__
    def __sub__(self,other):return self+(-other)
    def __mul__(self,other):
        if not isinstance(other,Fraction):other=Fraction(other)
        a=self.num.gcd(other.den); b=other.num.gcd(self.den)
        return Fraction((self.num/a)*(other.num/b),(self.den/b)*(other.den/a),False)
    __rmul__=__mul__
    def __truediv__(self,other):
        if not isinstance(other,Fraction):other=Fraction(other)
        return self*Fraction(other.den,other.num,False)
    def size(self):return len(self.num)+len(self.den)
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError(n)
        if n<0:return Fraction(self.den**(-n),self.num**(-n),False)
        return Fraction(self.num**n,self.den**n,False)

@lru_cache(maxsize=8192)
def rational(e):
    """Evaluate an expression tree without expanding a product of fractions."""
    e=s.sympify(e)
    if e.is_Rational:return Fraction(CTX.constant(fmpq(str(e))))
    if e in VARIABLES:return Fraction(CTX.gen(VARIABLES.index(e)))
    if e.is_Add:return sum((rational(a) for a in e.args),Fraction(0))
    if e.is_Mul:
        out=Fraction(1)
        for a in e.args:out=out*rational(a)
        return out
    if e.is_Pow and e.exp.is_Integer:return rational(e.base)**int(e.exp)
    raise ValueError(('not a rational function in the declared variables',e))

def rational_inverse(A,progress=None,with_det=False):
    n=len(A); B=[[Fraction(e) for e in row]+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    determinant=Fraction(1)
    for q in range(n):
        candidates=[(B[i][q].size(),i) for i in range(q,n) if B[i][q]]
        if not candidates:raise ValueError('singular minor')
        _,i=min(candidates)
        B[i],B[q]=B[q],B[i]
        if i!=q:determinant=-determinant
        pivot=B[q][q]; determinant=determinant*pivot
        B[q]=[e/pivot for e in B[q]]
        for i in range(n):
            if i==q or not B[i][q]:continue
            c=B[i][q]; B[i]=[x-c*y for x,y in zip(B[i],B[q])]
        if progress:progress(q)
    result=[row[n:] for row in B]
    assert all(not (B[i][j]-Fraction(int(i==j))) for i in range(n) for j in range(n))
    return (result,determinant) if with_det else result

def rational_chart(A,progress=None):
    B=[[Fraction(e) for e in row] for row in A]
    n=len(B); m=len(B[0]) if n else 0
    rows=list(range(n));cols=list(range(m));rank=0
    for q in range(min(n,m)):
        candidates=[(B[i][j].size(),i,j) for i in range(q,n)
                    for j in range(q,m) if B[i][j]]
        if not candidates:break
        _,i,j=min(candidates)
        B[i],B[q]=B[q],B[i];rows[i],rows[q]=rows[q],rows[i]
        for row in B:row[j],row[q]=row[q],row[j]
        cols[j],cols[q]=cols[q],cols[j]
        pivot=B[q][q]
        for i in range(q+1,n):
            if not B[i][q]:continue
            c=B[i][q]/pivot
            for j in range(q+1,m):B[i][j]=B[i][j]-c*B[q][j]
            B[i][q]=Fraction(0)
        rank=q+1
        if progress:progress(q)
    return rank,rows[:rank],cols[:rank]

def poly(expr):
    p=s.Poly(expr,*VARIABLES)
    return CTX.from_dict({m:fmpq(str(c)) for m,c in p.terms()})

def expr(p):
    return s.Add(*(s.Rational(str(c))*s.Mul(*(x**i for x,i in zip(VARIABLES,m)))
                   for m,c in p.to_dict().items()))

def polynomial_rows(K):
    """Clear coupling-only row denominators; record all such factors."""
    rows=[]; scales=[]
    for row in K.tolist():
        pairs=[s.fraction(s.cancel(e)) for e in row]
        den=s.lcm([p[1] for p in pairs])
        if den.has(D,S):
            raise ValueError('The unreduced matrix must be polynomial in D,S')
        values=[poly(s.cancel(e*den)) for e in row]
        content=ZERO
        for value in values:
            if value: content=value if not content else content.gcd(value)
        unit=ONE
        if content:
            c,fac=content.factor(); unit=CTX.constant(c)
            for f,power in fac:
                if f.degrees()[2]==0: unit*=f**power
        rows.append([p/unit for p in values])
        scales.append(s.cancel(den/expr(unit)))
    return rows,scales

def extract(A,rows,cols):
    return [[A[i][j] for j in cols] for i in rows]

def primitive_in_D(p):
    """Discard only D-independent factors; keep multiplicities."""
    _,factors=p.factor(); result=ONE
    for f,m in factors:
        if f.degrees()[2]>0: result*=f**m
    return result
