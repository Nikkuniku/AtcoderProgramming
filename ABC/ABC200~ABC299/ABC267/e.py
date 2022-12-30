import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
edge = [[]for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
cost = [0]*n

for i in range(n):
    for e in edge[i]:
        cost[e] += a[i]
q = [(cost[i], i) for i in range(n)]
heapq.heapify(q)
erased = [False]*n
ans = 0
while q:
    co, v = heapq.heappop(q)
    if erased[v]:
        continue
    erased[v] = True
    ans = max(ans, co)
    for e in edge[v]:
        if not erased[e]:
            cost[e] -= a[v]
            heapq.heappush(q, (cost[e], e))

print(ans)
