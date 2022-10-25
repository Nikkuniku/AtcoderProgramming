N, M = map(int, input().split())
W = list(map(int, input().split()))
INF = 1 << 10
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M+1):
        # No Choice
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if j-W[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-W[i]]+1)
ans = dp[N][M]
if ans == INF:
    ans = -1
print(ans)
