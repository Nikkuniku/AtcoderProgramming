from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append((v, b))
    Edge[v].append((u, b))
INF = 1 << 60
dist = [INF] * N
dist[0] = A[0]
q = [(0, dist[0])]
while q:
    v, d = heappop(q)
    if dist[v] > d:
        continue
    for to, cost in Edge[v]:
        if dist[v] + cost + A[to] < dist[to]:
            dist[to] = dist[v] + cost + A[to]
            q.append((to, dist[to]))
print(*dist[1:])
