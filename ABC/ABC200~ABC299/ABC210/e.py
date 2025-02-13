from itertools import accumulate
from collections import defaultdict
from math import gcd

N, M = map(int, input().split())
INF = 1 << 60
d = defaultdict(lambda: INF)
for _ in range(M):
    a, c = map(int, input().split())
    d[gcd(a, N)] = min(d[gcd(a, N)], c)
keys = list(d.keys())
compress = defaultdict(int)
for i, v in enumerate(keys):
    compress[v] = i
cost = [d[v] for v in keys]
cummin_left = list(accumulate(cost, min, initial=INF))
cummin_right = list(accumulate(cost[::-1], min, initial=INF))[::-1]
ans = INF
for g in keys:
    idx = compress[g]
    mincost = min(cummin_left[idx], cummin_right[idx + 1])
    tmp = (N - g) * d[g] + (g - 1) * mincost
    ans = min(ans, tmp)
if ans == INF:
    ans = -1
print(ans)
