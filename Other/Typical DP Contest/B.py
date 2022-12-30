from functools import lru_cache
A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0]*(B+1) for _ in range(A+1)]
S = sum(a)+sum(b)


@lru_cache
def rec(x, y):
    if x == 0 and y == 0:
        return 0
    if ((A+B)-(x+y)) % 2 != 0:
        if x == 0:
            res = rec(x, y-1)
        elif y == 0:
            res = rec(x-1, y)
        else:
            res = min(rec(x-1, y), rec(x, y-1))
    else:
        if x == 0:
            res = rec(x, y-1)+b[y-1]
        elif y == 0:
            res = rec(x-1, y)+a[x-1]
        else:
            res = max(rec(x-1, y)+a[x-1], rec(x, y-1)+b[y-1])
    dp[x][y] = res
    return res


ans = rec(A, B)
print(ans)
print(S)
