n=int(input())
a=list(map(int,input().split()))

from collections import deque
d=deque()

ans=0
last=-1
for i in range(n):
    if last==a[i]:
        d[-1][1]+=1
        ans+=1
        if d[-1][1]==a[i]:
            ans-=d[-1][1]
            d.pop()
    else:
        d.append([a[i],1])
        ans+=1
    last=-1
    if d:
        last=d[-1][0]
    print(ans)