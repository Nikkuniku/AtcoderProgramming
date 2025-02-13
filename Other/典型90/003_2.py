from collections import deque


def bfs(n, edge, s):
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


N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
dist1 = bfs(N, Edge, 0)
m = dist1.index(max(dist1))
ans = max(bfs(N, Edge, m)) + 1
print(ans)
