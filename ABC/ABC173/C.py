h,w,k=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(input()))

from itertools import product

Raw=list(product([0,1],repeat=h))
Column=list(product([0,1],repeat=w))

ans=0
for r in Raw:

    tmp=[]
    for i in range(len(r)):
        if r[i]==1:
            tmp.append(grid[i])
        
    if len(tmp)==0:
        continue

    for c in Column:
        cnt=0

        n=len(tmp)
        for l in range(n):
            for j in range(len(c)):
                if c[j]==1 and tmp[l][j]=='#':
                    cnt+=1
        if cnt==k:
            ans+=1

print(ans)            


        


