import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(1000000)
n=int(input())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    edge[u].append(v)
    edge[v].append(u)

ans=[[0,0] for _ in range(n)]
def dfs1(v,p):
    global r
    cnt=0
    ans[v][0]=r
    for e in edge[v]:
        if e==p:
            continue
        cnt+=1
        dfs1(e,v)
    if cnt==0:
        r+=1
def dfs2(v,p):
    global r
    cnt=0
    for e in edge[v]:
        if e==p:
            continue
        cnt+=1
        dfs2(e,v)
    if cnt==0:
        r+=1
    ans[v][1]=r
r=1
dfs1(0,-1)
r=0
dfs2(0,-1)
for i in range(n):
    print(*ans[i])