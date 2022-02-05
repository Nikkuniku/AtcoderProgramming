n=int(input())
a=list(map(int,input().split()))

from collections import defaultdict
d=defaultdict(lambda:0)

for i in range(n):
    d[a[i]]+=1
ans=0
for j in range(1,50001):
    if j==50000:
        p=d[j]
        ans+=p*(p-1)//2
    else:
        p=d[j]
        q=d[100000-j]
        ans+=p*q        
print(ans)