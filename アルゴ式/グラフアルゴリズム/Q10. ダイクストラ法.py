N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    Edge[u].append((w, v))
s = 0
F = [False]*N
INF = 1 << 30
dp = [INF]*N
dp[s] = 0
while 1:
    v, d = -1, INF
    for i in range(N):
        if not F[i] and d > dp[i]:
            v = i
            d = dp[i]
    for cost, e in Edge[v]:
        if F[e]:
            continue
        dp[e] = min(dp[e], dp[v]+cost)
    F[v] = True
    if False not in F:
        break
print(*dp, sep="\n")
