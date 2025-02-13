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


N = int(input())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
Edge_rev = [[] for _ in range(N)]
scc = Scc(N)
for i, v in enumerate(A):
    v -= 1
    Edge[i].append(v)
    Edge_rev[v].append(i)
    scc.add_edge(i, v)
groups = scc.scc()
cycle = [False] * N
ans = [1] * N
seen = [False] * N
for g in groups:
    if len(g) == 1:
        continue
    for v in g:
        cycle[v] = True
        ans[v] = len(g)


def dfs(v, k, p=-1):
    seen[v] = True
    ans[v] = k
    for e in Edge_rev[v]:
        if e == p:
            continue
        if cycle[e]:
            continue
        if e == v:
            continue
        dfs(e, k + 1, v)


for v in range(N):
    if seen[v]:
        continue
    dfs(v, ans[v])

print(sum(ans))
