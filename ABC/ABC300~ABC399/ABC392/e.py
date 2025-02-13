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


from collections import defaultdict

N, M = map(int, input().split())
UF = UnionFind(N - 1)
Cable = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    Cable.append((i, a, b))
    UF.unite(a, b)
abudants = defaultdict(list)
for i, a, b in Cable:
    r = UF.root(a)
    abudants[r].append((i, a, b))
pars = []
for i in range(N):
    if UF.root(i) == i:
        pars.append(i)
wastes = defaultdict(list)
s_pars = set(pars)
q = []
for r in pars:
    seen = set()
    for i, a, b in abudants[r]:
        if a == b:
            wastes[r].append((i, a, b))
        elif (a, b) in seen:
            wastes[r].append((i, a, b))
        else:
            seen.add((a, b))
    q.append((len(wastes[r]), r))
q.sort(reverse=True)
ans = []
for k, r in q:
    if k == 0:
        continue
    for i, a, b in wastes[r]:
        for s in s_pars:
            if UF.issame(a, s):
                continue
            ans.append((i + 1, b + 1, s + 1))
            UF.unite(b, s)
            s_pars.discard(s)
            break
        if UF.issize(0) == N:
            break
print(len(ans))
for c in ans:
    print(*c)
