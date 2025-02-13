from itertools import accumulate
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = sorted(A[:])
CUM = list(accumulate(B, initial=0))
ans = []
for a in A:
    idx = bisect_right(B, a)
    ans.append(CUM[-1] - CUM[idx])
print(*ans)
