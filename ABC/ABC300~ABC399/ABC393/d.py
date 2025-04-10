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


from itertools import accumulate

N = int(input())
S = input()
T = []
for i, v in enumerate(S):
    if v == "1":
        T.append(i)
if len(T) == 1:
    exit(print(0))
D = []
for i in range(len(T) - 1):
    D.append(T[i + 1] - T[i] - 1)
P = list(accumulate(D, initial=0))
Q = list(accumulate(D[::-1]))[::-1]
SegL = SegTree(P, segfunc, 0)
SegR = SegTree(Q, segfunc, 0)
ans = 1 << 60
M = len(P)
ans = [0] * M
for i in range(M):
    temp = P[i]
    res = SegL.query(i, M)
    res -= (M - i) * temp
    ans[i] += res
for i in range(1, len(Q)):
    temp = SegR.query(i, i + 1)
    res = SegR.query(0, i)
    res -= temp * i
    ans[i] += res

ans2 = 1 << 60
for i in range(len(ans) - 1):
    ans2 = min(ans2, ans[i])
print(ans2)
