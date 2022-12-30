from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
P = [0]+list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(1, N):
    Edge[i].append(P[i])
    Edge[P[i]].append(i)
ans = [0]*N


def rec(v, p=-1):
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, v)

    ans[v] = 1
    for e in Edge[v]:
        if e == p:
            continue
        ans[v] += ans[e]


rec(0)
ans = [ans[i]-1 for i in range(N)]
print(*ans, sep="\n")
