h,w=map(int,input().split())
rs,cs=map(int,input().split())
rt,ct=map(int,input().split())
INF = 10**8 + 9

grid=[["#"]*(w+2)]
for _ in range(h):
    g=list(input())
    grid.append(["#"]+g+["#"])

grid.append(["#"]*(w+2))

cost=[[INF]*(w+2) for _ in range(h+2)]
cost[rs][rt]=0
from collections import deque
q=deque()
# ↑
if grid[rs-1][cs]=='.':
    q.append([rs-1,cs,1])
    cost[rs-1][cs]=0
# →
if grid[rs][cs+1]=='.':
    q.append([rs,cs+1,2])    
    cost[rs][cs+1]=0
# ↓
if grid[rs+1][cs]=='.':
    q.append([rs+1,cs,3])
    cost[rs+1][cs]=0
# ←
if grid[rs][cs-1]=='.':
    q.append([rs,cs-1,4])
    cost[rs][cs-1]=0

while q:
    v=q.popleft()
    rv,cv=v[0],v[1]
    dir=v[2]
    # ↑
    if grid[rv-1][cv]=='.' and cost[rv-1][cv]>cost[rv][cv]:
        if dir==1:
            cost[rv-1][cv]=cost[rv][cv]
        else:
            cost[rv-1][cv]=min(cost[rv-1][cv],cost[rv][cv]+1)
        q.append([rv-1,cv,1])
    # →
    if grid[rv][cv+1]=='.' and cost[rv][cv+1]>cost[rv][cv]:
        if dir==2:
            cost[rv][cv+1]=cost[rv][cv]
        else:
            cost[rv][cv+1]=min(cost[rv][cv+1],cost[rv][cv]+1)
        q.append([rv,cv+1,2])
    # ↓
    if grid[rv+1][cv]=='.' and cost[rv+1][cv]>cost[rv][cv]:
        if dir==3:
            cost[rv+1][cv]=cost[rv][cv]
        else:
            cost[rv+1][cv]=min(cost[rv+1][cv],cost[rv][cv]+1)
        q.append([rv+1,cv,3])
    # ←
    if grid[rv][cv-1]=='.' and cost[rv][cv-1]>cost[rv][cv]:
        if dir==4:
            cost[rv][cv-1]=cost[rv][cv]
        else:
            cost[rv][cv-1]=min(cost[rv][cv-1],cost[rv][cv]+1)
        q.append([rv,cv-1,4])

print(cost[rt][ct])
