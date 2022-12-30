from heapq import heappush, heappop
n, m, x, y = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, t, k))
    edge[b].append((a, t, k))

INF = 10**18


def dijkstra(s, n):
    dist = [INF]*n
    hq = [(0, s)]
    dist[s] = 0
    mindist = [INF]*n
    seen = [False]*n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        if seen[y-1]:
            return dist
        for to, cost, s_time in edge[v]:
            if not seen[to] and dist[v]+(s_time - (dist[v] % s_time)) % s_time+cost < dist[to]:
                dist[to] = dist[v]+(s_time - (dist[v] % s_time)) % s_time+cost
                if dist[to] < mindist[to]:
                    heappush(hq, (dist[to], to))
                    mindist[to] = dist[to]
    return dist


ans = dijkstra(x-1, n)
if ans[y-1] == INF:
    ans = -1
else:
    ans = ans[y-1]
print(ans)
