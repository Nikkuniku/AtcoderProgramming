from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, i))
    Edge[b].append((a, c, i))
q = [(0, 0)]
dist = [1e18] * N
dist[0] = 0
ans = [-1] * N
while q:
    d, v = heappop(q)
    if d != dist[v]:
        continue
    for to, cost, j in Edge[v]:
        if dist[v] + cost < dist[to]:
            dist[to] = dist[v] + cost
            heappush(q, (dist[to], to))
            ans[to] = j
print(*[ans[i] + 1 for i in range(1, N)])
