import sys
sys.setrecursionlimit(10 ** 9)
n=int(input())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)

has=[0]*n
visited=[False]*n
def dfs(v):
    visited[v]=True
    has[v]=1
    for e in edge[v]:
        if not visited[e]:
            dfs(e)
            has[v]+=has[e]

dfs(0)
ans=0
for i in range(1,n):
    ans+=has[i]*(n-has[i])
print(ans)
