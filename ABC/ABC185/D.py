n,m=map(int,input().split())

ans=0
if m>0:
    a=list(map(int,input().split()))
    a=sorted(a)
else:
    ans=1

now=0
M=[]
for i in range(m):
    M.append(a[i]-now-1)
    now=a[i]

if len(M)>0:
    M.append(n-now)

B=float('inf')
for i in range(len(M)):
    if M[i]!=0:
        B=min(B,M[i])

import math 


for j in range(len(M)):
    ans+=math.ceil(M[j]/B)

print(ans)

