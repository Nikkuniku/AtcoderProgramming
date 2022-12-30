N, A, B = map(int, input().split())
Cost = [list(map(int, input().split())) for _ in range(3)]
INF = 1 << 60
dp = [[[INF]*4 for _ in range(3)] for _ in range(N+1)]
for j in range(3):
    dp[0][j][0] = 0

for i in range(N):
    for j in range(3):
        for k in range(1, 4):
            for s in range(3):
                if j == s:
                    tmp = dp[i][j][k-1]+Cost[j][i]
                    if k == 2:
                        tmp -= A
                    if k == 3:
                        tmp -= B
                        tmp = min(tmp, dp[i][j][k]+Cost[j][i]-B)
                    dp[i+1][j][k] = min(dp[i+1][j][k], tmp)
                else:
                    for t in range(1, 4):
                        dp[i+1][j][1] = min(dp[i+1][j][1],
                                            dp[i][s][t]+Cost[j][i])
ans = min(sum(dp[N], []))
print(ans)
