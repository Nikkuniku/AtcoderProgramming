from collections import deque

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
C = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] < H[b]:
        Edge[a].append(b)
    if H[b] < H[a]:
        Edge[b].append(a)
dist = [-1] * N
q = deque()
for v in C:
    dist[v - 1] = 0
    q.append(v - 1)
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v] + 1
        q.append(e)
print(*dist, sep="\n")
