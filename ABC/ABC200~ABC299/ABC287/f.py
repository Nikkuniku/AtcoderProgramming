from collections import deque
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
q = deque([0])
dist = [-1]*N
dist[0] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            q.append(e)
print(dist)
ans = [0]*N
for i in range(N):
    d = [0]*(N+1)
    for j in range(N):
        dist[]
