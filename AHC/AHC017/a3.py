from random import choice, randint
from collections import Counter
from heapq import heappush, heappop
from math import ceil
from collections import deque


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


N, M, D, K = map(int, input().split())
Edge = []
adj = [[] for _ in range(N+1)]
for i in range(M):
    u, v, w = map(int, input().split())
    Edge.append((i, u, v, w))
    adj[u].append((v, w, i))
    adj[v].append((u, w, i))

for _ in range(N):
    x, y = map(int, input().split())
Frequency = [0]*M
INF = 1 << 60


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    used = [-1]*n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost, idx in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                used[to] = idx
                heappush(hq, (dist[to], to))

    for i in range(1, n):
        if used[i] == -1:
            continue
        Frequency[used[i]] += 1
    return dist


for i in range(1, N+1):
    dijkstra(i, N+1)

inputEdges = []
for i, u, v, w in Edge:
    freq = Frequency[i]
    inputEdges.append((i, u, v, w, freq))

# 頻度は高く、コストが低いものから優先して木を作る
# inputEdges.sort(key=lambda x: x[3])
inputEdges.sort(key=lambda x: x[4], reverse=True)
did = [False]*M
ans = [-1]*M
for d in range(D):
    # 頂点集合作成
    UF = UnionFind(N)
    # 既に工事済みの辺はくっつける
    for i, u, v, _, _ in inputEdges:
        if did[i]:
            UF.unite(u, v)
    kouji = []
    # 最小全域木の要領で工事しても良い辺を見つける
    for i, u, v, w, freq in inputEdges:
        if UF.issame(u, v):
            kouji.append((i, u, v, w, freq))
            continue
        UF.unite(u, v)
    # 以下の条件でソートする
    # 重みが大きい
    # 頻度が小さい
    # kouji.sort(key=lambda x: x[3], reverse=True)
    kouji.sort(key=lambda x: x[4])
    # 工事数
    cnt = 0
    flg = True
    q = deque(kouji)
    for j in range(len(kouji)):
        if j % 5 < 4:
            i, u, v, w, freq = q.popleft()
            # 既に工事済みなら何もしない
            if did[i]:
                continue
            # 工事したことないなら工事する。
            ans[i] = d+1
            did[i] = True
        else:
            i, u, v, w, freq = q.pop()
            # 既に工事済みなら何もしない
            if did[i]:
                continue
            # 工事したことないなら工事する。
            ans[i] = d+1
            did[i] = True
        cnt += 1
        if cnt >= K:
            break
print(*ans)
print(Counter(ans))
