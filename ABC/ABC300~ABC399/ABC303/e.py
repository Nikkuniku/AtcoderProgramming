from collections import deque
N = int(input())
Edge = [[] for _ in range(N)]
deg = [0]*N
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    deg[u] += 1
    deg[v] += 1
    Edge[u].append(v)
    Edge[v].append(u)

V = []
for i in range(N):
    if deg[i] == 1:
        V.append(i)
q = deque(V)
ans = []
seen = [False]*N
while q:
    v = q.popleft()
    seen[v] = True
    for e in Edge[v]:
        if seen[e]:
            continue
        ans.append(deg[e])
        seen[e] = True
        # 中心から出ている点
        for r in Edge[e]:
            seen[r] = True
            for t in Edge[r]:
                if not seen[t]:
                    q.append(t)

ans.sort()
print(*ans)
