from collections import deque
n, x, y = map(int, input().split())
x, y = x-1, y-1
edge = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

dist = [-1]*n
fr = [-1]*n
q = deque([x])
dist[x] = 0
while q:
    v = q.popleft()
    for e in edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v]+1
            fr[e] = v
            q.append(e)

ans = []
now = y
while dist[now] != 0:
    ans.append(now)
    now = fr[now]
ans.append(x)
ans = [p+1 for p in ans][::-1]
print(*ans)
