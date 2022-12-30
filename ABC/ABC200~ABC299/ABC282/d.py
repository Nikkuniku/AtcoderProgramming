from collections import defaultdict
import sys


class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.size = [1]*(n + 1)

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
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

    def issize(self, x):
        return self.size[self.root(x)]


# 再帰の深さが1000を超えそうなときはこれをやっておく
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
edge = [[]for _ in range(N)]
deg = [0]*N
uf = UnionFind(N)
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    edge[u].append(v)
    edge[v].append(u)
    deg[u] += 1
    deg[v] += 1
    uf.unite(u, v)
colors = [0 for i in range(N)]


def dfs(v, color):
    # 今いる点を着色
    colors[v] = color
    # 今の頂点から行けるところをチェック
    for to in edge[v]:
        # 同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        # 未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    # 調べ終わったら矛盾がないのでTrue
    return True

# 2部グラフならTrue, そうでなければFalse


def is_bipartite(v):
    return dfs(v, 1)  # 頂点0を黒(1)で塗ってDFS開始


d = defaultdict(int)
color_group = defaultdict(int)
Connectivities = set()
for i in range(N):
    if uf.root(i) == i:
        if is_bipartite(i):
            Connectivities.add(i)
        else:
            print(0)
            exit()
# 連結成分ごとの色塗分けグループ
for i in range(N):
    p = uf.root(i)
    if p in Connectivities:
        color_group[(p, colors[i])] += 1

ans = N*(N-1)//2 - M
for i in Connectivities:
    a, b = color_group[(i, -1)], color_group[(i, 1)]
    ans -= (a*(a-1)//2 + b*(b-1)//2)

print(ans)
