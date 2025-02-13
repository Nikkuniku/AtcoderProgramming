from heapq import heappop, heappush


def dijkstra(N, edge, s):
    INF = 1 << 60
    dist = [INF] * N
    dist[s] = 0
    q = [(dist[s], s)]
    while q:
        d, v = heappop(q)
        if d != dist[v]:
            continue
        for to, c in edge[v]:
            if d + c < dist[to]:
                dist[to] = d + c
                heappush(q, (dist[to], to))
    return dist


N, M, T = map(int, input().split())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
inv_Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    inv_Edge[b].append((a, c))

dist = dijkstra(N, Edge, 0)
dist2 = dijkstra(N, inv_Edge, 0)
ans = -1
for v in range(N):
    t = max(0, T - dist[v] - dist2[v])
    ans = max(ans, A[v] * t)
print(ans)
