from sys import setrecursionlimit
setrecursionlimit(10**9)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
visited = [False]*N
limit = 10**6
ans = 0


def dfs(v):
    global ans
    if ans == limit:
        print(ans)
        exit()
    visited[v] = True
    ans += 1
    for e in Edge[v]:
        if not visited[e]:
            dfs(e)
    visited[v] = False


dfs(0)
print(ans)
