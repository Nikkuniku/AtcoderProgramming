from collections import defaultdict


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


N, M = map(int, input().split())
S = input()
INF = float('inf')

dp = [INF]*(N+1)
dp[N] = 0
Seg = SegTree(dp, segfunc, INF)
d = defaultdict(lambda: INF)
d[0] = N
for i in range(N-1, -1, -1):
    if S[i] == '1':
        continue
    p = Seg.query(i+1, min(N+1, i+M+1))
    dp[i] = p+1
    d[p+1] = min(d[p+1], i)
    Seg.update(i, p+1)
ans = []
cnt = dp[0]
if cnt == INF:
    ans.append(-1)
else:
    while cnt > 0:
        ans.append(d[cnt-1]-d[cnt])
        cnt -= 1
print(*ans)