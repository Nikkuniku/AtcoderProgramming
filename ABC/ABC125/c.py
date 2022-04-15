n=int(input())
a=list(map(int,input().split()))

from math import gcd

N=1
while n>N:
    N*=2
node=[0]*(2*N)
def update(k,x):
    k+=N-1
    node[k]=x
    while k>1:
        k//=2
        node[k]=gcd(node[2*k],node[2*k + 1])

for i in range(n):
    update(i+1,a[i])
ans=1

for i in range(n):
    update(i+1,0)
    ans=max(ans,node[1])
    update(i+1,a[i])
print(ans)