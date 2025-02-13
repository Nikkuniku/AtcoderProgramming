from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = SegTree(max, -1, A)
ans = []
for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        S.set(l - 1, r)
    elif t == 2:
        a = S.prod(l - 1, r)
        ans.append(a)
    elif t == 3:
        idx = S.max_right(l - 1, lambda p: p < r) + 1
        ans.append(idx)
print(*ans, sep="\n")
