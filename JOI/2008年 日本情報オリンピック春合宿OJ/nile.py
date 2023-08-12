def segfunc(x, y):
    return min(x, y)


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


N, D = map(int, input().split())
INF = 1 << 60
Seg = SegTree([INF]*(3*N), segfunc, INF)
dp0 = [INF]*(3*N)
dp1 = [INF]*(3*N)
for i in range(D):
    S = list(map(int, input().split()))
    if i == 0:
        for j in range(3*N):
            if j % 3 == 0:
                dp1[j] = S[j//3]
                Seg.update(j, dp1[j])
    else:
        for j in range(3*N):
            if j % 3 == 0:
                p = Seg.query(0, j-(j % 3))
                q = Seg.query(j+3-(j % 3), 3*N+1)
                dp1[j] = min(p, q)+S[j//3]
            elif j % 3 == 1:
                dp1[j] = dp0[j-1]+(9*S[j//3]//10)
            elif j % 3 == 2:
                dp1[j] = min(dp0[j-1], dp0[j])+(7*S[j//3]//10)
        for j in range(3*N):
            Seg.update(j, dp1[j])
    dp1, dp0 = dp0, dp1
ans = min(dp0)
print(ans)
