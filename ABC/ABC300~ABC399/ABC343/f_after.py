def segfunc(x, y):
    f1 = x[0]
    s1 = x[2]
    f2 = y[0]
    s2 = y[2]
    f_cnt, s_cnt = 0, 0
    f, s = 0, 0
    if f1 > f2:
        f = f1
        f_cnt = x[1]
        if f2 < s1:
            s = s1
            s_cnt = x[3]
        elif f2 > s1:
            s = f2
            s_cnt = y[1]
        elif f2 == s1:
            s = f2
            s_cnt = x[3] + y[1]
    elif f1 < f2:
        f = f2
        f_cnt = y[1]
        if f1 < s2:
            s = s2
            s_cnt = y[3]
        elif f1 > s2:
            s = f1
            s_cnt = x[1]
        elif s2 == f1:
            s = f1
            s_cnt = x[1] + y[3]
    elif f1 == f2:
        f = f1
        f_cnt = x[1] + y[1]
        if s1 > s2:
            s = s1
            s_cnt = x[3]
        elif s1 < s2:
            s = s2
            s_cnt = y[3]
        else:
            s = s1
            s_cnt = x[3] + y[3]
    return [f, f_cnt, s, s_cnt]


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [[ide_ele, 0, ide_ele - 1, 0]] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = [init_val[i], 1, ide_ele - 1, 0]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = [x, 1, self.ide_ele - 1, 0]
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = [self.ide_ele, 0, self.ide_ele - 1, 0]
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
A = list(map(int, input().split()))
Seg = SegTree(A, segfunc, -1)
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1:]
        p -= 1
        Seg.update(p, x)
    else:
        l, r = query[1:]
        l -= 1
        M = Seg.query(l, r)
        ans.append(M[3])
print(*ans, sep="\n")
