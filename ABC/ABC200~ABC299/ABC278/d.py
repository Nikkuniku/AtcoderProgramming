from bisect import bisect_left, bisect_right
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d1 = defaultdict(int)
d2 = defaultdict(int)
init = [0]
adds = [[0] for _ in range(N+1)]
ans = []
for i in range(Q):
    i += 1
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 1:
        init.append(i)
        d1[i] = query[1]
    elif query_type == 2:
        d2[(i, query[1])] += d2[(adds[query[1]][-1], query[1])]+query[2]
        adds[query[1]].append(i)
    else:
        p = query[1]
        c = init[-1]
        if init[-1] == 0:
            base = A[p-1]
        else:
            base = d1[init[-1]]
        if c < adds[p][-1]:
            b = bisect_right(init, adds[p][-1])-1
            inittime = init[b]
            idx = bisect_right(adds[p], inittime)
            ad = d2[(adds[p][-1], p)]-d2[(adds[p][idx-1], p)]
        else:
            ad = 0
        ans.append(base+ad)

print(*ans, sep="\n")
