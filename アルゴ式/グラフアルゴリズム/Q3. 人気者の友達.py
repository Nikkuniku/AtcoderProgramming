n, m = map(int, input().split())
edge = [[] for _ in range(n)]
indeg = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    indeg[a] += 1
    indeg[b] += 1
idx = indeg.index(max(indeg))
print(*sorted(edge[idx]))
