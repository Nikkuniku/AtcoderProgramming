from itertools import accumulate
from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
cum = list(accumulate(R, initial=0))
ans = []
for _ in range(Q):
    X = int(input())
    cnt = bisect_right(cum, X) - 1
    ans.append(cnt)
print(*ans, sep="\n")
