N = int(input())
P = [list(map(int, input().split())) for _ in range(3)]
INF = 1 << 30
dp = [[INF]*3 for _ in range(N+1)]
dp[1] = [0]*3
for i in range(1, N):
    for j in range(3):
        for k in range(3):
            dp[i+1][j] = min(dp[i+1][j], dp[i][k]+abs(P[j][i]-P[k][i-1]))
print(min(dp[N]))
