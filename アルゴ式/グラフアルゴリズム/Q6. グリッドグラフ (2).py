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


H, W = map(int, input().split())
UF = UnionFind(H*W)
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H-1)]
Edge = []
total = 0
for i in range(H):
    for j in range(W-1):
        p = i*W + j
        q = i*W + j+1
        Edge.append((p, q, A[i][j]))
        total += A[i][j]
for i in range(H-1):
    for j in range(W):
        p = i*W + j
        q = (i+1)*W + j
        Edge.append((p, q, B[i][j]))
        total += B[i][j]

Edge.sort(key=lambda x: x[2], reverse=True)
selected = 0
for u, v, c in Edge:
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    selected += c
print(total-selected)
