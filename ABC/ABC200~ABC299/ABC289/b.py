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
A = list(map(int, input().split()))

UF = UnionFind(N)
for i in range(M):
    UF.unite(A[i], A[i]+1)

ans = []
seen = [False]*(N+1)
for i in range(1, N+1):
    tmp = []
    for j in range(1, N+1):
        if i == UF.root(j):
            tmp.append(j)
    tmp.sort()
    tmp = tmp[::-1]
    for t in tmp:
        if seen[t]:
            continue
        else:
            ans.append(t)
print(*ans)
