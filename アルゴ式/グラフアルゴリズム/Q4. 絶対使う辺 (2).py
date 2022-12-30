N, M = map(int, input().split())
Edge = [[i]+list(map(int, input().split())) for i in range(M)]
Edge.sort(key=lambda x: x[3])


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


# 最小全域木のコストを求める
UF = UnionFind(N)
W = 0
used = []
for i, u, v, w in Edge:
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    W += w
    used.append(i)

ans = N-1
for k in used:
    UF = UnionFind(N)
    tmp = 0
    for i in range(M):
        ei, ui, vi, wi = Edge[i]
        if ei == k:
            continue
        if UF.issame(ui, vi):
            continue
        UF.unite(ui, vi)
        tmp += wi

    if tmp == W and UF.issize(0) == N:
        ans -= 1
print(ans)
