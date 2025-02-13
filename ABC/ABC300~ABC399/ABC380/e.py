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
        self.left = [i for i in range(n + 1)]
        self.right = [i for i in range(n + 1)]

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
        self.left[x] = min(self.left[x], self.left[y])
        self.right[x] = max(self.right[x], self.right[y])
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


N, Q = map(int, input().split())
C = [1] * (N + 1)
R = [i for i in range(N + 1)]
UF = UnionFind(N)
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1:]
        root = UF.root(x)
        if root == -1:
            root = x
        color = R[root]
        size = UF.issize(root)
        R[root] = R[x] = c
        C[color] -= size
        C[c] += size
        adj_root_left = UF.left[root]
        if 1 <= adj_root_left - 1 <= N:
            if R[UF.root(adj_root_left)] == R[UF.root(adj_root_left - 1)]:
                UF.unite(adj_root_left, adj_root_left - 1)

        adj_root_right = UF.right[root]
        if 1 <= adj_root_right + 1 <= N:
            if R[UF.root(adj_root_right)] == R[UF.root(adj_root_right + 1)]:
                UF.unite(adj_root_right, adj_root_right + 1)

    elif query[0] == 2:
        c = query[1]
        ans.append(C[c])
print(*ans, sep="\n")
