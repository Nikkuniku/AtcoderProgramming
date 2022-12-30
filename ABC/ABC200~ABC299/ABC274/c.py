import pypyjit
from sys import setrecursionlimit

setrecursionlimit(10000000)
pypyjit.set_param('max_unroll_recursion=-1')
n = int(input())
a = list(map(int, input().split()))
b = [(a[i], i+1) for i in range(n)]
b.sort(key=lambda x: x[0])
edge = [[] for _ in range(2*n + 2)]
for v, i in b:
    edge[v].append(2*i)
    edge[v].append(2*i+1)

    edge[2*i].append(v)
    edge[2*i+1].append(v)

ans = [0]*(2*n+2)


def dfs(v, p, depth):
    for e in edge[v]:
        if e == p:
            continue
        dfs(e, v, depth+1)

    ans[v] = depth


dfs(1, -1, 0)
print(*ans[1:], sep="\n")
