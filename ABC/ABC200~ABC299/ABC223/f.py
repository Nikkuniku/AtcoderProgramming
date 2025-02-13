# N: 処理する区間の長さ
from itertools import accumulate

N, Q = map(int, input().split())
N += 1

INF = 2**31 - 1

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
        data[i - 1] = min(data[2 * i - 1], data[2 * i])


# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l
    R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R - 1])
        if L & 1:
            s = min(s, data[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s


S = list(input())
A = []
for s in S:
    if s == "(":
        A.append(1)
    else:
        A.append(-1)
cum = list(accumulate(A, initial=0))
for i in range(len(cum)):
    update(i, i + 1, cum[i])
ans = []
for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        if S[l - 1] == S[r - 1]:
            continue
        else:
            if S[l - 1] == "(" and S[r - 1] == ")":
                update(l, N + 2, -2)
                update(r, N + 2, 2)
            elif S[l - 1] == ")" and S[r - 1] == "(":
                update(l, N + 2, 2)
                update(r, N + 2, -2)
            S[l - 1], S[r - 1] = S[r - 1], S[l - 1]
    elif t == 2:
        res = "No"
        a = query(l - 1, l)
        b = query(r, r + 1)
        m = query(l, r)
        if a == b and m >= a:
            res = "Yes"
        ans.append(res)
print(*ans, sep="\n")
