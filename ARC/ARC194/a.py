N = int(input())
A = list(map(int, input().split()))
INF = 1 << 60
dp = [[[-INF] * 2 for _ in range(2)] for _ in range(N + 1)]
dp[0] = [[0, 0], [0, 0]]
for i, v in enumerate(A):
    # 取る
    dp[i + 1][i % 2][0] = max(dp[i + 1][i % 2][0], max(dp[i][1 - i % 2]) + v)
    # 取らない
    if i > 0:
        dp[i + 1][i % 2][1] = max(dp[i + 1][i % 2][1], max(dp[i - 1][i % 2]))
ans = -INF
for i in range(2):
    ans = max(ans, max(dp[N][i]))
print(ans)
