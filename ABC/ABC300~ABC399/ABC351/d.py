class UnionFind:
    def __init__(self, n) -> None:
        """
        初期化

        Parameters
        ----------
        n:要素数
        """
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x) -> int:
        """
        xの属するグループの親番号を返す

        Parameters
        ----------
        x:要素番号

        Return
        ------
        res:int
            xの属するグループの親番号
        """
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y) -> bool:
        """
        xとyが同じグループに属するかどうかを返す

        Parameters
        ----------
        x,y:要素番号

        Return
        ------
        res:bool
            true:xとyは同じグループである
            false:xとyは同じグループでない
        """
        return self.root(x) == self.root(y)

    def unite(self, x, y) -> bool:
        """
        xの属するグループとyの属するグループを併合する

        Parameters
        ----------
        x,y:要素番号

        Return
        ------
        res:bool
            true:xとy、それぞれの属するグループを併合する
            false:xとyはすでに同じグループのため、併合は行わない
        """
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

    def issize(self, x) -> int:
        """
        xの属するグループのサイズを返す

        Return
        ------
        res:int
            xの属するグループのサイズ
        """
        return self.size[self.root(x)]

    def groups(self) -> list:
        """
        グループ構造の詳細を返す

        Return
        ------
        res:list[]
            グループ構造を返す
        """
        member = [[] for _ in range(len(self.par))]
        for v in range(len(self.par)):
            member[self.root(v)].append(v)
        res = []
        for mem in member:
            if mem:
                res.append(mem)
        return res


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
P = [[0] * W for _ in range(H)]
dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            P[i][j] = 2
            continue
        isOK = True
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == "#":
                isOK = False
        if isOK:
            P[i][j] = 1
        else:
            P[i][j] = 0
UF = UnionFind(H * W)
# 連結パート
for i in range(H):
    for j in range(W):
        if P[i][j] == 0 or P[i][j] == 2:
            continue
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if P[ni][nj] == 1:
                UF.unite(W * i + j, W * ni + nj)
from collections import defaultdict

d = defaultdict(int)
add = defaultdict(set)
for i in range(H):
    for j in range(W):
        if UF.root(W * i + j) == W * i + j:
            d[W * i + j] = UF.issize(W * i + j)
for i in range(H):
    for j in range(W):
        if P[i][j] == 0 or P[i][j] == 2:
            continue
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if P[ni][nj] == 0:
                add[UF.root(W * i + j)].add((ni, nj))
ans = 1
for k, v in d.items():
    tmp = v + len(add[k])
    ans = max(ans, tmp)
print(ans)
