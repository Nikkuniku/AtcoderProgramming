n, ma, mb = map(int, input().split())
med = [tuple(map(int, input().split())) for _ in range(n)]
INF = 1 << 18
dp = [[[INF]*(403) for _ in range(403)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    ai, bi, ci = med[i]
    for a in range(403):
        for b in range(403):
            dp[i+1][a][b] = min(dp[i+1][a][b], dp[i][a][b])
            if a-ai >= 0 and b-bi >= 0:
                dp[i+1][a][b] = min(dp[i+1][a][b], dp[i][a-ai][b-bi]+ci)

ans = INF
for i in range(1, 403):
    if ma*i <= 402 and mb*i <= 402:
        ans = min(ans, dp[n][ma*i][mb*i])
if ans == INF:
    ans = -1
print(ans)
