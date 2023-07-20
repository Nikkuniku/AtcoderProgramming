import resource
from sys import setrecursionlimit
setrecursionlimit(10**8)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
dp = [[0, 0] for _ in range(N)]
MOD = 998244353


def rec(v, p=-1):
    leaf = True
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, v)
        leaf = False
    if leaf:
        dp[v] = [1, 1]
    else:
        choice = 1
        notchoice = 1
        for e in Edge[v]:
            if e == p:
                continue
            choice *= dp[e][1]
            notchoice *= sum(dp[e])
            choice %= MOD
            notchoice %= MOD
        dp[v][0] = choice
        dp[v][1] = notchoice


rec(0)
ans = sum(dp[0]) % MOD
print(ans)
