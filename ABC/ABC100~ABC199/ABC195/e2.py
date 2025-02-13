import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")

from sys import setrecursionlimit
from functools import cache

setrecursionlimit(10**8)
N = int(input())
S = input()
X = input()
pows = [pow(10, j, 7) for j in range(N)]


@cache
def dfs(i, mo):
    if i == N:
        return mo == 0
    t = X[i]
    s = int(S[i])
    if t == "T":
        res = dfs(i + 1, mo) | dfs(i + 1, (mo + pows[N - 1 - i] * s) % 7)
    else:
        res = dfs(i + 1, mo) & dfs(i + 1, (mo + pows[N - 1 - i] * s) % 7)
    return res


ans = "Takahashi" if dfs(0, 0) else "Aoki"
print(ans)
