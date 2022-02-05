n = int(input())
a = list(map(int, input().split()))

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

com = [1]*(n)
for i in range(1, n):
    com[i] = (com[i-1]*(n-i)*inv[i]) % mod

ans = 0
for i in range(n):
    ans += com[i]*a[i]
    ans %= mod
print(ans)
