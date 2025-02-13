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


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
UF = UnionFind(N - 1)
MOD = 998244353
for i in range(N):
    p = P[i] - 1
    q = Q[i] - 1
    UF.unite(p, q)
f = [0] * (N + 1)
g = [0] * (N + 1)
for i in range(1, N + 1):
    if i == 1:
        f[i] = 2
        g[i] = 1
    elif i == 2:
        f[i] = 3
        g[i] = 3
    elif i == 3:
        f[i] = 5
        g[i] = 4
    else:
        f[i] = f[i - 1] + f[i - 2]
        g[i] = f[i - 1] + f[i - 3]
    f[i] %= MOD
    g[i] %= MOD
ans = 1
for gr in UF.groups():
    ans *= g[len(gr)]
    ans %= MOD
print(ans)
