from collections import deque
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

q = deque([0])
dist = [-1]*N
dist[0] = 0
while q:
    v = q.popleft()
    for e in edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            q.append(e)
ans = 'IMPOSSIBLE'
if dist[N-1] == 2:
    ans = 'POSSIBLE'
print(ans)
