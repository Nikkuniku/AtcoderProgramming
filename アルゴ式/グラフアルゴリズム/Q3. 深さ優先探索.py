from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
for i in range(N):
    Edge[i] = sorted(Edge[i])
dist = [0]*N
ans = []
seen = [False]*N


def rec(v, p=-1):
    seen[v] = True
    ans.append(v)
    for e in Edge[v]:
        if e == p:
            continue
        if seen[e]:
            continue
        rec(e, v)


rec(0)

print(*ans)
