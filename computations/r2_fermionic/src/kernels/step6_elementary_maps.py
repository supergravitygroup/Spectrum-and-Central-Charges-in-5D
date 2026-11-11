"""Literal tensor transcription of Step 6 Eqs. (4)--(32), (B8)--(B27).

Public functions return complete expressions at physical degree <=2, never
new physical fields. All generated dummy indices are fresh and typed.
"""
from step6_elementary_algebra import *

def G(a,b):return field('G',a,b)
def H(a,b):return field('H',a,b)
def E(a):
    b,c,d,e=[fresh() for _ in range(4)];i,j=fresh('i'),fresh('i')
    return (-eps(a,up(b),up(c),up(d),up(e))*D(dn(b),field('E3',dn(c),dn(d),dn(e)))/12
      -I*bps(dn(b),up(i))*ga(up(b),a)*vf(dn(i))/2
      -bps(dn(b),up(i))*ga(a,up(b),up(c))*ps(dn(c),up(j))*lp(dn(i),dn(j))/4)
def T(a,b):
    c,d,e=[fresh() for _ in range(3)];i=fresh('i')
    return (G(a,b)/8-H(a,b)/4+I*(bps(a,up(i))*ps(b,dn(i))-bps(b,up(i))*ps(a,dn(i)))/32
      -eps(a,b,dn(c),dn(d),dn(e))*bps(up(c),up(i))*ga(up(d))*ps(up(e),dn(i))/64)
def Gh(a,b):
    i=fresh('i');return G(a,b)+I*(bps(a,up(i))*ps(b,dn(i))-bps(b,up(i))*ps(a,dn(i)))/4
def K(c,a,b):
    i=fresh('i');return (bps(a,up(i))*ga(b)*ps(c,dn(i))-bps(b,up(i))*ga(a)*ps(c,dn(i)))/4+bps(a,up(i))*ga(c)*ps(b,dn(i))/4
def Rp(a,b,i):
    c,d=fresh(),fresh()
    return D(a,ps(b,i))-D(b,ps(a,i))+I*ga(up(c),up(d))*(G(dn(c),dn(d))-2*H(dn(c),dn(d)))*(ga(a)*ps(b,i)-ga(b)*ps(a,i))/8
def ph(a,i):
    b,c=fresh(),fresh()
    return I*ga(up(b))*Rp(a,dn(b),i)/3-I*ga(a)*ga(up(b),up(c))*Rp(dn(b),dn(c),i)/24
def Rq(a,b,i):return Rp(a,b,i)-I*(ga(a)*ph(b,i)-ga(b)*ph(a,i))
def dps(a,i):
    if i[1]>0:return raise_spin(lambda j:dps(a,j),i)
    b,c=fresh(),fresh();j=fresh('i')
    return ga(up(b),up(c))*(G(dn(b),dn(c))+2*H(dn(b),dn(c)))*ps(a,i)/8+g*lp(i,dn(j))*ps(a,up(j))/2-ph(a,i)
def chi(i):
    if i[1]>0:return raise_spin(chi,i)
    a=fresh();return I*ga(up(a))*dps(dn(a),i)/8+g*vf(i)/8
def ft():
    a,b,c,d=[fresh() for _ in range(4)];i=fresh('i')
    return (-field('R')/16-(D(dn(a),K(dn(b),up(a),up(b)))-D(dn(b),K(dn(a),up(a),up(b))))/16
      -I*bar(ph(dn(a),up(i)))*ga(up(a),up(b))*ps(dn(b),dn(i))/16
      -I*bps(dn(a),up(i))*(ga(up(a))*ga(up(c),up(d))*(G(dn(c),dn(d))-2*H(dn(c),dn(d)))*ga(up(b))
        -ga(up(b))*ga(up(c),up(d))*(G(dn(c),dn(d))-2*H(dn(c),dn(d)))*ga(up(a)))*ps(dn(b),dn(i))/256
      +bps(dn(a),up(i))*ga(up(a))*chi(dn(i)))
def Dc():
    a,b=fresh(),fresh();i=fresh('i')
    return (ft()/2-Gh(dn(a),dn(b))*Gh(up(a),up(b))/16-Q(26,3)*T(dn(a),dn(b))*T(up(a),up(b))
      +2*Gh(up(a),up(b))*T(dn(a),dn(b))+g*N/4+g*g*L*L/16
      -I*bps(dn(a),up(i))*dps(up(a),dn(i))/8-bps(dn(a),up(i))*ga(up(a))*chi(dn(i))/2)
