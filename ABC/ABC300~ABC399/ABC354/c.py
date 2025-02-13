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


from bisect import bisect_right

N = int(input())
B = [list(map(int, input().split())) + [i] for i in range(N)]
B.sort()
A = [B[i][0] for i in range(N)]
C = [B[i][1] for i in range(N)]
INF = 1 << 60
Seg = SegTree(C, segfunc, INF)
ans = []
for a, c, i in B:
    idx = bisect_right(A, a)
    p = Seg.query(idx, N + 1)
    if p < c:
        continue
    ans.append(i + 1)
ans.sort()
print(len(ans))
print(*ans)
