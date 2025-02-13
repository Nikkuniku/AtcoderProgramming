from collections import deque

N = int(input())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(N):
    S = list(input())
    for j, v in enumerate(S):
        if v == "Y":
            Edge[i].append(j)
value = [[-1] * N for _ in range(N)]
dist = [[-1] * N for _ in range(N)]
for i in range(N):
    value[i][i] = A[i]
for v in range(N):
    q = deque([v])
    dist[v][v] = 0
    while q:
        w = q.popleft()
        for e in Edge[w]:
            if dist[v][e] == -1:
                dist[v][e] = dist[v][w] + 1
                value[v][e] = A[e] + value[v][w]
                q.append(e)
            elif dist[v][e] == dist[v][w] + 1:
                value[v][e] = max(value[v][e], A[e] + value[v][w])
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if value[u][v] == -1:
        print("Impossible")
    else:
        print(dist[u][v], value[u][v])
