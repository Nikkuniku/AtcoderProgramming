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


W, H = map(int, input().split())
S = [[0]*(W+2)]
for _ in range(H):
    S.append([0]+list(map(int, input().split()))+[0])
S.append([0]*(W+2))
UF = UnionFind((W+2)*(H+2))
even = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
odd = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
edge = [even, odd]
for x in range(H+2):
    for y in range(W+2):
        for dx, dy in edge[x % 2]:
            nx = x+dx
            ny = y+dy
            if not (0 <= nx < H+2 and 0 <= ny < W+2):
                continue
            if S[x][y] == 0 and S[nx][ny] == 0:
                UF.unite((W+2)*x+y, (W+2)*nx+ny)
ans = 0
for x in range(H+2):
    for y in range(W+2):
        if S[x][y] == 0 and UF.issame(0, (W+2)*x+y):
            for dx, dy in edge[x % 2]:
                nx = x+dx
                ny = y+dy
                if not (0 <= nx < H+2 and 0 <= ny < W+2):
                    continue
                if S[nx][ny] == 1:
                    ans += 1
print(ans)
