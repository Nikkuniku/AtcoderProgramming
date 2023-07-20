from heapq import heappush, heappop
N, M = map(int, input().split())
H = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if H[u] >= H[v]:
        Edge[u].append((v, 0))
        Edge[v].append((u, H[u]-H[v]))
    else:
        Edge[v].append((u, 0))
        Edge[u].append((v, H[v]-H[u]))

INF = 10 ** 9


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in Edge[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


cost = dijkstra(0, N)
for i in range(N):
    cost[i] += H[i]-H[0]
    cost[i] *= -1
ans = max(cost)
print(ans)
