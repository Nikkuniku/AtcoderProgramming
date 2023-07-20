from collections import defaultdict


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
user = [input().split() for _ in range(N)]
used = set()
i = 0
d = defaultdict(int)
for s, t in user:
    if s not in used:
        d[s] = i
        i += 1
        used.add(s)
    if t not in used:
        d[t] = i
        i += 1
        used.add(t)

M = len(d.keys())
UF = UnionFind(M)
ans = 'Yes'
for s, t in user:
    v = d[s]
    w = d[t]
    if UF.issame(v, w):
        ans = 'No'
    UF.unite(v, w)
print(ans)
