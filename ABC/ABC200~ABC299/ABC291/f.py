from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
INF = 1 << 60
dp = [[INF]*M for _ in range(N)]
dp[0] = [0]*M
for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == '1':
            Edge[i+1+j].append(i)
            dp[i+1+j][j] = min(dp[i])+1
q = deque([N-1])
dist = [-1]*N
dist[N-1] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            q.append(e)

ans = []
for k in range(1, N-1):
    tmp = INF
    for i in range(1, M):
        for j in range(1, M):
            if k+i-M == k:
                continue
            tmp = min(tmp, dp[k+i][j]+dist[k+i])
    if tmp == INF:
        ans.append(-1)
    else:
        ans.append(tmp)
print(*ans)
