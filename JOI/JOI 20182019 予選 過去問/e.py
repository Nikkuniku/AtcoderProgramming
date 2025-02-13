from atcoder.lazysegtree import LazySegTree

INF = 1 << 63
ID = INF


def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper


N, M = map(int, input().split())
A = list(map(int, input().split()))
e = -INF
id_ = ID

# TODO (初期リストlst)
Seg_MinRange = LazySegTree(op, e, mapping, composition, id_, [-1] * (N + 2))
P = [list(map(int, input().split())) for _ in range(M)]
P.sort(reverse=True)
for l, r in P:
    Seg_MinRange.apply(l, r + 1, l)
dp = LazySegTree(op, e, mapping, composition, id_, [0] * (N + 2))
for i in range(1, N + 1):
    p = Seg_MinRange.get(i)
    if p != -1:
        v = dp.prod(0, p)
    else:
        v = dp.prod(0, i)
    dp.set(i, v + A[i - 1])
ans = dp.all_prod()
print(ans)
