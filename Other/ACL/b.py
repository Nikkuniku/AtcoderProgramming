from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Seg = SegTree(lambda x, y: x + y, 0, A)
ans = []
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 0:
        v = Seg.get(a)
        Seg.set(a, v + b)
    else:
        v = Seg.prod(a, b)
        ans.append(v)
print(*ans, sep="\n")
