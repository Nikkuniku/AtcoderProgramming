def solve(n, m, k):
    MOD = 998244353
    if n == 1 or m == 1:
        return pow(k, max(n, m), MOD)
    res = 0
    for i in range(1, k + 1):
        tmp = pow(k - i + 1, m, MOD)
        if k - i > 0:
            tmp -= pow(k - i, m, MOD)
        tmp *= pow(i, n, MOD)
        tmp %= MOD
        res += tmp
        res %= MOD
    return res


N, M, K = map(int, input().split())
print(solve(N, M, K))
