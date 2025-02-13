def segfunc(x, y):
    return max(x, y)


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


N, K = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(A)
ans = 0
right = 0
Seg = SegTree([0] * (maxA + 5), segfunc, 0)
for left in range(N):
    while (
        right < N
        and max(Seg.query(A[right], A[right] + 1) + 1, Seg.query(0, maxA + 1)) <= K
    ):
        Seg.add(A[right], 1)
        right += 1
    ans += right - 1 - left
    if right == left:
        right += 1
    else:
        Seg.add(A[left], -1)
print(ans)
