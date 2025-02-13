N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(int)
ans = 0
r = 0
tmp = 0
for l in range(N):
    while r < N and d[A[r]] + 1 < 2:
        tmp += 1
        d[A[r]] += 1
        r += 1
    ans = max(ans, tmp)
    if r == l:
        r += 1
    tmp -= 1
    d[A[l]] -= 1
print(ans)
