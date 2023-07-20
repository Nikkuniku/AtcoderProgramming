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
color = [False]*N


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
ans = 0
for v, _ in vertexes:
    if color[v]:
        continue
    for e in Edge[v]:
        if not color[e]:
            color[e] = True
            color[v] = True
            ans += 1
            break
print(ans)
