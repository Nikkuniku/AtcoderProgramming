n,x=map(int,input().split())
from itertools import product
balls=[]
for _ in range(n):
    l=list(map(int,input().split()))[1:]
    balls.append(l)

p=list(product(*balls))

ans=0
for c in p:
    tmp=1
    for y in c:
        tmp*=y
    
    if tmp==x:
        ans+=1

print(ans)