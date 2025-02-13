from bisect import bisect_left, bisect_right
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(A)
B = [maxA - A[i] for i in range(N)]
d = defaultdict(int)
for i in range(N):
    d[i] = B[i]
B.sort()
ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    p = bisect_left(B, d[y])
    q = bisect_right(B, d[x])
    ans.append(max(p - q, 0))
print(*ans, sep="\n")
