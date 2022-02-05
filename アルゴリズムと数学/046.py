from collections import deque
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())

grid=[]
for _ in range(r):
    grid.append(list(input()))

sy-=1
sx-=1
gy-=1
gx-=1

dist=[[-1]*c for _ in range(r)]
dist[sy][sx]=0
q=deque([[sy,sx]])
dx=[0,1,0,-1]
dy=[-1,0,1,0]

while q:
    v=q.popleft()

    for k in range(4):
        ny = v[0]+dy[k]
        nx = v[1]+dx[k]

        if grid[ny][nx]=='.' and dist[ny][nx]==-1:
            dist[ny][nx]=dist[v[0]][v[1]]+1
            q.append([ny,nx])

print(dist[gy][gx])