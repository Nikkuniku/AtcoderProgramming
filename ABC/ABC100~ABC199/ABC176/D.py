H,W=map(int,input().split())
Ch,Cw=map(int,input().split())
Dh,Dw=map(int,input().split())

grid=[]

for _ in range(H):
    grid.append(list(input()))

from collections import deque
d=deque([(Ch-1,Cw-1)])

dist=[[float('inf')]*W for _ in range(H)]
dist[Ch-1][Cw-1]=0

while d:
    v=d.popleft()
    h=v[0]
    w=v[1]

    for h2,w2 in (h+1,w),(h-1,w),(h,w-1),(h,w+1):
        if not (0<=h2<H and 0<=w2<W):
            continue
        if grid[h2][w2]=='.' and dist[h2][w2]>dist[h][w]:
            dist[h2][w2]=dist[h][w]
            d.appendleft((h2,w2))

    for h3,w3 in (h+1,w+1),(h-1,w+1),(h-1,w-1),(h+1,w-1):
        if not (0<=h3<H and 0<=w3<W):
            continue
        if grid[h3][w3]=='.' and dist[h3][w3]>dist[h][w]+1:
            dist[h3][w3]=dist[h][w]+1
            d.append((h3,w3))

    # 横6マス
    for hh in range(h-1,h+2):
        for ww in [w-2,w+2]:
            if not (0<=hh<H and 0<=ww<W):
                continue
            if grid[hh][ww]=='.' and dist[hh][ww]>dist[h][w]+1:
                dist[hh][ww]=dist[h][w]+1
                d.append((hh,ww))           
    # 上下
    for hh in [h-2,h+2]:
        for ww in range(w-2,w+3):
            if not (0<=hh<H and 0<=ww<W):
                continue
            if grid[hh][ww]=='.' and dist[hh][ww]>dist[h][w]+1:
                dist[hh][ww]=dist[h][w]+1
                d.append((hh,ww))    

# print(*grid,sep="\n")
# print(*dist,sep="\n")

ans=dist[Dh-1][Dw-1]
if ans==float('inf'):
    ans=-1
print(ans)