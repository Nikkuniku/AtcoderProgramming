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


N, M = map(int, input().split())
P = list(map(int, input().split()))
UF = UnionFind(N)
for i in range(N):
    UF.unite(i+1, P[i])
C = 0
for i in range(1, N+1):
    if UF.root(i) == i:
        C += 1
MOD = 998244353
inv_b = pow(2, MOD-2, MOD)
ans = (pow(M, N, MOD)-pow(M, C, MOD))*inv_b % MOD
print(ans)
