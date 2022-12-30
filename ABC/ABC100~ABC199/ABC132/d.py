N, K = map(int, input().split())
k = 2 * 10**5
mod = 10**9 + 7

fact = [1]*k  # fact[n] = (n! mod p)
factinv = [1]*k  # factinv[n] = ((n!)^(-1) mod p)
inv = [0]*k  # factinv 計算用
inv[1] = 1
for i in range(2, k):
    fact[i] = (fact[i-1]*i) % mod
    inv[i] = (mod - inv[mod % i]*(mod//i)) % mod
    factinv[i] = factinv[i-1]*inv[i] % mod


def cmb(n, r, p):
    re = 1
    for j in range(r):
        re = re*(n-j) % p
    re = re*factinv[r] % p
    return re


for i in range(1, K+1):
    ans = 0
    ans += cmb(K-1, i-1, mod)*cmb(N-K-1, i, mod)
    ans += cmb(K-1, i-1, mod)*cmb(N-K-1, i-1, mod)
    ans += cmb(K-1, i-1, mod)*cmb(N-K-1, i-1, mod)
    if i >= 2:
        ans += cmb(K-1, i-1, mod)*cmb(N-K-1, i-2, mod)
    ans %= mod
    print(ans)
