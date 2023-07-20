N, M = map(int, input().split())
dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    a, b = map(int, input().split())
    for j in range(M+1):
        if dp[i][j] >= 0:
            dp[i+1][j] = b
        if j-a >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i+1][j-a]-1)
ans = 'No'
if dp[N][M] >= 0:
    ans = 'Yes'
print(ans)
