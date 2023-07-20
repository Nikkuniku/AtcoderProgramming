from collections import defaultdict
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
ans = 2
for v in range(N):
    adj = set(Edge[v])
    adj.add(v)
    d = defaultdict(int)
    for u in adj:
        for e in Edge[u]:
            d[e] += 1
    P = list(d.values())
    if P.count(2) == 3:
        ans = max(ans, 3)
    if P.count(3) == 4:
        ans = max(ans, 4)
print(ans)