def DL(a,i,j):
    return D(a,lp(i,j))-I*(A('barpsi',a,i)*vf(j)+A('barpsi',a,j)*vf(i))/2
def Dv(a,i):
    if i[1]>0:return raise_spin(lambda j:Dv(a,j),i)
    b,c=fresh(),fresh();j=fresh('i')
    return (D(a,vf(i))-I*ga(up(b))*D(dn(b),lp(i,dn(j)))*ps(a,up(j))/2
      +I*ga(up(b))*E(dn(b))*ps(a,i)/2-N*ps(a,i)/2
      -lp(i,dn(j))*ga(up(b),up(c))*(G(dn(b),dn(c))-2*H(dn(b),dn(c)))*ps(a,up(j))/8
      +3*lp(i,dn(j))*ph(a,up(j)))
def BoxLt(i,j):
    if i[1]<0 or j[1]<0:return low_pair_from_upper(BoxLt,i,j)
    a,b,c=fresh(),fresh(),fresh();k=fresh('i')
    z=D(up(a),DL(dn(a),i,j))+K(dn(b),up(b),up(a))*D(dn(a),lp(i,j))+6*ft()*lp(i,j)
    z-=I*(bps(up(a),i)*Dv(dn(a),j)+bps(up(a),j)*Dv(dn(a),i))/2
    for x,y in [(i,j),(j,i)]:
        z+=2*(bps(up(a),x)*ga(dn(a))*chi(up(k))+bps(up(a),up(k))*ga(dn(a))*chi(x))*lp(y,dn(k))
    z-=6*lp(i,j)*bps(dn(a),up(k))*ga(up(a))*chi(dn(k))
    z-=(bvf(i)*ga(up(b),up(c))*T(dn(b),dn(c))*ga(up(a))*ps(dn(a),j)
         +bvf(j)*ga(up(b),up(c))*T(dn(b),dn(c))*ga(up(a))*ps(dn(a),i))/2
    z+=(bvf(i)*ga(up(a))*ph(dn(a),j)+bvf(j)*ga(up(a))*ph(dn(a),i))/2
    return z
def rho():
    i,j=fresh('i'),fresh('i');return poly(2*N/L)+I/L**3*lp(dn(i),dn(j))*bvf(up(i))*vf(up(j))
def lam(i):
    if i[1]>0:return raise_spin(lam,i)
    a,b,c,d=[fresh() for _ in range(4)];j,k=fresh('i'),fresh('i')
    return (-2*I/L*ga(up(a))*D(dn(a),vf(i))
      +ga(up(a),up(b))*(G(dn(a),dn(b))-2*H(dn(a),dn(b)))*vf(i)/(2*L)
      +(2*g/L-2*N/L**3)*lp(i,dn(j))*vf(up(j))
      +2*I/L**3*ga(up(a))*D(dn(a),lp(i,dn(j)))*lp(up(j),up(k))*vf(dn(k))
      -2*I/L**3*ga(up(a))*E(dn(a))*lp(i,dn(j))*vf(up(j))
      -ga(up(a))*ga(up(b))*D(dn(b),lp(i,dn(j)))*ps(dn(a),up(j))/L
      +ga(up(a))*ga(up(b))*E(dn(b))*ps(dn(a),i)/L
      +I*(N/L-g*L/2)*ga(up(a))*ps(dn(a),i)
      +I/(2*L)*lp(i,dn(j))*ga(up(a))*ga(up(b),up(c))*G(dn(b),dn(c))*ps(dn(a),up(j))
      +2/L*lp(i,dn(j))*ga(up(a),up(b))*D(dn(a),ps(dn(b),up(j)))
      +I/(4*L)*lp(i,dn(j))*ga(up(a),up(b))*ga(up(c),up(d))*(G(dn(c),dn(d))-2*H(dn(c),dn(d)))*ga(dn(a))*ps(dn(b),up(j)))
