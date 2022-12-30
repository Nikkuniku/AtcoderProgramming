N = int(input())
books = [list(map(int, input().split())) for _ in range(N)]
INF = 1 << 62
dp = [[INF]*N for _ in range(1 << N)]
for i in range(N):
    dp[1 << i][i] = 0

for s in range(1 << N):
    for u in range(N):
        if not s & (1 << u) and s != 0:
            continue
        for v in range(N):
            if s & (1 << v):
                continue
            dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v], max(
                dp[s][u], books[u][1]-books[u][0]+books[v][0]))

print(min(dp[(1 << N)-1]))
