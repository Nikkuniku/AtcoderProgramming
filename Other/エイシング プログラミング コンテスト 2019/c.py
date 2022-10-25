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
        for nx, ny in zip(dx, dy):
            if 0 <= i+nx < h and 0 <= j+ny < w:
                if grid[i][j] == grid[i+nx][j+ny]:
                    continue
                uf.unite(w*i+j, w*(i+nx)+(j+ny))

whs = [0]*(h*w+1)
for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            p = uf.root(w*i+j)
            whs[p] += 1

s = set()
ans = 0
for i in range(h):
    for j in range(w):
        p = uf.root(w*i+j)
        if p not in s:
            ans += whs[p]*(uf.issize(p)-whs[p])
            s.add(p)
print(ans)
