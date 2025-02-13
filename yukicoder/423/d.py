N, H = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
from itertools import accumulate

cum = list(accumulate(B, initial=0))
ans = 0
tired = 0
day = 0
r = 0
tmp = 0
for l in range(N):
    while r < N and tired + (day + 1) * B[r] <= H:
        tmp += A[r]
        tired += (day + 1) * B[r]
        day += 1
        r += 1
    ans = max(ans, tmp)
    if l == r:
        r += 1
    else:
        tmp -= A[l]
        tired -= cum[r] - cum[l]
        day -= 1
print(ans)
