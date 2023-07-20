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


N, D = map(int, input().split())


def dist(P1, P2):
    d = (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2
    return d


UF = UnionFind(N)
Points = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if dist(Points[i], Points[j]) <= D**2:
            UF.unite(i, j)
ans = []
for i in range(N):
    res = 'No'
    if UF.issame(i, 0):
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
