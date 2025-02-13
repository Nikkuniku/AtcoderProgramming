N, K, L = map(int, input().split())
p = N - K
ans = 1
MOD = 998244353
for i in range(p):
    ans *= L - i
    ans %= MOD
for _ in range(K):
    ans *= L - p
    ans %= MOD
ans %= MOD
print(ans)
