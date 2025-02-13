N, M, Q = map(int, input().split())
INF = 1 << 60
cost = [[INF] * N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0
Road = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = cost[b][a] = c
    Road.append((a, b, c))
ans = []
Queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    Queries.append(query)
    if query[0] == 1:
        a, b, c = Road[query[1] - 1]
        cost[a][b] = cost[b][a] = INF
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
Queries = Queries[::-1]
for i in range(Q):
    query = Queries[i]
    if query[0] == 1:
        a, b, c = Road[query[1] - 1]
        cost[a][b] = cost[b][a] = min(cost[a][b], c)
        for i in range(N):
            for j in range(N):
                cost[i][j] = min(
                    cost[i][j],
                    cost[i][a] + cost[b][j] + cost[a][b],
                    cost[i][b] + cost[a][j] + cost[b][a],
                )
    elif query[0] == 2:
        x, y = query[1:]
        x -= 1
        y -= 1
        temp = cost[x][y]
        if temp == INF:
            temp = -1
        ans.append(temp)
print(*ans[::-1], sep="\n")
