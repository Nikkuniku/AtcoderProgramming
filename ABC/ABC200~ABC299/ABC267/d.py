n, m = map(int, input().split())
a = list(map(int, input().split()))

INF = 1000_000_000_000_000
dp = [[-INF]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

for i in range(n):
    for j in range(1, m+1):
        dp[i+1][j] = max(dp[i][j], dp[i][j-1]+j*a[i])

ans = dp[n][m]
print(ans)
