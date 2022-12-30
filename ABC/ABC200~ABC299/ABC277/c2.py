from collections import defaultdict


class UnionFind:
    def __init__(self) -> None:
        self.par = defaultdict(lambda: -1)
        self.size = defaultdict(lambda: 1)

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


n = int(input())
uf = UnionFind()
ab = [list(map(int, input().split())) for _ in range(n)]

for a, b in ab:
    uf.unite(a, b)

ans = 1
nodes = list(uf.par.keys())
for k in nodes:
    if uf.issame(1, k):
        ans = max(ans, k)
print(ans)
print(uf.issize(1))
