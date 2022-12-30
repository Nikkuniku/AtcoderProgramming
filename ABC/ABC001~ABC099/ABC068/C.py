n,m = map(int,input().split())

edge = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a,b = a-1,b-1

    edge[a].append(b)
    edge[b].append(a)


from collections import deque

d = deque([0])

dist = [-1]*n
dist[0] = 0

while d:
    v = d.popleft()

    for w in edge[v]:
        if dist[w]==-1:
            dist[w]=dist[v]+1
            d.append(w)

 
if dist[-1]==2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

