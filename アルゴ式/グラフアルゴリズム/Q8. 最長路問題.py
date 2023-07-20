N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]
INF = 1 << 60
dp = [-INF]*N
dp[0] = 0
for cnt in range(N):
    for u, v, w in Edge:
        if dp[v] < dp[u]+w:
            dp[v] = dp[u]+w
ans = dp[-1]
print(ans)
