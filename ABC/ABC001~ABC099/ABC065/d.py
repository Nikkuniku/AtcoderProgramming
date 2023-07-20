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


N = int(input())
points = [list(map(int, input().split()))+[i] for i in range(N)]
Edge = []
points.sort(key=lambda x: x[0])
for i in range(N-1):
    a, b, x = points[i]
    c, d, y = points[i+1]
    cost = min(abs(a-c), abs(b-d))
    Edge.append((x, y, cost))
points.sort(key=lambda x: x[1])
for i in range(N-1):
    a, b, x = points[i]
    c, d, y = points[i+1]
    cost = min(abs(a-c), abs(b-d))
    Edge.append((x, y, cost))
UF = UnionFind(N)
ans = 0
Edge.sort(key=lambda x: x[2])
for u, v, w in Edge:
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    ans += w
print(ans)
