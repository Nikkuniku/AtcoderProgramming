n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a=sorted(a)
b=sorted(b)
c=sorted(c)

import bisect

t=[]

for i in range(n):
    index=bisect.bisect_right(c,b[i])
    t.append(n-index)

cum=[0]
for j in range(n):
    cum.append(cum[-1]+t[j])


ans=0
for k in range(n):
    index=bisect.bisect_right(b,a[k])

    if index==0:
        ans+=cum[-1]
    else:
        ans+=cum[-1]-cum[index]

print(ans)