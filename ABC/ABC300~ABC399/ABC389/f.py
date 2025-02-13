from atcoder.lazysegtree import LazySegTree

INF = 1 << 63


def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = -INF
id_ = 0
M = 5 * 10**5 + 5
dp = LazySegTree(op, e, mapping, composition, id_, [j for j in range(M)])
N = int(input())
for _ in range(N):
    L, R = map(int, input().split())
    l = dp.max_right(0, lambda x: x < L)
    r = dp.max_right(0, lambda x: x <= R)
    dp.apply(l, r, 1)
Q = int(input())
ans = []
for _ in range(Q):
    X = int(input())
    ans.append(dp.get(X))
print(*ans, sep="\n")
