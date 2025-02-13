from functools import lru_cache

N, A, X, Y = map(int, input().split())


@lru_cache(maxsize=None)
def f(k):
    if k == 0:
        return 0
    res = 6 * Y / 5
    for p in range(2, 7):
        res += f(k // p) / 5
    res = min(res, f(k // A) + X)

    return res


print(f(N))
