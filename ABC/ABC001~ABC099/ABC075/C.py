n,m=map(int,input().split())

E=[]
for _ in range(m):
    E.append(list(map(int,input().split())))

from collections import deque

def bridge_serach(num):
    global E
    edge=[[] for _ in range(n)]
    for i in range(m):
        if i==num:
            continue
        a,b=E[i][0]-1,E[i][1]-1
        
        edge[a].append(b)
        edge[b].append(a)

    d=deque([0])
    dist=[-1]*n
    dist[0]=0
    while d:
        v=d.popleft()

        for e in edge[v]:
            if dist[e]==-1:
                dist[e]=dist[v]+1
                d.append(e)

    # 非連結であればtrue
    if  -1 in set(dist):
        return True
    else:
        return False

ans=0
for k in range(m):
    if bridge_serach(k):
        ans+=1

print(ans)

    


    
