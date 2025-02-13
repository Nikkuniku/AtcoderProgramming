from itertools import accumulate
from sortedcontainers import SortedList

N = int(input())
X = SortedList(list(map(int, input().split())))
P = list(map(int, input().split()))
cum = list(accumulate(P, initial=0))
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    j = X.bisect_right(r)
    i = X.bisect_right(l - 1)
    tmp = cum[j] - cum[i]
    ans.append(tmp)
print(*ans, sep="\n")
