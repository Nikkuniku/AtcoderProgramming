import sys
sys.setrecursionlimit(10**6)

n,q=map(int,input().split())
x=list(map(int,input().split()))
values=[[] for _ in range(n)]
k=20
    
edge=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)
def dfs(v,p):
    for e in edge[v]:
        if e==p:
            continue
        dfs(e,v)
    values[v].append(x[v])
    for e in edge[v]:
        if e==p:
            continue
        values[v].extend(values[e])
    values[v].sort(reverse=True)
    values[v]=values[v][:k]

dfs(0,-1)
answer=[]
for _ in range(q):
    v,k=map(int,input().split())
    v-=1
    ans=values[v][k-1]
    answer.append(ans)
print(*answer,sep="\n")