from collections import deque
N, M = map(int, input().split())
edge = [[0]*N for _ in range(N)]
ans = 0
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u][v] = 1
    adj[u].append(v)
for s in range(N):
    q = deque([s])
    visited = [False]*N
    while q:
        v = q.popleft()
        visited[v] = True
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                if edge[s][e] == 0:
                    edge[s][e] = 1
                    ans += 1

print(ans)
