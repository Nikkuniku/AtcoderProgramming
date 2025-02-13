from sys import setrecursionlimit

setrecursionlimit(10**7)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)

ans = 0
seen = [False] * N
finished = [False] * N


def dfs(v, p=-1):
    global ans
    seen[v] = True
    ans += 1
    if ans > 10**6:
        return
    for e in Edge[v]:
        if e == p:
            continue
        if seen[e]:
            continue
        dfs(e, v)
    seen[v] = False


dfs(0)
print(min(ans, 10**6))
