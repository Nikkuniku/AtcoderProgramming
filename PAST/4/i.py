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


N = int(input())
A = list(map(int, input().split()))
S = sum(A)
B = A + A
ans = 1 << 60
Seg = SegTree(B, segfunc, 0)
for i in range(N):
    l = i
    r = N + i
    while r - l > 1:
        mid = (l + r) // 2
        tmp = Seg.query(i, mid)
        if 2 * tmp >= S:
            r = mid
        else:
            l = mid
    x_gt = Seg.query(i, r)
    ans = min(ans, abs(2 * x_gt - S))

    l = i
    r = N + i
    while r - l > 1:
        mid = (l + r) // 2
        tmp = Seg.query(i, mid)
        if 2 * tmp < S:
            l = mid
        else:
            r = mid
    x_lt = Seg.query(i, l)
    ans = min(ans, abs(2 * x_lt - S))
print(ans)
