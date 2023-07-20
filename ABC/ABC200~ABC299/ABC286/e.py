from collections import deque
N = int(input())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == 'Y':
            Edge[i].append(j)
INF = 1 << 30
dist = [[INF]*N for _ in range(N)]
cost = [[0]*N for _ in range(N)]
for s in range(N):
    dist[s][s] = 0
    cost[s][s] = A[s]
    q = deque([s])
    while q:
        v = q.popleft()
        for e in Edge[v]:
            if dist[s][e] >= dist[s][v]+1 and cost[s][e] < cost[s][v]+A[e]:
                dist[s][e] = dist[s][v]+1
                cost[s][e] = cost[s][v]+A[e]
                q.append(e)
ans = []
Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    s = 'Impossible'
    if dist[U][V] == INF:
        print(s)
    else:
        print(dist[U][V], cost[U][V])
