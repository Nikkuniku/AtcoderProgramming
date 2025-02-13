from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
dp = [1] * N
ans = 0


def dfs(v, p=-1):
    global ans
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v)
    for e in Edge[v]:
        if e == p:
            continue
        dp[v] += dp[e]
    if v != 0:
        ans += dp[v] * (N - dp[v])


dfs(0)
print(ans)
