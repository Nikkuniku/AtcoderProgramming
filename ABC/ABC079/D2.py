h,w=map(int,input().split())
c=[]
for _ in range(10):
    c.append(list(map(int,input().split())))

a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))
from collections import deque

distance=[0]*10

def func(s):
    global dist
    global distance
    dist=[float('inf')]*10
    dist[s]=0
    d=deque([s])

    while d:
        v=d.popleft()

        for e in range(10):
            if dist[v]+c[v][e]<dist[e]:
                dist[e]=dist[v]+c[v][e]
                d.append(e)

    distance[s]=dist[1]


for i in range(10):
    if i==1:
        continue
    func(i)
ans=0
for i in range(h):
    for j in range(w):
        ans+=distance[abs(a[i][j])]

print(ans)