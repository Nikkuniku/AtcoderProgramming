N, M = map(int, input().split())
INF = 1 << 60
cost = [[INF] * N for _ in range(N)]
for v in range(N):
    cost[v][v] = 0
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = cost[b][a] = c
    Edge[a].append((b, c))
    Edge[b].append((a, c))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
S = 0
for i in range(N):
    for j in range(i + 1, N):
        S += cost[i][j]
K = int(input())
ans = []
for _ in range(K):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if cost[x][y] <= z:
        ans.append(S)
        continue
    for i in range(N):
        for j in range(i + 1, N):
            tmp = min(cost[i][x] + z + cost[y][j], cost[j][x] + z + cost[y][i])
            if cost[i][j] <= tmp:
                continue
            diff = tmp - cost[i][j]
            cost[i][j] = cost[j][i] = tmp
            S += diff
    ans.append(S)
print(*ans, sep="\n")
