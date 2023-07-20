from itertools import accumulate


MOD = 998244353
table_len = 5 * 10**5
fac = [1, 1]
inv = [1, 1]
finv = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)
    inv.append(-inv[MOD % i] * (MOD // i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD)


def binom(n, r):
    return fac[n] * finv[n - r] % MOD * finv[r] % MOD


N, K = map(int, input().split())
A = set(list(map(int, input().split())))
M = N+K
need = 1
ans = 0
for x in range(M):
    if need > K:
        break
    p = K-need+x
    ans += binom(p, x)
    ans %= MOD
    if x not in A:
        need += 1
print(ans)
