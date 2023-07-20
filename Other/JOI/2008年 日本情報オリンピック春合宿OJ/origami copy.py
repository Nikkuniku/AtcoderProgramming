from sys import getsizeof
from collections import defaultdict
N = int(input())
d = defaultdict(int)
A, B = map(int, input().split())
for _ in range(N):
    p, q, r, s = map(int, input().split())
    for i in range(p, r+1):
        for j in range(q, s+1):
            d[i, j] += 1
M = max(d.values())
ans = list(d.values()).count(M)
print(M)
print(ans)

print(getsizeof(d))
