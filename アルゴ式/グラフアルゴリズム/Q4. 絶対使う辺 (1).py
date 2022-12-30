N, M = map(int, input().split())
Edge = [[i]+list(map(int, input().split())) for i in range(M)]
Edge.sort(key=lambda x: x[3])


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


# 最小全域木のコストを求める
UF = UnionFind(N)
W = 0
for i, u, v, w in Edge:
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    W += w

ans = 0
for k in range(M):
    UF = UnionFind(N)
    tmp = 0
    for i in range(M):
        if i == k:
            continue
        ei, ui, vi, wi = Edge[i]
        if UF.issame(ui, vi):
            continue
        UF.unite(ui, vi)
        tmp += wi

    if tmp != W:
        ans += 1
print(ans)
