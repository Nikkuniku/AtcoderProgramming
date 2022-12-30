V, E = map(int, input().split())
INF = 1 << 62
Edge = [[INF]*V for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    Edge[s][t] = d
dp = [[INF]*(1 << V) for _ in range(V)]
dp[0][0] = 0

for s in range(1 << V):
    for u in range(V):
        if not s & (1 << u) and s != 0:
            continue
        for v in range(V):
            if s & (1 << v):
                continue
            dp[v][s | (1 << v)] = min(dp[u][s]+Edge[u][v], dp[v][s | (1 << v)])

ans = dp[0][(1 << V)-1]
if ans == INF:
    ans = -1
print(ans)
