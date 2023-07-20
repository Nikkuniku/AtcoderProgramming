from collections import deque, defaultdict
d = defaultdict(list)
N, M = map(int, input().split())
edge = [[] for _ in range(N+M)]
for i in range(N):
    A = int(input())
    S = list(map(int, input().split()))
    for j in range(A):
        u = i
        v = S[j]+N-1
        edge[u].append(v)
        edge[v].append(u)
        if S[j] == M:
            d[M].append(i)
        if S[j] == 1:
            d[1].append(i)
q = deque(d[1])
dist = [-1]*(N+M)
for v in d[1]:
    dist[v] = 0
while q:
    v = q.popleft()
    for e in edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v]+1
        q.append(e)
INF = 1 << 60
ans = INF
for v in d[M]:
    if dist[v] == -1:
        continue
    ans = min(ans, dist[v]//2)
if ans == INF:
    ans = -1
print(ans)
