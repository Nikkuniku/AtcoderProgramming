class WeightedUnionFind:
    def __init__(self, n) -> None:
        self.par = [i for i in range(n + 1)]
        self.rank = [0]*(n + 1)
        # 親への重み(cost)
        self.weight = [0]*(n + 1)

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
n,m=map(int,input().split())
u=WeightedUnionFind(n)

ans='Yes'
for _ in range(m):
    l,r,d=map(int,input().split())

    if u.issame(l,r):
        if u.diff(l,r)!=d:
            ans='No'
            break
    else:
        u.unite(l,r,d)

print(ans)