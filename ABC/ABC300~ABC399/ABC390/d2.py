from sys import setrecursionlimit
setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))

B = [0] * (N + 1)
ans = set()


def dfs(d, sz):
    if d == N:
        res = 0
        for b in B:
            res ^= b
        ans.add(res)
        return
    for k in range(1, sz + 1 + 1):
        B[k] += A[d]
        dfs(d + 1, max(k, sz))
        B[k] -= A[d]
    return


dfs(0, 0)
print(len(ans))
