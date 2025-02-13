from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
dp = [1] * N


def dfs(v, p=-1):
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v)
    for e in Edge[v]:
        if e == p:
            continue
        dp[v] += dp[e]


dfs(0)
res = []
for e in Edge[0]:
    res.append(dp[e])
ans = 1
if len(res) > 1:
    ans = sum(res) - max(res) + 1
print(ans)
