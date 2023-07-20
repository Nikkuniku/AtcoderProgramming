N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 30
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for s in range(M+1):
        dp[i+1][s] = dp[i][s]
        if s-A[i] >= 0:
            dp[i+1][s] = min(dp[i+1][s], dp[i][s-A[i]]+1)
ans = -1 if dp[N][M] == INF else dp[N][M]
print(ans)
