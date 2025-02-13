from sys import setrecursionlimit

setrecursionlimit(10**8)
N, K = map(int, input().split())
S = set()
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
V = set()
W = list(map(int, input().split()))
for w in W:
    V.add(w - 1)


def dfs(v, p=-1):
    res = False
    for e in Edge[v]:
        if e == p:
            continue
        res |= dfs(e, v)
    if v in V:
        res |= True
    if res:
        S.add(v)
    return res


dfs(min(V))
print(len(S))
