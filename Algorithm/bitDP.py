n, m = map(int, input().split())
INF = 10**18
dist = [[INF]*n for _ in range(n)]
for _ in range(m):
    s, t, d = map(int, input().split())
    s, t = s-1, t-1
    dist[s][t] = d

dp = [[INF]*n for _ in range((1 << n))]
dp[0][0] = 0

for s in range(1 << n):
    for v in range(n):
        for u in range(n):
            if not (s >> u) & 1 and s != 0:
                continue
            if (s >> v) & 1 == 0:
                if dp[s][u]+dist[u][v] < dp[s | (1 << v)][v]:
                    dp[s | (1 << v)][v] = dp[s][u]+dist[u][v]

if dp[2**n-1][0] != INF:
    print(dp[2**n-1][0])
else:
    print(-1)
