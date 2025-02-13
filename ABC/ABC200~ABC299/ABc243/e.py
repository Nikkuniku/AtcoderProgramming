from heapq import heapify, heappop, heappush
from collections import defaultdict

N, M = map(int, input().split())
INF = 10**18
cost = [[INF] * N for _ in range(N)]
Edge = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = cost[b][a] = c
    Edge.append((a, b, c))

INF = 10**18
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
ans = 0
for a, b, c in Edge:
    unused = 0
    if cost[a][b] != c:
        unused = 1
    for k in range(N):
        if cost[a][k] + cost[k][b] <= c:
            unused = 1
    ans += unused
print(ans)
