N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]
INF = 1 << 60
dp = [INF]*N
prev = [-1]*N
dp[0] = 0
for cnt in range(N):
    for u, v, w in Edge:
        if dp[v] > dp[u]+w:
            dp[v] = dp[u]+w
            prev[v] = u
now = N-1
ans = []
while now != -1:
    ans.append(now)
    now = prev[now]
print(len(ans))
print(*ans[::-1])
