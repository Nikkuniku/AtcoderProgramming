def segfunc(x, y):
    return x + y


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


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
Q = int(input())
Seg1 = SegTree([0] * (N + 1), segfunc, 0)
Seg2 = SegTree([0] * (N + 1), segfunc, 0)
UF = UnionFind(N)
ans = []
added = set()
for _ in range(Q):
    t, x, y, v = map(int, input().split())
    if t == 0:
        if x in added:
            continue
        if x % 2 == 0:
            Seg1.add(x, -v)
            Seg2.add(x, v)
        else:
            Seg1.add(x, v)
            Seg2.add(x, -v)
        added.add(x)
        UF.unite(x, y)
    elif t == 1:
        if not UF.issame(x, y):
            ans.append("Ambiguous")
            continue
        if x == y:
            ans.append(v)
            continue
        if x < y:
            if x % 2 == 0:
                if abs(x - y) % 2 == 0:
                    diff = Seg1.query(x, y) + v
                else:
                    diff = Seg2.query(x, y) - v
            else:
                if abs(x - y) % 2 == 0:
                    diff = Seg2.query(x, y) + v
                else:
                    diff = Seg1.query(x, y) - v
        else:
            if x % 2 == 0:
                if abs(x - y) % 2 == 0:
                    diff = Seg2.query(y, x) + v
                else:
                    diff = Seg1.query(y, x) - v
            else:
                if abs(x - y) % 2 == 0:
                    diff = Seg1.query(y, x) + v
                else:
                    diff = Seg2.query(y, x) - v
        ans.append(diff)
print(*ans, sep="\n")
