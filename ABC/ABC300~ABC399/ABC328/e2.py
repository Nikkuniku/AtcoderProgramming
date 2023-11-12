class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

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


from itertools import combinations

N, M, K = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(M)]
C = combinations(range(M), N - 1)
ans = 1 << 60
for c in C:
    UF = UnionFind(N)
    Hascycle = False
    tmp = 0
    for p in c:
        u, v, w = cost[p]
        if UF.issame(u, v):
            Hascycle = True
            break
        UF.unite(u, v)
        tmp += w
        tmp %= K
    if UF.issize(1) == N and not Hascycle:
        ans = min(ans, tmp)
print(ans)
