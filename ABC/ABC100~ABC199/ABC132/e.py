from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
kenkenpa = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
S, T = map(int, input().split())
S -= 1
T -= 1
for s in range(N):
    tmp1 = set()
    tmp2 = set()
    tmp3 = set()
    for e in Edge[s]:
        tmp1.add(e)
    for t in tmp1:
        for e in Edge[t]:
            tmp2.add(e)
    for v in tmp2:
        for e in Edge[v]:
            tmp3.add(e)
    kenkenpa[s] = list(tmp3)
q = deque([S])
dist = [-1]*N
dist[S] = 0
while q:
    v = q.popleft()
    for e in kenkenpa[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v]+1
        q.append(e)
ans = dist[T]
print(ans)
