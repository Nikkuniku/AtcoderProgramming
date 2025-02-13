N, M, K = map(int, input().split())
MOD = 998244353
dp = [[0] * (N * M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(N * M + 1):
        for k in range(1, M + 1):
            if j + k <= N * M:
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= MOD
ans = 0
for j in range(K + 1):
    ans += dp[N][j]
    ans %= MOD
print(ans)
