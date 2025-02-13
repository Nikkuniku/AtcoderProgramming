N, M, L = map(int, input().split())
INF = 1 << 60
cost = [[INF] * N for _ in range(N)]
for v in range(N):
    cost[v][v] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = c
    cost[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
dist = [[INF] * N for _ in range(N)]
for v in range(N):
    dist[v][v] = 0
for v in range(N):
    for w in range(N):
        if cost[v][w] <= L:
            dist[v][w] = dist[w][v] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = []
Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    tmp = dist[s][t]
    if tmp == INF:
        tmp = 0
    ans.append(tmp - 1)
print(*ans, sep="\n")
