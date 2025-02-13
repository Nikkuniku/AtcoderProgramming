from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
dp = [[-1] * 1400 for _ in range(110)]


def rec(w, b):
    if dp[w][b] != -1:
        return dp[w][b]
    if w <= 0 and b <= 1:
        return 0
    s = set()
    if w >= 1:
        s.add(rec(w - 1, b + w))
    if b >= 2:
        for k in range(1, (b // 2) + 1):
            s.add(rec(w, b - k))
    mex = 0
    while mex in s:
        mex += 1
    dp[w][b] = mex
    return mex


W = list(map(int, input().split()))
B = list(map(int, input().split()))
xor = 0
for i in range(N):
    xor ^= rec(W[i], B[i])
ans = "First" if xor else "Second"
print(ans)
