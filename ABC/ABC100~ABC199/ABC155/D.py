n,k=map(int,input().split())
a=list(map(int,input().split()))

nega=[]
zeros=[]
pos=[]

a=sorted(a)

for i in range(n):
    if a[i]<0:
        nega.append(a[i])
    elif a[i]>0:
        pos.append(a[i])
    else:
        zeros.append(a[i])

        
l=-min(a)**2
r=max(a)**2

x=l+(r-l)//2

import bisect
while r-l>1:
    x=l+(r-l)//2
    cnt=0
    for i in range(n):
        p=x//a[i]
        j=bisect.bisect_right(a,p)

        cnt+=j
    
    if cnt>=k:
        r=x
    else:
        l=x

print(r)
