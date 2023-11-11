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


N = int(input())
UF = UnionFind()
for _ in range(N):
    a, b = map(int, input().split())
    UF.unite(a, b)

ans = 1
a = list(UF.par.keys())
for s in a:
    if UF.issame(1, s):
        ans = max(ans, s)
print(ans)
