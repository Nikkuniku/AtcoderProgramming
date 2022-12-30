from heapq import heappush, heappop
from collections import defaultdict
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
d = defaultdict(int)
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    d[(a, b)] = i+1
    d[(b, a)] = i+1
    adj[a].append((b, c))
    adj[b].append((a, c))


def dijkstra(s, n):  # (始点, ノード数)
    INF = 1 << 62
    dist = [INF] * n
    prev = [-1]*n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        if seen[v]:
            continue
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                prev[to] = v
                heappush(hq, (dist[to], to))
    return dist, prev


dist, prev = dijkstra(0, N)

ans = []
for t in range(N):
    if t == 0:
        continue
    s = prev[t]
    ans.append(d[(s, t)])
print(*ans)
