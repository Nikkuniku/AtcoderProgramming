import sys #追加
sys.setrecursionlimit(500*500)

n,q=map(int,input().split())

cost=[0]*n
edge = [[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

for _ in range(q):
    p,x=map(int,input().split())
    cost[p-1]+=x


visited=[-1]*n


def dfs(n,c):

    cost[n]+=c
    tmp=cost[n]
    visited[n]=0

    for v in edge[n]:
        if visited[v]==-1:
            dfs(v,tmp)
    

dfs(0,0)

print(*cost)