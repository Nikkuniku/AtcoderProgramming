from collections import defaultdict
import heapq
from collections import deque
N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
edge2 = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
indegree2 = [0]*(N+1)
dist = [-1]*(N+1)
d = defaultdict(lambda: -1)
for _ in range(M):
    x, y = map(int, input().split())
    edge[x].append(y)
    indegree[y] += 1
    if d[x, y] == -1:
        edge2[y].append(x)
        indegree2[x] += 1
        d[x, y] = 0
q = []
q2 = deque([])
heapq.heapify(q)
toposo = []
for v in range(1, N+1):
    if indegree[v] == 0:
        heapq.heappush(q, v)
    if indegree2[v] == 0:
        q2.append((N, v))
        dist[v] = N
while q:
    v = heapq.heappop(q)

    for e in edge[v]:
        indegree[e] -= 1
        if indegree[e] == 0:
            heapq.heappush(q, e)

    toposo.append(v)

if len(toposo) != N:
    print('No')
    exit()

seen = [False]*(N+1)
while q2:
    d, v = q2.popleft()
    seen[v] = True
    for e in edge2[v]:
        if seen[e]:
            continue
        dist[e] = d-1
        indegree2[e] -= 1
        if indegree2[e] == 0:
            q2.append((d-1, e))
if len(set(dist[1:])) == N:
    print('Yes')
    print(*dist[1:])
else:
    print('No')
