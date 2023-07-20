from collections import defaultdict


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


def dist(A, B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])


N, W, K, C = map(int, input().split())
for _ in range(N):
    S = list(map(int, input().split()))
Pos = [list(map(int, input().split()))+["w"] for _ in range(W)]
for _ in range(K):
    Pos.append(list(map(int, input().split()))+["h"])
# print(Pos)


# def BitDP(points):
#     A = points
#     L = len(points)
#     INF = 1 << 30
#     # s:訪れた頂点集合
#     # u:出発点
#     # v:目的地
#     # w:スタート地点
#     maxdist = INF
#     path = []
#     for w in range(L):
#         dp = [[INF]*L for _ in range(1 << L)]
#         dp[0][w] = 0
#         pre = [[-1]*L for _ in range(1 << L)]
#         for s in range(1 << L):
#             for u in range(L):
#                 if not (s >> u) & 1 and s != 0:
#                     continue
#                 for v in range(L):
#                     if (s >> v) & 1:
#                         continue
#                     cost = dist(Pos[points[u]][:2], Pos[points[v]][:2])
#                     if dp[s | (1 << v)][v] > dp[s][u]+cost:
#                         dp[s | (1 << v)][v] = dp[s][u]+cost
#                         pre[s | (1 << v)][v] = u
#         if maxdist > min(dp[(1 << L)-1]):
#             maxdist = min(dp[(1 << L)-1])
#             path = pre
#     now=dp[(1<<L)-1].index(maxdist)
#     s
#     respath=[]
#     while now!=-1:
#         respath.append(now)
#         s^=(1<<now)
#         now=path[s][]
#     return maxdist, path


# クラスタの作成
l = 0
r = N+1
while r-l > 1:
    mid = (l+r)//2
    UF = UnionFind(W+K)
    res = True
    for i in range(W+K):
        for j in range(W+K):
            P = Pos[i][:2]
            Q = Pos[j][:2]
            if dist(P, Q) <= mid:
                UF.unite(i, j)
    for i in range(W+K):
        IsConnectedSource = False
        for j in range(W):
            if UF.issame(i, j):
                IsConnectedSource = True
        if not IsConnectedSource:
            res = False
            break
    if res:
        r = mid
    else:
        l = mid
UF = UnionFind(W+K)
for i in range(W+K):
    for j in range(W+K):
        P = Pos[i][:2]
        Q = Pos[j][:2]
        if dist(P, Q) <= r:
            UF.unite(i, j)
Connectivity = defaultdict(list)
for i in range(len(UF.par)-1):
    if UF.par[i] == -1:
        Connectivity[i] = [i]
    else:
        Connectivity[UF.par[i]].append(i)

# print(UF.par)
# print(Connectivity)
# for k, v in Connectivity.items():
#     print(k, v)

excavated = [[False]*N for _ in range(N)]

NOT_BROKEN = 0
BROKEN = 1
FINISH = 2
INVALID = -1


def decrease_s(x, y, p):
    S[x][y] -= p
    if S[x][y] > 0:
        return NOT_BROKEN


def destruct(x, y):
    power = 100
    while not excavated[x][y]:
        print(x, y, power, flush=True)
        res = int(input())
        if res == FINISH:
            excavated[x][y] = True
            exit()
        elif res == BROKEN:
            excavated[x][y] = True
            return BROKEN
        elif res == INVALID:
            exit()


for k, vs in Connectivity.items():
    for i in range(len(vs)-1):
        x1, y1 = Pos[vs[i]][:2]
        x2, y2 = Pos[vs[i+1]][:2]
        sgn_X = 1 if x1 < x2 else -1
        sgn_Y = 1 if y1 < y2 else -1
        for X in range(x1, x2+sgn_X, sgn_X):
            if excavated[X][y1]:
                continue
            r = destruct(X, y1)
        for Y in range(y1, y2+sgn_Y, sgn_Y):
            if excavated[X][Y]:
                continue
            r = destruct(X, Y)
