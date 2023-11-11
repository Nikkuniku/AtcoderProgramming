N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(int)
d[0] = 1
s = 0
ans = 0
for i in range(N):
    if i % 2 == 0:
        s += A[i]
    else:
        s -= A[i]
    ans += d[s]
    d[s] += 1
print(ans)
