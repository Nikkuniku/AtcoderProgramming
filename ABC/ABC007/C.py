r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
sy,sx=sy-1,sx-1
meiro=[]
for _ in range(r):
    meiro.append(list(input()))

from collections import deque
q=deque([[sy,sx]])

dist=[[-1 for _ in range(c)] for _ in range(r)]


dist[sy][sx]=0
#スタート地点の周りの移動可能なマスをキューに入れる


while q:
    v=q.popleft()
    vy,vx=v[0],v[1]

    if meiro[vy+1][vx]=='.' and dist[vy+1][vx]==-1:
        dist[vy+1][vx]=dist[vy][vx]+1
        q.append([vy+1,vx])
    if meiro[vy-1][vx]=='.' and dist[vy-1][vx]==-1:
        dist[vy-1][vx]=dist[vy][vx]+1
        q.append([vy-1,vx])
    if meiro[vy][vx-1]=='.' and dist[vy][vx-1]==-1:
        dist[vy][vx-1]=dist[vy][vx]+1
        q.append([vy,vx-1])
    if meiro[vy][vx+1]=='.' and dist[vy][vx+1]==-1:
        dist[vy][vx+1]=dist[vy][vx]+1
        q.append([vy,vx+1])

print(dist[gy-1][gx-1])