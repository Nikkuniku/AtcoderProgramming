from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append((c, b))
    edge[b].append((c, a))
q = []
heapify(q)
heappush(q, (0, 0))
INF = 10**20
dist = [INF]*n
dist[0] = 0
while q:
    d, v = heappop(q)

    if d > dist[v]:
        continue

    for cost, to in edge[v]:
        if dist[to] > dist[v]+cost:
            dist[to] = dist[v]+cost
            heappush(q, (dist[to], to))

if dist[n-1] == INF:
    print(-1)
else:
    print(dist[n-1])
