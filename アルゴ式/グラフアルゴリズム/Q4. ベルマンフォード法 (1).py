N, M = map(int, input().split())
INF = 10**9
dist = [INF]*N
dist[0] = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    dist[v] = min(dist[v], dist[u]+w)
print(*dist, sep="\n")
