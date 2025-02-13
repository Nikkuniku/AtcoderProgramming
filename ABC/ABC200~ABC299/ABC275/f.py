N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 60
dp = [[[INF] * (M + 1) for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for k in range(M + 1):
        if k - A[i] >= 0:
            dp[i + 1][0][k] = min(dp[i][0][k - A[i]], dp[i][1][k - A[i]])
        dp[i + 1][1][k] = min(dp[i][0][k] + 1, dp[i][1][k])
ans = []
for k in range(1, M + 1):
    tmp = min(dp[N][0][k], dp[N][1][k])
    if tmp == INF:
        tmp = -1
    ans.append(tmp)
print(*ans, sep="\n")
