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


H, W = map(int, input().split())
uf = UnionFind(H*W)

grid = [list(input()) for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(H):
    for j in range(W):
        if grid[i][j] != 'B':
            continue

        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] == 'B':
                    uf.unite(W*i+j, W*ni+nj)

LU = [[[] for _ in range(W)] for _ in range(H)]
RD = [[[] for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] != 'B':
            continue
        # 根の場所を求める
        p = uf.root(W*i+j)
        x = p//W
        y = p % W

        if not LU[x][y]:
            LU[x][y].append((i, j))
        else:
            a, b = LU[x][y].pop()
            if i < a and j < b:
                LU[x][y].append((i, j))
            else:
                LU[x][y].append((a, b))

        if not RD[x][y]:
            RD[x][y].append((i, j))
        else:
            a, b = RD[x][y].pop()
            if a < i and b < j:
                RD[x][y].append((i, j))
            else:
                RD[x][y].append((a, b))

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] != 'B':
            continue
        # 根の場所を求める
        p = uf.root(W*i+j)
        x = p//W
        y = p % W
        if i == x and j == y:
            s = uf.issize(W*i+j)
            a, b = LU[x][y].pop()
            c, d = RD[x][y].pop()
            if (c-a+1)*(d-b+1) == s:
                ans += 1
print(ans)
