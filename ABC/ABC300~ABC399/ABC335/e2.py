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


N, M = map(int, input().split())
UF = UnionFind(N - 1)
A = list(map(int, input().split()))
Edge = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if A[u] == A[v]:
        UF.unite(u, v)
    Edge.append((u, v))
Edge_conv = []
for u, v in Edge:
    x = UF.root(u)
    y = UF.root(v)
    if x == -1:
        x = u
    if y == -1:
        y = v
    if A[x] < A[y]:
        Edge_conv.append((x, y, A[x]))
    if A[x] > A[y]:
        Edge_conv.append((y, x, A[y]))
dp = [0] * N
dp[UF.root(0)] = 1
Edge_conv.sort(key=lambda x: x[2])
for u, v, _ in Edge_conv:
    ru = UF.root(u)
    rv = UF.root(v)
    if ru == -1:
        ru = u
    if rv == -1:
        rv = v
    if dp[ru] > 0:
        dp[rv] = max(dp[rv], dp[ru] + 1)
print(dp[UF.root(N - 1)])
