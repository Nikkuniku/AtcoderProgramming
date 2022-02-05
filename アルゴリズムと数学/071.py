n = int(input())
A, B, C = [], [], []

for _ in range(n):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)


def func(x, y):
    return x+y


def solve_x(a, b, c, d):
    re = False
    if a != c:
        re = (d-b)/(a-c)
    return re


def solve_y(a, b, c, d):
    re = False
    if a != c:
        re = ((a*d)-(b*c))/(a-c)
    return re


px = []
py = []
for i in range(n):
    for j in range(i+1, n):
        a = A[i]
        b = B[i]
        c = C[i]
        d = A[j]
        e = B[j]
        f = C[j]
        if -a/b != -d/e:
            px.append(solve_x(-a/b, c/b, -d/e, f/e))
            py.append((-a/b)*px[-1] + (c/b))


def check(x, y):
    for k in range(n):
        if A[k]*x + B[k]*y > C[k]:
            return False
    return True


ans = -1
for i in range(len(px)):
    if check(px[i], py[i]):
        ans = max(ans, func(px[i], py[i]))

print(ans)
