import resource
from sys import setrecursionlimit
setrecursionlimit(10**8)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
N, S, K = map(int, input().split())
Edge = [[] for _ in range(N)]
InputEdges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
    InputEdges.append((a, b))
color = [-1]*N
dist = [0]*N


def rec(v, c=1, d=0, p=-1):
    color[v] = c
    dist[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        if color[e] != -1:
            continue
        rec(e, 1-c, d+1, v)


rec(S)
ans = 0
for i in range(N):
    if dist[i] <= K:
        if K % 2 == 0:
            ans += color[i] == color[S]
        else:
            ans += color[i] != color[S]
print(ans)
