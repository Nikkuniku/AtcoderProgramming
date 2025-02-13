from heapq import heappush, heappop

N, M, W = map(int, input().split())
Edge = [[] for _ in range(N)]
INF = 1 << 60
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, -c))
l = 0
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    dist = [-INF] * N
    hq = [(0, 0)]
    dist[0] = W
    seen = [False] * N
    K = mid
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in Edge[v]:
            if dist[to] < dist[v] + (-cost):
                dist[to] = dist[v] + (-cost)
                dist[to] -= K
                if dist[to] > 0:
                    heappush(hq, (-dist[to], to))
    if dist[-1] >= 0:
        l = mid
    else:
        r = mid
print(l)
