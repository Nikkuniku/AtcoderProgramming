from atcoder.segtree import SegTree
from collections import defaultdict

N, W = map(int, input().split())
Block = [[] for _ in range(W)]
INF = 1 << 60
V = [INF] * W
for i in range(N):
    x, y = map(int, input().split())
    x -= 1
    Block[x].append((y, i + 1))
    V[x] = min(V[x], y)
ExistNoBlock = False
for i in range(W):
    if V[i] == INF:
        V[i] = -1
        ExistNoBlock = True
    Block[i].sort(reverse=True)
Seg = SegTree(max, -1, V)
Time = defaultdict(lambda: INF)
keika = 0
while not ExistNoBlock:
    t = Seg.all_prod()
    keika += t
    for c in range(W):
        y, i = Block[c].pop()
        Time[i] = keika
        if Block[c]:
            y, _ = Block[c][-1]
            Seg.set(c, max(y - keika, 1))
        else:
            ExistNoBlock = True
Q = int(input())
ans = []
for _ in range(Q):
    t, a = map(int, input().split())
    if Time[a] <= t:
        print("No")
    else:
        print("Yes")
