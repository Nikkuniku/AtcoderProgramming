from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
MOD = 1000_000_007
dp = [[0] * 2 for _ in range(N)]
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)


def dfs(v, p=-1):
    isleaf = True
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v)
        isleaf = False
    if isleaf:
        dp[v] = [1, 1]
    else:
        t1 = 1
        t2 = 1
        for e in Edge[v]:
            if e == p:
                continue
            t1 *= sum(dp[e])
            t2 *= dp[e][0]
            t1 %= MOD
            t2 %= MOD
        dp[v][0] = t1
        dp[v][1] = t2


dfs(0)
ans = sum(dp[0]) % MOD
print(ans)
