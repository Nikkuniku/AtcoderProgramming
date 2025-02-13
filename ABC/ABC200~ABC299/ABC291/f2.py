from collections import deque

N, M = map(int, input().split())
Edge_1 = [[] for _ in range(N)]
Edge_N = [[] for _ in range(N)]
S = []
for i in range(N):
    Si = list(input())
    for j in range(M):
        if Si[j] == "1":
            Edge_1[i].append(i + j + 1)
            Edge_N[i + j + 1].append(i)
    S.append(Si)


def BFS(s, n, edge):
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for to in edge[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            q.append(to)
    return dist


dist1 = BFS(0, N, Edge_1)
distN = BFS(N - 1, N, Edge_N)
INF = 1 << 60
ans = [INF] * N
for k in range(1, N - 1):
    tmp = 1 << 60
    for i in range(k - M + 1, k):
        for m in range(M):
            if i + m + 1 <= k:
                continue
            if S[i][m] == "1" and dist1[i] != -1 and distN[i + m + 1] != -1:
                ans[k] = min(ans[k], dist1[i] + distN[i + m + 1] + 1)
for i in range(N):
    if ans[i] == INF:
        ans[i] = -1
print(*ans[1 : N - 1])
