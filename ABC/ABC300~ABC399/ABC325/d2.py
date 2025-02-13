from heapq import heapify, heappop, heappush
from bisect import bisect_left
from collections import defaultdict

N = int(input())
t = 0
T = set()
D = []
kukan = defaultdict(list)
for _ in range(N):
    ti, di = map(int, input().split())
    T.add(ti)
    D.append((ti + di, ti))
    kukan[ti].append((ti, ti + di))
heapify(D)
T = sorted(T)
ans = 0
q = []
while 1:
    for a, b in kukan[t]:
        heappush(q, (b, a))
    while q:
        b, a = heappop(q)
        if a <= t <= b:
            t += 1
            ans += 1
            break
    else:
        idx = bisect_left(T, t)
        if idx == len(T):
            break
        t = T[idx]
print(ans)
