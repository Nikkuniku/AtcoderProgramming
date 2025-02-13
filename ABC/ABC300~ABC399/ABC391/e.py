from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
S = input()
INF = 1 << 60
M = sum([pow(3, i) for i in range(N + 1)])
L = M - pow(3, N)
dp = [[INF] * 2 for _ in range(M)]


def dfs(v, d):
    if d == N:
        if S[v - L] == "0":
            dp[v][0] = 0
            dp[v][1] = 1
        else:
            dp[v][0] = 1
            dp[v][1] = 0
        return
    else:
        for i in range(3):
            dfs(3 * v + (i + 1), d + 1)
        zero = []
        one = []
        for i in range(3):
            zero.append(dp[3 * v + (i + 1)][0])
            one.append(dp[3 * v + (i + 1)][1])
        zero.sort()
        one.sort()
        dp[v][0] = sum(zero[:2])
        dp[v][1] = sum(one[:2])


dfs(0, 0)
print(dp)
