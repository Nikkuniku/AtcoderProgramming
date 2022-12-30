n=int(input())
a=list(map(int,input().split()))

mod=10**9+7
import numpy as np

cum=[]

prev=0
for i in range(n):
    tmp = prev%mod +a[i]%mod
    cum.append(tmp)
    prev = cum[-1]


ans=0
for i in range(n-1):
    p=a[i]
    t = cum[-1] - cum[i]

    ans+=(p*t)%mod

print(ans%mod)