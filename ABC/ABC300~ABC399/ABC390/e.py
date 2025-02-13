N, X = map(int, input().split())
INF = 1 << 60
dp = [[[INF] * 3 for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = [0, 0, 0]
for i in range(N):
    v, a, c = map(int, input().split())
    for x in range(X + 1):
        for k in range(3):
            dp[i + 1][x][k] = min(dp[i + 1][x][k], dp[i][x][k])
        if x - c >= 0:
            p = min(dp[i + 1][x])
            if v == 1:
                if dp[i][x - c][0] + a <= p:
                    dp[i + 1][x][0] = min(dp[i + 1][x][0], dp[i][x - c][0] + a)
                    dp[i + 1][x][1] = min(dp[i + 1][x][1], dp[i][x][1])
                    dp[i + 1][x][2] = min(dp[i + 1][x][2], dp[i][x][2])
            elif v == 2:
                if dp[i][x - c][1] + a <= p:
                    dp[i + 1][x][0] = min(dp[i + 1][x][0], dp[i][x][0])
                    dp[i + 1][x][1] = min(dp[i + 1][x][1], dp[i][x - c][1] + a)
                    dp[i + 1][x][2] = min(dp[i + 1][x][2], dp[i][x][2])
            elif v == 3:
                if dp[i][x - c][2] + a <= p:
                    dp[i + 1][x][0] = min(dp[i + 1][x][0], dp[i][x][0])
                    dp[i + 1][x][1] = min(dp[i + 1][x][1], dp[i][x][1])
                    dp[i + 1][x][2] = min(dp[i + 1][x][2], dp[i][x - c][2] + a)
print(dp[N][X])
