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
UF = UnionFind(2*N)
X = 0
for i in range(N):
    UF.unite(2*i, 2*i+1)
for _ in range(M):
    A, B, C, D = input().split()
    A = int(A)-1
    C = int(C)-1
    if B == 'R':
        if D == 'R':
            v = 2*A
            w = 2*C
        else:
            v = 2*A
            w = 2*C+1
    else:
        if D == 'R':
            v = 2*A+1
            w = 2*C
        else:
            v = 2*A+1
            w = 2*C+1
    if UF.issame(v, w):
        X += 1
    UF.unite(v, w)
Y = 0
for i in range(2*N):
    if UF.root(i) == i:
        Y += 1
print(X, Y-X)
