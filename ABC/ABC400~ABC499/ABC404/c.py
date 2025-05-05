from sys import setrecursionlimit

setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
if N != M:
    exit(print("No"))
seen = [False] * N
dist = [-1] * N


def dfs(v, d=0, p=-1):
    seen[v] = True
    dist[v] = d
    for to in Edge[v]:
        if to == p:
            continue
        if seen[to]:
            continue
        dfs(to, d + 1, v)


dfs(0)
p = max(dist)
w = dist.index(p)
if not (p == N - 1 and 0 in set(Edge[w])):
    exit(print("No"))
print("Yes")
