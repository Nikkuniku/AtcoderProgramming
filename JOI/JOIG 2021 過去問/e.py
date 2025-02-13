from heapq import heappop, heappush

N, M, L = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, True))
    Edge[b].append((a, c, False))
INF = 1 << 60
dist = [[INF] * N for _ in range(M + 1)]
dist[0][0] = 0
q = [(0, 0, 0)]
while q:
    d, v, k = heappop(q)
    if dist[k][v] < d:
        continue
    for to, cost, isSt in Edge[v]:
        if d + cost > L:
            continue
        if isSt:
            if dist[k][v] + cost < dist[k][to]:
                dist[k][to] = dist[k][v] + cost
                heappush(q, (dist[k][to], to, k))
        else:
            if k + 1 > M:
                continue
            if dist[k][v] + cost < dist[k + 1][to]:
                dist[k + 1][to] = dist[k][v] + cost
                heappush(q, (dist[k + 1][to], to, k + 1))
ans = M
for i in range(M + 1):
    if dist[i][N - 1] <= L:
        ans = min(ans, i)
        break
else:
    ans = -1
print(ans)
