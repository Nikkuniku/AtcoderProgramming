from itertools import combinations


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
grid = [list(input()) for _ in range(H)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
uf = UnionFind(H*W)
Adjacents = []
for i in range(H):
    for j in range(W):
        if grid[i][j] in ['S', '#']:
            continue
        for dx, dy in dxy:
            if 0 <= i+dx < H and 0 <= j+dy < W:
                if grid[i+dx][j+dy] == '.':
                    uf.unite(W*i+j, W*(i+dx)+j+dy)
                if grid[i+dx][j+dy] == 'S':
                    Adjacents.append((W*i+j))
ans = 'No'
Comb = combinations(Adjacents, 2)
for a, b in Comb:
    if uf.issame(a, b):
        ans = 'Yes'
print(ans)
