from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
for i in range(N):
    Edge[i] = sorted(Edge[i])
ans = []
color = [1]*N


def rec(v):
    color[v] = 0
    for e in Edge[v]:
        if color[e] == 0:
            continue
        rec(e)
    ans.append(v)


for v in range(N):
    if color[v] == 0:
        continue
    rec(v)
print(*ans[::-1])
