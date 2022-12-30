n,q=map(int,input().split())
tree=[0]*n
edge=[[] for _ in range(n)]
visited=[0]*n
visited[0]=1

import sys #追加
sys.setrecursionlimit(1000*1000)

for _ in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

for _ in range(q):
    p,x=map(int,input().split())
    tree[p-1]+=x

def rec(e,cost):
    global tree
    global visited
    cnt=0
    for r in edge[e]:
        if visited[r]==0:
            cnt+=1
            tree[r]+=cost
            visited[r]=1
            rec(r,tree[r])

    if cnt==0:
        return

rec(0,tree[0])

print(*tree)