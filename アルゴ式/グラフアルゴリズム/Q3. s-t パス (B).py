from collections import deque
N, M, s, t = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
seen = [False]*N
prev = [-1]*N

q = deque([s])
while q:
    v = q.popleft()
    seen[v] = True
    for e in Edge[v]:
        if seen[e]:
            continue
        q.append(e)
        prev[e] = v

ans = []
now = t
while now != -1:
    ans.append(now)
    now = prev[now]
print(len(ans))
print(*ans[::-1])
