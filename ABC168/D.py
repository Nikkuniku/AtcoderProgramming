n,m = map(int,input().split())

root = [[pow(10,9)]*n for _ in range(n)]

from collections import deque

root=[0]*n
r=[[]for i in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    r[a].append(b)
    r[b].append(a)

dist =[-1]*n
dist[0] = 0

q = deque([0])
prev=[-1] * n

while q:
    v = q.popleft()

    for j in r[v]:
        if dist[j]!=-1:
            continue
        else:
            dist[j] = dist[v] + 1
            prev[j] = v
            q.append(j)


for i in range(n):
    if i==0:
        print('Yes')
    else:
        print(prev[i]+1)
