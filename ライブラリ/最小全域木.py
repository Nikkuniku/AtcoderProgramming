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


V, E = map(int, input().split())
uf = UnionFind(V)
Edge = [list(map(int, input().split())) for _ in range(E)]
Edge.sort(key=lambda x: x[2])
AdoptedEdge = []
ans = 0
for a, b, c in Edge:
    if uf.issame(a, b):
        continue
    uf.unite(a, b)
    AdoptedEdge.append((a, b, c))
    ans += c
print(ans)
print(AdoptedEdge)
