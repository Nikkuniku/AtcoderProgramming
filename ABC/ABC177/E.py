n=int(input())
a=list(map(int,input().split()))

from math import gcd

flg=0
ans='pairwise coprime'
for i in range(n-1):
    for j in range(i+1,n-1):
        g=gcd(a[i],a[j])
        if g!=1:
            ans='setwise coprime'
            flg=1
            break

if flg==0:
    print(ans)
    exit(0)

tmp=a[0]
for j in range(1,n):
    tmp=gcd(tmp,a[j])

if tmp==1:
    print(ans)
    exit(0)
else:
    print('not coprime')

