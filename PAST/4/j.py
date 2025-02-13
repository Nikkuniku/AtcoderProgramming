from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
X = list(map(int, input().split()))
Group = [[] for _ in range(3)]
S = input()
for i, v in enumerate(S):
    if v == "A":
        Group[0].append(i)
    elif v == "B":
        Group[1].append(i)
    else:
        Group[2].append(i)
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((c, b))
    Edge[b].append((c, a))
INF = 1 << 60
q = [(0, 0)]
dist = [INF] * N
dist[0] = 0
while q:
    d, v = heappop(q)
    if dist[v] != d:
        continue
    for cost, e in Edge[v]:
        if d + cost < dist[e]:
            dist[e] = d + cost
            heappush(q, (dist[e], e))
    w = "ABC".index(S[v])
    R = set([0, 1, 2])
    R.discard(w)
    for i in R:
        for e in Group[i]:
            if w == 0 and i == 1:
                t = 0
            elif w == 0 and i == 2:
                t = 1
            elif w == 1 and i == 2:
                t = 2
            if d + X[t] < dist[e]:
                dist[e] = d + X[t]
                heappush(q, (dist[e], e))
ans = dist[-1]
print(ans)
