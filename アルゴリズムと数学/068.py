N,K=map(int,input().split())
V=list(map(int,input().split()))

ans=0

from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

for i in range(1,1<<K):
    k=0
    g=1
    for j in range(K):
        if (i>>j)&1:
            k+=1
            g=lcm(g,V[j])
    
    ans+=((-1)**(k-1))*(N//g)

print(ans)