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
S = [list(input()) for _ in range(N)]


def f(S, x, y):
    R = [["."] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == x and j == y:
                continue
            if S[i][j] == "#":
                R[i][j] = "#"
    UF = UnionFind(N * M)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        for j in range(M):
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy
                if not (0 <= ni < N and 0 <= nj < M):
                    continue
                if R[i][j] == R[ni][nj] == ".":
                    UF.unite(M * i + j, M * ni + nj)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if R[i][j] == ".":
                if UF.root(M * i + j) == M * i + j:
                    cnt += 1
    return cnt == 1


ans = 0
for i in range(N):
    for j in range(M):
        if S[i][j] == "#":
            ans += f(S, i, j)
print(ans)
