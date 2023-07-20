from sys import setrecursionlimit
setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
W = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]


def rec(v, p=-1):
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, v)

    for e in Edge[v]:
        if e == p:
            continue
        dp[v][0] += dp[e][1]
        dp[v][1] += max(dp[e])
    dp[v][0] += W[v]


rec(0)
ans = max(dp[0])
print(ans)
