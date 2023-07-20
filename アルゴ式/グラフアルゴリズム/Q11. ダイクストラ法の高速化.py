from heapq import heappop, heappush, heapify
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    Edge[u].append((w, v))
INF = 1 << 30
dp = [INF]*N
dp[0] = 0
visited = [False]*N
q = [(0, 0)]
heapify(q)
while q:
    d, v = heappop(q)
    if visited[v]:
        continue
    for cost, to in Edge[v]:
        if visited[to]:
            continue
        if dp[to] > dp[v]+cost:
            dp[to] = dp[v]+cost
            heappush(q, (dp[to], to))
    visited[v] = True
print(*dp, sep="\n")
