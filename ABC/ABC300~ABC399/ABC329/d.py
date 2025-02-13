from heapq import heappush, heappop
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []
maxv = 0

d = defaultdict(int)
hyou = [[] for _ in range(M + 1)]
for a in A:
    d[a] += 1
    maxv = max(maxv, d[a])
    if d[a] == maxv:
        heappush(hyou[maxv], a)
    v = heappop(hyou[maxv])
    ans.append(v)
    heappush(hyou[maxv], v)
print(*ans, sep="\n")
