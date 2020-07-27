n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


c1=0
c2=0

from math import floor
for i in range(n):
    if a[i]>b[i]:
        c1+=a[i]-b[i]
    elif a[i]<b[i]:
        c2+=floor((b[i]-a[i])/2)

if c2>=c1:
    print('Yes')
else:
    print('No')