N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 30
dp = [[-INF]*(K+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    dp[i+1][0] = max(dp[i][0], dp[i][K])+A[i]
    for j in range(1, K+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j-1])
        if j == K:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
print(max(dp[N][0], dp[N][K]))
