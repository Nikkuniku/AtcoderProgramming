n = int(input())
sx, sy, tx, ty = map(int, input().split())


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


uf = UnionFind(n)
cir = []
for _ in range(n):
    x, y, r = map(int, input().split())
    cir.append((x, y, r))

for i in range(n):
    for j in range(i+1, n):
        x1, y1, r1 = cir[i]
        x2, y2, r2 = cir[j]
        if abs(r1-r2)**2 <= ((x1-x2)**2) + ((y1-y2)**2) <= (r1+r2)**2:
            uf.unite(i+1, j+1)

s = -1
t = -1
# sの属する円を求める
for i in range(n):
    x, y, r = cir[i]
    if (x-sx)**2 + (y-sy)**2 == r**2:
        s = i+1
        break
# tの属する円を求める
for i in range(n):
    x, y, r = cir[i]
    if (x-tx)**2 + (y-ty)**2 == r**2:
        t = i+1
        break

if uf.issame(s, t):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
