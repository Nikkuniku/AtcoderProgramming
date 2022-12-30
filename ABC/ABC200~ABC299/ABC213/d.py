import sys
sys.setrecursionlimit(10**6)
n=int(input())
edge=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(n+1):
    edge[i]=sorted(edge[i])
    
ans=[]
visited=set()
def dfs(u,v):
    if len(visited)==n:
        return
    ans.append(v)
    visited.add(v)

    for e in edge[v]:
        if e in visited:
            continue
        dfs(v,e)
    
    ans.append(u)

dfs(1,1)
print(*ans[:-1])