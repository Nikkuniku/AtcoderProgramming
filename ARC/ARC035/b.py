n=int(input())
time=[]
mod= 1000000007
from collections import Counter
from math import factorial
for _ in range(n):
    t=int(input())
    time.append(t)
c=Counter(time)
ans=1
for v in list(c.values()):
    ans*=factorial(v)
    ans%=mod
t=0
time.sort()
for i in range(1,n):
    time[i]+=time[i-1]
for j in range(n):
    t+=time[j]
print(t)
print(ans)
