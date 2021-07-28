n=int(input())
x=list(map(int,input().split()))
m=60
divisor=[-1]*m
from math import gcd
for i in range(2,m):
    j=i
    while j<m:
        if divisor[j]==-1:
            divisor[j]=i
        j+=i 
coprime=[]
prime=[]
for y in x:
    if divisor[y]==y:
        prime.append(y)
    else:
        coprime.append(y)
ans=1
for z in prime:
    ans*=z
        
if len(coprime)>0:
    for j in range(2,51):
        flg=0
        for p in coprime:
            if gcd(p,j)==1:
                flg+=1
                break
        if flg==0:
            break

    q=gcd(ans,j)
    ans*=j//q

print(ans)