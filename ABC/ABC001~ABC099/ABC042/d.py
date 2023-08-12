H, W, A, B = map(int, input().split())
k = 2 * 10**5 + 2
mod = 10**9 + 7

fact = [1]*k  # fact[n] = (n! mod p)
factinv = [1]*k  # factinv[n] = ((n!)^(-1) mod p)
inv = [0]*k  # factinv 計算用
inv[1] = 1
for i in range(2, k):
    fact[i] = (fact[i-1]*i) % mod
    inv[i] = (mod - inv[mod % i]*(mod//i)) % mod
    factinv[i] = factinv[i-1]*inv[i] % mod
ans = fact[H+W-2]*factinv[H-1]*factinv[W-1] % mod
for b in range(1, B+1):
    tmp = fact[H-A-1+b-1]*factinv[H-A-1]*factinv[b-1] * \
        fact[A-1+W-b]*factinv[A-1]*factinv[W-b] % mod
    ans -= tmp
    ans %= mod
print(ans)
