N = int(input())
X, Y = map(int, input().split())
INF = 1 << 60
dp = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    a, b = map(int, input().split())
    for x in range(X + 1):
        for y in range(Y + 1):
            dp[i + 1][x][y] = min(dp[i + 1][x][y], dp[i][x][y])
            if dp[i + 1][min(x + a, X)][min(y + b, Y)] > dp[i][x][y] + 1:
                dp[i + 1][min(x + a, X)][min(y + b, Y)] = dp[i][x][y] + 1
ans = dp[N][X][Y]
if ans == INF:
    ans = -1
print(ans)
