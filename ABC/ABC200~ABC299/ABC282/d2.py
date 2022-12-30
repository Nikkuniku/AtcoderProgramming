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


N, M = map(int, input().split())
uf = UnionFind(2*N)
for _ in range(M):
    u, v = map(int, input().split())
    uf.unite(u-1, v-1+N)
    uf.unite(v-1, u-1+N)
is_bipertate = True
for i in range(N):
    if uf.issame(i, i+N):
        is_bipertate = False
Colors = [0]*(2*N)
for i in range(N):
    Colors[uf.root(i)] += 1
ans = N*(N-1)//2 - M
for c in Colors:
    ans -= c*(c-1)//2
print(ans if is_bipertate else 0)
