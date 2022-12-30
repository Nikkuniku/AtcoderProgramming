n=int(input())
a=list(map(int,input().split()))

A=max(a)

def min_factor(k):
    d=[]
    for i in range(k+1):
        d.append(i)

    i=2
    while i*i<=k:
        if d[i]==i:
            j=i*i
            while j<=k:
                if d[j]==j:
                    d[j]=i
                j+=i
        i+=1
    
    return d

def prime_factor_set(p):
    s=set()
    while p!=1:
        s.add(d[p])
        p//=d[p]  
    
    return s


d=min_factor(A)
cur=set()
flg=True
for i in range(n):
    tmp = prime_factor_set(a[i])
    if len(cur&tmp)>=1:
        flg=False
        break
    cur |= tmp

import numpy as np

g= np.gcd.reduce(a)

if flg:
    ans='pairwise coprime'
elif not flg and g==1:
    ans='setwise coprime'
else:
    ans='not coprime'

print(ans)