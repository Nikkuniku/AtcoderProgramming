from collections import deque
from math import log2

n = int(input())
edge = [[]for _ in range(n)]
k = int(log2(n))+1
next = [[-1]*n for _ in range(k)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

d = deque([0])
dist = [-1]*n
dist[0] = 0
while d:
    v = d.popleft()
    for e in edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
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

    for p in range(k):
        if ((dist[u]-dist[v]) >> p) & 1:
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
    c = query(u, v)
    return dist[u]+dist[v]-2*dist[c]


q, K = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    ans = distance(x, K)+distance(K, y)
    print(ans)
