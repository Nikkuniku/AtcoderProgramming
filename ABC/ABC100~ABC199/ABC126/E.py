import pypyjit
from sys import setrecursionlimit
setrecursionlimit(10**8)
pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
edge = [[] for _ in range(N)]
inputedge = []
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edge[a].append(b)
    edge[b].append(a)
    inputedge.append((a, b))

Base = 0
depth = [0]*N


def dfs(v, p=-1, d=1):
    depth[v] = d
    for e in edge[v]:
        if e == p:
            continue
        dfs(e, v, d+1)


def dfs2(v, p, cost):
    for e in edge[v]:
        if e == p:
            continue
        ans[e] += cost
        dfs2(e, v, ans[e])


ans = [0]*N
dfs(0)
Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().split())
    a, b = inputedge[e-1]
    if t == 1:
        if depth[a] > depth[b]:
            ans[a] += x
        else:
            Base += x
            ans[b] -= x
    else:
        if depth[a] > depth[b]:
            Base += x
            ans[a] -= x
        else:
            ans[b] += x

dfs2(0, -1, ans[0])
for c in ans:
    print(c+Base)
