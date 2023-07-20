N, M, K = map(int, input().split())
k = 2 * 10**5
mod = 998244353


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


p = 998244353
lim = 2*10**5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


ans = 0
for k in range(K+1):
    tmp = cmb(N-1, k, mod)*M*pow(M-1, N-k-1, mod)
    ans += tmp
    ans %= mod
print(ans)
