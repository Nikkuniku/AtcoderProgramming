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


N, M = map(int, input().split())
A = list(map(int, input().split()))
Edges = []
for i in range(N):
    for j in range(i+1, N):
        c = (pow(A[i], A[j], M) + pow(A[j], A[i], M)) % M
        Edges.append((i, j, c))
Edges.sort(key=lambda x: x[2], reverse=True)
uf = UnionFind(N)
ans = 0
for s, t, c in Edges:
    if uf.issame(s, t):
        continue
    uf.unite(s, t)
    ans += c
print(ans)
