from itertools import combinations
from bisect import bisect_right


def solve(X, A):
    res = -1
    idx = bisect_right(A, X)
    if idx != 0:
        res = A[idx-1]
    return res


C = list(combinations([i for i in range(60)], 3))
Can = []
for c in C:
    p1, p2, p3 = c
    tmp = (1 << p1)+(1 << p2)+(1 << p3)
    Can.append(tmp)
Can.sort()
T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    ans.append(solve(N, Can))
print(*ans, sep="\n")
