class WeightedUnionFind:
    def __init__(self, n) -> None:
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        # 親への重み(cost)
        self.weight = [0] * (n + 1)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.root(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y, w):
        rx = self.root(x)
        ry = self.root(y)

        # unionbysize
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def rank(self, x):
        return self.rank[x]

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


N = int(input())
Q = int(input())
UF_1 = WeightedUnionFind(N)
UF_2 = WeightedUnionFind(N)
ans = []
for _ in range(Q):
    t, x, y, v = map(int, input().split())
    if t == 0:
        if x % 2 == 0:
            UF_1.unite(x, y, -v)
            UF_2.unite(x, y, v)
        else:
            UF_1.unite(x, y, v)
            UF_2.unite(x, y, -v)
    elif t == 1:
        if not UF_1.issame(x, y):
            ans.append("Ambiguous")
            continue
        if x == y:
            ans.append(v)
            continue
        if abs(x - y) % 2 == 0:
            if x < y:
                if x % 2 == 0:
                    diff = UF_1.diff(x, y) + v
                else:
                    diff = UF_2.diff(x, y) + v
            else:
                if x % 2 == 0:
                    diff = UF_2.diff(y, x) + v
                else:
                    diff = UF_1.diff(y, x) + v
        else:
            if x < y:
                if x % 2 == 0:
                    diff = UF_2.diff(x, y) - v
                else:
                    diff = UF_1.diff(x, y) - v
            else:
                if x % 2 == 0:
                    diff = UF_1.diff(y, x) - v
                else:
                    diff = UF_2.diff(y, x) - v
        ans.append(diff)
print(*ans, sep="\n")
