"""Read-only Appendix-B correspondence checks; --write-log saves package outputs."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import sympy as sp
from grassmann import (Exterior, Jet, GAMMA, CHARGE, IDENTITY,
                       evaluate_block, compare_arrays)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECORDS = []


def exact(name, expression=0, *, expected_zero=True):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    zero = all(sp.expand(x) == 0 for x in entries)
    if zero != expected_zero:
        raise AssertionError(name)
    RECORDS.append(dict(check=name, method='exact symbolic',
                        expectation='zero' if expected_zero else 'nonzero negative control',
                        passed=True))


def finite(name, error, scale, tolerance=2e-11):
    relative = error / scale
    if not np.isfinite(relative) or relative > tolerance:
        raise AssertionError((name, error, scale, tolerance))
    RECORDS.append(dict(check=name, method='numerical bosons / formal Grassmann coefficients',
                        absolute_error=error, scale=scale, scaled_error=relative,
                        tolerance=tolerance))


def source_checks():
    manifest = json.loads((HERE/'source_manifest.json').read_text())
    for path, digest in manifest['repository_inputs'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise AssertionError('Source changed: '+path)
    for path, digest in manifest['implementation_hashes'].items():
        if hashlib.sha256((HERE/path).read_bytes()).hexdigest() != digest:
            raise AssertionError('Implementation changed: '+path)
    RECORDS.append(dict(check='source and implementation fingerprints', method='integrity',
                        passed=True))


def symbolic_checks():
    a,b,c,x,y,z,d,e,f = sp.symbols('a b c x y z d e f')
    upper = sp.Matrix([[a,b],[b,c]])
    bilinear = sp.Matrix([[x,y],[y,z]])
    derivative = sp.Matrix([[d,e],[e,f]])  # one arbitrary Lorentz component
    eps = sp.Matrix([[0,1],[-1,0]])
    down, bd = eps.T*upper*eps, eps.T*bilinear*eps
    norm2 = 2*upper.det()
    q = sum(upper[i,j]*bd[i,j] for i in range(2) for j in range(2))
    k = down*bilinear*down
    exact('norm and inverse triplet identity',upper*down-norm2*sp.eye(2)/2)
    exact('rho index placement',q-sum(down[i,j]*bilinear[i,j] for i in range(2) for j in range(2)))
    exact('NW-SE vector self-bilinear vanishes',sp.trace(bilinear*eps))
    exact('K = L_down Q - L^2 B_down/2',k-down*q+norm2*bd/2)
    exact('N block: paper versus corrected OP basis',
          norm2*bd-3*down*q-(-norm2*bd/2-3*k))
    exact('E block: paper versus corrected OP basis',
          -norm2*bd+3*down*q-(norm2*bd/2+3*k))
    exact('literal 2013 N coefficients are different',
          sp.I*(norm2*bd-3*down*q)-(-sp.I*norm2*bd/2-sp.Rational(4,3)*k),
          expected_zero=False)
    exact('literal 2013 E coefficients are different',
          -norm2*bd+3*down*q-(-sp.Rational(2,3)*norm2*bd-k/3),
          expected_zero=False)
    def symmetric(fn):
        return sp.Matrix(2,2,lambda i,j:(fn(i,j)+fn(j,i))/2)
    right, left, mixed = bilinear*eps, eps.T*bilinear, upper*eps
    paper_dl = -3*symmetric(lambda i,j:sum(down[k,i]*upper[l,m]*derivative[j,l]*right[k,m]
                                          for k in range(2) for l in range(2) for m in range(2)))
    paper_dl += norm2/2*symmetric(lambda i,j:sum(derivative[k,i]*right[k,j] for k in range(2)))
    s1 = norm2*symmetric(lambda i,j:sum(left[i,k]*derivative[j,k] for k in range(2)))
    s2 = symmetric(lambda i,j:sum(down[m,n]*mixed[k,i]*bilinear[m,n]*derivative[j,k]
                                  for k in range(2) for m in range(2) for n in range(2)))
    exact('DL block: paper versus coefficients (-1,+3)',paper_dl-(-s1+3*s2))
    d2,e2,f2 = sp.symbols('d2 e2 f2')
    derivative2 = sp.Matrix([[d2,e2],[e2,f2]])
    lower_upper = eps.T*upper
    def gradient_pair(first,second):
        second_down = eps.T*second*eps
        return sum(lower_upper[k,l]*first[k,p]*second_down[l,p]
                   for k in range(2) for l in range(2) for p in range(2))
    exact('Fhat triplet-gradient term is already antisymmetric',
          gradient_pair(derivative,derivative2)+gradient_pair(derivative2,derivative))
    exact('literal 2013 DL coefficients are different',
          paper_dl-(-sp.Rational(2,3)*s1-s2),expected_zero=False)
    unknowns = sp.symbols('c1 c2')
    residual = (paper_dl-unknowns[0]*s1-unknowns[1]*s2).applyfunc(sp.expand)
    equations = [coef for entry in residual for coef in sp.Poly(entry,a,b,c,x,y,z,d,e,f).coeffs()]
    solution = sp.solve(equations,unknowns,dict=True)
    if solution != [{unknowns[0]:-1,unknowns[1]:3}]:
        raise AssertionError(solution)
    RECORDS.append(dict(check='independent polynomial coefficient solve for DL basis',
                        method='exact symbolic',solution={'c1':'-1','c2':'3'},passed=True))

    ell = sp.Symbol('L',positive=True)
    t,dt,n,j,dj = sp.symbols('T dT LcontractDL J derivative_bilinear')
    # n=L^{ij}D L_ij, D L=n/L, and D J=2 derivative_bilinear.
    coefficient_derivative = sp.diff(ell**-3*t,ell)*n/ell + sp.diff(ell**-3*t,t)*dt
    expanded = -2*(coefficient_derivative*j+ell**-3*t*2*dj)
    expected = 6*ell**-5*t*n*j-2*ell**-3*dt*j-4*ell**-3*t*dj
    exact('Fhat bilinear derivative: coefficients +6,-2,-4 before index swap',expanded-expected)
    exact('Fhat leading current derivative',
          4*(sp.diff(ell**-1,ell)*n/ell*j+ell**-1*dj)
          -(4*ell**-1*dj-4*ell**-3*n*j))
    exact('Dphi corrected coefficient cancels partial epsilon',-sp.I/2+sp.I/2)
    exact('Dphi printed real coefficient fails',-sp.I/2+sp.Rational(1,2),expected_zero=False)
    u,v = sp.symbols('psi_phi psi_psi_L')
    ehat2 = -sp.I*u/2-v/4
    exact('ordinary current has no independent fermion bilinear',ehat2+sp.I*u/2+v/4)
    exact('setting Ehat2=0 violates the current relation',sp.I*u/2+v/4,expected_zero=False)
    # div(div(antisymmetric density)): independent symmetric derivatives of an antisymmetric tensor.
    h = sp.Matrix(5,5,lambda i,j:sp.Symbol('h'+str(min(i,j))+str(max(i,j))))
    curl = sp.Matrix(5,5,lambda i,j:0 if i==j else (1 if i<j else -1)*sp.Symbol('F'+str(min(i,j))+str(max(i,j))))
    exact('ordinary-current conservation by antisymmetry',sum(h[i,j]*curl[i,j] for i in range(5) for j in range(5)))

    tau = sp.Symbol('t')
    r0,r2,y0,y2,n0,n2,l0,l1,l3,p1 = sp.symbols('rho0 rho2 Y0 Y2 N0 N2 L0 lambda1 lambda3 phi1')
    density = (r0+tau**2*r2)*(n0+tau**2*n2)+l0*(y0+tau**2*y2)+(tau*l1+tau**3*l3)*tau*p1
    exact('BF order-two selection retains rho2,Y2,lambda1',
          sp.expand(density).coeff(tau,2)-(r0*n2+r2*n0+l0*y2+l1*p1))
    exact('cubic lambda only contributes at action order four',sp.expand(tau**3*l3*tau*p1).coeff(tau,2))


def grassmann_checks():
    # Exact-index convention checks, followed by the independent exterior engine.
    pauli1=sp.Matrix([[0,1],[1,0]])
    pauli2=sp.Matrix([[0,-sp.I],[sp.I,0]])
    pauli3=sp.diag(1,-1)
    g=[-sp.I*sp.kronecker_product(pauli3,sp.eye(2))]
    g += [sp.kronecker_product(pauli1,p) for p in (pauli1,pauli2,pauli3)]
    g += [sp.kronecker_product(pauli2,sp.eye(2))]
    charge=g[2]*g[4]
    for i in range(5):
        for j in range(5):
            exact(f'Clifford {i},{j}',g[i]*g[j]+g[j]*g[i]-(2*(-1 if i==0 else 1)*sp.eye(4) if i==j else sp.zeros(4)))
        exact(f'C gamma {i} is antisymmetric',(charge*g[i]).T+charge*g[i])
        finite(f'fixed gamma representation {i}',float(np.max(np.abs(GAMMA[i]-np.array(g[i],complex)))),1.)
    exact('linear Majorana C is antisymmetric',charge.T+charge)
    exact('gamma volume orientation',g[0]*g[1]*g[2]*g[3]*g[4]-sp.I*sp.eye(4))
    finite('fixed charge matrix',float(np.max(np.abs(CHARGE-np.array(charge,complex)))),1.)
    x,y,z = [Exterior.generator(k) for k in range(3)]
    finite('exterior anticommutation',(x*y+y*x).size(),1.)
    finite('exterior nilpotence',(x*x).size(),1.)
    finite('exterior associativity',((x*y)*z-x*(y*z)).size(),1.)
    jx,jy=Jet(x,z),Jet(y,Exterior.generator(3))
    finite('even variation product rule',
           ((jx*jy).variation-(z*y+x*Exterior.generator(3))).size(),1.)

    for seed in (7,4):
        for kind in ('N','E','DL'):
            largest_negative = 0.
            for direction in (range(1) if kind=='N' else range(5)):
                for component in (range(3) if kind=='DL' else range(1)):
                    got,want,old = evaluate_block(seed,kind,direction,component)
                    error,scale = compare_arrays(got,want)
                    finite(f'delta lambda scalar block seed={seed} {kind} a={direction} component={component}',error,scale)
                    error,scale=compare_arrays(got,old)
                    largest_negative=max(largest_negative,error/scale)
            if largest_negative < 1e-6:
                raise AssertionError((seed,kind,'2013 negative control was not detected'))
            RECORDS.append(dict(check=f'literal 2013 {kind} negative control seed={seed}',
                                method='numerical negative control',largest_scaled_error=largest_negative,
                                required_minimum=1e-6,passed=True))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-log',action='store_true')
    args=parser.parse_args()
    source_checks();symbolic_checks();grassmann_checks()
    report=dict(scope='Items 30-31 correspondence only; not a full nonlinear SUSY proof',
                versions=dict(python=platform.python_version(),sympy=sp.__version__,numpy=np.__version__),
                seeds=[7,4],checks=RECORDS)
    messages=[f'PASS: {len(RECORDS)} correspondence checks',
              'PASS: exact SU(2) bases, derivative rules, current and fermion order',
              'PASS: 42 formal-Grassmann scalar-block checks with numerical triplets',
              'PASS: six literal-2013 numerical negative controls',
              'Scope: no full gravitino-dependent transformation or quartic action claim']
    print('\n'.join(messages))
    if args.write_log:
        out=HERE/'outputs';out.mkdir(exist_ok=True)
        (out/'verification.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        (out/'verification.log').write_text('\n'.join(messages)+'\n')


if __name__=='__main__':
    main()
