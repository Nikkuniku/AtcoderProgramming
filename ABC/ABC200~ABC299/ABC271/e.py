n, m, k = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(m)]
E = list(map(int, input().split()))
INF = float('inf')
dp = [INF]*(n+1)
dp[1] = 0
for i in range(k):
    j = E[i]-1
    a, b, c = edge[j]
    if dp[a] == -1:
        continue
    dp[b] = min(dp[b], dp[a]+c)

ans = dp[n]
if ans == INF:
    print(-1)
else:
    print(ans)
