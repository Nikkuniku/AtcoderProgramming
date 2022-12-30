from bisect import bisect_left
from itertools import accumulate
N, T = map(int, input().split())
A = list(map(int, input().split()))
suma = sum(A)
T %= suma
csum = list(accumulate([0]+A))
idx = bisect_left(csum, T)
print(idx, T-csum[idx-1])
