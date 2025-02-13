from collections import defaultdict
from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list)
s = 0
B = [0] + A + [A[i] for i in range(N - 2)]
ans = 0
tmp = 0
for i in range(len(B)):
    s += B[i]
    s %= M
    idx = bisect_right(d[s], i - N)
    ans += len(d[s]) - idx
    if i <= N - 2:
        tmp += len(d[s]) - idx
    d[s].append(i)
print(ans - tmp)
