from collections import deque

N, M = map(int, input().split())
Edges = []
G = [[] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    Edges.append((x, y, z))
    G[x].append((y, z))
    G[y].append((x, z))
INF = 1 << 60
L = 30
dist = [[INF] * L for _ in range(N)]


def BFS(s):
    for b in range(L):
        q = deque([s])
        dist[s][b] = 0
        while q:
            v = q.popleft()
            for to, z in G[v]:
                # ビットがたっている時
                if z & (1 << b):
                    if dist[to][b] != INF:
                        if dist[v][b] == dist[to][b]:
                            exit(print(-1))
                    else:
                        dist[to][b] = dist[v][b] ^ 1
                        q.append(to)
                else:
                    if dist[to][b] != INF:
                        if dist[v][b] != dist[to][b]:
                            exit(print(-1))
                    else:
                        dist[to][b] = dist[v][b]
                        q.append(to)


BFS(0)
A = []
for b in range(L):
    v0 = 0
    v1 = 0
    for v in range(N):
        if dist[v][b] == 0:
            v0 += 1
        else:
            v1 += 1
    if v0 <= v1:
        A.append(0)
    else:
        A.append(1)
dist = [INF] * N

p = 0
for b in range(L):
    p += (1 << b) * A[b]


def BFS2(s):
    q = deque([s])
    dist[s] = p
    while q:
        v = q.popleft()
        for to, z in G[v]:
            if dist[to] != INF:
                if dist[v] ^ dist[to] != z:
                    exit(print(-1))
            else:
                dist[to] = dist[v] ^ z
                q.append(to)


BFS2(0)
print(*dist)
