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


N, Q = map(int, input().split())
S = list(input())
A = []
for i in range(1, N):
    if S[i - 1] != S[i]:
        A.append(1)
    else:
        A.append(0)
Seg = SegTree(A, segfunc, 0)
ans = []
for _ in range(Q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if t == 1:
        if 1 <= l:
            p = Seg.query(l - 1, l)
            Seg.update(l - 1, p ^ 1)
        if r < N - 1:
            q = Seg.query(r, r + 1)
            Seg.update(r, q ^ 1)
    else:
        tmp = Seg.query(l, r)
        if tmp == r - l:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans, sep="\n")
