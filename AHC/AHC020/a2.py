from random import shuffle
from random import randint
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
Scale = [5000]*N
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
around = []
for i in range(N):
    cnt = 0
    for a, b in People:
        if dist(*BroadCaster[i], a, b) <= 25000001:
            cnt += 1
    around.append((cnt, i))
around.sort()
around = around[::-1]
# 暫定値
BroadCasted = [[False]*N for _ in range(K)]
for _, i in around:
    l = 0
    r = Scale[i]
    while r-l > 1:
        mid = (l+r)//2
        isOK = True
        for j in range(K):
            if dist(*BroadCaster[i], *People[j]) <= mid**2:
                BroadCasted[j][i] = True
            else:
                BroadCasted[j][i] = False
        for j in range(K):
            if not any(BroadCasted[j]):
                isOK = False
        if isOK:
            r = mid
        else:
            l = mid
    Scale[i] = r

print(*Scale)
print(*UsedCable)
