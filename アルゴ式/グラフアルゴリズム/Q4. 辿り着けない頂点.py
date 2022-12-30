from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
ans = N
seen = [False]*N


def rec(v, p=-1):
    global ans
    seen[v] = True
    ans -= 1
    for e in Edge[v]:
        if e == p:
            continue
        if seen[e]:
            continue
        rec(e, v)


rec(0)
print(ans)
