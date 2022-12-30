from heapq import heappush, heappop
N, K = map(int, input().split())
adj = [[] for _ in range(N)]
INF = 1 << 30


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


ans = []
for _ in range(K):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 0:
        a, b = query[1:]
        a, b = a-1, b-1
        dist = dijkstra(a, N)
        ans.append(-1 if dist[b] == INF else dist[b])
    else:
        c, d, e = query[1:]
        c, d = c-1, d-1
        adj[c].append((d, e))
        adj[d].append((c, e))
print(*ans, sep="\n")
