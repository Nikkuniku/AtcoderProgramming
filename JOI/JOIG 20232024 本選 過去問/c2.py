from atcoder.segtree import SegTree
from collections import defaultdict
from sys import stdin

readline = stdin.readline
N = int(input())
V = []
P = set()
for j in range(N):
    c, x = map(int, readline().split())
    V.append((c, x, j))
    P.add(c)
compress = defaultdict(int)
for i, p in enumerate(sorted(P)):
    compress[p] = i
M = len(P)
SegMax = SegTree(max, -1, [-1] * M)
V.sort(key=lambda x: x[1])
ans = [1 << 60] * N
for c, x, j in V:
    i = compress[c]
    p = SegMax.prod(0, i)
    q = SegMax.prod(i + 1, M)
    t = max(p, q)
    if t != -1:
        if x - t < ans[j]:
            ans[j] = x - t
    SegMax.set(i, x)
INF = 1 << 60
SegMin = SegTree(min, INF, [INF] * M)
V = V[::-1]
for c, x, j in V:
    i = compress[c]
    p = SegMin.prod(0, i)
    q = SegMin.prod(i + 1, M)
    t = min(p, q)
    if t != INF:
        if t - x < ans[j]:
            ans[j] = t - x
    SegMin.set(i, x)
print(*ans, sep="\n")
