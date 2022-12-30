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
S = [input() for _ in range(H)]
UF = UnionFind(H*W)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if 0 <= ni < H and 0 <= nj < W:
                if S[ni][nj] == '.':
                    continue
                UF.unite(W*i + j, W*ni+nj)


ans = 0
for i in range(H):
    for j in range(W):
        if W*i+j == UF.root(W*i+j) and S[i][j] == '#':
            ans += 1
print(ans)
