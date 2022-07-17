from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
a = list(map(int, input().split()))
outdegree = [0]*n
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    outdegree[x] += 1
S = set()
for i, v in enumerate(outdegree):
    if v > 0:
        S.add(i)
INF = 10**18
val = [INF]*n
b = []
for i in range(n):
    if i in S:
        b.append((i, a[i]))
b.sort(key=lambda x: x[1])
for p in b:
    v, c = p
    d = deque([v])
    while d:
        v = d.popleft()

        for e in edge[v]:
            if val[e] > c:
                val[e] = c
                d.append(e)
ans = -INF
for i in range(n):
    ans = max(a[i]-val[i], ans)
print(ans)
