N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


def f(A, x, k):
    from bisect import bisect_right, bisect_left

    cnt = 0
    for i, v in enumerate(A):
        if i == 0:
            continue
        if v == 0:
            if x >= 0:
                cnt += i
        elif v > 0:
            p = x // v
            j = bisect_right(A, p)
            cnt += min(i, j)
        elif v < 0:
            p = -(-x // v)
            j = bisect_left(A, p)
            cnt += max(i - j, 0)
    return cnt >= k


l = -(1 << 60)
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    if f(A, mid, K):
        r = mid
    else:
        l = mid
print(r)