def Y(i,j):
    if i[1]>0 or j[1]>0:return raise_pair(Y,i,j)
    a,b=fresh(),fresh();k,m,l=[fresh('i') for _ in range(3)]
    z=BoxLt(i,j)/L-lp(i,j)*(N*N+E(dn(a))*E(up(a)))/L**3+Q(8,3)/L*lp(i,j)*T(dn(a),dn(b))*T(up(a),up(b))+4/L*lp(i,j)*Dc()
    for x,y in [(i,j),(j,i)]:
        z-=lp(up(k),up(m))*DL(dn(a),dn(k),x)*DL(up(a),y,dn(m))/(2*L**3)
        z+=E(dn(a))*lp(dn(k),x)*DL(up(a),y,up(k))/L**3
        z+=I*N/(2*L**3)*bvf(x)*vf(y)
        z-=bvf(x)*ga(up(a))*E(dn(a))*vf(y)/(2*L**3)
        z-=8*I/L*bar(chi(x))*vf(y)
        z+=lp(dn(k),x)*bvf(up(k))*ga(up(a))*Dv(dn(a),y)/L**3
        z-=Q(3,2)/L**5*lp(dn(k),x)*lp(up(l),up(m))*bvf(up(k))*ga(up(a))*D(dn(a),lp(y,dn(l)))*vf(dn(m))
        z+=bvf(up(l))*ga(up(a))*D(dn(a),lp(dn(l),x))*vf(y)/(4*L**3)
    z-=3*I*N/L**5*lp(i,j)*lp(up(k),up(l))*bvf(dn(k))*vf(dn(l))
    z+=3/L**5*lp(i,j)*lp(up(k),up(l))*bvf(dn(k))*ga(up(a))*E(dn(a))*vf(dn(l))
    z+=16*I/L**3*lp(i,j)*lp(dn(k),dn(l))*bar(chi(up(k)))*vf(up(l))
    z+=bvf(up(m))*ga(up(a))*D(dn(a),lp(i,j))*vf(dn(m))/(2*L**3)
    z+=2*I/L**3*lp(i,j)*bvf(up(k))*ga(up(a),up(b))*T(dn(a),dn(b))*vf(dn(k))
    return z
def Ap(a):
    i,j=fresh('i'),fresh('i')
    return 2/L*E(a)+s.sqrt(2)*field('V',a)-lp(dn(i),dn(j))*bvf(up(i))*ga(a)*vf(up(j))/L**3-I/L*bvf(up(i))*ps(a,dn(i))
def Fp(a,b):return D(a,Ap(b))-D(b,Ap(a))
def Fh(a,b):
    i=fresh('i')
    return Fp(a,b)-(bps(a,up(i))*ga(b)*lam(dn(i))-bps(b,up(i))*ga(a)*lam(dn(i)))/2+I*rho()*(bps(a,up(i))*ps(b,dn(i))-bps(b,up(i))*ps(a,dn(i)))/4
def Dr(a):
    i=fresh('i');return D(a,rho())-I*bps(a,up(i))*lam(dn(i))/2
def Dlam(a,i):
    if i[1]>0:return raise_spin(lambda j:Dlam(a,j),i)
    b,c=fresh(),fresh();j=fresh('i')
    return D(a,lam(i))+ga(up(b),up(c))*Fp(dn(b),dn(c))*ps(a,i)/4+I*ga(up(b))*Dr(dn(b))*ps(a,i)/2-Y(i,dn(j))*ps(a,up(j))-rho()*ga(up(b),up(c))*T(dn(b),dn(c))*ps(a,i)-rho()*ph(a,i)
def boxrho():
    a,b,c=fresh(),fresh(),fresh();i=fresh('i')
    return (D(up(a),Dr(dn(a)))+K(dn(b),up(b),up(a))*D(dn(a),rho())
      -I*bps(dn(a),up(i))*Dlam(up(a),dn(i))/2-2*rho()*bps(dn(a),up(i))*ga(up(a))*chi(dn(i))
      +bps(dn(a),up(i))*ga(up(a))*ga(up(b),up(c))*T(dn(b),dn(c))*lam(dn(i))/2
      +bar(ph(dn(a),up(i)))*ga(up(a))*lam(dn(i))/2+2*ft()*rho())
