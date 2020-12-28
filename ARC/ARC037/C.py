n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a=sorted(a)
b=sorted(b)

c=max(a)*max(b)

l=0
r=c

import bisect

while r-l>1:
    x=(l+r)//2

    cnt=0
    for i in range(n):
        q=x//a[i]

        j=bisect.bisect_right(b,q)


        cnt+=j

    if cnt>=k:
        r=x
    elif cnt<k:
        l=x

print(r)




