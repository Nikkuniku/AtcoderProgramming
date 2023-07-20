import pypyjit
from sys import setrecursionlimit
setrecursionlimit(10**9)
pypyjit.set_param('max_unroll_recursion=-1')
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
MOD = 10**9 + 7
dp = [[-1]*W for _ in range(H)]


def rec(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    res = 1
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for dx, dy in dxy:
        ni = i+dx
        nj = j+dy
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if A[i][j] < A[ni][nj]:
            res += rec(ni, nj)
            res %= MOD
    dp[i][j] = res
    return res


ans = 0
for i in range(H):
    for j in range(W):
        ans += rec(i, j)
        ans %= MOD
print(ans)
