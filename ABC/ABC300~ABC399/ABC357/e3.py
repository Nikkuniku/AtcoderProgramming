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


from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
ans = [1] * N
Edge = [[] for _ in range(N)]
indeg = [0] * N
outdeg = [0] * N
UF = UnionFind(N - 1)
for i, v in enumerate(A):
    Edge[v - 1].append(i)
    indeg[v - 1] += 1
    outdeg[i] += 1
    UF.unite(i, v - 1)
groups = UF.groups()


def dfs(v, cycles, s, p=-1):
    ans[v] = s
    for e in Edge[v]:
        if e == p:
            continue
        if e in cycles:
            continue
        dfs(e, cycles, s + 1, v)


# 連結成分ごとに処理
for g in groups:
    # 入次数がないもの空順に処理して閉路の点を求める
    cycle = set(g)
    q = deque()
    for v in g:
        if indeg[v] == 0:
            q.append(v)
    while q:
        v = q.popleft()
        cycle.discard(v)
        to = A[v] - 1
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)
    for v in cycle:
        dfs(v, cycle, len(cycle))
print(sum(ans))
