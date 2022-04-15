n=int(input())
a=list(map(int,input().split()))
from collections import deque
d=deque(a)
isnormal=True

ans='Yes'
while d:
    if (isnormal and d[-1]==0) or (not isnormal and d[-1]==1):
        d.pop()
    elif (isnormal and d[0]==0) or (not isnormal and d[0]==1):
        d.popleft()
        isnormal = not isnormal
    else:
        ans='No'
        break

print(ans)