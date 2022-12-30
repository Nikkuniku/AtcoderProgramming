N = int(input())
M = 2
P = [list(map(int, input().split())) for _ in range(2)]
INF = 1 << 60
dp = [[INF]*4 for _ in range(N+1)]
dp[0] = [0]*4
for i in range(N):
    for j in range(1 << M):
        for k in range(1 << M):
            if j & k == 0:
                continue
            tmp = 0
            for m in range(M):
                if j & (1 << m):
                    tmp += P[m][i]
            dp[i+1][j] = min(dp[i+1][j], dp[i][k]+tmp)
print(min(dp[N]))
