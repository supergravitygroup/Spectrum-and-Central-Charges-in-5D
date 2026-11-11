"""Bosonic LR + lambda GB and independent current-source representatives.

fs=True replaces the bare background C potential by its field-strength
representative, modulo bulk total derivatives and B'=B-C_bg wedge c/2.
This includes both constant and Fourier torus modes. Provenance is recorded
in source_manifest.json; source_weyl.py supplies the current conformal route.
"""
import symengine as se, itertools
from algebra import P, ZERO, inv, sqrt1, EPS
R5=range(5)
KCRR=[1]   # CS(Gamma) normalization; checked by the exact fs congruence
def zeros(*shape):
    if len(shape)==1: return [ZERO]*shape[0]
    return [zeros(*shape[1:]) for _ in range(shape[0])]
def psum(lst):
    out=P()
    for x in lst:
        if not x.iszero(): out=out+x
    return out

def build(eng,pert,verbose=False,model='GB',alpha=0,beta=0,zeta=0,fs=False):
    """pert: dict of perturbations in Cartesian frame components (P objects):
       'h'[a][b] (symm), 'C'[a], 'V'[a], 'B'[a][b], 'E'[a][b][c], 'L', 'N', 'Z'[a], 'Zb'[a]."""
    bg=eng.bg; C3=eng.Cs; Ed=eng.Ed; eta=eng.eta
    l,w,g,lam=bg['l'],bg['w'],bg['g'],bg['lam']
    I=se.I
    # ---- metric
    h=pert['h']
    gl=[[ (P(eta[a]) if a==b else ZERO)+h[a][b] for b in R5] for a in R5]
    hu=[[h[a][b]*(eta[a]*eta[b]) for b in R5] for a in R5]   # eta^aa h_ab eta^bb
    gi=[[None]*5 for _ in R5]
    for a in R5:
        for b in R5:
            ab=0
            for c in R5:
                x,y=hu[a][c],hu[c][b]
                ab+= eta[c]*(x.a*y.b+x.b*y.a)
            gi[a][b]=P(eta[a] if a==b else 0,-hu[a][b].a,-hu[a][b].b,se.expand(ab))
    t1a=sum(hu[a][a].a*eta[a] for a in R5); t1b=sum(hu[a][a].b*eta[a] for a in R5)
    # tr(eta^-1 h eta^-1 h) cross part
    tr2=0
    for a in R5:
        for c in R5:
            tr2+= (eta[a]*h[a][c].a)*(eta[c]*h[c][a].b)
    sq=P(1,t1a/2,t1b/2,se.expand(t1a*t1b/4-tr2/2))      # sqrt(-det g_ab)
    isq=inv(sq)
    # ---- connection  Gam_cab = g(nabla_a E_b, E_c)
    Gl=[[[None]*5 for _ in R5] for _ in R5]
    for c in R5:
        for a in R5:
            for b in R5:
                x=Ed(a,gl[b][c])+Ed(b,gl[a][c])-Ed(c,gl[a][b])
                for d in R5:
                    if C3[d][a][b]!=0: x=x+gl[d][c]*C3[d][a][b]
                    if C3[d][a][c]!=0: x=x-gl[d][b]*C3[d][a][c]
                    if C3[d][b][c]!=0: x=x-gl[d][a]*C3[d][b][c]
                Gl[c][a][b]=x*se.Rational(1,2)
    Gm=[[[psum([gi[d][c]*Gl[c][a][b] for c in R5]) for b in R5] for a in R5] for d in R5]   # Gm[d][a][b]=Gam^d_ab
    if verbose: print(' connection done',flush=True)
    # ---- Riemann R^d_{cab}
    Rm=[[[[ZERO]*5 for _ in R5] for _ in R5] for _ in R5]
    for d in R5:
        for c in R5:
            for a in R5:
                for b in range(a+1,5):
                    x=Ed(a,Gm[d][b][c])-Ed(b,Gm[d][a][c])
                    for e in R5:
                        x=x+Gm[e][b][c]*Gm[d][a][e]-Gm[e][a][c]*Gm[d][b][e]
                        if C3[e][a][b]!=0: x=x-Gm[d][e][c]*C3[e][a][b]
                    Rm[d][c][a][b]=x; Rm[d][c][b][a]=-x
    Rl=[[[[psum([gl[d][e]*Rm[e][c][a][b] for e in R5]) for b in R5] for a in R5] for c in R5] for d in R5]   # R_dcab
    M=[[[[psum([gi[c][e]*Rm[d][e][a][b] for e in R5]) for b in R5] for a in R5] for c in R5] for d in R5]    # R^{dc}_ab
    Ric=[[psum([Rm[a][c][a][b] for a in R5]) for b in R5] for c in R5]     # R_cb
    Ricm=[[psum([gi[c][e]*Ric[e][b] for e in R5]) for b in R5] for c in R5]  # R^c_b
    Rs=psum([Ricm[c][c] for c in R5])
    if verbose: print(' curvature done',flush=True)
    # ---- helpers
    def up2(T): return [[psum([gi[a][c]*gi[b][d]*T[c][d] for c in R5 for d in R5 if not T[c][d].iszero()]) for b in R5] for a in R5]
    def up1(T): return [psum([gi[a][c]*T[c] for c in R5 if not T[c].iszero()]) for a in R5]
    def mix(T): return [[psum([T[a][c]*gi[c][b] for c in R5 if not T[a][c].iszero()]) for b in R5] for a in R5]  # T_a^b
    def d1(A):
        out=zeros(5,5)
        for a in R5:
            for b in R5:
                if a==b: continue
                x=Ed(a,A[b])-Ed(b,A[a])
                for c in R5:
                    if C3[c][a][b]!=0: x=x-A[c]*C3[c][a][b]
                out[a][b]=x
        return out
    def dform(T,p):
        # general exterior derivative of a p-form given as nested lists (Cartesian frame comps)
        def comp(idx):
            x=P()
            for i in range(p+1):
                rest=idx[:i]+idx[i+1:]
                x=x+Ed(idx[i],get(T,rest))*((-1)**i)
            for i in range(p+1):
                for j in range(i+1,p+1):
                    rest=[idx[k] for k in range(p+1) if k not in (i,j)]
                    for c in R5:
                        cc=C3[c][idx[i]][idx[j]]
                        if cc!=0: x=x+get(T,[c]+rest)*(cc*(-1)**(i+j))
            return x
        return comp
    def get(T,idx):
        for i in idx: T=T[i]
        return T
    # ---- background + perturbations of matter fields
    if not fs:
        Cf=[P((bg['p']/w) if a==3 else 0)+pert['C'][a] for a in R5]
    else:
        Cf=[pert['C'][a] for a in R5]          # fluctuation only; flux enters through Gbg
    Gbg=zeros(5,5); Gbg[3][4]=P(bg['p']); Gbg[4][3]=P(-bg['p'])
    if bg['r']==0: Vf=[pert['V'][a] for a in R5]
    else: Vf=[P((bg['r']/w) if a==3 else 0)+pert['V'][a] for a in R5]
    Lf=P(bg['L'])+pert['L']; Nf=P(bg['N'])+pert['N']
    Zf=pert['Z']; Zb=pert['Zb']
    Bf=pert['B']
    Ebg=-4*bg['h']/g
    Ef=[[[pert['E'][a][b][c] for c in R5] for b in R5] for a in R5]
    for (a,b,c),sgn in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((1,0,2),-1),((0,2,1),-1),((2,1,0),-1)]:
        Ef[a][b][c]=Ef[a][b][c]+P(sgn*Ebg)
    G=d1(Cf)
    if fs:
        Gfl=G
        G=[[G[a][b]+Gbg[a][b] for b in R5] for a in R5]
    dV=d1(Vf)
    cV=[[dV[a][b]+(Zb[a]*Zf[b]-Zf[a]*Zb[b])*(2*I) for b in R5] for a in R5]
    dZ=d1(Zf); dZb=d1(Zb)
    cZ=[[dZ[a][b]-(Vf[a]*Zf[b]-Vf[b]*Zf[a])*I for b in R5] for a in R5]
    cZb=[[dZb[a][b]+(Vf[a]*Zb[b]-Vf[b]*Zb[a])*I for b in R5] for a in R5]
    dB=dform(Bf,2)
    H3=[[[None]*5 for _ in R5] for _ in R5]
    for a,b,c in itertools.permutations(R5,3):
        if a<b<c:
            if not fs:
                x=dB([a,b,c])+(Cf[a]*G[b][c]+Cf[b]*G[c][a]+Cf[c]*G[a][b])*se.Rational(1,2)+Ef[a][b][c]*(g/2)
            else:   # H = dB' + c^Gbg + (1/2) c^g + (g/2)E,  B' = B - (1/2) C_bg^c
                x=(dB([a,b,c])+(Cf[a]*Gbg[b][c]+Cf[b]*Gbg[c][a]+Cf[c]*Gbg[a][b])
                   +(Cf[a]*Gfl[b][c]+Cf[b]*Gfl[c][a]+Cf[c]*Gfl[a][b])*se.Rational(1,2)+Ef[a][b][c]*(g/2))
            for (i,j,k),s_ in [((a,b,c),1),((b,c,a),1),((c,a,b),1),((b,a,c),-1),((a,c,b),-1),((c,b,a),-1)]:
                H3[i][j][k]=x*s_
    for a in R5:
        for b in R5:
            for c in R5:
                if H3[a][b][c] is None: H3[a][b][c]=ZERO
    # raise H3
    H3u=[[[psum([gi[a][a2]*gi[b][b2]*gi[c][c2]*H3[a2][b2][c2] for a2 in R5 for b2 in R5 for c2 in R5 if not H3[a2][b2][c2].iszero()]) if a<b<c else None for c in R5] for b in R5] for a in R5]
    # H_ab = -(1/12) eps_abcde H^cde, eps_lower = -sq * epshat
    H=zeros(5,5)
    for p_,sg in EPS.items():
        a,b,c,d,e=p_
        if c<d<e:
            H[a][b]=H[a][b]+ (sq*H3u[c][d][e])*(se.Rational(-1,12)*(-sg)*6)
    dE=dform(Ef,3)
    dEc={}
    for idx in itertools.combinations(R5,4): dEc[idx]=dE(list(idx))
    Eup=[ZERO]*5
    for p_,sg in EPS.items():
        a=p_[0]; rest=tuple(sorted(p_[1:]))
        # eps^{a bcde} dE_bcde = 24 * sg' * dE_sorted ; collect via sorted rest with permutation sign
        if list(p_[1:])==list(rest):
            Eup[a]=Eup[a]+ (isq*dEc[rest])*(se.Rational(-1,48)*sg*24)
    Elow=[psum([gl[a][b]*Eup[b] for b in R5]) for a in R5]
    if verbose: print(' fields done',flush=True)
    Gu=up2(G); Hu=up2(H); cVu=up2(cV)
    Gm_=mix(G); Hm_=mix(H)
    def dot2(A,Bu): return psum([A[a][b]*Bu[a][b] for a in R5 for b in R5 if not A[a][b].iszero()])
    G2=dot2(G,Gu); H2=dot2(H,Hu); GH=dot2(G,Hu)
    def tr4(A,B,Cc,Dd):  # A_a^b B_b^c C_c^d D_d^a with mixed tensors
        AB=[[psum([A[a][b]*B[b][c] for b in R5]) for c in R5] for a in R5]
        CD=[[psum([Cc[a][b]*Dd[b][c] for b in R5]) for c in R5] for a in R5]
        return psum([AB[a][c]*CD[c][a] for a in R5 for c in R5])
    G4=None
    H4=tr4(Hm_,Hm_,Hm_,Hm_); GGGH=tr4(Gm_,Gm_,Gm_,Hm_); GHGH=tr4(Gm_,Hm_,Gm_,Hm_); GHHH=tr4(Gm_,Hm_,Hm_,Hm_)
    # curvature contractions
    Riem2=psum([M[d][c][a][b]*M[a][b][d][c] for d in R5 for c in R5 for a in R5 for b in R5])
    Ric2=psum([Ricm[c][b]*Ricm[b][c] for c in R5 for b in R5])
    GBd=Riem2-Ric2*4+Rs*Rs
    RHG=psum([M[a][b][c][d]*H[a][b]*Gu[c][d] for a in R5 for b in R5 for c in R5 for d in R5])
    RHH=psum([M[a][b][c][d]*H[a][b]*Hu[c][d] for a in R5 for b in R5 for c in R5 for d in R5])
    # R_ab H^ac G^b_c = R^b_a? use Ric lower R_ab, H^ac, G^b_c = g^{bd} G_dc ...  R_ab H^{ac} G^{b}{}_{c}
    Gmu=[[psum([gi[b][d]*G[d][c] for d in R5]) for c in R5] for b in R5]   # G^b_c
    RicHG=psum([Ric[a][b]*Hu[a][c]*Gmu[b][c] for a in R5 for b in R5 for c in R5])
    # eps terms
    Hmix=[[psum([H[b][g_]*gi[g_][f] for g_ in R5]) for f in R5] for b in R5]   # H_b^f
    def nab2(T):   # nabla_a T_bc
        return [[[ Ed(a,T[b][c]) - psum([Gm[e][a][b]*T[e][c] for e in R5]) - psum([Gm[e][a][c]*T[b][e] for e in R5]) for c in R5] for b in R5] for a in R5]
    nH=nab2(H); nG=nab2(G)
    divG=[psum([gi[f][b]*nG[b][a][f] for f in R5 for b in R5]) for a in R5]   # nabla^f G_af
    epsHdHG=P(); epsdGGG=P(); epsCRR=P(); epsCVV=P(); epsCZZ=P(); epsEGG=P(); epsEHH=P()
    X=[[[[ZERO]*5 for _ in R5] for _ in R5] for _ in R5]
    for b in R5:
        for c in range(b+1,5):
            for d in R5:
                for e in range(d+1,5):
                    x=psum([M[f][g_][b][c]*Rl[f][g_][d][e] for f in R5 for g_ in R5])
                    X[b][c][d][e]=x; X[c][b][d][e]=-x; X[b][c][e][d]=-x; X[c][b][e][d]=x
    if fs:
        # field-strength forms of the bare-C_bg parts (exact up to total derivatives):
        #  eps C_bg dv dv  ~ eps Gbg v dv ;  eps C_bg DZ DZbar ~ eps Gbg Z DZbar ;  eps C X ~ -(1/3) eps G CS(Gamma)
        dVfl=d1([pert['V'][a] for a in R5])
        Gam1=[[[Gm[dd][a][cc] for a in R5] for cc in R5] for dd in R5]     # (Gamma^d_c)_a
        def d1P(A): return d1(A)
        dGam=[[d1P(Gam1[dd][cc]) for cc in R5] for dd in R5]
        def CScomp(a,b,c):   # CS_{abc} = tr(Gam ^ dGam + 2/3 Gam^Gam^Gam)
            x=P()
            for dd in R5:
                for cc in R5:
                    A=Gam1[dd][cc]; Bm=dGam[cc][dd]
                    x=x+A[a]*Bm[b][c]+A[b]*Bm[c][a]+A[c]*Bm[a][b]
            y=P()
            for dd in R5:
                for e1 in R5:
                    for e2 in R5:
                        A=Gam1[dd][e1]; Bv=Gam1[e1][e2]; Cv=Gam1[e2][dd]
                        for (i,j,k),sg_ in [((a,b,c),1),((b,c,a),1),((c,a,b),1),((b,a,c),-1),((a,c,b),-1),((c,b,a),-1)]:
                            y=y+A[i]*Bv[j]*Cv[k]*sg_
            return x+y*se.Rational(2,3)
        CS012=CScomp(0,1,2)
    for p_,sg in EPS.items():
        a,b,c,d,e=p_
        epsHdHG=epsHdHG+ psum([Hmix[b][f]*nH[a][c][f] for f in R5])*G[d][e]*sg
        epsdGGG=epsdGGG+ divG[a]*G[b][c]*G[d][e]*sg
        epsCRR=epsCRR+ Cf[a]*X[b][c][d][e]*sg
        epsCVV=epsCVV+ Cf[a]*cV[b][c]*cV[d][e]*sg
        epsCZZ=epsCZZ+ Cf[a]*cZ[b][c]*cZb[d][e]*sg
        epsEGG=epsEGG+ Elow[a]*G[b][c]*G[d][e]*sg
        epsEHH=epsEHH+ Elow[a]*H[b][c]*H[d][e]*sg
        if fs and (a,b) in ((3,4),(4,3)):
            gb_=Gbg[a][b]
            epsCVV=epsCVV+ gb_*pert['V'][c]*dVfl[d][e]*sg
            epsCZZ=epsCZZ+ gb_*Zf[c]*cZb[d][e]*sg
    if fs:
        # eps^{abcde} Gbg_ab CS_cde = 12 p eps^{34012} CS_012
        epsCRR=epsCRR+ CS012*(bg['p']*12*EPS[(3,4,0,1,2)]*se.Rational(-1,3))*KCRR[0]
    # tensor eps^{abcde} = epshat/sq
    epsHdHG=epsHdHG*isq; epsdGGG=epsdGGG*isq; epsCRR=epsCRR*isq; epsCVV=epsCVV*isq; epsCZZ=epsCZZ*isq; epsEGG=epsEGG*isq; epsEHH=epsEHH*isq
    if verbose: print(' contractions done',flush=True)
    dL=[Ed(a,Lf) for a in R5]; dLu=up1(dL); dL2=psum([dL[a]*dLu[a] for a in R5])
    Zbu=up1(Zb); ZZ=psum([Zf[a]*Zbu[a] for a in R5])
    E2=psum([Elow[a]*Eup[a] for a in R5])
    EV=psum([Eup[a]*Vf[a] for a in R5]); EC=psum([Eup[a]*Cf[a] for a in R5])
    if fs:   # sq*E^a C_bg,a  ~  -(1/24) eps^{abcde} Gbg_ab E_cde  (fluctuation E)
        x=P()
        for p_,sg in EPS.items():
            a,b,c,d,e=p_
            if (a,b) in ((3,4),(4,3)): x=x+Gbg[a][b]*pert['E'][c][d][e]*sg
        EC=EC+isq*x*se.Rational(-1,24)
    cVH=dot2(cV,Hu)
    iL=inv(Lf)
    LLR=(Lf*(Rs-G2*se.Rational(1,2)+H2*4)+iL*dL2+Lf*ZZ*4-iL*Nf*Nf*2-iL*E2*2-EV*(2*se.sqrt(2))-EC*(4*g)
         -Lf*Nf*(2*g)-Nf*(4*g)+Lf*Lf*(2*g**2)-Lf*Lf*Lf*(g**2/2))
    LGB=(GBd*se.Rational(1,8)+RHG*se.Rational(1,2)-RHH-RicHG*2+Rs*GH*se.Rational(1,2)
         -H2*H2*2+H4*4-G2*GH*se.Rational(1,2)+GH*GH+GGGH-GHGH*2+GHHH*4
         +epsHdHG+epsdGGG*se.Rational(1,16)
         +epsCRR*se.Rational(1,16)-epsCVV*se.Rational(1,8)-epsCZZ*se.Rational(1,2)
         +Lf*cVH*(se.sqrt(2)*g)-Nf*GH*(2*g)-epsEGG*(g/8)-epsEHH*g
         +Lf*Lf*(Rs*se.Rational(-1,4)+G2*se.Rational(1,4)-GH*se.Rational(1,2)-H2*3-ZZ*2)*(g**2)-dL2*(g**2/2)+Nf*Nf*(g**2)+E2*(g**2)
         +Nf*Lf*Lf*(2*g**3)+Lf*Lf*Lf*Lf*(g**4/2))
    R12=se.Rational
    if model=='GB':
        tot=sq*(LLR+LGB*lam)
    elif model=='GBnoE':
        tot=sq*(LLR+lam*(LGB+epsEGG*(g/8)+epsEHH*g-E2*g**2))
    else:
        # extra contractions for the C^2+R^2/6 and LOG invariants (eqs. (2.11), (2.13))
        dGu=up1(divG); divG2=psum([divG[a]*dGu[a] for a in R5])
        EdivG=psum([Eup[a]*divG[a] for a in R5])
        # nabla_a H_bc nabla^a H^bc
        nHu=[[[psum([gi[a][a2]*gi[b][b2]*gi[c][c2]*nH[a2][b2][c2] for a2 in R5 for b2 in R5 for c2 in R5 if not nH[a2][b2][c2].iszero()]) for c in R5] for b in R5] for a in R5]
        dH2=psum([nH[a][b][c]*nHu[a][b][c] for a in R5 for b in R5 for c in R5])
        G4=tr4(Gm_,Gm_,Gm_,Gm_); GGHH=tr4(Gm_,Gm_,Hm_,Hm_)
        RicGG=psum([Ric[a][b]*Gu[a][c]*Gmu[b][c] for a in R5 for b in R5 for c in R5])
        Hmu=[[psum([gi[b][d]*H[d][c] for d in R5]) for c in R5] for b in R5]
        RicHH=psum([Ric[a][b]*Hu[a][c]*Hmu[b][c] for a in R5 for b in R5 for c in R5])
        cV2=dot2(cV,cVu)
        cZbu=up2(cZb); cZZ=dot2(cZ,cZbu)
        cVG=dot2(cV,Gu)
        eHHdG=P(); eHdGG=P()
        for p_,sg in EPS.items():
            a,b,c,d,e=p_
            eHHdG=eHHdG+divG[a]*H[b][c]*H[d][e]*sg      # eps^{abcde} divG_a H_bc H_de
            eHdGG=eHdGG+divG[a]*H[b][c]*G[d][e]*sg      # eps^{abcde} divG_a H_bc G_de
        eHHdG=eHHdG*isq; eHdGG=eHdGG*isq
        LW=(Riem2*R12(1,8)-Ric2*R12(1,6)+Rs*Rs*R12(1,24)-cV2*R12(1,6)-cZZ*R12(2,3)
            +RHG*R12(1,2)+RHH*R12(1,3)-RicGG*R12(1,3)+RicHG*R12(2,3)-RicHH*R12(8,3)
            +Rs*(GH*R12(-1,6)+H2*R12(2,3))
            -G2*G2*R12(1,24)+H2*H2*2+G4*R12(1,4)+H4*4-G2*H2*R12(4,3)+G2*GH*R12(1,6)+H2*GH*R12(8,3)
            -GH*GH*R12(1,3)-GGGH+GGHH*R12(8,3)+GHGH*R12(2,3)-GHHH*R12(20,3)+divG2*R12(1,3)-dH2*R12(4,3)
            -eHHdG*R12(2,3)+epsHdHG+eHdGG*R12(1,3)+epsdGGG*R12(1,48)
            +epsCRR*R12(1,16)-epsCVV*R12(1,24)-epsCZZ*R12(1,6)
            +Nf*(Rs*R12(-1,3)+G2*R12(2,3)-GH*R12(2,3)-H2*4)*g-Lf*(cVG-cVH*2)*(g/(3*se.sqrt(2)))
            -EdivG*(2*g/3)-epsEGG*(5*g/24)+epsEHH*(g/3)
            +Lf*Lf*(Rs*R12(-1,12)+G2*R12(1,6)-GH*R12(1,6)-H2)*(g**2)+Nf*Nf*(4*g**2/3)+E2*(g**2)
            +Nf*Lf*Lf*(2*g**3/3)+Lf*Lf*Lf*Lf*(g**4/12))
        Llog=(-Ric2*R12(1,6)+Rs*Rs*R12(1,24)+cV2*R12(1,12)+cZZ*R12(1,3)
            -RHH*R12(2,3)+RicGG*R12(1,6)-RicHG*R12(4,3)+RicHH*R12(4,3)
            +Rs*(GH*R12(1,3)-H2*R12(1,3))+G2*G2*R12(1,48)-H2*H2*2-G4*R12(1,8)+G2*H2*R12(2,3)-G2*GH*R12(1,3)
            -H2*GH*R12(4,3)+GH*GH*R12(2,3)+GGGH-GGHH*R12(4,3)-GHGH*R12(4,3)
            +GHHH*R12(16,3)-divG2*R12(1,6)+dH2*R12(2,3)
            +epsdGGG*R12(1,48)+eHHdG*R12(1,3)-eHdGG*R12(1,6)
            -epsCVV*R12(1,24)-epsCZZ*R12(1,6)
            +Nf*(Rs*R12(1,6)-G2*R12(1,3)-GH*R12(2,3)+H2*2)*g+Lf*(cVG+cVH*4)*(g/(6*se.sqrt(2)))
            +EdivG*(g/3)+epsEGG*(g/24)-epsEHH*(2*g/3)
            +Lf*Lf*(Rs*R12(-1,12)+G2*R12(1,24)-GH*R12(1,6)-H2-ZZ)*(g**2)-dL2*(g**2/4)-Nf*Nf*(g**2/6)
            +Nf*Lf*Lf*(2*g**3/3)+Lf*Lf*Lf*Lf*(5*g**4/24))
        if model in ('source_W','source_GB'):
            from source_weyl import evaluate
            LW=evaluate(dict(locals(),psum=psum))
        if model in ('source_LOG','source_GB'):
            # Current generic_combination/action.md G-LOG, before the cyclic-H
            # derivative is transferred with the gauged Bianchi identity.
            # This independent representative retains its explicit E^2 and
            # double-epsilon terms. See the chapter action_inputs.md.
            cyclic=psum([nH[a][b][c]*(nHu[b][c][a]+nHu[c][a][b])
                         for a in R5 for b in R5 for c in R5])
            eg=[P() for _ in R5]; eh=[P() for _ in R5]
            for pp,sg in EPS.items():
                a,b,c,d,e=pp
                eg[a]=eg[a]+G[b][c]*G[d][e]*isq*sg
                eh[a]=eh[a]+H[b][c]*H[d][e]*isq*sg
            double_epsilon=psum([gl[a][b]*eg[a]*eh[b] for a in R5 for b in R5])
            Llog=Llog+(RHH*R12(2,3)-RicHH*R12(4,3)-G2*G2*R12(1,24)
                +G4*R12(1,12)+GH*GH*R12(2,3)-GHGH*R12(4,3)
                +cyclic*R12(2,3)+double_epsilon*R12(1,12)
                -epsEGG*(g/12)+E2*(g**2/3))
        LR2=P()
        if zeta != 0:
            if fs:
                raise ValueError("The standalone R2 checks use the potential chart")
            from r2_density import density
            LR2=density(dict(locals(),psum=psum))
        tot=sq*(LLR+LW*alpha+Llog*beta+LR2*zeta)
    diag=dict(R=Rs.z,G34=G[3][4].z,H34=H[3][4].z,V34=cV[3][4].z,E=[x.z for x in Eup])
    return tot,diag
