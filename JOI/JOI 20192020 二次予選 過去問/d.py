from heapq import heappop, heappush

Tenkey = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [0, -1, -1]]
cost = [[1] * 10 for _ in range(10)]
for i in range(4):
    for j in range(3):
        v = Tenkey[i][j]
        if v == -1:
            continue
        for p in range(4):
            for q in range(3):
                w = Tenkey[p][q]
                if w == -1:
                    continue
                cost[v][w] = abs(i - p) + abs(j - q) + 1
M, R = map(int, input().split())
INF = 1 << 60
dist = [INF] * M
dist[0] = 0
q = [(dist[0], 0, 0)]
while q:
    d, v, k = heappop(q)
    if dist[v] < d:
        continue
    for to in range(10):
        next = (v * 10 + to) % M
        if dist[v] + cost[k][to] < dist[next]:
            dist[next] = dist[v] + cost[k][to]
            heappush(q, (dist[next], next, to))
print(dist[R])
