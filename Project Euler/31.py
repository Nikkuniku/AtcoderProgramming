Coins = [1, 2, 5, 10, 20, 50, 100, 200]
N = len(Coins)
M = 200
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    c = Coins[i]
    for m in range(M + 1):
        dp[i + 1][m] += dp[i][m]
        if m + c <= M:
            dp[i + 1][m + c] += dp[i][m]
print(dp[N][M])
