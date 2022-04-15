n=int(input())
from math import sqrt

ans=10**18
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        ans=min(ans,2*(i + n//i))
print(ans)