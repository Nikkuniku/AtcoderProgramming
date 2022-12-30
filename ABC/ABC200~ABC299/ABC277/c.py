from collections import defaultdict, deque
n = int(input())
edge = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = deque([1])
dist = defaultdict(int)
dist[1] = 0
while q:
    v = q.popleft()

    for e in edge[v]:
        if dist[e] == 0:
            dist[e] = dist[v]+1
            q.append(e)

ans = max(dist.keys())
print(ans)
