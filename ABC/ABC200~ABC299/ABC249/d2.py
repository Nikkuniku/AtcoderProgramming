n=int(input())
a=list(map(int,input().split()))
from collections import defaultdict
d=defaultdict(int)
ans=0
for ai in a:
    d[ai]+=1

for ai in a:
    i=1
    while i*i<=ai:
        if ai%i==0:
            if i==ai//i:
                ans+=d[i]*d[i]
            else:
                if i==1:
                    ans+=d[1]*d[ai]
                    ans+=d[ai]*d[1]            
                else:
                    ans+=d[i]*d[ai//i]
                    ans+=d[ai//i]*d[i]     
        i+=1          
print(ans)
        