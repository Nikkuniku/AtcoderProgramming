from bisect import bisect_right


def f(A, B, x, k):
    cnt = 0
    for a in A:
        idx = bisect_right(B, x // a)
        cnt += idx
    return cnt >= k


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
l = 1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    if f(A, B, mid, K):
        r = mid
    else:
        l = mid
print(r)
