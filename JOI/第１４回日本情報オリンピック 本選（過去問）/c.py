from collections import defaultdict
from heapq import heappop, heappush

N, M, C = map(int, input().split())
S = 0
Edge = [[] for _ in range(N)]
for i in range(M):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, d, i))
    Edge[b].append((a, d, i))
    S += d
INF = 1 << 60
dist = [INF] * N
dist[0] = 0
q = [(0, 0)]
while q:
    v, d = heappop(q)
    if d > dist[v]:
        continue
    for to, cost, _ in Edge[v]:
        if dist[v] + cost < dist[to]:
            dist[to] = dist[v] + cost
            heappush(q, (to, dist[to]))
ans = 1 << 60
d = defaultdict(list)
for i, v in enumerate(dist):
    d[v].append(i)
cost_list = sorted(d.keys())
tmp = 0
seen_edges = [False] * M
for cost in cost_list:
    for v in d[cost]:
        for e, c, i in Edge[v]:
            if seen_edges[i]:
                continue
            if dist[e] <= cost:
                seen_edges[i] = True
                tmp += c
    tmp_val = C * cost + (S - tmp)
    ans = min(ans, tmp_val)
print(ans)
