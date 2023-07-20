
from bisect import bisect_left
from collections import defaultdict


def mex(x, y, z):
    for i in range(4):
        if not (i == x or i == y or i == z):
            break
    return i


N = int(input())
A = list(map(int, input().split()))
S = list(input())
d = defaultdict(list)
for i in range(N):
    d[(S[i], A[i])].append(i)
for k in d.keys():
    d[k].sort()
ans = 0
for p in [0, 1, 2]:
    for j in d[('E', p)]:
        for q in [0, 1, 2]:
            for r in [0, 1, 2]:
                a = bisect_left(d[('M', q)], j)
                b = len(d[('X', r)])-bisect_left(d[('X', r)], j)
                ans += mex(p, q, r)*a*b
print(ans)
