from collections import deque
from math import log2

n = int(input())
edge = [[]for _ in range(n)]
k = int(log2(n))+1
next = [[-1]*n for _ in range(k)]

for _ in range(n-1):
    a, b, di = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append((b, di))
    edge[b].append((a, di))

d = deque([0])
dist = [-1]*n
dist_c = [-1]*n
dist[0] = 0
dist_c[0] = 0
while d:
    v = d.popleft()
    for e, di in edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            dist_c[e] = dist_c[v]+di
            next[0][e] = v
            d.append(e)
for i in range(1, k):
    for j in range(n):
        if next[i-1][j] == -1:
            continue
        next[i][j] = next[i-1][next[i-1][j]]


def query(u, v):
    # uの方が深いとする
    if dist[u] < dist[v]:
        u, v = v, u
    uv = dist[u]-dist[v]
    for p in range(k):
        if (uv >> p) & 1:
            u = next[p][u]
    if u == v:
        return u
    for p in range(k-1, -1, -1):
        if next[p][u] != next[p][v]:
            u = next[p][u]
            v = next[p][v]
    return next[0][u]


def distance(u, v):
    u, v = u-1, v-1
    lca = query(u, v)
    return dist_c[u] + dist_c[v] - 2*dist_c[lca]


q, K = map(int, input().split())
ans = []
for _ in range(q):
    x, y = map(int, input().split())
    ans.append(distance(x, K)+distance(K, y))
print(*ans, sep="\n")
