from sys import setrecursionlimit
setrecursionlimit(10**8)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
depth = [0]*N
color = [0]*N


def rec(v, d=0, p=-1):
    depth[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, d+1, v)


rec(0)
vertexes = []
for i, v in enumerate(depth):
    vertexes.append((i, v))
vertexes.sort(key=lambda x: x[1], reverse=True)
for v, _ in vertexes:
    flg = True
    for e in Edge[v]:
        if color[e]:
            flg = False
    if flg:
        color[v] = 1
ans = sum(color)
print(ans)
