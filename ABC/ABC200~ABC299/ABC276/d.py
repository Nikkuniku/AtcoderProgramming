from math import gcd
N = int(input())
a = list(map(int, input().split()))
g = gcd(0, a[0])
for i in range(1, N):
    g = gcd(g, a[i])


def f(m, p):
    res = 1 << 62
    ok = False
    for i in range(30):
        for j in range(30):
            if m == p*pow(2, i)*pow(3, j):
                res = min(res, i+j)
                ok = True
    if ok:
        return (ok, res)
    return (False, -1)


ans = 0
for i in range(N):
    q, cnt = f(a[i], g)
    if not q:
        print(-1)
        exit()
    else:
        ans += cnt
print(ans)
