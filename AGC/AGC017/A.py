n,p=map(int,input().split())
a=list(map(int,input().split()))

n_odd=0
n_even=0

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


for i in a:
    if i%2==0:
        n_even+=1
    else:
        n_odd+=1

ans=0

if p==0:    
    #p=0
    for j in range(n_odd+1):
        if j%2==1:
            continue
        else:
            tmp=0
            for l in range(n_even+1):
                tmp+=cmb(n_even,l)
            
            ans+=cmb(n_odd,j)*tmp
elif p==1:
    #p=1
    for k in range(n_odd+1):
        if k%2==0:
            continue
        else:
            tmp=0
            for l in range(n_even+1):
                tmp+=cmb(n_even,l)

            ans+=cmb(n_odd,k)*tmp

print(ans)

