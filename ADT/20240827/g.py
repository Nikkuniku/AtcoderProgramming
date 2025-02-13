from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append((v, b + A[v]))
    Edge[v].append((u, b + A[u]))
INF = 1 << 60
dist = [INF] * N
dist[0] = A[0]
q = [(dist[0], 0)]
while q:
    d, v = heappop(q)
    if dist[v] != d:
        continue
    for to, cost in Edge[v]:
        if dist[v] + cost < dist[to]:
            dist[to] = dist[v] + cost
            heappush(q, (dist[to], to))
print(*dist[1:])
