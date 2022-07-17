from collections import deque
from ast import Break
from dis import dis


n = int(input())
X = []
Y = []
P = []
for _ in range(n):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

tmp = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        d = abs(X[i]-X[j])+abs(Y[i]-Y[j])
        tmp.append((i+1, j+1, d/P[i]))

tmp.sort(key=lambda x: x[1])
INF = 10**18

l = -1
r = 10**18
while r-l > 1:
    mid = (l+r)//2

    edge = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = abs(X[i]-X[j])+abs(Y[i]-Y[j])
            if mid*P[i] >= d:
                edge[i].append(j)

    for v in range(n):
        dist = [-1]*n
        dist[v] = 0
        q = deque([v])

        while q:
            v = q.popleft()
            for e in edge[v]:
                if dist[e] == -1:
                    dist[e] = dist[v]+1
                    q.append(e)

        if -1 not in dist:
            break

    if -1 not in dist:
        r = mid
    else:
        l = mid

print(r)
