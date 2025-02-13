from math import gcd

N, M, K = map(int, input().split())
G = N * M // gcd(N, M)


def solve(k):
    a = k // N
    b = k // M
    c = k // G
    return a + b - (2 * c)


l = 0
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cnt = solve(mid)
    if cnt >= K:
        r = mid
    else:
        l = mid
print(r)
