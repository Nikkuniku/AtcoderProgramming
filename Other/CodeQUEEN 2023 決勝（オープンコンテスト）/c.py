from collections import deque
N, S, T = map(int, input().split())
S -= 1
T -= 1
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)

q = deque([S])
seen = [False]*N
seen[S] = True
past = [-1]*N
OnSTPath = []
while q:
    v = q.popleft()
    for e in Edge[v]:
        if seen[e]:
            continue
        seen[e] = True
        q.append(e)
        past[e] = v
now = T
while now != -1:
    OnSTPath.append(now)
    now = past[now]
ans = [-1]*N
q = deque()
for v in OnSTPath:
    ans[v] = 1
    q.append(v)
while q:
    v = q.popleft()
    for e in Edge[v]:
        if ans[e] != -1:
            continue
        ans[e] = ans[v]+1
        q.append(e)
print(*ans, sep="\n")
