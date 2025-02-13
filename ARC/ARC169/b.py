from itertools import accumulate
from bisect import bisect_left, bisect_right

N, S = map(int, input().split())
A = list(map(int, input().split()))
cum = list(accumulate(A, initial=0))
val = [0]
for j in range(1, N + 1):
    tmp = 0
    sj = cum[j]
    i = bisect_left(cum, sj - S)
    tmp = val[i] + j
    val.append(tmp)
print(sum(val))
