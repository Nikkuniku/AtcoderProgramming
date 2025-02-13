N, K = map(int, input().split())
MOD = 998244353
inv_P = pow(N * N, -1, MOD)
dp = [[0, 0] for _ in range(K + 1)]
dp[0][0] = 1
p = (N * N) - (2 * N) + 2
q = 2 * (N - 1)
for i in range(K):
    dp[i + 1][0] = dp[i][0] * p * inv_P + dp[i][1] * (N - 1) * 2 * inv_P
    dp[i + 1][1] = (dp[i][0] * 2 + dp[i][1] * (N - 2) * 2 + dp[i][1] * p) * inv_P
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD
tot = ((N * (N + 1)) // 2) - 1
ans = dp[K][0] + dp[K][1] * tot
ans %= MOD
print(ans)
