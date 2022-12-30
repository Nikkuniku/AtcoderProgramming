from collections import defaultdict
n, m = map(int, input().split())
x = list(map(int, input().split()))
d = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    d[c] = y

dp = [[0]*(n+2) for _ in range(n+1)]

mx = 0
for i in range(n):
    for j in range(1, i+2):
        if j == 1:
            dp[i+1][j] = mx+x[i]+d[j]
        else:
            dp[i+1][j] = dp[i][j-1]+x[i]+d[j]

    mx = max(dp[i])

ans = max(dp[n])
print(ans)