def DG(c,a,b,prime=False):
    d,e=fresh(),fresh();i=fresh('i');F=Fh if prime else Gh;Fp0=Fp if prime else G
    z=D(c,F(a,b))-K(c,up(d),a)*Fp0(b,dn(d))+K(c,up(d),b)*Fp0(a,dn(d))
    z+=I*(rho() if prime else poly(1))*bps(c,up(i))*Rq(a,b,dn(i))/2
    df=(lambda x:Dlam(x,dn(i))) if prime else (lambda x:dps(x,dn(i)))
    z+=bps(c,up(i))*(ga(a)*df(b)-ga(b)*df(a))/2
    if prime:
        z-=I*bps(c,up(i))*(ga(a)*ga(up(d),up(e))*T(dn(d),dn(e))*ga(b)-ga(b)*ga(up(d),up(e))*T(dn(d),dn(e))*ga(a))*lam(dn(i))/2
        z-=I*bar(ph(c,up(i)))*ga(a,b)*lam(dn(i))
    z+=bps(c,up(i))*ga(up(d))*(ps(a,dn(i))*Fp0(dn(d),b)-ps(b,dn(i))*Fp0(dn(d),a))/2
    return z
def DT(c,a,b):
    d=fresh();i=fresh('i')
    return D(c,T(a,b))-K(c,up(d),a)*T(b,dn(d))+K(c,up(d),b)*T(a,dn(d))-I*bps(c,up(i))*ga(a,b)*chi(dn(i))/2+Q(3,32)*I*bps(c,up(i))*Rq(a,b,dn(i))

def token(t):
    a,b,c,d,e=map(lambda x:x,'abcde');i,j='i','j'
    if t==r"\rho'":return rho()
    if t==r"(\rho')^2":return rho()**2
    if t==r"Y'^{ij}":return Y(up(i),up(j))
    if t==r"Y'_{ij}":return Y(dn(i),dn(j))
    if t==r"L_{ij}":return lp(dn(i),dn(j))
    if t==r"\bar\lambda'^i":return bar(lam(up(i)))
    if t==r"\lambda'_i":return lam(dn(i))
    if t==r"\lambda'^j":return lam(up(j))
    if t==r"\chi_i":return chi(dn(i))
    if t==r"\bar\chi^i":return bar(chi(up(i)))
    if t==r"\not{\mathcal D}\lambda'_i":
        x=fresh();return ga(up(x))*Dlam(dn(x),dn(i))
    if t==r"A'_a":return Ap(dn(a))
    if t==r"(\mathcal D_b\rho')":return Dr(dn(b))
    if t==r"\Box_c\rho'":return boxrho()
    if t==r"f_a^a":return ft()
    if t==r"D":return Dc()
    if t==r"T^2":
        x,y=fresh(),fresh();return T(dn(x),dn(y))*T(up(x),up(y))
    if t==r"T^{ab}":return T(up(a),up(b))
    if t in [r'\gamma\cdot T',r'\gamma\cdot\widehat G']:
        x,y=fresh(),fresh();return ga(up(x),up(y))*(T(dn(x),dn(y)) if t.endswith(' T') else Gh(dn(x),dn(y)))
    if t==r'\mathcal D_bT^{ab}':return DT(dn(b),up(a),up(b))
    if t==r'\mathcal D_b\widehat G^{ab}':return DG(dn(b),up(a),up(b))
    if t==r"\mathcal D_b\widehat F'^{ab}":return DG(dn(b),up(a),up(b),True)
    if t in [r'\widehat G^{ab}',r'\widehat G_{ab}',r'\widehat G_{de}']:
        xx=(up(a),up(b)) if '^' in t else ((dn(a),dn(b)) if t.endswith('{ab}') else (dn(d),dn(e)))
        return Gh(*xx)
    if t in [r"\widehat F'_{ab}",r"\widehat F'_{bc}"]:return Fh(dn(a),dn(b)) if t.endswith('{ab}') else Fh(dn(b),dn(c))
    if t==r'\varepsilon^{abcde}':return eps(*map(up,'abcde'))
    if t.startswith(r'\gamma^'):
        letters=t.split('^',1)[1].strip('{}');return ga(*map(up,letters))
    if t.startswith(r'\bar\psi_'):return bps(dn(t[len(r'\bar\psi_')]),up(i))
    if t.startswith(r'\phi_'):return ph(dn(t[len(r'\phi_{')]),dn(i))
    if t==r'\phi^a_i':return ph(up(a),dn(i))
    if t in [r'\psi^a_i',r'\psi^{aj}']:return ps(up(a),dn(i) if t.endswith('_i') else up(j))
    if t in [r'\psi_{ai}',r'\psi_{bi}',r'\psi_{ci}']:return ps(dn(t[len(r'\psi_{')]),dn(i))
    if t in [r'\psi_a^j',r'\psi_b^j',r'\psi_c^j']:return ps(dn(t[len(r'\psi_')]),up(j))
    raise ValueError(t)
