# N: 処理する区間の長さ
N = int(input())

INF = -1

LV = (N - 1).bit_length()
N0 = 2**LV
data = [0] * (2 * N0)
lazy = [0] * (2 * N0)


def gindex(l, r):
    L = (l + N0) >> 1
    R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1
        R >>= 1


# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i - 1]
        if not v:
            continue
        lazy[2 * i - 1] += v
        lazy[2 * i] += v
        data[2 * i - 1] += v
        data[2 * i] += v
        lazy[i - 1] = 0


# 区間[l, r)にxを加算
def update(l, r, x):
    (*ids,) = gindex(l, r)
    propagates(*ids)

    L = N0 + l
    R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R - 1] += x
            data[R - 1] += x
        if L & 1:
            lazy[L - 1] += x
            data[L - 1] += x
            L += 1
        L >>= 1
        R >>= 1
    for i in ids:
        data[i - 1] = max(data[2 * i - 1], data[2 * i])


# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l
    R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R - 1])
        if L & 1:
            s = max(s, data[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s


AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()
ans = 0
for i, v in enumerate(AB):
    a, b = v
    update(0, i + 1, b)
    update(i, i + 1, a)
    p = query(0, i + 1)
    tmp = p - a
    ans = max(ans, tmp)
print(ans)
