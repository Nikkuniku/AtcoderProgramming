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
Edge = []
for i in range(M):
    a, b, y = map(int, input().split())
    Edge.append((y, 1, a, b))
q = int(input())
for j in range(q):
    v, w = map(int, input().split())
    Edge.append((w, 2, j, v))
Edge.sort(key=lambda x: x[1], reverse=True)
Edge.sort(key=lambda x: x[0], reverse=True)
ans = [0]*q

UF = UnionFind(N)
for _, p, a, b in Edge:
    if p == 1:
        UF.unite(a, b)
    else:
        ans[a] = UF.issize(b)
print(*ans, sep="\n")
