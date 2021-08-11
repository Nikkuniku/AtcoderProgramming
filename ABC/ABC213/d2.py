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
def dfs(pre,crr):
    ans.append(crr)
    for v in edge[crr]:
        if v!=pre:
            dfs(crr,v)
            ans.append(crr)

dfs(1,1)
print(*ans)