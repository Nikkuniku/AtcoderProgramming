H,W=map(int,input().split())

ans=0
grid=[['#']*(W+2)]
for _ in range(H):
    p=list(input())
    grid.append(['#']+p+['#'])
    ans+=p.count('.')
grid.append(['#']*(W+2))

from collections import deque

dist=[[-1]*(W+2) for _ in range(H+2)]
dist[1][1]=0

d=deque([[1,1]])

while d:
    v=d.popleft()
    h=v[0]
    w=v[1]

    # up
    if dist[h-1][w]==-1 and grid[h-1][w]=='.':
        dist[h-1][w]=dist[h][w]+1
        d.append([h-1,w])
    # down
    if dist[h+1][w]==-1 and grid[h+1][w]=='.':
        dist[h+1][w]=dist[h][w]+1
        d.append([h+1,w])
    # right
    if dist[h][w+1]==-1 and grid[h][w+1]=='.':
        dist[h][w+1]=dist[h][w]+1
        d.append([h,w+1])
    # left
    if dist[h][w-1]==-1 and grid[h][w-1]=='.':
        dist[h][w-1]=dist[h][w]+1
        d.append([h,w-1])

if dist[H][W]==-1:
    ans=-1
else:
    ans-=(dist[H][W]+1)
print(ans)