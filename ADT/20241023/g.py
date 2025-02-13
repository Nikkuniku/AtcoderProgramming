from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left

N = int(input())
product = defaultdict(list)
S = set()
for _ in range(N):
    t, d = map(int, input().split())
    product[t].append((t, t + d))
    S.add(t)
S = sorted(S)
t = 0
ans = 0
q = []
while 1:
    if not q:
        idx = bisect_left(S, t)
        if idx == len(S):
            break
        t = S[idx]
    for a, b in product[t]:
        q.append((b, a))
    if not q:
        break
    while q:
        y, x = heappop(q)
        if x <= t <= y:
            ans += 1
            t += 1
            break
print(ans)
