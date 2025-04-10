from atcoder.segtree import SegTree


def Calc(k):
    return k * (k + 1) // 2


N = int(input())
P = list(map(int, input().split()))
A = [0] * (N + 1)
Seg = SegTree(lambda x, y: x + y, 0, A)
ans = 0
for i, v in enumerate(P):
    cnt = Seg.prod(v + 1, N + 1)
    temp = Calc(i) - Calc(i - cnt)
    ans += temp
    Seg.set(v, 1)
print(ans)
