N, M, E = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(E)]


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


uf = UnionFind(N+M)

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
cities = [0]*(N+M+1)
for i in range(1, N+M+1):
    if i <= N:
        cities[uf.root(i)] += 1
for i in range(1, N+M+1):
    cities[i] = cities[uf.root(i)]

for i in range(N+1, N+M+1):
    uf.unite(i, 0)

answer = []
ans = 0
for i in range(1, N+1):
    if uf.issame(i, 0):
        ans += 1
answer.append(ans)
query = orderdlist[::-1]
for i in range(Q):
    j = query[i]-1
    u, v = edge[j]
    if uf.issame(u, v):
        pass
    else:
        if (not uf.issame(u, 0)) and uf.issame(v, 0):
            ans += cities[uf.root(u)]
        elif (not uf.issame(v, 0)) and uf.issame(u, 0):
            ans += cities[uf.root(v)]
        else:
            p = cities[uf.root(u)]+cities[uf.root(v)]
            cities[uf.root(u)], cities[uf.root(v)] = p, p
        uf.unite(u, v)
    answer.append(ans)
answer = answer[:Q][::-1]
for a in answer:
    print(a)
