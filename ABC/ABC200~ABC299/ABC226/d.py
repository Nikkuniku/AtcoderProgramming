n=int(input())
town=[]
for _ in range(n):
    town.append(tuple(map(int,input().split())))

magic=set()
from math import gcd

for i in range(n):
    a,b=town[i]
    for j in range(i+1,n):
        c,d=town[j]

        p=c-a
        q=d-b
        r=a-c
        s=b-d
        g=gcd(p,q)
        magic.add((p//g,q//g))
        magic.add((r//g,s//g))
ans=len(magic)
print(ans)