from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
    t, x, a = map(int, input().split())
    d[(t, x)] = a
INF = float('inf')
dp = [[0, 0, 0, 0, 0]for _ in range(t+2)]
dp[0] = [0, -INF, -INF, -INF, -INF]
for i in range(1, t+2):
    for j in range(5):
        dp[i][j] = dp[i-1][j]+d[(i, j)]
        if j != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+d[(i, j)])
        if j != 4:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1]+d[(i, j)])
ans = max(dp[t])
print(ans)
