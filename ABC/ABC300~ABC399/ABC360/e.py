N, K = map(int, input().split())
MOD = 998244353
p = ((N - 1) ** 2 + 1) % MOD
q = 2
dp = [[0, 0] for _ in range(K + 1)]
dp[0][0] = 1
inv = pow(N * N, -1, MOD)
for i in range(K):
    dp[i + 1][0] = (dp[i][0] * p + dp[i][1] * (N - 1) * q) * inv
    dp[i + 1][1] = (dp[i][0] * q + dp[i][1] * p + dp[i][1] * (N - 2) * q) * inv
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD
prod = (N * (N + 1) // 2) - 1
ans = (dp[K][0] + dp[K][1] * prod % MOD) % MOD
print(ans)
