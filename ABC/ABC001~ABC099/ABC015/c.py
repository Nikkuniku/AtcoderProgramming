from sys import setrecursionlimit

setrecursionlimit(10**8)
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def dfs(s, i):
    if i == N:
        if s == 0:
            exit(print("Found"))
        return
    for j in range(K):
        dfs(s ^ T[i][j], i + 1)


dfs(0, 0)
print("Nothing")
