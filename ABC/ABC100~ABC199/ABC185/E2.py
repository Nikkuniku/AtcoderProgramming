N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
INF = 1 << 60
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N+1):
    for j in range(M+1):
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
ans = dp[N][M]
print(ans)
