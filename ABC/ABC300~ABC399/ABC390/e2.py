N, X = map(int, input().split())
INF = 1 << 60
dp = [[[-INF] * (X + 1) for _ in range(3)] for _ in range(N + 1)]
for i in range(3):
    dp[0][i][0] = 0
for i in range(N):
    v, a, c = map(int, input().split())
    for x in range(X + 1):
        for k in range(3):
            dp[i + 1][k][x] = dp[i][k][x]
        if x - c >= 0:
            dp[i + 1][v - 1][x] = max(dp[i + 1][v - 1][x], dp[i][v - 1][x - c] + a)
# M[i][j]:摂取カロリーがj以下となるようにビタミンiを摂取した時の最大値
M = [[0] * (X + 1) for _ in range(3)]
for i in range(3):
    for j in range(1, X + 1):
        M[i][j] = max(M[i][j - 1], dp[N][i][j])
ans = -1
for i in range(X + 1):
    for j in range(X - i):
        k = X - i - j
        temp = min(M[0][i], M[1][j], M[2][k])
        ans = max(ans, temp)
print(ans)
