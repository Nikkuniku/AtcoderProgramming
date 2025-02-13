from bisect import bisect_right
from itertools import accumulate

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
cumB = list(accumulate(B, initial=0))
ans = 0
for a in A:
    idx = bisect_right(B, P - a)
    ans += cumB[idx] + idx * a + P * (M - idx)
print(ans)
