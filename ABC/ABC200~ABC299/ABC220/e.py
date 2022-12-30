from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
ans = [0]*N
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

# sを根としたときの距離


def bfs(s):
    q = deque([s])
    dist = [-1]*N
    dist[s] = 0
    while q:
        v = q.popleft()
        for e in Edge[v]:
            if dist[e] == -1:
                dist[e] = dist[v]+1
                q.append(e)

    return dist
# それぞれの頂点を根としたときの部分木サイズを求める


dp = [1]*N


def dfs(v, p):
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v)
        dp[v] += dp[e]


dfs(0, -1)
s = 0
dist = bfs(s)
ans[s] = sum(dist)


q = deque([s])
seen = [False]*N
seen[s] = True
while q:
    v = q.popleft()

    for e in Edge[v]:
        if seen[e]:
            continue
        from_size = N-dp[e]
        to_size = dp[e]
        ans[e] = ans[v]+(from_size-to_size)
        seen[e] = True
        q.append(e)
print(*ans, sep="\n")
