class BellmanFord:
    def __init__(self, n, input_Edge) -> None:
        self.V = n
        self.INF = float('inf')
        self.Edge = input_Edge
        self.adj = [[] for _ in range(self.V)]
        for u, v, _ in input_Edge:
            self.adj[v].append(u)
        self.dist = [self.INF]*self.V

    def solve(self, start, goal) -> int:
        from collections import deque
        self.NegativeCycleOn_s_tPath = False
        q = deque([goal])
        seen = set([goal])
        while q:
            v = q.popleft()
            for e in self.adj[v]:
                if e in seen:
                    continue
                seen.add(e)
                q.append(e)
        seen.remove(goal)
        self.cnt = 0
        self.dist[start] = 0
        for self.cnt in range(self.V):
            changed = False
            for u, v, w in self.Edge:
                if self.dist[v] > self.dist[u]+w:
                    self.dist[v] = self.dist[u]+w
                    changed = True
                    if v in seen:
                        self.NegativeCycleOn_s_tPath = True
            if not changed:
                break

        res = self.dist[goal]
        if res == self.INF:
            return self.INF
        elif self.cnt == self.V-1 and self.NegativeCycleOn_s_tPath:
            return '-inf'
        return res


N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]
br = BellmanFord(N, Edge)
ans = br.solve(0, N-1)
if ans == float('inf'):
    print('impossible')
elif ans == float('-inf'):
    print('-inf')
else:
    print(ans)
