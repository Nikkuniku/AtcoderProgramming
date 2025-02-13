from itertools import accumulate
from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cum = list(accumulate(A, initial=0))
ans = []
for _ in range(Q):
    x = int(input())
    res = 0
    p = bisect_left(A, x)
    res = x * p - cum[p]
    q = bisect_right(A, x)
    res += (cum[-1] - cum[q]) - x * (N - q)
    ans.append(res)
print(*ans, sep="\n")
