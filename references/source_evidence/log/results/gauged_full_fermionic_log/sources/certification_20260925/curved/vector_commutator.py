"""C24 A.4 vector-vector commutator on elementary vector gaugino.
ASSERT_CONVENTION: metric_signature=mostly-plus, source_frame=Gold-S23-C24
"""
import curved_primary as c
from curved_primary import *
import exact_su2_components as su
import close_linearity as cl
up,dn=b.up,b.dn
def rs_lower(a,bb,s,k):
 t,z,cc,dd=b.fresh('s'),b.fresh('s'),b.fresh('l'),b.fresh('l')
 out=-Q(1,2)*F('G',up(cc),dn(s),up(t))*b.vec(dn(cc),F('w3a',a,bb,dn(t),up(k)))
 out-=Q(1,4)*(F('G',a,dn(s),up(t))*b.vec(up(cc),F('w3a',bb,dn(cc),dn(t),up(k)))-F('G',bb,dn(s),up(t))*b.vec(up(cc),F('w3a',a,dn(cc),dn(t),up(k))))
 out-=Q(1,8)*F('ws',dn(s),up(t))*F('w3a',a,bb,dn(t),up(k))
 out+=Q(1,16)*F('S',a,bb,dn(s),up(t))*F('w',up(cc),up(dd))*F('w3a',dn(cc),dn(dd),dn(t),up(k))
 out+=Q(3,16)*(F('w',up(cc),a)*F('w3a',bb,dn(cc),dn(s),up(k))-F('w',up(cc),bb)*F('w3a',a,dn(cc),dn(s),up(k)))
 return out

def rm(a,bb,cc,dd):
 s,t,v,z=[b.fresh('s') for _ in range(4)]
 WW=I*F('w4',dn(s),dn(t),dn(v),dn(z))
 for a1,b1,c1,d1 in [(s,t,v,z),(s,v,t,z),(s,z,t,v)]:WW+=F('ws',dn(a1),dn(b1))*F('ws',dn(c1),dn(d1))
 return -Q(1,4)*F('S',a,bb,up(s),up(t))*F('S',cc,dd,up(v),up(z))*WW

def vv(f,a,bb):
 s,t,cc,dd,k,l=[b.fresh(z) for z in ['s','s','l','l','u','u']]
 out=I*Q(1,2)*F('w3a',a,bb,up(s),dn(k))*b.D(f,s,k)
 out-=Q(1,2)*rm(a,bb,up(cc),up(dd))*b.M(f,cc,dd)
 out+=I*Q(3,4)*F('za',a,bb,up(k),up(l))*b.J(f,k,l)
 out-=b.eps(up(s),up(t))*rs_lower(a,bb,t,k)*b.Sgen(f,s,k)
 return out

def build():
 # p(L_G)=-lambda_B, so [D,D]lambda_B=-p([D,D]L_G).
 source=-vv(F('L','-sE','+uI'),'-lA','-lB')
 b.check(source,Q(7,2),{'lA':'-','lB':'-','sE':'-','uI':'+'})
 pp=p.project(source)
 rows={}
 for z in [0,1]:
  slot='CL'+str(z);p.FREE[slot]={'lA':'-','lB':'-','sE':'-'}
  aa=su.component(pp,{'uI':z});rr=c.canonical(aa,slot)
  rows[z]=rr;pickle.dump(rr,(OUT/(slot+'-commutator.pkl')).open('wb'));print(slot,len(rr.ts),flush=True)
 return rows

if __name__=='__main__':build()
