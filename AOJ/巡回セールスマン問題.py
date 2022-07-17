V, E = map(int, input().split())
S = 1 << V
INF = 10**8
dp = [[INF]*V for _ in range(S)]
dp[0][0] = 0
cost = [[INF]*V for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    cost[s][t] = d
for s in range(S):
    for u in range(V):
        if dp[s][u] == INF:
            continue
        if not (s >> u) and s != 0:
            continue
        for v in range(V):
            if s & (1 << v):
                continue
            if dp[s | (1 << v)][v] > dp[s][u]+cost[u][v]:
                dp[s | (1 << v)][v] = dp[s][u]+cost[u][v]

ans = dp[S-1][0]
if ans == INF:
    ans = -1
print(ans)
