from bisect import bisect_left
from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
dp = [1 << 60] * (N + 1)
dp[0] = 0
ans = [-1] * N


def dfs(v, cummax, p=-1):
    idx = bisect_left(dp, A[v])
    prev = dp[idx]
    dp[idx] = A[v]
    ans[v] = max(idx, cummax)
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, cummax + (prev == 1 << 60), v)
    dp[idx] = prev


dfs(0, 0)
print(*ans, sep="\n")
