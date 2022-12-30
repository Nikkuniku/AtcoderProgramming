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
uf.unite(1, 2)
uf.unite(1, 4)
uf.unite(1, 6)
uf.unite(3, 5)
print(uf.par)
