from bisect import bisect_left
from heapq import heappop, heapify, heappush
from collections import defaultdict

N = int(input())
T = set()
M = []
M = defaultdict(list)
for _ in range(N):
    t, d = map(int, input().split())
    M[t].append(t + d)
    T.add(t)
ans = 0
T = sorted(T)
t = 1
q = []
while 1:
    for r in M[t]:
        heappush(q, (r, t))
    while q:
        r, l = heappop(q)
        if l <= t <= r:
            ans += 1
            t += 1
            break
    else:
        idx = bisect_left(T, t)
        if idx == len(T):
            break
        t = T[idx]
print(ans)
