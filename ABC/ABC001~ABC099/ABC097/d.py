from collections import defaultdict


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


n, m = map(int, input().split())
p = list(map(int, input().split()))

u = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    u.unite(x, y)

d = defaultdict(int)
for i in range(n):
    d[p[i]] = i+1

ans = 0
for i in range(n):
    v = p[i]
    if u.issame(d[v], v):
        ans += 1

print(ans)
