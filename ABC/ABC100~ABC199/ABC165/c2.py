from sys import setrecursionlimit

setrecursionlimit(10**8)
N, M, Q = map(int, input().split())
ans = 0
P = [list(map(int, input().split())) for _ in range(Q)]


def dfs(v):
    global ans
    if len(v) == N:
        tmp = 0
        for a, b, c, d in P:
            a -= 1
            b -= 1
            if v[b] - v[a] == c:
                tmp += d
        ans = max(ans, tmp)
        return
    if v:
        for w in range(v[-1], M + 1):
            dfs(v + [w])
    else:
        for w in range(1, M + 1):
            dfs(v + [w])


dfs([])
print(ans)
