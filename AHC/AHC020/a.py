from math import ceil


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


def dist(a, b, c, d):
    return (a-c)**2 + (b-d)**2


N, M, K = map(int, input().split())
BroadCaster = [list(map(int, input().split())) for _ in range(N)]
Edge = [list(map(int, input().split()))+[i] for i in range(M)]
Edge.sort(key=lambda x: x[2])
UF = UnionFind(N)
# ******
# Output
Scale = [0]*N
UsedCable = [0]*M
# ******
for u, v, w, i in Edge:
    u -= 1
    v -= 1
    if UF.issame(u, v):
        continue
    UF.unite(u, v)
    UsedCable[i] = 1
People = [list(map(int, input().split())) for _ in range(K)]
ScaleCan = [[] for _ in range(N)]
for a, b in People:
    idx = -1
    dist_min = 1 << 60
    for i in range(N):
        dist_tmp = dist(a, b, *BroadCaster[i])
        if dist_min > dist_tmp:
            dist_min = dist_tmp
            idx = i
    dist_min = ceil(dist_min**(1/2))
    ScaleCan[idx].append(dist_min)
for i in range(N):
    if ScaleCan[i]:
        Scale[i] = max(ScaleCan[i])
for i in range(N):
    Scale[i] = max(0, Scale[i]-1)
print(*Scale)
print(*UsedCable)
