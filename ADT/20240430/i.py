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


from collections import deque

# n:頂点数
# m:辺の数
N, M = map(int, input().split())
scc = Scc(N)
Edge = [[] for _ in range(N)]
# 逆向きに格納
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    scc.add_edge(v, u)
    Edge[v].append(u)
groups = scc.scc()
q = deque()
for gr in groups:
    if len(gr) > 1:
        q.append(gr[0])
dist = [-1] * N
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v] + 1
        q.append(e)
ans = 0
for v in dist:
    ans += v >= 0
print(ans)
