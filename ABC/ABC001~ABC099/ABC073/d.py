N, M, R = map(int, input().split())
town = list(map(int, input().split()))
INF = 1 << 62
dist = [[INF]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c


def WarshallFloyd(d):
    for i in range(N):
        d[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

    return d


dist = WarshallFloyd(dist)


dp = [[INF]*R for _ in range(1 << R)]
for i in range(R):
    dp[1 << i][i] = 0
for s in range(1 << R):
    for v in range(R):
        for u in range(R):
            if not (s >> u) & 1 and s != 0:
                continue
            if not (s >> v) & 1:
                dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v],
                                          dp[s][u]+dist[town[u]-1][town[v]-1])
print(min(dp[(1 << R)-1]))
