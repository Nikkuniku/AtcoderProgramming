n=int(input())
a=list(map(int,input().split()))
hope_num=sum(a)/10
a+=a

ans='No'
if len(a)==1:
    print(ans)
    exit()

from collections import deque

q=deque()
total=0
for c in a:
    q.append(c)
    total+=c

    while q and len(q)<=n and total>hope_num:
        rm=q.popleft()
        total-=rm

    if total==hope_num:
        ans='Yes'
        break

print(ans)