h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]


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


uf = UnionFind(h*w)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            continue
        d = w*i+j
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            nd = w*ni+nj
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] == '#':
                    uf.unite(d, nd)

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            c = uf.issize(w*i + j)
            if c == 1:
                print('No')
                exit()
print('Yes')
