N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
booster = [list(map(int, input().split())) for _ in range(M)]
points = [[0, 0]]+booster+town
V = len(points)
INF = float('inf')
dp = [[INF]*(1 << V) for _ in range(V)]
dp[0][0] = 0
for s in range(1 << V):
    speed = 1
    for i in range(M):
        if s & (1 << (i+1)):
            speed *= 2
    for u in range(V):
        if not s & (1 << u) and s != 0:
            continue
        sx, sy = points[u]
        for v in range(V):
            if s & (1 << v):
                continue
            gx, gy = points[v]
            dist = ((sx-gx)**2 + (sy-gy)**2)**(1/2)
            if dp[v][s | (1 << v)] > dp[u][s]+dist/speed:
                dp[v][s | (1 << v)] = dp[u][s]+dist/speed
p = (((1 << N)-1) << (M+1)) | 1
ans = INF
for i in range(1 << M):
    q = p | (i << 1)
    ans = min(ans, dp[0][q])
print(ans)
