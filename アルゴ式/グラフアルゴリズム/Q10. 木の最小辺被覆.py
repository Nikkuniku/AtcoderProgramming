import resource
from sys import setrecursionlimit
setrecursionlimit(10**8)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
depth = [0]*N
cover = [False]*N


def rec(v, d=0, p=-1):
    depth[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, d+1, v)


rec(0)

vertexes = sorted([(i, v) for i, v in enumerate(depth)],
                  key=lambda x: x[1], reverse=True)
ans = 0
for v, _ in vertexes:
    if cover[v]:
        continue
    for e in Edge[v]:
        if depth[e] > depth[v]:
            continue
        ans += 1
        cover[v] = True
        cover[e] = True
if not cover[0]:
    ans += 1
print(ans)
