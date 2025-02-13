from atcoder.lazysegtree import LazySegTree


def op(ele1, ele2):
    return ele1 + ele2


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = 0
id_ = 0
N = int(input())
S = input()
lst = [0] * (N + 1)
# TODO (初期リストlst)
seg = LazySegTree(op, e, mapping, composition, id_, lst)
for i in range(N):
    s = int(S[i])
    if i == 0:
        seg.apply(0, N, s)
    elif i < N - 1:
        seg.apply(i, N, 2 * s)
    else:
        seg.apply(N - 1, N, (i + 1) * s)
ans = 0
for i in range(N - 1, -1, -1):
    p = seg.prod(i, i + 1)
    print(p)
