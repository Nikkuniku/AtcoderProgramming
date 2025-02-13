from itertools import product

N, M, K = map(int, input().split())


def gen(n, m, k):
    P = list(product(range(1, k + 1), repeat=n * m))
    s = set()
    for p in P:
        tmp = [[0] * m for _ in range(n)]
        for i in range(n * m):
            tmp[i // m][i % m] = p[i]
        t = []
        for i in range(n):
            t.append(min(tmp[i]))
        for j in range(m):
            col = []
            for i in range(n):
                col.append(tmp[i][j])
            t.append(max(col))
        s.add(tuple(t))
    s = sorted(list(s))
    return s


def solve(n, m, k):
    res = 0
    MOD = 998244353
    if n == 1 or m == 1:
        return pow(k, max(n, m), MOD)
    for i in range(1, k + 1):
        tmp = pow(k - i + 1, m, MOD)
        if k - i > 0:
            tmp -= pow(k - i, m, MOD)
        tmp *= pow(i, n, MOD)
        tmp %= MOD
        res += tmp
        res %= MOD
    return res


# L = 3
# C = [[0] * (L + 1) for _ in range(L + 1)]
# D = [[0] * (L + 1) for _ in range(L + 1)]
# for i in range(1, L + 1):
#     for j in range(1, L + 1):
#         C[i][j] = len(gen(i, j, K))
#         D[i][j] = solve(i, j, K)
# print(*C, sep="\n")
# print(*D, sep="\n")
print(solve(N, M, K))
