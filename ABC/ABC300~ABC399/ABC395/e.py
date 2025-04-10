from heapq import heappop, heappush

N, M, X = map(int, input().split())
Edge = [[] for _ in range(2 * N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append((v, 1))
    Edge[v + N].append((u + N, 1))
for v in range(N):
    Edge[v].append((v + N, X))
    Edge[v + N].append((v, X))
INF = 1 << 60
dist = [INF] * (2 * N)
dist[0] = 0
q = [(dist[0], 0)]
while q:
    d, v = heappop(q)
    if dist[v] != d:
        continue
    for to, cost in Edge[v]:
        if d + cost < dist[to]:
            dist[to] = d + cost
            heappush(q, (dist[to], to))
ans = min(dist[N - 1], dist[2 * N - 1])
print(ans)
