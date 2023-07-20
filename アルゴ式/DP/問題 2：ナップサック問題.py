N, W = map(int, input().split())
dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    wi, vi = map(int, input().split())
    for w in range(W+1):
        dp[i+1][w] = dp[i][w]
        if w-wi >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-wi]+vi)
print(dp[N][W])
