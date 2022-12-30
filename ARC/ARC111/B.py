N = int(input())
colors = 400002
deg = [0]*colors


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


uf = UnionFind(colors)
for _ in range(N):
    a, b = map(int, input().split())
    uf.unite(a, b)
    deg[a] += 1
    deg[b] += 1

for i in range(colors):
    if uf.root(i) == i:
        continue
    deg[uf.root(i)] += deg[i]

ans = 0
for i in range(colors):
    if uf.root(i) == i:
        deg[i] //= 2
        if deg[i]+1 == uf.issize(i):
            ans += uf.issize(i)-1
        else:
            ans += uf.issize(i)
print(ans)
