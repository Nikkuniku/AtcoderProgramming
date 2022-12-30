N, M = map(int, input().split())
edge = [0]*N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[y] |= (1 << x)
dp = [[0]*N for _ in range(1 << N)]
dp[0][0] = 1
for s in range(1 << N):
    for u in range(N):
        if not s & (1 << u) and s != 0:
            continue
        for v in range(N):
            if s & (1 << v):
                continue
            if s & edge[v] == edge[v]:
                dp[s | (1 << v)][v] += dp[s][u]
print(sum(dp[(1 << N)-1]))
