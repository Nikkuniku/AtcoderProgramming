n,m=map(int,input().split())
edge=[set() for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    edge[x-1].add(y-1)
    edge[y-1].add(x-1)

from itertools import combinations

ans=1
for i in range(1<<n):
    tmp=0
    can=[]
    for j in range(n):
        if (i>>j)&1:
            can.append(j)
    
    if len(can)<=1:
        continue

    c=list(combinations(can,2))
    for p,q in c:
        if q in edge[p] :
            tmp+=1
    if tmp==len((c)):
        ans=max(ans,len(can))

print(ans)