n=int(input())
k=len(str(n))

from itertools import product

ans=0


for j in range(3,k+1):
    p=list(product([3,5,7],repeat=j)) 

    for c in p:
        if (3 not in c) or (5 not in c) or (7 not in c):
            continue
        
        tmp=''
        for i in c:
            tmp+=str(i)

        if int(tmp)<=n:
            ans+=1

print(ans)  