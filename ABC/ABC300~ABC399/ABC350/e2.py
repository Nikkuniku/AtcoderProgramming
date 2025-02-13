from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10**8)
N, A, X, Y = map(int, input().split())
INF = 1 << 60


@lru_cache(maxsize=None)
def rec(v):
    if v == 0:
        return 0
    res = INF
    res = min(res, rec(v // A) + X)
    tmp = 6 * Y / 5
    for b in range(2, 7):
        tmp += rec(v // b) / 5
    res = min(res, tmp)
    return res


print(rec(N))
