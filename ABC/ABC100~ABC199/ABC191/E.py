from heapq import heappop, heappush
N, M = map(int, input().split())
INF = 1 << 62
adj = [[] for _ in range(N)]
selfloop = [INF]*N
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if a != b:
        adj[a].append([(b, c)])
    else:
        selfloop[a] = min(selfloop[a], c)


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
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
                heappush(hq, (dist[to], to))
    return dist


distance = []
for i in range(N):
    distance.append(dijkstra(i, N))
ans = [INF]*N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans[i] = min(ans[i], distance[i][j]+distance[j][i])

    ans[i] = min(ans[i], selfloop[i])

    if ans[i] == INF:
        ans[i] = -1

print(*ans, sep="\n")
