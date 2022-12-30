from sys import setrecursionlimit
setrecursionlimit(10**8)
N = int(input())
P = [0]+list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(1, N):
    Edge[i].append(P[i])
    Edge[P[i]].append(i)
for i in range(N):
    Edge[i] = sorted(Edge[i])
ans = []


def dfs(v, p=-1):
    ans.append(v)
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v)


dfs(0, 0)
print(*ans)
