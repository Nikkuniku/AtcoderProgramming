import sys
sys.setrecursionlimit(1000000)
MOD = 1000000007
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    edge[y].append(x)

dp = [[0, 0] for _ in range(n)]


def prod(a):
    ans = 1
    for c in a:
        ans *= c
    return ans


def rec(v, p=-1):
    check_leaf = len(edge[v])
    for e in edge[v]:
        if e == p:
            check_leaf -= 1

    if check_leaf > 0:
        for to in edge[v]:
            if to == p:
                continue
            rec(to, v)

        tmp_bw = []
        tmp_b = []
        for to in edge[v]:
            if to == p:
                continue
            tmp_bw.append(dp[to][0]+dp[to][1])
            tmp_b.append(dp[to][0])
        dp[v][0] += prod(tmp_bw)
        dp[v][1] += prod(tmp_b)
        dp[v][0] %= MOD
        dp[v][1] %= MOD
    else:
        dp[v][0] = 1
        dp[v][1] = 1


rec(0)
ans = (dp[0][0]+dp[0][1]) % MOD
print(ans)
