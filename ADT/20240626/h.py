from atcoder.segtree import SegTree

N, D = map(int, input().split())
A = list(map(int, input().split()))
L = 5 * 10**5
S = SegTree(max, 0, [0 for _ in range(L + 1)])
for a in A:
    l = max(0, a - D)
    r = min(L, a + D)
    p = S.prod(l, r + 1)
    S.set(a, p + 1)
print(S.all_prod())
