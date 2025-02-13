N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(N):
    for j in range(K):
        for m in range(1, M + 1):
            if j + m <= K:
                dp[i + 1][j + m] += dp[i][j]
                dp[i + 1][j + m] %= MOD
print(sum(dp[N]) % MOD)
