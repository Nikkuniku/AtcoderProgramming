n=int(input())
a=list(map(int,input().split()))

from itertools import product

pattern= list(product([0,1,2],repeat=n))

cnt=0
for p in pattern:
    ans=1
    for i in range(n):
        if p[i]==0:
            ans*=(a[i]-1) 
        elif p[i]==1:
            ans*=a[i] 
        else:
            ans*=(a[i]+1) 
        
    if ans%2==0:
        cnt+=1

print(cnt)