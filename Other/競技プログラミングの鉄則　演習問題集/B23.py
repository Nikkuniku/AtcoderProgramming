N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def dist(X, Y):
    return ((X[0]-Y[0])**2 + (X[1]-Y[1])**2)**(1/2)


INF = 1 << 62
dp = [[INF]*N for _ in range(1 << N)]
dp[0][0] = 0
for s in range(1 << N):
    for u in range(N):
        for v in range(N):
            if not s & (1 << u) and s != 0:
                continue
            if s & (1 << v):
                continue
            dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v],
                                      dp[s][u]+dist(points[u], points[v]))

ans = dp[-1][0]
print(ans)
