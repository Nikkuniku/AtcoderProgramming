n=int(input())
mod=10**9 + 7
import math
from collections import Counter
#試し割法
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

ans=[]
for i in range(1,n+1):
    arr=factorize(i)

    ans.append(arr)

ans=sum(ans,[])

c=list(Counter(ans).values())
cnt=1
for j in c:
    cnt*=(j+1)

print(cnt%mod)