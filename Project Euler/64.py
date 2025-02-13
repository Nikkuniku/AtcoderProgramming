def cfsqrt(m):
    n0 = int(m ** (1 / 2))
    if n0 * n0 == m:
        return [n0]
    n, a, b, cf = n0, 1, 0, []
    while True:
        b = n * a - b
        a = (m - b * b) // a
        n = (n0 + b) // a
        cf.append(n)
        if a == 1:
            break
    return [n0, cf]


N = 10000
ans = 0
for i in range(2, N + 1):
    res = cfsqrt(i)
    if len(res) == 1:
        continue
    ans += len(res[1]) % 2
print(ans)
