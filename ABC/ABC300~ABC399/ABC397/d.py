from sympy.solvers import solve
from sympy import Symbol


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


y = Symbol("y")
N = int(input())
for d in range(1, N):
    if d * d * d > N:
        break
    temp = 3 * y * y * d + 3 * y * d * d + d * d * d - N
    sol = solve(temp, y)
    a, b = sol
    if is_integer_num(a) and is_integer_num(b):
        exit(print(a, b))
print(-1)
