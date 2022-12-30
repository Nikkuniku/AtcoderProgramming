from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
for i in range(N):
    Edge[i] = sorted(Edge[i])
dist = [-1]*N
seen = [False]*N


def rec(v, d=0, p=-1):
    seen[v] = True
    dist[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        if seen[e]:
            continue
        rec(e, d+1, v)


rec(0)
ans = 'Yes'
if -1 in dist:
    ans = 'No'
print(ans)
