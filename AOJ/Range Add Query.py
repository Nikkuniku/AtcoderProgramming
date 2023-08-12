def segfunc(x, y):
    return x+y


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

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
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


N, Q = map(int, input().split())
Seg = SegTree([0]*(N+2), segfunc, 0)
ans = []
for _ in range(Q):
    t, *query = list(map(int, input().split()))
    if t == 0:
        s, t, x = query
        p = Seg.query(s, s+1)
        r = Seg.query(t+1, t+1+1)
        Seg.update(s, p+x)
        Seg.update(t+1, r-x)
    elif t == 1:
        i = query[0]
        res = Seg.query(0, i+1)
        ans.append(res)
print(*ans, sep="\n")
