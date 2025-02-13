from atcoder.lazysegtree import LazySegTree

INF = 1 << 63


def op(ele1, ele2):
    return min(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = INF
id_ = 0

Q = int(input())
seg = LazySegTree(op, e, mapping, composition, id_, [0] * (Q + 1))
C = 0
res = 0
ans_arr = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        C += 1
    elif query[0] == 2:
        T = query[1]
        seg.apply(0, C, T)
    elif query[0] == 3:
        H = query[1]
        l = 0
        r = Q + 1
        while r - l > 1:
            mid = (l + r) // 2
            tmp = seg.prod(0, mid)
            if tmp >= H:
                l = mid
            else:
                r = mid
        if l == 0:
            ans = 0
        else:
            p = seg.prod(l - 1, l)
            if p >= H:
                ans = l - res
                res += ans
        ans_arr.append(ans)
print(*ans_arr, sep="\n")
