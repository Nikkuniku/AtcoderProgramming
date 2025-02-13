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


N, M, K = map(int, input().split())
C = list(map(int, input().split()))
A = list(map(int, input().split()))
Seg = SegTree([1 << 60] * (M + 1), segfunc, 1 << 60)
for i in range(M):
    Seg.update(i + 1, A[i] * K)
from collections import deque

ans = 1 << 60
q = deque()
for i in range(N):
    c = C[i]
    q.append(c)
    Seg.add(c, -A[c - 1])
    if len(q) == K:
        ans = min(ans, Seg.query(1, M + 1))
        v = q.popleft()
        Seg.add(v, A[v - 1])
print(ans)
