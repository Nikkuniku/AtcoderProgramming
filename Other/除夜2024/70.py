from sys import setrecursionlimit

setrecursionlimit(10**8)
N, K = map(int, input().split())
R = list(map(int, input().split()))
ans = []


def dfs(A=[]):
    if len(A) == N:
        if sum(A) % K == 0:
            ans.append(A)
        return
    for r in range(1, R[len(A)] + 1):
        dfs(A + [r])
    return


dfs()
for c in ans:
    print(*c)
