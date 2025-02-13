N = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
Edge = [[] for _ in range(N)]
INF = 1 << 60
dist = [INF] * N
dp = [0] * N
dist[a] = 0
dp[a] = 1
MOD = 1000_000_007
from collections import deque

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)

q = deque([a])
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[v] + 1 <= dist[e]:
            if dist[e] == INF:
                q.append(e)
            dist[e] = dist[v] + 1
            dp[e] += dp[v]
            dp[e] %= MOD
ans = dp[b]
print(ans)
