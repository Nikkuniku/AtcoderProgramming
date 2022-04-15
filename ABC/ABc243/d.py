n,x=map(int,input().split())
s=input()
from collections import deque

d=deque([])
for i in range(n):
    d.append(s[i])
    if len(d)>1:
        if d[-2]=='L' and d[-1]=='U':
            d.pop()
            d.pop()
        elif d[-2]=='R' and d[-1]=='U':
            d.pop()
            d.pop()

ans=x
for j in range(len(d)):
    if d[j]=='L':
        ans*=2
    elif d[j]=='R':
        ans*=2
        ans+=1
    elif d[j]=='U':
        ans//=2
print(ans)