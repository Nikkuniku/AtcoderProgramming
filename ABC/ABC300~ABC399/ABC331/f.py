N, Q = map(int, input().split())
S = input()
B = 109
MOD = 998244353


def segfunc(x, y):
    return (x + y) % MOD


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


Init = []
Init_Rev = []
H = []
for i in range(N):
    H.append(pow(B, i, MOD))
for i in range(N):
    tmp1 = ord(S[i]) * H[N - 1 - i] % MOD
    tmp2 = ord(S[N - 1 - i]) * H[N - 1 - i] % MOD
    Init.append(tmp1)
    Init_Rev.append(tmp2)

Seg = SegTree(Init, segfunc, 0)
Seg_Rev = SegTree(Init_Rev, segfunc, 0)
ans = []
for _ in range(Q):
    t, *query = input().split()
    if t == "1":
        x = int(query[0]) - 1
        c = query[1]
        Seg.update(x, ord(c) * H[N - 1 - x] % MOD)
        Seg_Rev.update(N - 1 - x, ord(c) * H[x] % MOD)
    elif t == "2":
        L, R = query
        L = int(L)
        R = int(R)
        p = Seg.query(L - 1, R)
        p *= pow(B, -(N - R), MOD)
        p %= MOD
        l, r = N + 1 - R, N + 1 - L
        z = Seg_Rev.query(l - 1, r)
        z *= pow(B, -(N - r), MOD)
        z %= MOD
        res = "No"
        if p == z:
            res = "Yes"
        ans.append(res)
print(*ans, sep="\n")
