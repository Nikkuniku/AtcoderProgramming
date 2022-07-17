from math import factorial
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.size = [1]*(n + 1)

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        # 既に同じグループなら何もしない
        if x == y:
            return False

        # unionbysize
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]

        return True

    def issize(self, x):
        return self.size[self.root(x)]


uf_r = UnionFind(n)
uf_c = UnionFind(n)
for i in range(n):
    for j in range(i+1, n):
        MergeFlg = True
        for m in range(n):
            if a[i][m]+a[j][m] <= k:
                continue
            else:
                MergeFlg = False
        if MergeFlg:
            uf_r.unite(i+1, j+1)

for i in range(n):
    for j in range(i+1, n):
        MergeFlg = True
        for m in range(n):
            if a[m][i]+a[m][j] <= k:
                continue
            else:
                MergeFlg = False

        if MergeFlg:
            uf_c.unite(i+1, j+1)

ans = 1
MOD = 998244353

for i in range(1, n+1):
    if uf_c.par[i] == -1:
        ans *= factorial(uf_c.size[i])
        ans % MOD
    if uf_r.par[i] == -1:
        ans *= factorial(uf_r.size[i])
        ans %= MOD

print(ans)
