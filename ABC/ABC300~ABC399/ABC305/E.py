from collections import defaultdict, deque
N, M, K = map(int, input().split())
seen = [-1]*N
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

d = defaultdict(lambda: -1)
patrol = []
for _ in range(K):
    p, h = map(int, input().split())
    p -= 1
    d[p] = h
    patrol.append((p, h))
patrol.sort(key=lambda x: x[1], reverse=True)
for p, h in patrol:
    q = deque([(p, h)])
    if seen[p] >= h:
        continue
    while q:
        v, hp = q.popleft()
        if d[v] > hp:
            hp = d[v]
        seen[v] = hp
        if hp == 0:
            continue
        for e in Edge[v]:
            if seen[e] >= hp-1:
                continue
            q.append((e, hp-1))
ans = []
for i in range(N):
    if seen[i] >= 0:
        ans.append(i+1)
print(len(ans))
print(*ans)
