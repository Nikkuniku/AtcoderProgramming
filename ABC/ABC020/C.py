H,W,T=map(int,input().split())
grid=[]

for i in range(H):
    p=list(input())
    if 'S' in p:
        S=(i,p.index('S'))
    if 'G' in p:
        G=(i,p.index('G'))
    grid.append(p)

import heapq
def dijkstra(s,g,H,W,grid,x):
    dist=[[float('inf')]*W for _ in range(H)]
    seen=[[False]*W for _ in range(H)]

    hq=[(0,s)]
    dist[s[0]][s[1]]=0
    seen[s[0]][s[1]]=True
    while hq:
        v=heapq.heappop(hq)[1]

        h=v[0]
        w=v[1]
        seen[h][w]=True
        for h2,w2 in (h-1,w),(h,w+1),(h+1,w),(h,w-1):
            if not (0<=h2<H and 0<=w2<W):
                continue
            
            cost =0
            if grid[h2][w2]=='.' or grid[h2][w2]=='G':
                cost=1
            else:
                cost=x

            if seen[h2][w2]==False and dist[h][w]+cost<dist[h2][w2]:
                dist[h2][w2] = dist[h][w] + cost
                heapq.heappush(hq,(dist[h2][w2],(h2,w2)))
            
        
    return dist[g[0]][g[1]]

l=0
r=10**9

while r-l>1:
    mid = (l+r)//2

    if dijkstra(S,G,H,W,grid,mid)<=T:
        l=mid
    else:
        r=mid

print(l)


