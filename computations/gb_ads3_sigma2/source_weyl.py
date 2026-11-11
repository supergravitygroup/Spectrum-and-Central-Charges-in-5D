"""Current G-W, G-D7--G-D11 evaluated before the BPS substitution.

The two differentiated currents are integrated by parts once, retaining the
explicit conformal K and f corrections. This is a separate source route
from the rewritten Weyl expression in action.py.
"""
import symengine as se
from algebra import P, EPS

def evaluate(c):
    gi,gl,Ric,Rs,Rl=(c[x] for x in ('gi','gl','Ric','Rs','Rl'))
    G,H,Gu,G2,H2,GH=(c[x] for x in ('G','H','Gu','G2','H2','GH'))
    g,Lf,Nf,Cf,isq=(c[x] for x in ('g','Lf','Nf','Cf','isq'))
    psum,up2,mix,tr4,nab2,dot2=(c[x] for x in ('psum','up2','mix','tr4','nab2','dot2'))
    A=range(5); Q=se.Rational
    f=[[Ric[a][b]*Q(-1,6)+gl[a][b]*Rs*Q(1,48) for b in A] for a in A]
    fm=[[psum([f[a][b]*gi[b][h] for b in A]) for h in A] for a in A]
    T=[[(G[a][b]-H[a][b]*2)*Q(1,8) for b in A] for a in A]
    Tu=up2(T); Tm=mix(T)
    Tfirst=[[psum([gi[a][b]*T[b][h] for b in A]) for h in A] for a in A]
    T2=dot2(T,Tu); T4=tr4(Tm,Tm,Tm,Tm)
    dc=Rs*Q(-1,32)+G2*Q(5,96)+GH*Q(1,24)-H2*Q(13,24)+Nf*(g/4)+Lf*Lf*(g**2/16)
    Weyl=[[[[Rl[a][b][d][e]+(f[a][d]*gl[b][e]-f[b][d]*gl[a][e]
              -f[a][e]*gl[b][d]+f[b][e]*gl[a][d])*2
              for e in A] for d in A] for b in A] for a in A]
    Wup=[[[[psum([gi[a][i]*gi[b][j]*Weyl[i][j][d][e]
                  for i in A for j in A if not Weyl[i][j][d][e].iszero()])
                  for e in A] for d in A] for b in A] for a in A]
    WTT=psum([Weyl[a][b][d][e]*Tu[a][b]*Tu[d][e]
              for a in A for b in A for d in A for e in A])
    nt=nab2(T)
    ntu=[[[psum([gi[a][i]*gi[b][j]*gi[d][h]*nt[i][j][h]
                 for i in A for j in A for h in A if not nt[i][j][h].iszero()])
                 for d in A] for b in A] for a in A]
    dt=psum([nt[a][b][d]*ntu[a][b][d] for a in A for b in A for d in A])
    cross=psum([nt[b][a][d]*ntu[a][b][d] for a in A for b in A for d in A])
    div=[psum([gi[b][d]*nt[b][a][d] for b in A for d in A]) for a in A]
    div2=psum([gi[a][b]*div[a]*div[b] for a in A for b in A])
    fterm=psum([T[a][b]*gi[b][j]*f[j][d]*Tu[a][d]
                for a in A for b in A for j in A for d in A])
    current=[[psum([Wup[a][b][d][e]*Tu[d][e]*4 for d in A for e in A])
            -dc*Tu[a][b]*Q(64,3)-Tu[a][b]*T2*Q(128,9)
            -psum([Tfirst[a][d]*Tu[d][e]*Tfirst[b][e]*Q(512,3) for d in A for e in A])
            for b in A] for a in A]
    GQ=dot2(G,current)*Q(1,2)
    def K(a,b,d,e):
        return (f[a][b]*T[d][e]*2+gl[b][d]*psum([fm[a][h]*T[e][h] for h in A])*2
                -f[a][d]*T[e][b]*2-gl[b][e]*psum([fm[a][h]*T[d][h] for h in A])*2
                +f[a][e]*T[d][b]*2)
    epsTTd=P(); transfer=P(); conformal=P(); cs=P()
    for inds,sg in EPS.items():
        a,b,d,e,h=inds
        epsTTd=epsTTd+T[a][b]*T[d][e]*div[h]*sg
        for j in A:
            transfer=transfer+G[a][b]*(Tm[d][j]*nt[j][e][h]*Q(2,3)
                         +Tm[d][j]*nt[e][h][j])*sg
            conformal=conformal+Cf[a]*Tm[d][j]*(K(b,j,e,h)*Q(2,3)+K(b,e,h,j))*sg
        cs=cs+Cf[a]*psum([Wup[i][j][b][d]*Weyl[i][j][e][h] for i in A for j in A])*sg
    epsTTd=epsTTd*isq; transfer=transfer*isq; conformal=conformal*isq;cs=cs*isq
    return ((c['Riem2']-c['Ric2']*Q(4,3)+Rs*Rs*Q(1,6))*Q(1,8)
        +dc*dc*Q(64,3)+dc*T2*Q(1024,9)-WTT*Q(16,3)
        -c['cV2']*Q(1,6)-c['cZZ']*Q(2,3)
        -dt*Q(64,3)+cross*Q(64,3)+div2*Q(128,3)+fterm*Q(512,3)
        -epsTTd*Q(128,3)+T4*1024-T2*T2*Q(2816,27)
        +cs*Q(1,16)-c['epsCVV']*Q(1,24)-c['epsCZZ']*Q(1,6)
        +GQ-transfer*16-conformal*32
        -Lf*dot2(c['cV'],Tu)*(8*g/(3*se.sqrt(2))))
