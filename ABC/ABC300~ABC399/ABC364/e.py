N, X, Y = map(int, input().split())
INF = 1 << 60
dp = [[[INF] * (X + 1) for _ in range(N + 1)] for _ in range(N + 1)]
goods = [list(map(int, input().split())) for _ in range(N)]
dp[0][0][0] = 0
for i in range(N):
    x, y = goods[i]
    for k in range(i + 1):
        for a in range(X + 1):
            # 選ばない
            dp[i + 1][k][a] = min(dp[i + 1][k][a], dp[i][k][a])
            # 選ぶ
            if a + x <= X:
                dp[i + 1][k + 1][a + x] = min(dp[i + 1][k + 1][a + x], dp[i][k][a] + y)
ans = -1
for k in range(N + 1):
    isOK = False
    for x in range(X + 1):
        if dp[N][k][x] <= Y:
            isOK = True
    if not isOK:
        ans = max(ans, k)
        break
if ans == -1:
    ans = N
print(ans)
