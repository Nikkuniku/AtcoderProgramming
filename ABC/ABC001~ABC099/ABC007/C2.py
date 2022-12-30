R,C=map(int,input().split())
sy,sx =map(int,input().split())
gy,gx=map(int,input().split())

maze=[]
for _ in range(R):
    maze.append(list(input()))

from collections import deque
d=deque([[sy-1,sx-1]])
dist=[[-1]*(C+2) for _ in range(R+2)]
dist[sy-1][sx-1]=0
while d:
    v=d.popleft()
    h,w=v[0],v[1]

    # up
    if dist[h-1][w]==-1 and maze[h-1][w]=='.':
        dist[h-1][w]=dist[h][w]+1
        d.append([h-1,w])
    # down
    if dist[h+1][w]==-1 and maze[h+1][w]=='.':
        dist[h+1][w]=dist[h][w]+1
        d.append([h+1,w])
    # right
    if dist[h][w+1]==-1 and maze[h][w+1]=='.':
        dist[h][w+1]=dist[h][w]+1
        d.append([h,w+1])
    # left 
    if dist[h][w-1]==-1 and maze[h][w-1]=='.':
        dist[h][w-1]=dist[h][w]+1
        d.append([h,w-1])

print(dist[gy-1][gx-1])