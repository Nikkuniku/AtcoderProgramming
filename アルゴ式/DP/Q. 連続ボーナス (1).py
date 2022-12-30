N, A = map(int, input().split())
Cost = [list(map(int, input().split())) for _ in range(3)]
INF = 1 << 60
dp = [[INF]*3 for _ in range(N+1)]
dp[0] = [0]*3
for i in range(N):
    if i == 0:
        for j in range(3):
            for k in range(3):
                dp[i+1][j] = min(dp[i+1][j], dp[i][k]+Cost[j][i])
        continue
    for j in range(3):
        for k in range(3):
            dp[i+1][j] = min(dp[i+1][j], dp[i][k]+Cost[j]
                             [i]+(-A if k == j else 0))
ans=min(dp[N])
print(ans)
