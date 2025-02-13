import sympy
from sympy.solvers.diophantine.diophantine import find_DN, diop_DN, transformation_to_DN
from sympy.parsing.sympy_parser import parse_expr


def findDNAB(eqstr):
    sympy.var("x y")
    eq = parse_expr(eqstr)
    (D, N) = find_DN(eq)
    (A, B) = transformation_to_DN(eq)
    return (D, N, A, B)


def pelEq(D, N):
    # (u,v): solution to x**2-D*y**2=1
    (u, v) = diop_DN(D, 1)[0]
    # Matrix to generate other solution
    A = sympy.Matrix([[u, v * D], [v, u]])
    # List of fundamental solutions
    xyl = [sympy.Matrix([[x1], [y1]]) for (x1, y1) in diop_DN(D, N)]

    while True:
        yield [(xy[0], xy[1]) for xy in xyl]
        for i in range(len(xyl)):
            xyl[i] = A * xyl[i]


# solve quadratic equation with interger solutions
def diophQuad(eq):
    (D, N, A, B) = findDNAB(eq)
    ansPelEq = pelEq(D, N)
    while True:
        xyl = next(ansPelEq)
        for X, Y in xyl:
            (x, y) = A * sympy.Matrix([[abs(X)], [abs(Y)]]) + B
            yield (x, y)


F = [
    " 5*x**2 -4* y**2 + 8*x  +4 ",
    " 5*x**2 -4* y**2 - 8*x  +4 ",
    " 5*x**2 -4* y**2 - 2*x  +1 ",
    " 5*x**2 -4* y**2 + 2*x  +1 ",
]

ans = []
for f in F:
    ansDQ = diophQuad(f)
    for i in range(15):
        (x, y) = next(ansDQ)
        if int(x) == x:
            ans.append((x, y))
ans.sort()
triangles = []
for b, L in ans:
    if b > 0 and L > 0:
        triangles.append((b, L))
ans = 0
for i in range(12):
    ans += triangles[i][1]
print(ans)
print(triangles)
