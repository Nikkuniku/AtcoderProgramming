from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
dp = [0] * (N + 1)


def rec(m):
    if m == 1:
        return 0
    tmp = set()
    xor = rec(m // 2) ^ rec((m + 1) // 2)
    tmp.add(xor)
    if m >= 3:
        xor = rec(m // 3) ^ rec((m + 1) // 3) ^ rec((m + 2) // 3)
        tmp.add(xor)
    mex = 0
    while 1:
        if mex not in tmp:
            break
        mex += 1
    dp[m] = mex
    return mex


ans = "A" if rec(N) else "B"
print(ans)
