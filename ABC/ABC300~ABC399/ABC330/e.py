def segfunc(x, y):
    return min(x, y)


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


from collections import defaultdict

d = defaultdict(int)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
INF = 1 << 60
Seg = SegTree([i for i in range(N + 5)], segfunc, INF)
for a in A:
    if a <= N + 4:
        Seg.update(a, INF)
    d[a] += 1
ans = []
for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1
    d[A[i]] -= 1
    if d[A[i]] == 0 and A[i] <= N + 4:
        Seg.update(A[i], A[i])
    A[i] = x
    d[x] += 1
    if x <= N + 4:
        Seg.update(x, INF)
    p = Seg.query(0, N + 5)
    ans.append(p)
print(*ans, sep="\n")
