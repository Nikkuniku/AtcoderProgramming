class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.rank = [0]*(n + 1)

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
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

    def rank(self, x):
        return self.rank[x]


N, M, K = map(int, input().split())
UF = UnionFind(N)
Edge = [list(map(int, input().split())) for _ in range(M)]
Edge.sort(key=lambda x: x[2])
ans = []
for u, v, w in Edge:
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    ans.append(w)
    if len(ans) == K:
        break
if len(ans) < K:
    print(-1)
else:
    print(sum(ans))
