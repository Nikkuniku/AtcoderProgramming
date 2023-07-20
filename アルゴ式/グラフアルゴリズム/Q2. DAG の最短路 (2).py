N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    Edge[u].append((v, w))
INF = 1 << 30
dist = [INF]*N
dist[0] = 0
for v in range(N):
    for e, c in Edge[v]:
        dist[e] = min(dist[e], dist[v]+c)
ans = -1 if dist[N-1] == INF else dist[N-1]
print(ans)
