import sys

sys.setrecursionlimit(10**8)


class Scc:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, fr, to):
        assert 0 <= fr < self.n
        assert 0 <= to < self.n
        self.edges.append((fr, to))

    def scc(self):
        csr_start = [0] * (self.n + 1)
        csr_elist = [0] * len(self.edges)
        for fr, to in self.edges:
            csr_start[fr + 1] += 1
        for i in range(1, self.n + 1):
            csr_start[i] += csr_start[i - 1]
        counter = csr_start[:]
        for fr, to in self.edges:
            csr_elist[counter[fr]] = to
            counter[fr] += 1

        self.now_ord = self.group_num = 0
        self.visited = []
        self.low = [0] * self.n
        self.ord = [-1] * self.n
        self.ids = [0] * self.n

        def _dfs(v):
            self.low[v] = self.ord[v] = self.now_ord
            self.now_ord += 1
            self.visited.append(v)
            for i in range(csr_start[v], csr_start[v + 1]):
                to = csr_elist[i]
                if self.ord[to] == -1:
                    _dfs(to)
                    self.low[v] = min(self.low[v], self.low[to])
                else:
                    self.low[v] = min(self.low[v], self.ord[to])
            if self.low[v] == self.ord[v]:
                while 1:
                    u = self.visited.pop()
                    self.ord[u] = self.n
                    self.ids[u] = self.group_num
                    if u == v:
                        break
                self.group_num += 1

        for i in range(self.n):
            if self.ord[i] == -1:
                _dfs(i)
        for i in range(self.n):
            self.ids[i] = self.group_num - 1 - self.ids[i]
        groups = [[] for _ in range(self.group_num)]
        for i in range(self.n):
            groups[self.ids[i]].append(i)
        return groups


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


from collections import deque
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
UF = UnionFind(N - 1)
indeg = [0] * N
outdeg = [0] * N
infrom = defaultdict(list)
to = [-1] * N
for i, v in enumerate(A):
    UF.unite(i, v - 1)
    indeg[v - 1] += 1
    outdeg[i] += 1
    infrom[v - 1].append(i)
    to[i] = v - 1
# scc:強連結成分分解
scc = Scc(N)

# sccを初期化した後は、辺を加える。
# tupleの形で,(a,b)（aからbへ向かう辺）をABに格納
AB = [(i, A[i] - 1) for i in range(N)]
for a, b in AB:
    scc.add_edge(a, b)
groups = scc.scc()
print(groups)
cycle = set()
for g in groups:
    if len(g) > 0:
        cycle.add(g)
ans = 0
for g in UF.groups():
    outonly = 0
    cycle = 0
    M = len(g)
    q = deque()
    tmp = 0
    iscycle = False
    for v in g:
        if v in cycle:
            iscycle = True
            break
    for v in g:
        if v == A[v] - 1:
            q.append(v)
        elif indeg[v] > 0 and outdeg[v] == 0:
            q.append(v)
    seen = defaultdict(lambda: False)
    inonly = 0
    while q:
        v = q.popleft()
        inonly += 1
        for k in infrom[v]:
            indeg[v] -= 1
            outdeg[k] -= 1
            if outdeg[k] == 0:
                q.append(k)

print(ans)
