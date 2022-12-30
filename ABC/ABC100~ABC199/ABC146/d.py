from collections import deque, defaultdict
n = int(input())
edge = [[] for _ in range(n+1)]
edges = []
d = defaultdict(int)
for i in range(n-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    edge[a].append(b)
    edge[b].append(a)
# (頂点,色)
q = deque([(1, -1)])
dist = [-1]*(n+1)
dist[1] = 0
while q:
    v, c = q.popleft()
    k = 1

    for e in edge[v]:
        if dist[e] == -1:
            if k == c:
                k += 1
            dist[e] = dist[v]+1
            d[(v, e)] = k
            d[(e, v)] = k
            q.append((e, k))
            k += 1
print(max(d.values()))
for c in edges:
    print(d[c])
