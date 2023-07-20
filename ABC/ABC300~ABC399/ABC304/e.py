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
UF = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    UF.unite(u-1, v-1)
# 連結成分ごとにグルーピング
gr = [-1]*N
cnt = 0
for i in range(N):
    if i == UF.root(i):
        gr[i] = cnt
        cnt += 1
for i in range(N):
    gr[i] = gr[UF.root(i)]
K = int(input())
Edge = [set() for _ in range(cnt)]
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    Edge[gr[x]].add(gr[y])
    Edge[gr[y]].add(gr[x])
ans = []
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    res = 'Yes'
    if gr[q] in Edge[gr[p]]:
        res = 'No'
    ans.append(res)
print(*ans, sep="\n")
