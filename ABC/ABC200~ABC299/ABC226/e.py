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
MOD = 998244353
uf = UnionFind(N)
Edges = [[] for _ in range(N)]
deg = [0]*N
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    uf.unite(a, b)
    deg[a] += 1
    deg[b] += 1

ans = 1
for i in range(N):
    if i == uf.root(i):
        continue
    deg[uf.root(i)] += deg[i]

for i in range(N):
    if i == uf.root(i):
        deg[i] //= 2
        if uf.issize(i) == deg[i]:
            ans *= 2
        else:
            ans *= 0
    ans %= MOD
print(ans)
