def f(t, C, D):
    if t + 1 == 0:
        return 1 << 60
    return t + (D // (t + 1)) + C


from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, d))
    Edge[b].append((a, c, d))
INF = 1 << 60
dist = [INF] * N
dist[0] = 0
q = [(0, 0)]
heapify(q)
while q:
    d, v = heappop(q)
    if d > dist[v]:
        continue
    for u, C, D in Edge[v]:
        min_dist = INF
        if d <= int(D**0.5):
            for p in range(int(D**0.5) - 2, int(D**0.5) + 2):
                if d + p < 0:
                    continue
                min_dist = min(min_dist, f(d + p, C, D))
        else:
            min_dist = min(min_dist, f(d, C, D))
        if dist[u] > min_dist:
            dist[u] = min_dist
            heappush(q, (dist[u], u))
ans = dist[-1]
if ans == INF:
    ans = -1
print(ans)
