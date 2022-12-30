from collections import deque
N, M, s, t = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
q = deque([s])
dist = [-1]*N
dist[s] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            q.append(e)

ans = 'Yes'
if dist[t] == -1:
    ans = 'No'
print(ans)
