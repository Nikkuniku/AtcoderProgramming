from heapq import heappop, heappush

N, M, P, Y = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    Edge[b].append((a, c))
Shop = [-1] * N
for _ in range(P):
    d, e = map(int, input().split())
    Shop[d - 1] = e
dist = [-1] * N
dist[0] = Y
q = [(-Y, 0)]
while q:
    d, v = heappop(q)
    if dist[v] != -d:
        continue
    for to, c in Edge[v]:
        if dist[to] < max(-d - c, 0):
            dist[to] = max(-d - c, 0)
            heappush(q, (-dist[to], to))
ans = 0
for v in range(N):
    if Shop[v] == -1:
        continue
    ans = max(ans, dist[v] // Shop[v])
print(ans)
