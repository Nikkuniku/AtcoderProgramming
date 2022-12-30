from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
P = [0]+list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(1, N):
    Edge[i].append(P[i])
    Edge[P[i]].append(i)
ans = [0]*N


def rec(v, d=0, p=-1):
    ans[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, d+1, v)


rec(0)
print(max(ans))
