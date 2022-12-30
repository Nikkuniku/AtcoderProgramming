from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
n = int(input())


@lru_cache(maxsize=None)
def s(n):
    if n == 1:
        return [1]

    t = s(n-1)+[n]+s(n-1)
    return t


ans = []
tmp = s(n)
print(*tmp)
