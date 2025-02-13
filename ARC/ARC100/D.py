from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
revA = A[::-1]
cum = list(accumulate(A))
cum_rev = list(accumulate(A[::-1]))
ans = 1 << 60
for k in range(1, N - 2):
    l = 0
    r = k
    while r - l > 1:
        mid = (l + r) // 2
        if cum[mid] <= cum[k] - cum[mid]:
            l = mid
        else:
            r = mid
    P = cum[l]
    Q = cum[k] - cum[l]
    if l + 1 < k:
        if abs(P - Q + 2 * A[l + 1]) <= abs(P - Q):
            P += A[l + 1]
            Q -= A[l + 1]
    l = 0
    r = N - 2 - k
    while r - l > 1:
        mid = (l + r) // 2
        if cum_rev[mid] <= cum_rev[N - 2 - k] - cum_rev[mid]:
            l = mid
        else:
            r = mid
    R = cum_rev[l]
    S = cum_rev[N - 2 - k] - cum_rev[l]
    if l + 1 < N - 2 - k:
        if abs(R - S + 2 * revA[l + 1]) <= abs(R - S):
            R += revA[l + 1]
            S -= revA[l + 1]
    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
print(ans)
