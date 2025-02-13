N, P = map(int, input().split())
dp = [[-(1 << 60)] * (P + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    a, b = map(int, input().split())
    for p in range(P + 1):
        if p - a >= 0:
            dp[i + 1][p] = max(dp[i + 1][p], dp[i][p - a] + b)
        dp[i + 1][p] = max(dp[i + 1][p], dp[i][p])
print(max(dp[N]))
