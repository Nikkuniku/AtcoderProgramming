from heapq import heappush, heappop

INF = 1 << 60


N = int(input())
edge = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, x = map(int, input().split())
    edge[i].append((i + 1, a))
    if i == x - 1:
        continue
    edge[i].append((x - 1, b))


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in edge[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


res = dijkstra(0, N)[-1]
print(res)
