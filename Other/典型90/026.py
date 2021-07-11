import sys
sys.setrecursionlimit(10**7)

n=int(input())
edge=[[]for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)
colors=[0]*n

def dfs(v,color):
    colors[v]=color

    for to in edge[v]:
        if colors[to]==color:
            return False
        
        if colors[to]==0 and not dfs(to,-color):
            return False
    
    return True

def is_bipartite(v):
    return dfs(v,1)

from collections import deque

q=deque([0])
dist=[-1]*n
dist[0]=0

while q:
    v=q.popleft()

    for e in edge[v]:
        if dist[e]==-1:
            dist[e] = dist[v]+1
            q.append(e)

v = dist.index(max(dist))

is_bipartite(v)
c_1 = colors.count(1)
c_2 = colors.count(-1)

ans=[]
c=1
if c_1<c_2:
    c=-1

for i in range(n):
    if colors[i]==c:
        ans.append(i+1)
        if len(ans)==n//2:
            break

print(*ans)