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
S = input()
C = list(map(int, input().split()))

p1 = [0] * N
p2 = [0] * N
for i, v in enumerate(S):
    if i % 2 == 0:
        if v == "0":
            p2[i] = C[i]
        elif v == "1":
            p1[i] = C[i]
    else:
        if v == "0":
            p1[i] = C[i]
        elif v == "1":
            p2[i] = C[i]


Seg_p1 = SegTree(p1, segfunc, 0)
Seg_p2 = SegTree(p2, segfunc, 0)
ans = 1 << 60
for i in range(N - 1):
    tmp1 = Seg_p2.query(0, i + 1) + Seg_p1.query(i + 1, N)
    tmp2 = Seg_p1.query(0, i + 1) + Seg_p2.query(i + 1, N)
    ans = min(ans, tmp1, tmp2)
print(ans)
