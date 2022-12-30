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


N, M, Q = map(int, input().split())
uf = UnionFind(N)
Queries = []
ans = ['No']*Q
for _ in range(M):
    a, b, c = map(lambda x: int(x)-1, input().split())
    Queries.append((0, -1, a, b, c))
for i in range(Q):
    u, v, w = map(lambda x: int(x)-1, input().split())
    Queries.append((1, i, u, v, w))

Queries.sort(key=lambda x: x[4])
for query in Queries:
    q, idx, u, v, w = query
    if q == 0:
        uf.unite(u, v)
    else:
        if uf.issame(u, v):
            continue
        ans[idx] = 'Yes'
print(*ans, sep="\n")
