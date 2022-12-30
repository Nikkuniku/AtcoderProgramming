from collections import deque
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
C = list(map(lambda x: int(x)-1, input().split()))
q = deque(C)
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] < H[b]:
        edge[a].append(b)
    else:
        edge[b].append(a)
dist = [-1]*N
for c in C:
    dist[c] = 0
while q:
    v = q.popleft()
    for e in edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            q.append(e)
print(*dist, sep="\n")
