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
        self.gsize = n

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
        self.gsize -= 1

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


def mapping(i, j, w):
    return i * w + j


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dij_L = [(-1, 0), (1, 0), (0, -1)]
dij_R = [(-1, 0), (1, 0), (0, 1)]
UF_L = UnionFind(H * W)
UF_R = UnionFind(H * W)
dp = [-1] * W
ep = [-1] * W
for j in range(W):
    for i in range(H):
        v = mapping(i, j, W)
        for di, dj in dij_L:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if A[i][j] != A[ni][nj]:
                continue
            w = mapping(ni, nj, W)
            UF_L.unite(v, w)
    dp[j] = UF_L.gsize - H * (W - j - 1)
for j in range(W - 1, -1, -1):
    for i in range(H):
        v = mapping(i, j, W)
        for di, dj in dij_R:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if A[i][j] != A[ni][nj]:
                continue
            w = mapping(ni, nj, W)
            UF_R.unite(v, w)
    ep[j] = UF_R.gsize - H * j
ans = 1 << 60
for k in range(W - 1):
    ans = min(ans, dp[k] + ep[k + 1])
print(ans)
