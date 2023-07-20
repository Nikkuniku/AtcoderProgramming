from collections import defaultdict
N = int(input())
Edge = [[] for _ in range(N)]
d = defaultdict(int)
deg = [0]*N
for i in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
    deg[a] += 1
    deg[b] += 1
    d[(a, b)] = i
    d[(b, a)] = i
ans = 0
Edges = [False]*(N-1)
CoveredEdge = 0
vertex = []
for i, v in enumerate(deg):
    vertex.append((i, v))
vertex.sort(key=lambda x: x[1], reverse=True)
for v, _ in vertex:
    if CoveredEdge == N-1:
        continue
    selected = False
    for e in Edge[v]:
        if Edges[d[e, v]]:
            continue
        selected = True
        Edges[d[(e, v)]] = True
        CoveredEdge += 1

    if selected:
        ans += 1
print(ans)
