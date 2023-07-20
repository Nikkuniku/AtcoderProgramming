from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
S, T = map(int, input().split())
S -= 1
T -= 1
q = deque([(S, 0)])
dist = [[-1]*N for _ in range(3)]
dist[0][S] = 0
while q:
    v, c = q.popleft()
    for e in Edge[v]:
        if dist[(c+1) % 3][e] != -1:
            continue
        dist[(c+1) % 3][e] = dist[c][v]+1
        q.append((e, (c+1) % 3))
if dist[0][T] == -1:
    ans = -1
else:
    ans = dist[0][T] // 3
print(ans)
