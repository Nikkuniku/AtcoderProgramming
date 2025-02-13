from collections import deque
from heapq import heappop, heappush

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
Edge = [[] for _ in range(N)]
dist = [-1] * N
q = deque()
for _ in range(K):
    C = int(input())
    C -= 1
    dist[C] = 0
    q.append(C)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v] + 1
        q.append(e)
INF = 1 << 60
dp = [INF] * N
dp[0] = 0
q = [(dp[0], 0)]
while q:
    d, v = heappop(q)
    if d > dp[v]:
        continue
    for to in Edge[v]:
        if dist[to] == 0 and to != 0:
            continue
        if to == N - 1:
            if d < dp[to]:
                dp[to] = d
                heappush(q, (dp[to], to))
        if dist[to] <= S:
            if d + Q < dp[to]:
                dp[to] = d + Q
                heappush(q, (dp[to], to))
        else:
            if d + P < dp[to]:
                dp[to] = d + P
                heappush(q, (dp[to], to))
print(dp[N - 1])
