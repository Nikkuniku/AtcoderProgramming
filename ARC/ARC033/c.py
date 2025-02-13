def segfunc(x, y):
    return x + y


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


Q = int(input())
L = 200005
Seg = SegTree([0] * L, segfunc, 0)


def binary(X):
    l = 0
    r = L
    while r - l > 1:
        mid = (l + r) // 2
        cnt = Seg.query(0, mid)
        if cnt >= X:
            r = mid
        else:
            l = mid
    return r


ans = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        Seg.update(x, 1)
    elif t == 2:
        v = binary(x) - 1
        print(v)
        Seg.update(v, 0)
