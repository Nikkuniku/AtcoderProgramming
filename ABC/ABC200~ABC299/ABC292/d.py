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
UF = UnionFind(N)
degree = [0]*N
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    UF.unite(u, v)
    degree[u] += 1
    degree[v] += 1
for i in range(N):
    if i != UF.root(i):
        degree[UF.root(i)] += degree[i]
ans = 'Yes'
for i in range(N):
    if i == UF.root(i):
        if UF.size[i] != degree[i]//2:
            ans = 'No'
print(ans)
