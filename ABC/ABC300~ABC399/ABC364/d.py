from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


def solve(b, k):
    l = -1
    r = 1 << 30
    while r - l > 1:
        mid = (l + r) // 2
        idx = bisect_right(A, b + mid)
        idy = bisect_left(A, b - mid)
        if idx - idy >= k:
            r = mid
        else:
            l = mid
    return r


ans = []
for _ in range(Q):
    B, K = map(int, input().split())
    ans.append(solve(B, K))
print(*ans, sep="\n")
