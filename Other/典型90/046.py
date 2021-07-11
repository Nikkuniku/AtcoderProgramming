n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
mod=46
for i in range(n):
    a[i] = a[i]%mod
    b[i] = b[i]%mod
    c[i] = c[i]%mod

from collections import Counter
ca =Counter(a)
cb =Counter(b)
cc =Counter(c)

a=list(ca.keys())
b=list(cb.keys())
c=list(cc.keys())

ans=0
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            p = a[i]+b[j]+c[k]

            if p%mod==0:
                ans+=ca[a[i]]*cb[b[j]]*cc[c[k]]

print(ans)