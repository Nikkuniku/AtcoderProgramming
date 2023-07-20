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
N = min(H, W)
C = [list(input()) for _ in range(H)]

UF = UnionFind(H*W)
dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]
for i in range(H):
    for j in range(W):
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if 0 <= ni < H and 0 <= nj < W:
                if C[i][j] == '#' and C[ni][nj] == '#':
                    UF.unite(W*i+j, W*ni+nj)
ans = [0]*N
for i in range(H):
    for j in range(W):
        if UF.root(W*i+j) == W*i+j and C[i][j] == '#':
            p = (UF.issize(W*i+j)-1)//4
            ans[p-1] += 1
print(*ans)
