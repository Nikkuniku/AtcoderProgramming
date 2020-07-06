s=list(input())
n=len(s)

if n==1:
    print(0)
    exit(0)
from collections import deque

d=deque(s)
i=0
j=1
cnt=0
while d:
    f=d[0]
    l=d[-1]
    if f==l:
        d.popleft()
        if len(d)==0:
            break
        d.pop()
    else:
        if f=='x' and l!='x':
            cnt+=1
            d.popleft()
        elif f!='x' and l=='x':
            cnt+=1
            d.pop()
        else:
            print(-1)
            exit(0)

print(cnt)

