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


def modinv(a: int, m: int) -> int:
    """
    モジュラ逆元
    ax mod m =1の解x=a^(-1)を返す

    Parameters
    ----------
    a:int
    m:int
    """
    x, y, u, v = 1, 0, 0, 1
    M = m
    while m > 0:
        k = a // m
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, m = m, a % m
    assert a == 1, "a and m aren't relatively prime numbers"
    if x < 0:
        x += M
    return x


H, W = map(int, input().split())
UF = UnionFind(H * W)
S = [list(input()) for _ in range(H)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
red = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            red += 1
            continue
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == "#":
                UF.unite(W * i + j, W * ni + nj)
init = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        if UF.root(W * i + j) == W * i + j:
            init += 1
MOD = 998244353
P = modinv(red, MOD)
res = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        roots = set()
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == "#":
                roots.add(UF.root(W * ni + nj))
        if len(roots) == 0:
            res += init + 1
        elif len(roots) > 0:
            res += init - (len(roots) - 1)
ans = res * P % MOD
print(ans)
