N, M, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v = map(int, input().split())
    if u >= N+1:
        u = 0
    if v >= N+1:
        v = 0
    edge.append((u, v))


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


uf = UnionFind(N+1)

s = set()
orderdlist = []
Q = int(input())
for _ in range(Q):
    j = int(input())
    s.add(j)
    orderdlist.append(j)

for i in range(E):
    if i+1 in s:
        continue
    u, v = edge[i]
    uf.unite(u, v)

answer = []
query = orderdlist[::-1]
for i in range(Q):
    j = query[i]-1
    u, v = edge[j]
    answer.append(uf.issize(0)-1)
    uf.unite(u, v)

answer = answer[:Q][::-1]
for a in answer:
    print(a)
