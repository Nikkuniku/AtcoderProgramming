n, W = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*(W+1) for _ in range(n+1)]
for i in range(n):
    w, v = goods[i]
    for j in range(W+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j-w >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-w]+v)

print(dp[n][W])
