from bisect import bisect_left
from itertools import accumulate

N, D = map(int, input().split())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
acx = list(accumulate(X, initial=0))
acy = list(accumulate(Y, initial=0))
Disty = [0] * (D + 1)
L = 10**6
for y in range(-L - D, L + D + 1):
    idx = bisect_left(Y, y)
    tmp = y * idx - acy[idx] + (acy[-1] - acy[idx]) - y * (N - idx)
    if tmp > D:
        continue
    Disty[tmp] += 1
cum_Disty = list(accumulate(Disty))
ans = 0
for x in range(-L - D, L + D + 1):
    idx = bisect_left(X, x)
    p = x * idx - acx[idx] + (acx[-1] - acx[idx]) - x * (N - idx)
    if D - p < 0:
        continue
    ans += cum_Disty[D - p]
print(ans)
